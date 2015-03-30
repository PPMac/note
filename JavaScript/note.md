第一章 JavaScript概述
====================

1. 术语解释

ECMA:欧洲计算机制造协会



第二章 语法结构
==============

1. JavaScript是区分大小写的
2. 注释方式(和C一样):

    * //
    * /\*这里是注释内容\*/


3. 标识符(JavaScript中标识符用来对变量和函数进行命名)

标识符必须以字母, 下划线(\_),或美元符号($)开始。



第三章
======

1. JavaScipt的数据类型分为两种：原始类型和对象类型。

    * JavaScript的原始类型包括数字，字符串和布尔值。
    * JavsScript中有两个特殊的原始值: null和undefined
    * JavsScript中除了数字，字符串，布尔值，null和undefined就是对象了。
    * 如果函数用来初始化(new)一个对象, 我们称之为构造函数。
    * JavaScript中预定义的三种类： Date, RegExp, Exception
    * JavaScript有自己的内存管理机制，可以自动进行垃圾回收。
    * JavaScript的类型可以分为原始类型和对象类型，也可以分为拥有方法的类型和不能拥有方法的类型，
    * 同样可以分为可变类型和不可变类型。可变类型是指值可以修改的对象和数组属于可变类型。数字，字符串和布尔值属于不可变的类型。


2. 和其他语言不同，JavaScript不区分整数值和浮点值。JavaScript中的所有数字均用浮点值表示。

3. 数学运算

        ```javascript
        Math.pow(2, 10)    // => 1024; 2的10次幂
        Math.round(.6)     // => 1; 四舍五入
        Math.ceil(.6)      // => 1; 向上求整
        Math.floor(.6)     // => 0; 向下求整
        Math.abs(-5)       // => 5; 求绝对值
        Math.max(x, y, z)  // 求最大值
        Math.min(x, y, z)  // 求最小值
        Math.random()     // 生成一个大于等于0小于1.0的伪随机数
        Math.PI           // => 3.141592653589793 ; 圆周率
        Math.E             //自然对数的底数e
        Math.sqrt(9)       // => 3; 9的平方根
        ```


4. JavaScript中的算术运算在溢出时(overflow), 下溢(underflow), 或被0整除时不会报错。

当数字的运算结果超过了JavaScript所能表示的数字上限（溢出）时，结果为一个特殊的无穷大(infinity)的值。
在JavaScript中用Infinity表示。无穷大的值的行为特性与我们所期望的是一致的：基于他们的加减乘除都是无穷大。

被零整除在JavaScript中并不报错，它只是简单的返回无穷大(Infinity)或负无穷大(-Infinity)。但是有一个例外: 零除以零是没有意义的，它的结果是非数字值(not a number), 用NaN表示。
NaN有一点特殊，它与任何值都不等，包括它自身，也就是说，没法用 x == NaN来判断变量x是否是NaN,相反，应当使用x != x 来判断，当且仅当x为NaN时，表达式的结果才为true.

函数IsNaN()的作用与此类似,如果参数是NaN或者一个非数字，则返回true
函数IsFinite(), 在参数不是NaN, Infinity, -Infinity的时候才返回true

5. 日期和时间

        ```javascript
        var then = new Date(2012, 02,12);  // 月份是从0开始的，这里构建的日期是2012年03月12日。
        var now = new Date();  //当前日期和时间
        var elapsed = now - then // 日期减法： 计算日期间隔的毫秒数
        now.getFullYear();
        now.getMonth();    // 从0开始
        now.getDate();     // 得到日期
        now.getDay();      // 得到星期几， 星期日至星期六(0-6)
        ```


6. 字符串

        ```javascript
        var s = 'hello, world';
        s.length;   // 长度属性
        s.charAt(0);  // => 'h'; 第一个字符
        s.charAt(s.length-1);   // => 'd', 最后一个字符
        s.substring(1, 4);     // => 'ell',  第2到4个字符
        s.slice(1,4);          // 同上
        s.slice(-3)            // => 'rld'，最后3个字符
        s.indexOf('l');        // 第一次出现'l'的索引
        s.lastIndexOf('l');    // 最后一次出现'l'的索引
        s.indexOf('l', 3);     // '3' 在位置3及之后首次出现'l'字符的索引
        s.split(', ');         // ['hello', 'world'] , 分割成子串
        s.replace('h', 'H');    // 'Hello, world' 替换首次出现
        s.replace('l', 'L');   //   'heLlo, world'
        s.replace(/l/g, 'L');   // 全局替换 'heLLo,worLd'
        s.toUpperCase();        // 大写
        s[1]                    // 'e'
        ```

