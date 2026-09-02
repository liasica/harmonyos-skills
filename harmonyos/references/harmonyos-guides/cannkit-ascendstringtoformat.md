---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstringtoformat
title: AscendStringToFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > AscendStringToFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0316dd471cb92004560732132de26f4fb745e07799a3c1564d9e0128430f2c0d
---

## 函数功能

将字符串转化为Format类型值。

使用该接口需要包含type\_utils.h头文件。

```cpp
#include "graph/utils/type_utils.h"
```

## 函数原型

```cpp
static Format AscendStringToFormat(const AscendString &str);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| str | 输入 | 待转换的Format字符串形式，[AscendString](cannkit-ascendstring-construction-and-destructor.md)类型。 |

## 返回值

输入合法时，返回转换后的Format enum值，枚举定义请参考[Format](cannkit-ge-format.md)；输入不合法时，返回FORMAT\_RESERVED，并打印报错信息。

## 约束说明

无

## 调用示例

```cpp
ge::AscendString format_str("NHWC");
auto format = AscendStringToFormat(format_str); // 1
```
