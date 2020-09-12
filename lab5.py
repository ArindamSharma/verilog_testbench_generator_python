import os
from random import random
def hello(x,str1,i):
    p=[]
    while(i<len(x)):
        # x[i]=x[i].split("//")[0].split("\n")[0].strip("\t").strip(" ")
        if(x[i].find(str1+" ")!=-1):
            c=0
            while(True):
                # print(i)
                x[i]=x[i].split("//")[0].split("\n")[0].strip("\t").strip(" ")
                if(x[i].find(";")!=-1):
                    p.append(x[i])
                    i+=1
                    c+=1
                    break
                else:
                    p.append(x[i])
                    i+=1
            if(c>0):
                break
        i+=1
    sr=""
    # print(p[0])
    for i in range(len(p)):
        sr=sr+p[i].strip(" ").strip("\t")
    # print(sr,i)
    return sr
# -------------------------------------------------------------------
# os.system("cls")
os.system("clear")
a=input("Enter the file name :-")
# a="fourbitadder"
try:
    file1=open(a+".v","r")
except (FileNotFoundError,KeyboardInterrupt):
    print("No such Verilog File exist with name '"+a+"'")
    exit(0)

glob=input("Do you want Manual Entries or Default Entries (1 or 0 respictively):-")

file2=open(a+"_tb.v","w")
f1=(file1.readlines())
file1.close()
b="`include \""+a+".v\"\n\n"+"module top;\n"
file2.write(b)
# print(f1)
module=""
list1=[]
o1=[]
o2=[]
i1=[]
i2=[]
i=0
sr=""
while(i<len(f1)-1):
    # print(i)
    f1[i]=f1[i].split("//")[0].split("\n")[0].strip("\t").strip(" ")
    # print(f1[i])
    if(f1[i].find("module ")!=-1):
        sr=hello(f1,"module",i)
        # print(sr)
        module=sr.split("module")[1].split("(")[0].strip(" ")
        list1=sr.split("(")[1].split(")")[0].split(",")
        print(list1)
    elif(f1[i].find("input ")!=-1):
        sr=hello(f1,"input",i)
        print(sr)
        if(sr.find("[")!=-1):
            for v in sr.split("]")[1].split(";")[0].split(","):
                i2.append([v.strip("\t").strip(" "),((int(sr.split("[")[1].split("]")[0].split(":")[0])+1))])
        else:
            for g in sr.split("input ")[1].split(";")[0].split(","):
                i1.append(g.strip("\t").strip(" "))
    elif(f1[i].find("output ")!=-1):
        sr=hello(f1,"output",i)
        print(sr)
        if(sr.find("[")!=-1):
            for v in sr.split("]")[1].split(";")[0].split(","):
                o2.append([v.strip("\t").strip(" "),((int(sr.split("[")[1].split("]")[0].split(":")[0])+1))])
        else:
            for g in sr.split("output ")[1].split(";")[0].split(","):
                o1.append(g.strip("\t").strip(" "))
    i+=1

# print(list1,"\n")

# i=0
# while(i<len(f1)):
#     if(sr.find("input")!=-1):
#         if(sr.find("[")!=-1):
#             for v in sr.split("]")[1].split(";")[0].split(","):
#                 i2.append([v,((int(sr.split("[")[1].split("]")[0].split(":")[0])+1))])
#         else:
#             count=i

#             if(len(sr.split("input ")[1].split(";")[0])>1):
#                 for g in sr.split("input ")[1].split(";")[0].split(","):
#                     i1.append(g)
#             else:
#                 i1.append(sr.split("input ")[1].split(";")[0])
#     i+=1
# i=0
# while(i<len(f1)):
#     if(sr.find("output")!=-1):
#         if(sr.find("[")!=-1):
#             for v in sr.split("]")[1].split(";")[0].split(","):
#                 o2.append([v,((int(sr.split("[")[1].split("]")[0].split(":")[0])+1))])
#         else:
#             if(len(sr.split("output ")[1].split(";")[0])>1):
#                 for g in sr.split("output ")[1].split(";")[0].split(","):
#                     o1.append(g)
#             else:
#                 o1.append(sr.split("output ")[1].split(";")[0])
#     i+=1

