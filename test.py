import subprocess
import filecmp
mytest = open("mytest.txt","w+")
inputdata = """LOAD_CONST 1 0
LOAD_CONST 2 1
LOAD_CONST 3 2
LOAD_CONST 4 3
LOAD_CONST 5 4
LOAD_CONST 6 5
LOAD_CONST 7 6
LOAD_CONST 1 7
LOAD_CONST 1 8
LOAD_CONST 1 9
LOAD_CONST 1 10
LOAD_CONST 1 11
LOAD_CONST 1 12
LOAD_CONST 1 13
CYCLIC_SHIFT_TO_RIGHT 7 0 14 0
CYCLIC_SHIFT_TO_RIGHT 8 1 14 1
CYCLIC_SHIFT_TO_RIGHT 9 2 14 2
CYCLIC_SHIFT_TO_RIGHT 10 3 14 3
CYCLIC_SHIFT_TO_RIGHT 11 4 14 4
CYCLIC_SHIFT_TO_RIGHT 12 5 14 5
CYCLIC_SHIFT_TO_RIGHT 13 6 14 6
WRITE 21 14
WRITE 22 15
WRITE 23 16
WRITE 24 17
WRITE 25 18
WRITE 26 19
WRITE 27 20
READ 20 1 28
READ 20 2 29
READ 20 3 30
READ 20 4 31
READ 20 5 32
READ 20 6 33
READ 20 7 34
"""
mytest.write(inputdata)
mylog = open("mylog.txt","w+")
mydata = open("mydata.txt","w+")
mytest.close()
mylog.close()
mydata.close()
subprocess.run(['python', 'assembler.py', 'mytest.txt', 'mylog.xml', 'mydata.bin'])

result1 = filecmp.cmp("mylog.xml", "testlog_expected.xml", shallow=False)
result2 = filecmp.cmp("mydata.bin", "testdata_expected.bin", shallow=False)
if(result1 and result2):
    print("Test assembler successfully completed")
else:
    print("Test assembler failed")
myresult = open("myresult.xml","w+")
myresult.close()
subprocess.run(['python', 'interpreter.py', 'testdata_expected.bin', 'myresult.xml', '0-34'])
result3 = filecmp.cmp("myresult.xml", "testresult_expected.xml", shallow=False)
if(result3):
    print("Test interpreter successfully completed")
else:
    print("Test interpreter failed")



