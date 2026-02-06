def a():
 aq = int(input("ادخل عمرك"))

 if aq <= 18:
    print(" يمكنك الدخول")
 elif aq <= 100:
    print('انت شايب جدا ارحل')
 else:
    print("مرحبا عمرك هو", aq)
a()

def b():
 names = ["فهد", "خالد", "طاهر", 12]
 names[1] = "عبد الله"
 names.insert(2, "امين")
 names.remove("طاهر")
 print(names)

 ages = [12, 45, 10, 1]
 ages.clear()

 child_date = ("احمد", "الرياض", "1-2-2010")
 child_date = {"name":"احمد", "city":"الرياض", "date":"1-2-2010"}
 del child_date["city"]
 print(child_date.values())
b()
def c():
 aa = 1
 while aa <=5:
    print(aa)
    aa += 1

 student = ['مالك', "طارق", "صهيب", "غاشم"]
 for s in student:
    print(s)

 for w in range(5, 10):
    print(w)
c()

def d():
  bbbb = -111
  print(abs(bbbb))

  cccc = 3.56789
  print(round(cccc, 2))

  zzzz = 4
  print(pow(zzzz, 3))

  ssss = 16, 25, 9, 4
  print(max(ssss))
  print(min(ssss))
  print(sum(ssss))
c()

import math
vvvv = 144
print(math.sqrt(vvvv))
print(math.remainder(10, 3))


import random
print(random.randint(1, 100))


import datetime
date = datetime.datetime.now(2020, 10, 5)
print(date)
time = datetime.time(14, 30, 0)
print(time)
Now = datetime.datetime.now()
print(Now)
print(date.strftime('%A %B %Y'))
print(date.strftime('%I %M %S'))


alphapite = "abcdefghijklmnopqrstuvwxyz"
print(alphapite[0])
print(alphapite[-2])
print(alphapite.index("m"))

text = 'مرحبا بكم في عالم البرمجة'
print(text[0:7:2])
s = slice(0, 7, 2)
print(text[s])