import sys
import xml.etree.ElementTree as ET
if(len(sys.argv)>1):
    inputfile = open(sys.argv[1])
    outputfile = open(sys.argv[2], "w")
    diap = sys.argv[3]
else:
    inputfile = open("data.bin")
    outputfile = open("result.xml", "w")
    diap = "0-34"
data = (inputfile.read()).split()
i = 0
memory = [-1]*10000
while(i<len(data)):
    a = int(format(int(data[i],16), "08b")[0:5],2)
    shift = 0
    bindata=""
    if(a==26):#Загрузка константы
        for j in range(0, 7):
            bindata+=format(int(data[i+j],16), "08b")
            shift = j
        b = int(bindata[5:24],2)#константа
        c = int(bindata[24:50],2)#адрес
        memory[c]=b
    elif(a==4):#Чтение значения из памяти
        for j in range(0, 9):
            bindata+=format(int(data[i+j],16), "08b")
            shift = j
        b = int(bindata[5:31],2)#адрес
        c = int(bindata[31:57],2)#смещение
        d = int(bindata[57:71],2)#новый адрес
        memory[d] = memory[b+c]
    elif(a==27):#Запись значение в память
        for j in range(0, 8):
            bindata+=format(int(data[i+j],16), "08b")
            shift = j
        b = int(bindata[5:31],2)#новый адрес
        c = int(bindata[31:57],2)#адрес
        memory[b]=memory[c]
    elif(a==10):
        for j in range(0, 13):
            bindata+=format(int(data[i+j],16), "08b")
            shift = j
        b = int(bindata[5:31],2)#адрес второго операнда
        c = int(bindata[31:57],2)#адрес первого операнда
        d = int(bindata[57:83],2)#адрес
        e = int(bindata[83:97],2)#смещение
        memory[d+e]=memory[c] >> memory[b]
    else:
        print("error")
        break
    i+=shift+1
root = ET.Element("memory")
a = int(diap.split("-")[0])
b = int(diap.split("-")[1])
for i in range(a, b+1):
    ET.SubElement(root, "registr_"+str(i)).text = str(memory[i])
outputfile.write(ET.tostring(root, encoding='unicode'))
inputfile.close()
outputfile.close()
