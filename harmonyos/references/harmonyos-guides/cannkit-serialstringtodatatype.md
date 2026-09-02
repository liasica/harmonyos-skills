---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-serialstringtodatatype
title: SerialStringToDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > SerialStringToDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3dff18daf6db12d1bf4624b86dab14e94d129dd4588d2e7d3900dff3d9ffa5f1
---

## 函数功能

将DataType的字符串表达转换为DataType枚举值。

从GCC 5.1版本开始，libstdc++为了更好的实现C++11规范，更改了std::string和std::list的一些接口，导致新老版本ABI不兼容。所以推荐使用[AscendStringToDataType](cannkit-ascendstringtodatatype.md)替代本接口。

使用该接口需要包含type\_utils.h头文件。

```cpp
#include "graph/utils/type_utils.h"
```

## 函数原型

```cpp
DataType SerialStringToDataType(const std::string &str);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| str | 输入 | 待转换的DataType字符串形式。 |

## 返回值

输入合法时，返回转换后的DataType enum值，枚举定义请参考[DataType](cannkit-ge-datatype.md)；输入不合法时，返回DT\_UNDEFINED并打印报错日志。

## 约束说明

无

## 调用示例

```cpp
std::string type_str = "DT_UINT32";
auto data_type = SerialStringToDataType(type_str); // 8
```
