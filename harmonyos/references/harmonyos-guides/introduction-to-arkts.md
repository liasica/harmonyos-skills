---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts
title: ArkTS语言介绍
breadcrumb: 指南 > 基础入门 > 学习ArkTS语言 > ArkTS语言介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:35+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:937689a36ead05035a369f19f9fbdd138c46ca8eac222ffe12a9e27417b0cef5
---

ArkTS是一种设计用于构建高性能应用的编程语言。它在继承TypeScript语法的基础上进行了优化，以提供更高的性能和开发效率。

许多编程语言在设计之初未考虑移动设备，导致应用运行缓慢、低效且功耗大。随着移动设备在日常生活中越来越普遍，针对移动环境的编程语言优化需求日益增加。ArkTS专为解决这些问题而设计，聚焦提高运行效率。

TypeScript是在JavaScript基础上通过添加类型定义扩展而来的，ArkTS则是TypeScript的进一步扩展。TypeScript提供了一种更结构化的JavaScript编码方法，深受开发者喜爱。ArkTS保持了TypeScript的大部分语法，旨在为现有的TypeScript开发者提供高度兼容的体验，帮助移动开发者快速上手。

ArkTS的一大特性是它专注于低运行时开销。ArkTS对TypeScript的动态类型特性施加了更严格的限制，以减少运行时开销，提高执行效率。通过取消动态类型特性，ArkTS代码能更有效地被运行前编译和优化，从而实现更快的应用启动和更低的功耗。

ArkTS语言设计中考虑了与TypeScript和JavaScript的互通性。许多移动应用开发者希望重用TypeScript和JavaScript代码及库，因此ArkTS提供与TypeScript和JavaScript的无缝互通，使开发者可以轻松集成TypeScript和JavaScript代码到应用中，充分利用现有代码和库进行ArkTS开发。

本教程将指导开发者了解ArkTS的核心功能、语法和最佳实践，助力开发者使用ArkTS高效构建高性能的移动应用。

如需详细了解ArkTS语言，请参阅[ArkTS具体指南](arkts-overview.md)和[DevEco Studio](ide-tools-overview.md)。

## 基本知识

### 声明

ArkTS通过声明引入变量、常量、类型和函数。

**变量声明**

使用关键字let声明的变量可以在程序执行期间具有不同的值。

```
1. let hi: string = 'hello';
2. hi = 'hello, world';
```

**常量声明**

使用关键字const声明的常量为只读类型，只能被赋值一次。

```
1. const hello: string = 'hello';
```

对常量重新赋值会造成编译时错误。

**自动类型推断**

如果变量或常量的声明包含初始值，开发者无需显式指定类型，因为ArkTS规范已列举了所有允许自动推断类型的场景。

以下示例中，两条声明语句都是有效的，两个变量都是string类型：

```
1. let hi1: string = 'hello';
2. let hi2 = 'hello, world';
```

### 类型

**基本类型和引用类型**

基本数据类型包括number、string等简单类型，它们可以准确地表示单一的数据类型。对基本类型的存储和访问都是直接的，比较时直接比较其值。

引用类型包括对象、数组和函数等复杂数据结构。这些类型通过引用访问数据，对象和数组可以包含多个值或键值对，函数则可以封装可执行的代码逻辑。引用类型在内存中通过指针访问数据，修改引用会影响原始数据。

**number类型**

ArkTS提供number类型，任何整数和浮点数都可以被赋给此类型的变量。

数字字面量包括整数字面量和十进制浮点数字面量。

整数字面量包括以下类别：

* 十进制整数，由数字序列组成。例如：0、117、-345。
* 十六进制整数，以0x（或0X）开头，包含数字（0-9）和字母a-f或A-F。例如：0x1123、0x00111、-0xF1A7。
* 八进制整数，以0o（或0O）开头，只能包含数字（0-7）。例如：0o777。
* 二进制整数，以0b（或0B）开头，只能包含数字0和1。例如：0b11、0b0011、-0b11。

浮点数字面量包括以下部分：

* 十进制整数，可为有符号数（前缀为“+”或“-”）。
* 小数点（“.”）。
* 小数部分（由十进制数字字符串表示）。
* 指数部分，以“e”或“E”开头，后跟有符号（前缀为“+”或“-”）或无符号整数。

示例：

```
1. let n1 = 3.14;
2. let n2 = 3.141592;
3. let n3 = 0.5;
4. let n4 = 1e2;

6. function factorial(n: number): number {
7. if (n <= 1) {
8. return 1;
9. }
10. return n * (n - 1);
11. }
12. // ...
13. factorial(n1) // 6.719600000000001
14. factorial(n2) // 6.728008294464001
15. factorial(n3) // 1
16. factorial(n4) // 9900
```

number类型在表示大整数（即超过-9007199254740991~9007199254740991）时会造成精度丢失。在开发时可以按需使用bigint类型来确保精度：

```
1. let bigInt: bigint = 999999999999999999999999999999999999999999999999999999999999n;
2. console.info('bigInt:' + bigInt.toString());
```

**boolean类型**

boolean类型由true和false两个逻辑值组成。

通常在条件语句中使用boolean类型的变量：

```
1. let isDone: boolean = false;

3. // ...

5. if (isDone) {
6. console.info('Done!');
7. }
```

**string类型**

string类型代表字符序列，可以使用转义字符来表示字符。

字符串字面量由单引号（'）或双引号（"）之间括起来的零个或多个字符组成。字符串字面量还有一特殊形式，是用反向单引号（`）括起来的模板字面量。

```
1. let s1 = 'Hello, world!\n';
2. let s2 = 'this is a string';
3. let a = 'Success';
4. let s3 = `The result is ${a}`;
```

**void类型**

void类型用于指定函数没有返回值。

此类型只有一个值，同样是void。由于void是引用类型，因此它可以用于泛型类型参数。

```
1. class Class<T> {
2. // ...
3. }
4. let instance: Class<void>;
```

**Object类型**

Object类型是所有引用类型的基类型。任何值，包括基本类型的值，都可以直接被赋给Object类型的变量（基本类型值会被自动装箱）。

object类型用于表示除基本类型外的类型。

```
1. let o1: Object = 'Alice';
2. let o2: Object = ['a', 'b'];
3. let o3: Object = 1;
4. let o4: object = [1, 2, 3];
```

**array类型**

array类型，即数组，是由可赋值给数组声明中指定的元素类型的数据组成的对象。

数组可由数组复合字面量赋值。数组复合字面量是用方括号括起来的零个或多个表达式列表，每个表达式为数组中的一个元素。数组的长度由数组中元素的个数确定。数组中第一个元素的索引为0。

以下示例将创建包含三个元素的数组：

```
1. let names: string[] = ['Alice', 'Bob', 'Carol'];
```

**enum类型**

enum类型，即枚举类型，是预先定义的一组命名值的值类型，其中命名值又称为枚举常量。

使用枚举常量时必须以枚举类型名称为前缀。

```
1. enum ColorSet { Red, Green, Blue }
2. let c: ColorSet = ColorSet.Red;
```

常量表达式用于显式设置枚举常量的值。

```
1. enum ColorSet { White = 0xFF, Grey = 0x7F, Black = 0x00 }
2. let c: ColorSet = ColorSet.Black;
```

**Union类型**

Union类型，即联合类型，是由多个类型组合成的引用类型。联合类型包含了变量可能的所有类型。

```
1. class Cat {
2. public name: string = 'cat';
3. // ...
4. }

6. class Dog {
7. public name: string = 'dog';
8. // ...
9. }

11. class Frog {
12. public name: string = 'frog';
13. // ...
14. }

16. type Animal = Cat | Dog | Frog | number | string | null | undefined;
17. // Cat、Dog、Frog是一些类型（类或接口）

19. let animal: Animal = new Cat();
20. animal = new Frog();
21. animal = 42;
22. animal = 'dog';
23. animal = undefined;
24. // 可以将类型为联合类型的变量赋值为任何组成类型的有效值
```

