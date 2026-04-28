---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-require
title: @Require装饰器：校验构造传参
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > @Require装饰器：校验构造传参
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f93796da9105a4f249e903688f43b630755cfdcc3ef01bfb8fe69d1e2b2d83f
---

@Require是校验@Prop、@State、@Provide、@BuilderParam、@Param和普通变量（无状态装饰器修饰的变量）是否需要构造传参的一个装饰器。

说明

从API version 11开始对@Prop/@BuilderParam进行校验。

从API version 11开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

从API version 12开始对@State/@Provide/@Param/普通变量（无状态装饰器修饰的变量）进行校验。

## 概述

当@Require装饰器和[@Prop](arkts-prop.md)、[@State](arkts-state.md)、[@Provide](arkts-provide-and-consume.md)、[@Param](arkts-new-param.md)、[@BuilderParam](arkts-builderparam.md)、普通变量（无状态装饰器修饰的变量）结合使用时，在构造该自定义组件时，@Prop、@State、@Provide、@Param、@BuilderParam和普通变量（无状态装饰器修饰的变量）必须在构造时传参。

## 限制条件

@Require装饰器仅用于装饰struct内的@Prop、@State、@Provide、@BuilderParam、@Param和普通变量（无状态装饰器修饰的变量）。

预览器的限制场景请参考[PreviewChecker检测规则](../harmonyos-guides-V5/ide-previewer-previewchecker-V5.md)。

## 使用场景

当Child组件内使用@Require装饰器和@Prop、@State、@Provide、@BuilderParam、@Param和普通变量（无状态装饰器修饰的变量）结合使用时，父组件SceneRequire在构造Child时必须传参，否则编译不通过。

```
1. @Entry
2. @Component
3. struct SceneRequire {
4. @State message: string = 'Hello World';

6. @Builder
7. buildTest() {
8. Row() {
9. Text('Hello, world')
10. .fontSize(30)
11. }
12. }

14. build() {
15. Row() {
16. // 构造Child时需传入所有@Require对应参数，否则编译失败。
17. Child({
18. regularValue: this.message,
19. stateValue: this.message,
20. provideValue: this.message,
21. initMessage: this.message,
22. message: this.message,
23. buildTest: this.buildTest,
24. initBuildTest: this.buildTest
25. })
26. }
27. }
28. }

30. @Component
31. struct Child {
32. @Require regularValue: string;
33. @Require @State stateValue: string;
34. @Require @Provide provideValue: string;
35. @Require @BuilderParam buildTest: () => void;
36. @Require @BuilderParam initBuildTest: () => void;
37. @Require @Prop initMessage: string;
38. @Require @Prop message: string;

40. build() {
41. Column() {
42. Text(this.initMessage)
43. .fontSize(30)
44. Text(this.message)
45. .fontSize(30)
46. this.initBuildTest();
47. this.buildTest();
48. }
49. .width('100%')
50. .height('100%')
51. }
52. }
```

