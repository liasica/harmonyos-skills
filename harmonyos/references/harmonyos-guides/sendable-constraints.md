---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-constraints
title: Sendable使用规则与约束
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > Sendable使用规则与约束
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3bf02233a8ef4f05acd1f9bd672f5bb98e0c640e7c986c07bfcee7816d3b1065
---

## 继承规则

### Sendable类必须继承自Sendable类

Sendable对象的布局和原型链不可变，而非Sendable对象可以通过特殊方式修改布局。因此，不允许互相继承。这里的类不包含变量，Sendable类不能继承自变量。

**正例：**

```
1. @Sendable
2. class A {
3. constructor() {
4. }
5. }

7. @Sendable
8. class B extends A {
9. constructor() {
10. super()
11. }
12. }
```

**反例：**

```
1. class A {
2. constructor() {
3. }
4. }

6. @Sendable
7. class B extends A { // A不是sendable class，B不能继承它，编译报错
8. constructor() {
9. super()
10. }
11. }
```

### 非Sendable类必须继承自非Sendable类

Sendable对象的布局和原型链不可变，而非Sendable对象可以通过特殊方式修改布局，因此不允许互相继承。

**正例：**

```
1. class A {
2. constructor() {
3. }
4. }

6. class B extends A {
7. constructor() {
8. super()
9. }
10. }
```

**反例：**

```
1. @Sendable
2. class A {
3. constructor() {
4. }
5. }

7. class B extends A { // A是sendable class，B不能继承它，编译报错
8. constructor() {
9. super()
10. }
11. }
```

## 接口实现规则

### 非Sendable类禁止实现Sendable接口

非Sendable类实现Sendable接口时，可能被误认为是Sendable类，导致错误使用。

**正例：**

```
1. interface I {};

3. class B implements I {};
```

**反例：**

```
1. import { lang } from '@kit.ArkTS';

3. type ISendable = lang.ISendable;

5. interface I extends ISendable {};

7. class B implements I {};  // I是sendable interface，B不能实现，编译报错
```

## Sendable类/接口成员变量规则

### 必须是Sendable支持的数据类型

