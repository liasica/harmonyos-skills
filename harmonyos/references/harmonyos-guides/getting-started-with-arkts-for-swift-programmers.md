---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/getting-started-with-arkts-for-swift-programmers
title: 从Swift到ArkTS的迁移指导
breadcrumb: 指南 > 基础入门 > 学习ArkTS语言 > 面向其他语言的ArkTS迁移指导 > 从Swift到ArkTS的迁移指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ab12ac556515e4fe8a3a090435e9032fddf78a9f0c9047cc7a707104dd8e1d2c
---

对于熟悉Swift的开发者而言，ArkTS作为新的开发语言，带来了全新的开发体验与机遇。ArkTS在语法和编程范式上不仅继承了现代语言的特性，还针对生态进行了深度优化。理解Swift与ArkTS的差异和共性，能够帮助开发者快速上手应用开发，避开常见的编程误区。

本文档基于Swift语言对ArkTS语言进行对比和介绍。如需更详细的了解，可参考[ArkTS语言介绍](introduction-to-arkts.md)。

## 探索Swift与ArkTS的差异

本文档将帮助Swift开发者梳理在转向ArkTS开发过程中会遇到的误解和陷阱。ArkTS的语法、类型系统以及应用开发模式与Swift存在差异，在学习过程中需特别注意这些关键区别。建议先掌握ArkTS的基础语法和运行时行为，再重点对比其与Swift的不同之处。

## 基础语法

### 变量声明

**ArkTS示例：**

```
1. // 类型注解（类似Swift）。
2. let age: number = 20;
3. const program: string = 'ArkTS';

5. // 类型推断（类似Swift的局部变量类型推断）。
6. let version = 5.0;
```

### 基础数据类型

| Swift类型 | ArkTS类型 | 示例代码 | 核心差异说明 |
| --- | --- | --- | --- |
| Bool | boolean | let isDone: boolean = false; | 定义方式相似，均用于逻辑判断。 |
| Int8 | number | let count: number = 10; | Swift的Int8为8位整数。  ArkTS统一用number表示小整数类型。 |
| Int16 | number | let count: number = 10; | Swift的Int16为16位整数。  ArkTS统一用number表示小整数类型。 |
| Int32 | number | let count: number = 10; | Swift的Int32为32位整数。  ArkTS的number是双精度浮点型，可存储整数和浮点数。 |
| Int64 | number | let largeNum: number = 9007199254740991; | Swift需处理大整数。  ArkTS用同一类型表示。 |
| Float | number | let pi: number = 3.14; | Swift需显式指定Float。  ArkTS直接使用number。 |
| Double | number | let e: number = 2.71828; | Swift区分Float和Double。  ArkTS统一用number表示所有数值类型。 |
| Character | string | let c: string = 'a'; | ArkTS无Character类型，单字符场景使用string。 |
| String | string | let message: string = 'Hello'; | 定义方式类似，但ArkTS字符串支持模板字面量和更灵活的操作。 |

### 复杂数据类型