可以使用不同机制获取联合类型中的特定类型值。

示例：

```
1. class Cat { sleep () {}; meow () {} }
2. class Dog { sleep () {}; bark () {} }
3. class Frog { sleep () {}; leap () {} }

5. type Animal = Cat | Dog | Frog;

7. function foo(animal: Animal) {
8. if (animal instanceof Frog) {  // 判断animal是否是Frog类型
9. animal.leap();  // animal在这里是Frog类型
10. }
11. animal.sleep(); // Animal具有sleep方法
12. }
```

**Aliases类型**

Aliases类型为匿名类型（如数组、函数、对象字面量或联合类型）提供名称，或为已定义的类型提供替代名称。

```
1. // 二维数组类型
2. type Matrix = number[][];
3. const gameBoard: Matrix = [
4. [1, 0],
5. [0, 1]
6. ];

8. // 函数类型
9. type Handler = (s: string, no: number) => string;
10. const repeatString: Handler = (str, times) => {
11. return str.repeat(times);
12. };
13. console.info(repeatString('abc', 3)); // 'abcabcabc'
14. // ...
15. // 泛型函数类型
16. type Predicate<T> = (x: T) => boolean;
17. const isEven: Predicate<number> = (num) => num % 2 === 0;

19. // 可为空的对象类型
20. type NullableObject = Object | null;

22. class Cat {
23. }

25. let animalData: NullableObject = new Cat();
26. let emptyData: NullableObject = null;
```

### 运算符

**赋值运算符**

赋值运算符=，使用方式如x=y。

复合赋值运算符将赋值与运算符组合在一起，例如：a += b 等价于 a = a + b，

其中的 += 即为复合赋值运算符

复合赋值运算符包括：+=、-=、\*=、/=、%=、<<=、>>=、>>>=、&=、|=、^=。

**比较运算符**

| 运算符 | 说明 |
| --- | --- |
| === | 如果两个操作数严格相等（对于不同类型的操作数认为是不相等的），则返回true。 |
| !== | 如果两个操作数严格不相等（对于不同类型的操作数认为是不相等的），则返回true。 |
| == | 如果两个操作数相等，则返回true。 |
| != | 如果两个操作数不相等，则返回true。 |
| > | 如果左操作数大于右操作数，则返回true。 |
| >= | 如果左操作数大于或等于右操作数，则返回true。 |
| < | 如果左操作数小于右操作数，则返回true。 |
| <= | 如果左操作数小于或等于右操作数，则返回true。 |

===与==的区别：

```
1. // ==只比较目标的值相等
2. console.info(String(null == undefined)); // true
3. // ===比较目标的值和类型都相等
4. console.info(String(null === undefined)); // false
```

**算术运算符**

一元运算符包括：-、+、--、++。

二元运算符列举如下：

| 运算符 | 说明 |
| --- | --- |
| + | 加法 |
| - | 减法 |
| \* | 乘法 |
| / | 除法 |
| % | 除法后余数 |

**位运算符**

| 运算符 | 说明 |
| --- | --- |
| a & b | 按位与：如果两个操作数的对应位都为1，则将这个位设置为1，否则设置为0。 |
| a | b | 按位或：如果两个操作数的相应位中至少有一个为1，则将这个位设置为1，否则设置为0。 |
| a ^ b | 按位异或：如果两个操作数的对应位不同，则将这个位设置为1，否则设置为0。 |
| ~ a | 按位非：反转操作数的位。 |
| a << b | 左移：将a的二进制表示向左移b位。 |
| a >> b | 算术右移：将a的二进制表示向右移b位，带符号扩展。 |
| a >>> b | 逻辑右移：将a的二进制表示向右移b位，左边补0。 |

**逻辑运算符**

| 运算符 | 说明 |
| --- | --- |
| a && b | 逻辑与 |
| a || b | 逻辑或 |
| ! a | 逻辑非 |

**instanceof运算符**

instanceof运算符用于在运行时检查一个对象是否是指定类或其子类的实例。

示例如下：

```
1. obj instanceof className
```

返回值类型为boolean。

如果obj是className类或其子类的实例，则返回值为true；否则，返回值为false。

示例：

```
1. class Person {}
2. const person = new Person();
3. if ((person instanceof Person)) {
4. console.info('true'); // true
5. }

7. class Animal {}
8. class Bird extends Animal {}
9. const bird = new Bird();
10. if (bird instanceof Animal) {
11. console.info('true'); // true
12. }
```

### 语句

**if语句**

if语句用于需要根据逻辑条件执行不同语句的场景。当逻辑条件为真时，执行对应的一组语句，否则执行另一组语句（如果有的话）。

else部分也可以包含if语句。

if语句如下所示：

```
1. if (condition1) {
2. // 语句1
3. } else if (condition2) {
4. // 语句2
5. } else {
6. // else语句
7. }
```

条件表达式可以是任何类型，非boolean类型会进行隐式类型转换：

```
1. let s1 = 'Hello';
2. if (s1) {
3. console.info(s1); // 打印"Hello"
4. }

6. let s2 = 'World';
7. if (s2.length != 0) {
8. console.info(s2); // 打印"World"
9. }
```

**switch语句**

使用switch语句执行与switch表达式值匹配的代码块。

switch语句如下所示：

```
1. switch (expression) {
2. case label1: // 如果label1匹配,则执行
3. // ...
4. // 语句1
5. // ...
6. break; // 可省略
7. case label2:
8. case label3: // 如果label2或label3匹配,则执行
9. // ...
10. // 语句23
11. // ...
12. break; // 可省略
13. default:
14. // 默认语句
15. }
```

如果switch表达式的值等于某个label的值，则执行相应的语句。

如果没有任何一个label值与表达式值相匹配，并且switch具有default子句，那么程序会执行default子句对应的代码块。

break语句（可选的）允许跳出switch语句并继续执行switch语句之后的语句。

如果没有break语句，则执行switch中的下一个label对应的代码块。

**条件表达式**

条件表达式根据第一个表达式的布尔值来返回其他两个表达式之一的结果。

示例如下：

```
1. condition ? expression1 : expression2
```

如果condition的值为真值（转换后为true的值），则使用expression1作为该表达式的结果；否则，使用expression2作为该表达式的结果。

示例：

```
1. let message = Math.random() > 0.5 ? 'Valid' : 'Failed';
```

condition如果是非bool值则会进行隐式转换。

示例：

```
1. console.info('a' ? 'true' : 'false'); // true
2. console.info('' ? 'true' : 'false'); // false
3. console.info(1 ? 'true' : 'false'); // true
4. console.info(0 ? 'true' : 'false'); // false
5. console.info(null ? 'true' : 'false'); // false
6. console.info(undefined ? 'true' : 'false'); // false
```

**for语句**

for语句会被重复执行，直到循环退出语句值为false。

for语句如下所示：

```
1. for ([init]; [condition]; [update]) {
2. statements
3. }
```

for语句的执行流程如下：

1、 执行init表达式（如有）。此表达式通常初始化一个或多个循环计数器。

2、 计算condition。如果它为真值（转换后为true的值），则执行循环主体的语句。如果它为假值（转换后为false的值），则for循环终止。

3、 执行循环主体的语句。

4、 如果有update表达式，则执行该表达式。

5、 返回步骤2。

示例：

```
1. let sum = 0;
2. for (let i = 0; i < 10; i += 2) {
3. sum += i;
4. }
```

**for-of语句**

使用for-of语句可遍历数组、Set、Map、字符串等可迭代的类型。示例如下：

```
1. for (forVar of IterableExpression) {
2. // process forVar
3. }
```

示例：

```
1. for (let ch of 'a string object') {
2. console.info(ch);
3. // ...
4. }
```

**while语句**

只要condition为真值（转换后为true的值），while语句就会执行statements语句。示例如下：

```
1. while (condition) {
2. statements
3. }
```

示例：

