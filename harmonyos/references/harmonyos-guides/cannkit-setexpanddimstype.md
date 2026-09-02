---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setexpanddimstype
title: SetExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > SetExpandDimsType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:492b78299853402f9b1b7605c467e1181ff0224b1b4bbe3020bd983e03aedefb
---

## 函数功能

设置补维规则。

## 函数原型

```cpp
void SetExpandDimsType(const ExpandDimsType &expand_dims_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| expand\_dims\_type | 输入 | 补维规则。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
ExpandDimsType new_dim_type("1010");
format.SetExpandDimsType(new_dim_type);
```
