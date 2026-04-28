---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-high-performance
title: ArkTS高性能编程
breadcrumb: 最佳实践 > 应用框架 > ArkTS语言 > ArkTS高性能编程
category: best-practices
scraped_at: 2026-04-28T08:20:05+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:d770d231ba6b449c37c7d470d3f06358926ea2c58c8984303d18da119f0aea98
---

## 概述

高性能编程指的是在语法使用过程中，通过优化一些影响性能的代码片段，使代码以最优的方式执行。以下实践是在开发过程中总结的高性能写法和建议，包括变量声明、属性访问、数值计算、数据结构使用以及函数声明与使用等内容。在实现业务功能时，应理解高性能写法的原理，并将其应用于代码逻辑中。

## 变量声明

### 使用const声明常量

对于初期明确不会改变的变量，尽量使用const进行初始化，这里的常量包含基础类型和引用类型。通过const保证地址不会发生变化，能够极大减少由于编码时误操作导致的赋值等行为，造成对原有逻辑的改变，声明为const能够在编译时及时发现错误。其中当const声明的是引用类型时，引用类型内部的属性变化是允许的，对于这种不存在地址变化的情况下，也建议使用const声明。

【反例】

```
1. // The variable does not change in the subsequent process. It is recommended to declare it as a constant
2. let PRICE = 10000;

4. function getPrice() {
5. return PRICE;
6. }

8. class ClassA {
9. propA: string = 'propA';
10. }

12. // The variable address of the reference type is not changed in the subsequent process, only the variable property is modified. In this example, it is recommended to change the value of let to const
13. let classA: ClassA = new ClassA();
14. classA.propA = 'Property A';
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L2-L16)

【正例】

```
1. const PRICE = 10000; // When a constant is declared as a base type, its content cannot be changed

3. function getPrice() {
4. return PRICE;
5. }

7. class ClassA {
8. propA: string = 'propA';
9. }

11. // When a constant is declared as a reference type, its address cannot be changed, but its properties can be changed
12. const classA: ClassA = new ClassA();
13. classA.propA = 'Property A';
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment2.ets#L8-L21)

### 指定number的类型

对于number类型，编译器在优化时会区分int和double类型。开发者在初始化number类型的变量时，如果预期是整数类型就初始化为0，小数类型就初始化为0.0，避免将一个number类型初始化为undefined或者null。

【正例】

```
1. function calAddSum(addNum: number): number {
2. // count is expected to be int, do not declare it as undefined/null or 0.0, directly initialize it to 0
3. let count = 0;
4. count += addNum;
5. return count;
6. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment2.ets#L25-L31)

### 减少使用ESObject

ESObject主要用于在ArkTS和TS/JS跨语言调用的场景中作为类型标注，在非跨语言场景中使用ESObject标注类型，会引入不必要的跨语言调用，造成额外的性能开销，建议在非跨语言调用的场景下，避免使用ESObject，引入明确的类型进行标注。

【反例】

```
1. // lib.ets
2. interface TestA {
3. sum: number
4. }

6. export function getObject(value: number): TestA {
7. let obj: TestA = { sum: value };
8. return obj;
9. }

11. // app.ets
12. import { getObject } from 'lib';
13. let obj:ESObject = getObject(123); // Define the accepted type through ESObject.
```

【正例】

1、导出对应的接口类型和方法。

```
1. export interface TestA {
2. sum: number
3. }

5. export function getObject(value: number): TestA {
6. let obj: TestA = { sum: value };
7. return obj;
8. }
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L20-L28)

2、在使用该方法的文件中引入对应的类型。

```
1. import { getObject, TestA } from './segment';

3. let obj: TestA = getObject(123); // Explicitly introduce the label type
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment2.ets#L2-L4)

## 属性访问

### 减少变量的属性查找

在要求性能的场景下，建议通过将全局变量存储为局部变量的方式来减少全局查找，因为访问局部变量的速度要比访问全局变量的速度更快。重复的访问同一个变量，将造成不必要的消耗，尤其当类似的访问出现在循环过程中，其对于性能的影响更大。

在实际开发场景中，可能会遇到在循环中会大量进行一些常量的访问操作，该常量在循环中不会改变，可以提取到循环外部，减少属性访问的次数。例如下面这个示例，Time是一个包含了日期信息的对象，Time.INFO是记录日期的数组，示例中对于Time.INFO[year - Time.START]的访问，在每一次循环中，都会执行一次。

【反例】

```
1. class Time {
2. static START: number = 1987;
3. static INFO: number[] = [2001, 2002, 2003, 2004, 2005, 2006]
4. }

