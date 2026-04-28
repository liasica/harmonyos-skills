---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h
title: drawing_error_code.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5cf8ba233c83b9c085ddfb09a7c08c4bd7fcdfaca01dc3c44accd1fbef691999
---

## 概述

PhonePC/2in1TabletTVWearable

声明与绘图模块中的错误码相关的函数。

**引用文件：** <native\_drawing/drawing\_error\_code.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | OH\_Drawing\_ErrorCode | 枚举本模块可能产生的错误码。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_ErrorCodeGet()](capi-drawing-error-code-h.md#oh_drawing_errorcodeget) | 获取本模块的错误码。 |
| [void OH\_Drawing\_ErrorCodeReset(void)](capi-drawing-error-code-h.md#oh_drawing_errorcodereset) | 将本模块的错误码重置为OH\_DRAWING\_SUCCESS。  通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)获取的本模块错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，但是不会在执行成功后被重置为OH\_DRAWING\_SUCCESS。  调用本接口可将错误码重置为OH\_DRAWING\_SUCCESS，避免多个接口间互相干扰，方便开发者调试。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum OH_Drawing_ErrorCode
```

**描述**

枚举本模块可能产生的错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_DRAWING\_SUCCESS = 0 | 操作成功完成。 |
| OH\_DRAWING\_ERROR\_NO\_PERMISSION = 201 | 权限校验失败。 |
| OH\_DRAWING\_ERROR\_INVALID\_PARAMETER = 401 | 无效的输入参数，如参数中传入了NULL。 |
| OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE = 26200001 | 输入参数不在有效的范围内。 |
| OH\_DRAWING\_ERROR\_ALLOCATION\_FAILED = 26200002 | 内存分配失败。  **起始版本：** 13 |
| OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH = 26200003 | 输入属性id无匹配的函数。  **起始版本：** 21 |
| OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER = 26200004 | 输入参数不正确，例如入参的指针为空。  **起始版本：** 22 |
| OH\_DRAWING\_ERROR\_FILE\_NOT\_FOUND = 26200005 | 文件未找到，指定的文件不存在或路径不正确。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_OPEN\_FILE\_FAILED = 26200006 | 打开文件失败，权限不足或I/O问题造成。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_FILE\_SEEK\_FAILED = 26200007 | 文件定位失败。系统无法重新定位文件读取指针。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_GET\_FILE\_SIZE\_FAILED = 26200008 | 获取文件大小失败，系统无法获取文件大小信息。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_READ\_FILE\_FAILED = 26200009 | 读取文件失败，文件无法完整读取或包含不可读数据。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_EMPTY\_FILE = 26200010 | 文件为空，指定的字体文件为空，不包含有效数据。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_FILE\_CORRUPTED = 26200011 | 文件损坏，文件内容无效或损坏，无法解析。  **起始版本：** 23 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_ErrorCodeGet()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_ErrorCodeGet()
```

**描述**

获取本模块的错误码。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 获取本模块的最近一次的错误码。当函数成功运行后，本函数返回的错误码不会被修改。 |

### OH\_Drawing\_ErrorCodeReset()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_ErrorCodeReset(void)
```

**描述**

将本模块的错误码重置为OH\_DRAWING\_SUCCESS。

通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)获取的本模块错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，但是不会在执行成功后被重置为OH\_DRAWING\_SUCCESS。

调用本接口可将错误码重置为OH\_DRAWING\_SUCCESS，避免多个接口间互相干扰，方便开发者调试。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18
