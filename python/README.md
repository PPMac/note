# Python学习笔记

## 1. 文章参考

* Python 新员工教材(楚广明 2012)
* Python基础教程（第2版）

## 2. Python 概述

1. Python 使用强制缩进的编码风格,并以此组织代码块
2. Python 语句结尾不用分号
3. Python 标明注释用#(单行)或三引号(多行)(注:三引号实际上是定义字符串的, 也可以起到注释作用)
4. Python 语言没有入口方法(main),代码会从头到尾顺序执行
5. Python 用 import 引用所需要的模块
    * import math
    * from math import sqrt
    * from math import sqrt as a


## 3. 版本选择

### 3.1 Python 2 OR Python3 ?

官网的一句话: https://wiki.python.org/moin/Python2orPython3
>Short version: Python 2.x is legacy, Python 3.x is the present and future of the language


### 3.2 Jython OR IronPython ?

Python有多个发行版本可以选择，如:

* 官方Python
* ActivePython
* Stackless Python
* Jython
* IronPython

其中，官方python, ActivePython, Stackless Python都是基于C语言编写的。

ActivePython的内核与适用于Windows版本的标准python相同，最大区别在于它包含了许多额外独立的可用的工具(模块)， 如果你正在使用windows的话，ActivePython绝对值得一试。

Stackless Python是python版本的重新实现版本，基于原始的代码，但也包含了一些重要的内部改动。最大的优点就是允许深层次的递归并且多线程执行更加高效。

Jython利用java实现，运行在Java虚拟机中， 而IcronPython则是利用C#实现，运行于公共语言运行时(Common Language Runtime), 这个就是.NET的“java虚拟机”。

## 4. Python Shell (ipython && bpython)

* 写一些简单的调试代码
* 查看帮助信息(help, dir, type,  print module.__file__)
* 强大的计算器
    除法有坑：
    默认情况下是执行整数除法

    ```python
    >>> 1 / 2
    0
    ```

    如果希望执行普通除法的话, 有如下方法解决:

    * 将参与数除法的两个数中的一个转变为浮点数

    ```python
    >>> 1.0 / 2
    0.5
    ```

    * from __future__ import division (python中的时光机)

    ```python
    >>> from __future__ import division
    >>> 1 / 2
    0.5
    ```

    * 运行python时, 使用命令行开关-Qnew


## 5. 基本数据类型

>一切数据是对象,一切命名是引用

Python与java 的变量(函数、类等其他标识符)的命名规范基本一样,同样对大小写敏感。不一样的地方
是Python 中以下划线开始或者结束的标识符通常有特殊的意义.
例如以一个下划线开始的标识符如\_foo 不能用
from module import \*语句导入。前后均有两个下划线的标识符,如\_\_init\_\_被特殊方法保留。前边有两个下划线的标识符,如\_\_bar,被用来实现类私有属性。

Python 没有常量,如果你非要定义常量,可以参考例子`const.py`和`use_const.py`

```python
#--file: const.py --
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1、使用__setattr__来控制重新绑定
2、sys.modules[name]得到的是模块对象，通过模块对象可以访问其模块属性；
而Python不会进行严格的类型检测，所以直接将一个 _const类对象加入sys.modules字典，
而__name__的值为对应模块const的名字const，通过 sys.modules[__name__] = _const()用类对象替换模块对象，将对应的名字空间加以限制.
当使用import const时，会发生sys.modules[const] = _const()；
而访问const.attrvalue时会发生sys.modules[const].attrvalue，即 _const().attrvalue
"""

# 以单下划线开头的变量和函数被默认当作内部函数，
# 如果使用 from a_module import * 导入时，这部分变量和函数不会被导入
class _const:

    class _ConstTypeError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self._ConstTypeError, "Can't rebind const %s" % name
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self._ConstTypeError, "Can't unbind const %s" % name

import sys
sys.modules[__name__] = _const()
```


```python
# --file: use_const.py --
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import const

const.magic = 23
const.magic = 33


"""
out put:

Traceback (most recent call last):
  File "use_const.py", line 6, in &lt;module&gt;
    const.magic = 33
  File "/data/github/temp/python_brief/code/const.py", line 20, in __setattr__
    raise self._ConstTypeError, "Can't rebind const %s" % name
const._ConstTypeError: Can't rebind const magic
"""
```


