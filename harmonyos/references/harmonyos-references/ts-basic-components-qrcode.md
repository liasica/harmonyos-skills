---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-qrcode
title: QRCode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > QRCode
category: harmonyos-references
scraped_at: 2026-04-28T08:02:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cc527e9ca627831b009fe6bdcea9ef4dd83c6bb3b39bd2b694b2098379a93c9a
---

用于显示单个二维码的组件。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 二维码组件的像素点数量与内容有关，组件尺寸过小可能导致内容无法展示，此时需要适当调整组件尺寸。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

QRCode(value: ResourceStr)

创建二维码组件，通过扫描组件显示的二维码图案可以获取二维码中包含的字符串信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 二维码内容字符串。最大支持512个字符，若超出，则截取前512个字符。  从API version 20开始，支持Resource类型。  **说明：**  设置为null时与设置字符串“null”效果一致；设置为undefined时与设置字符串“undefined”效果一致；当传入空字符串时，将生成无效二维码。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

PhonePC/2in1TabletTVWearable

color(value: ResourceColor)

设置二维码颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 二维码颜色。默认值：'#ff000000'，且不跟随系统深浅色模式切换而修改。 |

### backgroundColor

PhonePC/2in1TabletTVWearable

backgroundColor(value: ResourceColor)

设置二维码背景颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 二维码背景颜色。  默认值：Color.White  从API version 11开始，默认值改为'#ffffffff'，且不跟随系统深浅色模式切换而修改。 |

### contentOpacity11+

PhonePC/2in1TabletTVWearable

contentOpacity(value: number | Resource)

设置二维码内容颜色的不透明度。不透明度最小值为0，最大值为1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 二维码内容颜色的不透明度。  默认值：1  取值范围：[0, 1]，超出取值范围按默认值处理。 |

## 事件

PhonePC/2in1TabletTVWearable

通用事件支持[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)和[挂载卸载事件](ts-universal-events-show-hide.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置颜色、背景颜色、不透明度）

该示例展示了QRCode组件的基本使用方法，通过[color](ts-basic-components-qrcode.md#color)属性设置二维码颜色、[backgroundColor](ts-basic-components-qrcode.md#backgroundcolor)属性设置二维码背景颜色、[contentOpacity](ts-basic-components-qrcode.md#contentopacity11)属性设置二维码不透明度。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct QRCodeExample {
5. private value: string = 'hello world';

7. build() {
8. Column({ space: 5 }) {
9. Text('normal').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
10. QRCode(this.value).width(140).height(140)

12. // 设置二维码颜色
13. Text('color').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
14. QRCode(this.value).color(0xF7CE00).width(140).height(140)

16. // 设置二维码背景色
17. Text('backgroundColor').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
18. QRCode(this.value).width(140).height(140).backgroundColor(Color.Orange)

20. // 设置二维码不透明度
21. Text('contentOpacity').fontSize(9).width('90%').fontColor(0xCCCCCC).fontSize(30)
22. QRCode(this.value).width(140).height(140).color(Color.Black).contentOpacity(0.1)
23. }.width('100%').margin({ top: 5 })
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/3V8rOokPRLyN-KbBNjz3kA/zh-cn_image_0000002552800268.png?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=7501BDCDC007A5CB727430C96588748EE7137146146730D93302BC7B7BC5E19C)

### 示例2（设置背景颜色为透明）

该示例通过[backgroundColor](ts-basic-components-qrcode.md#backgroundcolor)属性设置二维码背景颜色为透明，从而实现二维码内容与背景融合。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct QRCodeExample {
5. private value: string = 'hello world';

7. build() {
8. Column({ space: 5 }) {
9. RelativeContainer() {
10. // $r('app.media.ocean')需要替换为开发者所需的图像资源文件。
11. Image($r('app.media.ocean'))
12. // 设置二维码背景色为透明
13. QRCode(this.value).width(200).height(200).backgroundColor('#00ffffff')
14. }.width(200).height(200)
15. }.width('100%').margin({ top: 5 })
16. }
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/4_G8o2-qRkOCTeea0fCqEQ/zh-cn_image_0000002583439963.png?HW-CC-KV=V1&HW-CC-Date=20260428T000202Z&HW-CC-Expire=86400&HW-CC-Sign=F4473137AC8DE966BA51F634AF1604F7817C4A8FAEDD0DEF56E7C2CAC3690C9E)
