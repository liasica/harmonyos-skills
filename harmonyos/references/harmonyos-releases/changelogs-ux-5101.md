---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-5101
title: UX样式或效果的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > OS平台行为变更说明 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:00+08:00
doc_updated_at: 2026-02-14
content_hash: sha256:a533081ffdbbbaa1ed450d7dcbf12bbd9f0bfb2fa7374c168b8453d1ddb2a2af
---

## 按钮默认值变更为新增圆角矩形类型

**变更原因**

原有默认类型按钮是胶囊按钮，在适老化场景下字体过大，在多行等场景下胶囊按钮文字易超出其圆角范围。不符合简单易用及高端精致原则，因此新增圆角矩形类型按钮，默认值变为新增的圆角矩形类型。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

变更前：ButtonOptions中type的默认值为ButtonType.Capsule。

变更后：ButtonOptions中type的默认值为ButtonType.ROUNDED\_RECTANGLE。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/v6pIIMXmS6aMF2W8TiYl_Q/zh-cn_image_0000002295507629.png?HW-CC-KV=V1&HW-CC-Date=20260427T233459Z&HW-CC-Expire=86400&HW-CC-Sign=BAF7A725CD2270E438B49E16C0B86A95EA04CD035941C02BABAD892B1886F5D1 "点击放大")

**起始API Level**

9

**变更的接口/组件**

Button组件中ButtonOptions对象的type属性默认值。

**适配指导**

开发者在使用Button组件时，按钮的默认类型会从Capsule类型变更为ROUNDED\_RECTANGLE类型，两个类型对应的圆角大小存在差异，如果应用期望保持变更之前的圆角大小，需要手动添加type属性并指定为Capsule类型。

```
1. @Entry
2. @Component
3. struct ButtonExample {
4. build() {
5. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
6. Text('Capsule button with rounded corners by default.').fontSize(9).fontColor(0xCCCCCC)
7. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
8. Button('Capsule')
9. .type(ButtonType.Capsule)
10. .backgroundColor(0x317aff)
11. .height(60)
12. .controlSize(ControlSize.NORMAL)
13. .width(180)
14. }
15. Text('Rounded rectangle button with rounded corners by default.').fontSize(9).fontColor(0xCCCCCC)
16. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
17. Button('Rounded rectangle')
18. .type(ButtonType.ROUNDED_RECTANGLE)
19. .backgroundColor(0x317aff)
20. .controlSize(ControlSize.NORMAL)
21. .height(60)
22. .width(180)
23. }
24. }.height(400).padding({ left: 35, right: 35, top: 35 })
25. }
26. }
```

## 修复Popup高级组件宽度限制计算错误的问题

**变更原因**

目前宽度最大限制不符合ux规范，在手机屏幕场景下，会出现Popup高级组件无法撑满屏幕的情况，影响体验。

**变更影响**

此变更不涉及应用适配。

变更前：屏幕宽度小于400vp时，Popup高级组件最大宽度为当前屏幕宽度-80vp。

变更后：屏幕宽度小于400vp时，Popup高级组件最大宽度为当前屏幕宽度。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

11

**变更的接口/组件**

Popup高级组件。

**适配指导**

如果用户原来没有自定义Popup高级组件的宽度，且内容宽度大于320vp，变更前按320vp显示，变更后，Popup高级组件会变宽；如不符合预期，可以手动修改为想要的宽度。

## 半模态底部样式最大高度默认避让状态栏安全区

**变更原因**

UX规格变更。

半模态底部样式最大高度默认避让状态栏安全区。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

场景1：竖屏下，状态栏隐藏时，半模态底部样式最大高度也需要避让状态栏安全区。

* 变更前：状态栏隐藏时，半模态底部样式最大高度距离屏幕上边界8vp，未避让状态栏安全区。
* 变更后：API version 18及以后，状态栏隐藏时，半模态底部样式最大高度距离状态栏下边界8vp，避让状态栏安全区。该样式的最大高度为屏幕高度 - (窗口状态栏安全区高度 + 安全间距8vp)。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

场景2：横屏下，状态栏不隐藏时，半模态底部样式最大高度也需要避让状态栏安全区。

* 变更前：状态栏不隐藏时，半模态底部样式最大高度距离屏幕上边界8vp，未避让状态栏安全区，且与状态栏区域重合。
* 变更后：API version 18及以后，状态栏不隐藏时，半模态底部样式最大高度距离状态栏下边界8vp，避让状态栏安全区。该样式的最大高度为屏幕高度 - (窗口状态栏安全区高度 + 安全间距8vp)。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

11

**变更的接口/组件**

bindSheet的LARGE属性

**适配指导**

若开发者自定义的builder面板内容是固定高度，建议使用100%布局，变更后自定义的内容也可以自动撑满半模态面板。

若按变更前的最大高度规格限制的builder内容，需要变更为新规格计算。