### 5.1 常见的数据类型

#### 空类型

空类型(None)表示该值是一个空对象,比如没有明确定义返回值的函数就是返回None。
空类型没有任何属性,经常被用做函数中可选参数的默认值. None的布尔值为假。

#### 布尔类型

Python 中用 True 和 False 来定义真假
在Python中,None, 任何数值类型中的0, 空字符串, 空元组, 空列表, 空字典都被当作False, 其他对象均为True.

#### 数值类型

Python拥有四种数值类型: 整型(int)、长整型(long)、浮点类型(float)以及复数类型(complex)。
这些类型是不可变的，就是说整数对象一旦创建，其值便不可更改.
相反，系统将创建新的简单类型对象并将其赋值给变量。通过 Python id 函数，可以查看基本PyObject 标识的变更方式,另外str类型同样是不可变的。

```python
>>> i = 100
>>> id(i)
8403284
>>> i = 101
>>> id(i)
8403296
```

python语言的整型相当于C语言中的long, 在32位机器上的范围是 -2^31 ~ 2^31 - 1, 查看本机int的最大值sys.maxint

十六进制和八进制的表示方法

```python
>>> 0xF
15
>>> 010
8
```

#### 列表(list)

Python包含7种内建的序列：列表，元组，字符串，Unicode字符串，bytearrays, buffer对象和xrange对象.

(There are seven sequence types: strings, Unicode strings, lists, tuples, bytearrays, buffers, and xrange objects.)

列表和元组的主要区别在于：列表可以修改，元组则不能


##### 通用序列操作

*  索引

```python
>>> a='hello'
>>> a[0]
'h'
>>> a[-1]
'o'
```

* 切片

```python
# 分片操作是需要提供两个索引作边界的，第一个索引的元素是包含在分片内，第二个不包含(左闭右开)
>>> a='hello,world'
>>> a[2:6]
'llo,'
>>> a[-7:-1]
'o,worl'
# 切片中最左边的索引比最右边的在序列中晚出现，结果就是一个空的序列
>>> a[-2:-6]
''
>>> a[:3]
'hel'
>>> a[3:]
'lo,world'
>>> a[:]
'hello,world'

# 指定步长n，从开始到结束每隔(n-1)个元素
>>> a[::3]
'hlwl'
# 步长为负数时，从右开始往左数
>>> a[::-3]
'dooe'
# 步长不能为0
>>> a[::0]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: slice step cannot be zero

```

* 序列相加

```python
>>> [1,2,3]+[3,4,5]
[1, 2, 3, 3, 4, 5]
>>> 'hello' + 'world'
'helloworld'
# 只有相同类型的序列才可以相加
>>> [1,2,3] +'hello'
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: can only concatenate list (not "str") to list
```

* 乘法

```python
>>> print 'x' * 10
xxxxxxxxxx
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

* 成员资格

```python
>>> a ='hello'
>>> 'h' in a
True
>>> 'w' in a
False
```

* 长度，最大值和最小值

```python
>>> a=[5,2,4]
>>> len(a)
3
>>> max(a)
5
>>> min(a)
2

