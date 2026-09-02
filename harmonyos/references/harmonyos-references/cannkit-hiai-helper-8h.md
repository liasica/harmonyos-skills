---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-helper-8h
title: hiai_helper.h
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 头文件 > hiai_helper.h
category: harmonyos-references
scraped_at: 2026-09-02T15:03:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f8d1a9d070afe1fc44b9ab288e34f845e95d0c39d027cc8216cfaa054c23663b
---

## 概述

查询CANN Kit版本以及检查模型支持情况的接口。

**引用文件：** <CANNKit/hiai\_helper.h>

**库：** libhiai\_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：** [CANN](cannkit.md)

## 汇总

### 枚举

| 名称 | 描述 |
| --- | --- |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) {  HIAI\_COMPATIBILITY\_COMPATIBLE = 0,  HIAI\_COMPATIBILITY\_INCOMPATIBLE = 1  } | 编译后模型兼容性结果。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| const char \* [HMS\_HiAI\_GetVersion](cannkit.md#hms_hiai_getversion) (void) | 获取CANN Kit版本号，返回值为一个字符串，其格式遵循hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3规范。其中X1字段用于标识NPU支持状态。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。 |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromFile](cannkit.md#hms_hiaicompatibility_checkfromfile) (const char \*file) | 查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromBuffer](cannkit.md#hms_hiaicompatibility_checkfrombuffer) (const void \*data, size\_t size) | 查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