记住，在JavaScript字符串是固定不变的，类似`replace()`和`toUpperCase()`方法都是返回新的字符串，原字符串本身没有改变。


7. 模式匹配

尽管RegExp并不是JavaScript的基本类型，但是它依然具有直接量写法。可以直接在JavaScript中使用。在两条斜线之间的文本构成了一个正则表达式直接量。

    ```javascript
    var text="testing: 1,2,3";
    var pattern = /\d+/g;   // 匹配所有包含一个或多个数字的实例
    pattern.test(text);   // true
    text.search(pattern);  // 首次匹配成功的位置9
    text.match(pattern);   // ['1', '2', '3'] 所有匹配成功的数组
    text.replace(pattern, "#");  //  "testing: #,#,#"
    text.split(/\D+/);           // ["", "1", "2", "3"]
    ```


8. 布尔值

任意的JavaScipt值都可以被转换成布尔值。下面这些值都会被转换成false

* undefined
* null
* 0
* -0
* NaN
* ""  //空字符串

所有其它的值，包括所有的对象和数组都会转换为true.


9. null和undefined

null: 表示空值。
undefined: 表示变量没有初始化。

typeof null // "object"
typeof undefined  // "undefined"

null == undefined  // true
null === undefined // false

null和undefined都不包含任何方法和属性


10. 全局对象

* 全局属性：如：undefined, Infinity和NaN
* 全局函数：如： isNaN(), parseInt()
* 构造函数：如： Date(), RegExp(), String(), Object(), Array()
* 全局对象：如： Math, JSON


11. 包装对象

JavaScript对象是一种复合值：它是属性或已命名值得集合。通过'.'符号引用属性值。当属性值是一个函数的时候，称其为方法。

我们可以看到字符串也有属性和方法：

    ```javascript
    var s = 'hello, world';
    s.length;   // 长度属性
    s.charAt(0);  // => 'h'; 第一个字符
    ```

字符串既然不是对象，为什么它会有方法呢？ 只要引用了字符串s的属性，JavaScript就会将字符串值通过调用new String(s)的方法转换为对象，这个对象继承了字符串的方法。
并被用来处理属性引用。一旦属性引用结束，这个新创建的对象就会销毁（其实在实现上并不一定创建或销毁这个临时对象，然而整个过程可以看起来是这样）。

同字符串一样，数字和布尔值也是具有各种的方法：通过`Number()`和`Boolean()`构造函数创建一个临时对象。

null 和undefined没有包装对象：访问他们的属性会造成一个错误类型。

看如下代码：

    ```javascript
    var s = "hello";
    s.len = 5;
    var t = s.len;
    ```

当运行上面的代码时，t的值是undefined, 第二行代码创建一个临时字符串对象，并给其len属性赋值为5，随即销毁这个对象。第三行通过原始的字符串创建一个新的字符串对象，尝试读取它的len属性，这个属性当然不存在。

存取字符串，数字或布尔值时的属性时创建的对象称作包装对象。


12. 对象的比较并非值的比较： 即使两个对象包含同样的属性及同样的值，他们也是不相等的。各个索引元素完全相同的两个数组也是不相等的。

        ```javascript
        var o = {x:1}, p = {x:1}；
        o == p // false

        var a = [], b = [];
        a == b // false
        ```


对象的比较均是引用的比较：当且仅当两个对象引用一个基对象时，他们才相等。

    ```javascript
    var a= [];
    b = a;
    b[0] = 1;
    a[0]   // 1
    a == b  // true
    ```


13. 类型转换


表:

     值                 |     转换为字符串       |   数字     |   布尔值     |   对象
-----------------------------------------------------------------------------------------------------
undefined               |    "undefined"         |  NaN       |   false      |  throws TypeError
null                    |    "null"              |    0       |   false      |  throws TypeError
-----------------------------------------------------------------------------------------------------
true                    |    "true"              |    1       |              |  new Boolean(true)
false                   |    "false"             |    0       |              |  new Boolean(false)
-----------------------------------------------------------------------------------------------------
""(空字符串)            |                        |     0      |   false      |  new String("")
"1.2"(非空，数字)       |                        |    1.2     |   true       |  new String("1.2")
"one"(非空，非数字)     |                        |     NaN    |   true       |  new String("one")
-----------------------------------------------------------------------------------------------------
0                       |    “0”                 |            |   false      |  new Number(0)
-0                      |    “0”                 |            |   false      |  new Number(-0)
NaN                     |    “NaN”               |            |   false      |  new Number(NaN)
Infinity                |    "Infinity"          |            |   true       |  new Number(Infinity)
-Infinity               |    "-Infinity"         |            |   true       |  new Number(-Infinity)
1                       |     "1"                |            |   true       |  new Number(1)
-----------------------------------------------------------------------------------------------------
{}(任意对象)            |     见后面16           | 见后面16   |   true       |
[](任意数组)            |     ""                 |   0        |   true       |
[9](1个数字元素)        |     "9"                |   9        |   true       |
['a'](其他数组)         |     使用join()方法     |   NaN      |   true       |
function(){}(任意函数)  |     见后面16           |   NaN      |   ture       |
-----------------------------------------------------------------------------------------------------

