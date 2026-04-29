---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style
title: @Styles装饰器：定义组件重用样式
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > @Styles装饰器：定义组件重用样式
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2ba5b54f45cad71dc3f695eb9a2f8272756a54fb194dbb436c0b593e242f52f5
---

如果每个组件的样式都需要单独设置，在开发过程中会出现大量代码在进行重复样式设置，虽然可以复制粘贴，但为了代码简洁性和后续方便维护，我们推出了可以提炼公共样式进行复用的装饰器@Styles。

@Styles装饰器可以将多条样式设置提炼成一个方法，直接在组件声明的位置调用。通过@Styles装饰器可以快速定义并复用自定义样式。

说明

从API version 9开始支持。

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

* 当前@Styles仅支持[通用属性](../harmonyos-references/ts-component-general-attributes.md)和[通用事件](../harmonyos-references/ts-component-general-events.md)。
* @Styles可以定义在组件内或全局，在全局定义时需在方法名前面添加function关键字，组件内定义时则不需要添加function关键字。请参考用例[组件内styles和全局styles的用法](arkts-style.md#组件内styles和全局styles的用法)。
* 组件内@Styles的优先级高于全局@Styles。框架优先找当前组件内的@Styles，如果找不到，则会全局查找。

说明

只能在当前文件内使用@Styles，不支持export。

若需要实现样式导出，推荐使用[AttributeModifier](arkts-user-defined-extension-attributemodifier.md)。

定义在组件内的@Styles可以通过this访问组件的常量和状态变量，并可以在@Styles里通过事件来改变状态变量的值，示例如下：

```
1. @Entry
2. @Component
3. struct FancyUse {
4. @State heightValue: number = 50;

6. @Styles
7. fancy() {
8. .height(this.heightValue)
9. .backgroundColor(Color.Blue)
10. .onClick(() => {
11. this.heightValue = 100;
12. })
13. }

15. build() {
16. Column() {
17. Button('change height')
18. .fancy()
19. }
20. .height('100%')
21. .width('100%')
22. }
23. }
```

[StylesDecorator2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentExtension/entry/src/main/ets/pages/StylesDecorator/StylesDecorator2.ets#L30-L54)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/AQel9SoKSlyNIRxh_KvZzA/zh-cn_image_0000002589243881.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052706Z&HW-CC-Expire=86400&HW-CC-Sign=33CA2670F95FD4BD8D29496948667739E7E3124857AD865F803A0C7617B835E8)

## 限制条件

* @Styles方法不支持传入参数，编译期会报错。

```
1. // 错误写法： @Styles不支持参数，编译期报错
2. @Styles
3. function globalFancy (value: number) {
4. .width(value)
5. }
```

```
1. // 正确写法
2. @Styles
3. function globalFancy () {
4. .width(100)
5. }
```

[StylesDecorator2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentExtension/entry/src/main/ets/pages/StylesDecorator/StylesDecorator2.ets#L16-L22)

* 不支持在@Styles方法内使用逻辑组件，逻辑组件内的属性不生效。

```
1. // 错误写法
2. @Styles
3. function backgroundColorStyle() {
4. if (true) {
5. .backgroundColor(Color.Red)
6. }
7. }
```

```
1. // 正确写法
2. @Styles
3. function backgroundColorStyle() {
4. .backgroundColor(Color.Red)
5. }
```

[StylesDecorator2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentExtension/entry/src/main/ets/pages/StylesDecorator/StylesDecorator2.ets#L23-L29)

## 使用场景

### 组件内@Styles和全局@Styles的用法

```
1. // 定义在全局的@Styles封装的样式
2. @Styles
3. function globalFancy1() {
4. .width(150)
5. .height(100)
6. .backgroundColor(Color.Pink)
7. }

9. @Entry
10. @Component
11. struct GlobalFancy {
12. @State heightValue: number = 100;

14. // 定义在组件内的@Styles封装的样式
15. @Styles
16. fancy() {
17. .width(200)
18. .height(this.heightValue)
19. .backgroundColor(Color.Gray)
20. .onClick(() => {
21. this.heightValue = 200;
22. })
23. }

25. build() {
26. Column({ space: 10 }) {
27. // 使用全局的@Styles封装的样式
28. Text('FancyA')
29. .globalFancy1()
30. .fontSize(30)
31. // 使用组件内的@Styles封装的样式
32. Text('FancyB')
33. .fancy()
34. .fontSize(30)
35. }
36. .width('100%')
37. }
38. }
```

[StylesDecorator1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ComponentExtension/entry/src/main/ets/pages/StylesDecorator/StylesDecorator1.ets#L16-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/sCZXEUc1ShanBDN58WZMxw/zh-cn_image_0000002558764074.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052706Z&HW-CC-Expire=86400&HW-CC-Sign=14FA02F6AD6D0D00B20175E512F6A6C5472CE453830BC5B2EEC2BE3066005FDD)