```


##### 列表常见操作

* 赋值

```python
>>> x=[1,2,3]
>>> x[1]=4
>>> x
[1, 4, 3]
```

* 删除元素

```python
>>> x=[1,2,3]
>>> del x[1]
>>> x
[1, 3]
```

* 切片赋值

```python
>>> a=list('perl')
>>> a[2:]=list('ar')
>>> a
['p', 'e', 'a', 'r']
# 与原序列不等长赋值
>>> a[1:]=list('ython')
>>> a
['p', 'y', 't', 'h', 'o', 'n']
# 在不替换任何元素的情况下插入新元素
>>> b=[1,5]
>>> b[1:1]=[2,3,4]
>>> b
[1, 2, 3, 4, 5]
# 删除元素
>>> b[1:4]=[]
>>> b
[1, 5]
```

* 常用函数

append(x) 尾部追加 单个对象 x,使用多个对象会引起异常.

count(x) 返回对象 x 在 list 中出现的次数

extend(L) 将列表 L 中的项添加到表中

index(x) 返回匹配对象 x 第一个表项的索引,无匹配时产生异常

insert(i,x) 在索引‘i’的元素前插入对象 x

pop(x) 删除列表中索引 x 的表项,并返回同该表项的值,无参数删除最后一个元素

remove(x) 删除表匹配对象 x 的第一个元素,无匹配时异常

reverse() 颠倒列表元素的顺序

sort() 对列表排序


上面append， extend， insert， remove，reverse，sort都是直接修改原来的列表，而不是返回一个新的列表

```python
# append
>>> a=[1, 2, 3]
>>> b=a.append(4)
>>> b
>>> a
[1, 2, 3, 4]

# count
>>> b=list('hello')
>>> b.count('l')
2

# extend
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]

# index
>>> b=list('hello')
>>> b.index('e')
1
>>> b.index('w')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: 'w' is not in list

# insert
>>> a = [1, 2, 3, 4]
>>> a.insert(2, 0)
>>> a
[1, 2, 0, 3, 4]

# pop
>>> a.pop()
4
>>> a
[1, 2, 0, 3]
>>> a.pop(2)
0

# remove
>>> a=list('hello')
>>> a.remove('l')
>>> a
['h', 'e', 'l', 'o']
>>> a.remove('w')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: list.remove(x): x not in list

# reverse
>>> a=[1, 2, 3]
>>> a.reverse()
>>> a
[3, 2, 1]

# sort
>>> a = [4, 6, 5, 1, 7]
>>> a.sort()
>>> a
[1, 4, 5, 6, 7]

# sorted函数，会返回排好续的列表
>>> a = [4, 6, 5, 1, 7]
>>> b=sorted(a)
>>> b
[1, 4, 5, 6, 7]
>>> a
[4, 6, 5, 1, 7]
```

* 高级排序

```python
>>>help(list.sort)
"""
sort(...)
    L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
    cmp(x, y) -> -1, 0, 1
(END)
"""
```

cmp(e1, e2) 是带两个参数的比较函数, 返回值: 负数: e1 < e2, 0: e1 == e2, 正数: e1 > e2. 默认为 None, 即用内建的比较函数.
key 是带一个参数的函数, 用来为每个元素提取比较值. 默认为 None, 即直接比较每个元素.
通常, key 和 reverse 比 cmp 快很多, 因为对每个元素它们只处理一次; 而 cmp 会处理多次.

```python
>>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# sort by age
>>> students.sort(key=lambda student : student[2])
>>> students
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


>>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# sort by age
>>> students.sort(cmp=lambda x, y : cmp(x[2], y[2]))
>>> students
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> a = [4, 6, 5, 1, 7]
>>> a.sort(reverse=True)
>>> a
[7, 6, 5, 4, 1]
```

* 把列表当作堆栈使用

利用列表的常用函数可以很方便的实现堆栈(后进先出)的效果.

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

* 把列表当作队列使用

虽然列表可以当作队列(先进先出)使用,但是这样用效率不高。相对来说从列表末尾添加和弹出很快；在头部插入和弹出很慢（因为，为了一个元素，要移动整个列表中的所有元素）。

如果要实现队列,可以使用 collections.deque，它为在首尾两端快速插入和删除而设计。

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

* 函数式编程工具

对于列表来讲, 有三个内置函数 filter(), map(), 和 reduce() 。

filter(function, sequence) 返回一个sequence（序列），包括了给定序列中所有调用 function(item) 后返回值为true的元素。如果该 序列 （sequence）是一个 string（字符串）或者 tuple（元组），返回值必定是同一类型，否则，它总是list

```python
# 求不能被2和3整除的序列
>>> def f(x): return x % 2 != 0 and x % 3 != 0
>>> filter(f, range(2, 25))
[5, 7, 11, 13, 17, 19, 23]
>>> filter(None,range(1, 6))
[1, 2, 3, 4, 5]

