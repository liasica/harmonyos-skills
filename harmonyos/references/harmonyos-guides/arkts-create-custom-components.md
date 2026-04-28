---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components
title: 创建自定义组件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 创建自定义组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:54+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:45ca9bc463f87c53d68bdfd095dc3f4733ac0013ba4eb5846da4f00dbb7a142d
---

在ArkUI中，UI显示的内容均为组件，由框架直接提供的称为系统组件，由开发者定义的称为自定义组件。进行UI界面开发时，不仅要组合使用系统组件，还需考虑代码的可复用性、业务逻辑与UI的分离，以及后续版本的演进等因素。因此，将UI和部分业务逻辑封装成自定义组件是不可或缺的能力。

自定义组件具有以下特点：

* 可组合：允许开发者组合使用系统组件及其属性和方法。
* 可重用：自定义组件可以被其他组件重用，并作为不同的实例在不同的父组件或容器中使用。
* 数据驱动UI更新：通过状态变量的改变，来驱动UI的刷新。

## 自定义组件的基本用法

以下示例展示了自定义组件的基本用法。

```
1. @Component
2. struct HelloComponent {
3. @State message: string = 'Hello, World!';

5. build() {
6. // HelloComponent自定义组件组合系统组件Row和Text
7. Row() {
8. Text(this.message)
9. .onClick(() => {
10. // 状态变量message的改变驱动UI刷新，UI从'Hello, World!'刷新为'Hello, ArkUI!'
11. this.message = 'Hello, ArkUI!';
12. })
13. }
14. }
15. }
```

[ParentComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/ParentComponent.ets#L15-L32)

注意

如果在其他文件中引用自定义组件，需要使用export关键字导出组件，并在使用的页面import该自定义组件。

可以在其他自定义组件的build()函数中多次创建HelloComponent，以实现自定义组件的重用。

```
1. @Entry
2. @Component
3. struct ParentComponent {
4. build() {
5. Column() {
6. Text('ArkUI message')
7. HelloComponent({ message: 'Hello World!' })
8. Divider()
9. HelloComponent({ message: 'Hello ArkTS!' })
10. }
11. }
12. }
```

[ParentComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/ParentComponent.ets#L33-L47)

要完全理解上面的示例，需要了解自定义组件的以下概念定义，本文将在后面的小节中介绍：

* [自定义组件的基本结构](arkts-create-custom-components.md#自定义组件的基本结构)
* [成员函数/变量](arkts-create-custom-components.md#成员函数变量)
* [自定义组件的参数规定](arkts-create-custom-components.md#自定义组件的参数规定)
* [build()函数实现规则](arkts-create-custom-components.md#build函数实现规则)
* [自定义组件通用样式](arkts-create-custom-components.md#自定义组件通用样式)

## 自定义组件的基本结构

### struct

自定义组件基于struct实现，struct + 自定义组件名 + {...}的组合构成自定义组件，不能有继承关系。对于struct的实例化，可以省略new。

说明

自定义组件名、类名、函数名不得与系统组件名重复。

### @Entry

@Entry装饰的自定义组件将作为[UI页面](arkts-router-to-navigation.md#页面结构)的入口。在单个UI页面中，仅允许存在一个由@Entry装饰的自定义组件作为页面的入口。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 10开始，@Entry可以接受一个可选的[LocalStorage](../harmonyos-references/ts-state-management.md#localstorage9)参数或者一个可选的EntryOptions10+参数。

从API version 11开始，该装饰器支持在元服务中使用。

```
1. @Entry
2. @Component
3. struct MyComponent {
4. // ...
5. }
```

[Entry.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/Entry.ets#L15-L33)

**EntryOptions10+**

命名路由跳转选项。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| routeName | string | 否 | 是 | 表示作为命名路由页面的名字。 |
| storage | [LocalStorage](arkts-localstorage.md) | 否 | 是 | 页面级的UI状态存储。当未传入时，框架会创建一个新的LocalStorage实例作为默认值。 |
| useSharedStorage12+ | boolean | 否 | 是 | 是否使用[loadContent](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)传入的LocalStorage实例对象。默认值false。true：使用共享的[LocalStorage](arkts-localstorage.md)实例对象。false：不使用共享的[LocalStorage](arkts-localstorage.md)实例对象。 |

说明

当useSharedStorage设置为true且storage已赋值时，useSharedStorage的值优先级更高。

```
1. @Entry({ routeName: 'myPage' })
2. @Component
3. struct MyComponent {
4. // ...
5. }
```

[RouteName.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/RouteName.ets#L15-L33)

### @Component

@Component装饰的struct为V1自定义组件，可以使用[状态管理V1版本](arkts-state-management-overview.md#状态管理v1)装饰器的能力。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，@Component可以接受一个[ComponentOptions参数](../harmonyos-references/ts-custom-component-parameter.md#componentoptions)。

从API version 11开始，该装饰器支持在元服务中使用。

```
1. @Component
2. struct MyComponent {
3. // ...
4. }
```

[Component.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/Component.ets#L16-L33)

### @ComponentV2

@ComponentV2装饰的struct为V2自定义组件，可以使用[状态管理V2版本](arkts-state-management-overview.md#状态管理v2)装饰器的能力。

说明

@ComponentV2装饰器从API version 12开始支持。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

和[@Component装饰器](arkts-create-custom-components.md#component)一样，@ComponentV2装饰器用于装饰自定义组件：

* 在@ComponentV2装饰的自定义组件中，开发者仅可以使用全新的状态变量装饰器，包括[@Local](arkts-new-local.md)、[@Param](arkts-new-param.md)、[@Once](arkts-new-once.md)、[@Event](arkts-new-event.md)、[@Provider](arkts-new-provider-and-consumer.md)、[@Consumer](arkts-new-provider-and-consumer.md)等。
* @ComponentV2装饰的自定义组件暂不支持[LocalStorage](arkts-localstorage.md)等现有自定义组件的能力。
* 无法同时使用@ComponentV2与@Component装饰同一个struct结构。
* @ComponentV2支持一个可选的[ComponentOptions参数](../harmonyos-references/ts-custom-component-parameter.md#componentoptions)，来实现[组件冻结功能](arkts-custom-components-freezev2.md)。
* 一个简单的@ComponentV2装饰的自定义组件应具有以下部分：

  ```
  1. @Entry
  2. @ComponentV2 // 装饰器
  3. struct ComponentV2Test { // struct声明的数据结构
  4. @Local message: string = 'Hello World';
  5. build() { // build定义的UI
  6. RelativeContainer() {
  7. Text(this.message)
  8. .id('HelloWorld')
  9. // $r('app.float.page_text_font_size')需要替换为开发者所需的资源文件;
  10. .fontSize($r('app.float.page_text_font_size'))
  11. .fontWeight(FontWeight.Bold)
  12. .alignRules({
  13. center: { anchor: '__container__', align: VerticalAlign.Center },
  14. middle: { anchor: '__container__', align: HorizontalAlign.Center }
  15. })
  16. .onClick(() => {
  17. this.message = 'Welcome';
  18. })
  19. }
  20. .height('100%')
  21. .width('100%')
  22. }
  23. }
  ```

  [PageComponentV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/wrapbuilder/entry/src/main/ets/pages/PageComponentV2.ets#L20-L44)

除非特别说明，@ComponentV2装饰的自定义组件将与@Component装饰的自定义组件保持相同的行为。

### build()函数

build()函数用于定义自定义组件的声明式UI描述，自定义组件必须定义build()函数。

```
1. @Component
2. struct MyComponent {
3. build() {
4. // ...
5. }
6. }
```

[BuildFunction.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/BuildFunction.ets#L16-L33)

### @Reusable

@Reusable装饰V1自定义组件，使得该自定义组件具有被复用的能力。详细请参考：[@Reusable装饰器：组件复用](arkts-reusable.md#使用场景)。

说明

从API version 10开始，该装饰器支持在ArkTS卡片中使用。

```
1. @Reusable
2. @Component
3. struct MyComponent {
4. // ...
5. }
```

[Reusable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/Reusable.ets#L16-L34)

### @ReusableV2

@ReusableV2装饰V2自定义组件，使得该自定义组件具有被复用的能力。详细请参考：[@ReusableV2装饰器：V2组件复用](arkts-new-reusablev2.md#使用场景)。

说明

从API version 18开始，该装饰器支持在元服务中使用。

```
1. @ReusableV2
2. @ComponentV2
3. struct MyComponent {
4. // ...
5. }
```

## 成员函数/变量

自定义组件除了必须要实现build()函数外，还可以实现其他成员函数，成员函数具有以下约束：

* 自定义组件的成员函数仅能从组件内部访问，且不建议声明为静态函数。

自定义组件可以包含成员变量，成员变量具有以下约束：

* 自定义组件的成员变量仅能从组件内部访问，且不建议声明为静态变量。
* 自定义组件的成员变量本地初始化有些是可选的，有些是必选的。具体是否需要本地初始化，是否需要从父组件通过参数传递初始化子组件的成员变量，请参考[状态管理](arkts-state-management-overview.md)。

## 自定义组件的参数规定

以下示例展示了如何在build方法里创建自定义组件，并在创建自定义组件的过程中，根据装饰器的规则来初始化自定义组件的参数。

```
1. @Component
2. struct MyComponent {
3. countDownFrom: number = 0;
4. color: Color = Color.Blue;

6. build() {
7. Column() {
8. Text(`${this.countDownFrom}`)
9. .backgroundColor(this.color)
10. }
11. }
12. }

14. @Entry
15. @Component
16. struct ParentComponent {
17. private someColor: Color = Color.Pink;

19. build() {
20. Column() {
21. // 创建MyComponent实例，并将创建MyComponent成员变量countDownFrom初始化为10，将成员变量color初始化为this.someColor
22. MyComponent({ countDownFrom: 10, color: this.someColor })
23. }
24. }
25. }
```

[ParameterSpecification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/ParameterSpecification.ets#L15-L42)

以下示例代码将父组件中的函数传递给子组件，并在子组件中调用。

```
1. @Entry
2. @Component
3. struct Parent {
4. @State cnt: number = 0;
5. submit: () => void = () => {
6. this.cnt++;
7. };

9. build() {
10. Column() {
11. Text(`${this.cnt}`)
12. Son({ submitArrow: this.submit })
13. }
14. }
15. }

17. @Component
18. struct Son {
19. submitArrow?: () => void;

21. build() {
22. Row() {
23. Button('add')
24. .width(80)
25. .onClick(() => {
26. if (this.submitArrow) {
27. this.submitArrow()
28. }
29. })
30. }
31. .height(56)
32. }
33. }
```

[ParentFunction.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/ParentFunction.ets#L15-L50)

## build()函数实现规则

所有在build()函数中声明的语句统称为UI描述，UI描述需要遵循以下规则：

* @Entry装饰的自定义组件，其build()函数下的根节点唯一且必要，且必须为容器组件，其中ForEach禁止作为根节点。

  @Component装饰的自定义组件，其build()函数下的根节点唯一且必要，可以为非容器组件，其中ForEach禁止作为根节点。

  ```
  1. @Entry
  2. @Component
  3. struct MyComponent {
  4. build() {
  5. // 根节点唯一且必要，必须为容器组件
  6. Row() {
  7. ChildComponent()
  8. }
  9. }
  10. }

  12. @Component
  13. struct ChildComponent {
  14. build() {
  15. // 根节点唯一且必要，可为非容器组件
  16. // 请将$r('app.media.startIcon')替换为实际资源文件
  17. Image($r('app.media.startIcon'))
  18. }
  19. }
  ```

  [MyComponentBuild.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/MyComponentBuild.ets#L15-L36)
* 不允许声明本地变量，反例如下。

  ```
  1. build() {
  2. // 反例：不允许声明本地变量
  3. let num: number = 1;
  4. }
  ```
* 不允许在UI描述里直接使用console.info，但允许在方法或者函数里使用，反例如下。

  ```
  1. build() {
  2. // 反例：不允许console.info
  3. console.info('print debug log');
  4. }
  ```
* 不允许创建本地的作用域，反例如下。

  ```
  1. build() {
  2. // 反例：不允许本地作用域
  3. {
  4. // ...
  5. }
  6. }
  ```
* 不允许调用没有用@Builder装饰的方法，允许系统组件的参数是TS方法的返回值。

  ```
  1. @Component
  2. struct ParentComponent {
  3. doSomeCalculations() {
  4. }
  5. build() {
  6. Column() {
  7. // 反例：不能调用没有用@Builder装饰的方法
  8. this.doSomeCalculations();
  9. }
  10. }
  11. }
  ```

  ```
  1. @Component
  2. struct ParentComponent {
  3. calcTextValue(): string {
  4. return 'Hello World';
  5. }

  7. @Builder
  8. doSomeRender() {
  9. Text(`Hello World`)
  10. }

  12. build() {
  13. Column() {
  14. // 正例：可以调用
  15. this.doSomeRender()
  16. // 正例：参数可以为调用TS方法的返回值
  17. Text(this.calcTextValue())
  18. }
  19. }
  20. }
  ```

  [BuilderMethod.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/BuilderMethod.ets#L16-L38)
* 不允许使用switch语法，当需要使用条件判断时，请使用[if](arkts-rendering-control-ifelse.md)。示例如下。

  ```
  1. build() {
  2. Column() {
  3. // 反例：不允许使用switch语法
  4. switch (expression) {
  5. case 1:
  6. Text('...')
  7. break;
  8. case 2:
  9. Image('...')
  10. break;
  11. default:
  12. Text('...')
  13. break;
  14. }
  15. }
  16. }
  ```

  ```
  1. build() {
  2. Column() {
  3. // 正例：使用if
  4. if (this.expression == 1) {
  5. Text('...')
  6. } else if (this.expression == 2) {
  7. Image('...')
  8. } else {
  9. Text('...')
  10. }
  11. }
  12. }
  ```

  [If.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/If.ets#L20-L34)
* 不允许使用表达式，请使用if组件，示例如下。

  ```
  1. build() {
  2. Column() {
  3. // 反例：不允许使用表达式
  4. (this.aVar > 10) ? Text('...') : Image('...')
  5. }
  6. }
  ```

  ```
  1. build() {
  2. Column() {
  3. // 正例：使用if判断
  4. if (this.aVar > 10) {
  5. Text('...')
  6. } else {
  7. Image('...')
  8. }
  9. }
  10. }
  ```

  [ModuleComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/ModuleComponent.ets#L20-L32)
* 不允许直接改变状态变量，反例如下。

  ```
  1. @Component
  2. struct MyComponent {
  3. @State textColor: Color = Color.Yellow;
  4. @State columnColor: Color = Color.Green;
  5. @State count: number = 1;
  6. build() {
  7. Column() {
  8. // 应避免直接在Text组件内改变count的值
  9. Text(`${this.count++}`)
  10. .width(50)
  11. .height(50)
  12. .fontColor(this.textColor)
  13. .onClick(() => {
  14. this.columnColor = Color.Red;
  15. })
  16. Button("change textColor").onClick(() =>{
  17. this.textColor = Color.Pink;
  18. })
  19. }
  20. .backgroundColor(this.columnColor)
  21. }
  22. }
  ```

  在ArkUI状态管理中，状态驱动UI更新。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/pXmAcYuMR6ierxaSQ400MA/zh-cn_image_0000002583477553.png?HW-CC-KV=V1&HW-CC-Date=20260427T233853Z&HW-CC-Expire=86400&HW-CC-Sign=CB6EB222A9A703B8A6539C4491A41A3C50BE59ED1C185A560CFC63E46C246326)

  所以，不能在自定义组件的build()或@Builder方法里直接改变状态变量，这可能会造成循环渲染的风险。Text('${this.count++}')在全量更新或最小化更新会产生不同的影响：

  + 全量更新（API8及以前版本）： ArkUI可能会陷入一个无限的重渲染的循环里，因为Text组件的每一次渲染都会改变应用的状态，就会再引起下一轮渲染的开启。 当 this.columnColor 更改时，都会执行整个build构建函数，因此，Text(${this.count++})绑定的文本也会更改，每次重新渲染Text(${this.count++})，又会使this.count状态变量更新，导致新一轮的build执行，从而陷入无限循环。
  + 最小化更新（API9及以上版本）：当this.columnColor更新时，仅Column组件更新，Text组件不会更新。只有当this.textColor更改时，会去更新整个Text组件，其所有属性函数都会执行，所以会看到Text(${this.count++})自增。因为目前UI以组件为单位进行更新，如果组件上某一个属性发生改变，会更新整个的组件。所以整体的更新链路是：this.textColor = Color.Pink ->Text组件整个更新->this.count++ ->Text组件整个更新。值得注意的是，这种写法在初次渲染时会导致Text组件渲染两次，影响性能。

  build函数中更改应用状态的行为可能比上面的示例更加隐蔽，例如：

  + 在@Builder，[@Extend](arkts-extend.md)或[@Styles](arkts-style.md)方法内改变状态变量 。
  + 在计算参数时调用函数中改变应用状态变量，例如 Text('${this.calcLabel()}')。
  + 对当前数组做出修改，sort()改变了数组this.arr，随后的filter方法会返回一个新的数组。

    ```
    1. // 反例
    2. @State arr : Array<...> = [ ... ];
    3. ForEach(this.arr.sort().filter(...),
    4. item => {
    5. // ...
    6. })
    ```

    ```
    1. // 正确的执行方式为：filter返回一个新数组，后面的sort方法才不会改变原数组this.arr
    2. ForEach(this.arr.filter((item, index) => index >= 2).sort(),
    3. (item: number) => {
    4. // ...
    5. });
    ```

    [ForEachFilter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/ForEachFilter.ets#L21-L27)

  该问题可以参考[常见问题：build函数中更改状态变量导致appfreeze](arkts-state-management-faq-inner-component.md#build函数中更改状态变量导致appfreeze)。

## 自定义组件通用样式

自定义组件通过“.”链式调用设置通用样式。

```
1. @Component
2. struct ChildComponent {
3. build() {
4. Button(`Hello World`)
5. }
6. }

8. @Entry
9. @Component
10. struct MyComponent {
11. build() {
12. Row() {
13. ChildComponent()
14. .width(200)
15. .height(300)
16. .backgroundColor(Color.Red)
17. }
18. }
19. }
```

[MyComponentStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/MyComponentStyle.ets#L15-L36)

说明

ArkUI给自定义组件设置样式时，相当于给ChildComponent套了一个不可见的容器组件，这些样式是设置在容器组件上，而非直接设置给ChildComponent的Button组件。渲染结果显示，背景颜色红色并没有直接设置到Button上，而是设置在Button所在的不可见容器组件上。

## 限制条件

### V1自定义组件不支持静态代码块

静态代码块用于初始化静态属性。

* 在@Component或@CustomDialog装饰的自定义组件中编写静态代码块时，该代码不会被执行。从API version 22开始，添加对静态代码块的校验，编译期告警提示静态代码块不生效。

  ```
  1. @Component
  2. struct MyComponent {
  3. static a: string = '';
  4. // 静态代码块不生效，a的值仍为空字符串''
  5. static {
  6. this.a = 'hello world';
  7. }
  8. // ...
  9. }
  ```

  [StaticCodeV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/StaticCodeV1.ets#L16-L37)
* 在@ComponentV2装饰的自定义组件中支持使用。

  ```
  1. @ComponentV2
  2. struct MyComponent {
  3. static a: string = '';
  4. // 静态代码块生效，a的值变为'hello world'
  5. static {
  6. this.a = 'hello world';
  7. }
  8. // ...
  9. }
  ```

  [StaticCodeV2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/createCustomComponents/entry/src/main/ets/component/StaticCodeV2.ets#L16-L36)

### @Component与@ComponentV2混用

在将@Component装饰的自定义组件与@ComponentV2装饰的自定义组件混合使用时，可参考[状态管理V1和V2混用场景](v1v2-mixing.md)。