# ----------------------------------------------------------
print(list1,"\n\n",i1,"\n",i2,"\n",o1,"\n",o2,"\n\n")
# i1=[value for value in i1 if value in list1]
i=0
while(i<len(i1)):
    c=0
    for j in list1:
        if(j.strip(" ")==i1[i]):
            c=c+1
    if(c==0):
        i1.remove(i1[i])
        i=-1
    i+=1
i=0
while(i<len(i2)):
    c=0
    for j in list1:
        if(j.strip(" ")==i2[i][0]):
            c=c+1
    if(c==0):
        i2.remove(i2[i])
        i=-1
    i+=1

i=0
while(i<len(o1)):
    c=0
    for j in list1:
        if(j.strip(" ")==o1[i]):
            c=c+1
    if(c==0):
        o1.remove(o1[i])
        i=-1
    i+=1
i=0
while(i<len(o2)):
    c=0
    for j in list1:
        if(j.strip(" ")==o2[i][0]):
            c=c+1
    if(c==0):
        o2.remove(o2[i])
        i=-1
    i+=1
# ---------------------------------------------------------------------------------    
# print(i1,"\n",i2,"\n",o1,"\n",o2)
if(len(i1)!=0):
    file2.write("\nreg ")
    for i in range(len(i1)):
        if(i==len(i1)-1):
            file2.write(i1[i]+";")
        else:
            file2.write(i1[i]+",")
if(len(o1)!=0):
    file2.write("\nwire ")
    for i in range(len(o1)):
        if(i==len(o1)-1):
            file2.write(o1[i]+";")
        else:
            file2.write(o1[i]+",")
if(len(i2)!=0):
    for i in i2:
        file2.write("\nreg ["+str(int(i[1])-1)+":0]"+i[0]+";")
if(len(o2)!=0):
    for i in o2:
        file2.write("\nwire ["+str(int(i[1])-1)+":0]"+i[0]+";")
file2.write("\n")

file2.write("\ninteger ")
for i in range(len(i1)+len(i2)):
    if(i==len(i1)+len(i2)-1):
        file2.write("n"+str(i))
    else:
        file2.write("n"+str(i)+",")
file2.write(";\n")

file2.write("\n\t"+module+" FA_")
file2.write(str(int(random()*100)))
file2.write("(")
for i in range(len(list1)):
    if(i==len(list1)-1):
        file2.write(list1[i])
    else:
        file2.write(list1[i]+",")
file2.write(");\n")
#--------------------
sum1=0
file2.write("\ninitial\n")
# file2.write("\nalways")
file2.write("\nbegin\n")

if(glob=="1"):
    print("Total "+str(len(i1)+len(i2))+" Variables Found Input Verilog File ")

for i in range(len(i1)+len(i2)):
    if(i!=0):
        for j in range(i):
            file2.write("\t")
    if(i<len(i1)):
        h=2
        if(glob=="1"):
            chan=input(str(i+1)+"th Found Variable "+i1[i]+" with range 0-"+str(h-1)+" Do you want changes (l-h):-")
            if(len(chan)==0):
                sum1+=h
                file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
            else:
                try:
                    if(0<=int(chan.split("-")[0])<2 and 0<=int(chan.split("-")[1])<2):
                        sum1+=int(chan.split("-")[1])-int(chan.split("-")[0])+1
                        file2.write("\tfor( n"+str(i)+" = "+chan.split("-")[0]+" ;n"+str(i)+" < "+str(int(chan.split("-")[1])+1)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
                    else:
                        print("Wrong Input Default Taken")
                        sum1+=h
                        file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
                except (IndexError,ValueError):
                    print("Wrong Input Default Taken")
                    sum1+=h
                    file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
        else:
            sum1+=h
            file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )

    else:
        power=(i2[i-len(i1)][1])
        h=2**power
        if(glob=="1"):
            # print("Found Input Variable "+i2[i-len(i1)][0]+" with range 0-"+str(2**(i2[i-len(i1)][1])-1)+" ")
            chan=input(str(i+1)+"th Found Input Variable "+i2[i-len(i1)][0]+" with range 0-2^"+str(power)+"("+str(h-1)+") Do you want changes (l-h):-")
            if(len(chan)==0):
                sum1+=h
                file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
            else:
                try:
                    if(0<=int(chan.split("-")[0])<=h and 0<=int(chan.split("-")[1])<=h):
                        sum1+=int(chan.split("-")[1])-int(chan.split("-")[0])+1
                        file2.write("\tfor( n"+str(i)+" = "+chan.split("-")[0]+" ;n"+str(i)+" < "+str(int(chan.split("-")[1])+1)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
                    else:
                        print("Wrong Input Default Taken")
                        sum1+=h
                        file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
                except (IndexError,ValueError):
                    print("Wrong Input Default Taken")
                    sum1+=h
                    file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )
        else:
            sum1+=h
            file2.write("\tfor( n"+str(i)+" = 0 ;n"+str(i)+" < "+str(h)+" ; n"+str(i)+" = n"+str(i)+"+1)\n" )

    if(i!=0):
        for j in range(i):
            file2.write("\t")
    file2.write("\tbegin\n")

