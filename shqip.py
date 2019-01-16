'''
Python eshte nje gjuh programuese.
Gjuhë skriptive e nivelit të lartë.
Suporton programimin e orientuar nga objekti.
Python eshte Me burime të hapura (Open Source)
Eshte e lehte per tu mesuar posaqerisht per fillestaret.
Python gjen zbatim në:
Web Aplikacione
Aplikacione Desktop etj.

Operatorët logjikë
and = Kontrollon për vërtetësi vlerë në dy anët e operatorit dhe atëherë kushti është i vërtetë.
or = Kontrollon për vërtetësi kushti në të paktën njërën anë të operatorit dhe atëherë kushti është i vërtetë.
not = Mohimi i rezultatit para operatorit not.
print (2 < 3 and 3 > 1) #True
print(2 < 3 or 3 > 1) #True
print(2 < 3 or not 3 > 1) #True (2shi o ma i vogel se 3shi [True] or 3shi o mi madh se 1 mirpo tash duhet e kunderta se e kna not perpara kshtu qe TRUE OR FALSE = TRUE)
print(2 < 3 and not 3 > 1) #False

Operatorët krahasues
• == equal to (barabert) [if 2 == 2]
• != not equal to (Nuk është e barabartë me) [if 2!= 3]
• < less than (me e vogel se) [if 1 < 4]
• > greater than (me e madhe se) [if 6 > 9]
• <= less than or equal to (me e vogel se ose e barart me) [if 8 <= 8]
• >= greater than or equal to (me e madhe se ose e barabarte) [5 >= 5]

Operatorët aritmetikë
+ addition (mbledhja) (2 + 2) = 4
- subtraction (zbirtja) (2 - 2) = 0
* multiplication (shumzimi) (2 * 2) = 4
/ division (pjestimi)
Kryen pjesëtimin. Kujdes! Nëse në të dy anët e operatorit kemi numra të plotë pjesa dhjetore nuk shfaqet, psh 8 / 5 jep 1. Nëse duam rezultatin e saktë 1.6 duhet të shkruajmë 8.0 / 5 ose 8 / 5.0
(2 % 2) = 1.0 (1 * 2 = 2)
** exponent (Kryen ngritjen në fuqi. ) (3 ** 2) = 9 (9 ** 2) = 81
// Kryen pjesëtim të plotë pa pjesë dhjetore edhe nëse të dy numrat nuk janë të plotë. Shembull:
% remainder (Kryen pjesëtim me mbetje dhe jep si rezultat vetëm mbetjen.) (2 % 2) = 0 mbetja

Variablat Emrat e ndryshoreve:
Mund të fillojnë me shkronjë të madhe ose jo
Përveç gërmave mund të përmbajnë edhe karakterin _
Mund të përmbajnë numra, mjafton të mos fillojnë me një të tillë
'''

# Funksioni for
#for i in 'python':
  #print ('germa', i) germa p germa y

'''
Funksioni range
Funksioni range() është i lidhur ngushtë me ciklin for.
Ky funksion i gatshëm i pythonit bën të mundur shfaqjen e numrave në progresion aritmetik (në matematikë progresion aritmetik është një sekuencë numrash ku diferenca e dy numrave fqinjë është konstante).
Nese nuk vendoset defiernca aj automatikisht ka vleren 1.
Sintaksa është: range(fillimi, perfundimi, diferenca = 1)
'''
#for x in range(10, 20, 1):
  #print(x)

# numrat tek dhe qift
'''
for i in range(1,5):
  if i % 2 == 0:
    print(i, "eshte qift")
  else:
    print(i, "eshte tek")
'''
'''
1 eshte tek
2 eshte qift
3 eshte tek
4 eshte qift
[1shi kur pjestohet me 2 dhe mbetja nuk mbet 0 numri eshte tek, e kunderta qift.]
'''

'''
printo numrat vetem tek nga 1 deri 5 
for i in range (1,5,2):
  print i
  '''


# Numri faktorial
def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
#print("Numri faktorial i numrit 5:", factorial(5)) #Numri faktorial i numrit 5: 120

