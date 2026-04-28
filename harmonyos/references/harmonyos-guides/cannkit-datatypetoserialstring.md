---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-datatypetoserialstring
title: DataTypeToSerialString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > DataTypeToSerialString
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55eedf7fdd6833aba52e96de98189c6744d776811d575f76613d1b05aa2e0f1a
---

## 函数功能

将DataType类型值转化为字符串表达。

从GCC 5.1版本开始，libstdc++为了更好的实现C++11规范，更改了std::string和std::list的一些接口，导致新老版本ABI不兼容。所以推荐使用[DataTypeToAscendString](cannkit-datatypetoascendstring.md)替代本接口。

使用该接口需要包含type\_utils.h头文件。

```
1. #include "graph/utils/type_utils.h"
```

## 函数原型

```
1. std::string DataTypeToSerialString(const DataType data_type);
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

```
1. DataType data_type = ge::DT_UINT32;
2. auto type_str = DataTypeToSerialString(data_type); // "DT_UINT32"
```
