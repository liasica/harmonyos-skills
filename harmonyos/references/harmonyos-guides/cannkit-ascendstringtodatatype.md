---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstringtodatatype
title: AscendStringToDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > AscendStringToDataType
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:944e9f22b3599fd19ec886a4e71bbf156781a8dea4b33a62c26f0266bad3e081
---

## 函数功能

将DataType的字符串表达转换为DataType枚举值。

使用该接口需要包含type\_utils.h头文件。

```
1. #include "graph/utils/type_utils.h"
```

## 函数原型

```
1. static DataType AscendStringToDataType(const AscendString &str);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| str | 输入 | 待转换的DataType字符串形式，[AscendString](cannkit-ascendstring-construction-and-destructor.md)类型。 |

## 返回值

输入合法时，返回转换后的DataType enum值，枚举定义请参考[DataType](cannkit-ge-datatype.md)；输入不合法时，返回DT\_UNDEFINED并打印报错日志。

## 约束说明

无

## 调用示例

```
1. ge::AscendString type_str("DT_UINT32");
2. auto data_type = AscendStringToDataType(type_str); // 8
```
