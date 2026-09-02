---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-serialstringtoformat
title: SerialStringToFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > SerialStringToFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b67323e2b9f58f0642a3a477ccac49771122c1811c7315d03a595fc9992026b
---

## 函数功能

将字符串转化为Format类型值。

从GCC 5.1版本开始，libstdc++为了更好的实现C++11规范，更改了std::string和std::list的一些接口，导致新老版本ABI不兼容。所以推荐使用[AscendStringToFormat](cannkit-ascendstringtoformat.md)替代本接口。

使用该接口需要包含type\_utils.h头文件。

```cpp
#include "graph/utils/type_utils.h"
```

## 函数原型

```cpp
Format SerialStringToFormat(const std::string &str);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| str | 输入 | 待转换的Format字符串形式。 |

## 返回值

输入合法时，返回转换后的Format enum值，枚举定义请参考[Format](cannkit-ge-format.md)；输入不合法时，返回FORMAT\_RESERVED，并打印报错信息。

## 约束说明

无

## 调用示例

```cpp
std::string format_str = "NHWC";
auto format = SerialStringToFormat(format_str); // 1
```
