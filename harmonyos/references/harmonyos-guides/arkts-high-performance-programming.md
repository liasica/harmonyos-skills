---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-high-performance-programming
title: ArkTS高性能编程实践
breadcrumb: 指南 > 基础入门 > 学习ArkTS语言 > ArkTS高性能编程实践
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:316725fb8fe478a1938213cd205fdd0ac774b54bf1390c69b738aa7246ada877
---

## 概述

本文提供应用性能敏感场景下的高性能编程建议，帮助开发者编写高性能应用。高性能编程实践是在开发过程中总结的一些高性能写法和建议。在实现业务功能时，应同步思考并理解高性能写法的原理，并将其应用于代码逻辑中。关于ArkTS编程规范，请参考[ArkTS编程规范](arkts-coding-style-guide.md)。

## 声明与表达式

### 使用const声明不变的变量

不变的变量推荐使用const声明。

```
1. const index = 10000; // 该变量在后续过程中未发生改变，建议声明成常量。
```

### number类型变量避免整型和浮点型混用

针对number类型，运行时在优化时会区分整型和浮点型数据。建议避免在初始化后改变数据类型。

```
1. let intNum = 1;
2. intNum = 1.1;  // 该变量在声明时为整型数据，建议后续不要赋值浮点型数据。

4. let doubleNum = 1.1;
5. doubleNum = 1;  // 该变量在声明时为浮点型数据，建议后续不要赋值整型数据。
```

### 数值计算避免溢出

常见的可能导致溢出的数值计算包括如下场景，溢出之后，会导致引擎走入慢速的溢出逻辑分支处理，影响后续的性能。

* 针对加法、减法、乘法、指数运算等运算操作，应避免数值大于INT32\_MAX（2147483647）或小于INT32\_MIN（-2147483648）。
* 针对&（and）、>>>（无符号右移）等运算操作，应避免数值大于INT32\_MAX。

### 循环中常量提取，减少属性访问次数

如果常量在循环中不会改变，可以将其提取到循环外部，减少访问次数。

```
1. class Time {
2. static start: number = 0;
3. static info: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
4. }

6. function getNum(num: number): number {
7. let total: number = 348;
8. for (let index: number = 0x8000; index > 0x8; index >>= 1) {
9. // 此处会多次对Time的info及start进行查找，并且每次查找出来的值是相同的。
10. total += ((Time.info[num - Time.start] & index) !== 0) ? 1 : 0;
11. }
12. return total;
13. }
```

优化后的代码如下，可以将Time.info[num - Time.start]提取为常量，这样可以显著减少属性访问次数，提升性能。

```
1. class TimeBetter {
2. static start: number = 0;
3. static info: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
4. }

6. function getNumBetter(num: number): number {
7. let total: number = 348;
8. const info = TimeBetter.info[num - TimeBetter.start];  // 从循环中提取不变量。
9. for (let index: number = 0x8000; index > 0x8; index >>= 1) {
10. if ((info & index) != 0) {
11. total++;
12. }
13. }
14. return total;
15. }
```

## 函数

### 建议使用参数传递函数外的变量

使用闭包会造成额外的开销。在性能敏感场景中，建议使用参数传递函数外的变量替代。

```
1. let arr = [0, 1, 2];

3. function fooWithout(): number {
4. return arr[0] + arr[1];
5. }

7. fooWithout();
```

建议使用参数传递函数外部的变量，以替代使用闭包。

```
1. let arr_ = [0, 1, 2];

3. function fooWithArray(array: number[]): number {
4. return array[0] + array[1];
5. }

7. fooWithArray(arr_);
```

### 避免使用可选参数

函数的可选参数表示参数可能为undefined，在函数内部使用该参数时，需要进行非空值的判断，造成额外的开销。

```
1. function add(left?: number, right?: number): number | undefined {
2. if (left != undefined && right != undefined) {
3. return left + right;
4. }
5. return undefined;
6. }
```

根据业务需求，将函数参数声明为必选参数。考虑使用默认参数。

```
1. function addWithParams(left: number = 0, right: number = 0): number {
2. return left + right;
3. }
```

## 数组

### 数值数组推荐使用TypedArray

涉及纯数值计算时，推荐使用TypedArray数据结构。

优化前的代码示例：

```
1. const arr1 = new Array<number>(1, 2, 3);
2. const arr2 = new Array<number>(4, 5, 6);
3. let res = new Array<number>(3);
4. for (let i = 0; i < 3; i++) {
5. res[i] = arr1[i] + arr2[i];
6. }
```

优化后的代码示例：

```
1. const typedArray1 = Int8Array.from([1, 2, 3]);
2. const typedArray2 = Int8Array.from([4, 5, 6]);
3. let res1 = new Array<number>(3);
4. for (let i = 0; i < 3; i++) {
5. res1[i] = typedArray1[i] + typedArray2[i];
6. }
```

### 避免使用稀疏数组

运行时在分配超过1024大小的数组或稀疏数组时，会采用hash表来存储元素。在该模式下，访问数组元素速度较慢。代码开发时应避免数组变成稀疏数组。

```
1. // 直接分配100000大小的数组，运行时会处理成用hash表来存储元素。
2. let count = 100000;
3. let res: number[] = new Array(count).fill(0);

5. // 创建数组后，直接在9999处赋值，会变成稀疏数组。
6. let result: number[] = [];
7. result[9999] = 0;
```

### 避免使用联合类型数组

避免使用联合类型数组。避免在数值数组中混合使用整型数据和浮点型数据。

```
1. let arrNum: number[] = [1, 1.1, 2]; // 数值数组中混合使用整型数据和浮点型数据。
2. let arrUnion: (number | string)[] = [1, 'hello']; // 联合类型数组。
```

根据业务需求，将相同类型的数据放在同一数组中。

```
1. let arrInt: number[] = [1, 2, 3];
2. let arrDouble: number[] = [0.1, 0.2, 0.3];
3. let arrString: string[] = ['hello', 'world'];
```

## 异常

### 避免频繁抛出异常

创建异常时会构造异常的栈帧，造成性能损耗。在性能敏感场景下，如for循环语句中，应避免频繁抛出异常。

优化前的代码示例：

```
1. function div(a: number, b: number): number {
2. if (a <= 0 || b <= 0) {
3. throw new Error('Invalid numbers.');
4. }
5. return a / b;
6. }

8. function sum(num: number): number {
9. let sum = 0;
10. try {
11. for (let t = 1; t < 100; t++) {
12. sum += div(t, num);
13. }
14. } catch (e) {
15. console.info(e.message);
16. }
17. return sum;
18. }
```

优化后的代码示例：

```
1. function sumBetter(num: number): number {
2. let sum = 0;
3. for (let t = 1; t < 100; t++) {
4. // 直接拦截异常场景，避免频繁抛出异常
5. if (num <= 0) {
6. console.info('Invalid numbers.');
7. }
8. sum += divBetter(t, num);
9. }
10. return sum;
11. }
```
