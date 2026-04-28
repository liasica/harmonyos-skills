---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder
title: wrapBuilder：封装全局@Builder
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > wrapBuilder：封装全局@Builder
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9d4f45d56011271f6ca0e42fb6a15245e041ecd6fb543e8855c96f816b75fe9
---

当在一个struct内使用多个全局@Builder函数实现UI的不同效果时，代码维护将变得非常困难，且页面不够整洁。此时，可以使用[wrapBuilder](../harmonyos-references/ts-universal-wrapbuilder.md)封装全局@Builder。

在阅读本文档前，建议阅读：[@Builder](arkts-builder.md)。

说明

从API version 11开始支持。

从API version 12开始，wrapBuilder支持在元服务中使用。

从API version 22开始，推荐开发者使用[mutableBuilder](arkts-mutablebuilder.md)，支持二次赋值后刷新UI。

当@Builder方法赋值给变量或者数组后，在UI方法中无法使用。

```
1. @Builder
2. function builderElement() {}

4. let builderArr: Function[] = [builderElement];
5. @Builder
6. function testBuilder() {
7. ForEach(builderArr, (item: Function) => {
8. item();
9. })
10. }
```

在上述代码中，builderArr是一个由@Builder方法组成的数组。在ForEach循环中取每个@Builder方法时，会出现@Builder方法在UI方法中无法使用的问题。

