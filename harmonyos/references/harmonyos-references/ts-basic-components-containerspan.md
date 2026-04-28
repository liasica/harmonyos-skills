---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan
title: ContainerSpan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > ContainerSpan
category: harmonyos-references
scraped_at: 2026-04-28T08:01:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:14ef60e18acdfc173624e4d3b181893f1d09992aad1a68ee8909ffcca8fc08fa
---

[Text](ts-basic-components-text.md)组件的子组件，用于统一管理多个[Span](ts-basic-components-span.md)、[ImageSpan](ts-basic-components-imagespan.md)的背景色及圆角弧度。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含[Span](ts-basic-components-span.md)、[ImageSpan](ts-basic-components-imagespan.md) 子组件。

## 接口

PhonePC/2in1TabletTVWearable

ContainerSpan()

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

仅支持以下属性：

### textBackgroundStyle

PhonePC/2in1TabletTVWearable

textBackgroundStyle(style: TextBackgroundStyle)

设置文本背景样式。子组件在不设置该属性时，将继承此属性值。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11对象说明) | 是 | 文本背景样式。  默认值：  {  color: Color.Transparent,  radius: 0  } |

### attributeModifier12+

PhonePC/2in1TabletTVWearable

attributeModifier(modifier: AttributeModifier<ContainerSpanAttribute>)

设置组件的动态属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifiert)<ContainerSpanAttribute> | 是 | 动态设置组件的属性。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](ts-basic-components-containerspan.md#textbackgroundstyle)属性展示了文本设置背景样式的效果。

```
1. // xxx.ets
2. @Component
3. @Entry
4. struct Index {
5. build() {
6. Column() {
7. Text() {
8. ContainerSpan() {
9. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
10. ImageSpan($r('app.media.app_icon'))
11. .width('40vp')
12. .height('40vp')
13. .verticalAlign(ImageSpanAlignment.CENTER)
14. Span('   Hello World !   ').fontSize('16fp').fontColor(Color.White)
15. }
16. .textBackgroundStyle({
17. color: "#7F007DFF",
18. radius: {
19. topLeft: 12,
20. topRight: 12,
21. bottomLeft: 12,
22. bottomRight: 12
23. }
24. })
25. }
26. }.width('100%').alignItems(HorizontalAlign.Center)
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/aTS0fy8FTTCwh8RzOpSxjQ/zh-cn_image_0000002552800166.png?HW-CC-KV=V1&HW-CC-Date=20260428T000149Z&HW-CC-Expire=86400&HW-CC-Sign=D75D13B8F0F5F8F3F8DB060D07C2090728BB427ED8DA4B7048F0E8769677028F)

### 示例2（通过attributeModifier设置背景样式）

从API version 12开始，该示例通过[attributeModifier](ts-basic-components-containerspan.md#attributemodifier12)属性展示了文本设置背景样式的效果。

```
1. import { ContainerSpanModifier } from '@kit.ArkUI';

3. class MyContainerSpanModifier extends ContainerSpanModifier {
4. applyNormalAttribute(instance: ContainerSpanAttribute): void {
5. super.applyNormalAttribute?.(instance);
6. this.textBackgroundStyle({ color: "#7F007DFF", radius: "12vp" });
7. }
8. }

10. @Entry
11. @Component
12. struct ContainerSpanModifierExample {
13. @State containerSpanModifier: ContainerSpanModifier = new MyContainerSpanModifier();

15. build() {
16. Column() {
17. Text() {
18. ContainerSpan() {
19. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
20. ImageSpan($r('app.media.startIcon'))
21. .width('40vp')
22. .height('40vp')
23. .verticalAlign(ImageSpanAlignment.CENTER)
24. Span(' I\'m ContainerSpan attributeModifier ').fontSize('16fp').fontColor(Color.White)
25. }.attributeModifier(this.containerSpanModifier as MyContainerSpanModifier)
26. }
27. }.width('100%').alignItems(HorizontalAlign.Center)
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/v8zcH3q4SM2jrzvGVpmYaw/zh-cn_image_0000002583439861.png?HW-CC-KV=V1&HW-CC-Date=20260428T000149Z&HW-CC-Expire=86400&HW-CC-Sign=49BBE053F2097C4F8461D6B7714BA09CF58EC28E093E177DF788F0B865A9BBC8)