```
1. let n = 0;
2. let x = 0;
3. while (n < 3) {
4. n++;
5. x += n;
6. }
```

**do-while语句**

如果condition的值为真值（转换后为true的值），那么statements语句会重复执行。示例如下：

```
1. do {
2. statements
3. } while (condition)
```

示例：

```
1. let i = 0;
2. do {
3. i += 1;
4. } while (i < 10)
```

**break语句**

使用break语句可以终止循环语句或switch。

示例：

```
1. let x = 0;
2. while (true) {
3. x++;
4. if (x > 5) {
5. break;
6. }
7. }
```

如果break语句后带有标识符，则将控制流转移到该标识符所包含的语句块之外。

示例：

```
1. let x = 1;
2. label: while (true) {
3. switch (x) {
4. case 1:
5. // statements
6. break label; // 中断while语句
7. }
8. }
```

**continue语句**

continue语句会停止当前循环迭代的执行，并将控制传递给下一次迭代。

示例：

```
1. let sum = 0;
2. for (let x = 0; x < 100; x++) {
3. if (x % 2 == 0) {
4. continue;
5. }
6. sum += x;
7. }
```

**throw和try语句**

throw语句用于抛出异常或错误：

```
1. throw new Error('this error')
```

try语句用于捕获和处理异常或错误：

```
1. try {
2. // ...
3. } catch (e) {
4. // 异常处理
5. // ...
6. }
```

下面的示例中throw和try语句用于处理除数为0的错误：

```
1. class ZeroDivisor extends Error {}

3. function divide (a: number, b: number): number {
4. if (b == 0) {
5. throw new ZeroDivisor();
6. }
7. return a / b;
8. }

10. function process(a: number, b: number) {
11. try {
12. let res = divide(a, b);
13. console.info('result: ' + res);
14. } catch (x) {
15. console.error('some error');
16. }
17. }
```

支持finally语句：

```
1. function processData(s: string) {
2. let error: Error | null = null;

4. try {
5. console.info('Data processed: ' + s);
6. // ...
7. // 可能发生异常的语句
8. // ...
9. } catch (e) {
10. error = e as Error;
11. // ...
12. // 异常处理
13. // ...
14. } finally {
15. // 无论是否发生异常都会执行的代码
16. if (error != null) {
17. console.error(`Error caught: input='${s}', message='${error.message}'`);
18. }
19. }
20. }
```

## 函数

### 函数声明

函数声明引入一个函数，包含其名称、参数列表、返回类型和函数体。

以下示例是一个简单的函数和它的语法语义说明：

1.参数类型标注：x: string, y: string 显式声明参数类型为字符串类型。

2.返回值类型：: string 指定函数返回值为字符串类型。

```
1. function add(x: string, y: string): string {
2. let z: string = `${x} ${y}`;
3. return z;
4. }
```

在函数声明中，必须为每个参数标记类型。如果参数为可选参数，那么允许在调用函数时省略该参数。函数的最后一个参数可以是rest参数。

### 可选参数

可选参数的格式可为name?: Type。

```
1. function hello(name?: string) {
2. if (name == undefined) {
3. console.info('Hello!');
4. } else {
5. console.info(`Hello, ${name}!`);
6. }
7. }
```

可选参数的另一种形式为设置的参数默认值。如果在函数调用中这个参数被省略了，则会使用此参数的默认值作为实参。

```
1. function multiply(n: number, coeff: number = 2): number {
2. return n * coeff;
3. }
4. // ...
5. multiply(2);  // 返回2*2
6. multiply(2, 3); // 返回2*3
```

### rest参数

函数的最后一个参数可以是rest参数，格式为...restName: Type[]。rest参数允许函数接收一个不定长数组，用于处理不定数量的参数输入。

```
1. function sum(...numbers: number[]): number {
2. let res = 0;
3. for (let n of numbers) {
4. res += n;
5. }
6. return res;
7. }
8. // ...
9. sum(); // 返回0
10. sum(1, 2, 3); // 返回6
```

### 返回类型

如果可以从函数体内推断出函数返回类型，则可在函数声明中省略标注返回类型。

```
1. // 显式指定返回类型
2. function foo(): string { return 'foo'; }

4. // 推断返回类型为string
5. function goo() { return 'goo'; }
```

不需要返回值的函数的返回类型可以显式指定为void或省略标注。这类函数不需要返回语句。

以下示例中两种函数声明方式都是有效的：

```
1. function hi1() { console.info('hi'); }
2. function hi2(): void { console.info('hi'); }
```

### 函数的作用域

函数中定义的变量和其他实例仅可以在函数内部访问，不能从外部访问。

如果函数中定义的变量与外部作用域中已有实例同名，则函数内的局部变量定义将覆盖外部定义。

```
1. let outerVar = 'I am outer ';

3. function func() {
4. let outerVar = 'I am inside';
5. console.info(outerVar); // 输出: I am inside
6. }
7. // ...
8. func();
```

### 函数调用

调用函数以执行其函数体，实参值会赋值给函数的形参。

如果函数定义如下：

```
1. function join(x: string, y: string): string {
2. let z: string = `${x} ${y}`;
3. return z;
4. }
```

则此函数的调用需要包含两个string类型的参数：

```
1. let x = join('hello', 'world');
2. console.info(x); // 输出: hello world
```

### 函数类型

函数类型通常用于定义回调函数：

```
1. type trigFunc = (x: number) => number // 这是一个函数类型

3. function doAction(f: trigFunc) {
4. f(3.141592653589); // 调用函数
5. }

7. doAction(Math.sin); // 将函数作为参数传入
```

### 箭头函数（又名Lambda函数）

函数可以定义为箭头函数，例如：

```
1. let sum = (x: number, y: number): number => {
2. return x + y;
3. }
```

箭头函数的返回类型可以省略，此时返回类型从函数体推断。

表达式可以指定为箭头函数，使表达更简短，因此以下两种表达方式是等价的：

```
1. let sum1 = (x: number, y: number) => { return x + y; }
2. let sum2 = (x: number, y: number) => x + y
```

### 闭包

闭包是由函数及声明该函数的环境组合而成的。该环境包含了这个闭包创建时作用域内的任何局部变量。

在下例中，f函数返回了一个闭包，它捕获了count变量，每次调用z，count的值会被保留并递增。

```
1. function f(): () => number {
2. let count = 0;
3. let g = (): number => { count++; return count; };
4. return g;
5. }
6. // ...
7. let z = f();
8. z(); // 返回：1
9. z(); // 返回：2
```

### 函数重载

可以通过编写重载，指定函数的不同调用方式。具体方法是，为同一个函数写入多个同名但签名不同的函数头，函数实现紧随其后。

```
1. function foo1(x: number): void;            /* 第一个函数定义 */
2. function foo1(x: string): void;            /* 第二个函数定义 */
3. function foo1(x: number | string): void {  /* 函数实现 */
4. }

6. foo1(123);     // OK，使用第一个定义
7. foo1('aa'); // OK，使用第二个定义
```

不允许重载函数有相同的参数列表，否则将导致编译错误。

## 类

类声明引入一个新类型，并定义其字段、方法和构造函数。

在以下示例中，定义了Person类，该类具有字段name和surname、构造函数和方法fullName：

```
1. class Person {
2. public name: string = '';
3. public surname: string = '';
4. constructor (n: string, sn: string) {
5. this.name = n;
6. this.surname = sn;
7. }
8. fullName(): string {
9. return this.name + ' ' + this.surname;
10. }
11. }
```

定义类后，可以使用关键字new创建实例：

```
1. let p = new Person('John', 'Smith');
2. console.info(p.fullName());
```

或者，可以使用对象字面量创建实例：

```
1. class Point {
2. public x: number = 0;
3. public y: number = 0;
4. }
5. let p: Point = {x: 42, y: 42};
```

### 字段

字段是直接在类中声明的某种类型的变量。

类可以具有实例字段或者静态字段。

**实例字段**

实例字段存在于类的每个实例上。每个实例都有自己的实例字段集合。

