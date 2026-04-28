---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvasgradient
title: CanvasGradient
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > CanvasGradient
category: harmonyos-references
scraped_at: 2026-04-28T08:02:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:13861809e5b868ba4b3ad5afbc9e68824662df0af097f43fed42fe4519397ef8
---

渐变对象。

说明

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## addColorStop

PhonePC/2in1TabletTVWearable

addColorStop(offset: number, color: string): void

设置渐变断点值，包括偏移和颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 设置渐变点距离起点的位置占总体长度的比例，范围为[0, 1]。  设置offset<0或offset>1无渐变效果。  异常值undefined和null按无效值处理，忽略本次断点值。NaN会导致CanvasGradient异常，Infinity会导致整个CanvasGradient不生效。 |
| color | string | 是 | 设置渐变的颜色。颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中string类型说明。  未按格式设置颜色无渐变效果。 |

**示例：**

通过addColorStop设置渐变断点值，包括偏移和颜色。支持设置rgb或者argb格式颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct AddColorStop {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. let grad = this.context.createLinearGradient(50, 0, 300, 100)
16. grad.addColorStop(0.0, 'rgb(39,135,217)')
17. grad.addColorStop(0.5, 'rgb(255,238,240)')
18. grad.addColorStop(1.0, 'rgb(23,169,141)')
19. this.context.fillStyle = grad
20. this.context.fillRect(0, 0, 400, 400)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/AWPPj6yzSpC5KIGF8ymwQQ/zh-cn_image_0000002583439973.png?HW-CC-KV=V1&HW-CC-Date=20260428T000204Z&HW-CC-Expire=86400&HW-CC-Sign=7AF8B77248B2F00058F097AED4C5CFCC2B765A869ADFB2B16F8FD61612A266AE)

## addColorStop20+

PhonePC/2in1TabletTVWearable

addColorStop(offset: number, color: string | ColorMetrics): void

设置渐变断点值，包括偏移和颜色。支持设置rgb或者argb格式颜色。支持通过传入[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)类型设置P3色域颜色值，可在支持高色域的设备上获得更丰富的色彩表现。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 设置渐变点距离起点的位置占总体长度的比例，范围为[0, 1]。  设置offset<0或offset>1无渐变效果。  异常值undefined和null按无效值处理，不设置本次断点值，NaN会导致CanvasGradient异常，Infinity会导致整个CanvasGradient不生效。 |
| color | string | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 是 | 设置渐变填充的颜色。  可以使用[colorWithSpace](js-apis-arkui-graphics.md#colorwithspace20)方法构造指定色域属性[ColorSpace](ts-appendix-enums.md#colorspace20)为SRGB或DISPLAY\_P3的颜色。每个渐变ColorMetrics的色域属性应当统一，设置不同色域的属性时将抛出异常，错误码：103701。  设置null和undefined无效，忽略本次断点值。 |

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](errorcode-canvas.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 103701 | The color's ColorSpace is not the same as the last color's. |

说明

仅[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)对象的[fillStyle](ts-canvasrenderingcontext2d.md#fillstyle)和[strokeStyle](ts-canvasrenderingcontext2d.md#strokestyle)属性支持设置P3广色域的CanvasGradient对象，且需要将Canvas组件所在窗口的色域模式通过[setWindowColorSpace](arkts-apis-window-window.md#setwindowcolorspace9)方法设置为广色域模式WIDE\_GAMUT。

**示例：**

通过addColorStop设置指定色域的渐变断点值，包括偏移和颜色。设置窗口色域模式为广色域参照方法[setWindowColorSpace](arkts-apis-window-window.md#setwindowcolorspace9)。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { ColorMetrics } from '@kit.ArkUI'

5. @Entry
6. @Component
7. struct AddColorStop {
8. private settings: RenderingContextSettings = new RenderingContextSettings(true);
9. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .onReady(() => {
17. // 设置fillStyle为SRGB色域效果的gradient
18. let gradSRGB = this.context.createLinearGradient(85, 10, 160, 110)
19. // 使用try catch对可能出现的异常进行捕获
20. try {
21. gradSRGB.addColorStop(0.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 0.0, 0.0, 1.0))
22. gradSRGB.addColorStop(0.5, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 1.0, 1.0, 1.0, 1.0))
23. gradSRGB.addColorStop(1.0, ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.0, 1.0, 0.0, 1.0))
24. } catch (error) {
25. let e: BusinessError = error as BusinessError;
26. console.error(`Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
27. }
28. this.context.fillStyle = gradSRGB
29. this.context.fillRect(10, 10, 150, 150)

31. // 设置fillStyle为DISPLAY_P3色域效果的gradient
32. let gradP3 = this.context.createLinearGradient(245, 10, 320, 110)
33. // 使用try catch对可能出现的异常进行捕获
34. try {
35. gradP3.addColorStop(0.0, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1.0, 0.0, 0.0, 1.0))
36. gradP3.addColorStop(0.5, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 1.0, 1.0, 1.0, 1.0))
37. gradP3.addColorStop(1.0, ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.0, 1.0, 0.0, 1.0))
38. } catch (error) {
39. let e: BusinessError = error as BusinessError;
40. console.error(`Failed to addColorStop. Code: ${e.code}, message: ${e.message}`);
41. }
42. this.context.fillStyle = gradP3
43. this.context.fillRect(170, 10, 150, 150)
44. })
45. }
46. .width('100%')
47. .height('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/NtBvpKY_RECVqHNF2wqqMw/zh-cn_image_0000002552959928.png?HW-CC-KV=V1&HW-CC-Date=20260428T000204Z&HW-CC-Expire=86400&HW-CC-Sign=E911DDBB03D9103CC1FFE7734BE4671D7633538BF9779F89ED56E3A554D3E4A0)
