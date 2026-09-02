---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-datatypetoserialstring
title: DataTypeToSerialString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > DataTypeToSerialString
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:99aa183985e848fcdb65376d20f9566ee71aa8e9e49b329202d2d0e06e453ff9
---

## 函数功能

将DataType类型值转化为字符串表达。

从GCC 5.1版本开始，libstdc++为了更好的实现C++11规范，更改了std::string和std::list的一些接口，导致新老版本ABI不兼容。所以推荐使用[DataTypeToAscendString](cannkit-datatypetoascendstring.md)替代本接口。

使用该接口需要包含type\_utils.h头文件。

```cpp
#include "graph/utils/type_utils.h"
```

## 函数原型

```cpp
std::string DataTypeToSerialString(const DataType data_type);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data\_type | 输入 | 待转换的DataType，支持的DataType请参考[DataType](cannkit-ge-datatype.md)。 |

## 返回值

转换后的DataType字符串。

## 约束说明

无

## 调用示例

```cpp
DataType data_type = ge::DT_UINT32;
auto type_str = DataTypeToSerialString(data_type); // "DT_UINT32"
```