>>> range(5)
[0, 1, 2, 3, 4]
# 注意0并没有被返回
>>> filter(None, range(5))
[1, 2, 3, 4]

```

map(function, sequence)为每一个元素依次调用 function(item) 并返回一个所有返回值的列表.

```python
>>> def cube(x): return x*x*x
...
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

可以传入多个序列，函数也必须要有对应数量的参数，执行时会依次用各序列上对应的元素来调用函数（如果某些序列比其它的短，就用 None 来代替）。如果把 None 做为一个函数传入，则直接返回参数做为替代。

```python
>>> seq = range(8)
>>> def add(x, y): return x+y
>>> map(add, seq, seq)
[0, 2, 4, 6, 8, 10, 12, 14]
>>> map(None, seq, seq)
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
```

reduce(func, sequence) 返回一个单值，它是这样构造的：首先以序列的前两个元素调用函数 function ，再以返回值和第三个参数调用，依次执行下去。

```python

>>> def add(x,y): return x+y
# 计算1加到10的和
>>> reduce(add, range(1, 11))
55
```

如果序列中只有一个元素，就返回它，如果序列是空的，就抛出一个异常。

可以传入第三个参数做为初始值。如果序列是空的，就返回初始值，否则函数会先接收初始值和序列的第一个元素，然后是返回值和下一个元素，依此类推。

```python

>>> reduce(add,[2])
2
>>> reduce(add,[])
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: reduce() of empty sequence with no initial value
>>> reduce(add, range(1,11),9)
64
>>> reduce(add, [],9)
9
```


#### 元组(tuple)

元祖和序列最大的区别是： 序列可以修改，元祖则不能。

元祖在只有一个值时，逗号也必须有:

```python
>>> a=(2)
>>> a
2
>>> b=(2,)
>>> b
(2,)
>>> print type(a)
<type 'int'>
>>> print type(b)
<type 'tuple'>
```

元组除了创建和访问元组元素之外，没有什么其他的操作

```python
>>> pprint.pprint(dir(tuple))
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__getslice__',
 '__gt__',
 '__hash__',
 '__init__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'count',
 'index']
```



#### 字符串

所有前面介绍的标准的序列操作（索引，切片，乘法，成员资格判断，求长度，最大值，最小值）对字符串同样适用。
但是有一点需要注意的是字符串是不可变的，因此切片赋值是不可以的。

Python中普通的字符串在内部是以ASCII码存储的，而Unicode字符串在存储为16位的Unicode编码
在 Python 中定义一个标准字符串(str)可以使用单引号、双引号、三引号。
字符串前面加r,表示是原始字符串.

```python
>>> a='Hello,\nWorld'
>>> b=r'Hello,\nWorld'
>>>print a
Hello,
World
>>>print b
Hello,\nWorld

# 字符串前面加u,表示Unicode字符串
>>> a='hello'
>>> b=u'hello'
>>> print type(a)
&lt;type 'str'&gt;
>>> print type(b)
&lt;type 'unicode'&gt;
```

同时需要注意的是的，在使用UTF-8编码时，非unicode字符中一个汉字的长度是3,
gbk是2.unicode字符中一个汉字的长度是1

```python
>>> a='中'
>>> a
'\xe4\xb8\xad'
>>> b=u'中'
>>> b
u'\u4e2d'
>>> c=b.encode('gbk')
>>> c
'\xd6\xd0'
>>> print len(a), len(b), len(c)
3 1 2
>>>
```


* 字符串格式

```python
>>> '%x' % 10
'a'
>>> '%X' % 10
'A'
>>> '%d' % 10
'10'
>>> from math import pi
# 保留小数位数
>>> '%.2f' % pi
'3.14'
# 右对齐
>>> '%10.2f' % pi
'      3.14'
# 左对齐
>>> '%-10.2f' % pi
'3.14      '
# 填充
>>> '%010.2f' % pi
'0000003.14'
# 格式化字符串里面包括百分号的时候，要用%%
>>> '%d%%' % 100
'100%'
```

* 模板字符串