| Swift类型体系 | ArkTS类型体系 | ArkTS示例代码 | 核心差异说明 |
| --- | --- | --- | --- |
| **数组**：var arr: [Int] = [1, 2, 3] | **Array**：let arr: number[] = [1, 2, 3]; | // 动态长度语法糖  let dynamicArr = [4, 5, 6]; | Swift数组长度可变。  ArkTS的Array是动态数组，支持push/pop等操作；可直接用[]简化初始化。数组不会越界，当数组下标超过数组长度时会得到undefined。 |
| **集合 - Set**：var mySet: Set<String> = ["a", "b"] | **Set**：let mySet: Set<string> = new Set(["a", "b"]); | mySet.add('c'); // 向集合内添加元素  for (const item of mySet) {...); // 迭代访问 | Swift集合通过类型声明。  ArkTS中集合的类型较灵活，适合动态场景。 |
| **字典 - Dictionary**：var dict: [String: Int] = ["key": 1] | **Map**：let map: Map<string, number> = new Map(); | map.set('key', 1); // 添加键值对  let value = map.get('key'); // 获取值  map.has('key'); // 检查键是否存在 | Swift的Dictionary需显式声明类型。  ArkTS的Map操作更直接，支持链式调用。 |
| **协议**：protocol Shape { func area() -> Double } | **interface**：interface Shapes { area(): number; } | class Rectangles implements Shapes {  public width: number = 0;  public height: number = 0;  area(): number { return this.width \* this.height; }  } | 语法结构相似，但ArkTS接口实现无需显式修饰符，且支持可选属性。 |
| **类**：class Circle: Shape { /\* 类定义 \*/ } | **class**：class Circles implements Shape { /\* 类定义 \*/ } | class Circles {  radius: number;  constructor(radius: number = 10) { // 支持参数默认值  this.radius = radius;  }  } | ArkTS类支持属性默认值、可选参数，语法更简洁。 |
| **枚举**：enum Color { case red, green, blue } | **enum**：enum Colors { Red, Green, Blue } | enum Colors { Red = 1, Green, Blue };  let color = Colors.Green; // 值为2（自动递增） | 基本概念一致，但ArkTS枚举不支持Swift中的自定义构造函数和方法，仅支持简单的数值或字符串枚举。 |

### 函数与闭包

Swift和ArkTS在函数方面语法趋同，细节上有差别。

相似点：常规函数定义和箭头函数。

**ArkTS示例：** 函数定义

```
1. // 常规函数定义，与Swift类似。
2. function add(x: number, y: number): number {
3. return x + y;
4. }
5. // ...
6. // 简洁的箭头函数形式，类似Swift的闭包语法。
7. const multiply = (a: number, b: number): number => a * b;
```

差异点：

1. ArkTS提供类型声明层面的多态，仅用于类型检查和文档提示，实际只有一个实现函数。

   **ArkTS示例：** ArkTS函数重载

   ```
   1. function foo(x: number): void;            /*  第一个函数定义。  */
   2. function foo(x: string): void;            /*  第二个函数定义。  */
   3. function foo(x: number | string): void {  /*  函数实现。       */
   4. }
   5. // ...
   6. foo(123);     //  OK，使用第一个定义。
   7. foo('aa'); // OK，使用第二个定义。
   ```
2. ArkTS可选参数使用?，如function foo(name?: string)，而非Swift的默认值语法。

   ```
   1. function foo2(name?: string) {}  /*  name为可选参数。  */
   2. // ...
   3. foo2('hello');     //  OK，传入name参数。
   4. foo2();     //  OK，不传name参数。
   ```

### 基础类库

ArkTS基础类库和容器类库增强了语言的基础功能，包括高精度浮点运算、二进制Buffer、XML生成解析转换和多种容器库等能力，协助开发者简化开发工作，提升开发效率。

## 语言结构

Swift是一种融合面向对象、函数式和协议导向范式的现代语言，强调安全性、性能与简洁性，适用于跨平台开发。

ArkTS融合声明式UI、函数式和面向对象范式，通过响应式系统和跨设备适配能力，高效构建多端一致的高性能应用。

### 模块与包管理

在Swift中，开发者使用模块（module）来组织代码，通过import语句引入其他模块中的类。

ArkTS也有自己的模块和包管理机制，同样通过import语句引入其他模块中的功能。

**ArkTS示例：**

```
1. // 引入ArkTS标准库中的ArkTS容器集。

3. import { collections } from '@kit.ArkTS';
```

由于ArkTS的模块系统更注重模块化开发和代码复用，能够更便捷地管理不同功能模块之间的依赖关系，所以在使用方式上，与Swift的模块管理会有所区别。

### 类与命名空间特性

ArkTS的类系统在语法层面与Swift相似，但在高阶特性上展现出更现代的设计理念。

| 特性 | Swift实现方式 | ArkTS实现方式 | 说明 |
| --- | --- | --- | --- |
| 命名空间组织 | 嵌套结构/内部类 | namespace关键字或模块文件结构。 | 支持显式命名空间与模块化组织的混合模式。 |
| 类继承机制 | 基于类的继承体系 | 基于原型链的继承机制。 | 语法相似但底层机制不同。 |
| 类成员可见性 | public/private/internal | 同Swift，但支持模块级可见性控制。 | 增加了模块导出控制的维度。 |

**命名空间管理**

ArkTS支持显式命名空间（namespace）和模块化组织。

**ArkTS示例：**

```
1. namespace Models {
2. export class User {
3. // 实现细节。
4. // ...
5. }

7. export interface Repository {
8. // 接口定义。
9. }
10. }
```

相比Swift的模块+内部类组合，ArkTS的命名空间能更直观地实现代码分层。

### 异步编程模型

**单线程vs多线程**

Swift使用async/await + Task实现异步编程，使用多线程和DispatchQueue实现并发。

ArkTS基于事件循环，使用Promise/async/await处理异步，避免阻塞主线程。

**错误处理**

Swift的同步代码通过try/catch捕获异常，异步异常需特殊处理。

ArkTS中未捕获的Promise错误可能导致静默失败，需显式使用try/catch或.catch。

### this的绑定

Swift的方法中，self始终指向类的实例对象，由代码结构在编译时确定。在方法中，self指向调用该方法的对象实例，无法通过调用方式改变self的指向。

**Swift示例：**

```
1. class MyClass {
2. func method() {
3. print(self) // 始终指向MyClass的实例。
4. }
5. }
```

ArkTS的this指向取决于函数调用时的上下文。

**ArkTS示例：**

```
1. class A {
2. bar: string = 'I am A';

4. foo() {
5. console.info(this.bar);
6. }
7. }

9. class B {
10. bar: string = 'I am B';

12. callFunction(fn: () => void) {
13. fn();
14. }
15. }

17. function callFunction(fn: () => void) {
18. fn();
19. }
20. // ...
21. let a: A = new A();
22. let b: B = new B();

24. // callFunction(a.foo); // 程序crash。this的上下文发生了变化。
25. // b.callFunction(a.foo); // 程序crash。this的上下文发生了变化。
26. b.callFunction(a.foo.bind(b)) // 输出'I'm B'。
```

## 类型系统

ArkTS与Swift的类型系统也存在差异。

### 类型推断与可选类型

相较于Swift需要显式类型声明和严格的nil检查，ArkTS的类型系统提供了更灵活的表达方式。

ArkTS具有强大的类型推断能力，编译器能够根据上下文自动推断出变量的类型，所以很多时候不需要显式声明变量的类型。

**ArkTS示例：**

```
1. let num = 10; // 编译器自动推断num为number类型。
```

```
1. interface Person {
2. name: string;
3. age?: number;  // age是可选属性。
4. }

6. const person: Person = {
7. name: 'Alice',
8. };
```

**ArkTS示例：**

### 联合类型

联合类型这种类型组合能力为复杂场景提供了更强的表达力，是ArkTS类型系统的重要创新点。

ArkTS支持联合类型（|）。联合类型表示一个值可以是多种类型中的一种。

**ArkTS示例：**

```
1. // 联合类型示例。

3. let value: string | number;
4. value = 'hello';
5. value = 123;
```
