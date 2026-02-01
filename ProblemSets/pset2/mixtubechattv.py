import unittest

class MessageNode:
    def __init__(self, viewer, msg):
        self.viewer = viewer
        self.msg = msg
        self.prev = None
        self.next = None

class ViewerMessageList:

    def __init__(self):
        self.head = None

    def add(self, msg_node):
        node  = {"msg": msg_node, "next": self.head}
        self.head = node

    def iterate(self):
        cur = self.head
        while cur:
            yield cur["msg"]
            cur = cur["next"]

class ChatDB:
    def __init__(self):
        self.viewers = []
        self.head = None
        self.tail = None

    def build(self, V):
        self.viewers = []
        self.head = None
        self.tail = None

        if len(V) > 0:
            for v in V:
                self.viewers.append((v, ViewerMessageList()))
            self.mergesort(self.viewers, 0, len(self.viewers) -1)

    def mergesort(self, A, i , j): 
        if i < j:
            m = (i+j)//2
            self.mergesort(A, i, m)
            self.mergesort(A, m+1, j)
            L = A[i:m+1]
            R = A[m+1:j+1]
            self.merge(A, L , R, i , j , m)
    
    def merge(self, A, L, R, i, j, m):
        k = i
        l = 0
        r = 0
        while((l < m+1-i) and (r < j-m) ):
            if(L[l][0] <= R[r][0]):
                A[k] = L[l]
                k += 1
                l += 1
            else:
                A[k] = R[r]
                k += 1
                r += 1
        if( l == m+1-i):
            while(r<j-m):
                A[k] = R[r]
                k += 1
                r += 1
        else:
            while(l< m+1 -i):
                A[k] = L[l]
                k += 1
                l += 1
    
    def _find_viewer(self, v):
        left = 0
        right = len(self.viewers) -1
        while left <= right:
            mid = (left+right)//2
            mid_v = self.viewers[mid][0]
            if mid_v == v:
                return mid
            elif mid_v < v:
                left  = mid+1
            else: right = mid-1
        return None
    
    def send(self,v,m):
        idx = self._find_viewer(v)
        if idx is None:
            return
        viewerid, viewerlist = self.viewers[idx]
        if viewerlist is None:
            return
        node = MessageNode(v, m)
        ## adding to chat
        node.next = self.head
        if self.head:
            self.head.prev = node
        else: self.tail = node
        self.head = node
        ## adding to viewer list
        viewerlist.add(node)

    def recent(self,k):
        out = []
        cur =self.head
        while cur and k>0:
            out.append((cur.viewer,cur.msg))
            cur = cur.next
            k -= 1
        return out
    
    def _remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def ban(self, v):
        idx = self._find_viewer(v)
        if idx is None:
            return
        viewer, lv = self.viewers[idx]
        if lv is None: ## already banned
            return
        for msg_node in lv.iterate():
            self._remove_node(msg_node)

        self.viewers[idx] = (viewer, None)



# ===================== TESTS =====================


class TestMixBookTubeChat(unittest.TestCase):

    def setUp(self):
        self.chat = ChatDB()
        self.chat.build([10, 5, 20])

    def test_initial_recent_empty(self):
        self.assertEqual(self.chat.recent(5), [])

    def test_send_and_recent(self):
        self.chat.send(10, "hello")
        self.chat.send(5, "yo")
        self.chat.send(10, "again")

        self.assertEqual(
            self.chat.recent(3),
            [(10, "again"), (5, "yo"), (10, "hello")]
        )

    def test_recent_k_smaller(self):
        self.chat.send(10, "a")
        self.chat.send(5, "b")
        self.chat.send(20, "c")

        self.assertEqual(
            self.chat.recent(2),
            [(20, "c"), (5, "b")]
        )

    def test_ban_removes_messages(self):
        self.chat.send(10, "a")
        self.chat.send(5, "b")
        self.chat.send(10, "c")
        self.chat.send(20, "d")

        self.chat.ban(10)

        self.assertEqual(
            self.chat.recent(10),
            [(20, "d"), (5, "b")]
        )

    def test_send_after_ban(self):
        self.chat.send(10, "x")
        self.chat.ban(10)
        self.chat.send(10, "y")

        self.assertEqual(self.chat.recent(5), [])

    def test_ban_twice_safe(self):
        self.chat.send(5, "m1")
        self.chat.ban(5)
        self.chat.ban(5)

        self.assertEqual(self.chat.recent(5), [])

    def test_multiple_users_ban_one(self):
        self.chat.send(10, "a")
        self.chat.send(5, "b")
        self.chat.send(20, "c")
        self.chat.send(5, "d")

        self.chat.ban(5)

        self.assertEqual(
            self.chat.recent(10),
            [(20, "c"), (10, "a")]
        )

    def test_ban_nonexistent(self):
        self.chat.send(10, "hi")
        self.chat.ban(999)

        self.assertEqual(self.chat.recent(5), [(10, "hi")])

    def test_build_resets_state(self):
        self.chat.send(10, "x")

        self.chat.build([1, 2])

        self.assertEqual(self.chat.recent(5), [])
        self.chat.send(1, "new")

        self.assertEqual(self.chat.recent(5), [(1, "new")])


if __name__ == "__main__":
    unittest.main()