```python
from string import Template
>>> s=Template('Hello $x,my name is $y')
>>> d={'x': 'boy', 'y': 'Lucy'}
>>> s.substitute(d)
'Hello boy,my name is Lucy'
```

* 常用函数

```python
>>> pprint.pprint(dir(str))
['__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getnewargs__',
 '__getslice__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmod__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '_formatter_field_name_split',
 '_formatter_parser',
 'capitalize',  # 首字母大写
 'center',      # center(width, fillchar) 按照制定的长度width，让字符串居中，填充fillchar
 'count',
 'decode',
 'encode',
 'endswith',
 'expandtabs',  # 用空格替换tab
 'find',
 'format',
 'index',
 'isalnum',     # Return True if all characters in S are alphanumeric(字母数字)
 'isalpha',     # Return True if all characters in S are alphabetic(拼音)
 'isdigit',
 'islower',
 'isspace',
 'istitle',
 'isupper',
 'join',
 'ljust',       # 按照指定的长度左对齐,不足的填充指定的字符
 'lower',
 'lstrip',
 'partition',   # 按照制定的分割符号分隔str,返回分割符号前,分割符号,分割符号后
 'replace',
 'rfind',
 'rindex',      # 返回查找字符的最大索引值
 'rjust',
 'rpartition',  # 跟partition, 只是从后往前找
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',    # 反转字母的大小写
 'title',       # 每个单词收字母大写
 'translate',   # 单个字符的替换
 'upper',       # 全部转换成大写
 'zfill']
```

```python
>>> a='a\tb\rc\n'
>>> a
'a\tb\rc\n'
>>> import string
# create translate table
>>> tb=string.maketrans('\t\r\n','trn')
>>> a.translate(tb)
'atbrcn'
```

#### 字典

* 字典的格式化

```python
>>> info = {'name':'lianglin', 'age':25}
>>> 'my name is %(name)s, my age is %(age)d' % info
'my name is lianglin, my age is 25'
```

* 常用函数

has_keys(x) 若字典中有 x 返回 true

keys() 返回键的列表

values() 返回值的列表

dict.items() 返回 tuples 的列表。每个 tuple 有字典的 dict 的键和相应的值组成

clear() 删除词典的所有条目

copy() 返回字典的高层结构的拷贝,但不复制嵌入结构,而复制那些结构的引用。

update(x) 用字典 x 中的键/值对更新字典的内容。如果字典x中的键不存在元字典中，则原字典添加x字典的键/值信息。

get(x[,y]) 返回键 x。若未找到返回 None


```python
# copy 方法实际上是浅复制(shallow copy)
>>> x={'name': 'admin', 'machines': ['foo', 'bar', 'baz']}
>>> y=x.copy()
>>> y['name']='admin_y'
>>> y['machines'].remove('foo')
>>> x
{'name': 'admin', 'machines': ['bar', 'baz']}
>>> y
{'name': 'admin_y', 'machines': ['bar', 'baz']}
>>>
# 深度复制（deep copy)
>>> from copy import deepcopy
>>> dc =deepcopy(y)
>>> dc
{'name': 'admin_y', 'machines': ['bar', 'baz']}
>>> dc['machines'].append('foo')
>>> dc
{'name': 'admin_y', 'machines': ['bar', 'baz', 'foo']}
>>> y
{'name': 'admin_y', 'machines': ['bar', 'baz']}

# update
>>> x={'name': 'admin', 'machines': ['foo', 'bar', 'baz']}
>>> x.update({'name':'admin_update'})
>>> x
{'name': 'admin_update', 'machines': ['foo', 'bar', 'baz']}
>>> x.update({'time':'now time'})
>>> x
{'name': 'admin_update', 'machines': ['foo', 'bar', 'baz'], 'time': 'now time'}
```

#### 集合(set)

Python 中的集合是指无序的、不重复的
元素集,类似数学中的集合概念,可对其进行交、并、差、补等逻辑运算。

```python
>>> a = [2,3,4,2,1]
>>> set(a)
set([1, 2, 3, 4])

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                              # letters in a but not in b
set(['r', 'd', 'b'])
>>> a | b                              # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                              # letters in both a and b
set(['a', 'c'])
>>> a ^ b                              # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])
```

