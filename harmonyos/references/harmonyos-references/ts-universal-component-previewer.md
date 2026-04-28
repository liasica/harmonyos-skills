---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-previewer
title: 组件预览
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 组件预览 > 组件预览
category: harmonyos-references
scraped_at: 2026-04-28T08:02:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:08de0fb88b05bd0db4e5b93d9494b1f6d0f4386aec0ef1b3c7b58b77ab20a520
---

组件预览支持以自定义组件为最小单位进行预览，方便开发者查看单个自定义组件UI效果。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

组件预览详情，请查看[组件预览特性文档](../harmonyos-guides/ui-ide-previewer.md#组件预览)。

## @Preview装饰器

PhonePC/2in1TabletTVWearable

@Preview装饰器用来装饰自定义组件，从而实现组件预览。

说明

该接口支持在ArkTS卡片中使用，但是ArkTS卡片中暂不支持组件预览。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## PreviewParams9+

PhonePC/2in1TabletTVWearable

@Preview参数对象。

设置@Preview的参数，指定预览设备的相关属性，如不同设备、不同屏幕状态等。

说明

PreviewParams中只支持使用与定义参数类型相匹配的入参，否则所有的@Preview的参数都将被置为默认值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| title | string | 否 | 是 | 组件预览模块名，默认为自定义组件名称。 |
| width | number | 否 | 是 | 预览设备的宽度，单位：px，默认为1080px。取值范围为[20, 3000]内的整数。 |
| height | number | 否 | 是 | 预览设备的高度，单位：px，默认为2340px。取值范围为[20, 3000]内的整数。 |
| locale | string | 否 | 是 | 预览设备的语言，如zh\_CN、en\_US等，默认为zh\_CN。 |
| colorMode | string | 否 | 是 | 显示的亮暗模式，tv设备默认为dark且仅支持dark，其他设备默认为light且仅支持light。 |
| deviceType | string | 否 | 是 | 组件预览渲染的设备类型，默认为Phone。设备类型枚举值参考[deviceTypes标签](../harmonyos-guides/module-configuration-file.md#devicetypes标签)。 |
| dpi | number | 否 | 是 | 预览设备的屏幕DPI值，默认为480。取值范围为[120, 640]内的整数。 |
| orientation | string | 否 | 是 | 预览设备的横竖屏状态，取值为portrait或landscape，默认为portrait。 |
| roundScreen | boolean | 否 | 是 | 预览的屏幕形状是否为圆形，默认为false。true为圆形，false为非圆形。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例分别使用了不传参@Preview和传参的@Preview。

```
1. @Entry
2. @Preview
3. @Component
4. struct Index {
5. @State message: string = 'default Preview';

7. build() {
8. RelativeContainer() {
9. Text(this.message)
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. }
13. .height('100%')
14. .width('100%')
15. }
16. }

18. @Preview({
19. title: 'PreviewParams',
20. width: 540,
21. height: 1170
22. })
23. @Component
24. struct Test {
25. @State message: string = 'PreviewParams';

27. build() {
28. RelativeContainer() {
29. Text(this.message)
30. .fontSize(40)
31. .fontWeight(FontWeight.Bold)
32. }
33. .height('100%')
34. .width('100%')
35. }
36. }
```