要访问实例字段，需要使用类的实例。

```
1. class Person1 {
2. public name: string = '';
3. public age: number = 0;
4. constructor(n: string, a: number) {
5. this.name = n;
6. this.age = a;
7. }

9. getName(): string {
10. return this.name;
11. }
12. }
13. // ...
14. let p1 = new Person1('Alice', 25);
15. p1.name; // Alice
16. let p2 = new Person1('Bob', 28);
17. p2.getName(); // Bob
```

**静态字段**

使用关键字static将字段声明为静态。静态字段属于类本身，类的所有实例共享一个静态字段。

要访问静态字段，需要使用类名：

```
1. class Person2 {
2. public static numberOfPersons = 0;
3. constructor() {
4. // ...
5. Person2.numberOfPersons++;
6. // ...
7. }
8. }

10. Person2.numberOfPersons;
```

**字段初始化**

为了减少运行时错误并提升执行性能，ArkTS要求所有字段在声明时或构造函数中显式初始化，与标准TS的strictPropertyInitialization模式相同。

以下代码在ArkTS中不合法。

```
1. class Person {
2. name: string; // undefined

4. setName(n: string): void {
5. this.name = n;
6. }

8. getName(): string {
9. // 开发者使用"string"作为返回类型，这隐藏了name可能为"undefined"的事实。
10. // 更合适的做法是将返回类型标注为"string | undefined"，以告诉开发者这个API所有可能的返回值。
11. return this.name;
12. }
13. }

15. let jack = new Person();
16. // 假设代码中没有对name赋值，即没有调用"jack.setName('Jack')"
17. jack.getName().length; // 运行时异常：name is undefined
```

在ArkTS中，开发者应该这样写代码。

```
1. class Person3 {
2. public name: string = '';

4. setName(n: string): void {
5. this.name = n;
6. }

8. // 类型为'string'，不可能为"null"或者"undefined"
9. getName(): string {
10. return this.name;
11. }
12. }

15. let jack = new Person3();
16. // 假设代码中没有对name赋值，即没有调用"jack.setName('Jack')"
17. jack.getName().length; // 0, 没有运行时异常
```

接下来的代码示例展示了当name的值可能为undefined时，如何正确编写代码。

```
1. class Person {
2. name?: string; // 可能为`undefined`

4. setName(n: string): void {
5. this.name = n;
6. }

8. // 编译时错误：name可以是"undefined"，所以这个API的返回值类型不能仅定义为string类型
9. getNameWrong(): string {
10. return this.name;
11. }

13. getName(): string | undefined { // 返回类型匹配name的类型
14. return this.name;
15. }
16. }

18. let jack = new Person();
19. // 假设代码中没有对name赋值，即没有调用"jack.setName('Jack')"

21. // 编译时错误：编译器认为下一行代码有可能会访问undefined的属性，报错
22. jack.getName().length;  // 编译失败

24. jack.getName()?.length; // 编译成功，没有运行时错误
```

**getter和setter**

setter和getter可用于提供对类属性的受控访问。

在以下示例中，setter用于禁止将\_age属性设置为无效值：

```
1. class Person4 {
2. public name: string = '';
3. private _age: number = 0;
4. get age(): number { return this._age; }
5. set age(x: number) {
6. if (x < 0) {
7. throw Error('Invalid age argument');
8. }
9. this._age = x;
10. }
11. }
12. // ...
13. let p = new Person4();
14. p.age; // 输出0
15. // ...
16. p.age = -42; // 设置无效age值会抛出错误
```

在类中可以定义getter或者setter。

### 方法

方法属于类。类可以定义实例方法或者静态方法。静态方法属于类本身，只能访问静态字段。而实例方法既可以访问静态字段，也可以访问实例字段，包括类的私有字段。

**实例方法**

以下示例说明了实例方法的工作原理。

calculateArea方法计算矩形面积：

```
1. class RectangleSize {
2. private height: number = 0;
3. private width: number = 0;
4. constructor(height: number, width: number) {
5. this.height = height;
6. this.width = width;
7. }
8. calculateArea(): number {
9. return this.height * this.width;
10. }
11. }
```

必须通过类的实例调用实例方法：

```
1. let square = new RectangleSize(10, 10);
2. square.calculateArea(); // 输出：100
```

**静态方法**

使用关键字 static 声明静态方法。静态方法属于类，只能访问静态字段。

静态方法定义了类作为一个整体的公共行为。

必须通过类名调用静态方法：

```
1. class C2 {
2. public static staticMethod(): string {
3. return 'this is a static method.';
4. }
5. }
6. // ...
7. console.info(C2.staticMethod());
```

**继承**

一个类可以继承另一个类（称为基类），并使用以下语法实现多个接口：

```
1. class [extends BaseClassName] [implements listOfInterfaces] {
2. // ...
3. }
```

继承类继承基类的字段和方法，但不继承构造函数。继承类可以新增定义字段和方法，也可以覆盖其基类定义的方法。

基类也称为“父类”或“超类”。继承类也称为“派生类”或“子类”。

示例：

```
1. class Person5 {
2. public name: string = '';
3. public _age = 0;
4. get age(): number {
5. return this._age;
6. }
7. }
8. class Employee extends Person5 {
9. public salary: number = 0;
10. calculateTaxes(): number {
11. return this.salary * 0.42;
12. }
13. }
```

包含implements子句的类必须实现列出的接口中定义的所有方法，但使用默认实现定义的方法除外。

```
1. interface DateInterface {
2. now(): string;
3. }
4. class MyDate implements DateInterface {
5. now(): string {
6. // 在此实现
7. return 'now';
8. }
9. }
```

**父类访问**

关键字super可用于访问父类的方法和构造函数。在实现子类功能时，可以通过该关键字从父类中获取所需接口：

```
1. class RectangleSize {
2. protected height: number = 0;
3. protected width: number = 0;

5. constructor (h: number, w: number) {
6. this.height = h;
7. this.width = w;
8. }

10. draw() {
11. /* 绘制边界 */
12. }
13. }
14. class FilledRectangle extends RectangleSize {
15. public color = ''
16. constructor (h: number, w: number, c: string) {
17. super(h, w); // 父类构造函数的调用
18. this.color = c;
19. }

21. draw() {
22. super.draw(); // 父类方法的调用
23. /* 填充矩形 */
24. }
25. }
```

**方法重写**

子类可以重写其父类中定义的方法的实现。重写的方法必须具有与原始方法相同的参数类型和相同或派生的返回类型。

```
1. class RectangleSize {
2. // ...
3. area(): number {
4. // 实现
5. return 0;
6. }
7. }
8. class Square extends RectangleSize {
9. private side: number = 0;
10. area(): number {
11. return this.side * this.side;
12. }
13. }
```

**方法重载签名**

通过重载签名，指定方法的不同调用。具体方法为，为同一个方法写入多个同名但签名不同的方法头，方法实现紧随其后。

```
1. class C {
2. foo(x: number): void;            /* 第一个签名 */
3. foo(x: string): void;            /* 第二个签名 */
4. foo(x: number | string): void {  /* 实现签名 */
5. }
6. }
7. let c = new C();
8. c.foo(123);     // OK，使用第一个签名
9. c.foo('aa'); // OK，使用第二个签名
```

如果两个重载签名的名称和参数列表均相同，则为错误。

### 构造函数

类声明可以包含用于初始化对象状态的构造函数。

构造函数定义如下：

```
1. constructor ([parameters]) {
2. // ...
3. }
```

如果未定义构造函数，则会自动创建具有空参数列表的默认构造函数，例如：

```
1. class Point {
2. public x: number = 0;
3. public y: number = 0;
4. }
5. let p = new Point();
```

在这种情况下，默认构造函数使用字段类型的默认值初始化实例中的字段。

**派生类的构造函数**

构造函数函数体的第一条语句可以使用关键字super来显式调用直接父类的构造函数。