为了解决这一问题，引入wrapBuilder作为全局@Builder封装函数。wrapBuilder返回WrappedBuilder对象，用于[全局@Builder](arkts-builder.md#全局自定义构建函数)的赋值和传递。

## 接口说明

wrapBuilder是一个模板函数，返回一个WrappedBuilder对象。

```
1. declare function wrapBuilder<Args extends Object[]>(builder: (...args: Args) => void): WrappedBuilder<Args>;
```

同时 WrappedBuilder对象也是一个模板类。

```
1. declare class WrappedBuilder<Args extends Object[]> {
2. builder: (...args: Args) => void;

4. constructor(builder: (...args: Args) => void);
5. }
```

说明

模板参数Args extends Object[]需要匹配@Builder函数参数的类型。

使用方法：

```
1. let builderVar: WrappedBuilder<[string, number]> = wrapBuilder(MyBuilder);
2. let builderArr: WrappedBuilder<[string, number]>[] = [wrapBuilder(MyBuilder)]; // 可以放入数组
```

## 限制条件

1. wrapBuilder方法只能传入[全局@Builder](arkts-builder.md#全局自定义构建函数)方法。
2. WrappedBuilder对象的builder属性方法仅限在struct内部使用。

## @Builder方法赋值给变量

使用@Builder装饰器装饰的方法myBuilder作为wrapBuilder的参数，然后将wrapBuilder的返回值赋值给变量globalBuilder，以解决@Builder方法赋值给变量后无法使用的问题。

```
1. @Builder
2. function myBuilder(value: string, size: number) {
3. Text(value)
4. .fontSize(size)
5. }

7. let globalBuilder: WrappedBuilder<[string, number]> = wrapBuilder(myBuilder);

9. @Entry
10. @Component
11. struct TestIndex {
12. @State message: string = 'Hello World';

14. build() {
15. Row() {
16. Column() {
17. globalBuilder.builder(this.message, 50)
18. }
19. .width('100%')
20. }
21. .height('100%')
22. }
23. }
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/wrapbuilder/entry/src/main/ets/pages/PageTwo.ets#L15-L39)

## @Builder方法赋值给变量在UI语法中使用

自定义组件IndexItem使用ForEach进行不同@Builder函数的渲染，可以使用builderArr声明的wrapBuilder数组来实现不同的@Builder函数的效果。整体代码会更加整洁。

```
1. @Builder
2. function myBuilder0(value: string, size: number) {
3. Text(value)
4. .fontSize(size)
5. .fontColor(Color.Blue)
6. }

8. @Builder
9. function yourBuilder(value: string, size: number) {
10. Text(value)
11. .fontSize(size)
12. .fontColor(Color.Pink)
13. }

15. const builderArr: WrappedBuilder<[string, number]>[] = [wrapBuilder(myBuilder0), wrapBuilder(yourBuilder)];

17. @Entry
18. @Component
19. struct IndexItem {
20. @Builder
21. IndexItem() {
22. ForEach(builderArr, (item: WrappedBuilder<[string, number]>) => {
23. item.builder('Hello World', 30);
24. })
25. }

27. build() {
28. Row() {
29. Column() {
30. this.IndexItem();
31. }
32. .width('100%')
33. }
34. .height('100%')
35. }
36. }
```

[PageThree.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/wrapbuilder/entry/src/main/ets/pages/PageThree.ets#L15-L52)

## @Builder方法赋值给类或者接口的属性

使用@Builder装饰器装饰的方法MyBuilder作为wrapBuilder的参数，然后将wrapBuilder的返回值赋值给接口ChildOptions中的属性，可以以数据的形式传递给其他子组件调用。

```
1. @Builder
2. function MyBuilder(value: string, size: number) {
3. Text(value)
4. .fontSize(size)
5. }

7. interface ChildOptions {
8. wrappedBuilder: WrappedBuilder<[string, number]>; // 类型为WrappedBuilder的属性可以传递@Builder函数
9. }

11. @Entry
12. @Component
13. struct Index {
14. childOptions: ChildOptions = {
15. wrappedBuilder: wrapBuilder(MyBuilder)
16. };

18. build() {
19. Row() {
20. Column() {
21. Child({ options: this.childOptions })
22. }
23. .width('100%')
24. }
25. .height('100%')
26. }
27. }

29. @Component
30. struct Child {
31. @Prop options: ChildOptions;
32. build() {
33. this.options.wrappedBuilder.builder('Hello', 20);
34. }
35. }
```

## 引用传递

按引用传递参数时，状态变量的改变会引起@Builder方法内的UI刷新。

```
1. class Tmp {
2. public paramA2: string = 'hello';
3. }

5. @Builder
6. function overBuilder(param: Tmp) {
7. Column() {
8. Text(`wrapBuildervalue:${param.paramA2}`)
9. }
10. }

12. const wBuilder: WrappedBuilder<[Tmp]> = wrapBuilder(overBuilder);

14. @Entry
15. @Component
16. struct Parent {
17. @State label: Tmp = new Tmp();

19. build() {
20. Column() {
21. wBuilder.builder({ paramA2: this.label.paramA2 })
22. Button('Click me').onClick(() => {
23. this.label.paramA2 = 'ArkUI';
24. })
25. }
26. }
27. }
```

[PageFour.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/wrapbuilder/entry/src/main/ets/pages/PageFour.ets#L15-L43)

## 常见问题

### 重复定义wrapBuilder失效

在同一个自定义组件内，同一个wrapBuilder只能初始化一次。例如，builderObj通过wrapBuilder(MyBuilderFirst)初始化后，再次对builderObj赋值wrapBuilder(MyBuilderSecond)将不会生效。

```
1. @Builder
2. function myBuilderFirst(value: string, size: number) {
3. Text('MyBuilderFirst：' + value)
4. .fontSize(size)
5. }

7. @Builder
8. function myBuilderSecond(value: string, size: number) {
9. Text('MyBuilderSecond：' + value)
10. .fontSize(size)
11. }

13. interface BuilderModel {
14. globalBuilder: WrappedBuilder<[string, number]>;
15. }

17. @Entry
18. @Component
19. struct TestBuilderIndex {
20. @State message: string = 'Hello World';
21. @State builderObj: BuilderModel = { globalBuilder: wrapBuilder(myBuilderFirst) };

23. aboutToAppear(): void {
24. setTimeout(() => {
25. // wrapBuilder(myBuilderSecond) 不会生效
26. this.builderObj.globalBuilder = wrapBuilder(myBuilderSecond);
27. }, 1000);
28. }

30. build() {
31. Row() {
32. Column() {
33. this.builderObj.globalBuilder.builder(this.message, 20)
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
```

[PageFive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/wrapbuilder/entry/src/main/ets/pages/PageFive.ets#L15-L55)
