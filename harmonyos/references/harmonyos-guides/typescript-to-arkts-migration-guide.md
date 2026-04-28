---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typescript-to-arkts-migration-guide
title: 从TypeScript到ArkTS的适配规则
breadcrumb: 指南 > 基础入门 > 学习ArkTS语言 > 从TypeScript到ArkTS的适配指导 > 从TypeScript到ArkTS的适配规则
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:36+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b07c29b95184d64d6b0f6a5640f962349e72cb8b2ec3be3257257dc289baf3b1
---

ArkTS规范约束了TypeScript（简称TS）中影响开发正确性或增加运行时开销的特性。本文罗列了ArkTS中限制的TS特性，并提供重构代码的建议。ArkTS保留了TS大部分语法特性，未在本文中约束的TS特性，ArkTS完全支持。例如，ArkTS支持自定义装饰器，语法与TS一致。按本文约束进行代码重构后，代码仍为合法有效的TS代码。

**示例**

包含关键字var的原始TypeScript代码：

```
1. function addTen(x: number): number {
2. var ten = 10;
3. return x + ten;
4. }
```

重构后的代码：

```
1. function addTen(x: number): number {
2. let ten = 10;
3. return x + ten;
4. }
```

**级别**

约束分为两个级别：错误、警告。

* 错误：必须要遵从的约束。如果不遵从该约束，将会导致程序编译失败。
* 警告：推荐遵从的约束。尽管现在违反该约束不会影响编译流程，但是在将来，违反该约束可能会导致程序编译失败。

**不支持的特性**

目前，不支持的特性主要包括：

* 与降低运行时性能的动态类型相关的特性。
* 需要编译器额外支持从而导致项目构建时间增加的特性。

根据开发者的反馈和实际场景的数据，未来将逐步减少不支持的特性。

## 概述