```
1. class RectangleSize {
2. constructor(width: number, height: number) {
3. // ...
4. }
5. }
6. class Square extends RectangleSize {
7. constructor(side: number) {
8. super(side, side);
9. }
10. }
```

**构造函数重载签名**

可以通过编写重载签名，指定构造函数的不同调用方式。具体方法是，为同一个构造函数写入多个同名但签名不同的构造函数头，构造函数实现紧随其后。

```
1. class C {
2. constructor(x: number)             /* 第一个签名 */
3. constructor(x: string)             /* 第二个签名 */
4. constructor(x: number | string) {  /* 实现签名 */
5. }
6. }
7. let c1 = new C(123);      // OK，使用第一个签名
8. let c2 = new C('abc');    // OK，使用第二个签名
```

如果两个重载签名的名称和参数列表均相同，则为错误。

### 可见性修饰符

类的方法和属性都可以使用可见性修饰符。

可见性修饰符包括：private、protected和public。默认可见性为public。

**Public（公有）**

public修饰的类成员（字段、方法、构造函数）在程序的任何可访问该类的地方都是可见的。

**Private（私有）**

private修饰的成员不能在声明该成员的类之外访问，例如：

```
1. class C {
2. public x: string = '';
3. private y: string = '';
4. set_y (new_y: string) {
5. this.y = new_y; // OK，因为y在类本身中可以访问
6. }
7. }
8. let c = new C();
9. c.x = 'a'; // OK，该字段是公有的
10. c.y = 'b'; // 编译时错误：'y'不可见
```

**Protected（受保护）**

protected修饰符的作用与private修饰符非常相似，不同点是protected修饰的成员允许在派生类中访问，例如：

```
1. class Base {
2. protected x: string = '';
3. private y: string = '';
4. }
5. class Derived extends Base {
6. foo() {
7. this.x = 'a'; // OK，访问受保护成员
8. this.y = 'b'; // 编译时错误，'y'不可见，因为它是私有的
9. }
10. }
```

### 对象字面量

对象字面量是一个表达式，可用于创建类实例并提供一些初始值。它在某些情况下更方便，可以用来代替new表达式。

对象字面量的表示方式是：封闭在花括号对({})中的'属性名：值'的列表。

```
1. class C {
2. public n: number = 0;
3. public s: string = '';
4. }

6. let c: C = {n: 42, s: 'foo'};
```

ArkTS是静态类型语言，如上述示例所示，对象字面量只能在可以推导出该字面量类型的上下文中使用。其他正确的例子如下所示：

```
1. class C1 {
2. public n: number = 0;
3. public s: string = '';
4. }

6. function foo(c1: C1) {}

8. let c1: C1

10. c1 = {n: 42, s: 'foo'};  // 使用变量的类型
11. foo({n: 42, s: 'foo'}); // 使用参数的类型

13. function bar(): C1 {
14. return {n: 42, s: 'foo'}; // 使用返回类型
15. }
```

也可以在数组元素类型或类字段类型中使用：

```
1. class C {
2. public n: number = 0;
3. public s: string = '';
4. }
5. let cc: C[] = [{n: 1, s: 'a'}, {n: 2, s: 'b'}];
```

**Record类型的对象字面量**

泛型Record<K, V>用于将类型（键类型）的属性映射到另一个类型（值类型）。常用对象字面量来初始化该类型的值：

```
1. let map: Record<string, number> = {
2. 'John': 25,
3. 'Mary': 21
4. };
5. // ...
6. map['John']; // 25
```

类型K可以是字符串类型或数值类型(不包括bigint)，而V可以是任何类型。

```
1. interface PersonInfo {
2. age: number;
3. salary: number;
4. }
5. let map: Record<string, PersonInfo> = {
6. 'John': { age: 25, salary: 10},
7. 'Mary': { age: 21, salary: 20}
8. }
```

### 抽象类

带有abstract修饰符的类称为抽象类。抽象类可用于表示一组更具体的概念所共有的概念。

尝试创建抽象类的实例会导致编译错误：

```
1. abstract class X {
2. field: number;
3. constructor(p: number) {
4. this.field = p;
5. }
6. }

8. let x = new X(666)  // 编译时错误：不能创建抽象类的具体实例
```

抽象类的子类可以是抽象类也可以是非抽象类。抽象父类的非抽象子类可以实例化。因此，执行抽象类的构造函数和该类非静态字段的字段初始化器：

```
1. abstract class Base {
2. private field: number;
3. constructor(p: number) {
4. this.field = p;
5. }
6. }

8. class Derived extends Base {
9. constructor(p: number) {
10. super(p);
11. }
12. }

14. let x = new Derived(666);
```

**抽象方法**

带有abstract修饰符的方法称为抽象方法，抽象方法可以被声明但不能被实现。

只有抽象类内才能有抽象方法，如果非抽象类具有抽象方法，则会发生编译时错误：

```
1. class Y {
2. abstract method(p: string)  // 编译时错误：抽象方法只能在抽象类内。
3. }
```

## 接口

接口声明引入新类型。接口是定义代码协定的常见方式。

任何类的实例，只要实现了特定接口，即可通过该接口实现多态。

接口通常包含属性和方法的声明。

示例：

```
1. interface Style {
2. color: string; // 属性
3. }
4. interface AreaSize {
5. calculateAreaSize(): number; // 方法的声明
6. someMethod(): void;     // 方法的声明
7. }
```

实现接口的类示例：

```
1. // 接口：
2. interface AreaSize {
3. calculateAreaSize(): number; // 方法的声明
4. someMethod(): void;     // 方法的声明
5. }

7. // 实现：
8. class RectangleSize implements AreaSize {
9. private width: number = 0;
10. private height: number = 0;
11. someMethod(): void {
12. console.info('someMethod called');
13. }
14. calculateAreaSize(): number {
15. this.someMethod(); // 调用另一个方法并返回结果
16. return this.width * this.height;
17. }
18. }
```

### 接口属性

接口属性可以是字段、getter、setter或getter和setter组合的形式。

属性字段只是getter/setter对的便捷写法。以下表达方式是等价的：

```
1. interface Style {
2. color: string;
3. }
```

```
1. interface Style {
2. get color(): string;
3. set color(x: string);
4. }
```

实现接口的类也可以使用以下两种方式：

```
1. interface Style {
2. color: string;
3. }

5. class StyledRectangle implements Style {
6. public color: string = '';
7. }
```

```
1. interface Style {
2. color: string;
3. }

5. class StyledRectangle implements Style {
6. private _color: string = '';
7. get color(): string { return this._color; }
8. set color(x: string) { this._color = x; }
9. }
```

### 接口继承

接口可以继承其他接口，示例如下：

```
1. interface Style {
2. color: string;
3. }

5. interface ExtendedStyle extends Style {
6. width: number;
7. }
```

继承接口包含被继承接口的所有属性和方法，还可以添加自己的属性和方法。

### 抽象类和接口

抽象类与接口都无法实例化。抽象类是类的抽象，抽象类用来捕捉子类的通用特性，接口是行为的抽象。在ArkTS语法中抽象类与接口的区别如下：

* 一个类只能继承一个抽象类，而一个类可以实现一个或多个接口；

```
1. // Bird类继承Animal抽象类并实现多个接口CanFly、CanSwim
2. class Bird extends Animal implements CanFly, CanSwim {
3. // ...
4. }
```

* 接口中不能含有静态代码块以及静态方法，而抽象类可以有静态代码块和静态方法；

```
1. interface MyInterface {
2. // 错误：接口中不能包含静态成员
3. static staticMethod(): void;

5. // 错误：接口中不能包含静态代码块
6. static { console.info('static'); };
7. }

9. abstract class MyAbstractClass {
10. // 正确：抽象类可以有静态方法
11. static staticMethod(): void { console.info('static'); }

13. // 正确：抽象类可以有静态代码块
14. static { console.info('static initialization block'); }
15. }
```

* 抽象类里面可以有方法的实现，但是接口没有方法的实现，是完全抽象的；

