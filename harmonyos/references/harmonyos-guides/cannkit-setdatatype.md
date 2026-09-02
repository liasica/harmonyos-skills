---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdatatype
title: SetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > SetDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:090c3741be00d600fbb9da519bc808791bda2ed9637e3fd23433675354bc481e
---

## 函数功能

设置Tensor的数据类型。

## 函数原型

```cpp
void SetDataType(const ge::DataType data_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data\_type | 输入 | 需要设置的Tensor的数据类型。  关于ge::DataType的定义，请参见[DataType](cannkit-ge-datatype.md)。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
StorageShape sh({1, 2, 3}, {1, 2, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
t.SetDataType(ge::DT_DOUBLE);
```