6. function getDay(year: number): number {
7. let totalDays: number = 348;
8. for (let index: number = 0x8000; index > 0x8; index >>= 1) {
9. // The value of Time is the same as that of the value of the value of the value of the value of the time
10. totalDays += ((Time.INFO[year - Time.START] & index) !== 0) ? 1 : 0;
11. }
12. return totalDays;
13. }
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L32-L45)

【正例】

```
1. // Code after optimization
2. class Time {
3. static START: number = 1987;
4. static INFO: number[] = [2001, 2002, 2003, 2004, 2005, 2006];
5. }

7. function getDay(year: number): number {
8. let totalDays: number = 348;
9. // Extract invariants from the loop
10. const info = Time.INFO[year - Time.START];
11. for (let index: number = 0x8000; index > 0x8; index >>= 1) {
12. if ((info & index) !== 0) {
13. totalDays++;
14. }
15. }
16. return totalDays;
17. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment2.ets#L35-L52)

### 给类属性添加访问修饰符

在ArkTS中，对于类结构的属性提供了private、protected和public可访问修饰符。默认情况下一个属性的可访问修饰符为public。选取适当的可访问修饰符可以提升代码的安全性、可读性。

【反例】

```
1. class Counter {
2. // The access modifier is not set. The default value is public
3. count: number = 0;

5. getCount(): number {
6. return this.count;
7. }
8. }

10. // When accessing
11. const counter: Counter = new Counter();
12. console.info(counter.count.toString()); // can be accessed through the instance
13. console.info(counter.getCount().toString());
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L49-L61)

【正例】

```
1. class Counter {
2. // Set the access modifier to private
3. private count: number = 0;

5. public getCount(): number {
6. return this.count;
7. }
8. }

10. // When accessing
11. const counter: Counter = new Counter();
12. let res = counter.getCount();
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment2.ets#L56-L67)

说明

当设置为private时，无法通过对象字面量的方式初始化类，在有需要通过字面量创建、或者直接访问属性时，设置为public。

## 数值计算

### 数值计算使用TypedArray

如果是纯数值计算的场合，推荐使用TypedArray数据结构。TypedArray类型化数组是一种类似数组的对象，其提供了一种用于在内存缓冲中访问原始二进制数据的机制。在一些图像数据处理、加解密的数据计算过程中使用TypedArray可以提高数据处理的效率，因为TypedArray是基于ArrayBuffer实现，在性能方面也能够进行较大提升。

【反例】

```
1. const array1 = new Array(1, 2, 3); // For this scenario, it is recommended that you do not use new Array (1, 2, 3)
2. const array2 = new Array(4, 5, 6); // For this scenario, it is recommended that new Array (4, 5, 6) be not used
3. const res = new Array<number>(3);
4. for (let i = 0; i < 3; i++) {
5. res[i] = array1[i] + array2[i];
6. }
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L65-L71)

【正例】

```
1. const typedArray1 =
2. new Int8Array([1, 2, 3]); // For this scenario, it is recommended that you do not use new Array ([1, 2, 3])
3. const typedArray2 =
4. new Int8Array([4, 5, 6]); // For this scenario, it is recommended that you do not use new Array ([4, 5, 6])
5. const res1 = new Int8Array(3);
6. for (let i = 0; i < 3; i++) {
7. res1[i] = typedArray1[i] + typedArray2[i];
8. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment2.ets#L71-L78)

## 数据结构的使用

### 选取合适的数据结构

有些时候会采用Record的方式作为临时容器来处理属性存取的逻辑，例如如下案例中，对于info执行的操作是set存储以及读取的操作，这里更好的方式是采用标准内置Map以及基础类库提供的高性能容器类如HashMap。HashMap是ArkTS提供的高性能容器类，底层基于哈希表实现（哈希冲突时会在链表与红黑树间动态切换以优化性能），提供了高性能的数据读写操作，可以用来实现键值对的快速读写。

【反例】

```
1. class InfoUtil {
2. getInfo(t1: string, t2: string): string {
3. if (t1 === t2) {
4. return '';
5. }
6. // The common Record object is used as the container
7. let info: Record<string, string> = {};
8. this.setInfo(info);
9. let t3 = info[t2];
10. return (t3 != null) ? t3 : '';
11. }

13. setInfo(info: Record<string, string>) {
14. // The interface actually performs the map operation
15. info.aaa = 'aaa';
16. info.bbb = 'bbb';
17. info.ccc = 'ccc';
18. }
19. }
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L75-L94)

