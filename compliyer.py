import sys
import os
out=[]
#print(sys.argv)
if 2<=len(sys.argv):
    try:
        t=open(sys.argv[1])
    except:

        print("not a file")
        quit()
    t.close()
else:
    print("no file specified")
    quit()

linenumbers=False
numbersout=False
debug=False
if len(sys.argv)>=2:
    for i in range(2,len(sys.argv)):
        if sys.argv[i]=="-ln":
            linenumbers=True
        if sys.argv[i]=="-no":
            numbersout=True
        if sys.argv[i]=="-de":
            debug=True


def htob(hex):
    return (bin(int(hex, 16))[2:].zfill(8))
    "{0:08b}".format(int(hex, 16))
print(htob("00"))

f = open(sys.argv[1])
intr = ["data", "goto", "out", "adda", "addb", "addo", "wait", "reg1", "rego1", "reg2", "rego2"]
asin = ["00000000", "00000001", "00000010", "00000011", "00000100", "00000101", "00000000", "00000110", "00000111",
        "00001000", "00001001"]
labels={}
data = f.read().split("\n")
i=1
count=0
for lines in data:
    print(lines)
    if lines == "":
        0
    elif lines[0] == "#":
        0
    elif lines.split(" ")[0]=="label":
        labels[lines.split(" ")[1]]=i
        out.append("00000000")
        out.append("00000000")
        print(labels)
        i += 1
        count += 1
    elif lines.split(" ")[0] == "jmp":

        out.append("00000001")
        out.append('{0:08b}'.format(labels[lines.split(" ")[1]]))
        i += 1
        count += 1
    else:
        l = lines.split(" ")

        if len(l) == 1:
            l.append("00")
        if debug:
            print(l)

        if len(l[1]) == 2:
            if numbersout:
                print(i, asin[intr.index(l[0])], htob(l[1]))
                out.append(asin[intr.index(l[0])])
                out.append(htob(l[1]))

            else:
                print(asin[intr.index(l[0])], htob(l[1]))
                out.append(asin[intr.index(l[0])])
                out.append(htob(l[1]))

        else:
            if numbersout:
                print(i, asin[intr.index(l[0])], l[1])
                out.append(asin[intr.index(l[0])])
                out.append(l[1])

            else:
                print(asin[intr.index(l[0])], l[1])
                out.append(asin[intr.index(l[0])])
                out.append(l[1])

        i+=1
        count+=1
"""for i in range(len(out)):
    out[i]=out[i]+b" """
def split(word):
    return [char for char in word]
out.append("10000001")
out.append("00000000")
count+=1

print(out)
f.close()
f=open("out.bin","w")
f.writelines(out)
f.close()
f=open("out.py","w")
o=[]
for i in range(0,count):
    o.append(list(reversed(split(out[2*i])))+list(reversed(split(out[2*i+1]))))
f.writelines([f"c = {str(o)}"])