### 数据类型转换

str(x) 将对象 x 翻译为字符串

list(x) 将对象序列 x 作为列表返回。例如‘hello’返回['h','e','l','l','o'],将 tuple 转换为列表

tuple(x) 将对象序列 x 作为 tuple 返回

int(x) 将字符串和数字转换为整数,对浮点进行舍位而非舍入

long(x) 将字符串和数字转换为长整形

float(x) 将 str 和 num 转换为浮点对象

complex(x,y) 将 x 做实部,y 做虚部创建复数

hex(x) 将整数或长整数转换为十六进制字符串

oct(x) 将整数或长整数转换为八进制字符串

ord(x) 返回字符 x 的 ASCII 值

chr(x) 返回 ASCII 码 x 代表的字符

min(x[,...]) 返回序列中最小的元素

max(x[,...]) 返回序列中最大的元素



## 流程控制

if...elif...else
for
while
break
continue
pass

python中的for语句相当于java中的foreach语句,它用于从集合对象(list/str/tuple等)中遍历数据

python中没有switch...case语句,只能用if...elif...else语句表达

python中也没有do...while

列表内涵(List comprehension)
Python 最强有力的语法之一,常用于从集合对象中有选择地获取并计算元素,虽然多数情况下可
以使用 for/if 等语句组合完成同样的任务,但列表内涵书写的代码更加简洁。
列表内涵的一般形式如下,我们可以把[]内的列表内涵写为一行,也可以写为多行。

```
[表达式 for item1 in 序列 1 ... for itemN in 序列 N if 条件表达式]
```

上面的表达式分为三部分: 最左边是生成每个元素的表达式,然后是 for 迭代过程,最右边可以设定一个 if
判断作为过滤条件。


列表内涵的一个著名例子是生成九九乘法表:

```python
>>> s=[(x,y,x*y) for x in range(1,10) for y in range(1,10) if x>=y]
>>> s
[(1, 1, 1), (2, 1, 2), (2, 2, 4), (3, 1, 3), (3, 2, 6), (3, 3, 9), (4, 1, 4), (4, 2, 8), (4, 3, 12), (4, 4, 16), (5, 1, 5), (5, 2, 10), (5, 3, 15), (5, 4, 20), (5, 5, 25), (6, 1, 6), (6, 2, 12), (6, 3, 18), (6, 4, 24), (6, 5, 30), (6, 6, 36), (7, 1, 7), (7, 2, 14), (7, 3, 21), (7, 4, 28), (7, 5, 35), (7, 6, 42), (7, 7, 49), (8, 1, 8), (8, 2, 16), (8, 3, 24), (8, 4, 32), (8, 5, 40), (8, 6, 48), (8, 7, 56), (8, 8, 64), (9, 1, 9), (9, 2, 18), (9, 3, 27), (9, 4, 36), (9, 5, 45), (9, 6, 54), (9, 7, 63), (9, 8, 72), (9, 9, 81)]
>>>
```

三目运算符( ? :)
```
>>> a = True if 5>3 else False
>>> a
True
```


## 函数

* 函数的定义  def foo(): pass
* 返回值     def foo(n): return n + 1
* 位置参数   def foo(a, b):pass (参数多的时候，位置难记)
* 默认参数   def foo(a="hello", b='world'): pass
* 收集参数   def foo(a, b, *args, **kwargs): pass
```
def foo(*args):
    for i in args:
        print i


foo(1, 2, 3)
a = [1, 2, 3]
foo(*a)


def bar(**kwargs):
    for key, value in kwargs.items():
        print key, value


bar(name="Jack", age=12)

user = {"name": "Jack", "age": 12}
bar(**user)

```

