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

