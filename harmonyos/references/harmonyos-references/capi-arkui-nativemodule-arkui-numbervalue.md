---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-numbervalue
title: ArkUI_NumberValue
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NumberValue
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f790ed5c8f1f372d65fc59ef6084a2ee929e7d8371825bc985c280d9ae36041a
---

```c
typedef union {...} ArkUI_NumberValue
```

## 概述

ArkUI 在 Native 侧使用的数字类型，用于通过统一类型承载浮点、有符号整型和无符号整型数值。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float f32 | 浮点类型的变量，用于存储浮点类型的数值。 |
| int32\_t i32 | 有符号整型的变量，用于存储有符号整型的数值。 |
| uint32\_t u32 | 无符号整型的变量，用于存储无符号整型的数值。 |
