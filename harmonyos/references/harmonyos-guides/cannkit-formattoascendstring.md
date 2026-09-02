---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-formattoascendstring
title: FormatToAscendString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > FormatToAscendString
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:0dd60789aabff3fb139ecb6bf4aecb821edee944d9a591790ddcb0e0e60e414b
---

## 函数功能

将Format类型值转化为字符串表达。

使用该接口需要包含type\_utils.h头文件。

```cpp
#include "graph/utils/type_utils.h"
```

## 函数原型

```cpp
static AscendString FormatToAscendString(const Format &format);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 待转换的Format，支持的Format请参考[Format](cannkit-ge-format.md)。 |

## 返回值

转换后的Format字符串，[AscendString](cannkit-ascendstring-construction-and-destructor.md)类型。

## 约束说明

无

## 调用示例

```cpp
ge::Format format = ge::Format::FORMAT_NHWC;
auto format_str = FormatToAscendString(format); // "NHWC"
const char *ptr = format_str.GetString(); // 获取char*指针
```
