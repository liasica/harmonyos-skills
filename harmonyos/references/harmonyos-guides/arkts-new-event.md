---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-event
title: @Event装饰器：规范组件输出
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理组件拥有的状态 > @Event装饰器：规范组件输出
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:18+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d0680dcbc18eae2c374a684a265845ccb71fb4cbd6810c746fc77e0e4bab806c
---

为了实现子组件向父组件要求更新@Param装饰变量的能力，开发者可以使用@Event装饰器。使用@Event装饰回调方法是一种规范，表明子组件需要传入更新数据源的回调。

@Event主要配合@Param实现数据的双向同步。在阅读本文档前，建议提前阅读：[@Param](arkts-new-param.md)。

说明

从API version 12开始，在@ComponentV2装饰的自定义组件中支持使用@Event装饰器。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

## 概述

由于@Param装饰的变量在本地无法更改，使用@Event装饰器装饰回调方法并调用，可以实现更新数据源的变量，再通过[@Local](arkts-new-local.md)的同步机制，将修改同步回@Param装饰的变量，以此达到主动更新@Param装饰变量的效果。

@Event用于装饰组件对外输出的方法：

* @Event装饰的回调方法中参数以及返回值由开发者决定。
* @Event装饰非回调类型的变量不会生效。当@Event没有初始化时，会自动生成一个空的函数作为默认回调。
* 当@Event未被外部初始化，但本地有默认值时，会使用本地默认的函数进行处理。

@Param标志着组件的输入，表明该变量受父组件影响，而@Event标志着组件的输出，可以通过该方法影响父组件。使用@Event装饰回调方法是一种规范，表明该回调作为自定义组件的输出。父组件需要判断是否提供对应方法用于子组件更改@Param变量的数据源。

## 装饰器说明

| @Event属性装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 允许装饰的变量类型 | 回调方法，例如()=>void、(x:number)=>boolean等。回调方法是否含有参数以及返回值由开发者决定。 |
| 允许传入的函数类型 | 箭头函数。 |

## 限制条件

* @Event只能用在[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件中。当装饰非方法类型的变量时，不会有任何作用。

  ```
  1. @ComponentV2
  2. struct Index {
  3. @Event changeFactory: () => void = () => {}; // 正确用法
  4. @Event message: string = 'abcd'; // 错误用法，装饰非函数类型变量，@Event无作用
  5. }
  6. @Component
  7. struct Index {
  8. @Event changeFactory: () => void = () => {}; // 错误用法，编译时报错
  9. }
  ```

## 使用场景

### 更改父组件中变量

使用@Event可以更改父组件中变量，当该变量作为子组件@Param变量的数据源时，该变化会同步回子组件的@Param变量。

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Local title: string = 'Title One';
5. @Local fontColor: Color = Color.Red;

7. build() {
8. Column() {
9. Child({
10. title: this.title,
11. fontColor: this.fontColor,
12. changeFactory: (type: number) => {
13. if (type == 1) {
14. this.title = 'Title One';
15. this.fontColor = Color.Red;
16. } else if (type == 2) {
17. this.title = 'Title Two';
18. this.fontColor = Color.Green;
19. }
20. }
21. })
22. }
23. }
24. }

26. @ComponentV2
27. struct Child {
28. @Param title: string = '';
29. @Param fontColor: Color = Color.Black;
30. @Event changeFactory: (x: number) => void = (x: number) => {};

32. build() {
33. Column() {
34. Text(`${this.title}`)
35. .fontColor(this.fontColor)
36. // 使用changeFactory更改父组件中的变量type
37. Button('change to Title Two')
38. .onClick(() => {
39. this.changeFactory(2);
40. })
41. Button('change to Title One')
42. .onClick(() => {
43. this.changeFactory(1);
44. })
45. }
46. }
47. }
```

[EventDecoratorTest1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventDecorator/entry/src/main/ets/pages/EventDecoratorTest1.ets#L15-L62)

值得注意的是，使用@Event修改父组件的值是立刻生效的，但从父组件将变化同步回子组件的过程是异步的，即在调用完@Event的方法后，子组件内的值不会立刻变化。这是因为@Event将子组件值实际的变化能力交由父组件处理，在父组件实际决定如何处理后，将最终值在渲染之前同步回子组件。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const TAG = '[Sample_EventDecorator]';
3. const DOMAIN = 0xF811;
4. @ComponentV2
5. struct Child2 {
6. @Param index: number = 0;
7. @Event changeIndex: (val: number) => void;

9. build() {
10. Column() {
11. Text(`Child index: ${this.index}`)
12. .onClick(() => {
13. this.changeIndex(20);
14. // 输出子组件this.index，验证调用@Event后值不会立即同步回子组件
15. hilog.info(DOMAIN, TAG, `after changeIndex ${this.index}`);
16. })
17. }
18. }
19. }
20. @Entry
21. @ComponentV2
22. struct Index2 {
23. @Local index: number = 0;

25. build() {
26. Column() {
27. Child2({
28. index: this.index,
29. changeIndex: (val: number) => {
30. this.index = val;
31. // 输出父组件的index，用于对比子组件侧日志
32. hilog.info(DOMAIN, TAG, `in changeIndex ${this.index}`);
33. }
34. })
35. }
36. }
37. }
```

[EventDecoratorTest2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventDecorator/entry/src/main/ets/pages/EventDecoratorTest2.ets#L15-L52)

在上面的示例中，点击文字触发@Event函数事件改变子组件的值，打印出的日志为：

```
1. in changeIndex 20
2. after changeIndex 0
```

这表明在调用changeIndex之后，父组件中index的值已经变化，但子组件中的index值还没有同步变化。
