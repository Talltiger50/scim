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
    return (bin(int(hex, 16))[2:].zfill(8)).encode()



f = open(sys.argv[1])
intr = ["db", "jmp", "out", "adda", "addb", "addo", "wait", "regA", "regoA", "regB", "regoB","regoB"]
asin = [b"00000000", b"00000001", b"00000010", b"00000011", b"00000100", b"00000101", b"00000000", b"00000110", b"00000111",
        b"00001000", b"00001001"]
data = f.read().split("\n")
i=1

for lines in data:
    if lines == "":
        0
    elif lines[0] == "#":
        0

    else:
        if linenumbers:
            l = lines.split(" ")

            if len(l) == 2:
                l.append("00")
            if debug:
                print(l)
            if len(l[2]) == 3:
                if numbersout:
                    print(i,asin[intr.index(l[1])], htob(l[2]))
                    out.append(asin[intr.index(l[1])])
                    out.append(htob(l[2]))

                else:
                    print(asin[intr.index(l[1])], htob(l[2]))
                    out.append(asin[intr.index(l[1])])
                    out.append(htob(l[2]))
            else:
                if numbersout:
                    print(i,asin[intr.index(l[1])], l[2])
                    out.append(asin[intr.index(l[1])])
                    out.append(l[2])
                else:
                    print(asin[intr.index(l[1])], l[2])
                    out.append(asin[intr.index(l[1])])
                    out.append(l[2])
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
"""for i in range(len(out)):
    out[i]=out[i]+b" """
print(out)
f.close()
f=open("out.bin","wb")
f.writelines(out)
f.close()