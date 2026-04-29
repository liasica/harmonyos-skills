---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-lattice
title: Class (Lattice)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (Lattice)
category: harmonyos-references
scraped_at: 2026-04-29T14:05:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7291f527bfbab598f3531a83aec8a541c87a8bef2d4f7f4af503a6539236781d
---

矩形网格对象。该对象用于将图片按照矩形网格进行划分。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## createImageLattice12+

PhonePC/2in1TabletTVWearable

static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制。如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。其余网格将进行缩放，来适应剩余的空间。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xDivs | Array<number> | 是 | 用于划分图像的X坐标值数组。该参数为整数。 |
| yDivs | Array<number> | 是 | 用于划分图像的Y坐标值数组。该参数为整数。 |
| fXCount | number | 是 | X坐标值数组的大小。基于功能和性能的考虑，取值范围为[0, 5]。 |
| fYCount | number | 是 | Y坐标值数组的大小。基于功能和性能的考虑，取值范围为[0, 5]。 |
| fBounds | [common2D.Rect](js-apis-graphics-common2d.md#rect) | null | 否 | 可选，要绘制的原始边界矩形，矩形参数须为整数，默认为原始图像矩形大小（若矩形参数为小数，会直接舍弃小数部分，转为整数）。 |
| fRectTypes | Array<[RectType](arkts-apis-graphics-drawing-e.md#recttype12)> | null | 否 | 可选，填充网格类型的数组，默认为空。如果设置，大小必须为(fXCount + 1) \* (fYCount + 1)。 |
| fColors | Array<[common2D.Color](js-apis-graphics-common2d.md#color)> | null | 否 | 可选，填充网格的颜色数组，默认为空。如果设置，大小必须为(fXCount + 1) \* (fYCount + 1)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Lattice](arkts-apis-graphics-drawing-lattice.md) | 返回创建的矩形网格对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. let xDivs : Array<number> = [1, 2, 4];
7. let yDivs : Array<number> = [1, 2, 4];
8. let lattice = drawing.Lattice.createImageLattice(xDivs, yDivs, 3, 3); // 划分(3+1)*(3+1)的网格，下图蓝色填充矩形为固定网格
9. }
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/NbMVN0OkRA6yaDH53HPtcQ/zh-cn_image_0000002589247197.png?HW-CC-KV=V1&HW-CC-Date=20260429T060514Z&HW-CC-Expire=86400&HW-CC-Sign=9B14EAAC165AA7BC500AC42CA6D996D672D9DEF24DFDE5158528022AC32054C0)

## createImageLattice18+

PhonePC/2in1TabletTVWearable

static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number, fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制。如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。其余网格将进行缩放，来适应剩余的空间。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| xDivs | Array<number> | 是 | 用于划分图像的X坐标值数组。该参数为整数。 |
| yDivs | Array<number> | 是 | 用于划分图像的Y坐标值数组。该参数为整数。 |
| fXCount | number | 是 | X坐标值数组的大小。基于功能和性能的考虑，取值范围为[0, 5]。 |
| fYCount | number | 是 | Y坐标值数组的大小。基于功能和性能的考虑，取值范围为[0, 5]。 |
| fBounds | [common2D.Rect](js-apis-graphics-common2d.md#rect) | null | 否 | 可选，要绘制的原始边界矩形，矩形参数须为整数，默认为原始图像矩形大小（若矩形参数为小数，会直接舍弃小数部分，转为整数）。 |
| fRectTypes | Array<[RectType](arkts-apis-graphics-drawing-e.md#recttype12)> | null | 否 | 可选，填充网格类型的数组，默认为空。如果设置，大小必须为(fXCount + 1) \* (fYCount + 1)。 |
| fColors | Array<number> | null | 否 | 可选，填充网格的颜色数组，颜色用16进制ARGB格式的32位无符号整数表示，参数默认为空。如果设置，大小必须为(fXCount + 1) \* (fYCount + 1)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Lattice](arkts-apis-graphics-drawing-lattice.md) | 返回创建的矩形网格对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types;3.Parameter verification failed. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. let xDivs : Array<number> = [1, 2, 4];
7. let yDivs : Array<number> = [1, 2, 4];
8. let colorArray :Array<number>=[0xffffffff,0x44444444,0x99999999,0xffffffff,0x44444444,0x99999999,0xffffffff,0x44444444,0x99999999,0x44444444,0x99999999,0xffffffff,0x44444444,0x99999999,0xffffffff,0x44444444];
9. let lattice = drawing.Lattice.createImageLattice(xDivs, yDivs, 3, 3,null,null,colorArray);
10. }
11. }
```
