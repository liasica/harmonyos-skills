---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-b123sp16
title: UX样式或效果的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > OS平台行为变更说明 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-29T13:23:38+08:00
doc_updated_at: 2026-01-16
content_hash: sha256:56d5ef40afbc5b322018b02ebf8386020c577ada6b75d39058f2d9dde789e49e
---

## borderImage的outset属性按照实际的延伸距离来绘制边框向外扩展的效果

**变更原因**

borderImage中的边框外延距离（outset属性）在无需绘制的区域不会被绘制，这与预期行为不符。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：borderImage中的边框外延距离（outset属性）在无需绘制的区域不会被绘制。

变更后：borderImage中的边框外延距离（outset属性）按照实际延伸距离进行绘制。

**起始API Level**

9

**变更的接口/组件**

[borderImage](../harmonyos-references/ts-universal-attributes-border-image.md#borderimage)中的outset属性。

**适配指导**

默认效果变更，应注意变更后的默认效果是否符合开发者预期，如不符合则应自定义修改效果控制变量以达到预期。

## Canvas使用toDataURL接口生成图片，对于带有透明度的图片，创建为“image/png”或“image/webp”格式时，其效果可能会发生变更

**变更原因**

变更前效果未达到预期。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

变更前：Canvas使用toDataURL接口生成图片，对于带有透明度的图片，创建为“image/png”或“image/webp”格式时，带透明度部分会与黑色背景混合，效果与原图有色差。

变更后：Canvas使用toDataURL接口生成图片，对于带有透明度的图片，创建为“image/png”或“image/webp”格式时，变更为与原图一致。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

8

**变更的接口/组件**

Canvas组件的toDataURL接口。

**适配指导**

默认效果变更，但开发者需审视此变更是否对自身相关业务代码逻辑产生影响，若有影响需根据自身业务代码进行对应适配。示例代码详情请看[toDataURL接口示例](../harmonyos-references/ts-canvasrenderingcontext2d.md#todataurl)。

## bindSheet半模态面板视觉样式增加

**变更原因**

增强视觉效果。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

设备宽度在600-840vp间时，SheetOptions中的preferType设置为SheetType.POPUP，原先显示居中弹窗样式，现在显示跟手弹窗样式。

API version 14及以后，设备宽度在600-840vp间时，默认显示居中弹窗样式，增加跟手弹窗样式。

变更前：设备宽度在600-840vp间时，SheetOptions中的preferType设置为SheetType.POPUP，实际显示居中弹窗样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/przeKRN_SqSM3Rp8CqqN-w/zh-cn_image_0000002334372189.png?HW-CC-KV=V1&HW-CC-Date=20260429T052337Z&HW-CC-Expire=86400&HW-CC-Sign=BBA9AB1B73C8160D189F5E6178AD85CF577B381C3B7098477F213CDE496A7C0C)

变更后：设备宽度在600-840vp间时，SheetOptions中的preferType设置为SheetType.POPUP，实际显示跟手弹窗样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/qlA2LDb0QOOfiT1yOK8qAQ/zh-cn_image_0000002334332009.png?HW-CC-KV=V1&HW-CC-Date=20260429T052337Z&HW-CC-Expire=86400&HW-CC-Sign=123E6E4A92222D33B36CE58F24D585CF085B3297C737049EB541717E4A774CAA)

**起始API Level**

11

**变更的接口/组件**

bindSheet半模态面板。

**适配指导**

设备宽度在600-840vp间时，如需显示跟手弹窗样式，则SheetOptions中的preferType设置为SheetType.POPUP；如需显示底部弹窗样式，则preferType设置为SheetType.BOTTOM；如需显示居中弹窗样式，则preferType设置为SheetType.CENTER或者不设置。

## bindSheet半模态面板标题与关闭按钮布局变更

**变更原因**

增强视觉效果。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.2(14)时生效。

API version 14及以后，关闭按钮不显示时，关闭按钮区域放开限制给标题栏区域布局。

变更前：关闭按钮不显示时，关闭按钮区域未放开限制给标题栏区域布局。

变更后：关闭按钮不显示时，关闭按钮区域放开限制给标题栏区域布局。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

11

**变更的接口/组件**

showClose
