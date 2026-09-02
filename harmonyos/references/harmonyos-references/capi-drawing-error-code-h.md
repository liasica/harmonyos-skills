---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-error-code-h
title: drawing_error_code.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_error_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f3733813e98803b61c933defe50782103d3691d49b50c937af36bda1f860fdc
---

## 概述

声明与绘图模块中的错误码相关的函数。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_error\_code.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | OH\_Drawing\_ErrorCode | 枚举本模块可能产生的错误码。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_ErrorCodeGet()](capi-drawing-error-code-h.md#oh_drawing_errorcodeget) | 获取本模块最近一次的错误码。  本模块的错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，在执行成功后不会被重置为OH\_DRAWING\_SUCCESS。可通过[OH\_Drawing\_ErrorCodeReset](capi-drawing-error-code-h.md#oh_drawing_errorcodereset)重置错误码。 |
| [void OH\_Drawing\_ErrorCodeReset(void)](capi-drawing-error-code-h.md#oh_drawing_errorcodereset) | 将本模块的错误码重置为OH\_DRAWING\_SUCCESS。  通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)获取的本模块错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，但是不会在执行成功后被重置为OH\_DRAWING\_SUCCESS。  调用本接口可将错误码重置为OH\_DRAWING\_SUCCESS，避免多个接口间互相干扰，方便开发者调试。 |

## 枚举类型说明

### OH\_Drawing\_ErrorCode

```c
enum OH_Drawing_ErrorCode
```

**描述**

枚举本模块可能产生的错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_DRAWING\_SUCCESS = 0 | 操作成功完成。 |
| OH\_DRAWING\_ERROR\_NO\_PERMISSION = 201 | 权限校验失败。请检查是否已申请所需权限。 |
| OH\_DRAWING\_ERROR\_INVALID\_PARAMETER = 401 | 无效的输入参数，如参数中传入了NULL。请检查参数类型、取值范围或参数是否为空。 |
| OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE = 26200001 | 输入参数不在有效的范围内。请检查参数值是否在接口文档规定的有效范围内。 |
| OH\_DRAWING\_ERROR\_ALLOCATION\_FAILED = 26200002 | 内存分配失败。  **起始版本：** 13 |
| OH\_DRAWING\_ERROR\_ATTRIBUTE\_ID\_MISMATCH = 26200003 | 输入属性id无匹配的函数。请检查属性id是否正确，确保使用有效的属性id。  **起始版本：** 21 |
| OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER = 26200004 | 输入参数不正确，例如入参的指针为空。请检查传入的参数是否正确，确保指针参数有效且不为空。  **起始版本：** 22 |
| OH\_DRAWING\_ERROR\_FILE\_NOT\_FOUND = 26200005 | 文件未找到，指定的文件不存在或路径不正确。请检查文件路径是否正确，确保文件存在且路径格式有效。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_OPEN\_FILE\_FAILED = 26200006 | 打开文件失败，权限不足或I/O问题造成。请检查文件权限设置是否正确，或稍后重试。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_FILE\_SEEK\_FAILED = 26200007 | 文件定位失败。系统无法重新定位文件读取指针。请检查文件是否被其他进程占用，或重新打开文件后重试。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_GET\_FILE\_SIZE\_FAILED = 26200008 | 获取文件大小失败，系统无法获取文件大小信息。请检查文件是否存在且可访问，确保文件未被损坏。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_READ\_FILE\_FAILED = 26200009 | 读取文件失败，文件无法完整读取或包含不可读数据。请检查文件是否完整且未被损坏，确保文件格式正确。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_EMPTY\_FILE = 26200010 | 文件为空，指定的字体文件为空，不包含有效数据。请检查文件内容，确保使用包含有效数据的字体文件。  **起始版本：** 23 |
| OH\_DRAWING\_ERROR\_FILE\_CORRUPTED = 26200011 | 文件损坏，文件内容无效或损坏，无法解析。请检查文件是否完整，尝试重新获取或替换有效的文件。  **起始版本：** 23 |

## 函数说明

### OH\_Drawing\_ErrorCodeGet()

```c
OH_Drawing_ErrorCode OH_Drawing_ErrorCodeGet()
```

**描述**

获取本模块最近一次的错误码。

本模块的错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，在执行成功后不会被重置为OH\_DRAWING\_SUCCESS。可通过[OH\_Drawing\_ErrorCodeReset](capi-drawing-error-code-h.md#oh_drawing_errorcodereset)重置错误码。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 返回本模块最近一次的错误码。当函数成功运行后，本函数返回的错误码不会被修改。 |

### OH\_Drawing\_ErrorCodeReset()

```c
void OH_Drawing_ErrorCodeReset(void)
```

**描述**

将本模块的错误码重置为OH\_DRAWING\_SUCCESS。

通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)获取的本模块错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，但是不会在执行成功后被重置为OH\_DRAWING\_SUCCESS。

调用本接口可将错误码重置为OH\_DRAWING\_SUCCESS，避免多个接口间互相干扰，方便开发者调试。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18
