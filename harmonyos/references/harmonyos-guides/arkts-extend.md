---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend
title: @Extend装饰器：定义扩展组件样式
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > @Extend装饰器：定义扩展组件样式
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8805606868f36cc4cbdafd280e1152a6554cefcd2c8336667c4e192f899c185a
---

在前文的示例中，可以使用[@Styles](arkts-style.md)用于样式的重用，在@Styles的基础上，我们提供了@Extend，用于扩展组件样式。

说明

从API version 9开始支持。

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

### 语法

```
1. @Extend(UIComponentName) function functionName { ... }
```

### 使用规则

* 和@Styles不同，@Extend支持封装指定组件的私有属性、私有事件和自身定义的全局方法。

  ```
  1. // @Extend(Text)可以支持Text的私有属性fontColor
  2. @Extend(Text)
  3. function fancy() {
  4. .fontColor(Color.Red)
  5. }

  7. // superFancyText可以调用预定义的fancy
  8. @Extend(Text)
  9. function superFancyText(size: number) {
  10. .fontSize(size)
  11. .fancy()
  12. }
  ```

  [GlobalFunctionExtension.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/GlobalFunctionExtension.ets#L29-L42)
* 使用@Extend封装指定组件的私有属性、私有事件和自身定义的全局方法时，不支持和@Styles混用。

  ```
  1. @Styles
  2. function fancy() {
  3. .backgroundColor(Color.Red)
  4. }

  6. // superFancyText不可以调用预定义的fancy
  7. @Extend(Text)
  8. function superFancyText(size: number) {
  9. .fontSize(size)
  10. .fancy()
  11. }
  ```
* 和@Styles不同，@Extend装饰的方法支持传入参数，调用遵循TS方法传值调用。

  ```
  1. // xxx.ets
  2. @Extend(Text)
  3. function fancy(fontSize: number) {
  4. .fontColor(Color.Red)
  5. .fontSize(fontSize)
  6. }

  8. @Entry
  9. @Component
  10. struct FancyUse {
  11. build() {
  12. Row({ space: 10 }) {
  13. Text('Fancy')
  14. .fancy(16)
  15. Text('Fancy')
  16. .fancy(24)
  17. }
  18. }
  19. }
  ```

  [ExtendParameterUsage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendParameterUsage.ets#L28-L48)
* @Extend装饰的方法的参数可以为function，作为Event事件的句柄。

  ```
  1. @Extend(Text)
  2. function makeMeClick(onClick: () => void) {
  3. .backgroundColor(Color.Blue)
  4. .onClick(onClick)
  5. }

  7. @Entry
  8. @Component
  9. struct FancyUse {
  10. @State label: string = 'Hello World';

  12. onClickHandler() {
  13. this.label = 'Hello ArkUI';
  14. }

  16. build() {
  17. Row({ space: 10 }) {
  18. Text(`${this.label}`)
  19. .makeMeClick(() => {
  20. this.onClickHandler();
  21. })
  22. }
  23. }
  24. }
  ```

  [ExtendFunctionHandle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendFunctionHandle.ets#L29-L54)
* @Extend的参数可以为[状态变量](arkts-state-management-overview.md)，当状态变量改变时，UI可以正常的被刷新渲染。

  ```
  1. @Extend(Text)
  2. function fancy(fontSize: number) {
  3. .fontColor(Color.Blue)
  4. .fontSize(fontSize)
  5. }

  7. @Entry
  8. @Component
  9. struct FancyUse {
  10. @State fontSizeValue: number = 20;

  12. build() {
  13. Column({ space: 10 }) {
  14. Text('Fancy')
  15. .fancy(this.fontSizeValue)
  16. .onClick(() => {
  17. this.fontSizeValue = 30;
  18. })
  19. }
  20. .width('100%')
  21. }
  22. }
  ```

  [ExtendUIStateVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUIStateVariable.ets#L29-L51)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/ljCFbqSJSB-iiaMDDWKteg/zh-cn_image_0000002558604418.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052706Z&HW-CC-Expire=86400&HW-CC-Sign=B4B0D7612736ADCAC37BAACAF2B5CFA87F507606E1223CC052BED215816B2EFD)

## 限制条件

* 和@Styles不同，@Extend仅支持在全局定义，不支持在组件内部定义。

说明

仅限在当前文件内使用，不支持导出。

如果要实现export功能，推荐使用[AttributeModifier](arkts-user-defined-extension-attributemodifier.md)。

【反例】

```
1. @Entry
2. @Component
3. struct FancyUse {
4. // 错误写法，@Extend仅支持在全局定义，不支持在组件内部定义
5. @Extend(Text) function fancy (fontSize: number) {
6. .fontSize(fontSize)
7. }

9. build() {
10. Row({ space: 10 }) {
11. Text('Fancy')
12. .fancy(16)
13. }
14. }
15. }
```

【正例】

```
1. // 正确写法
2. @Extend(Text)
3. function fancy(fontSize: number) {
4. .fontSize(fontSize)
5. }

7. @Entry
8. @Component
9. struct FancyUse {
10. build() {
11. Row({ space: 10 }) {
12. Text('Fancy')
13. .fancy(16)
14. }
15. }
16. }
```

[ExtendPositiveExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendPositiveExample.ets#L29-L46)

## 使用场景

以下示例声明了3个Text组件，每个Text组件均设置了[fontStyle](../harmonyos-references/ts-appendix-enums.md#fontstyle)、[fontWeight](../harmonyos-references/ts-appendix-enums.md#fontweight) 和[backgroundColor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)样式。

```
1. @Entry
2. @Component
3. struct FancyUse {
4. @State label: string = 'Hello World';

6. build() {
7. Row({ space: 10 }) {
8. Text(`${this.label}`)
9. .fontStyle(FontStyle.Italic)
10. .fontWeight(500)
11. .backgroundColor(Color.Yellow)
12. Text(`${this.label}`)
13. .fontStyle(FontStyle.Italic)
14. .fontWeight(600)
15. .backgroundColor(Color.Pink)
16. Text(`${this.label}`)
17. .fontStyle(FontStyle.Italic)
18. .fontWeight(700)
19. .backgroundColor(Color.Orange)
20. }.margin('20%')
21. }
22. }
```

[ExtendUsageScenario.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenario.ets#L29-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/CZitWo0lQiqgAvmxJYezeg/zh-cn_image_0000002589323943.png?HW-CC-KV=V1&HW-CC-Date=20260429T052706Z&HW-CC-Expire=86400&HW-CC-Sign=D431E2D439C4AE55A6FECC4E04AF032BB76B23E94B3AF26EF7D668EB5AB6B41B)

使用@Extend将样式组合复用，示例如下。

```
1. @Extend(Text)
2. function fancyText(weightValue: number, color: Color) {
3. .fontStyle(FontStyle.Italic)
4. .fontWeight(weightValue)
5. .backgroundColor(color)
6. }
```

[ExtendUsageScenariotwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenariotwo.ets#L29-L36)

通过@Extend组合样式后，使得代码更加简洁，增强可读性。

```
1. @Entry
2. @Component
3. struct FancyUse {
4. @State label: string = 'Hello World';

6. build() {
7. Row({ space: 10 }) {
8. Text(`${this.label}`)
9. .fancyText(100, Color.Blue)
10. Text(`${this.label}`)
11. .fancyText(200, Color.Pink)
12. Text(`${this.label}`)
13. .fancyText(300, Color.Orange)
14. }.margin('20%')
15. }
16. }
```

[ExtendUsageScenariotwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/extend/ExtendUsageScenariotwo.ets#L37-L54)