从表中可以看出如下几点：

1. 对象的布尔值均是true
2. 当记不清一个值(x)转换为字符串，数字，布尔值的值时，可以用如下方法测试。

    * 检查转换为字符串: x + ""
    * 检查转换为数字: +x
    * 检查转换为布尔值 !!x


14. 转换和相等性

"==" 号操作符在判断两个值时是否相等时做了类型转换，而 "==="不会。


    ```javascript
    null == undefined  //两个值被认为相等
    "0"  == 0          // 比较之前两个值被转换为数字
    0 == false         //比较之前两个值被转换为布尔值
    "0"  == false      //比较之前两个值被转换为数字
    ```

需要说明的是, 一个值被转换为另一个值并不意味着两个值相等。比如，如果在期望使用布尔值的地方使用了unfefined的。它会转换为false, 但这不表明

    ```javascript
    undefinded == false // false
    ```


15. 显式转换

尽管JavaScript可以自动做很多类型转换，但是有时仍需要做显式转换。


    ```javascript
    Number("3")
    String(flase)
    Boolan([])
    Object(3)  // 等于 new Number(3)
    Object(null)  // 空对象
    Object(undefined)  // 空对象

    x + "" // 等价于 String(x)
    +x   // 等价于Number(x), 也可以写成x - 0
    !!x  // 等价于Boolean(x), 注意是双引号
    ```


数字转换为字符串


    ```javascript
    var n = 17;
    n.toString();   // n 转换为10进制的字符串
    n.toString(2);  // n 转换为2进制的字符串
    n.toString(16); // n 转换为16进制的字符串

    var n = 12345.678;
    n.toFixed(0);    //123456
    n.toFixed(2);    //123456.79
    n.toFixed(5);    //123456.78900
    n.toExponential(1);   //"1.2e+4"
    n.toPrecision(4);   // 123.5e+5
    n.toPrecision(7);   // 123456.8
    n.toPrecision(10);   // 123456.7890
    ```

* toFixed()根据小数点后的指导位数将数字转换为字符串， 它从不使用指数计数法
* toExponential()使用指数计数法将数字转换为指数形式的字符串
* toPrecision()根据指定的有效数字位数将数字转换为字符串，如果有效位数的数字少于数字的整数部分，则转换为指数形式。
* 三个方法都会适当的进行四舍五入或补充0.

如果通过Number()函数转换传入的一个字符串，它会试图将它转换为一个整数或浮点数直接量，这个方法只能用于十进制转换， 并且不能出现非法的尾随字符。
parseInt()和parseFloat()函数更加灵活。
parseInt()函数只解析整数，而parseFloat()可以解析整数和浮点数。
如果字符串前缀是“0x”或者“0X”， parseInt()会将其解析为16进制数。

parseInt()和parseFloat()都会跳过任意数量的前导空格，尽可能多的解析更多数值字符，并且忽略后面的内容，如果第一个非空格字符是非法的数字直接量，将返回结果NaN。

    ```javascript
    parseInt("3 aa bb");  // 3
    parseInt("    3.14 m")  // 3.14
    parseInt("-12.34")    // -12
    parseInt("0xff")    // 255
    parseInt("$12.34)   // NaN
    ```

parseInt可以接收第二个参数表示指定数字的转换基数

    ```javascript
    parseInt("11", 2)  // 3
    ```



16. 对象转换为原始值

对象到布尔值的转换非常简单，所有的对象（包括数组和函数）都转换为true。对于包装对象亦是如此: new Boolean(false)是一个对象而不是原始值，它将转换为true。

对象到字符串和对象到数字的转换都是通过调用待转换对象的一个方法来完成的。

JavaScript中的对象到字符串的转换经过了如下这些步骤。

