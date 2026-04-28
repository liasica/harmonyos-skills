---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-once
title: @Once：初始化同步一次
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理组件拥有的状态 > @Once：初始化同步一次
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5428eded4b5c066df6a60ecb5fcfb0c63e574952b3fcaea79f6087779db15592
---

想要实现仅从外部初始化一次且不接受后续同步变化的能力，可以使用@Once装饰器搭配@Param装饰器。

阅读本文档前，请先阅读[@Param](arkts-new-param.md)。

说明

从API version 12开始，在@ComponentV2装饰的自定义组件中支持使用@Once装饰器。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Once装饰器在变量初始化时接受外部传入值进行初始化，后续数据源更改不会同步给子组件：

* @Once必须搭配@Param使用，单独使用或搭配其他装饰器使用都是不允许的。
* @Once不影响@Param的观测能力，仅针对数据源的变化做拦截。
* @Once与@Param装饰变量的先后顺序不影响使用功能。
* @Once与@Param搭配使用时，可以在本地修改@Param变量的值。

## 装饰器使用规则说明

@Once装饰器作为辅助装饰器，本身没有装饰类型要求和变量观察能力。

| @Once变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 使用条件 | 无法单独使用，必须配合@Param装饰器使用。 |

## 限制条件

* @Once仅在[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件中与@Param搭配使用。

  ```
  1. @ComponentV2
  2. struct MyComponent {
  3. @Param @Once onceParam: string = 'onceParam'; // 正确用法
  4. @Once onceStr: string = 'Once'; // 错误用法，@Once无法单独使用
  5. @Local @Once onceLocal: string = 'onceLocal'; // 错误用法，@Once不能与@Local一起使用
  6. // ···
  7. }
  8. @Component
  9. struct Index {
  10. @Once @Param onceParam: string = 'onceParam'; // 错误用法
  11. }
  ```

  [MyComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewOnce/entry/src/main/ets/pages/MyComponent.ets#L29-L57)
* @Once与@Param的先后顺序无关，可以写成@Param @Once也可以写成@Once @Param。

  ```
  1. @ComponentV2
  2. struct MyComponent {
  3. // ···
  4. @Param @Once param1: number = 0;
  5. @Once @Param param2: number = 0;
  6. // ···
  7. }
  ```

  [MyComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewOnce/entry/src/main/ets/pages/MyComponent.ets#L30-L58)

## 使用场景

### 变量仅初始化同步一次

@Once用于期望变量仅初始化同步数据源一次，之后不再继续同步变化的场景。

```
1. @ComponentV2
2. struct ChildComponent {
3. @Param @Once onceParam: string = '';

5. build() {
6. Column() {
7. Text(`onceParam: ${this.onceParam}`)
8. }
9. }
10. }

12. @Entry
13. @ComponentV2
14. struct MyComponent {
15. // ···
16. @Local message: string = 'Hello World';

18. build() {
19. Column() {
20. Text(`Parent message: ${this.message}`)
21. Button('change message')
22. .onClick(() => {
23. this.message = 'Hello Tomorrow';
24. })
25. ChildComponent({ onceParam: this.message })
26. }
27. }
28. }
```

[MyComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewOnce/entry/src/main/ets/pages/MyComponent.ets#L16-L59)

### 本地修改@Param变量

当@Once与@Param结合使用时，可以解除@Param无法在本地修改的限制，并能够触发UI刷新。此时，使用@Param和@Once的效果类似于[@Local](arkts-new-local.md)，但@Param和@Once还能接收外部传入的初始值。

```
1. @ObservedV2
2. class Info {
3. @Trace name: string;
4. constructor(name: string) {
5. this.name = name;
6. }
7. }
8. @ComponentV2
9. struct Child {
10. @Param @Once onceParamNum: number = 0;
11. @Param @Once @Require onceParamInfo: Info;

13. build() {
14. Column() {
15. Text(`Child onceParamNum: ${this.onceParamNum}`)
16. Text(`Child onceParamInfo: ${this.onceParamInfo.name}`)
17. Button('changeOnceParamNum')
18. .onClick(() => {
19. this.onceParamNum++;
20. })
21. Button('changeParamInfo')
22. .onClick(() => {
23. this.onceParamInfo = new Info('Cindy');
24. })
25. }
26. }
27. }
28. @Entry
29. @ComponentV2
30. struct Index {
31. @Local localNum: number = 10;
32. @Local localInfo: Info = new Info('Tom');

34. build() {
35. Column() {
36. Text(`Parent localNum: ${this.localNum}`)
37. Text(`Parent localInfo: ${this.localInfo.name}`)
38. Button('changeLocalNum')
39. .onClick(() => {
40. this.localNum++;
41. })
42. Button('changeLocalInfo')
43. .onClick(() => {
44. this.localInfo = new Info('Cindy');
45. })
46. Child({
47. onceParamNum: this.localNum,
48. onceParamInfo: this.localInfo
49. })
50. }
51. }
52. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewOnce/entry/src/main/ets/pages/Index.ets#L16-L69)
