---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-datatypetoascendstring
title: DataTypeToAscendString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > DataTypeToAscendString
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b449b6c2ec3539bcfd3d55ba13e9fdb55659296f7c7177b18038e32b29256c7a
---

## 函数功能

将DataType类型值转化为字符串表达。

使用该接口需要包含type\_utils.h头文件。

```
1. #include "graph/utils/type_utils.h"
```

## 函数原型

```
1. static AscendString DataTypeToAscendString(const DataType &data_type);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data\_type | 输入 | 待转换的DataType，支持的DataType请参考[DataType](cannkit-ge-datatype.md)。 |

## 返回值

转换后的DataType字符串，[AscendString](cannkit-ascendstring-construction-and-destructor.md)类型。

## 约束说明

无

## 调用示例

```
1. DataType data_type = ge::DT_UINT32;
2. auto type_str = DataTypeToAscendString(data_type); // "DT_UINT32"
3. const char *ptr = type_str.GetString();  // 获取char*指针
```
