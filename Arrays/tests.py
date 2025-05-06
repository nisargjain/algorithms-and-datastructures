from array_seq import Array_Seq

X = Array_Seq()
X.build([2,3,4])
X.printseq()
X.insert_at(2, 5)
X.printseq()
X.delete_at(1)
X.printseq()