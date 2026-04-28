---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-coding-style-guide
title: ArkTS编程规范
breadcrumb: 指南 > 基础入门 > 学习ArkTS语言 > ArkTS编程规范
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:af1b2281e5b8b38eb984bfcb8549b6eacdfc9a102d5c7016a4aef3e7415db133
---

## 目标和适用范围

本文参考业界标准和实践，结合ArkTS语言特点，提供编码指南，以提高代码的规范性、安全性和性能。

本文适用于使用ArkTS编写的开发场景。

## 规则来源

ArkTS在保持TypeScript基本语法风格的基础上，进一步强化静态检查和分析。本文部分规则筛选自《[OpenHarmony应用TS&JS编程指南](https://gitcode.com/openharmony/docs/blob/master/zh-cn/contribute/OpenHarmony-Application-Typescript-JavaScript-coding-guide.md)》，为ArkTS语言新增的语法添加了规则，旨在提高代码可读性、执行性能。

## 章节概览

### 代码风格

包含命名和格式。

### 编程实践

包含声明与初始化、数据类型、运算与表达式、异常等。

参考了《OpenHarmony应用TS&JS编程指南》中的规则，去除了ArkTS语言不涉及的部分，并为新增的语法添加了规则。

## 术语和定义

| 术语 | 缩略语 | 中文解释 |
| --- | --- | --- |
| ArkTS | 无 | ArkTS编程语言 |
| TypeScript | TS | TypeScript编程语言 |
| JavaScript | JS | JavaScript编程语言 |
| ESObject | 无 | 在ArkTS跨语言调用的场景中，用以标注JS/TS对象的类型 |

## 总体原则

规则分为两个级别：要求和建议。

**要求**：表示原则上应该遵从。本文所有内容目前均为针对ArkTS的要求。

**建议**：表示该条款属于最佳实践，可结合实际情况考虑是否纳入。

## 命名

### 为标识符取一个好名字，提高代码可读性

**【描述】**

好的标识符命名应遵循以下原则：

* 清晰表达意图，避免使用单个字母或非标准缩写命名。
* 使用正确的英文单词并符合英文语法，不要使用中文拼音。
* 确保语句清晰，避免歧义。

### 类名、枚举名、命名空间名采用UpperCamelCase风格

**【级别】建议**

**【描述】**

类采用首字母大写的驼峰命名法。

类名通常是名词或名词短语，例如Person、Student、Worker。不应使用动词，也应该避免类似Data、Info这样的模糊词。

**【正例】**

```
1. // 类名
2. class User {
3. username: string

5. constructor(username: string) {
6. this.username = username;
7. }

9. sayHi() {
10. console.info('hi' + this.username);
11. }
12. }

14. // 枚举名
15. enum UserType {
16. TEACHER = 0,
17. STUDENT = 1
18. };

20. // 命名空间
21. namespace Base64Utils {
22. export function encrypt() {
23. // todo encrypt
24. }

26. export function decrypt() {
27. // todo decrypt
28. }
29. };
```

### 变量名、方法名、参数名采用lowerCamelCase风格

**【级别】建议**

**【描述】**

函数的命名通常是动词或动词短语，采用小驼峰命名。示例如下：

1. load + 属性名()
2. put + 属性名()
3. is + 布尔属性名()
4. has + 名词/形容词()
5. 动词()
6. 动词 + 宾语()

变量名通常是名词或名词短语，采用小驼峰命名，便于理解。

**【正例】**

```
1. let msg = 'Hello world';

3. function sendMsg(msg: string) {
4. // todo send message
5. // ...
6. }

8. let userName = 'Zhangsan';

10. function findUser(userName: string) {
11. // todo find user by user name
12. // ...
13. }
```

### 常量名、枚举值名采用全部大写，单词间使用下划线隔开

**【级别】建议**

**【描述】**

常量命名，应该由全大写单词与下划线组成，单词间用下划线分割。常量命名要尽量表达完整的语义。

**【正例】**

```
1. enum UserType1 {
2. TEACHER = 0,
3. STUDENT = 1
4. };

6. const MAX_USER_SIZE = 10000;
```

### 避免使用否定的布尔变量名，布尔型的局部变量或方法需加上表达是非意义的前缀

**【级别】建议**

**【描述】**

布尔型的局部变量建议加上表达是非意义的前缀，比如is，也可以是has、can、should等。但是，当使用逻辑非运算符，并出现双重否定时，会出现理解问题，比如!isNotError，难以理解。因此，应避免定义否定的布尔变量名。

**【反例】**

```
1. let isNoError = true;
2. let isNotFound = false;

4. function empty() {}
5. function next() {}
```

**【正例】**

```
1. let isError = false;
2. let isFound = true;

4. function isEmpty() {}
5. function hasNext() {}
```

## 格式

### 使用空格缩进，禁止使用tab字符

**【级别】建议**

**【描述】**

只允许使用空格(space)进行缩进。

建议大部分场景优先使用2个空格，换行导致的缩进优先使用4个空格。

不允许插入制表符Tab。当前几乎所有的集成开发环境（IDE）和代码编辑器都支持配置将Tab键自动扩展为2个空格输入，应在代码编辑器中配置使用空格进行缩进。

**【正例】**

```
1. class DataSource {
2. id: number = 0
3. title: string = ''
4. content: string = ''
5. }

7. const dataSource: DataSource[] = [
8. {
9. id: 1,
10. title: 'Title 1',
11. content: 'Content 1'
12. },
13. {
14. id: 2,
15. title: 'Title 2',
16. content: 'Content 2'
17. }

19. ];

21. function test(dataSource: DataSource[]) {
22. if (!dataSource.length) {
23. return;
24. }

26. for (let data of dataSource) {
27. if (!data || !data.id || !data.title || !data.content) {
28. continue;
29. }
30. // some code
31. }

33. // some code
34. }
```

### 行宽不超过120个字符

**【级别】建议**

**【描述】**

代码行宽不宜过长，否则不利于阅读。

控制行宽可以间接引导程序员缩短函数和变量的命名，减少嵌套层数，精炼注释，从而提升代码可读性。

建议每行字符数不超过120个，除非需要显著增加可读性（超过120个），且不会隐藏信息。

例外：如果一行注释包含了超过120个字符的命令或URL，则可以保持一行，以方便复制、粘贴和通过grep查找；预处理的error信息在一行便于阅读和理解，即使超过120个字符。

### 条件语句和循环语句的实现建议使用大括号

**【级别】建议**

**【描述】**

在if、for、do、while等语句的执行体加大括号{}是一种最佳实践，因为省略大括号可能导致错误，并且降低代码的清晰度。

**【反例】**

```
1. let condition = true;
2. if (condition)
3. console.info('success');
4. for (let idx = 0; idx < 5; ++idx)
5. console.info('', idx);
```

**【正例】**

```
1. let condition = true;
2. if (condition) {
3. console.info('success');
4. }
5. for (let idx = 0; idx < 5; ++idx) {
6. console.info('', idx);
7. }
```

### switch语句的case和default需缩进一层

**【级别】建议**

**【描述】**

switch的case和default要缩进一层（2个空格）。开关标签之后换行的语句，需再缩进一层（2个空格）。

**【正例】**

```
1. switch (condition) {
2. case 0: {
3. doSomething();
4. break;
5. }
6. case 1: {
7. doOtherthing();
8. break;
9. }
10. default:
11. break;
12. }
```

### 表达式换行需保持一致性，运算符放行末

**【级别】建议**

**【描述】**

当语句过长或可读性不佳时，需要在合适的地方进行换行。

换行时将操作符放在行末，表示“未结束，后续还有”，保持与常用的格式化工具的默认配置一致。

**【正例】**

```
1. // 假设条件语句超出行宽
2. if (userCount > MAX_USER_COUNT ||
3. userCount < MIN_USER_COUNT) {
4. doSomething();
5. }
```

### 多个变量定义和赋值语句不允许写在一行

**【级别】要求**

**【描述】**

每个语句的变量声明都应只声明一个变量。

这种方式更便于添加变量声明，无需考虑将分号改为逗号，以免引入错误。此外，每个语句只声明一个变量，使用调试器逐个调试也很方便，而不是一次跳过所有变量。

**【反例】**

```
1. let maxCount = 10, isCompleted = false;
2. let pointX, pointY;
3. pointX = 10; pointY = 0;
```

**【正例】**

```
1. let maxCount = 10;
2. let isCompleted = false;
3. let pointX = 0;
4. let pointY = 0;
```

### 空格应该突出关键字和重要信息，避免不必要的空格

**【级别】建议**

**【描述】**

空格应该突出关键字和重要信息。总体建议如下：

1. if, for, while, switch等关键字与左括号(之间加空格。
2. 在函数定义和调用时，函数名称与参数列表的左括号(之间不加空格。
3. 关键字else或catch与其之前的大括号}之间加空格。
4. 任何打开大括号({)之前加空格，有两个例外：

a) 在作为函数的第一个参数或数组中的第一个元素时，对象之前不用加空格，例如：foo({ name: 'abc' })。

b) 在模板中，不用加空格，例如：abc${name}。

5. 二元操作符(+ - \* = < > <= >= === !== && ||)前后加空格；三元操作符(? :)符号两侧均加空格。

6. 数组初始化中的逗号和函数中多个参数之间的逗号后加空格。

7. 在逗号(,)或分号(;)之前不加空格。

8. 数组的中括号([])内侧不要加空格。

9. 不要出现多个连续空格。在某行中，多个空格若不是用来作缩进的，通常是个错误。

**【反例】**

```
1. // if 和左括号 ( 之间没有加空格
2. if(isJedi) {
3. fight();
4. }
5. // ...
6. // 函数名fight和左括号 ( 之间加了空格
7. function fightBad (): void {
8. console.info('Swooosh!');
9. }
```

**【正例】**

```
1. // if 和左括号之间加一个空格
2. if (isJedi) {
3. fight();
4. }
5. // ...
6. // 函数名fight和左括号 ( 之间不加空格
7. function fight(): void {
8. console.info('Swooosh!');
9. }
```

**【反例】**

```
1. if (flag) {
2. // ...
3. }else { // else 与其前面的大括号 } 之间没有加空格
4. // ...
5. }
```

**【正例】**

```
1. if (flag) {
2. // ...
3. } else { // else 与其前面的大括号 } 之间增加空格
4. // ...
5. }
```

**【正例】**

```
1. function foo() { // 函数声明时，左大括号 { 之前加个空格
2. // ...
3. }
4. // ...
5. bar('attr', { // 左大括号前加个空格
6. age: '1 year',
7. sbreed: 'Bernese Mountain Dog',
8. });
```

**【正例】**

```
1. const arr = [1, 2, 3]; // 数组初始化中的逗号后面加个空格，逗号前面不加空格
2. myFunc(bar1, foo1, baz); // 函数的多个参数之间的逗号后加个空格，逗号前面不加空格
```

### 建议字符串使用单引号

**【级别】建议**

**【描述】**

为了保持代码一致性和可读性，建议使用单引号。

**【反例】**

```
1. let message1 = 'world';
2. console.info(message1);
```

**【正例】**

```
1. let message2 = 'world';
2. console.info(message2);
```

### 对象字面量属性超过4个，需要都换行

**【级别】建议**

**【描述】**

对象字面量的属性应保持一致的格式：要么每个属性都换行，要么所有属性都在同一行。当对象字面量的属性超过4个时，建议统一换行。

**【反例】**

```
1. interface I {
2. name: string
3. age: number
4. value: number
5. sum: number
6. foo: boolean
7. bar: boolean
8. }

10. let obj1: I = { name: 'tom', age: 16, value: 1, sum: 2, foo: true, bar: false }
```

**【正例】**

```
1. interface I {
2. name: string
3. age: number
4. value: number
5. sum: number
6. foo: boolean
7. bar: boolean
8. }

10. // ...
11. let obj2: I = {
12. name: 'tom',
13. age: 16,
14. value: 1,
15. sum: 2,
16. foo: true,
17. bar: false
18. }
```

### 把else/catch放在if/try代码块关闭括号的同一行

**【级别】建议**

**【描述】**

编写条件语句时，建议将else放在if代码块关闭括号的同一行。同样，编写异常处理语句时，建议将catch放在try代码块关闭括号的同一行。

**【反例】**

```
1. if (isOk) {
2. doThing1();
3. doThing2();
4. }
5. else {
6. doThing3();
7. }
```

**【正例】**

```
1. if (isOk) {
2. doThing1();
3. doThing2();
4. } else {
5. doThing3();
6. }
```

**【反例】**

```
1. try {
2. doSomething();
3. }
4. catch (err) {
5. // 处理错误。
6. }
```

**【正例】**

```
1. try {
2. doSomething();
3. } catch (err) {
4. // 处理错误。
5. }
```

### 大括号{和语句在同一行

**【级别】建议**

**【描述】**

应保持一致的大括号风格。建议将大括号置于控制语句或声明语句的同一行。

**【反例】**

```
1. function foo1()
2. {
3. // ...
4. }
```

**【正例】**

```
1. function foo2() {
2. // ...
3. }
```

## 编程实践

### 建议添加类属性的可访问修饰符

**【级别】建议**

**【描述】**

ArkTS提供了private, protected和public可访问修饰符。默认情况下，属性的可访问修饰符为public。选取适当的可访问修饰符可以提升代码的安全性和可读性。注意：如果类中包含private属性，无法通过对象字面量初始化该类。

**【反例】**

```
1. class C1 {
2. count: number = 0

4. getCount(): number {
5. return this.count
6. }
7. }
```

**【正例】**

```
1. class C2 {
2. private count: number = 0

4. public getCount(): number {
5. return this.count
6. }
7. }
```

### 不建议省略浮点数小数点前后的0

**【级别】建议**

**【描述】**

ArkTS中，浮点值包含一个小数点，不要求小数点之前或之后必须有一个数字。在小数点前面和后面都添加数字可以提高代码的可读性。

**【反例】**

```
1. const num1 = .5;
2. const num2 = 2.;
3. const num3 = -.7;
```

**【正例】**

```
1. const num4 = 0.5;
2. const num5 = 2.0;
3. const num6 = -0.7;
```

### 判断变量是否为Number.NaN时必须使用Number.isNaN()方法

**【级别】要求**

**【描述】**

在ArkTS中，Number.NaN是Number类型的一个特殊值。它被用来表示非数值，这里的数值是指在IEEE浮点数算术标准中定义的双精度64位格式的值。

在ArkTS中，Number.NaN的独特之处在于它不等于任何值，包括其本身。与Number.NaN进行比较时，结果是令人困惑的：Number.NaN !== Number.NaN 和 Number.NaN != Number.NaN 的值都是 true。

因此，必须使用Number.isNaN()函数来测试一个值是否是Number.NaN。

**【反例】**

```
1. if (foo == Number.NaN) {
2. // ...
3. }

5. if (foo != Number.NaN) {
6. // ...
7. }
```

**【正例】**

```
1. if (Number.isNaN(foo)) {
2. // ...
3. }

5. if (!Number.isNaN(foo)) {
6. // ...
7. }
```

### 数组遍历优先使用Array对象方法

**【级别】要求**

**【描述】**

对于数组遍历，应该优先使用Array对象方法，如：forEach(), map(), every(), filter(), find(), findIndex(), reduce(), some()。

**【反例】**

```
1. const numbers = [1, 2, 3, 4, 5];
2. // 依赖已有数组来创建新的数组时，通过for遍历，生成一个新数组
3. const increasedByOne1: number[] = [];
4. for (let i = 0; i < numbers.length; i++) {
5. increasedByOne1.push(numbers[i] + 1);
6. }
```

**【正例】**

```
1. const numbers = [1, 2, 3, 4, 5];
2. // ...
3. // better: 使用map方法是更好的方式
4. const increasedByOne2: number[] = numbers.map(num => num + 1);
```

### 不要在控制性条件表达式中执行赋值操作

**【级别】要求**

**【描述】**

控制性条件表达式用于 if、while、for 以及 ?: 等条件判断语句中。

在控制性条件表达式中执行赋值容易导致意外行为，且降低代码的可读性。

**【反例】**

```
1. // 在控制性判断中赋值不易理解
2. if (isFoo = false) {
3. // ...
4. }
```

**【正例】**

```
1. const isFoo = false; // 在上面赋值，if条件判断中直接使用
2. if (isFoo) {
3. // ...
4. }
```

### 在finally代码块中，不要使用return、break、continue或抛出异常，避免finally块非正常结束

**【级别】要求**

**【描述】**

在finally代码块中，直接使用return、break、continue、throw语句或调用方法时未处理异常，会导致finally代码块无法正常结束。finally代码块异常结束会影响try或catch代码块中异常的抛出，也可能影响方法的返回值。因此，必须确保finally代码块正常结束。

**【反例】**

```
1. function foo4() {
2. try {
3. // ...
4. return 1;
5. } catch (err) {
6. // ...
7. return 2;
8. } finally {
9. return 3;
10. }
11. }
```

**【正例】**

```
1. function foo5() {
2. try {
3. // ...
4. return 1;
5. } catch (err) {
6. // ...
7. return 2;
8. } finally {
9. console.info('XXX!');
10. }
11. }
```

### 避免使用ESObject

**【级别】建议**

**【描述】**

ESObject主要用于ArkTS和TS/JS的跨语言调用场景中的类型标注。在非跨语言调用场景中使用ESObject标注类型，会引入不必要的跨语言调用，导致额外的性能开销。

**【反例】**

```
1. // lib.ets
2. export interface I {
3. sum: number
4. }

6. export function getObject1(value: number): I {
7. let obj: I = { sum: value };
8. return obj
9. }
```

```
1. import { getObject1 } from './lib'
2. // ...
3. let obj1: I = getObject1(123);
```

**【正例】**

```
1. // lib.ets
2. export interface I {
3. sum: number
4. }

6. // ...
7. export function getObject2(value: number): I {
8. let obj: I = { sum: value };
9. return obj
10. }
```

```
1. // Index.ets
2. import { getObject2, I } from './lib';
3. // ...
4. let obj2: I = getObject2(123);
```

### 使用T[]表示数组类型

**【级别】建议**

**【描述】**

ArkTS提供了两种数组类型的表示方式：T[]和Array<T>。建议所有数组类型均使用T[]表示，以提高代码可读性。

**【反例】**

```
1. let x: Array<number> = [1, 2, 3];
2. let y: Array<string> = ['a', 'b', 'c'];
```

**【正例】**

```
1. // 统一使用T[]语法
2. let x: number[] = [1, 2, 3];
3. let y: string[] = ['a', 'b', 'c'];
```
