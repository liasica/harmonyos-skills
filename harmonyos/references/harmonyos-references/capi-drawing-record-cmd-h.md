---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-record-cmd-h
title: drawing_record_cmd.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_record_cmd.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8547632a3a5170378de33ecbc565928fe22bde567f7467b4d0d2bf334210fdb9
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与录制指令对象相关的功能函数。

**引用文件：** <native\_drawing/drawing\_record\_cmd.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_RecordCmdUtils\* OH\_Drawing\_RecordCmdUtilsCreate(void)](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilscreate) | 创建一个录制指令工具对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsDestroy(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils)](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsdestroy) | 销毁一个录制指令工具对象，并回收该对象占用的内存。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsBeginRecording(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils,int32\_t width, int32\_t height, OH\_Drawing\_Canvas\*\* canvas)](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsbeginrecording) | 开始录制。此接口需要与[OH\_Drawing\_RecordCmdUtilsFinishRecording](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsfinishrecording)接口成对使用。  指令录制工具生成录制类型的画布对象，可调用drawing的绘制接口，记录接下来所有的绘制指令。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdUtilsFinishRecording(OH\_Drawing\_RecordCmdUtils\* recordCmdUtils,OH\_Drawing\_RecordCmd\*\* recordCmd)](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsfinishrecording) | 结束录制。在调用此接口前，需要先调用[OH\_Drawing\_RecordCmdUtilsBeginRecording](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsbeginrecording)接口。  指令录制工具结束录制指令，将录制类型画布对象记录的绘制指令存入生成的录制指令对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_RecordCmdDestroy(OH\_Drawing\_RecordCmd\* recordCmd)](capi-drawing-record-cmd-h.md#oh_drawing_recordcmddestroy) | 销毁录制指令对象，并回收该对象占用的内存。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_RecordCmdUtilsCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_RecordCmdUtils* OH_Drawing_RecordCmdUtilsCreate(void)
```

**描述**

创建一个录制指令工具对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md)\* | 返回用于录制指令的工具对象。 |

### OH\_Drawing\_RecordCmdUtilsDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsDestroy(OH_Drawing_RecordCmdUtils* recordCmdUtils)
```

**描述**

销毁一个录制指令工具对象，并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md)\* recordCmdUtils | 指向录制指令工具对象[OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数recordCmdUtils为空。 |

### OH\_Drawing\_RecordCmdUtilsBeginRecording()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsBeginRecording(OH_Drawing_RecordCmdUtils* recordCmdUtils,int32_t width, int32_t height, OH_Drawing_Canvas** canvas)
```

**描述**

开始录制。此接口需要与[OH\_Drawing\_RecordCmdUtilsFinishRecording](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsfinishrecording)接口成对使用。

指令录制工具生成录制类型的画布对象，可调用drawing的绘制接口，记录接下来所有的绘制指令。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md)\* recordCmdUtils | 指向录制工具对象[OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md)的指针。 |
| int32\_t width | 画布的宽度。 |
| int32\_t height | 画布的高度。 |
| [OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)\*\* canvas | 指向画布对象[OH\_Drawing\_Canvas](capi-drawing-oh-drawing-canvas.md)的二级指针，作为出参，开发者无需释放。  该画布对象不支持嵌套调用[OH\_Drawing\_CanvasDrawRecordCmd](capi-drawing-canvas-h.md#oh_drawing_canvasdrawrecordcmd)接口。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS, 表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER, 表示参数recordCmdUtils或者canvas为空。  当width和height小于等于0的时，也会返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。  返回OH\_DRAWING\_ERROR\_ALLOCATION\_FAILED，表示系统内存不足。 |

### OH\_Drawing\_RecordCmdUtilsFinishRecording()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsFinishRecording(OH_Drawing_RecordCmdUtils* recordCmdUtils,OH_Drawing_RecordCmd** recordCmd)
```

**描述**

结束录制。在调用此接口前，需要先调用[OH\_Drawing\_RecordCmdUtilsBeginRecording](capi-drawing-record-cmd-h.md#oh_drawing_recordcmdutilsbeginrecording)接口。

指令录制工具结束录制指令，将录制类型画布对象记录的绘制指令存入生成的录制指令对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md)\* recordCmdUtils | 指向录制指令工具对象[OH\_Drawing\_RecordCmdUtils](capi-drawing-oh-drawing-recordcmdutils.md)的指针。 |
| [OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md)\*\* recordCmd | 指向录制指令对象[OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md)的二级指针，作为出参，开发者调用[OH\_Drawing\_CanvasDrawRecordCmd](capi-drawing-canvas-h.md#oh_drawing_canvasdrawrecordcmd)接口绘制该对象。需要调用[OH\_Drawing\_RecordCmdDestroy](capi-drawing-record-cmd-h.md#oh_drawing_recordcmddestroy)接口释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数recordCmdUtils或者recordCmd为空。  返回OH\_DRAWING\_ERROR\_ALLOCATION\_FAILED，表示系统内存不足。 |

### OH\_Drawing\_RecordCmdDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_RecordCmdDestroy(OH_Drawing_RecordCmd* recordCmd)
```

**描述**

销毁录制指令对象，并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md)\* recordCmd | 指向对象[OH\_Drawing\_RecordCmd](capi-drawing-oh-drawing-recordcmd.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数recordCmd为空。 |
