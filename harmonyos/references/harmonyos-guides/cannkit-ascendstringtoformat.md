---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstringtoformat
title: AscendStringToFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > AscendStringToFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8b9dea1e9ab39c0066e925c4cafc3a6e83035b3d3f5e44b6a55c45c34d40299
---

## 函数功能

将字符串转化为Format类型值。

使用该接口需要包含type\_utils.h头文件。

```
1. #include "graph/utils/type_utils.h"
```

## 函数原型

```
1. static Format AscendStringToFormat(const AscendString &str);
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

```
1. ge::AscendString format_str("NHWC");
2. auto format = AscendStringToFormat(format_str); // 1
```
