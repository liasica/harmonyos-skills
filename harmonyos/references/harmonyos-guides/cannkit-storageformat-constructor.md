---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > 构造函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4bb9643cad3e55022d9930243fb88b99f80bb291b2bfbde9d3ea432eaa4f385a
---

## 函数功能

构造一个格式，格式包括原始格式、运行时格式、补维规则。

## 函数原型

```
1. StorageFormat()
2. StorageFormat(const ge::Format origin_format, const ge::Format storage_format, const ExpandDimsType &expand_dims_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| origin\_format | 输入 | 原始格式。 |
| storage\_format | 输入 | 运行时格式。 |
| expand\_dims\_type | 输入 | 补维规则。 |

## 返回值

返回一个指定了origin\_format、storage\_format和expand\_dims\_type的StorageFormat对象 **。**

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
```
