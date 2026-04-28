---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-formattoserialstring
title: FormatToSerialString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > FormatToSerialString
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b200a8494ebc1f4fb6b4bf254f1c6a4eb2f3bc1a9f83eebfcaf004b6bca70e63
---

## 函数功能

将Format类型值转化为字符串表达。

从GCC 5.1版本开始，libstdc++为了更好的实现C++11规范，更改了std::string和std::list的一些接口，导致新老版本ABI不兼容。所以推荐使用[FormatToAscendString](cannkit-formattoascendstring.md)替代本接口。

使用该接口需要包含type\_utils.h头文件。

```
1. #include "graph/utils/type_utils.h"
```

## 函数原型

```
1. std::string FormatToSerialString(const Format format);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| format | 输入 | 待转换的Format，支持的Format请参考[Format](cannkit-ge-format.md)。 |

## 返回值

转换后的Format字符串。

## 约束说明

无

## 调用示例

```
1. ge::Format format = ge::Format::FORMAT_NHWC;
2. auto format_str = FormatToSerialString(format); // "NHWC"
```