```
1. abstract class MyAbstractClass {
2. // 正确：抽象类里面可以有方法的实现
3. func(): void { console.info('func'); }
4. }
5. interface MyInterface {
6. // 错误：接口没有方法的实现，是完全抽象的
7. func(): void { console.info('func'); }
8. }
```

* 抽象类可以有构造函数，而接口不能有构造函数。

```
1. abstract class MyAbstractClass {
2. constructor(){}  // 正确：抽象类可以有构造函数
3. }
4. interface MyInterface {
5. constructor(); // 错误：接口中不能有构造函数
6. }
```

## 泛型类型和函数

泛型类型和函数使代码能够以类型安全的方式操作多种数据类型，而无需为每种类型编写重复的逻辑。

### 泛型类和接口

类和接口可以定义为泛型，将参数添加到类型定义中。如以下示例中的类型参数Element：

```
1. class CustomStack<Element> {
2. public push(e: Element):void {
3. // ...
4. }
5. }
```

要使用类型CustomStack，必须为每个类型参数指定类型实参：

```
1. let s = new CustomStack<string>();
2. s.push('hello');
```

编译器在使用泛型类型和函数时会确保类型安全。参见以下示例：

```
1. let s = new CustomStack<string>();
2. s.push(55); // 将会产生编译时错误
```

### 泛型约束

泛型类型的类型参数可以被限制只能取某些特定的值。例如，MyHashMap<Key, Value>这个类中的Key类型参数必须具有hash方法。

```
1. interface Hashable {
2. hash(): number;
3. }
4. class MyHashMap<Key extends Hashable, Value> {
5. public set(k: Key, v: Value) {
6. let h = k.hash();
7. // ...其他代码...
8. }
9. }
```

在上面的例子中，Key类型扩展了Hashable，Hashable接口的所有方法都可以为key调用。

### 泛型函数

使用泛型函数可编写更通用的代码。比如返回数组最后一个元素的函数：

```
1. function last(x: number[]): number {
2. return x[x.length - 1];
3. }
4. // ...
5. last([1, 2, 3]); // 3
```

如果需要为任何数组定义相同的函数，使用类型参数将该函数定义为泛型：

```
1. function last1<T>(x: T[]): T {
2. return x[x.length - 1];
3. }
```

现在，该函数可以与任何数组一起使用。

在函数调用中，类型实参可以显式或隐式设置：

```
1. // 显式设置的类型实参
2. let res1: string = last<string>(['aa', 'bb']);
3. let res2: number = last<number>([1, 2, 3]);

5. // 隐式设置的类型实参
6. // 编译器根据调用参数的类型来确定类型实参
7. let res3: number = last([1, 2, 3]);
```

### 泛型默认值

泛型类型的类型参数可以设置默认值，这样无需指定实际类型实参，直接使用泛型类型名称即可。以下示例展示了类和函数的这一特性。

```
1. class SomeType {}
2. interface Interface <T1 = SomeType> { }
3. class Base <T2 = SomeType> { }
4. class Derived1 extends Base implements Interface { }
5. // Derived1在语义上等价于Derived2
6. class Derived2 extends Base<SomeType> implements Interface<SomeType> { }

8. function foo<T = number>(): void {
9. // ...
10. }
11. foo();
12. // 此函数在语义上等价于下面的调用
13. foo<number>();
```

## 空安全

默认情况下，ArkTS中的所有类型都不允许为空，这类似于TypeScript的(strictNullChecks)模式，但规则更严格。

在下面的示例中，所有行都会导致编译时错误：

```
1. let x: number = null;    // 编译时错误
2. let y: string = null;    // 编译时错误
3. let z: number[] = null;  // 编译时错误
```

可以为空值的变量定义为联合类型T | null。

```
1. let x: number | null = null;
2. x = 1;    // ok
3. x = null; // ok
4. if (x != null) { /* do something */ }
```

### 非空断言运算符

后缀运算符!可用于断言其操作数为非空。

当应用于可空类型的值时，编译时类型会变为非空类型。例如，类型从T | null变为T：

```
1. class A {
2. value: number = 0;
3. }

5. function foo(a: A | null) {
6. a.value;   // 编译时错误：无法访问可空值的属性
7. a!.value;  // 编译通过，如果运行时a的值非空，可以访问到a的属性；如果运行时a的值为空，则发生运行时异常
8. }
```

### 空值合并运算符

空值合并二元运算符??用于检查左侧表达式的求值是否等于null或者undefined。如果是，则表达式的结果为右侧表达式；否则，结果为左侧表达式。

换句话说，a ?? b等价于三元运算符(a != null && a != undefined) ? a : b。

在以下示例中，getNick方法返回已设置的昵称。如果未设置，则返回空字符串。

```
1. class Person {
2. // ...
3. public nick: string | null = null;
4. getNick(): string {
5. return this.nick ?? '';
6. }
7. }
```

### 可选链

访问对象属性时，如果属性是undefined或null，可选链运算符返回undefined。

```
1. class Person {
2. public nick: string | null = null;
3. public spouse?: Person

5. setSpouse(spouse: Person): void {
6. this.spouse = spouse;
7. }

9. getSpouseNick(): string | null | undefined {
10. return this.spouse?.nick;
11. }

13. constructor(nick: string) {
14. this.nick = nick;
15. this.spouse = undefined;
16. }
17. }
```

说明

getSpouseNick的返回类型必须为string | null | undefined，因为该方法在某些情况下会返回null或undefined。

可选链可以任意长，可以包含任意数量的?.运算符。

在以下示例中，如果Person实例的spouse属性不为空，并且spouse的nick属性也不为空时，输出spouse.nick。否则，输出undefined。

```
1. class Person {
2. public nick: string | null = null;
3. public spouse?: Person;

5. constructor(nick: string) {
6. this.nick = nick;
7. this.spouse = undefined;
8. }
9. }

11. let p: Person = new Person('Alice');
12. p.spouse?.nick; // undefined
```

## 模块

程序可划分为多组编译单元或模块。

每个模块都有其自己的作用域，即在模块中创建的任何声明（变量、函数、类等）在该模块之外都不可见，除非它们被显式导出。

与此相对，必须首先将另一个模块导出的变量、函数、类、接口等导入到当前模块中。

### 导出

可以使用关键字export导出顶层的声明。

未导出的声明名称被视为私有名称，只能在声明该名称的模块中使用。

```
1. export class Point {
2. public x: number = 0;
3. public y: number = 0;
4. constructor(x: number, y: number) {
5. this.x = x;
6. this.y = y;
7. }
8. }
9. export let origin = new Point(0, 0);
10. export function Distance(p1: Point, p2: Point): number {
11. return Math.sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y));
12. }
```

**导出默认导出的对象**

```
1. class Demo{
2. constructor(){
3. }
4. }
5. export default new Demo();
```

### 导入

**静态导入**

导入声明用于导入从其他模块导出的实体，并在当前模块中提供其绑定。导入声明由两部分组成：

* 导入路径，用于指定导入的模块；
* 导入绑定，用于定义导入的模块中的可用实体集和使用形式（限定或不限定使用）。

导入绑定可以有几种形式。

假设模块的路径为“./utils”，并且导出了实体“X”和“Y”。

导入绑定\* as A表示绑定名称“A”，通过A.name可访问从导入路径指定的模块导出的所有实体：

```
1. import * as Utils from './utils';
2. // ...
3. Utils.X // 表示来自Utils的X
4. Utils.Y // 表示来自Utils的Y
```

导入绑定{ ident1, ..., identN }表示将导出的实体与指定名称绑定，该名称可以用作简单名称：

```
1. import { X, Y } from './utils';
2. // ...
3. X // 表示来自utils的X
4. Y // 表示来自utils的Y
```

如果标识符列表定义了ident as alias，则实体ident将绑定在名称alias下：

```
1. import { X as Z, Y } from './utils';
2. Z // 表示来自Utils的X
3. Y // 表示来自Utils的Y
4. X // 编译时错误：'X'不可见
```