Sendable数据不得持有非Sendable数据，因此Sendable类或接口的成员变量必须是[Sendable支持的数据类型](arkts-sendable.md#sendable支持的数据类型)。

**正例：**

```
1. @Sendable
2. class A {
3. constructor() {
4. }
5. a: number = 0;
6. }
```

**反例：**

```
1. @Sendable
2. class A {
3. constructor() {
4. }
5. b: Array<number> = [1, 2, 3] // 编译报错，需使用collections.Array
6. }
```

### 不支持使用!断言

Sendable对象的成员属性必须赋初值，而“!”修饰的变量可以不赋初值，因此不支持使用“!”。

**正例：**

```
1. @Sendable
2. class A {
3. constructor() {
4. }
5. a: number = 0;
6. }
```

**反例：**

```
1. @Sendable
2. class A {
3. constructor() {
4. }
5. a!: number; // 编译报错，不支持使用“!”
6. }
```

### 不支持使用计算属性名

Sendable对象的布局不可更改，因为计算属性无法静态确定对象布局，所以不支持。

**正例：**

```
1. @Sendable
2. class A {
3. num1: number = 1;
4. num2: number = 2;
5. add(): number {
6. return this.num1 + this.num2;
7. }
8. }
```

**反例：**

```
1. enum B {
2. b1 = "bbb"
3. }
4. @Sendable
5. class A {
6. ["aaa"]: number = 1; // 编译报错，不支持["aaa"]
7. [B.b1]: number = 2; // 编译报错，不支持[B.b1]
8. }
```

### 不支持使用类型别名

Sendable类的成员变量不能使用类型别名（即使用type关键字定义的别名）。

**正例：**

```
1. @Sendable
2. class B {
3. num1: number = 1;
4. num2: number = 2;
5. add(): number {
6. return this.num1 + this.num2;
7. }
8. }
```

**反例：**

```
1. type A = number;

3. @Sendable
4. class B {
5. num1: A = 1; // 运行报错，不支持使用类型别名
6. num2: A = 2; // 运行报错，不支持使用类型别名
7. add(): number {
8. return this.num1 + this.num2;
9. }
10. }
```

## 泛型规则

### 泛型类中的Sendable类、SendableLruCache、collections.Array、collections.Map和collections.Set的模板类型必须是Sendable类型

Sendable数据不能持有非Sendable数据，因此泛型类中的Sendable数据的模版类型必须是Sendable类型。

**正例：**

```
1. import { collections } from '@kit.ArkTS';

3. try {
4. let arr1: collections.Array<number> = new collections.Array<number>();
5. let num: number = 1;
6. arr1.push(num);
7. } catch (e) {
8. console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
9. }
```

**反例：**

```
1. import { collections } from '@kit.ArkTS';

3. try {
4. let arr1: collections.Array<Array<number>> = new collections.Array<Array<number>>(); // 编译报错，模板类型必须是Sendable类型
5. let arr2: Array<number> = new Array<number>();
6. arr2.push(1);
7. arr1.push(arr2);
8. } catch (e) {
9. console.error(`taskpool execute: Code: ${e.code}, message: ${e.message}`);
10. }
```

## 上下文访问规则

### Sendable类的内部不允许使用当前模块内上下文环境中定义的变量

由于Sendable对象在不同并发实例间的上下文环境不同，属于单个虚拟机实例，如果直接访问会有非预期行为。不支持Sendable对象使用当前模块内上下文环境中定义的变量，违反此规则会在编译阶段报错。

说明

从API version 12开始，Sendable class的内部支持使用top level的Sendable class对象。

**正例：**

```
1. import { lang } from '@kit.ArkTS';

3. type ISendable = lang.ISendable;

5. interface I extends ISendable {}

7. @Sendable
8. class B implements I {
9. static o: number = 1;
10. static bar(): B {
11. return new B();
12. }
13. }

15. @Sendable
16. class C {
17. v: I = new B();
18. u: number = B.o;

20. foo() {
21. return B.bar();
22. }
23. }
```

**反例：**

```
1. import { lang } from '@kit.ArkTS';

3. type ISendable = lang.ISendable;

5. interface I extends ISendable {}

7. @Sendable
8. class B implements I {}

10. function bar(): B {
11. return new B();
12. }

14. let b = new B();

16. {
17. @Sendable
18. class A implements I {}

20. @Sendable
21. class C {
22. u: I = bar(); // bar不是sendable class对象，编译报错
23. v: I = new A(); // A不是定义在top level中，编译报错

25. foo() {
26. return b; // b不是sendable class对象，而是sendable class的实例，编译报错
27. }
28. }
29. }
```

## @Sendable装饰器使用规则

### @Sendable装饰器仅支持修饰类和函数

当前仅支持修饰类和函数。

**正例：**

```
1. @Sendable
2. type SendableFuncType = () => void;

4. @Sendable
5. class C {}

7. @Sendable
8. function SendableFunc() {
9. console.info("Sendable func");
10. }
```

**反例：**

```
1. @Sendable
2. type A = number; // 编译报错

4. @Sendable
5. type D = C; // 编译报错
```

### Sendable类和Sendable函数禁止使用除@Sendable外的装饰器

在ts文件中定义类装饰器时，可能会改变类的结构，进而引发运行时错误。

**正例：**

```
1. @Sendable
2. class A {
3. num: number = 1;
4. }
```

**反例：**

```
1. @Sendable
2. @Observed // 编译报错
3. class C {
4. num: number = 1;
5. }
```

### 支持在Sendable class上叠加自定义装饰器

从API version 22开始，支持在Sendable class上叠加使用除@Sendable装饰器之外的其他自定义装饰器。

通过在[工程级build-profile.json5文件](ide-hvigor-build-profile-app.md)的"buildOption"字段下的"strictMode"中增加"disableSendableCheckRules"字段，配置该能力。

"disableSendableCheckRules"字段及其具体取值示例如下：

```
1. "buildOption": {
2. "strictMode": {
3. "caseSensitiveCheck": true,
4. "useNormalizedOHMUrl": true,
5. "disableSendableCheckRules": ["arkts-sendable-class-decorator"]
6. }
7. }
```

说明

* "disableSendableCheckRules"字段值为包含Sendable规则的数组。

  + 默认不展示，即默认不支持在Sendable class上叠加使用除@Sendable之外的其他自定义装饰器。
  + 禁止配置为空数组。
  + 当数组中配置了"arkts-sendable-class-decorator"规则时，支持在Sendable class上叠加除@Sendable之外的其他自定义装饰器。
* @Sendable和其他自定义装饰器叠加使用可能造成运行时异常，需要开发者适配装饰器函数的实现。

## 初始化规则

### 禁止使用对象字面量/数组字面量初始化Sendable对象

对象字面量和数组字面量不是Sendable类型。Sendable类型必须通过Sendable类型的new表达式创建。

**正例：**

```
1. import { collections } from '@kit.ArkTS';

3. let arr1: collections.Array<number> = new collections.Array<number>(1, 2, 3); // 是Sendable类型
```

**反例：**

```
1. import { collections } from '@kit.ArkTS';

3. let arr2: collections.Array<number> = [1, 2, 3]; // 不是Sendable类型，编译报错
4. let arr3: number[] = [1, 2, 3]; // 不是Sendable类型，正例，不报错
5. let arr4: number[] = new collections.Array<number>(1, 2, 3); // 编译报错
```

## 类型转换规则

### 禁止非Sendable类型强制转换为Sendable

除了Object类型，非Sendable类型不能强转成Sendable类型。非Sendable类型通过as强转成Sendable类型后，实际数据仍为非Sendable类型，会导致错误使用。Sendable类型在不违反Sendable规则的前提下，需要和非Sendable类型行为兼容，因此Sendable类型可以通过as强转成非Sendable类型。

**正例：**

```
1. class A {
2. state: number = 0;
3. }

5. @Sendable
6. class SendableA {
7. state: number = 0;
8. }

10. let a1: A = new SendableA() as A;
```

**反例：**

```
1. class A {
2. state: number = 0;
3. }

5. @Sendable
6. class SendableA {
7. state: number = 0;
8. }

10. let a2: SendableA = new A() as SendableA; // 编译报错
```

## 函数规则

### 箭头函数不可标记为Sendable

箭头函数不支持@Sendable装饰器，因此它是非Sendable函数，因此不支持共享。

**正例：**

```
1. @Sendable
2. type SendableFuncType = () => void;

4. @Sendable
5. function SendableFunc() {
6. console.info("Sendable func");
7. }

9. @Sendable
10. class SendableClass {
11. constructor(f: SendableFuncType) {
12. this.func = f;
13. }
14. func: SendableFuncType;
15. }

17. let sendableClass = new SendableClass(SendableFunc);
```

**反例：**

```
1. @Sendable
2. type SendableFuncType = () => void;
3. let func: SendableFuncType = () => {}; // 编译报错

5. @Sendable
6. class SendableClass {
7. func: SendableFuncType = () => {}; // 编译报错
8. }
```

## 与TS/JS交互的规则

### ArkTS通用规则（目前只针对Sendable对象）

| 规则 |
| --- |
| Sendable对象传入TS/JS的接口中，禁止操作其对象布局（增、删属性，改变属性类型）。 |
| Sendable对象设置到TS/JS的对象上，TS中获取到Sendable对象后，禁止操作其对象布局（增、删属性，改变属性类型）。 |
| Sendable对象放入TS/JS的容器中，TS中获取到Sendable对象后，禁止操作其对象布局（增、删属性，改变属性类型）。 |

说明

改变属性类型不包括Sendable对象类型的改变，例如从Sendable class A变为Sendable class B。

### NAPI规则（目前只针对Sendable对象）

NAPI相关接口请参考[Sendable相关的NAPI接口](use-napi-about-extension.md#sendable相关)，具体使用请参考[Native与Sendable ArkTS对象绑定](use-sendable-napi.md)。

| 规则 |
| --- |
| 禁止删除属性。不能使用napi\_delete\_property接口。 |
| 禁止新增属性。不能使用napi\_set\_property、napi\_set\_named\_property、napi\_define\_properties接口。 |
| 禁止修改属性类型。不能使用napi\_set\_property、napi\_set\_named\_property、napi\_define\_properties接口。 |
| 不支持Symbol相关接口和类型。不能使用napi\_create\_symbol、napi\_is\_symbol\_object、napi\_symbol接口。 |

## 与UI交互的规则

Sendable数据需要与[makeObserved](arkts-new-makeobserved.md)配合使用，才可以观察Sendable对象的数据变化，具体使用请参考[makeObserved和@Sendable装饰的class配合文档](arkts-new-makeobserved.md#makeobserved和sendable装饰的class配合使用)。

## 在HAR包中的使用规则

Sendable可在[HAR](har-package.md)包中使用。当在字节码HAR中使用Sendable时，无需进行额外配置，可直接使用。当在TS HAR中使用Sendable时，需在HAR模块下的module.json5文件中将"metadata"字段下的"name"设置为“UseTsHar”，配置如下所示。

```
1. {
2. "module": {
3. "name": "library",
4. "type": "har",
5. "deviceTypes": [
6. "tablet",
7. "2in1"
8. ],
9. "metadata": [
10. {
11. "name": "UseTsHar",
12. "value": "true"
13. }
14. ]
15. }
16. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/src/main/module.json5#L15-L32)
