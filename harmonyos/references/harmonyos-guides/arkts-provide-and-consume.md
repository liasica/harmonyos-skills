---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume
title: @Provide装饰器和@Consume装饰器：与后代组件双向同步
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理组件拥有的状态 > @Provide装饰器和@Consume装饰器：与后代组件双向同步
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:04+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:39e76faf9724e231c46cd154fc106608b9cbf5ded6f3b14d1071fe540079f68a
---

@Provide和@Consume，应用于与后代组件的双向数据同步、状态数据在多个层级之间传递的场景。不同于上文提到的父子组件之间通过命名参数机制传递，@Provide和@Consume摆脱参数传递机制的束缚，实现跨层级传递。

其中@Provide装饰的变量是在祖先组件中，可以理解为被“提供”给后代的状态变量。@Consume装饰的变量是在后代组件中，去“消费（绑定）”祖先组件提供的变量。

@Provide/@Consume是跨组件层级的双向同步。在阅读@Provide和@Consume文档前，建议开发者对UI范式基本语法和自定义组件有基本的了解。建议提前阅读：[基本语法概述](arkts-basic-syntax-overview.md)，[声明式UI描述](arkts-declarative-ui-description.md)，[创建自定义组件](arkts-create-custom-components.md)。最佳实践请参考[状态管理最佳实践](../best-practices/bpta-status-management.md)。常见问题请参考[状态管理常见问题](arkts-state-management-faq.md)。

说明

从API version 9开始，这两个装饰器支持在ArkTS卡片中使用。

从API version 11开始，这两个装饰器支持在元服务中使用。

API version 19及以前，@Provide和@Consume双向同步仅支持声明式节点场景。

从API version 20开始，@Consume装饰的变量支持设置默认值。当查找不到@Provide的匹配结果时，@Consume装饰的变量会使用默认值进行初始化；当查找到@Provide的匹配结果时，@Consume装饰的变量会优先使用@Provide匹配结果的值，默认值不生效。

