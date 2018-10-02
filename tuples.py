Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t=12,23,'hello'
>>> type(t)
<class 'tuple'>
>>> t[]0
SyntaxError: invalid syntax
>>> t[0]
12
>>> t
(12, 23, 'hello')
>>> t[0]=55
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t[0]=55
TypeError: 'tuple' object does not support item assignment
>>> r=11,22,'rrrr',(5,6)
>>> r
(11, 22, 'rrrr', (5, 6))
>>> #nested tuples
>>> #tuples are immutable
>>> empty=()
>>> len(empty)
0
>>> s=1,2
>>> s+=s
>>> s
(1, 2, 1, 2)
>>> s*=s
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s*=s
TypeError: can't multiply sequence by non-int of type 'tuple'
>>> #tuple packing
>>> t=11,22,'hell'
>>> x,y,z=t
>>> x
11
>>> y
22
>>> z
'hell'
>>> x,y,z,w=t
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x,y,z,w=t
ValueError: not enough values to unpack (expected 4, got 3)
>>> 
>>> 
>>> #mixed values
>>> mixed=('c',0,0,'K','I','E')
>>> mixed
('c', 0, 0, 'K', 'I', 'E')
>>> for i in mixed:
	print(i,":",type(i))

c : <class 'str'>
0 : <class 'int'>
0 : <class 'int'>
K : <class 'str'>
I : <class 'str'>
E : <class 'str'>
>>> mixed[1]='0'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    mixed[1]='0'
TypeError: 'tuple' object does not support item assignment
>>> mixed[1]='o'
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    mixed[1]='o'
TypeError: 'tuple' object does not support item assignment
>>> li=[1,2,3,4,5]
>>> to=1,2,3,4,5
>>> to.append(5)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    to.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> li.append(5)
>>> a=5,6
>>> b=1,4
>>> a>b
True
>>> c=1,5
>>> b>c
False
>>> #checks like in strings, every element one by one
>>> #srtcmp
>>> #tuples are faster than lists
>>> #protect data which is immutable
>>> #tuples can be used as keys on dictionaries
>>> #swap (x,y)=(y,x)
>>> 
>>> 
>>> #are tuples fully immutable?
>>> t=1,2,3,4,[3,5]
>>> t
(1, 2, 3, 4, [3, 5])
>>> t[2][0]=9
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t[2][0]=9
TypeError: 'int' object does not support item assignment
>>> t[2][1]=9
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    t[2][1]=9
TypeError: 'int' object does not support item assignment
>>> t[4][0]=9
>>> t
(1, 2, 3, 4, [9, 5])
>>> #can change list element in tuple
>>> id(t[1])
140733512537152
>>> #memory location of a perticular id
>>> 
>>> id(t[2])
140733512537184
>>> t1=1,1,2,4,5
>>> id(t[1])
140733512537152
>>> id(t[0])
140733512537120
>>> id(t1[1])
140733512537120
>>> id(t1[0])
140733512537120
>>> t[4].append(8)
>>> t
(1, 2, 3, 4, [9, 5, 8])
>>> for i in t:
	print(i,":",type(i))

1 : <class 'int'>
2 : <class 'int'>
3 : <class 'int'>
4 : <class 'int'>
[9, 5, 8] : <class 'list'>
>>> t+t1
(1, 2, 3, 4, [9, 5, 8], 1, 1, 2, 4, 5)
>>> t1*2
(1, 1, 2, 4, 5, 1, 1, 2, 4, 5)
>>> t1
(1, 1, 2, 4, 5)
>>> t
(1, 2, 3, 4, [9, 5, 8])
>>> t.min()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    t.min()
AttributeError: 'tuple' object has no attribute 'min'
>>> min(t1)
1
>>> t.count(1)
1
>>> len(t)
5
>>> t.any()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    t.any()
AttributeError: 'tuple' object has no attribute 'any'
>>> any(t)
True
>>> #any checks if it is iterable or not
>>> sum(t)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    sum(t)
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> t.sum()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    t.sum()
AttributeError: 'tuple' object has no attribute 'sum'
>>> t.sorted()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    t.sorted()
AttributeError: 'tuple' object has no attribute 'sorted'
>>> 
>>> 
>>> 
#tuple conversion
>>> l=[1,2,3,4]
>>> t=tuple(l)
>>> t
(1, 2, 3, 4)
>>> sorted(t)
[1, 2, 3, 4]
>>> t=3,2,5,1,7,99,0
>>> sorted(t)
[0, 1, 2, 3, 5, 7, 99]
>>> type(t)
<class 'tuple'>
>>> t
(3, 2, 5, 1, 7, 99, 0)
>>> 