for i in range(len(i1)+len(i2)):
    for j in range(len(i1)+len(i2)+1):
        file2.write("\t")
    if(i<len(i1)):
        file2.write(str(i1[i])+"="+"n"+str(i)+";\n")
    else:
        file2.write((i2[i-len(i1)][0])+"= n"+str(i)+";\n")

for i in range(len(i1)+len(i2)+1):
    file2.write("\t")
file2.write("#10 ;\n")

for i in range(len(i1)+len(i2),0,-1):
    for j in range(i-1):
        file2.write("\t")
    file2.write("\tend\n")

file2.write("end\n")
#------------------------------------------------------------------------------
# print(sum1)
if(glob=="1"):
    choice=input("Your Output has 2^"+str(sum1)+" Combinations Do you want to set limit :-")
    try:
        int(choice)
    except ValueError:
        print("Default Value Taken")
        choice=''
else:
    choice=''

pre=""
if(glob=="1"):
    pree=input("Output will be in Decimal or Binary (1-0 recpectively):-")
    if(pree=="1"):
        pre="d"
    else:
        pre="b"
else:
    pre="b"
#--------------------------------------------------------------------
file2.write("\ninitial\nbegin")
file2.write("\n\t$monitor($time,\" ")
if(len(i1)!=0):
    for i in range(len(i1)):
        if(i==0):
            file2.write("  "+i1[i]+" = %"+pre+",")
        else:
            file2.write(i1[i]+" = %"+pre+",")
if(len(i2)!=0):
    for i in range(len(i2)):
        file2.write(i2[i][0]+" = %"+pre+", ")
if(len(o1)!=0):
    for i in range(len(o1)):
        file2.write(o1[i]+" = %"+pre+", ")
if(len(o2)!=0):
    for i in range(len(o2)):
        if(i==len(o2)-1):
            file2.write(o2[i][0]+" = %"+pre)
        else:
            file2.write(o2[i][0]+" = %"+pre+",")
file2.write("\",")
if(len(i1)!=0):
    for i in range(len(i1)):
        file2.write(i1[i]+",")
if(len(i2)!=0):
    for i in range(len(i2)):
        file2.write(i2[i][0]+",")
if(len(o1)!=0):
    for i in range(len(o1)):
        file2.write(o1[i]+",")
if(len(o2)!=0):
    for i in range(len(o2)):
        if(i==len(o2)-1):
            file2.write(o2[i][0])
        else:
            file2.write(o2[i][0]+",")
file2.write(");\n")
if(glob=="1"):
	ch=input("Do you want to create vcd file (yes or no):-")
	yes="Yes"
	if(ch.upper()==yes.upper()):
		file2.write("\t$dumpfile(\""+a+".vcd\");\n")
		file2.write("\t$dumpvars;\n")
else:
	file2.write("\t$dumpfile(\""+a+".vcd\");\n")
	file2.write("\t$dumpvars;\n")
if(len(choice)!=0):
    file2.write("\t#"+(choice)+" $finish;\n")
file2.write("\nend\n")
#------------------------------------------------------------------------------
#end line
file2.write("\nendmodule")
file2.close()
print("Test Bench "+a+"_tb.v Created Sucessfully")
os.system("iverilog "+a+".v")
print("File :- "+a+".v"+" Compilation Sucessful")
os.system("iverilog "+a+"_tb.v")
print("TestBanch :- "+a+"_tb.v"+" Compiled Sucessful")
tb=input("Do you want to Run TestBench :-")
if(len(tb)!=0):
    os.system("./a.out")
    os.system("rm a.out")
# os.system("rm "+a+"_tb.v")