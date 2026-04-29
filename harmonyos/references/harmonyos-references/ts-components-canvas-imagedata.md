---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata
title: ImageData
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > ImageData
category: harmonyos-references
scraped_at: 2026-04-29T13:52:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:39abac27f4097371778b6038d17ade78109e9d95b852044b191a4b5744dc6126
---

ImageData对象可以存储canvas渲染的像素数据。

说明

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

创建ImageData时，宽高不超过16384px，最大面积不超过16000px\*16000px，超过最大面积则无法正常绘制。当创建面积超过536870911px时，返回值的width和height均为0px，data为undefined。

## constructor

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, data?: Uint8ClampedArray)

创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 矩形区域宽度，默认单位为vp。  异常值NaN和Infinity按0处理。 |
| height | number | 是 | 矩形区域高度，默认单位为vp。  异常值NaN和Infinity按0处理。 |
| data | [Uint8ClampedArray](arkts-apis-arkts-collections-uint8clampedarray.md) | 否 | 一维数组，保存了相应的颜色数据，数据值范围为0到255。  传入异常值undefined时，data为undefined。  默认值：值全为0的一维数组 |

## constructor12+

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, data?: Uint8ClampedArray, unit?: LengthMetricsUnit)

创建宽为width，高为height，像素为data的ImageData，如果data未定义，则填充值全为0的一维数组，支持使用unit配置ImageData对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 矩形区域宽度，默认单位为vp。  异常值NaN和Infinity按0处理。 |
| height | number | 是 | 矩形区域高度，默认单位为vp。  异常值NaN和Infinity按0处理。 |
| data | [Uint8ClampedArray](arkts-apis-arkts-collections-uint8clampedarray.md) | 否 | 一维数组，保存了相应的颜色数据，数据值范围为0到255。  传入异常值undefined时，data为undefined。  默认值：值全为0的一维数组 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 否 | 用来配置ImageData对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值undefined、NaN和Infinity按默认值处理。  默认值：DEFAULT |

## 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | 矩形区域实际像素宽度。  单位为px。 |
| height | number | 是 | 否 | 矩形区域实际像素高度。  单位为px。 |
| data | [Uint8ClampedArray](arkts-apis-arkts-collections-uint8clampedarray.md) | 是 | 否 | 一维数组，保存了相应的颜色数据，数据值范围为0到255。 |

说明

可使用[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)接口进行单位转换。

## 示例

PhonePC/2in1TabletTVWearable

使用getImageData接口获得一个ImageData对象。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Translate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/1234.png"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/1234.png");

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. this.context.drawImage(this.img, 0, 0, 130, 130)
18. let imageData = this.context.getImageData(50, 50, 130, 130)
19. this.context.putImageData(imageData, 150, 150)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ulzIKuyLRpeUCpHh8NZvkQ/zh-cn_image_0000002558606826.png?HW-CC-KV=V1&HW-CC-Date=20260429T055229Z&HW-CC-Expire=86400&HW-CC-Sign=8909D7FC14C8355E0800F8166EDC58679B3E817D961BF222604826ADC86C7213)