# Funksionet upper, lower, len, max, min, sum
x = "shqip"
y = "SHQIP"
z = [1,9,4]
p = [1,1,1,1]
#print("Funksioni upper:", x.upper())#Funksioni upper: SHQIP
#print("Funksioni lower:", x.lower())#Funksioni lower: shqip
#print("Funksioni len:", len(x))#Funksioni len: 5
#print("Funksioni max:", max(z))#Funksioni max: 9
#print("Funksioni min:", min(z))#Funksioni min: 1
#print("Funksioni sum:", sum(p))#Funksioni sum: 4 [1+1+1+1]

# Classes
class Qenet:
  def __init__(self, name, color):
    self.name = name
    self.color = color
  def name():
    return self.name
qeni_1 = Qenet("Qeni i sabitit", "I Kuq")
#print("Clasa qenet:", qeni_1.name, qeni_1.color) #Clasa qenet: Qeni i sabitit I Kuq
class Banka:
	def __init__(self):
		self.bilanci = 0
	def shto(self, shuma):
		self.bilanci = self.bilanci + shuma
		return self.bilanci
	def terhiq(self, shuma):
		self.bilanci = self.bilanci - shuma
		return self.bilanci
student_genti = Banka()
#print(student_genti.shto(10)) #10 [10 sepse bilanci o 0]
#print(student_genti.terhiq(1))#9 [9 sepse i kemi terheq 1 prej 10 qe patum me heret]
#print(student_genti.bilanci) #9 [bilanci tani eshte 9]
class Dog():
  def bark(self):
    print("Woof")
husky = Dog()
#husky.bark() #Woof
class A:
  def method(self):
    print("A method")
class B(A):
  def another_method(self):
    print("B method")
class C(B):
  def third_method(self):
    print("C method")
c = C()
#c.method() #A method [func. method nuk egziton ne C kontrollon ne B ska as ne B shkon e merr ne a]
#c.another_method() #B method [func. another_method nuk egziton ne C kontrollon ne B dhe e merr ne B]
#c.third_method() #C method [func. third_method kontrollon ne C dhe e gjen dhe e printon]

class A:
	def f(self):
		return self.g()
	def g(self):
		return "A"
class B(A):
	def g(self):
		return "B"
a = A()
b = B()
#print(a.f(), b.f()) # A B   = f nuk osht ne B e merr ne A self.g e kthen ne B
#print(a.g(), b.g()) # A B

# "/" pjestimi "%" mbetja
#print(2 + 3 * 4) #14 [3 here 4 = 12, 12 + 2 = 14]
#print((2 + 3) * 4) #20 [2+3 = 5, 5 * 4 = 20]

x = 0
y = 0
def incr(x):
  y = x + 1
  return y
incr(5)
#print(x, y) #0 0

x = 10
def f():
  return x + 1
#print("X:", x) #X: 10
#print("F:", f()) #F: 11
#print("X:", x) #X: 10

x = 1
def f():
  x = 2
  return x
#print("X:", x) #X: 1
#print("F:", f()) #F: 2
#print("X:", x) #F: 1

x = 1
def f():
  global x
  y = x
  x = 2
  return x + y
#print(x) #1
#print(f()) #3
#print(x) #2

x = 2
def f(a):
  x = a * a
  return x
y = f(3)
#print(x, y) #2 9

# Problem 12: Write a function count_digits to find number of digits in the given number.
def count_digits(number):
  return len(str(number))
#print(count_digits(1111111111111111)) #16

# Problem 13: Write a function istrcmp to compare two strings, ignoring the case.
def istrcmp(string1, string2):
  string1 = string1.upper()
  string2 = string2.upper()
  if string1 == string2:
    return True
  else:
    return False;
#print(istrcmp("a", "A")) #True

#print("False eshte me e madhe se 0 ? Jo sepse dyjat kan vleren 0", False > 0)
#print("True eshte me madhe se 0 sepse ka True ka vlere 1", True > 0)

# lists
a = [1, 2, "hello", "world", ["another", "list"]]
#print(a[4][0]) #another
#print(a[4]) #['another', 'list']

#Modules
import time
#print(time.asctime()) #Tue Jan 15 22:17:35 2019