* 如果对象具有toString()方法，则调用这个方法。如果它返回一个原始值，JavaScript将这个值转换为字符串（如果本身不是字符串的话）， 并返回这个字符串结果。

* 如果对象没有toString()方法，或者这个方法并不返回一个原始值，那么JavaScript会调用valueOf()方法。如果存在这个方法，则JavaScript调用它，如果返回值是原始值，
  JavaScript将这个值转换为字符串（如果本身不是字符串的话）， 并返回这个字符串结果。

* 否则，JavaScript无法从toString()或ValueOf()方法返回一个原始值，因此这时它将抛出一个类型错误异常。

在对象到数字的转换过程中，JavaScript做了同样的事情，只是它会首先尝试使用valueOf()方法。

* 如果对象具有valueOf()方法，则调用这个方法。如果它返回一个原始值，JavaScript将这个值转换为数字（如果本身不是数字的话）， 并返回这个数字结果。

* 如果对象没有valueOf()方法，或者这个方法并不返回一个原始值，那么JavaScript会调用toString()方法。如果存在这个方法，则JavaScript调用它，如果返回值是原始值，
  JavaScript将这个值转换为数字（如果本身不是数字的话）， 并返回这个数字结果。

* 否则，JavaScript无法从toString()或ValueOf()方法返回一个原始值，因此这时它将抛出一个类型错误异常。


对象转换为数字的细节解释了为什么空数组会被转换为数字0以及为什么单个元素的数组同样会转会成一个数字。

数组继承了默认的valueOf()方法，但这个方法返回一个对象而不是原始值，因此，数组到数字的转换会调用toString()方法。空数组转会为空字符串，空字符串转换为数字0.
含有一个元素的数组转换为字符串的结果和这个元素转换为数字的结果一样。如果数组只包含一个数字元素，这这个数字转换为字符串，再转换为数字。



17. 变量声明

使用关键字var

    ```javascript
    var a,
    var i=1, j=2
    ```

声明了一个变量，在给它存入值之前，它的初始值就是undefined


18. 变量作用域

一个变量的作用域(scope)是源程序代码中定义这个变量的区域。全局变量拥有全局作用域，函数内声明的变量只在函数内有定义。

在函数体内，局部变量的优先级高于同名变量的全局变量。如果在函数内声明一个局部变量或者在函数参数中带有的变量和全局变量同名，那么全局变量就被局部变量覆盖。

    ```javascript
    var scope = "global";

    function checscope() {
        var scope = "local";  // 局部变量覆盖全局变量
        return scope;
    }

    checkscope();   // "local"
    ```

尽管在全局作用域下声明全局变量可以不写var语句，但是声明局部变量时则必须使用var.

    ```javascript
    var scope = "global";

    function checscope2() {
        scope = "local";
        myscope = “local”;
        return [scope, myscope];
    }

    checkscope2();   // ["local", "local"]
    scope;    // "local"
    myscope;   // "local"
    ```


18. 函数作用域和声明提前

在一些类似C语言的编程语言中， 花括号内的每一段代码都有各自的作用域，而且变量在声明它们之前是不可见的，我们成为块级作用域(block scope)。
而JavaScript中没有块级作用域，取而代之JavaScript使用了函数作用域(function scope)： 变量在声明它们的函数体及这个函数体嵌套的任意函数体内部都是有定义的。


    ```javascript
    function test(){
        var i = 0;
        if (typeof o == 'object'){
            var j = 0;
            for (var k=0; k<10; k++){
                console.log(k);   // 0 -> 9
            }
            console.log(k);  // 10
        }
        console.log(j);    // 0
    }
    ```

JavaScript中所有的变量声明都会被提前到函数顶部，同时函数变量的初始化留在原来的位置。

    ```javascript
    var scope = "global";
    function f() {
        console.log(scope);   // undefined, 而不是global
        var scope = "local";
        console.log(scope);  // local
    }
    ```

19. 作为属性的变量

当声明一个JavaScipt的全局变量时，实际上是定义了一个全局对象的属性。
当使用var声明一个变量时，创建的这个对象是不可配置的， 也就是说无法通过delete运算符删除。
没有使用var时创建的变量是可配置的.

    ```javascript
    var truevar = 1; //声明一个不可删除的全局变量
    fakevar = 2; // 创建全局对象的一个可删除属性
    this.fakevar2 = 2; // 同上
    delete truevar;  // false, 变量并没有被删除
    delete fakevar;  // true, 变量被删除
    delete this.fakevar2;  // true, 变量被删除
    ```
