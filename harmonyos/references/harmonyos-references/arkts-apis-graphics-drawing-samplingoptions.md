---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-samplingoptions
title: Class (SamplingOptions)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (SamplingOptions)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cdfee53c77f4f7bb7d738692cee1fe7a137d1eb5f468a021393dc590ca3127ca
---

采样选项对象。

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

## constructor12+

PhonePC/2in1TabletTVWearable

constructor()

构造一个新的采样选项对象，[FilterMode](arkts-apis-graphics-drawing-e.md#filtermode12)的默认值为FILTER\_MODE\_NEAREST。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. const pen = new drawing.Pen();
8. let samplingOptions = new drawing.SamplingOptions();
9. }
10. }
```

## constructor12+

PhonePC/2in1TabletTVWearable

constructor(filterMode: FilterMode)

构造一个新的采样选项对象。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filterMode | [FilterMode](arkts-apis-graphics-drawing-e.md#filtermode12) | 是 | 过滤模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. import { RenderNode } from '@kit.ArkUI';
2. import { common2D, drawing } from '@kit.ArkGraphics2D';

4. class DrawingRenderNode extends RenderNode {
5. draw(context : DrawContext) {
6. const canvas = context.canvas;
7. let samplingOptions = new drawing.SamplingOptions(drawing.FilterMode.FILTER_MODE_NEAREST);
8. }
9. }
```
