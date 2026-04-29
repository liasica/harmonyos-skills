---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-stack-layout
title: 层叠布局 (Stack)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 层叠布局 (Stack)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b66703cd66d47b2d5d16b95c57edf71ad6c265066ae5aa65bca417791248fa73
---

## 概述

层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](../harmonyos-references/ts-container-stack.md)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素的顺序为Item1->Item2->Item3。

**图1** 层叠布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/MhCg7vp3RciQ26Z8CvhRLg/zh-cn_image_0000002558604546.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=82E7BDF4379879EF203E7B9FE00675816E1E3AD51691C87BCDCB5EE1D18A9D9D)

说明

过多的嵌套组件数会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠布局的效果，减少了嵌套组件数进而优化性能。最佳实践请参考[组件嵌套优化-优先使用组件属性代替嵌套组件](../best-practices/bpta-component-nesting-optimization.md#section78181114123811)。

## 开发布局

Stack组件为容器组件，容器内可包含各种子元素。其中子元素默认进行居中堆叠。子元素被约束在Stack下，进行自己的样式定义以及排列。

```
1. // xxx.ets
2. let mTop:Record<string,number> = { 'top': 50 }

4. @Entry
5. @Component
6. struct StackLayoutExample {
7. build() {
8. Column(){
9. Stack({ }) {
10. Column(){}.width('90%').height('100%').backgroundColor('#ff58b87c')
11. Text('text').width('60%').height('60%').backgroundColor('#ffc3f6aa')
12. Button('button').width('30%').height('30%').backgroundColor('#ff8ff3eb').fontColor('#000')
13. }.width('100%').height(150).margin(mTop)
14. }
15. }
16. }
```

[StackLayoutExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/stacklayout/StackLayoutExample.ets#L15-L32)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/GSZ0HvukRimR2nfuYqHaNg/zh-cn_image_0000002589324071.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=C9404FFDA9A22543F2D3700293AE74762D59DF282CA0312BA3B4DA8066877C17)

## 对齐方式

Stack组件通过[alignContent参数](../harmonyos-references/ts-container-stack.md#aligncontent)实现位置的相对移动。如图2所示，支持九种对齐方式。

**图2** Stack容器内元素的对齐方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/qfhX9XxwQNS58LobTlDvtw/zh-cn_image_0000002589244011.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=3534547F70221716EC6326CF95D704CFE745852392C92BF7FB8C32915CE3B537)

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StackAlignContentExample {
5. build() {
6. Stack({ alignContent: Alignment.TopStart }) {
7. Text('Stack').width('90%').height('100%').backgroundColor('#e1dede').align(Alignment.BottomEnd)
8. Text('Item 1').width('70%').height('80%').backgroundColor(0xd2cab3).align(Alignment.BottomEnd)
9. Text('Item 2').width('50%').height('60%').backgroundColor(0xc1cbac).align(Alignment.BottomEnd)
10. }.width('100%').height(150).margin({ top: 5 })
11. }
12. }
```

[StackLayoutAlignContent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/stacklayout/StackLayoutAlignContent.ets#L15-L28)

## Z序控制

Stack容器中兄弟组件显示层级关系可以通过[Z序控制](../harmonyos-references/ts-universal-attributes-z-order.md)的zIndex属性改变。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

在层叠布局中，如果后面子元素尺寸大于前面子元素尺寸，则前面子元素完全隐藏。

```
1. Stack({ alignContent: Alignment.BottomStart }) {
2. Column() {
3. // 请将$r('app.string.stack_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
4. Text($r('app.string.stack_num1')).textAlign(TextAlign.End).fontSize(20)
5. }.width(100).height(100).backgroundColor(0xffd306)

7. Column() {
8. // 请将$r('app.string.stack_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
9. Text($r('app.string.stack_num2')).fontSize(20)
10. }.width(150).height(150).backgroundColor(Color.Pink)

12. Column() {
13. // 请将$r('app.string.stack_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
14. Text($r('app.string.stack_num3')).fontSize(20)
15. }.width(200).height(200).backgroundColor(Color.Grey)
16. }.width(350).height(350).backgroundColor(0xe0e0e0)
```

[StackLayoutNozIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/stacklayout/StackLayoutNozIndex.ets#L20-L37)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/jQItktHJQYqiYapa-9kKtA/zh-cn_image_0000002558764204.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=4FECAA881392341A9334B7F69BB538BCDF3643338A1BC38383495BBB6E5E1CF5)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1、子元素2的zIndex属性后，可以将元素展示出来。

```
1. Stack({ alignContent: Alignment.BottomStart }) {
2. Column() {
3. // 请将$r('app.string.stack_num1')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素1"
4. Text($r('app.string.stack_num1')).fontSize(20)
5. }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)

7. Column() {
8. // 请将$r('app.string.stack_num2')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素2"
9. Text($r('app.string.stack_num2')).fontSize(20)
10. }.width(150).height(150).backgroundColor(Color.Pink).zIndex(1)

12. Column() {
13. // 请将$r('app.string.stack_num3')替换为实际资源文件，在本示例中该资源文件的value值为"Stack子元素3"
14. Text($r('app.string.stack_num3')).fontSize(20)
15. }.width(200).height(200).backgroundColor(Color.Grey)
16. }.width(350).height(350).backgroundColor(0xe0e0e0)
```

[StackLayoutzIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/stacklayout/StackLayoutzIndex.ets#L20-L37)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/OfFBirEtQQuW-7BFdgFBTQ/zh-cn_image_0000002558604548.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=7F92E7D318A530A7C44DFB31E357437510ADBD89963380B2319918CAAEE8C50E)

## 场景示例

使用层叠布局快速搭建页面。

```
1. @Entry
2. @Component
3. struct StackSample {
4. private arr: string[] = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7', 'APP8'];

6. build() {
7. Stack({ alignContent: Alignment.Bottom }) {
8. Flex({ wrap: FlexWrap.Wrap }) {
9. ForEach(this.arr, (item:string) => {
10. Text(item)
11. .width(100)
12. .height(100)
13. .fontSize(16)
14. .margin(10)
15. .textAlign(TextAlign.Center)
16. .borderRadius(10)
17. .backgroundColor(0xFFFFFF)
18. }, (item:string):string => item)
19. }.width('100%').height('100%')

21. Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
22. // 请将$r('app.string.contacts')替换为实际资源文件，在本示例中该资源文件的value值为"联系人"
23. Text($r('app.string.contacts')).fontSize(16)
24. // 请将$r('app.string.setting')替换为实际资源文件，在本示例中该资源文件的value值为"设置"
25. Text($r('app.string.setting')).fontSize(16)
26. // 请将$r('app.string.text_message')替换为实际资源文件，在本示例中该资源文件的value值为"短信"
27. Text($r('app.string.text_message')).fontSize(16)
28. }
29. .width('50%')
30. .height(50)
31. .backgroundColor('#16302e2e')
32. .margin({ bottom: 15 })
33. .borderRadius(15)
34. }.width('100%').height('100%').backgroundColor('#CFD0CF')
35. }
36. }
```

[StackLayoutSceneExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultipleLayoutProject/entry/src/main/ets/pages/stacklayout/StackLayoutSceneExample.ets#L15-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/qswuW_2STjazFp42z5yYtg/zh-cn_image_0000002589324073.png?HW-CC-KV=V1&HW-CC-Date=20260429T052738Z&HW-CC-Expire=86400&HW-CC-Sign=A4A2A27AF08EB081378023B00A4C53E16CF3473DC4E644DDA0AFAD84160E1F2A)

## 示例代码

* [组件堆叠](https://gitcode.com/HarmonyOS_Samples/component-stack)