**动态导入**

在应用开发的有些场景中，如果希望根据条件导入模块或者按需导入模块，可以使用动态导入代替静态导入。

import()语法被称为动态导入（dynamic import），是一种类似函数的表达式，用于动态导入模块。调用这种方式，会返回一个promise。

如下例所示，import(modulePath)可以加载模块并返回一个promise，该promise resolve为一个包含其所有导出的模块对象。该表达式可以在代码中的任意位置调用。

```
1. // Calc.ets
2. export function add(a:number, b:number):number {
3. let c = a + b;
4. console.info('Dynamic import, %d + %d = %d', a, b, c);
5. return c;
6. }
```

```
1. // Index.ets
2. // ESObject是ArkTS跨语言调用场景中用于标注JS/TS对象的类型
3. import('./Calc').then((obj: ESObject) => {
4. console.info(obj.add(3, 5));
5. }).catch((err: Error) => {
6. console.error('Module dynamic import error: ', err);
7. });
```

如果在异步函数中，可以使用let module = await import(modulePath)。

```
1. // say.ets
2. export function hi() {
3. console.info('Hello');
4. }
5. export function bye() {
6. console.info('Bye');
7. }
```

那么，可以像下面这样进行动态导入：

```
1. async function test() {
2. let ns = await import('./say');
3. let hi = ns.hi;
4. let bye = ns.bye;
5. hi();
6. bye();
7. }
```

更多的使用动态import的业务场景和使用实例见[动态import](arkts-dynamic-import.md)。

**导入HarmonyOS SDK的开放能力**

HarmonyOS SDK提供的开放能力（接口）也需要在导入声明后使用。可直接导入接口模块来使用该模块内的所有接口能力，例如：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
```

从HarmonyOS NEXT Developer Preview 1版本开始引入Kit概念。SDK对同一个Kit下的接口模块进行了封装，开发者在示例代码中可通过导入Kit的方式来使用Kit所包含的接口能力。其中，Kit封装的接口模块可查看SDK目录下Kit子目录中各Kit的定义。在代码开发中，推荐通过导入Kit方式使用开放能力。

通过导入Kit方式使用开放能力有三种方式：

* 方式一：导入Kit下单个模块的接口能力。例如：

  ```
  1. import { UIAbility } from '@kit.AbilityKit';
  ```
* 方式二：导入Kit下多个模块的接口能力。例如：

  ```
  1. import { UIAbility, Ability, Context } from '@kit.AbilityKit';
  ```
* 方式三：导入Kit包含的所有模块的接口能力。例如：

  ```
  1. import * as module from '@kit.AbilityKit';
  ```

  其中，“module”为别名，可自定义，然后通过该名称调用模块的接口。

  说明

  方式三可能会导入过多无需使用的模块，导致编译后的HAP包太大，占用过多资源，请谨慎使用。

### 顶层语句

顶层语句是指在模块最外层编写的语句，不被任何函数、类或块级作用域包裹。这些语句包括变量声明、函数声明和表达式。

## 关键字

### this

关键字this只能在类的实例方法中使用。

**示例**

```
1. class A {
2. private count: string = 'a';
3. m(i: string): void {
4. this.count = i;
5. }
6. }
```

使用限制：

* 不支持this类型
* 不支持在函数和类的静态方法中使用this

**示例**

```
1. class A {
2. n: number = 0;
3. f1(arg1: this) {} // 编译时错误，不支持this类型
4. static f2(arg1: number) {
5. this.n = arg1;  // 编译时错误，不支持在类的静态方法中使用this
6. }
7. }

9. function foo(arg1: number) {
10. this.n = i;       // 编译时错误，不支持在函数中使用this
11. }
```

关键字this的指向:

* 调用实例方法的对象
* 正在构造的对象

## 注解

注解（Annotation）是一种语言特性，它通过添加元数据来改变应用声明的语义。

注解的声明和使用如下所示：

**示例：**

```
1. // 注解的声明：
2. @interface ClassAuthor {
3. authorName: string
4. }

6. // 注解的使用：
7. @ClassAuthor({authorName: "Bob"})
8. class MyClass {
9. // ...
10. }
```

* 使用@interface声明注解。
* 注解ClassAuthor需要将元信息添加到类声明中。
* 注解必须放置在声明之前。
* 注解可以包含上述示例中所示的参数。

对于要使用的注解，其名称必须以符号@（例如：@MyAnno）为前缀。符号@和名称之间不允许有空格和行分隔符。

```
1. ClassAuthor({authorName: "Bob"}) // 编译错误：注解需要'@'为前缀
2. @ ClassAuthor({authorName: "Bob"}) // 编译错误：符号`@`和名称之间不允许有空格和行分隔符
```

如果在使用位置无法访问注解名称，则会发生编译错误。

注解声明可以导出并在其他文件中使用。

多个注解可以应用于同一个声明（注解间的先后顺序不影响使用）。

```
1. @MyAnno()
2. @ClassAuthor({authorName: "John Smith"})
3. class MyClass1 {
4. // ...
5. }
```

注解不是Typescript中的特性，只能在.ets/.d.ets文件中使用。

注意

应用开发中，在[release模式下构建](ide-hvigor-build-har.md#section19788284410)源码HAR，并同时[开启混淆](source-obfuscation.md)时，由于编译产物为JS文件，而在JS中没有注解的实现机制，因此会在编译过程中被移除，导致无法通过注解实现AOP插桩。

为避免因此引起的功能异常，禁止在JS HAR(编译产物中存在JS的HAR包)中使用注解。

如果需要在release模式并且开启混淆的情况下构建含有注解的HAR包，可以构建[字节码HAR](ide-hvigor-build-har.md#section16598338112415)。

### 用户自定义注解

**从API version 20及之后版本，支持用户自定义注解。**

**用户自定义注解的声明**

用户自定义注解的定义与interface的定义类似，其中的interface关键字以符号@为前缀。

注解字段仅限于下面列举的类型：

* number
* boolean
* string
* 枚举
* 以上类型的数组

  说明

  + 如果使用其他类型用作注解字段的类型，则会发生编译错误。
  + 注解字段类型不支持bigint。

注解字段的默认值必须使用常量表达式来指定。

常量表达式的场景如下所示：

* 数字字面量
* 布尔字面量
* 字符串字面量
* 枚举值（需要在编译时确定值）
* 以上常量组成的数组

  说明

  如果枚举值不能在编译时确定，会编译报错。

```
1. // a.ts
2. export enum X {
3. x = foo(); // x不是编译时能确定的常量
4. }

6. // b.ets
7. import {X} from './a';

9. @interface Position {
10. data: number = X.x; // 编译错误：注解字段的默认值必须使用常量表达式
11. }
```

注解必须定义在顶层作用域（top-level），否则会出现编译报错。

注解的名称不能与注解定义所在作用域内可见的其他实体名称相同，否则会出现编译报错。

注解不支持类型Typescript中的合并，否则会出现编译报错。

```
1. namespace ns {
2. @interface MetaInfo { // 编译错误：注解必须定义在顶层作用域
3. // ...
4. }
5. }

7. @interface Position {
8. // ...
9. }

11. class Position { // 编译错误：注解的名称不能与注解定义所在作用域内可见的其他实体名称相同
12. // ...
13. }

15. @interface ClassAuthor {
16. name: string;
17. }

19. @interface ClassAuthor { // 编译错误：注解的名称不能与注解定义所在作用域内可见的其他实体名称相同
20. data: string;
21. }
```

注解不是类型，把注解当类型使用时会出现编译报错（例如：对注解使用类型别名）。

```
1. @interface Position {}
2. type Pos = Position; // 编译错误：注解不是类型
```

注解不支持在类的getter和setter方法中添加，若添加注解会编译报错。

```
1. @interface ClassAuthor {
2. authorName: string;
3. }

