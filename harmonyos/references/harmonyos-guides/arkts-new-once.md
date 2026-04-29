---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-once
title: @Once：初始化同步一次
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理组件拥有的状态 > @Once：初始化同步一次
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:18+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c59547b60fd402aef91fdd279e8e94a96304e33ca4f193ddbae414cfe1bb6c64
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
3. // @Once装饰的onceParam仅初始化同步一次
4. @Param @Once onceParam: string = '';

6. build() {
7. Column() {
8. Text(`onceParam: ${this.onceParam}`)
9. }
10. }
11. }

13. @Entry
14. @ComponentV2
15. struct MyComponent {
16. // ...
17. @Local message: string = 'Hello World';

19. build() {
20. Column() {
21. Text(`Parent message: ${this.message}`)
22. Button('change message')
23. .onClick(() => {
24. this.message = 'Hello Tomorrow';
25. })
26. ChildComponent({ onceParam: this.message })
27. }
28. }
29. }
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
10. // @Once与@Param结合使用时，可以在本地修改，并能够触发UI刷新
11. @Param @Once onceParamNum: number = 0;
12. @Param @Once @Require onceParamInfo: Info;

14. build() {
15. Column() {
16. Text(`Child onceParamNum: ${this.onceParamNum}`)
17. Text(`Child onceParamInfo: ${this.onceParamInfo.name}`)
18. Button('changeOnceParamNum')
19. .onClick(() => {
20. this.onceParamNum++;
21. })
22. Button('changeParamInfo')
23. .onClick(() => {
24. this.onceParamInfo = new Info('Cindy');
25. })
26. }
27. }
28. }
29. @Entry
30. @ComponentV2
31. struct Index {
32. @Local localNum: number = 10;
33. @Local localInfo: Info = new Info('Tom');

35. build() {
36. Column() {
37. Text(`Parent localNum: ${this.localNum}`)
38. Text(`Parent localInfo: ${this.localInfo.name}`)
39. Button('changeLocalNum')
40. .onClick(() => {
41. this.localNum++;
42. })
43. Button('changeLocalInfo')
44. .onClick(() => {
45. this.localInfo = new Info('Cindy');
46. })
47. Child({
48. onceParamNum: this.localNum,
49. onceParamInfo: this.localInfo
50. })
51. }
52. }
53. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsNewOnce/entry/src/main/ets/pages/Index.ets#L16-L69)