本节罗列了ArkTS不支持或部分支持的TypeScript特性。完整的列表以及详细的代码示例和重构建议，请参考[约束说明](typescript-to-arkts-migration-guide.md#约束说明)。更多案例请参考[适配指导案例](arkts-more-cases.md)。

### 强制使用静态类型

静态类型是ArkTS的重要特性之一。当程序使用静态类型时，所有类型在编译时已知，这有助于开发者理解代码中的数据结构。编译器可以提前验证代码的正确性，减少运行时的类型检查，从而提升性能。

基于上述考虑，ArkTS中禁止使用any类型。

**示例**

```
1. // 不支持：
2. let res: any = some_api_function('hello', 'world');
3. // 支持：
4. class CallResult {
5. public succeeded(): boolean {
6. return false;
7. }
8. public errorMessage(): string {
9. return '123';
10. }
11. }
12. function some_api_function(param1: string, param2: string): CallResult {
13. return new CallResult();
14. }

16. let res: CallResult = some_api_function('hello', 'world');
17. if (!res.succeeded()) {
18. console.info('Call failed: ' + res.errorMessage());
19. }
```

any类型在TypeScript中并不常见，仅约1%的TypeScript代码库使用。代码检查工具（例如ESLint）也制定了一系列规则来禁止使用any。因此，虽然禁止any将导致代码重构，但重构量很小，有助于整体性能提升。

### 禁止在运行时变更对象布局

为实现最佳性能，ArkTS要求在程序执行期间不能更改对象的布局。换句话说，ArkTS禁止以下行为：

* 向对象中添加新的属性或方法。
* 从对象中删除已有的属性或方法。
* 将任意类型的值赋值给对象属性。

TypeScript编译器已经禁止了许多此类操作。然而，有些操作还是有可能绕过编译器的，例如，使用as any转换对象的类型，或者在编译TS代码时关闭严格类型检查的配置，或者在代码中通过@ts-ignore忽略类型检查。

在ArkTS中，严格类型检查不是可配置项。ArkTS强制进行部分严格类型检查，并通过规范禁止使用any类型，禁止在代码中使用@ts-ignore。

**示例**

```
1. class Point {
2. public x: number = 0
3. public y: number = 0

5. constructor(x: number, y: number) {
6. this.x = x;
7. this.y = y;
8. }
9. }

11. // 无法从对象中删除某个属性，从而确保所有Point对象都具有属性x
12. let p1 = new Point(1.0, 1.0);
13. delete p1.x;           // 在TypeScript和ArkTS中，都会产生编译时错误
14. delete (p1 as any).x;  // 在TypeScript中不会报错；在ArkTS中会产生编译时错误

16. // Point类没有定义命名为z的属性，在程序运行时也无法添加该属性
17. let p2 = new Point(2.0, 2.0);
18. p2.z = 'Label';           // 在TypeScript和ArkTS中，都会产生编译时错误
19. (p2 as any).z = 'Label';   // 在TypeScript中不会报错；在ArkTS中会产生编译时错误

21. // 类的定义确保了所有Point对象只有属性x和y，并且无法被添加其他属性
22. let p3 = new Point(3.0, 3.0);
23. let prop = Symbol();      // 在TypeScript中不会报错；在ArkTS中会产生编译时错误
24. (p3 as any)[prop] = p3.x; // 在TypeScript中不会报错；在ArkTS中会产生编译时错误
25. p3[prop] = p3.x;          // 在TypeScript和ArkTS中，都会产生编译时错误

27. // 类的定义确保了所有Point对象的属性x和y都具有number类型，因此，无法将其他类型的值赋值给它们
28. let p4 = new Point(4.0, 4.0);
29. p4.x = 'Hello!';          // 在TypeScript和ArkTS中，都会产生编译时错误
30. (p4 as any).x = 'Hello!'; // 在TypeScript中不会报错；在ArkTS中会产生编译时错误

32. // 使用符合类定义的Point对象：
33. function distance(p1: Point, p2: Point): number {
34. return Math.sqrt(
35. (p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y)
36. );
37. }
38. let p5 = new Point(5.0, 5.0);
39. let p6 = new Point(6.0, 6.0);
40. console.info('Distance between p5 and p6: ' + distance(p5, p6));
```

修改对象布局会影响代码可读性和运行时性能。定义类后，在其他地方修改对象布局，容易引起困惑乃至引入错误。此外，还需要额外的运行时支持，增加执行开销。这与静态类型约束冲突：使用显式类型时，不应添加或删除属性。

当前，只有少数项目允许在运行时变更对象布局，一些常用的代码检查工具也增加了相应的限制规则。虽然需要少量代码重构，但由此带来的性能提升收益十分可观。

### 限制运算符的语义

为获得更好的性能并鼓励开发者编写更清晰的代码，ArkTS限制了一些运算符的语义。详细的语义限制，请参考[约束说明](typescript-to-arkts-migration-guide.md#约束说明)。

**示例**

```
1. // 一元运算符`+`只能作用于数值类型：
2. let t = +42;   // 合法运算
3. let s = +'42'; // 编译时错误
```

使用额外的语义重载语言运算符会增加语言规范的复杂度，而且，开发者还被迫牢记所有可能的例外情况及对应的处理规则。在特定情况下，这会导致不必要的运行时开销。

当前只有不到1%的代码库使用该特性。因此，尽管限制运算符的语义需要重构代码，但重构量很小且非常容易操作，并且，通过重构能使代码更清晰、具备更高性能。

### 不支持 structural typing

假设两个不相关的类T和U都拥有相同的publicAPI：

```
1. class T {
2. public name: string = ''

4. public greet(): void {
5. console.info('Hello, ' + this.name);
6. }
7. }

9. class U {
10. public name: string = ''

12. public greet(): void {
13. console.info('Greetings, ' + this.name);
14. }
15. }
```

类型为T的值是否能赋给类型为U的变量。

```
1. let u: U = new T(); // 是否允许？
```

类型为T的值是否能传递给接受类型为U的参数的函数。

```
1. function greeter(u: U) {
2. console.info('To ' + u.name);
3. u.greet();
4. }

6. let t: T = new T();
7. greeter(t); // 是否允许？
```

具体采用哪种方法，情况如下：

* T和U没有继承关系或没有implements相同的接口，但由于它们具有相同的publicAPI，它们“在某种程度上是相等的”，因此上述两个问题的答案都是“是”。
* T和U没有继承关系或没有implements相同的接口，应当始终被视为完全不同的类型，因此上述两个问题的答案都是“否”。

采用第一种方法的语言支持structural typing，而采用第二种方法的语言则不支持structural typing。目前TypeScript支持structural typing，而ArkTS不支持。

关于structural typing是否有助于生成清晰、易理解的代码，目前尚无定论。ArkTS不支持structural typing的原因如下：

因为对structural typing的支持是一个重大的特性，需要在语言规范、编译器和运行时进行大量的考虑和仔细的实现。另外，由于ArkTS使用静态类型，运行时为了支持这个特性需要额外的性能开销。

鉴于此，当前我们还不支持该特性。根据实际场景的需求和反馈，我们后续会重新加以考虑。更多案例和建议请参考[约束说明](typescript-to-arkts-migration-guide.md#约束说明)。

## 约束说明

### 对象的属性名必须是合法的标识符

**规则：**arkts-identifiers-as-prop-names

**级别：错误**

**错误码：10605001**

在ArkTS中，对象的属性名不能为数字或字符串。例外：ArkTS支持属性名为字符串字面量和枚举中的字符串值。通过属性名访问类的属性，通过数值索引访问数组元素。

**TypeScript**

```
1. var x = { 'name': 'x', 2: '3' };

3. console.info(x['name']); // x。
4. console.info(x[2]); // 3。
```

**ArkTS**

```
1. class X {
2. public name: string = '';
3. }
4. let x: X = { name: 'x' };
5. console.info(x.name); // x。

7. let y = ['a', 'b', 'c'];
8. console.info(y[2]); // c。

10. // 在需要通过非标识符（即不同类型的key）获取数据的场景中，使用Map<Object, some_type>。
11. let z = new Map<Object, string>();
12. z.set('name', '1');
13. z.set(2, '2');
14. console.info(z.get('name'));  // 1。
15. console.info(z.get(2)); // 2。

17. enum Test {
18. A = 'aaa',
19. B = 'bbb'
20. };

22. let obj: Record<string, number> = {
23. [Test.A]: 1,   // 枚举中的字符串值。
24. [Test.B]: 2,   // 枚举中的字符串值。
25. ['value']: 3   // 字符串字面量。
26. };
```

### 不支持Symbol()API

**规则：**arkts-no-symbol

**级别：错误**

**错误码：10605002**

在ArkTS中，对象布局在编译时确定，不可在运行时更改，因此不支持Symbol() API。该API在静态类型语言中通常没有实际意义。

ArkTS只支持Symbol.iterator。

### 不支持以#开头的私有字段

**规则：**arkts-no-private-identifiers

**级别：错误**

**错误码：10605003**

ArkTS不支持使用#符号开头声明的私有字段。改用private关键字。

**TypeScript**

```
1. class C {
2. #foo: number = 42
3. }
```

**ArkTS**

```
1. class C {
2. private foo: number = 42;
3. }
```

### 类型、命名空间的命名必须唯一

**规则：**arkts-unique-names

**级别：错误**

**错误码：10605004**

类型（类、接口、枚举）和命名空间的名称必须唯一，并且不能与其他名称（如变量名、函数名）重复。

**TypeScript**

```
1. let X: string
2. type X = number[] // 类型的别名与变量同名。
```

**ArkTS**

```
1. let X: string;
2. type T = number[]; // 为避免名称冲突，此处不允许使用X。
```

### 使用let而非var

**规则：**arkts-no-var

**级别：错误**

**错误码：10605005**

let关键字可以在块级作用域中声明变量，帮助程序员避免错误。因此，ArkTS不支持var，请使用let声明变量。

**TypeScript**

```
1. function f(shouldInitialize: boolean) {
2. if (shouldInitialize) {
3. var x = 'b';
4. }
5. return x;
6. }

8. console.info(f(true));  // b
9. console.info(f(false)); // undefined

11. let upperLet = 0;
12. {
13. var scopedVar = 0;
14. let scopedLet = 0;
15. upperLet = 5;
16. }
17. scopedVar = 5; // 可见
18. scopedLet = 5; // 编译时错误
```

**ArkTS**

```
1. function f(shouldInitialize: boolean): string {
2. let x: string = 'a';
3. if (shouldInitialize) {
4. x = 'b';
5. }
6. return x;
7. }

9. console.info(f(true));  // b
10. console.info(f(false)); // a

12. let upperLet = 0;
13. let scopedVar = 0;
14. {
15. let scopedLet = 0;
16. upperLet = 5;
17. }
18. scopedVar = 5;
19. scopedLet = 5; // 编译时错误
```

### 使用具体的类型而非any或unknown

**规则：**arkts-no-any-unknown

**级别：错误**

**错误码：10605008**

ArkTS不支持any和unknown类型。显式指定具体类型。

**TypeScript**

```
1. let value1: any
2. value1 = true;
3. value1 = 42;

5. let value2: unknown
6. value2 = true;
7. value2 = 42;
```

**ArkTS**

```
1. let valueB: boolean = true; // 或者 let valueB = true。
2. let valueN: number = 42; // 或者 let valueN = 42。
3. let valueO1: Object = true;
4. let valueO2: Object = 42;
```

### 使用class而非具有call signature的类型

**规则：**arkts-no-call-signatures

**级别：错误**

**错误码：10605014**

ArkTS不支持对象类型中包含call signature。

**TypeScript**

```
1. type DescribableFunction = {
2. description: string
3. (someArg: string): string // call signature。
4. }

6. function doSomething(fn: DescribableFunction): void {
7. console.info(fn.description + ' returned ' + fn(''));
8. }
```

**ArkTS**

```
1. class DescribableFunction {
2. public description: string;
3. public invoke(someArg: string): string {
4. return someArg;
5. }
6. constructor() {
7. this.description = 'desc';
8. }
9. }

11. function doSomething(fn: DescribableFunction): void {
12. console.info(fn.description + ' returned ' + fn.invoke(''));
13. }

15. doSomething(new DescribableFunction());
```

### 使用class而非具有构造签名的类型

**规则：**arkts-no-ctor-signatures-type

**级别：错误**

**错误码：10605015**

ArkTS不支持对象类型中的构造签名。改用类。

**TypeScript**

```
1. class SomeObject { }

3. type SomeConstructor = {
4. new(s: string): SomeObject
5. }

7. function fn(ctor: SomeConstructor) {
8. return new ctor('hello');
9. }
```

**ArkTS**

```
1. class SomeObject {
2. public f: string;
3. constructor (s: string) {
4. this.f = s;
5. }
6. }

8. function fn(s: string): SomeObject {
9. return new SomeObject(s);
10. }
```

### 仅支持一个静态块

**规则：**arkts-no-multiple-static-blocks

**级别：错误**

**错误码：10605016**

ArkTS不允许类中存在多个静态块。如果存在多个静态块语句，请将其合并到一个静态块中。

**TypeScript**

```
1. class C {
2. static s: string

4. static {
5. C.s = 'aa'
6. }
7. static {
8. C.s = C.s + 'bb'
9. }
10. }
```

**ArkTS**

```
1. class C {
2. public static s: string;

4. static {
5. C.s = 'aa';
6. C.s = C.s + 'bb';
7. }
8. }
```

### 不支持index signature

**规则：**arkts-no-indexed-signatures

**级别：错误**

**错误码：10605017**

ArkTS不允许index signature，改用数组。

**TypeScript**

```
1. // 带index signature的接口：
2. interface StringArray {
3. [index: number]: string
4. }

6. function getStringArray(): StringArray {
7. return ['a', 'b', 'c'];
8. }

10. const myArray: StringArray = getStringArray();
11. const secondItem = myArray[1];
```

**ArkTS**

```
1. class X {
2. public f: string[] = [];
3. }

5. let myArray: X = new X();
6. const secondItem = myArray.f[1];
```

### 使用继承而非intersection type

**规则：**arkts-no-intersection-types

**级别：错误**

**错误码：10605019**

目前ArkTS不支持intersection type，可以使用继承作为替代方案。

**TypeScript**

```
1. interface Identity {
2. id: number
3. name: string
4. }

6. interface Contact {
7. email: string
8. phoneNumber: string
9. }

11. type Employee = Identity & Contact
```

**ArkTS**

```
1. interface Identity {
2. id: number;
3. name: string;
4. }

6. interface Contact {
7. email: string;
8. phoneNumber: string;
9. }

11. interface Employee extends Identity,  Contact {}
```

### 不支持this类型

**规则：**arkts-no-typing-with-this

**级别：错误**

**错误码：10605021**

ArkTS不支持this类型，改用显式具体类型。

**TypeScript**

```
1. interface ListItem {
2. getHead(): this
3. }

5. class C {
6. n: number = 0

8. m(c: this) {
9. // ...
10. }
11. }
```

**ArkTS**

```
1. interface testListItem {
2. getHead(): testListItem;
3. }

5. class C {
6. public n: number = 0;

8. m(c: C) {
9. // ...
10. }
11. }
```

### 不支持条件类型

**规则：**arkts-no-conditional-types

**级别：错误**

**错误码：10605022**

ArkTS不支持条件类型别名，建议引入带显式约束的新类型，或使用Object进行逻辑重构。

不支持infer关键字。

**TypeScript**

```
1. type X<T> = T extends number ? T : never;
2. type Y<T> = T extends Array<infer Item> ? Item : never;
```

**ArkTS**

```
1. // 在类型别名中提供显式约束。
2. type X1<T extends number> = T;

4. // 用Object重写，类型控制较少，需要更多的类型检查以确保安全。
5. type X2<T> = Object;

7. // Item必须作为泛型参数使用，并能正确实例化。
8. type YI<Item, T extends Array<Item>> = Item;
```

### 不支持在constructor中声明字段

**规则：**arkts-no-ctor-prop-decls

**级别：错误**

**错误码：10605025**

ArkTS禁止在构造函数中声明类字段，所有字段都必须在class作用域内显式声明。

**TypeScript**

```
1. class Person {
2. constructor(
3. protected ssn: string,
4. private firstName: string,
5. private lastName: string
6. ) {
7. this.ssn = ssn;
8. this.firstName = firstName;
9. this.lastName = lastName;
10. }

12. getFullName(): string {
13. return this.firstName + ' ' + this.lastName;
14. }
15. }
```

**ArkTS**

```
1. class Person {
2. protected ssn: string;
3. private firstName: string;
4. private lastName: string;

6. constructor(ssn: string, firstName: string, lastName: string) {
7. this.ssn = ssn;
8. this.firstName = firstName;
9. this.lastName = lastName;
10. }

12. getFullName(): string {
13. return this.firstName + ' ' + this.lastName;
14. }
15. }
```

### 接口中不支持构造签名

**规则：**arkts-no-ctor-signatures-iface

**级别：错误**

**错误码：10605027**

ArkTS语法禁止在接口（interface）中定义构造签名。作为替代方案，建议使用普通函数或方法来实现相同功能。

**TypeScript**

```
1. interface I {
2. new(s: string): I;
3. }

5. function fn(i: I) {
6. return new i('hello');
7. }
```

**ArkTS**

```
1. interface I {
2. create(s: string): I;
3. }

5. function fn(i: I) {
6. return i.create('hello');
7. }
```

### 不支持索引访问类型

**规则：**arkts-no-aliases-by-index

**级别：错误**

**错误码：10605028**

ArkTS不支持索引访问类型。

### 不支持通过索引访问字段

**规则：**arkts-no-props-by-index

**级别：错误**

**错误码：10605029**

ArkTS不支持动态声明字段，不支持动态访问字段。只能访问已在类中声明或者继承可见的字段，访问其他字段将会造成编译时错误。

使用点操作符访问字段，例如（obj.field），不支持索引访问（obj['field']）。

ArkTS支持通过索引访问TypedArray（例如Int32Array）中的元素。

**TypeScript**

```
1. class Point {
2. x: string = '';
3. y: string = '';
4. }
5. let p: Point = { x: '1', y: '2' };
6. console.info(p['x']); // 1。

8. class Person {
9. name: string = '';
10. age: number = 0;
11. [key: string]: string | number;
12. }

14. let person: Person = {
15. name: 'John',
16. age: 30,
17. email: '***@example.com',
18. phoneNumber: '18*********',
19. }
```

**ArkTS**

```
1. class Point {
2. x: string = ''
3. y: string = ''
4. }
5. let p: Point = {x: '1', y: '2'};
6. console.info(p.x); // 1

8. class Person {
9. name: string
10. age: number
11. email: string
12. phoneNumber: string

14. constructor(name: string, age: number, email: string,
15. phoneNumber: string) {
16. this.name = name;
17. this.age = age;
18. this.email = email;
19. this.phoneNumber = phoneNumber;
20. }
21. }

23. let person = new Person('John', 30, '***@example.com', '18*********');
24. console.info(person['name']);     // 编译时错误
25. console.info(person.unknownProperty); // 编译时错误

27. let arr = new Int32Array(1);
28. arr[0];
```

### 不支持structural typing

**规则：**arkts-no-structural-typing

**级别：错误**

**错误码：10605030**

ArkTS不支持structural typing，编译器无法比较两种类型的publicAPI并决定它们是否相同。使用其他机制，例如继承、接口或类型别名。

**TypeScript**

```
1. interface I1 {
2. f(): string
3. }

5. interface I2 { // I2等价于I1
6. f(): string
7. }

9. class X {
10. n: number = 0
11. s: string = ''
12. }

14. class Y { // Y等价于X
15. n: number = 0
16. s: string = ''
17. }

19. let x = new X();
20. let y = new Y();

22. // 将X对象赋值给Y对象
23. y = x;

25. // 将Y对象赋值给X对象
26. x = y;

28. function foo(x: X) {
29. console.info(x.n + x.s);
30. }

32. // 由于X和Y的API是等价的，所以X和Y是等价的
33. foo(new X());
34. foo(new Y());
```

**ArkTS**

```
1. interface I1 {
2. f(): string
3. }

5. type I2 = I1 // I2是I1的别名

7. class B {
8. n: number = 0
9. s: string = ''
10. }

12. // D是B的继承类，构建了子类型和父类型的关系
13. class D extends B {
14. constructor() {
15. super()
16. }
17. }

19. let b = new B();
20. let d = new D();

22. console.info('Assign D to B');
23. b = d; // 合法赋值，因为B是D的父类

25. // 将b赋值给d将会引起编译时错误
26. // d = b

28. interface Z {
29. n: number
30. s: string
31. }

33. // 类X implements 接口Z，构建了X和Y的关系
34. class X implements Z {
35. n: number = 0
36. s: string = ''
37. }

39. // 类Y implements 接口Z，构建了X和Y的关系
40. class Y implements Z {
41. n: number = 0
42. s: string = ''
43. }

45. let x: Z = new X();
46. let y: Z = new Y();

48. console.info('Assign X to Y');
49. y = x // 合法赋值，它们是相同的类型

51. console.info('Assign Y to X');
52. x = y // 合法赋值，它们是相同的类型

54. function foo(c: Z): void {
55. console.info(c.n + c.s);
56. }

58. // 类X和类Y implement 相同的接口，因此下面的两个函数调用都是合法的
59. foo(new X());
60. foo(new Y());
```

### 需要显式标注泛型函数类型实参

**规则：**arkts-no-inferred-generic-params

**级别：错误**

**错误码：10605034**

如果可以从传递给泛型函数的参数中推断出具体类型，ArkTS允许省略泛型类型实参。否则，省略泛型类型实参会发生编译时错误。

禁止仅基于泛型函数返回类型推断泛型类型参数。

**TypeScript**

```
1. function choose<T>(x: T, y: T): T {
2. return Math.random() < 0.5 ? x: y;
3. }

5. let x = choose(10, 20);   // 推断choose<number>(...)
6. let y = choose('10', 20); // 编译时错误

8. function greet<T>(): T {
9. return 'Hello' as T;
10. }
11. let z = greet() // T的类型被推断为“unknown”
```

**ArkTS**

```
1. function choose<T>(x: T, y: T): T {
2. return Math.random() < 0.5 ? x: y;
3. }

5. let x = choose(10, 20);   // 推断choose<number>(...)
6. let y = choose('10', 20); // 编译时错误

8. function greet<T>(): T {
9. return 'Hello' as T;
10. }
11. let z = greet<string>();
```

### 需要显式标注对象字面量的类型

**规则：**arkts-no-untyped-obj-literals

**级别：错误**

**错误码：10605038**

在 ArkTS 中，需要显式标注对象字面量的类型，否则将导致编译时错误。在某些场景下，编译器可以根据上下文推断出字面量的类型。

在以下上下文中不支持使用字面量初始化类和接口：

* 初始化具有any、Object或object类型的任何对象
* 初始化带有方法的类或接口
* 初始化包含自定义含参数的构造函数的类
* 初始化带readonly字段的类

**例子1**

**TypeScript**

```
1. let o1 = { n: 42, s: 'foo' };
2. let o2: Object = { n: 42, s: 'foo' };
3. let o3: object = { n: 42, s: 'foo' };

5. let oo: Object[] = [{ n: 1, s: '1' }, { n: 2, s: '2' }];
```

**ArkTS**

```
1. class C1 {
2. public n: number = 0;
3. public s: string = '';
4. }

6. let o1: C1 = {n: 42, s: 'foo'};
7. let o2: C1 = {n: 42, s: 'foo'};
8. let o3: C1 = {n: 42, s: 'foo'};

10. let oo: C1[] = [{n: 1, s: '1'}, {n: 2, s: '2'}];
```

**例子2**

**TypeScript**

```
1. class C2 {
2. s: string;
3. constructor(s: string) {
4. this.s = 's =' + s;
5. }
6. }
7. let o4: C2 = { s: 'foo' };
```

**ArkTS**

```
1. class C2 {
2. public s: string;
3. constructor(s: string) {
4. this.s = 's =' + s;
5. }
6. }
7. let o4 = new C2('foo');
```

**例子3**

**TypeScript**

```
1. class C3 {
2. readonly n: number = 0;
3. readonly s: string = '';
4. }
5. let o5: C3 = { n: 42, s: 'foo' };
```

**ArkTS**

```
1. class C3 {
2. public n: number = 0;
3. public s: string = '';
4. }
5. let o5: C3 = {n: 42, s: 'foo'};
```

**例子4**

**TypeScript**

```
1. abstract class A { }
2. let o6: A = {};
```

**ArkTS**

```
1. abstract class A {}
2. class C extends A {}
3. let o6: C = {}; // 或 let o6: C = new C()。
```

**例子5**

**TypeScript**

```
1. class C4 {
2. n: number = 0;
3. s: string = '';
4. f() {
5. console.info('Hello');
6. }
7. }
8. let o7: C4 = { n: 42, s: 'foo', f: () => { } };
```

**ArkTS**

```
1. class C4 {
2. public n: number = 0;
3. public s: string = '';
4. f() {
5. console.info('Hello');
6. }
7. }
8. let o7 = new C4();
9. o7.n = 42;
10. o7.s = 'foo';
```

**例子6**

**TypeScript**

```
1. class Point {
2. x: number = 0;
3. y: number = 0;
4. }

6. function getPoint(o: Point): Point {
7. return o;
8. }

10. // TS支持structural typing，可以推断p的类型为Point。
11. let p = { x: 5, y: 10 };
12. getPoint(p);

14. // 可通过上下文推断出对象字面量的类型为Point。
15. getPoint({ x: 5, y: 10 });
```

**ArkTS**

```
1. class Point {
2. public x: number = 0;
3. public y: number = 0;

5. // 在字面量初始化之前，使用constructor()创建一个有效对象。
6. // 由于没有为Point定义构造函数，编译器将自动添加一个默认构造函数。
7. }

9. function getPoint(o: Point): Point {
10. return o;
11. }

13. // 字面量初始化需要显式定义类型。
14. let p: Point = {x: 5, y: 10};
15. getPoint(p);

17. // getPoint接受Point类型，字面量初始化生成一个Point的新实例。
18. getPoint({x: 5, y: 10});
```

### 对象字面量不能用于类型声明

**规则：**arkts-no-obj-literals-as-types

**级别：错误**

**错误码：10605040**

ArkTS不支持使用对象字面量声明类型，建议使用类或接口声明类型。

**TypeScript**

```
1. let o: { x: number, y: number } = {
2. x: 2,
3. y: 3
4. }

6. type S = Set<{ x: number, y: number }>
```

**ArkTS**

```
1. class O {
2. public x: number = 0;
3. public y: number = 0;
4. }

6. let o: O = {x: 2, y: 3};

8. type S = Set<O>;
```

### 数组字面量必须仅包含可推断类型的元素

**规则：**arkts-no-noninferrable-arr-literals

**级别：错误**

**错误码：10605043**

ArkTS将数组字面量的类型推断为所有元素的联合类型。如果其中任何一个元素的类型无法推导，则在编译时会发生错误。

**TypeScript**

```
1. let a = [{ n: 1, s: '1' }, { n: 2, s: '2' }];
```

**ArkTS**

```
1. class C {
2. public n: number = 0
3. public s: string = ''
4. }

6. let a1 = [{n: 1, s: '1'} as C, {n: 2, s: '2'} as C]; // a1的类型为“C[]”。
7. let a2: C[] = [{n: 1, s: '1'}, {n: 2, s: '2'}];    // a2的类型为“C[]”。
```

### 使用箭头函数而非函数表达式

**规则：**arkts-no-func-expressions

**级别：错误**

**错误码：10605046**

ArkTS不支持函数表达式，使用箭头函数（=>）。

**TypeScript**

```
1. let f = function (s: string) {
2. console.info(s);
3. }
```

**ArkTS**

```
1. let f = (s: string) => {
2. console.info(s);
3. }
```

### 不支持使用类表达式

**规则：**arkts-no-class-literals

**级别：错误**

**错误码：10605050**

ArkTS不支持类表达式，必须显式声明一个类。

**TypeScript**

```
1. const Rectangle = class {
2. constructor(height: number, width: number) {
3. this.height = height;
4. this.width = width;
5. }

7. height;
8. width;
9. }

11. const rectangle = new Rectangle(0.0, 0.0);
```

**ArkTS**

```
1. class TestRectangle {
2. constructor(testHeight: number, testWidth: number) {
3. this.testHeight = testHeight;
4. this.testWidth = testWidth;
5. }

7. public testHeight: number;
8. public testWidth: number;
9. }

11. const rectangle = new TestRectangle(0.0, 0.0);
```

### 类不允许implements

**规则：**arkts-implements-only-iface

**级别：错误**

**错误码：10605051**

ArkTS中只有接口可以被implements，类不允许被implements。

**TypeScript**

```
1. class C {
2. foo() { }
3. }

5. class C1 implements C {
6. foo() { }
7. }
```

**ArkTS**

```
1. interface C {
2. foo(): void
3. }

5. class C1 implements C {
6. foo() {}
7. }
```

### 不支持修改对象的方法

**规则：**arkts-no-method-reassignment

**级别：错误**

**错误码：10605052**

ArkTS不支持修改对象的方法。在静态语言中，对象布局固定，类的所有实例共享同一个方法。

若需为特定对象添加方法，可封装函数或采用继承机制。

**TypeScript**

```
1. class C {
2. foo() {
3. console.info('foo');
4. }
5. }

7. function bar() {
8. console.info('bar');
9. }

11. let c1 = new C();
12. let c2 = new C();
13. c2.foo = bar;

15. c1.foo(); // foo。
16. c2.foo(); // bar。
```

**ArkTS**

```
1. class C {
2. foo() {
3. console.info('foo');
4. }
5. }

7. class Derived extends C {
8. foo() {
9. console.info('Extra');
10. super.foo();
11. }
12. }

14. function bar() {
15. console.info('bar');
16. }

18. let c1 = new C();
19. let c2 = new C();
20. c1.foo(); // foo。
21. c2.foo(); // foo。

23. let c3 = new Derived();
24. c3.foo(); // Extra foo。
```

### 类型转换仅支持as T语法

**规则：**arkts-as-casts

**级别：错误**

**错误码：10605053**

在ArkTS中，as关键字是类型转换的唯一语法，错误的类型转换会导致编译时错误或者运行时抛出ClassCastException异常。ArkTS不支持使用<type>语法进行类型转换。

需要将primitive类型（如number或boolean）转换为引用类型时，请使用new表达式。

**TypeScript**

```
1. class testShape { }
2. class testCircle extends testShape { x: number = 5 }
3. class testSquare extends testShape { y: string = 'a' }

5. function createShape(): testShape {
6. return new testCircle();
7. }

9. let c1 = <testCircle>createShape();

11. let c2 = createShape() as testCircle;

13. // 如果转换错误，不会产生编译时或运行时报错。
14. let c3 = createShape() as testSquare;
15. console.info(c3.y); // undefined。

17. // 在TS中，由于`as`关键字不会在运行时生效，所以`instanceof`的左操作数不会在运行时被装箱成引用类型。
18. let e1 = (5.0 as Number) instanceof Number; // false。

20. // 创建Number对象，获得预期结果：
21. let e2 = (new Number(5.0)) instanceof Number; // true。
```

**ArkTS**

```
1. class TestShape {}
2. class TestCircle extends TestShape { public x: number = 5 }

5. function createShape(): TestShape {
6. return new TestCircle();
7. }

10. let c1 = createShape() as TestCircle;

12. // 创建Number对象，获得预期结果：
13. let e1 = (new Number(5.0)) instanceof Number; // true
```

### 不支持JSX表达式

**规则：**arkts-no-jsx

**级别：错误**

**错误码：10605054**

不支持使用JSX。

### 一元运算符+、-和~仅适用于数值类型

**规则：**arkts-no-polymorphic-unops

**级别：错误**

**错误码：10605055**

ArkTS对一元运算符实施严格的类型检查，仅允许操作数值类型。与TypeScript不同，ArkTS禁止隐式的字符串转换到数值，开发者必须使用显式类型的转换方法。

**TypeScript**

```
1. let a = +5;    // 5（number类型）
2. let b = +'5';    // 5（number类型）
3. let c = -5;    // -5（number类型）
4. let d = -'5';    // -5（number类型）
5. let e = ~5;    // -6（number类型）
6. let f = ~'5';    // -6（number类型）
7. let g = +'string'; // NaN（number类型）

9. function returnTen(): string {
10. return '-10';
11. }

13. function returnString(): string {
14. return 'string';
15. }

17. let x = +returnTen();  // -10（number类型）
18. let y = +returnString(); // NaN
```

**ArkTS**

```
1. let a = +5;    // 5（number类型）
2. let b = +'5';    // 编译时错误
3. let c = -5;    // -5（number类型）
4. let d = -'5';    // 编译时错误
5. let e = ~5;    // -6（number类型）
6. let f = ~'5';    // 编译时错误
7. let g = +'string'; // 编译时错误

9. function returnTen(): string {
10. return '-10';
11. }

13. function returnString(): string {
14. return 'string';
15. }

17. let x = +returnTen();  // 编译时错误
18. let y = +returnString(); // 编译时错误
```

### 不支持delete运算符

**规则：**arkts-no-delete

**级别：错误**

**错误码：10605059**

在ArkTS中，对象布局于编译时确定，运行时不可更改，因此删除属性的操作无意义。

**TypeScript**

```
1. class Point {
2. x?: number = 0.0;
3. y?: number = 0.0;
4. }

6. let p = new Point();
7. delete p.y;
```

**ArkTS**

```
1. // 可以声明一个可空类型并使用null作为缺省值。
2. class Point {
3. public x: number | null = 0;
4. public y: number | null = 0;
5. }

7. let p = new Point();
8. p.y = null;
```

### 仅允许在表达式中使用typeof运算符

**规则：**arkts-no-type-query

**级别：错误**

**错误码：10605060**

ArkTS仅支持在表达式中使用typeof运算符，不允许使用typeof作为类型。

**TypeScript**

```
1. let n1 = 42;
2. let s1 = 'foo';
3. console.info(typeof n1); // 'number'。
4. console.info(typeof s1); // 'string'。
5. let n2: typeof n1;
6. let s2: typeof s1;
```

**ArkTS**

```
1. let n1 = 42;
2. let s1 = 'foo';
3. console.info(typeof n1); // 'number'。
4. console.info(typeof s1); // 'string'。
5. let n2: number;
6. let s2: string;
```

### 部分支持instanceof运算符

**规则：**arkts-instanceof-ref-types

**级别：错误**

**错误码：10605065**

TypeScript中，instanceof运算符的左操作数类型必须为any类型、对象类型或类型参数，否则结果为false。ArkTS中，instanceof运算符的左操作数类型必须为引用类型（如对象、数组或函数），否则会发生编译时错误。此外，左操作数必须是对象实例。

**TypeScript**

```
1. let num: number = 42;
2. let result = num instanceof Number;
3. console.info('result = ', result); // result = false。
```

**ArkTS**

```
1. let num: number = 42;
2. let result = num instanceof Number; // 编译报错
```

### 不支持in运算符

**规则：**arkts-no-in

**级别：错误**

**错误码：10605066**

在ArkTS中，对象布局在编译时已知且运行时无法修改，因此不支持in运算符。需要检查类成员是否存在时，使用instanceof代替。

**TypeScript**

```
1. class Person {
2. name: string = '';
3. }
4. let p = new Person();

6. let b = 'name' in p; // true。
```

**ArkTS**

```
1. class Person {
2. public name: string = '';
3. }
4. let p = new Person();

6. let b = p instanceof Person; // true，且属性name一定存在。
```

### 不支持解构赋值

**规则：**arkts-no-destruct-assignment

**级别：错误**

**错误码：10605069**

ArkTS不支持解构赋值。可使用其他替代方法，例如，使用临时变量。

**TypeScript**

```
1. let [one, two] = [1, 2]; // 此处需要分号。
2. [one, two] = [two, one];

4. let head, tail;
5. [head, ...tail] = [1, 2, 3, 4];
```

**ArkTS**

```
1. let arr: number[] = [1, 2];
2. let one = arr[0];
3. let two = arr[1];

5. let tmp = one;
6. one = two;
7. two = tmp;

9. let data: Number[] = [1, 2, 3, 4];
10. let head = data[0];
11. let tail: Number[] = [];
12. for (let i = 1; i < data.length; ++i) {
13. tail.push(data[i]);
14. }
```

### 逗号运算符,仅用在for循环语句中

**规则：**arkts-no-comma-outside-loops

**级别：错误**

**错误码：10605071**

在ArkTS中，逗号运算符仅适用于for循环语句，用于明确执行顺序。

注意

* 这与声明变量和函数参数传递时使用的逗号分隔符不同。

**TypeScript**

```
1. for (let i = 0, j = 0; i < 10; ++i, j += 2) {
2. // ...
3. }

5. let x = 0;
6. x = (++x, x++); // 1。
```

**ArkTS**

```
1. for (let i = 0, j = 0; i < 10; ++i, j += 2) {
2. // ...
3. }

5. // 通过语句表示执行顺序，而非逗号运算符。
6. let x = 0;
7. ++x;
8. x = x++;
```

### 不支持解构变量声明

**规则：**arkts-no-destruct-decls

**级别：错误**

**错误码：10605074**

ArkTS不支持解构变量声明。解构变量声明是一个依赖于结构兼容性的动态特性，且解构声明中的名称必须与被解构对象中的属性名称一致。

**TypeScript**

```
1. class Point {
2. x: number = 0.0;
3. y: number = 0.0;
4. }

6. function returnZeroPoint(): Point {
7. return new Point();
8. }

10. let { x, y } = returnZeroPoint();
```

**ArkTS**

```
1. class Point {
2. public x: number = 0.0;
3. public y: number = 0.0;
4. }

6. function returnZeroPoint(): Point {
7. return new Point();
8. }

10. // 创建一个局部变量来处理每个字段。
11. let zp = returnZeroPoint();
12. let x = zp.x;
13. let y = zp.y;
```

### 不支持在catch语句标注类型

**规则：**arkts-no-types-in-catch

**级别：错误**

**错误码：10605079**

TypeScript的catch语句中，只能标注any或unknown类型。ArkTS不支持这些类型，应省略类型标注。

**TypeScript**

```
1. try {
2. // ...
3. } catch (a: unknown) {
4. // 处理异常。
5. }
```

**ArkTS**

```
1. try {
2. // ...
3. } catch (a) {
4. // 处理异常。
5. }
```

### 不支持for .. in

**规则：**arkts-no-for-in

**级别：错误**

**错误码：10605080**

在ArkTS中，对象布局在编译时确定且运行时不可修改，因此不支持使用for .. in迭代对象属性。

**TypeScript**

```
1. let a: string[] = ['1.0', '2.0', '3.0'];
2. for (let i in a) {
3. console.info(a[i]);
4. }
```

**ArkTS**

```
1. let a: string[] = ['1.0', '2.0', '3.0'];
2. for (let i = 0; i < a.length; ++i) {
3. console.info(a[i]);
4. }
```

### 不支持映射类型

**规则：**arkts-no-mapped-types

**级别：错误**

**错误码：10605083**

ArkTS不支持映射类型，使用其他语法表示相同语义。

**TypeScript**

```
1. type OptionsFlags<Type> = {
2. [Property in keyof Type]: boolean
3. }
```

**ArkTS**

```
1. class C {
2. public n: number = 0;
3. public s: string = '';
4. }

6. class CFlags {
7. public n: boolean = false;
8. public s: boolean = false;
9. }
```

### 不支持with语句

**规则：**arkts-no-with

**级别：错误**

**错误码：10605084**

ArkTS不支持with语句，使用其他语法来表示相同的语义。

**TypeScript**

```
1. with (Math) { // 编译时错误, 但是仍能生成JavaScript代码
2. let r: number = 42;
3. let area: number = PI * r * r;
4. }
```

**ArkTS**

```
1. let r: number = 42;
2. let area: number = Math.PI * r * r;
```

### 限制throw语句中表达式的类型

**规则：**arkts-limited-throw

**级别：错误**

**错误码：10605087**

ArkTS只支持抛出Error类或其派生类的实例。禁止抛出其他类型的数据，例如number或string。

**TypeScript**

```
1. throw 4;
2. throw '';
3. throw new Error();
```

**ArkTS**

```
1. throw new Error();
```

### 限制省略函数返回类型标注

**规则：**arkts-no-implicit-return-types

**级别：错误**

**错误码：10605090**

ArkTS在部分场景中支持对函数返回类型进行推断。当return语句中的表达式是对某个函数或方法进行调用，且该函数或方法的返回类型没有被显著标注时，会出现编译时错误。在这种情况下，请标注函数返回类型。

**TypeScript**

```
1. // 只有在开启noImplicitAny选项时会产生编译时错误。
2. function f(x: number) {
3. if (x <= 0) {
4. return x;
5. }
6. return g(x);
7. }

9. // 只有在开启noImplicitAny选项时会产生编译时错误。
10. function g(x: number) {
11. return f(x - 1);
12. }

14. function doOperation(x: number, y: number) {
15. return x + y;
16. }

18. f(10);
19. doOperation(2, 3);
```

**ArkTS**

```
1. // 需标注返回类型：
2. function f(x: number): number {
3. if (x <= 0) {
4. return x;
5. }
6. return g(x);
7. }

9. // 可以省略返回类型，返回类型可以从f的类型标注推导得到。
10. function g(x: number): number {
11. return f(x - 1);
12. }

14. // 可以省略返回类型。
15. function doOperation(x: number, y: number) {
16. return x + y;
17. }

19. f(10);
20. doOperation(2, 3);
```

### 不支持参数解构的函数声明

**规则：**arkts-no-destruct-params

**级别：错误**

**错误码：10605091**

ArkTS要求实参必须直接传递给函数，且必须指定到形参。

**TypeScript**

```
1. function drawText({ text = '', location: [x, y] = [0, 0], bold = false }) {
2. text;
3. x;
4. y;
5. bold;
6. }

8. drawText({ text: 'Hello, world!', location: [100, 50], bold: true });
```

**ArkTS**

```
1. function drawText(text: String, location: number[], bold: boolean) {
2. let x = location[0];
3. let y = location[1];
4. text;
5. x;
6. y;
7. bold;
8. }

10. function main() {
11. drawText('Hello, world!', [100, 50], true);
12. }
```

### 不支持在函数内声明函数

**规则：**arkts-no-nested-funcs

**级别：错误**

**错误码：10605092**

ArkTS不支持在函数内声明函数，改用lambda函数。

**TypeScript**

```
1. function addNum(a: number, b: number): void {

3. // 函数内声明函数。
4. function logToConsole(message: string): void {
5. console.info(message);
6. }

8. let result = a + b;

10. // 调用函数。
11. logToConsole('result is ' + result);
12. }
```

**ArkTS**

```
1. function addNum(a: number, b: number): void {
2. // 使用lambda函数代替声明函数。
3. let logToConsole: (message: string) => void = (message: string): void => {
4. console.info(message);
5. }

7. let result = a + b;

9. logToConsole('result is ' + result);
10. }
```

### 不支持在函数和类的静态方法中使用this

**规则：**arkts-no-standalone-this

**级别：错误**

**错误码：10605093**

ArkTS中this只能在类的实例方法中使用，不支持在函数和类的静态方法中使用。

**TypeScript**

```
1. function foo(i: string) {
2. this.count = i; // 只有在开启noImplicitThis选项时会产生编译时错误。
3. }

5. class A {
6. count: string = 'a';
7. m = foo;
8. }

10. let a = new A();
11. console.info(a.count); // 打印a。
12. a.m('b');
13. console.info(a.count); // 打印b。
```

**ArkTS**

```
1. class A {
2. public count: string = 'a'
3. m(i: string): void {
4. this.count = i;
5. }
6. }

8. function main(): void {
9. let a = new A();
10. console.info(a.count);  // 打印a。
11. a.m('b');
12. console.info(a.count);  // 打印b。
13. }
```

### 不支持生成器函数

**规则：**arkts-no-generators

**级别：错误**

**错误码：10605094**

目前ArkTS不支持生成器函数，可使用async或await机制处理并行任务。

**TypeScript**

```
1. function* counter(start: number, end: number) {
2. for (let i = start; i <= end; i++) {
3. yield i;
4. }
5. }

7. for (let num of counter(1, 5)) {
8. console.info(num.toString());
9. }
```

**ArkTS**

```
1. async function complexNumberProcessing(num: number): Promise<number> {
2. // ...
3. return num;
4. }

6. async function foo() {
7. for (let i = 1; i <= 5; i++) {
8. await complexNumberProcessing(i);
9. }
10. }

12. foo();
```

### 使用instanceof和as进行类型保护

**规则：**arkts-no-is

**级别：错误**

**错误码：10605096**

在ArkTS中，不支持is关键字，必须使用instanceof运算符来替代。在使用instanceof之前，必须先使用as运算符将对象转换为所需类型。

**TypeScript**

```
1. class Foo {
2. foo: string = ''
3. common: string = ''
4. }

6. class Bar {
7. bar: string = ''
8. common: string = ''
9. }

11. function isFoo(arg: any): arg is Foo {
12. return arg.foo !== undefined;
13. }

15. function doStuff(arg: Foo | Bar) {
16. if (isFoo(arg)) {
17. console.info(arg.foo);  // OK
18. console.info(arg.bar);  // 编译时错误
19. } else {
20. console.info(arg.foo);  // 编译时错误
21. console.info(arg.bar);  // OK
22. }
23. }

25. doStuff({ foo: '123', common: '123' });
26. doStuff({ bar: '123', common: '123' });
```

**ArkTS**

```
1. class Foo {
2. foo: string = ''
3. common: string = ''
4. }

6. class Bar {
7. bar: string = ''
8. common: string = ''
9. }

11. function isFoo(arg: Object): boolean {
12. return arg instanceof Foo;
13. }

15. function doStuff(arg: Object): void {
16. if (isFoo(arg)) {
17. let fooArg = arg as Foo;
18. console.info(fooArg.foo);   // OK
19. console.info(arg.bar);    // 编译时错误
20. } else {
21. let barArg = arg as Bar;
22. console.info(arg.foo);    // 编译时错误
23. console.info(barArg.bar);   // OK
24. }
25. }

27. function main(): void {
28. doStuff(new Foo());
29. doStuff(new Bar());
30. }
```

### 部分支持展开运算符

**规则：**arkts-no-spread

**级别：错误**

**错误码：10605099**

ArkTS仅支持使用展开运算符展开数组、Array的子类和TypedArray（例如Int32Array）。仅支持使用在以下场景中：

1. 传递给剩余参数时；
2. 复制一个数组到数组字面量。

**TypeScript**

```
1. function foo(x: number, y: number, z: number) {
2. // ...
3. }

5. let args: [number, number, number] = [0, 1, 2];
6. foo(...args);
```

**ArkTS**

```
1. function logNumbers(x: number, y: number, z: number) {
2. // ...
3. }

5. let numbers: number[] = [1, 2, 3];
6. logNumbers(numbers[0], numbers[1], numbers[2]);
```

**TypeScript**

```
1. let point2d = { x: 1, y: 2 };
2. let point3d = { ...point2d, z: 3 };
```

**ArkTS**

```
1. class Point2D {
2. public x: number = 0;
3. public y: number = 0;
4. }

6. class Point3D {
7. public x: number = 0;
8. public y: number = 0;
9. public z: number = 0
10. constructor(p2d: Point2D, z: number) {
11. this.x = p2d.x;
12. this.y = p2d.y;
13. this.z = z;
14. }
15. }

17. let p3d = new Point3D({ x: 1, y: 2 } as Point2D, 3);

19. class DerivedFromArray extends Uint16Array {};

21. let arr1 = [1, 2, 3];
22. let arr2 = new Uint16Array([4, 5, 6]);
23. let arr3 = new DerivedFromArray([7, 8, 9]);
24. let arr4 = [...arr1, 10, ...arr2, 11, ...arr3];
```

### 接口不能继承具有相同方法的两个接口

**规则：**arkts-no-extend-same-prop

**级别：错误**

**错误码：106050102**

在TypeScript中，如果一个接口继承了两个具有相同方法的接口，则必须使用联合类型声明该方法的返回值类型。在ArkTS中，由于接口不能包含两个无法区分的方法（如参数列表相同但返回类型不同），因此不能继承具有相同方法的两个接口。

**TypeScript**

```
1. interface Mover {
2. getStatus(): { speed: number }
3. }
4. interface Shaker {
5. getStatus(): { frequency: number }
6. }

8. interface MoverShaker extends Mover, Shaker {
9. getStatus(): {
10. speed: number
11. frequency: number
12. }
13. }

15. class C implements MoverShaker {
16. private speed: number = 0
17. private frequency: number = 0

19. getStatus() {
20. return { speed: this.speed, frequency: this.frequency };
21. }
22. }
```

**ArkTS**

```
1. class MoveStatus {
2. public speed: number;
3. constructor() {
4. this.speed = 0;
5. }
6. }
7. interface Mover {
8. getMoveStatus(): MoveStatus
9. }

11. class ShakeStatus {
12. public frequency: number;
13. constructor() {
14. this.frequency = 0;
15. }
16. }
17. interface Shaker {
18. getShakeStatus(): ShakeStatus
19. }

21. class MoveAndShakeStatus {
22. public speed: number;
23. public frequency: number;
24. constructor() {
25. this.speed = 0;
26. this.frequency = 0;
27. }
28. }

30. class C implements Mover, Shaker {
31. private moveStatus: MoveStatus;
32. private shakeStatus: ShakeStatus;

34. constructor() {
35. this.moveStatus = new MoveStatus();
36. this.shakeStatus = new ShakeStatus();
37. }

39. public getMoveStatus(): MoveStatus {
40. return this.moveStatus;
41. }

43. public getShakeStatus(): ShakeStatus {
44. return this.shakeStatus;
45. }

47. public getStatus(): MoveAndShakeStatus {
48. return {
49. speed: this.moveStatus.speed,
50. frequency: this.shakeStatus.frequency
51. };
52. }
53. }
```

### 不支持声明合并

**规则：**arkts-no-decl-merging

**级别：错误**

**错误码：10605103**

ArkTS不支持类和接口的声明合并。

**TypeScript**

```
1. interface Document {
2. createElement(tagName: any): number;
3. }

5. interface Document {
6. createElement(tagName: string): boolean;
7. }

9. interface Document {
10. createElement(tagName: number): number;
11. createElement(tagName: boolean): boolean;
12. createElement(tagName: string, value: number): string;
13. }
```

**ArkTS**

```
1. interface Document {
2. createElement(tagName: number): number;
3. createElement(tagName: boolean): boolean;
4. createElement(tagName: string, value: number): number;
5. createElement(tagName: string): string;
6. createElement(tagName: Object): object;
7. }
```

### 接口不能继承类

**规则：**arkts-extends-only-class

**级别：错误**

**错误码：10605104**

在ArkTS中，接口不能继承类，只能继承其他接口。

**TypeScript**

```
1. class Control {
2. state: number = 0;
3. }

5. interface SelectableControl extends Control {
6. select(): void
7. }
```

**ArkTS**

```
1. interface Control {
2. state: number
3. }

5. interface SelectableControl extends Control {
6. select(): void
7. }
```

### 不支持构造函数类型

**规则：**arkts-no-ctor-signatures-funcs

**级别：错误**

**错误码：10605106**

ArkTS不支持构造函数类型，改用lambda函数。

**TypeScript**

```
1. class Person {
2. constructor(
3. name: string,
4. age: number
5. ) { }
6. }
7. type PersonCtor = new (name: string, age: number) => Person;

9. function createPerson(Ctor: PersonCtor, name: string, age: number): Person {
10. return new Ctor(name, age);
11. }

13. const person = createPerson(Person, 'John', 30);
```

**ArkTS**

```
1. class Person {
2. constructor(
3. name: string,
4. age: number
5. ) {}
6. }
7. type PersonCtor = (n: string, a: number) => Person

9. function createPerson(ctor: PersonCtor, n: string, a: number): Person {
10. return ctor(n, a);
11. }

13. let impersonate: PersonCtor = (n: string, a: number): Person => {
14. return new Person(n, a);
15. }

17. const person = createPerson(impersonate, 'John', 30);
```

### 只能使用类型相同的编译时表达式初始化枚举成员

**规则：**arkts-no-enum-mixed-types

**级别：错误**

**错误码：10605111**

ArkTS不支持使用运行期间计算的表达式初始化枚举成员。枚举中所有显式初始化的成员必须具有相同类型。

**TypeScript**

```
1. enum E1 {
2. A = 0xa,
3. B = 0xb,
4. C = Math.random(),
5. D = 0xd,
6. E // 推断出0xe。
7. }

9. enum E2 {
10. A = 0xa,
11. B = '0xb',
12. C = 0xc,
13. D = '0xd'
14. }
```

**ArkTS**

```
1. enum E1 {
2. A = 0xa,
3. B = 0xb,
4. C = 0xc,
5. D = 0xd,
6. E // 推断出0xe。
7. }

9. enum E2 {
10. A = '0xa',
11. B = '0xb',
12. C = '0xc',
13. D = '0xd'
14. }
```

### 不支持enum声明合并

**规则：**arkts-no-enum-merging

**级别：错误**

**错误码：10605113**

ArkTS不支持enum声明合并。

**TypeScript**

```
1. enum ColorSet {
2. RED,
3. GREEN
4. }
5. enum ColorSet {
6. YELLOW = 2
7. }
8. enum ColorSet {
9. BLACK = 3,
10. BLUE
11. }
```

**ArkTS**

```
1. enum ColorSet {
2. RED,
3. GREEN,
4. YELLOW,
5. BLACK,
6. BLUE
7. }
```

### 命名空间不能被用作对象

**规则：**arkts-no-ns-as-obj

**级别：错误**

**错误码：10605114**

ArkTS不支持将命名空间用作对象，可以使用类或模块。

**TypeScript**

```
1. namespace MyNamespace {
2. export let x: number;
3. }

5. let m = MyNamespace;
6. m.x = 2;
```

**ArkTS**

```
1. namespace MyNamespace {
2. export let x: number;
3. }

5. MyNamespace.x = 2;
```

### 不支持命名空间中的非声明语句

**规则：**arkts-no-ns-statements

**级别：错误**

**错误码：10605116**

在ArkTS中，命名空间用于定义标识符的可见范围，仅在编译时有效。因此，命名空间中不支持非声明语句。可以将非声明语句写在函数中。

**TypeScript**

```
1. namespace A {
2. export let x: number;
3. x = 1;
4. }
```

**ArkTS**

```
1. namespace A {
2. export let x: number

4. export function init() {
5. x = 1;
6. }
7. }

9. // 调用初始化函数来执行。
10. A.init();
```

### 不支持require和import赋值表达式

**规则：**arkts-no-require

**级别：错误**

**错误码：10605121**

ArkTS不支持通过require导入和import赋值表达式，改用import。

**TypeScript**

```
1. import m = require('mod')
```

**ArkTS**

```
1. import * as m from 'mod'
```

### 不支持export = ...语法

**规则：**arkts-no-export-assignment

**级别：错误**

**错误码：10605126**

ArkTS不支持export = ...语法，改用常规的export或import。

**TypeScript**

```
1. // module1
2. export = Point

4. class Point {
5. constructor(x: number, y: number) {}
6. static origin = new Point(0, 0)
7. }

9. // module2
10. import Pt = require('module1')

12. let p = Pt.Point.origin;
```

**ArkTS**

```
1. // module1
2. export class Point {
3. constructor(x: number, y: number) {}
4. static origin = new Point(0, 0)
5. }

7. // module2
8. import * as Pt from 'module1'

10. let p = Pt.Point.origin
```

### 不支持ambient module声明

**规则：**arkts-no-ambient-decls

**级别：错误**

**错误码：10605128**

由于ArkTS本身有与JavaScript交互的机制，ArkTS不支持ambient module声明。

**TypeScript**

```
1. declare module 'someModule' {
2. export function normalize(s: string): string;
3. }
```

**ArkTS**

```
1. // 从原始模块中导入需要的内容
2. import { normalize } from 'someModule'
```

### 不支持在模块名中使用通配符

**规则：**arkts-no-module-wildcards

**级别：错误**

**错误码：10605129**

在ArkTS中，导入是编译时而非运行时行为，不支持在模块名中使用通配符。

**TypeScript**

```
1. // 声明
2. declare module '*!text' {
3. const content: string
4. export default content
5. }

7. // 使用代码
8. import fileContent from 'some.txt!text'
```

**ArkTS**

```
1. // 声明
2. declare namespace N {
3. function foo(x: number): number
4. }

6. // 使用代码
7. import * as m from 'module'
8. console.info('N.foo called: ' + N.foo(42));
```

### 不支持通用模块定义(UMD)

**规则：**arkts-no-umd

**级别：错误**

**错误码：10605130**

ArkTS不支持通用模块定义（UMD）。因为在ArkTS中没有“脚本”的概念（相对于“模块”）。此外，在ArkTS中，导入是编译时而非运行时特性。改用export和import语法。

**TypeScript**

```
1. // math-lib.d.ts
2. export const isPrime(x: number): boolean
3. export as namespace mathLib

5. // 脚本中
6. mathLib.isPrime(2)
```

**ArkTS**

```
1. // math-lib.d.ts
2. namespace mathLib {
3. export isPrime(x: number): boolean
4. }

6. // 程序中
7. import { mathLib } from 'math-lib'
8. mathLib.isPrime(2)
```

### 不支持new.target

**规则：**arkts-no-new-target

**级别：错误**

**错误码：10605132**

ArkTS没有原型的概念，因此不支持new.target。此特性不符合静态类型的原则。

### 不支持确定赋值断言

**规则：**arkts-no-definite-assignment

**级别：警告**

**错误码：10605134**

ArkTS不支持确定赋值断言，例如：let v!: T。改为在声明变量的同时为变量赋值。

**TypeScript**

```
1. let x!: number // 提示：在使用前将x初始化

3. initialize();

5. function initialize() {
6. x = 10;
7. }

9. console.info('x = ' + x);
```

**ArkTS**

```
1. function initialize(): number {
2. return 10;
3. }

5. let x: number = initialize();

7. console.info('x = ' + x);
```

### 不支持在原型上赋值

**规则：**arkts-no-prototype-assignment

**级别：错误**

**错误码：10605136**

ArkTS没有原型的概念，因此不支持在原型上赋值。此特性不符合静态类型的原则。

**TypeScript**

```
1. let C = function (p) {
2. this.p = p; // 只有在开启noImplicitThis选项时会产生编译时错误。
3. }

5. C.prototype = {
6. m() {
7. console.info(this.p);
8. }
9. }

11. C.prototype.q = function (r: string) {
12. return this.p == r;
13. }
```

**ArkTS**

```
1. class C {
2. public p: string = '';
3. m() {
4. console.info(this.p);
5. }
6. q(r: string) {
7. return this.p === r;
8. }
9. }
```

### 不支持globalThis

**规则：**arkts-no-globalthis

**级别：警告**

**错误码：10605137**

由于ArkTS不支持动态更改对象的布局，因此不支持全局作用域和globalThis。

**TypeScript**

```
1. // 全局文件中。
2. var abc = 100;

4. // 从上面引用'abc'。
5. let x = globalThis.abc;
```

**ArkTS**

```
1. // file1
2. export let abc: number = 100;

4. // file2
5. import * as M from 'file1'

7. let x = M.abc;
```

### 不支持一些utility类型

**规则：**arkts-no-utility-types

**级别：错误**

**错误码：10605138**

ArkTS仅支持Partial、Required、Readonly和Record，不支持TypeScript中其他的Utility Types。

对于Partial<T>类型，泛型参数T必须为类或者接口类型。

对于Record类型的对象，通过索引访问到的值的类型是包含undefined的联合类型。

### 不支持对函数声明属性

**规则：**arkts-no-func-props

**级别：错误**

**错误码：10605139**

由于ArkTS不支持动态改变函数对象布局，因此，不支持对函数声明属性。

### 不支持Function.apply和Function.call

**规则：**arkts-no-func-apply-call

**级别：错误**

**错误码：10605152**

ArkTS不允许使用标准库函数Function.apply和Function.call，因为这些函数用于显式设置被调用函数的this参数。在ArkTS中，this的语义仅限于传统的OOP风格，函数体中禁止使用this。

### 不支持Function.bind

**规则：**arkts-no-func-bind

**级别：警告**

**错误码：10605140**

ArkTS禁用标准库函数Function.bind。标准库使用这些函数显式设置被调用函数的this参数。在ArkTS中，this仅限于传统OOP风格，函数体中禁用使用this。

### 不支持as const断言

**规则：**arkts-no-as-const

**级别：错误**

**错误码：10605142**

ArkTS不支持as const断言和字面量类型。在标准TypeScript中，as const用于标注字面量类型。

**TypeScript**

```
1. // 'hello'类型
2. let x = 'hello' as const;

4. // 'readonly [10, 20]'类型
5. let y = [10, 20] as const;

7. // '{ readonly text: 'hello' }'类型
8. let z = { text: 'hello' } as const;
```

**ArkTS**

```
1. // 'string'类型。
2. let x: string = 'hello';

4. // 'number[]'类型。
5. let y: number[] = [10, 20];

7. class Label {
8. public text: string = '';
9. }

11. // 'Label'类型。
12. let z: Label = {
13. public text: 'hello',
14. }
```

### 不支持导入断言

**规则：**arkts-no-import-assertions

**级别：错误**

**错误码：10605143**

ArkTS不支持导入断言。因为导入是编译时特性，运行时检查导入API是否正确没有意义。改用常规的import语法。

**TypeScript**

```
1. import { obj } from 'something.json' assert { type: 'json' }
```

**ArkTS**

```
1. // 编译时将检查导入T的正确性
2. import { something } from 'module'
```

### 限制使用标准库

**规则：**arkts-limited-stdlib

**级别：错误**

**错误码：10605144**

ArkTS不允许使用TypeScript或JavaScript标准库中的某些接口。大部分接口与动态特性有关。ArkTS中禁止使用以下接口：

全局对象的属性和方法：eval

Object：\_\_proto\_\_、\_\_defineGetter\_\_、\_\_defineSetter\_\_、

\_\_lookupGetter\_\_、\_\_lookupSetter\_\_、assign、create、

defineProperties、defineProperty、freeze、

fromEntries、getOwnPropertyDescriptor、getOwnPropertyDescriptors、

getOwnPropertySymbols、getPrototypeOf、

hasOwnProperty、is、isExtensible、isFrozen、

isPrototypeOf、isSealed、preventExtensions、

propertyIsEnumerable、seal、setPrototypeOf

Reflect：apply、construct、defineProperty、deleteProperty、

getOwnPropertyDescriptor、getPrototypeOf、

isExtensible、preventExtensions、

setPrototypeOf

Proxy：handler.apply()、handler.construct()、

handler.defineProperty()、handler.deleteProperty()、handler.get()、

handler.getOwnPropertyDescriptor()、handler.getPrototypeOf()、

handler.has()、handler.isExtensible()、handler.ownKeys()、

handler.preventExtensions()、handler.set()、handler.setPrototypeOf()

### 强制进行严格类型检查

**级别：错误**

**错误码：10605999**

在编译阶段，会进行TypeScript严格模式的类型检查，包括：

noImplicitReturns,

strictFunctionTypes,

strictNullChecks,

strictPropertyInitialization。

**TypeScript**

```
1. // 只有在开启noImplicitReturns选项时会产生编译时错误。
2. function foo(s: string): string {
3. if (s != '') {
4. console.info(s);
5. return s;
6. } else {
7. console.info(s);
8. }
9. }

11. let n: number = null; // 只有在开启strictNullChecks选项时会产生编译时错误。
```

**ArkTS**

```
1. function foo(s: string): string {
2. console.info(s);
3. return s;
4. }

6. let n1: number | null = null;
7. let n2: number = 0;
```

在定义类时，如果无法在声明时或者构造函数中初始化某实例属性，那么可以使用确定赋值断言符!来消除strictPropertyInitialization的报错。

使用确定赋值断言符会增加代码错误的风险。开发者必须确保实例属性在使用前已赋值，以避免运行时异常。

使用确定赋值断言符会增加运行时开销，应尽量避免使用。

使用确定赋值断言符将产生warning: arkts-no-definite-assignment。

**TypeScript**

```
1. class C {
2. name: string  // 只有在开启strictPropertyInitialization选项时会产生编译时错误。
3. age: number   // 只有在开启strictPropertyInitialization选项时会产生编译时错误。
4. }

6. let c = new C();
```

**ArkTS**

```
1. class C {
2. name: string = ''
3. age!: number      // warning: arkts-no-definite-assignment

5. initAge(age: number) {
6. this.age = age;
7. }
8. }

10. let c = new C();
11. c.initAge(10);
```

### 不允许通过注释关闭类型检查

**规则：**arkts-strict-typing-required

**级别：错误**

**错误码：10605146**

在ArkTS中，类型检查不是可选项。不允许通过注释关闭类型检查，不支持使用@ts-ignore和@ts-nocheck。

**TypeScript**

```
1. // @ts-nocheck
2. // ...
3. // 关闭了类型检查后的代码
4. // ...

6. let s1: string = null; // 没有报错。

8. // @ts-ignore
9. let s2: string = null; // 没有报错。
```

**ArkTS**

```
1. let s1: string | null = null; // 没有报错，合适的类型
2. let s2: string = null; // 编译时报错
```

### 允许.ets文件import.ets/.ts/.js文件源码, 不允许.ts/.js文件import.ets文件源码

**规则：**arkts-no-ts-deps

**级别：错误**

**错误码：10605147**

.ets文件可以import.ets/.ts/.js文件源码，但是.ts/.js文件不允许import.ets文件源码。

**TypeScript**

```
1. // app.ets
2. export class C {
3. // ...
4. }

6. // lib.ts
7. import { C } from 'app'
```

**ArkTS**

```
1. // lib1.ets
2. export class C {
3. // ...
4. }

6. // lib2.ets
7. import { C } from 'lib1'
```

### class不能被用作对象

**规则：**arkts-no-classes-as-obj

**级别：警告**

**错误码：10605149**

在ArkTS中，class声明的是一个新类型，不是值。因此，不支持将class用作对象，例如将其赋值给一个对象。

### 不支持在import语句前使用其他语句

**规则：**arkts-no-misplaced-imports

**级别：错误**

**错误码：10605150**

在ArkTS中，除动态 import 语句外，所有 import 语句都应置于其他语句之前。

**TypeScript**

```
1. class C {
2. s: string = ''
3. n: number = 0
4. }

6. import foo from 'module1'
```

**ArkTS**

```
1. import foo from 'module1'

3. class C {
4. s: string = ''
5. n: number = 0
6. }

8. import('module2').then(() => {}).catch(() => {})  // 动态import
```

### 限制使用ESObject类型

**规则：**arkts-limited-esobj

**级别：警告**

**错误码：10605151**

为了防止动态对象（来自.ts/.js文件）在静态代码（.ets文件）中的滥用，ESObject类型在ArkTS中的使用是受限的。

在API版本18以前，唯一允许使用ESObject类型的场景是局部变量的声明。ESObject类型变量只能被跨语言调用的对象赋值，例如：ESObject、any、unknown、匿名类型等。禁止使用在.ets文件中定义的静态类型值初始化ESObject类型变量。ESObject类型变量只能用于跨语言调用的函数或赋值给另一个ESObject类型变量。

从API版本18开始，ESObject类型不再支持赋值对象字面量类型。ESObject类型支持在动态导入场景中作为类型标注，以及用于属性访问（点操作符和[]访问）、调用表达式和new表达式。

**ArkTS**

```
1. // lib.d.ts
2. declare function foo(): any;
3. declare function bar(a: any): number;

5. // main.ets
6. let e0: ESObject = foo(); // API18以前，编译时错误：ESObject类型只能用于局部变量；API18以后，OK，显式标注ESObject类型

8. function f() {
9. let e1 = foo();        // 编译时错误：e1的类型是any
10. let e2: ESObject = 1;  // API18以前，编译时错误：不能用非动态值初始化ESObject类型变量；API18以后，OK，支持赋值数字类型
11. let e3: ESObject = {}; // API18以前，编译时错误：不能用非动态值初始化ESObject类型变量；API18以后，编译时错误：ESObject不支持赋值对象字面量类型
12. let e4: ESObject = []; // API18以前，编译时错误：不能用非动态值初始化ESObject类型变量；API18以后，OK，支持赋值数组类型
13. let e5: ESObject = ''; // API18以前，编译时错误：不能用非动态值初始化ESObject类型变量；API18以后，OK，支持赋值字符串类型
14. e5['prop'];            // API18以前，编译时错误：不能访问ESObject类型变量的属性；API18以后，OK，支持[]访问
15. e5[1];                 // API18以前，编译时错误：不能访问ESObject类型变量的属性；API18以后，OK，支持[]访问
16. e5.prop;               // API18以前，编译时错误：不能访问ESObject类型变量的属性；API18以后，OK，支持点操作符访问

18. let e6: ESObject = foo(); // OK，显式标注ESObject类型
19. let e7: ESObject = e6;    // OK，使用ESObject类型赋值
20. bar(e7);                  // OK，ESObject类型变量传给跨语言调用的函数
21. }
```