5. @ClassAuthor({authorName: 'John Smith'})
6. class MyClass {
7. private _name: string = 'Bob';

9. @ClassAuthor({authorName: 'John Smith'}) // 编译错误：注解不支持在类的getter和setter方法添加
10. get name() {
11. return this._name;
12. }

14. @ClassAuthor({authorName: 'John Smith'}) // 编译错误：注解不支持在类的getter和setter方法添加
15. set name(authorName: string) {
16. this._name = authorName;
17. }
18. }
```

**用户自定义注解的使用**

注解声明示例如下：

```
1. @interface ClassPreamble {
2. authorName: string;
3. revision: number = 1;
4. }
5. @interface MyAnno {}
```

当前仅允许对class declarations和method declarations使用注解，对类和方法可以同时使用同一个注解。

注解用法示例如下：

```
1. @ClassPreamble({authorName: "John", revision: 2})
2. class C1 {
3. // ...
4. }

7. @ClassPreamble({authorName: "Bob"}) // revision的默认值为1
8. class C2 {
9. // ...
10. }

12. @MyAnno() // 对类和方法可以同时使用同一个注解
13. class C3 {
14. @MyAnno()
15. foo() {}
16. @MyAnno()
17. static bar() {}
18. }
```

注解中的字段顺序不影响使用。

```
1. @ClassPreamble1({authorName: "John", revision: 2})
2. // ...
3. // the same as:
4. @ClassPreamble1({revision: 2, authorName: "John"})
```

使用注解时，必须给所有没有默认值的字段赋值，否则会发生编译错误。

说明

赋值应当与注解声明的类型一致，所赋的值与注解字段默认值的要求一样，只能使用常量表达式。

```
1. @ClassPreamble() // 编译错误：authorName字段未定义
2. class C1 {
3. // ...
4. }
```

如果注解中定义了数组类型的字段，则使用数组字面量来设置该字段的值。

```
1. @interface ClassPreamble2 {
2. authorName: string;
3. revision: number = 1;
4. reviewers: string[];
5. }

7. @ClassPreamble2(
8. {
9. authorName: "Alice",
10. reviewers: ["Bob", "Clara"]
11. }
12. )
13. class C0 {
14. // ...
15. }
```

如果不需要定义注解字段，可以省略注解名称后的括号。

```
1. @MyAnno
2. class C4 {
3. // ...
4. }
```

**导入和导出注解**

注解也可以被导入导出。针对导出，当前仅支持在定义时的导出，即export @interface的形式。

**示例：**

```
1. export @interface MyAnno1 {}
```

针对导入，当前仅支持import {}和import \* as两种方式。

**示例：**

```
1. // a.ets
2. export @interface MyAnno2 {}
3. export @interface ClassAuthor2 {}
```

```
1. // b.ets
2. import { MyAnno2 } from './a';
3. import * as ns from './a';
4. // ...
5. @MyAnno2
6. @ns.ClassAuthor2
7. class C {
8. // ...
9. }
```

* 不允许在import中对注解进行重命名。

```
1. import { MyAnno as Anno } from './a'; // 编译错误：不允许在import中对注解进行重命名
```

不允许对注解使用任何其他形式的 import/export，这会导致编译报错。

* 由于注解不是类型，因此禁止使用type符号进行导入和导出。

```
1. import type { MyAnno } from './a'; // 编译错误：注解不允许使用'type'符号进行导入和导出
```

* 如果仅从模块导入注解，则不会触发模块的副作用。

```
1. // a.ets
2. export @interface Anno {}

4. export @interface ClassAuthor1 {}

6. console.info('hello');
```

```
1. // b.ets
2. import { MyAnno2 } from './a';
3. import * as ns from './a';
4. // 仅引用了Anno注解，不会导致a.ets的console.info执行
5. class X {
6. // ...
7. }
```

**.d.ets文件中的注解**

注解可以出现在.d.ets文件中。

可以在.d.ets文件中用环境声明（ambient declaration）来声明注解。

```
1. ambientAnnotationDeclaration:
2. 'declare' userDefinedAnnotationDeclaration
3. ;
```

**示例：**

```
1. // a.d.ets
2. export declare @interface ClassAuthor3 {}
```

上述声明中：

* 不会引入新的注解定义，而是提供注解的类型信息。
* 注解需定义在其他源代码文件中。
* 注解的环境声明和实现需要完全一致，包括字段的类型和默认值。

```
1. // a.d.ets
2. export declare @interface NameAnno{name: string = ""}

4. // a.ets
5. export @interface NameAnno{name: string = ""} // ok
```

环境声明的注解和class类似，也可以被import使用。

```
1. // a.d.ets
2. export declare @interface MyAnno {}

4. // b.ets
5. import { MyAnno } from './a';

7. @MyAnno
8. class C {
9. // ...
10. }
```

**编译器自动生成的.d.ets文件**

当编译器根据ets代码自动生成.d.ets文件时，存在以下2种情况。

1. 当注解定义被导出时，源代码中的注解定义会在.d.ets文件中保留。

   ```
   1. // a.ets
   2. export @interface ClassAuthor5 {}

   4. @interface MethodAnno { // 没导出
   5. data: number;
   6. }
   ```

   ```
   1. // a.d.ets
   2. export declare @interface ClassAuthor3 {}
   ```
2. 当下面所有条件成立时，源代码中实体的注解实例会在.d.ets文件中保留。

   2.1 注解的定义被导出（import的注解也算作被导出）。

   2.2 如果实体是类，则类被导出。

   2.3 如果实体是方法，则类被导出，并且方法不是私有方法。

   ```
   1. // a.ets
   2. import { ClassAuthor } from './author';

   4. export @interface MethodAnno {
   5. data: number = 0;
   6. }

   8. @ClassAuthor
   9. class MyClass {
   10. @MethodAnno({data: 123})
   11. foo() {}

   13. @MethodAnno({data: 456})
   14. private bar() {}
   15. }

   17. // a.d.ets 编译器生成的声明文件
   18. import {ClassAuthor} from "./author";

   20. export declare @interface MethodAnno {
   21. data: number = 0;
   22. }

   24. @ClassAuthor
   25. export declare class MyClass {
   26. @MethodAnno({data: 123})
   27. foo(): void;

   29. bar; // 私有方法不保留注解
   30. }
   ```

**开发者生成的.d.ets文件**

开发者生成的.d.ets文件中的注解信息不会自动应用到实现的源代码中。

**示例：**

```
1. // b.d.ets 开发者生成的声明文件
2. @interface ClassAuthor {}

4. @ClassAuthor // 声明文件中有注解
5. class C {
6. // ...
7. }

9. // b.ets 开发者对声明文件实现的源代码
10. @interface ClassAuthor {}

12. // 实现文件中没有注解
13. class C {
14. // ...
15. }
```

在最终编译产物中，class C没有注解。

**重复注解和继承**

同一个实体不能重复使用同一注解，否则会导致编译错误。

```
1. @MyAnno({name: "123", value: 456})
2. @MyAnno({name: "321", value: 654}) // 编译错误：不允许重复注释
3. class C {
4. // ...
5. }
```

子类不会继承基类的注解，也不会继承基类方法的注解。

**注解和抽象类、抽象方法**

不支持对抽象类或抽象方法使用注解，否则将导致编译错误。

```
1. @MyAnno // 编译错误：不允许在抽象类和抽象方法上使用注解
2. abstract class C {
3. @MyAnno
4. abstract foo(): void; // 编译错误：不允许在抽象类和抽象方法上使用注解
5. }
```

## ArkUI支持

本节演示ArkTS为创建图形用户界面（GUI）程序提供的机制。ArkUI基于TypeScript提供了一系列扩展能力，以声明式地描述应用程序的GUI以及GUI组件间的交互。

### ArkUI示例

[MVVM代码示例](arkts-mvvm.md#代码示例)提供了一个完整的基于ArkUI的应用程序，以展示其GUI编程功能。

有关ArkUI功能的更多详细信息，请参见ArkUI[基本语法概述](arkts-basic-syntax-overview.md)。
