---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-helper-8h
title: hiai_helper.h
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 头文件 > hiai_helper.h
category: harmonyos-references
scraped_at: 2026-04-28T08:18:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3c3d2800f7317964cb7cb782f1ff70ac2ce62bfb37bf615c3f663aecf0d161b4
---

## 概述

PhonePC/2in1TabletTV

查询CANN Kit版本以及检查模型支持情况的接口。

**引用文件：** <CANNKit/hiai\_helper.h>

**库：** libhiai\_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：** [CANN](cannkit.md)

## 汇总

PhonePC/2in1TabletTV

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) {  HIAI\_COMPATIBILITY\_COMPATIBLE = 0,  HIAI\_COMPATIBILITY\_INCOMPATIBLE = 1  } | 编译后模型兼容性结果。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| const char \* [HMS\_HiAI\_GetVersion](cannkit.md#hms_hiai_getversion) (void) | 获取CANN Kit版本号，并通过返回模板hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3指定X1是否为0来区分是否支持NPU。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。 |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromFile](cannkit.md#hms_hiaicompatibility_checkfromfile) (const char \*file) | 查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
| [HiAI\_Compatibility](cannkit.md#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromBuffer](cannkit.md#hms_hiaicompatibility_checkfrombuffer) (const void \*data, size\_t size) | 查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
