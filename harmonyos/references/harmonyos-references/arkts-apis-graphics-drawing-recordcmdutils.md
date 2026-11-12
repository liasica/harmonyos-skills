---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-recordcmdutils
title: Class (RecordCmdUtils)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (RecordCmdUtils)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:56+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:78c5d4b79533d427e5fefbfd7ed1acad655def19077b438b00a3439ff2068774
---

指令录制工具对象，用于生成可回放的录制绘制指令。通过[beginRecording](arkts-apis-graphics-drawing-recordcmdutils.md#beginrecording)获取录制类型的画布，在该画布上调用的绘制接口会被录制为指令；录制完成后通过[finishRecording](arkts-apis-graphics-drawing-recordcmdutils.md#finishrecording)生成[RecordCmd](arkts-apis-graphics-drawing-i.md#recordcmd)对象，再调用[Canvas.drawRecordCmd](arkts-apis-graphics-drawing-canvas.md#drawrecordcmd)即可回放录制的绘制指令。

**说明** 

* 起始版本： 26.0.1。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

```ts
import { drawing } from '@kit.ArkGraphics2D';
```

## beginRecording

beginRecording(width: number, height: number): Canvas

获取用于录制绘制指令的画布对象，之后在返回的画布上调用的绘制接口都会被录制为绘制指令。返回的画布对象仅在录制期间有效，录制结束后需调用[finishRecording](arkts-apis-graphics-drawing-recordcmdutils.md#finishrecording)结束录制。

**系统能力：** SystemCapability.Graphics.Drawing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 录制画布的宽度。单位为物理像素px，取值范围为int范围内的正整数。输入浮点数，按照向下取整处理。 |
| height | number | 是 | 录制画布的高度。单位为物理像素px，取值范围为int范围内的正整数。输入浮点数，按照向下取整处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Canvas](arkts-apis-graphics-drawing-canvas.md) | 返回用于录制绘制指令的画布对象。在该画布上调用的绘制接口都会被录制为绘制指令。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error. Possible causes: Incorrect parameter range. |

**示例：**

```ts
import { RenderNode, DrawContext } from '@kit.ArkUI';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const recordCmdUtils = new drawing.RecordCmdUtils();
    const recordCanvas = recordCmdUtils.beginRecording(200, 200);
    const pen = new drawing.Pen();
    pen.setStrokeWidth(5);
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    recordCanvas.attachPen(pen);
    recordCanvas.drawRect({ left : 0, right : 100, top : 0, bottom : 100 });
    recordCanvas.detachPen();
    const recordCmd = recordCmdUtils.finishRecording();
    canvas.drawRecordCmd(recordCmd);
  }
}
```

## finishRecording

finishRecording(): RecordCmd

结束录制，返回录制的绘制指令对象[RecordCmd](arkts-apis-graphics-drawing-i.md#recordcmd)。调用本接口前需先调用[beginRecording](arkts-apis-graphics-drawing-recordcmdutils.md#beginrecording)开始录制，录制期间在画布上记录的所有绘制指令会被封装到返回的RecordCmd对象中。

**系统能力：** SystemCapability.Graphics.Drawing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RecordCmd](arkts-apis-graphics-drawing-i.md#recordcmd) | 返回已录制的绘制指令对象，可用于[Canvas.drawRecordCmd](arkts-apis-graphics-drawing-canvas.md#drawrecordcmd)回放绘制指令。 |

**示例：**

```ts
import { RenderNode, DrawContext } from '@kit.ArkUI';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    const canvas = context.canvas;
    const recordCmdUtils = new drawing.RecordCmdUtils();
    const recordCanvas = recordCmdUtils.beginRecording(200, 200);
    const pen = new drawing.Pen();
    pen.setStrokeWidth(5);
    pen.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
    recordCanvas.attachPen(pen);
    recordCanvas.drawRect({ left : 0, right : 100, top : 0, bottom : 100 });
    recordCanvas.detachPen();
    const recordCmd = recordCmdUtils.finishRecording();
    canvas.drawRecordCmd(recordCmd);
  }
}
```

## getHeight

getHeight(): number

获取录制画布的高度。

**系统能力：** SystemCapability.Graphics.Drawing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回录制画布的高度，单位为物理像素px，与开始录制时通过[beginRecording](arkts-apis-graphics-drawing-recordcmdutils.md#beginrecording)传入的height值相同。 |

**示例：**

```ts
const recordCmdUtils = new drawing.RecordCmdUtils();
recordCmdUtils.beginRecording(200, 100);
let height = recordCmdUtils.getHeight();
recordCmdUtils.finishRecording();
```

## getWidth

getWidth(): number

获取录制画布的宽度。

**系统能力：** SystemCapability.Graphics.Drawing

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回录制画布的宽度，单位为物理像素px，与开始录制时通过[beginRecording](arkts-apis-graphics-drawing-recordcmdutils.md#beginrecording)传入的width值相同。 |

**示例：**

```ts
const recordCmdUtils = new drawing.RecordCmdUtils();
recordCmdUtils.beginRecording(200, 100);
let width = recordCmdUtils.getWidth();
recordCmdUtils.finishRecording();
```
