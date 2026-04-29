---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-hyperlink
title: Hyperlink
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > Hyperlink
category: harmonyos-references
scraped_at: 2026-04-29T13:52:13+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:b15b81b6d5cb08a2920f7133e8289e03168056566fd0b9e1927cf278e26fd3cf
---

超链接组件，组件宽高范围内点击实现跳转。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅支持与系统浏览器配合使用。

## 需要权限

PhonePC/2in1TabletTVWearable

跳转的目标应用使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含[Image](ts-basic-components-image.md)子组件。

## 接口

PhonePC/2in1TabletTVWearable

Hyperlink(address: string | Resource, content?: string | Resource)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | [Resource](ts-types.md#resource) | 是 | Hyperlink组件跳转的网页。 |
| content | string | [Resource](ts-types.md#resource) | 否 | Hyperlink组件中超链接显示文本。  默认值：''。若不传该参数且组件内无子组件时，默认显示address参数值链接地址。  **说明：**  组件内有子组件时，不显示超链接文本。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

PhonePC/2in1TabletTVWearable

color(value: Color | number | string | Resource)

设置超链接文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Color](ts-appendix-enums.md#color) | number | string | [Resource](ts-types.md#resource) | 是 | 超链接文本的颜色。  phone默认值为'#ff007dff'，wearable设备默认值'#1F71FF'，tv设备默认值为'#266EFB'，均显示为蓝色。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例展示了超链接图片和文本跳转的效果。

```
1. @Entry
2. @Component
3. struct HyperlinkExample {
4. build() {
5. Column() {
6. Column() {
7. Hyperlink('https://example.com/') {
8. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.bg'))
10. .width(200)
11. .height(100)
12. }
13. }

15. Column() {
16. Hyperlink('https://example.com/', 'Go to the developer website') {
17. }
18. .color(Color.Blue)
19. }
20. }.width('100%').height('100%').justifyContent(FlexAlign.Center)
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/X0ma9TnIRFaMBN70W-ZwRw/zh-cn_image_0000002589326209.png?HW-CC-KV=V1&HW-CC-Date=20260429T055209Z&HW-CC-Expire=86400&HW-CC-Sign=1C26F5DCFB18E55A51CB965F0247778E8C7E91B27E9C3410302570C9DBB97212)