从API version 20开始，通过配置[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)的[BuildOptions](../harmonyos-references/js-apis-arkui-buildernode.md#buildoptions12)参数enableProvideConsumeCrossing为true，使得@Provide和@Consume支持跨[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)双向同步。但需要注意，BuilderNode会在上树前构造节点，所以BuilderNode内部定义的@Consume需要设置默认值，并在BuilderNode上树后，重新获取最近的@Provide数据，与之建立双向同步关系。具体可见[@Consume在跨BuilderNode场景下和@Provide建立双向同步](arkts-provide-and-consume.md#consume在跨buildernode场景下和provide建立双向同步)。

## 概述

@Provide/@Consume装饰的状态变量有以下特性：

* @Provide装饰的状态变量自动对其所有后代组件可用，开发者不需要多次在组件之间传递变量。
* 后代通过使用@Consume获取@Provide提供的变量，建立在@Provide和@Consume之间的双向数据同步，与[@State](arkts-state.md)/[@Link](arkts-link.md)不同的是，前者可以更便捷的在多层级父子组件之间传递。
* @Provide和@Consume通过变量名或者变量别名绑定，需要类型相同，否则会发生类型隐式转换，从而导致应用行为异常。

```
1. // 通过相同的变量名绑定
2. @Provide age: number = 0;
3. @Consume age: number;

5. // 通过相同的变量别名绑定
6. @Provide('a') id: number = 0;
7. @Consume('a') age: number;

9. // 通过Provide的变量别名和Consume的变量名相同绑定
10. @Provide('a') id: number = 0;
11. @Consume a: number;

13. // 通过Provide的变量名和Consume的变量别名绑定
14. @Provide id: number = 0;
15. @Consume('id') a: number;
```

当@Provide指定变量别名时，会同时保存变量名与变量别名，@Consume在查找时，会优先以变量别名作为查找值去匹配，如果没有别名则用变量名作为查找值，只要@Consume提供的查找值与@Provide保存的变量名或别名中任意一项一致，即可成功建立绑定关系。

## 装饰器说明

| @Provide变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 别名：常量字符串，可选。  如果指定了别名，则通过别名来绑定变量；如果未指定别名，则通过变量名绑定变量。  allowOverride：允许重写，string类型，可选。  如果使用allowOverride指定别名，则别名可以被重写，即可以存在同名的@Provide变量。  未使用allowOverride时则不允许重名。示例见[@Provide支持allowOverride参数](arkts-provide-and-consume.md#provide支持allowoverride参数)。 |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum类型，以及这些类型的数组。  API version 10开始支持[Date类型](arkts-provide-and-consume.md#装饰date类型变量)。  API version 11及以上支持[Map](arkts-provide-and-consume.md#装饰map类型变量)、[Set](arkts-provide-and-consume.md#装饰set类型变量)类型、undefined和null类型、ArkUI框架定义的联合类型[Length](../harmonyos-references/ts-types.md#length)、[ResourceStr](../harmonyos-references/ts-types.md#resourcestr)、[ResourceColor](../harmonyos-references/ts-types.md#resourcecolor)类型以及这些类型的联合类型，示例见[@Provide和Consume支持联合类型实例](arkts-provide-and-consume.md#provide和consume支持联合类型实例)。 |
| 不允许装饰的变量类型 | 不支持装饰Function类型。 |
| 初始化规则 | 必须定义本地默认值。  可以从父组件传入非undefined类型变量，此时使用该传入变量进行初始化。  父组件未传入或传入undefined类型变量时，使用本地默认值进行初始化。 |
| 同步规则 | **在子组件使用时：**  不与父组件中的任何类型变量同步。  父组件传入的外部变量对@Provide初始化时，仅作为初始值，后续变量的变化不会同步至@Provide。  **在父组件使用时：**  可以初始化子组件的常规变量、@State、@Link、[@Prop](arkts-prop.md)、@Provide。  @Provide变量的变化会同步给子组件的@Link、@Prop变量。  与后代子组件中别名匹配的@Consume变量双同步。 |

**图1** @Provide初始化规则图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/FMSWsnBMT1Chgxq9wrz4mA/zh-cn_image_0000002583477603.png?HW-CC-KV=V1&HW-CC-Date=20260427T233902Z&HW-CC-Expire=86400&HW-CC-Sign=08F642F6F7D384CF3EB6AF1CC23CE918C1DA17DA05ABA89EB169CB05486026F5)

| @Consume变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 别名：常量字符串，可选。  如果指定了别名，则通过别名来绑定变量；如果未指定别名，则通过变量名绑定变量。 |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum类型，以及这些类型的数组。  API version 10开始支持[Date类型](arkts-provide-and-consume.md#装饰date类型变量)。  API version 11及以上支持[Map](arkts-provide-and-consume.md#装饰map类型变量)、[Set](arkts-provide-and-consume.md#装饰set类型变量)类型、undefined和null类型、ArkUI框架定义的联合类型[Length](../harmonyos-references/ts-types.md#length)、[ResourceStr](../harmonyos-references/ts-types.md#resourcestr)、[ResourceColor](../harmonyos-references/ts-types.md#resourcecolor)类型以及这些类型的联合类型，示例见[@Provide和Consume支持联合类型实例](arkts-provide-and-consume.md#provide和consume支持联合类型实例)。  **说明：**  API version 20之前，@Consume装饰的变量，在其父组件或者祖先组件上，必须有对应的属性和别名的@Provide装饰的变量。 |
| 不允许装饰的变量类型 | 不支持装饰Function类型。 |
| 初始化规则 | API version 20之前，@Consume装饰的变量不支持本地设置默认值，必须要有与其匹配的@Provide装饰的变量。  从API version 20开始，@Consume支持设置默认值。若存在匹配成功的@Provide，则会使用@Provide的变量值作为初始值。若未匹配到@Provide变量，则使用本地默认值。示例见[@Consume装饰的变量支持设置默认值](arkts-provide-and-consume.md#consume装饰的变量支持设置默认值)。 |
| 同步规则 | **在子组件使用时：**  与祖先组件匹配的@Provide变量双向同步。  **在父组件使用时：**  可以初始化子组件的常规变量、@State、@Link、@Prop、@Provide。  @Consume变量的变化会同步给子组件的@Link、@Prop变量。 |

**图2** @Consume初始化规则图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/SCbOUo5hRSuIk5kGcy_93A/zh-cn_image_0000002552797954.png?HW-CC-KV=V1&HW-CC-Date=20260427T233902Z&HW-CC-Expire=86400&HW-CC-Sign=1101FFFFFE4FF270E7E06CBE515B13DB5D75C9C362A0B3A59EDB3A59A7BAA1E6)

## 观察变化和行为表现

### 观察变化

* 当装饰的数据类型为boolean、string、number类型时，可以观察到数值的变化。
* 当装饰的数据类型为class或者Object的时候，可以观察到赋值和属性赋值的变化（属性为Object.keys(observedObject)返回的所有属性）。
* 当装饰Array时，可以观察到数组本身、数组项的赋值及其API操作带来的变化。详见[装饰Array类型变量](arkts-provide-and-consume.md#装饰array类型变量)。
* 当装饰的对象是Date时，可以观察到Date整体的赋值，同时可通过调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds 更新Date的属性，详见[装饰Date类型变量](arkts-provide-and-consume.md#装饰date类型变量)。
* 当装饰的变量是Map时，可以观察到Map整体的赋值，同时可通过调用Map的接口set, clear, delete 更新Map的值。详见[装饰Map类型变量](arkts-provide-and-consume.md#装饰map类型变量)。
* 当装饰的变量是Set时，可以观察到Set整体的赋值，同时可通过调用Set的接口add, clear, delete 更新Set的值。详见[装饰Set类型变量](arkts-provide-and-consume.md#装饰set类型变量)。

### 框架行为

1. 初始渲染：

   1. @Provide装饰的变量会以Map的形式，传递给当前@Provide所属组件的所有子组件。
   2. 子组件中如果使用@Consume变量，则会在Map中查找是否有该变量名/alias（别名）对应的@Provide的变量。在API version 20之前，如果查找不到，框架会抛出JS ERROR。从API version 20开始，如果查找不到，会判断@Consume装饰的变量是否设置了默认值，如果没有设置默认值，框架会抛出JS ERROR。
   3. 在初始化@Consume变量时，如果在Map中有该变量名/alias（别名）对应的@Provide的变量，则和@State/@Link的流程类似，@Consume变量会在Map中查找到对应的@Provide变量进行保存，并把自己注册给@Provide。
   4. 从API version 20开始，在初始化@Consume变量时，如果在Map中没有该变量名/alias（别名）对应的@Provide的变量，而@Consume的变量设置了默认值时，@Consume变量会利用默认值创建一个临时的数据源，保证通知链路的连续性。
2. 当@Provide装饰的数据变化时：

   1. 通过初始渲染的步骤可知，子组件@Consume已把自己注册给父组件。父组件@Provide变量变更后，会遍历更新所有依赖它的系统组件（elementid）和状态变量（@Consume）。
   2. 通知@Consume更新后，子组件所有依赖@Consume的系统组件（elementId）都会被通知更新。以此实现@Provide对@Consume状态数据同步。
3. 当@Consume装饰的数据变化时：

   通过初始渲染的步骤可知，子组件@Consume持有@Provide的实例。在@Consume更新后调用@Provide的更新方法，将更新的数值同步回@Provide，以此实现@Consume向@Provide的同步更新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/uXBiMDQeQq-11Z_n_75j1w/zh-cn_image_0000002583437649.png?HW-CC-KV=V1&HW-CC-Date=20260427T233902Z&HW-CC-Expire=86400&HW-CC-Sign=22222FC4E22BC5DEAB107C11C11C1E3E027823E2696A4A5AF24B254EE74DE262)

## 限制条件

1. @Provide/@Consume的参数key必须为string类型，否则编译时会报错。

   ```
   1. // 错误写法，编译报错
   2. let change: number = 10;
   3. @Provide(change) message: string = 'Hello';

   5. // 正确写法
   6. let change: string = 'change';
   7. @Provide(change) message: string = 'Hello';
   ```
2. @Consume装饰的变量不能在构造参数中传入初始化，否则编译时会报错。@Consume仅能通过key来匹配对应的@Provide变量或者从API version 20开始设置默认值进行初始化。

   【反例】

   ```
   1. @Component
   2. struct Child {
   3. @Consume msg: string;

   5. build() {
   6. Text(this.msg)
   7. }
   8. }

   10. @Entry
   11. @Component
   12. struct Parent {
   13. @Provide message: string = 'Hello';

   15. build() {
   16. Column() {
   17. // 错误写法，不允许外部传入初始化
   18. Child({msg: 'Hello'})
   19. }
   20. }
   21. }
   ```

   【正例】

   ```
   1. @Component
   2. struct Child {
   3. @Consume num: number;
   4. // 从API version 20开始，@Consume装饰的变量支持设置默认值
   5. @Consume num1: number = 17;

   7. build() {
   8. Column() {
   9. Text(`Value of num: ${this.num}`)
   10. Text(`Value of num1: ${this.num1}`)
   11. }
   12. }
   13. }

   15. @Entry
   16. @Component
   17. struct Parent {
   18. @Provide num: number = 10;

   20. build() {
   21. Column() {
   22. Text(`Value of num: ${this.num}`)
   23. Child()
   24. }
   25. }
   26. }
   ```

   [ProvideConsumeProperDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeProperDemo.ets#L15-L42)
3. @Provide的key重复定义时，框架会抛出运行时错误，从API version 23开始，将返回错误码[140114](../harmonyos-references/errorcode-statemanagement.md#section140114-声明重复key的provide)，提醒开发者重复定义key。如果开发者需要重复key，可以使用[allowOverride](arkts-provide-and-consume.md#provide支持allowoverride参数)。

   ```
   1. // 错误写法，a重复定义
   2. @Provide('a') count: number = 10;
   3. @Provide('a') num: number = 10;

   5. // 正确写法
   6. @Provide('a') count: number = 10;
   7. @Provide('b') num: number = 10;
   ```
4. 在API version 20之前，初始化@Consume变量时，如果开发者没有定义对应key的@Provide变量，框架会抛出运行时错误，提示开发者初始化@Consume变量失败，原因是无法找到其对应key的@Provide变量。从API version 20开始，初始化@Consume变量时，如果开发者没有定义对应key的@Provide变量，同时没有设置默认值，框架会抛出运行时错误，从API version 23开始，将返回错误码[140112](../harmonyos-references/errorcode-statemanagement.md#section140112-consume缺失对应的provide)，提示开发者初始化@Consume变量失败，原因是无法找到其对应key的@Provide变量同时也没有设置默认值。

   【反例】

   ```
   1. @Component
   2. struct Child {
   3. @Consume num: number;

   5. build() {
   6. Column() {
   7. Text(`num的值: ${this.num}`)
   8. }
   9. }
   10. }

   12. @Entry
   13. @Component
   14. struct Parent {
   15. // 错误写法，缺少@Provide
   16. num: number = 10;

   18. build() {
   19. Column() {
   20. Text(`num的值: ${this.num}`)
   21. Child()
   22. }
   23. }
   24. }
   ```

   【正例】

   ```
   1. @Component
   2. struct Child {
   3. @Consume num: number;
   4. // 正确写法 从API version 20开始，@Consume装饰的变量支持设置默认值
   5. @Consume numWithDefaultValue: number = 6;

   7. build() {
   8. Column() {
   9. Text(`Value of num: ${this.num}`)
   10. Text(`Value of numWithDefaultValue: ${this.numWithDefaultValue}`)
   11. }
   12. }
   13. }

   15. @Entry
   16. @Component
   17. struct Parent {
   18. // 正确写法
   19. @Provide num: number = 10;

   21. build() {
   22. Column() {
   23. Text(`Value of num: ${this.num}`)
   24. Child()
   25. }
   26. }
   27. }
   ```

   [ProvideConsumeProperDemoTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeProperDemoTwo.ets#L15-L43)
5. @Provide与@Consume不支持装饰Function类型的变量，API version 23之前，框架会抛出运行时错误。

   从API version 23开始，添加对@Provide与@Consume装饰Function类型变量的校验，编译期会报错。
6. 从API version 20开始，支持跨BuilderNode配对@Provide/@Consume。在BuilderNode上树时，@Consume通过key匹配找到最近的@Provide，两者类型需要一致，如果不一致，则会抛出运行时错误。

   需要注意类型不相等判断，包括类实例的判断，比如：

   ```
   1. class A {}
   2. class B {}
   3. // 两个message都为object类型，但其构造函数不同，属于不同类型
   4. @Provide message: A = new A();
   5. @Consume message: B = new B();
   ```

   在非BuilderNode场景中，仍建议配对的@Provide/@Consume类型一致。虽然在运行时不会有强校验，但在@Consume装饰的变量初始化时，会隐式转换成@Provide装饰变量的类型。

   ```
   1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

   3. @Builder
   4. function buildText() {
   5. Column() {
   6. Child()
   7. }
   8. }

   10. class TextNodeController extends NodeController {
   11. private builderNode: BuilderNode<[]> | null = null;

   13. constructor() {
   14. super();
   15. }

   17. makeNode(context: UIContext): FrameNode | null {
   18. this.builderNode = new BuilderNode(context);
   19. // 配置跨BuilderNode支持@Provide/@Consume
   20. this.builderNode.build(wrapBuilder(buildText), undefined,
   21. { enableProvideConsumeCrossing: true });
   22. // 将BuilderNode的根节点挂载到NodeContainer
   23. return this.builderNode.getFrameNode();
   24. }
   25. }

   27. @Entry
   28. @Component
   29. struct Index {
   30. @Provide message: string = 'hello';
   31. controller: TextNodeController = new TextNodeController();

   33. build() {
   34. Column() {
   35. NodeContainer(this.controller)
   36. .width('100%')
   37. .height(100)
   38. }
   39. .width('100%')
   40. .height('100%')
   41. }
   42. }

   45. @Component
   46. struct Child {
   47. // Child通过BuilderNode上树后，@Consume和Index中的@Provide建立连接时发现类型不一致，抛出运行时错误
   48. @Consume message: number = 0;

   50. build() {
   51. Column() {
   52. Text(`@Consume ${this.message}`)
   53. }
   54. }
   55. }
   ```

   [ProvideConsumeBuilderNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeBuilderNode.ets#L15-L71)
7. 父组件传入undefined时，@Provide装饰的变量仍使用本地默认值进行初始化。

   ```
   1. @Entry
   2. @Component
   3. struct Parent {
   4. @State count: number | undefined = undefined;

   6. build() {
   7. Column() {
   8. Text(`Parent count value: ${this.count}`)
   9. .fontSize(20)
   10. .margin(10)
   11. Child({ count: this.count })
   12. }
   13. }
   14. }

   16. @Component
   17. struct Child {
   18. @Provide count: number | undefined = 0;

   20. build() {
   21. Column() {
   22. Text(`Child count value: ${this.count}`)
   23. .fontSize(20)
   24. .margin(10)
   25. }
   26. }
   27. }
   ```

## 使用场景

### @Provide变量与@Consume变量建立双向绑定

以下示例是@Provide变量与后代组件中@Consume变量进行双向同步的场景。当分别点击ToDo和ToDoItem组件内的Button时，count的更改会双向同步在ToDo和ToDoItem中。

```
1. @Component
2. struct ToDoItem {
3. // @Consume装饰的变量通过相同的属性名绑定其祖先组件ToDo内的@Provide装饰的变量
4. @Consume count: number;

6. build() {
7. Column() {
8. Text(`count(${this.count})`)
9. Button(`count(${this.count}), count + 1`)
10. .onClick(() => this.count += 1)
11. }
12. .width('50%')
13. }
14. }

16. @Component
17. struct ToDoList {
18. build() {
19. Row({ space: 5 }) {
20. ToDoItem()
21. ToDoItem()
22. }
23. }
24. }

26. @Component
27. struct ToDoDemo {
28. build() {
29. ToDoList()
30. }
31. }

33. @Entry
34. @Component
35. struct ToDo {
36. // @Provide装饰的变量count由入口组件ToDo提供其后代组件
37. @Provide count: number = 0;

39. build() {
40. Column() {
41. Button(`count(${this.count}), count + 1`)
42. .onClick(() => this.count += 1)
43. ToDoDemo()
44. }
45. }
46. }
```

[ProvideConsumeBidirectionalSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeBidirectionalSync.ets#L15-L62)

### 装饰Array类型变量

以下示例中，message类型为number[]，点击Button改变message的值，视图会随之刷新。

```
1. @Entry
2. @Component
3. struct Index {
4. @Provide message: number[] = [0, 1, 2, 3];

6. build() {
7. Column() {
8. ForEach(this.message, (item: number) => {
9. Text(`Provide ${item}`)
10. .fontSize(20)
11. .margin(10)
12. })
13. // 新增数组元素，触发UI刷新
14. Button('Push element')
15. .onClick(() => {
16. this.message.push(4);
17. })
18. .width(300)
19. .margin(10)
20. // 删除数组元素，触发UI刷新
21. Button('Pop element')
22. .onClick(() => {
23. this.message.pop();
24. })
25. .width(300)
26. .margin(10)
27. Child()
28. }
29. }
30. }

32. @Component
33. struct Child {
34. @Consume message: number[] = [0, 1, 2, 3];

36. build() {
37. Row() {
38. Column() {
39. ForEach(this.message, (item: number) => {
40. Text(`Consume ${item}`)
41. .fontSize(20)
42. .margin(10)
43. })
44. // 对数组整体重新赋值，触发UI刷新
45. Button('Reset array')
46. .onClick(() => {
47. this.message = [9, 8, 7, 6];
48. })
49. .width(300)
50. .margin(10)
51. // 更新数组元素，触发UI刷新
52. Button('Modify element[0]')
53. .onClick(() => {
54. this.message[0] = 10;
55. })
56. .width(300)
57. .margin(10)
58. }
59. .width('100%')
60. }
61. }
62. }
```

### 装饰Map类型变量

说明

从API version 11开始，@Provide，@Consume支持Map类型。

以下示例中，message类型为Map<number, string>，点击Button改变message的值，视图会随之刷新。

```
1. @Component
2. struct Child {
3. @Consume message: Map<number, string>

5. build() {
6. Column() {
7. ForEach(Array.from(this.message.entries()), (item: [number, string]) => {
8. Text(`${item[0]}`)
9. .fontSize(30)
10. Text(`${item[1]}`)
11. .fontSize(30)
12. Divider()
13. })
14. Button('Consume init Map')
15. .onClick(() => {
16. this.message = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
17. })
18. Button('Consume set new one')
19. .onClick(() => {
20. this.message.set(4, 'd');
21. })
22. Button('Consume clear')
23. .onClick(() => {
24. this.message.clear();
25. })
26. Button('Consume replace the first item')
27. .onClick(() => {
28. this.message.set(0, 'aa');
29. })
30. Button('Consume delete the first item')
31. .onClick(() => {
32. this.message.delete(0);
33. })
34. }
35. }
36. }

39. @Entry
40. @Component
41. struct MapSample {
42. @Provide message: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']])

44. build() {
45. Row() {
46. Column() {
47. Button('Provide init Map')
48. .onClick(() => {
49. this.message = new Map([[0, 'a'], [1, 'b'], [3, 'c'], [4, 'd']]);
50. })
51. Child()
52. }
53. .width('100%')
54. }
55. .height('100%')
56. }
57. }
```

[ProvideConsumeMapSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeMapSync.ets#L15-L73)

### 装饰Set类型变量

说明

从API version 11开始，@Provide，@Consume支持Set类型。

以下示例中，message类型为Set<number>，点击Button改变message的值，视图会随之刷新。

```
1. @Component
2. struct Child {
3. @Consume message: Set<number>

5. build() {
6. Column() {
7. ForEach(Array.from(this.message.entries()), (item: [number, number]) => {
8. Text(`${item[0]}`)
9. .fontSize(30)
10. Divider()
11. })
12. Button('Consume init set')
13. .onClick(() => {
14. this.message = new Set([0, 1, 2, 3, 4]);
15. })
16. Button('Consume set new one')
17. .onClick(() => {
18. this.message.add(5);
19. })
20. Button('Consume clear')
21. .onClick(() => {
22. this.message.clear();
23. })
24. Button('Consume delete the first one')
25. .onClick(() => {
26. this.message.delete(0);
27. })
28. }
29. .width('100%')
30. }
31. }

34. @Entry
35. @Component
36. struct SetSample {
37. @Provide message: Set<number> = new Set([0, 1, 2, 3, 4])

39. build() {
40. Row() {
41. Column() {
42. Button('Provide init set')
43. .onClick(() => {
44. this.message = new Set([0, 1, 2, 3, 4, 5]);
45. })
46. Child()
47. }
48. .width('100%')
49. }
50. .height('100%')
51. }
52. }
```

[ProvideConsumeSetSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeSetSync.ets#L15-L68)

### 装饰Date类型变量

以下示例中，selectedDate类型为Date，点击Button改变selectedDate的值，视图会随之刷新。

```
1. @Component
2. struct Child {
3. @Consume selectedDate: Date;

5. build() {
6. Column() {
7. Button(`child increase the day by 1`)
8. .onClick(() => {
9. this.selectedDate.setDate(this.selectedDate.getDate() + 1);
10. })
11. Button('child update the new date')
12. .margin(10)
13. .onClick(() => {
14. this.selectedDate = new Date('2023-09-09');
15. })
16. DatePicker({
17. start: new Date('1970-1-1'),
18. end: new Date('2100-1-1'),
19. selected: this.selectedDate
20. })
21. }
22. }
23. }

25. @Entry
26. @Component
27. struct Parent {
28. @Provide selectedDate: Date = new Date('2021-08-08')

30. build() {
31. Column() {
32. Button('parent increase the day by 1')
33. .margin(10)
34. .onClick(() => {
35. this.selectedDate.setDate(this.selectedDate.getDate() + 1);
36. })
37. Button('parent update the new date')
38. .margin(10)
39. .onClick(() => {
40. this.selectedDate = new Date('2023-07-07');
41. })
42. DatePicker({
43. start: new Date('1970-1-1'),
44. end: new Date('2100-1-1'),
45. selected: this.selectedDate
46. })
47. Child()
48. }
49. }
50. }
```

[ProvideConsumeDateSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeDateSync.ets#L15-L66)

### Provide和Consume支持联合类型实例

@Provide和@Consume支持联合类型和undefined和null。以下示例中，count类型为string | undefined，当点击父组件Parent中的Button改变count的属性或者类型时，Child中也会对应刷新。

```
1. @Component
2. struct Child {
3. // @Consume装饰的变量通过相同的属性名绑定其祖先组件Ancestors内的@Provide装饰的变量
4. @Consume count: string | undefined;

6. build() {
7. Column() {
8. Text(`count(${this.count})`)
9. Button(`count(${this.count}), Child`)
10. .onClick(() => this.count = 'Ancestors')
11. }
12. .width('50%')
13. }
14. }

16. @Component
17. struct Parent {
18. build() {
19. Row({ space: 5 }) {
20. Child()
21. }
22. }
23. }

25. @Entry
26. @Component
27. struct Ancestors {
28. // @Provide装饰的联合类型count由入口组件Ancestors提供其后代组件
29. @Provide count: string | undefined = 'Child';

31. build() {
32. Column() {
33. Button(`count(${this.count}), Child`)
34. .onClick(() => this.count = undefined)
35. Parent()
36. }
37. }
38. }
```

[ProvideConsumeFederation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeFederation.ets#L15-L54)

### @Provide支持allowOverride参数

allowOverride：@Provide重写选项。

说明

从API version 11开始使用。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| allowOverride | string | 否 | 是否允许@Provide重写。允许在同一组件树下通过allowOverride重写同名的@Provide。如果开发者未写allowOverride，定义同名的@Provide，运行时会报错。 |

```
1. @Component
2. struct MyComponent {
3. @Provide({ allowOverride: 'reviewVotes' }) reviewVotes: number = 10;

5. build() {
6. }

8. }
```

[ProvideConsumeProvideAllowOverride.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeProvideAllowOverride.ets#L15-L26)

完整示例如下：

```
1. @Component
2. struct GrandSon {
3. // @Consume装饰的变量通过相同的属性名绑定其祖先内的@Provide装饰的变量
4. @Consume('reviewVotes') reviewVotes: number;

6. build() {
7. Column() {
8. Text(`reviewVotes(${this.reviewVotes})`) // Text显示10
9. Button(`reviewVotes(${this.reviewVotes}), give +1`)
10. .onClick(() => this.reviewVotes += 1)
11. }
12. .width('50%')
13. }
14. }

16. @Component
17. struct Child {
18. @Provide({ allowOverride: 'reviewVotes' }) reviewVotes: number = 10;

20. build() {
21. Row({ space: 5 }) {
22. GrandSon()
23. }
24. }
25. }

27. @Component
28. struct Parent {
29. @Provide({ allowOverride: 'reviewVotes' }) reviewVotes: number = 20;

31. build() {
32. Child()
33. }
34. }

36. @Entry
37. @Component
38. struct GrandParent {
39. @Provide('reviewVotes') reviewVotes: number = 40;

41. build() {
42. Column() {
43. Button(`reviewVotes(${this.reviewVotes}), give +1`)
44. .onClick(() => this.reviewVotes += 1)
45. Parent()
46. }
47. }
48. }
```

[ProvideConsumeProvideAllowOverride.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeProvideAllowOverride.ets#L28-L77)

在上面的示例中：

* GrandParent声明了@Provide('reviewVotes') reviewVotes: number = 40。
* Parent是GrandParent的子组件，声明@Provide为allowOverride，重写父组件GrandParent的@Provide('reviewVotes') reviewVotes: number = 40。如果不设置allowOverride，则会抛出运行时报错，提示@Provide重复定义。Child同理。
* GrandSon在初始化@Consume的时候，@Consume装饰的变量通过相同的属性名绑定其最近的祖先的@Provide装饰的变量。
* GrandSon查找到相同属性名的@Provide在祖先Child中，所以@Consume('reviewVotes') reviewVotes: number初始化数值为10。如果Child中没有定义与@Consume同名的@Provide，则继续向上寻找Parent中的同名@Provide值为20，以此类推。
* 如果查找到根节点还没有找到key对应的@Provide，则会报初始化@Consume找不到@Provide的报错。

### @Consume装饰的变量支持设置默认值

说明

从API version 20开始，@Consume装饰的变量支持设置默认值。

```
1. @Component
2. struct MyComponent {
3. @Consume('withDefault') defaultValue: number = 10;

5. build() {
6. }

8. }
```

[ProvideConsumeDecoratedVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeDecoratedVariable.ets#L15-L26)

完整示例如下：

```
1. @Entry
2. @Component
3. struct Parent {
4. @Provide('firstKey') provideOne: string | undefined = undefined;
5. @Provide('secondKey') provideTwo: string = 'the second provider';

7. build() {
8. Column() {
9. Row() {
10. Column() {
11. Text(`${this.provideOne}`)
12. Text(`${this.provideTwo}`)
13. }

15. Column() {
16. // 点击change provideOne按钮，provideOne和子组件中的textOne属性会同时变化
17. Button('change provideOne')
18. .onClick(() => {
19. this.provideOne = undefined;
20. })
21. // 点击change provideTwo按钮，provideTwo和子组件中的textTwo属性会同时变化
22. Button('change provideTwo')
23. .onClick(() => {
24. this.provideTwo = 'the next provider';
25. })
26. }
27. }

29. Row() {
30. Column() {
31. Child()
32. }
33. }
34. }
35. }
36. }

38. @Component
39. struct Child {
40. // @Consume装饰的变量通过相同的别名绑定其祖先内的@Provide装饰的变量，同时设置默认值
41. @Consume('firstKey') textOne: string | undefined = 'child';
42. // @Consume装饰的变量通过相同的别名绑定其祖先内的@Provide装饰的变量，没有设置默认值
43. @Consume('secondKey') textTwo: string;
44. // @Consume装饰的变量在祖先内没有匹配成功的@Provide装饰的变量，但设置了默认值
45. @Consume('thirdKey') textThree: string = 'defaultValue';

47. build() {
48. Column() {
49. Text(`${this.textOne}`)
50. Text(`${this.textTwo}`)
51. Text(`${this.textThree}`)
52. // 点击change textOne按钮，textOne和父组件的provideOne会同时变化
53. Button('change textOne')
54. .onClick(() => {
55. this.textOne = 'not undefined';
56. })
57. // 点击change textTwo按钮，textTwo和父组件的provideTwo会同时变化
58. Button('change textTwo')
59. .onClick(() => {
60. this.textTwo = 'change textTwo';
61. })
62. }
63. }
64. }
```

[ProvideConsumeDecoratedVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeDecoratedVariable.ets#L28-L93)

在上面的示例中：

* Parent声明了@Provide('firstKey') provideOne: string | undefined = undefined 与 @Provide('secondKey') provideTwo: string = 'the second provider'。
* Child声明了@Consume('firstKey') textOne: string | undefined = 'child'，@Consume('secondKey') textTwo: string 与 @Consume('thirdKey') textThree: string = 'defaultValue'。
* Child是Parent的子组件，Child在初始化@Consume装饰的三个属性时，textOne根据'firstKey'别名绑定Parent中的provideOne属性，provideOne的值会覆盖textOne的默认值，所以textOne初始化的值为undefined；textTwo根据'secondKey'别名绑定Parent中的providedTwo属性，textTwo初始化的值为'the second provider'；textThree在祖先组件中不存在匹配结果，如果@Consume没有设置默认值，则会抛出运行时错误，示例中textThree有默认值'defaultValue'，所以textThree初始化的值为'defaultValue'。
* @Consume装饰的属性设置的默认值仅在祖先组件没有匹配结果时才生效，有匹配结果时无影响。

### @Consume在跨BuilderNode场景下和@Provide建立双向同步

说明

从API version 20开始，支持跨BuilderNode配对@Provide/@Consume。

BuilderNode支持@Provide/@Consume，需注意：

1. 在BuilderNode子树中定义的@Consume需要设置默认值，或者在子树中已存在配对的@Provide，否则会发生运行时报错。
2. BuilderNode上树后，设置默认值的@Consume会向上查找@Provide，根据key的匹配规则找到最近的@Provide后，会和@Provide建立双向同步关系。如果找不到配对的@Provide，则@Consume仍使用默认值。
3. 建立双向同步的关系后，如果@Provide装饰变量的值和@Consume的默认值不同，则会回调@Consume的[@Watch](arkts-watch.md)方法，以及与@Consume有同步关系的变量的@Watch方法，例如@Consume通知与其双向同步的@Link触发@Watch方法。
4. BuilderNode下树后，@Consume会再次试图查找对应的@Provide，如果发现下树后无法再找到之前配对的@Provide，则断开和@Provide的双向同步关系，@Consume装饰的变量恢复成默认值。
5. @Consume断开和@Provide的连接，恢复成默认值时，会判断@Consume装饰变量的值从和@Provide变为@Consume的默认值是否有变化，如果有变化，则会回调@Consume以及与其有同步关系变量的@Watch方法。

在下面的例子中：

1. 点击add Child:
   * 构建BuilderNode下的子节点Child，Child中@Consume未找到@Provide，使用本地默认值default value初始化。
   * BuilderNode上树时，Child中@Consume向上找到最近的Index中的@Provide，将@Consume从默认值更新为@Provide的值，并回调@Consume的@Watch方法。
2. @Provide和@Consume配对后，建立双向同步关系。点击Text(`@Provide: ${this.message}`)和Text(`@Consume ${this.message}`)，@Provide和@Consume绑定的Text组件刷新，并回调@Provide和@Consume的@Watch方法。
3. 点击remove Child, BuilderNode子节点下树，Child中的@Consume和Index中的@Provide断开连接，Child中的@Consume恢复成默认值，并回调@Consume的@Watch方法。
4. 点击dispose Child，释放BuilderNode下子节点，BuilderNode子节点Child销毁，执行[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. @Builder
7. function buildText() {
8. Column() {
9. Child()
10. }
11. }

13. class TextNodeController extends NodeController {
14. private rootNode: FrameNode | null = null;
15. private uiContext: UIContext | null = null;
16. private builderNode: BuilderNode<[]> | null = null;

18. constructor() {
19. super();
20. }

22. makeNode(context: UIContext): FrameNode | null {
23. this.rootNode = new FrameNode(context);
24. this.uiContext = context;
25. // 将rootNode节点挂载在NodeContainer下
26. return this.rootNode;
27. }

29. addBuilderNode(): void {
30. if (this.builderNode === null && this.uiContext && this.rootNode) {
31. this.builderNode = new BuilderNode(this.uiContext);
32. // 配置跨BuilderNode支持@Provide/@Consume
33. this.builderNode.build(wrapBuilder(buildText), undefined,
34. { enableProvideConsumeCrossing: true });
35. // 将BuilderNode的根节点挂载到rootNode节点下
36. try {
37. this.rootNode.appendChild(this.builderNode.getFrameNode());
38. } catch (e) {
39. hilog.error(DOMAIN, 'testTag', 'Failed to appendChild', JSON.stringify(e) ?? '');
40. }
41. }
42. }

44. removeBuilderNode(): void {
45. if (this.rootNode && this.builderNode) {
46. // 从rootNode节点下的BuildNode节点移除
47. try {
48. this.rootNode.removeChild(this.builderNode.getFrameNode());
49. } catch (e) {
50. hilog.error(DOMAIN, 'testTag', 'Failed to removeChild', JSON.stringify(e) ?? '');
51. }
52. }
53. }

55. disposeNode(): void {
56. if (this.rootNode && this.builderNode) {
57. // 立即释放当前BuilderNode
58. this.builderNode.dispose();
59. }
60. }
61. }

63. @Entry
64. @Component
65. struct Index {
66. @Provide @Watch('onChange') message: string = 'hello';
67. controller: TextNodeController = new TextNodeController();

69. onChange() {
70. hilog.info(DOMAIN, 'testTag', '%{public}s', `Index Provide change ${this.message}`);
71. }

73. build() {
74. Column() {
75. Text(`@Provide: ${this.message}`)
76. .fontSize(20)
77. .onClick(() => {
78. this.message += ' Provide';
79. })

81. // 执行BuilderNode的build方法，构造Child自定义组件
82. // 并将BuilderNode挂载在NodeContainer下
83. // Child中@Consume可以和当前Index中的@Provide配对
84. // @Consume装饰的变量message从default value变为hello，并回调@Consume的@Watch方法
85. Button('add Child')
86. .onClick(() => {
87. this.controller.addBuilderNode();
88. })
89. // 将BuilderNode下的节点从NodeContainer上移除
90. // @Consume修饰的变量message从和@Provide配对的值变为default value，并回调@Consume的@Watch方法
91. Button('remove Child')
92. .onClick(() => {
93. this.controller.removeBuilderNode();
94. })

96. // 立即释放当前BuilderNode，BuilderNode下节点销毁，Child组件执行aboutToDisappear
97. Button('dispose Child')
98. .onClick(() => {
99. this.controller.disposeNode();
100. })
101. NodeContainer(this.controller)
102. .width('100%')
103. .height(100)
104. .backgroundColor(Color.Pink)
105. }
106. .width('100%')
107. .height('100%')
108. }
109. }

112. @Component
113. struct Child {
114. @Consume @Watch('onChange') message: string = 'default value';

116. onChange() {
117. hilog.info(DOMAIN, 'testTag', '%{public}s', `Child Consume change ${this.message}`);
118. }

120. aboutToDisappear(): void {
121. hilog.info(DOMAIN, 'testTag', '%{public}s', `Child aboutToDisappear`);
122. }

124. build() {
125. Column() {
126. Text(`@Consume ${this.message}`)
127. .fontSize(20)
128. .onClick(() => {
129. this.message += ' Consume';
130. })
131. }
132. }
133. }
```

## 常见问题

### @BuilderParam尾随闭包情况下@Provide未定义错误

在此[尾随闭包](arkts-builderparam.md#尾随闭包初始化组件)场景下，CustomWidget执行this.builder()创建子组件CustomWidgetChild时，this指向的是HomePage。因此找不到CustomWidget的@Provide变量，所以下面示例会报找不到@Provide错误，和@BuilderParam连用的时候要谨慎this的指向。

错误示例：

```
1. class Tmp {
2. a: string = '';
3. }

5. @Entry
6. @Component
7. struct HomePage {
8. // 错误点1：HomePage未声明@Provide
9. @Builder
10. builder2($$: Tmp) {
11. Text(`${$$.a}测试`)
12. }

14. build() {
15. Column() {
16. // 错误点2：使用尾随闭包的形式将创建CustomWidgetChild的函数传递给CustomWidget，此时尾随闭包中this指向HomePage
17. CustomWidget() {
18. CustomWidgetChild({ builder: this.builder2 })
19. }
20. }
21. }
22. }

24. @Component
25. struct CustomWidget {
26. // 错误点3：@Provide变量声明在CustomWidget中，仅有CustomWidget自身及其子组件能够消费
27. @Provide('a') a: string = 'abc';
28. @BuilderParam
29. builder: () => void;

31. build() {
32. Column() {
33. Button('你好').onClick(() => {
34. if (this.a == 'ddd') {
35. this.a = 'abc';
36. }
37. else {
38. this.a = 'ddd';
39. }

41. })
42. this.builder()
43. }
44. }
45. }

47. @Component
48. struct CustomWidgetChild {
49. // 错误点4：尝试消费CustomWidget的@Provide('a')，但实际上CustomWidgetChild的父组件为HomePage，无法找到对应的@Provide
50. @Consume('a') a: string;
51. @BuilderParam
52. builder: ($$: Tmp) => void;

54. build() {
55. Column() {
56. this.builder({ a: this.a })
57. }
58. }
59. }
```

正确示例：

```
1. class Tmp {
2. public name: string = '';
3. }

5. @Entry
6. @Component
7. struct HomePage {
8. // 修正点1：将@Provide声明在Entry组件（根作用域），确保子组件能正确消费
9. @Provide('name') name: string = 'abc';

11. @Builder
12. builder2($$: Tmp) {
13. Text(`${$$.name} test`)
14. }

16. build() {
17. Column() {
18. Button('Hello').onClick(() => {
19. if (this.name == 'ddd') {
20. this.name = 'abc';
21. } else {
22. this.name = 'ddd';
23. }
24. })
25. // 修正点2：CustomWidget不再声明@Provide，仅作为容器传递builder
26. CustomWidget() {
27. CustomWidgetChild({ builder: this.builder2 })
28. }
29. }
30. }
31. }

33. @Component
34. struct CustomWidget {
35. @BuilderParam
36. builder: () => void;

38. build() {
39. this.builder()
40. }
41. }

43. @Component
44. struct CustomWidgetChild {
45. // 修正点3：@Consume从根作用域（HomePage）获取@Provide('name')，作用域正确
46. @Consume('name') name: string;
47. @BuilderParam
48. builder: ($$: Tmp) => void;

50. build() {
51. Column() {
52. this.builder({ name: this.name })
53. }
54. }
55. }
```

[ProvideConsumeProvideError.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/provideAndConsume/ProvideConsumeProvideError.ets#L15-L71)
