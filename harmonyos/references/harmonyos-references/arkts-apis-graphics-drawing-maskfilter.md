---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-maskfilter
title: Class (MaskFilter)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (MaskFilter)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b743263d60c32cda0b88cc396cf6a038df8b34028ee578725e62258762c72b98
---

蒙版滤镜对象。

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

## createBlurMaskFilter12+

PhonePC/2in1TabletTVWearable

static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter

创建具有模糊效果的蒙版滤镜。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurType | [BlurType](arkts-apis-graphics-drawing-e.md#blurtype12) | 是 | 模糊类型。 |
| sigma | number | 是 | 高斯模糊的标准偏差，必须为大于0的浮点数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MaskFilter](arkts-apis-graphics-drawing-maskfilter.md) | 返回创建的蒙版滤镜对象。 |

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
6. const canvas = context.canvas;
7. let maskFilter = drawing.MaskFilter.createBlurMaskFilter(drawing.BlurType.OUTER, 10);
8. }
9. }
```
