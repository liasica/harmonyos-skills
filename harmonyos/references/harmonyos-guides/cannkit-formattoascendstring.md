---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-formattoascendstring
title: FormatToAscendString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > FormatToAscendString
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:221220fd2fc509a50a0cf8e44171c2f1defe7308c31e3bfb9ac0f9eb1e4b45e0
---

## 函数功能

将Format类型值转化为字符串表达。

使用该接口需要包含type\_utils.h头文件。

```
1. #include "graph/utils/type_utils.h"
```

## 函数原型

```
1. static AscendString FormatToAscendString(const Format &format);
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

```
1. ge::Format format = ge::Format::FORMAT_NHWC;
2. auto format_str = FormatToAscendString(format); // "NHWC"
3. const char *ptr = format_str.GetString();  // 获取char*指针
```