## 异常
什么是异常？
抛出异常:raise
常见异常:
Exception: 所有异常的基类
IOException: 试图打开不存在的文件或打开文件时发生错误时引发
IndexException: 使用序列中不存在的索引时引发
KeyError: 使用映射中不存在的键值时引发
SyntaxError: 代码为错误形式时引发
TypeError: 错误的对象类型
ZeroDivisionError: 除数为0
自定义异常:
class MyException(Exception):pass
捕获异常
try:
except:
except:
else:
......
finally:
```
try:
    x = 1 / 2
    print x

    d = {}
    print d['name']
except ZeroDivisionError, e:
    print e
    print "catch exception"
except (ZeroDivisionError, KeyError), e:
    print e

except:
    pass
else:
    print "No exception"
finally:
    print "DONE"

```
## 程序调试
print
trace 模块
python -m trace --trace script.py |grep '^(mod1.py|mod2.py)'
shell (http://qixinglu.com/post/embed_python_shell_in_code.html)
```
def foo():
    text = "hello world"

    import code
    pyshell = code.InteractiveConsole(locals=locals())
    pyshell.interact()

    print "DONE"
foo()

#ipython shell
def bar():
    text = "hello world"

    from IPython.Shell import IPShellEmbed
    ipshell = IPShellEmbed()
    ipshell()

    print text

bar()
# 在调试时修改变量的值并不会影响代码里的变量
```
pdb (http://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/)
python -m pdb myscript.py
=====================================================
help	帮助
list 或 l	查看当前行的代码段
break line_num或 b line_num 设置断点（在指定的行号出设置断点，如果只执行b，查看所有断点)
continue 或 c	继续执行程序

step 或 s	进入函数
return 或 r	执行代码直到从当前函数返回
exit 或 q	中止并退出
next 或 n	执行下一行
pp	打印变量的值
=====================================================

pdb的直接替代者：
ipdb(easy_install ipdb) – 类似ipython(有自动完成，显示颜色等)
pudb(easy_install pudb) – 基于curses（类似图形界面接口），特别适合浏览源代码
使用pydev
http://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/



## 开发环境
ipython, bpython
eclipse + pydev
vim + python-mode(https://github.com/klen/python-mode)
语法高亮
虚拟环境支持
运行代码 (<leader>r)
添加删除断点（<leader>b)
优化缩进
代码折叠
代码检查(pylint, pyflakes, pylama)
帮助文档查看(pylint, pyflakes, pylama, ...)
自动解决PEP8错误(什么是PEPE8? Style Guide for Python Code<http://www.python.org/dev/peps/pep-0008/>)
代码快速跳转
更多...



* python 函数主要是通过def来进行函数操作的,def的功能是创建一个对象，并且赋值给某个变量。
当python运行到def语句时，它会生成一个函数对象并且复制给某个函数名，函数名就是函数的引用，
相当于函数名存了函数对象的地址。

* 函数是通过return来返回值的。

* python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。
实际上,这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象(比如字典或者列表)的引用,
就能修改对象的原始值——相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象(比如数字、字
符或者元组)的引用,就不能直接修改原始对象——相当于通过“传值'来传递对象.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建一个新的对象,不会改变原来的引用
def add_list(p):
    p = p + [1]

#改变原来的引用
def edit_list(p):
    p.append(1)

def change_int(x):
    x = 10

a = [1, 2, 3, 4]
b = 5

# out put
# origin a = [1, 2, 3, 4]
# after call add_list: a = [1, 2, 3, 4]
# after call edit_list: a = [1, 2, 3, 4, 1]
# origin b = 5
# after call change_int: b = 5
```

* 参数
可变长度的参数
星号操作符是将参数作为元组传递给函数
双星号是将参数作为字典传递给函数

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bar(*args):
    for argv in args:
        print argv

def foo(**kargs):
    for key, value in kargs.items():
        print "%s => %s" % (key, value)

bar(1, 2, 3)
bar(*(1, 2, 3))
foo(a='form1', b='form2')
foo(**{'a': 'form1', 'b': 'form2'})

# out put
"""
1
2
3
1
2
3
a => form1
b => form2
a => form1
b => form2
"""
```


## 其它

eval()函数, 用来计算存储在字符串中的有效Python表达式
exec()函数, 用来执行储存在字符串中python语句
execfile()函数, 用来执行一个外部的py文件

```python
>>> str="1+2"
>>> print eval(str)

>>> exec "a=100"
print a

>>> execfile(r’/tmp/a.py’)
```

## 未完待续......
