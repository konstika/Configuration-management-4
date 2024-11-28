import sys
import xml.etree.ElementTree as ET

def to_bytes(n):
    res=""
    for i in range(0, len(n)-1, 2):
        res+="0x"+n[i]+n[i+1]+" "
    return res
if(len(sys.argv)>1):
    inputfile = open(sys.argv[1])
    log = open(sys.argv[2], "w")
    outputfile = open(sys.argv[3] , "w")
else:
    inputfile = open("test.txt")
    log = open("log.xml", "w")
    outputfile = open("data.bin" , "w")
result = ""
root = ET.Element("log")
for line in inputfile:
    opers = (line.replace("\n","")).split()
    command = ET.SubElement(root, "command")
    res=""
    if(opers[0]=="LOAD_CONST"):#Загрузка константы
        a = (format(26, '05b'))
        b = (format(int(opers[1]), '019b'))
        c = (format(int(opers[2]), '026b'))
        dop = (format(0, '06b'))
        res += to_bytes(str(format(int(a+b+c+dop, 2),'014x')))
        ET.SubElement(command, "a").text = "26"
        ET.SubElement(command, "b").text = opers[1]
        ET.SubElement(command, "c").text = opers[2]
        ET.SubElement(command, "bin").text = res[:-1]
    elif(opers[0]=="READ"):#Чтение значения из памяти
        a = (format(4, '05b'))
        b = (format(int(opers[1]), '026b'))
        c = (format(int(opers[2]), '026b'))
        d = (format(int(opers[3]), '014b'))
        dop = (format(0, '01b'))
        res += to_bytes(str(format(int(a+b+c+d+dop, 2),'018x')))
        ET.SubElement(command, "a").text = "4"
        ET.SubElement(command, "b").text = opers[1]
        ET.SubElement(command, "c").text = opers[2]
        ET.SubElement(command, "d").text = opers[3]
        ET.SubElement(command, "bin").text = res[:-1]
    elif(opers[0]=="WRITE"):#Запись значения в память
        a = (format(27, '05b'))
        b = (format(int(opers[1]), '026b'))
        c = (format(int(opers[2]), '026b'))
        dop = (format(0, '07b'))
        res += to_bytes(str(format(int(a+b+c+dop, 2),'016x')))
        ET.SubElement(command, "a").text = "27"
        ET.SubElement(command, "b").text = opers[1]
        ET.SubElement(command, "c").text = opers[2]
        ET.SubElement(command, "bin").text = res[:-1]
    elif(opers[0]=="CYCLIC_SHIFT_TO_RIGHT"):#побитовый циклический сдвиг вправо
        a = (format(10, '05b'))
        b = (format(int(opers[1]), '026b'))
        c = (format(int(opers[2]), '026b'))
        d = (format(int(opers[3]), '026b'))
        e = (format(int(opers[4]), '014b'))
        dop = (format(0, '07b'))
        res += to_bytes(str(format(int(a+b+c+d+e+dop, 2),'026x')))
        ET.SubElement(command, "a").text = "10"
        ET.SubElement(command, "b").text = opers[1]
        ET.SubElement(command, "c").text = opers[2]
        ET.SubElement(command, "d").text = opers[3]
        ET.SubElement(command, "e").text = opers[4]
        ET.SubElement(command, "bin").text = res[:-1]
    else:
        print("error")
    result+=res
    
result = result[:-1]
inputfile.close()
log.write(ET.tostring(root, encoding='unicode'))
log.close()
outputfile.write(result)
outputfile.close()