# plus mbledhja
#print("Mbledhja e listest me komanden sum ,", sum([1, 2, 3]))



x = [1, 2, 3, 4]
#print(x[-1]) # prej right edhe numrin jo prje 0 po prej 1

#Mund të përdorim ":" në listë për të marrë pjesë në një listë. numri i 2t fillon te numroj prej 1
x = [1, 2, 3, 4, 5, 6, 7, 8]
#print(x[0:4]) #[1, 2, 3, 4]
#print(x[1:4]) #[2, 3, 4]
#print(x[:4]) #[1, 2, 3, 4]
#print(x[:]) #[1, 2, 3, 4, 5, 6, 7, 8]
#print(x[::-1]) #[8, 7, 6, 5, 4, 3, 2, 1]
#print(x) #[1, 5, 3, 4]

#Presence of a key in a list can be tested using in operator.
x = [1, 2, 3, 4]
#print(2 in x) #True
#print(21 in x) #False

# shtimi ne list me komand append
a = [1, 2]
a.append(3)
#print(a) # [1,2,3]

#List members can be modified by assignment.
x = [1, 2, 3, 4]
x[1] = 5
#print(x) #[1, 5, 3, 4]

#lista me nr prej 0 deri 4
#for x in [1, 2, 3, 4]:
  #print(x)
#for i in range(0, 5):
  #print(i)

# Write a function unique to find all the unique elements of a list.
def lista_unike(lista):
  new_list = []
  for x in lista:
    if x not in new_list:
      new_list.append(x)
  return new_list
#print(lista_unike(["1", "1", "2"]))#['1', '2']

# Renditja e listest
a = [2, 10, 4, 3, 7]
a.sort()
#print(a) #[2, 3, 4, 7, 10]

a, b = 1, 2
#print(a) #1
#print(b) #2


#a, b = 2, 3
#c, b = a, c + 1
#print(a, b, c)#2 2 3


x, y = 2, 6
x, y = y, x + 2
#print(x, y) #2 2

x = "shqip"
#print(x[4]) #p
# Për të indeksuar nga fundi, përdoren numrat negativë. (nga fundi num numron nga zero por prej 1)
#print(x[-5]) #s


def shumzo(nr):
  return nr * nr
#print(shumzo(shumzo(3))) #81

# funksion per me gjet "pi" ne matmatik
pi = 3.14
def area(r):
  return pi * r * r
#print(area(11)) #379.94

# nese variabla merret si globale ne fuksione atehere variabla ndryshon
x = 1
def po():
  global x
  x = 10
  return x
#print(x) #1
#print(po()) #10
#print(x) #10

#And some arguments can have default values.
#def increment(x, amount=1):

#The built-in function "int" converts string to ingeter and built-in function "str" converts integers and other type of objects to strings.
int("50") #50
str(123) #"123"

# Methods
# Methods are special kind of functions that work on an object.
# For example, upper is a method available on string objects.
x = "hello"
#print(x.upper()) #HELLO
# metoda dallon prej funksioni sepse metoda eshte e integruar e funksioni i shkruar prej neve.


#x = 2
#if x == 2:
  #print(x)
#else:
  #print(zzz) # no error edhe pse nuk u defino variabl

# Kapercimi i një hapi të ciklit - continue
x=0
while x < 10:
  x = x+1
  if x == 7:
    continue
  #print(x)
# numrat printohen prej 1 deri ne 10 mirpo 7shi jo pershkak qe po e kapercejm

'''Shembull: Të krijojmë një matricë me përmasa 3x3.

>>>
matrica = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrica[0][2]  # rreshti i pare elementi i trete
3
matrica[2][1]  # rreshti i trete elementi i dyte
8
'''

# metada insert per lista
x = [1,2,3,4]
x.insert(0, "bla")
#print(x) #['bla', 1, 2, 3, 4]

'''
class Shembull(object):
  def printo(self, emri):
    self.emri = emri
    printo self.emri
objekti = Shembull()
objekti.printo('piton')
'''
# heqja e elmentit te fundit prej liste
x = [1,2,3,4,5,6]
print(x[0:-1])

for i in range(10):
  print( i, i*i, i*i*i)