【正例】

```
1. import HashMap from '@kit.ArkTS';

3. class InfoUtil {
4. getInfo(t1: string, t2: string): string {
5. if (t1 === t2) {
6. return '';
7. }
8. // The HashMap is used for read and write operations
9. let info: HashMap<string, string> = new HashMap();
10. this.setInfo(info);
11. let t3 = info.get(t2);
12. return (t3 != null) ? t3 : '';
13. }

15. setInfo(info: HashMap<string, string>) {
16. // ...
17. info.set('aaa', 'aaa');
18. info.set('bbb', 'bbb');
19. info.set('ccc', 'ccc');
20. }
21. }
```

[segment3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment3.ets#L2-L23)

### 避免造成稀疏数组

分配数组时，需要避免使用如下的方式进行处理。当虚拟机在分配大小超过1024KB大小的数组时，会变成用哈希表来存储元素，相对数组用偏移来访问元素速度较慢，在开发时，尽量避免数组变成稀疏数组。

【反例】

```
1. // The following case will become a sparse array
2. // 1. Directly allocate an array with a size of 100,000, and the virtual machine processes it as a hash table to store elements
3. let count = 100000;
4. let result: number[] = new Array(count);
5. // 2. After allocating the array, it will become a sparse array directly, initialize at 9999
6. result[9999] = 0;
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L98-L103)

## 函数声明与使用

### 函数内部变量尽量使用参数传递

能传递参数的尽量传递参数，不要使用闭包，闭包作为参数会多一次闭包的创建和访问。在普通函数中，修改外部作用域的变量时，建议通过函数的参数传递，因为在直接声明时引用外部作用域的变量，如果没有及时清理，可能有内存泄漏的风险。ArkTS中函数参数是引用类型时，作用于引用类型的修改会进行引用传递，函数内对形参的修改也会作用在实参上。

说明

建议开发者优先使用[Code Linter代码检查](../harmonyos-guides/ide-code-linter.md)进行代码检查，重点关注[@performance/hp-performance-no-closures](../harmonyos-guides/ide_hp-performance-no-closures.md)规则。若扫描结果中出现该规则相关问题，可参考本章节提供的优化建议进行调整。

【反例】

```
1. const arr: number[] = [0, 1, 2];

3. function foo() {
4. arr[0] = 1;
5. // arr keeps the use of external variables
6. return arr[0] + arr[1];
7. }

9. let aFoo = foo;
10. aFoo();
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment.ets#L108-L117)

【正例】

```
1. let arr: number[] = [0, 1, 2];

3. // Change to pass by parameters
4. function foo(array: Array<number>): number {
5. array[0] = 1;
6. return array[0] + array[1];
7. }

9. foo(arr);
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment2.ets#L82-L90)

## 高性能导入导出写法

### 减少多层间接导出方式

【反例】在使用export导出方法时，开发者会使用export ... from 'xxx' 的写法进行变量间接导出。特别地，会有开发者在Index文件中，加载非直接导出的文件。

```
1. // main: Hap import har file
2. import { one } from '@har/Index';

4. // har/Index.ets （one level）
5. export * from './InnerIndex';
6. export * from './Utils';
7. export * from './Logs';
8. export * from './Service';
9. export * from './Common';
10. export * from './Feature';

12. // InnerIndex.ets (two level)
13. export * from './ThirdIndex';
14. export { two } from 'Temp';
15. export * from './Utils';
16. export * from './Logs';
17. export * from './Service';

19. // ...more level

21. // LastIndex.ets (N level)
22. export * from './Utils';
23. export { three } from 'Temp';
24. export * from './Numbers';

26. // Numbers.ets
27. export const one: number = 1;
```

[segment6.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment6.ets#L4-L30)

Numbers文件导出变量one ，最终在Index.ets中暴露出去，但例子的实际查找过程为： '@har/Index' -> 'InnerIndex' -> ... -> 'LastIndex' -> 'Numbers'，这些中间层的连接查找都是额外耗时。

推荐写法：在Index.ets等暴露接口的文件中，依赖直接导出变量的文件。

【正例】去掉多层的间接export，即在Index.ets中直接export \* from './Numbers'。

```
1. // main: Hap import har file
2. import { one } from '@har/Index';

4. // har/Index.ets
5. export * from './Numbers'; // only one level

7. // Numbers.ets
8. export const one: number = 1;
```

[segment6.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment6.ets#L34-L41)

此时，实际查找过程为： '@har/Index' -> 'Numbers'。在解析变量导入导出时，ArkTS模块化会进行两步操作：1.通过模块名查找对应的模块；2.在对应模块中查找原始的导出变量。因此，如果中间层增加，会花费更多的时间查找每个模块，增加依赖解析阶段的耗时。

注意

跳过的中间文件如果有顶层代码等写法，可能会对其他文件的执行产生影响，需修改。具体可参考：[模块加载副作用及优化](../harmonyos-guides-V5/arkts-module-side-effects-V5.md)。

### 减少同文件大量export \*导出方式

export \*对于开发者而言是非常简便的导出方式，尤其在Index文件中使用间接导出时，export \*方式可以让开发者减少维护成本，只需要修改导出和导入文件即可，无需修改间接导出层。

对应地，这种写法在性能上会劣化于具名导出方式，因此，在应用对性能要求较高时，推荐使用具名导出方式。

【反例】Index.ets中使用“export \* from '../Numbers'”。

```
1. // main.ets
2. import { one } from '@har/Index';

4. // @har/Index.ets
5. export * from './Numbers';
6. export * from './Utils';
7. export * from './Logs';
8. export * from './Service';
9. export * from './Common';
10. export * from './Feature';

12. // Numbers.ets
13. export const one : number = 1;
```

[segment6.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment6.ets#L45-L57)

在解析命名空间变量导出时，ArkTS模块化会根据变量名one，去Index文件查找对应的导出名，查找过程为：'main -> @har/Index -> Numbers', 在Numbers中找到导出名为one的变量后，记录这条信息。根据ECMA规范，解析命名空间导出不会在此时退出，而是会返回遍历其他导出，确认不存在非同文件的同名导出，因此，整个查找流程为：'main -> @har/Index -> Numbers -> Utils-> Logs -> Service-> Common -> Feature', 确认没有非同文件的同名导出后，才会判定Numbers的导出是正确的记录。

推荐写法：在Index.ets等暴露接口的文件中，依赖直接导出变量的文件。

【正例】Index.ets中使用“export { one } from '.../Numbers'”。

```
1. // main.ets
2. import { one } from '@har/Index';

4. // @har/Index.ets
5. export { one }  from '../Numbers';  // use named export
6. export * from './Utils';
7. export * from './Logs';
8. export * from './Service';
9. export * from './Common';
10. export * from './Feature';

12. // Numbers.ets
13. export const one: number = 1;
```

[segment6.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkTS_high_performance_segment/entry/src/main/ets/segment/segment6.ets#L61-L73)

修改为具名导出后，整体查找流程为：'main -> @har/Index -> Numbers'，不再会去继续向下查找，减少耗时。同理，@har/Index.ets文件下其他export \*导出也推荐改用具名导出。

## 延迟加载Lazy-Import使用指导

随着应用功能持续增加，应用规模不断扩大，依赖的模块文件逐渐变多，应用冷启动加载模块的时间也越来越长。而在实际冷启动过程中执行了很多应用整体依赖但当前未使用的文件，此时可以通过延迟加载（lazy-import）的方法延缓对这些冗余文件的加载，使待加载文件在冷启动阶段不被加载，而在后续导出变量被真正使用时再同步加载执行文件，节省资源以提高应用冷启动性能。

详细请参见：[延迟加载（lazy import）](../harmonyos-guides/arkts-lazy-import.md)。

## 示例代码

* [ArkTS高性能编程代码片段](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/ArkTS_high_performance_segment)