[SceneRequire.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RequireDemo/entry/src/main/ets/pages/SceneRequire.ets#L16-L69)

使用[@ComponentV2](arkts-create-custom-components.md#componentv2)修饰的自定义组件ChildPage通过父组件ParentPage进行初始化，因为有@Require装饰@Param，所以父组件必须进行构造赋值。

```
1. @ObservedV2
2. class Info {
3. @Trace public name: string = '';
4. @Trace public age: number = 0;
5. }

7. @ComponentV2
8. struct ChildPage {
9. @Require @Param childInfo: Info;
10. @Require @Param stateValue: string;

12. build() {
13. Column() {
14. Text(`ChildPage childInfo name :${this.childInfo.name}`)
15. .fontSize(15)
16. .height(30)
17. Text(`ChildPage childInfo age :${this.childInfo.age}`)
18. .fontSize(15)
19. .height(30)
20. Text(`ChildPage stateValue age :${this.stateValue}`)
21. .fontSize(15)
22. .height(30)
23. }
24. }
25. }

27. @Entry
28. @ComponentV2
29. struct ParentPage {
30. info1: Info = { name: 'Tom', age: 25 };
31. label1: string = 'Hello World';
32. @Local info2: Info = { name: 'Tom', age: 25 };
33. @Local label2: string = 'Hello World';

35. build() {
36. Column() {
37. Text(`info1: ${this.info1.name}  ${this.info1.age}`) // Text1。
38. .fontSize(25)
39. .height(30)
40. // 父组件ParentPage构造子组件ChildPage时进行了构造赋值。
41. // 为ChildPage中被@Require @Param装饰的childInfo和stateValue属性传入了值。
42. ChildPage({ childInfo: this.info1, stateValue: this.label1 }) // 创建自定义组件。
43. Text(`info2: ${this.info2.name}  ${this.info2.age}`) // Text2。
44. .fontSize(25)
45. .height(30)
46. // 同上，在父组件创建子组件的过程中进行构造赋值。
47. ChildPage({ childInfo: this.info2, stateValue: this.label2 }) // 创建自定义组件。
48. Button('change info1&info2')
49. .onClick(() => {
50. this.info1 = { name: 'Cat', age: 18 }; // Text1不会刷新，原因是info1没有装饰器装饰，监听不到值的改变。
51. this.info2 = { name: 'Cat', age: 18 }; // Text2会刷新，原因是info2有装饰器装饰，能够监听到值的改变。
52. this.label1 = 'Luck'; // 不会刷新，原因是label1没有装饰器装饰，监听不到值的改变。
53. this.label2 = 'Luck'; // 会刷新，原因是label2有装饰器装饰，可以监听到值的改变。
54. })
55. }
56. .width('100%')
57. }
58. }
```

[ParentPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RequireDemo/entry/src/main/ets/pages/ParentPage.ets#L16-L82)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/B7t0F5KsQgW4CGnaYmLGmQ/zh-cn_image_0000002552797938.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233859Z&HW-CC-Expire=86400&HW-CC-Sign=CF084852B5353FDE31E2F0F394B8FE962E1369617E2609E022196DB5231E65EC)

从API version 18开始，使用@Require装饰@State、@Prop、@Provide装饰的状态变量，可以在无本地初始值的情况下直接在组件内使用，不会编译报错。

```
1. @Entry
2. @Component
3. struct PageOne {
4. message: string = 'Hello World';

6. build() {
7. Column() {
8. ChildIndex({ message: this.message })
9. }
10. }
11. }

13. @Component
14. struct ChildIndex {
15. @Require @State message: string;

17. build() {
18. Column() {
19. Text(this.message) // 从API version 18开始，可以编译通过。
20. }
21. }
22. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RequireDemo/entry/src/main/ets/pages/PageOne.ets#L16-L39)

## 常见问题

当状态管理V1组件内将@Require装饰器与@Prop、@State、@Provide、@BuilderParam、普通变量（无状态装饰器修饰的变量）结合使用时，若父组件Index在构造Child时未传递相应参数，则会导致编译失败。当状态管理V2组件内将@Require装饰器与@Param结合使用时，若父组件Index在构造ChildV2时未传递相应参数，则同样会导致编译失败。

【反例】

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World!';

6. @Builder
7. buildTest() {
8. Row() {
9. Text('Hello, world!!')
10. .fontSize(30)
11. }
12. }

14. build() {
15. Row() {
16. // 构造Child、ChildV2组件时没有传参，会导致编译不通过。
17. Child()
18. ChildV2()
19. }
20. }
21. }

23. @Component
24. struct Child {
25. // 使用@Require必须构造时传参。
26. @Require regularValue: string;
27. @Require @State stateValue: string;
28. @Require @Provide provideValue: string;
29. @Require @BuilderParam initBuildTest: () => void;
30. @Require @Prop initMessage: string;

32. build() {
33. Column() {
34. Text(this.initMessage)
35. .fontSize(30)
36. this.initBuildTest();
37. }
38. }
39. }

41. @ComponentV2
42. struct ChildV2 {
43. // 使用@Require必须构造时传参。
44. @Require @Param message: string;

46. build() {
47. Column() {
48. Text(this.message)
49. }
50. }
51. }
```

当父组件Example在构造ChildV1与ChildV2时传递了相应的参数，则编译通过。

【正例】

```
1. @Entry
2. @Component
3. struct Example {
4. @State message: string = 'Hello World!';

6. @Builder
7. buildTest() {
8. Row() {
9. Text('Hello, world!!')
10. .fontSize(30)
11. }
12. }

14. build() {
15. Row() {
16. // 构造ChildV1、ChildV2组件时传递相应参数，编译通过。
17. ChildV1({
18. regularValue: 'Hello',
19. stateValue: 'Hello',
20. provideValue: 'Hello',
21. initBuildTest: this.buildTest,
22. initMessage: 'Hello'
23. })
24. ChildV2({ message: this.message })
25. }
26. }
27. }

29. @Component
30. struct ChildV1 {
31. // 使用@Require必须构造时传参。
32. @Require regularValue: string;
33. @Require @State stateValue: string;
34. @Require @Provide provideValue: string;
35. @Require @BuilderParam initBuildTest: () => void;
36. @Require @Prop initMessage: string;

38. build() {
39. Column() {
40. Text(this.initMessage)
41. .fontSize(30)
42. this.initBuildTest();
43. }
44. }
45. }

47. @ComponentV2
48. struct ChildV2 {
49. // 使用@Require必须构造时传参。
50. @Require @Param message: string;

52. build() {
53. Column() {
54. Text(this.message)
55. }
56. }
57. }
```

[Example.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RequireDemo/entry/src/main/ets/pages/Example.ets#L16-L74)
