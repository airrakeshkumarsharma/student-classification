import pandas as pd
import random

#Serial Number
sno = []

#Academic Behaviour
active = []
sem = []

#Higher Studies
name = []
mba = []
ms = []
mtech = []

#Job
govtjob = []
it = []
entrepreneur = []

#Co-circular activities
sports=[]
music=[]
dance=[]
others=[]

#General Behaviour
result=[]


#print("0 -> Not Attentive")
#print("1 -> A Bit Attentive")
#print("2 -> Attentive")
#print("3 -> Hyperactive")

for i in range(1,61):
    
    a = random.randint(0,3)
    s = random.randint(0,10)

    #a = int(input("Enter the Academic behaviour marks on a scale of 0 to 3"))
    #s = int(input("Enter the Semester marks on a scale of 0 to 10"))    
    
    active.append(a)
    sem.append(s)
    sno.append(i)

print("Academic Behaviour")
print("Attentive",active)
print("Semester marks",sem)


#print("0->Not Intrested")
#print("1->Confused")
#print("2-> Interested")
#print("3->Passionate")

for i in range(1,61):

    mba1 = random.randint(0,3)
    ms1 = random.randint(0,3)
    mtech1 = random.randint(0,3)

    #mba1 = input("Enter your intrest in mba on a scale of 0 to 3")
    #ms1 = input("Enter your intrest in ms on a scale of 0 to 3")
    #mtech1 = input("Enter your intrest in mtech on a scale of 0 to 3")

    mtech.append(mtech1)
    ms.append(ms1)
    mba.append(mba1)

print("Higher Studies")
print("M.tech",mtech)
print("MS",ms)
print("MBA",mba)


#print("0 -> Not Intrested")
#print("1 -> Confused")
#print("2 -> Interested")
#print("3 -> Passionate")

for i in range(1,61):

    g = random.randint(0,3)
    it1 = random.randint(0,3)
    e = random.randint(0,3)

    #g = input("Enter your intrest in govt job on a scale of 0 to 3")
    #it1 = input("Enter your intrest in IT job on a scale of 0 to 3")
    #e = input("Enter your intrest in entrepeneurship on a scale of 0 to 3")

    it.append(it1)
    entrepreneur.append(e)
    govtjob.append(g)

print("JOB")
print("IT job",it)
print("Bussiness",entrepreneur)
print("Govt Job",govtjob)


#print("1 -> Not Intrested")
#print("2 -> On and OFF")
#print("3 -> Regular")
#print("4 -> Passionate")

for i in range(1,61):

    s = random.randint(0,3)
    m = random.randint(0,3)
    d = random.randint(0,3)
    o = random.randint(0,3)

    #s = input ("Enter your intrest in sports on a scale of 0 to 3")
    #m = input ("Enter your intrest in music on a scale of 0 to 3")
    #d = input ("Enter your intrest in dance on a scale of 0 to 3")
    #o = input ("Enter your intrest in others on a scale of 0 to 3")

    music.append (m)
    sports.append (s)
    dance.append (d)
    others.append (o)

print("Co-Circular Activities")
print("music",music)
print("sports",sports)
print("dance",dance)
print("others",others)


#print("For grading any student consider the categories:")
#print(" polite, not polite")
#print(" responisible, not responsible")
#print(" honest, not honest")
#print(" give the data in number format:")
#print("0 -> No postive aspect")
#print("1 -> one postive aspect")
#print("2 -> two postive aspect")
#print("3 -> three postive aspect")

for i in range(1,61):

    k = random.randint(0,3)
    
    #k = int (input ("enter remarks for the student:"))
    
    result.append(k)

print("General Behaviour")
print(result)


csvf = pd.DataFrame({"S.No": sno, "Attentiveness": active, "Sem Marks": sem, "MBA": mba, "MS": ms, "M.Tech": mtech, "GOVTJOB": govtjob, "IT": it, "ENTREPRENEUR": entrepreneur, "sports": sports, "music": music, "dance": dance, "others": others, "StudentBehaviour":result})
csvf.to_csv("AcademicBehaviour.csv",index="false")
print(csvf)
