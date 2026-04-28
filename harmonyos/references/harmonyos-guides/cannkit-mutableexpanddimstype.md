---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableexpanddimstype
title: MutableExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > MutableExpandDimsType
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ffcb9a18f2271b49247ade0c0043eec8fac8a04847007c09bbe08df2c53ecc03
---

## 函数功能

获取可写的补维规则。

## 函数原型

```
1. ExpandDimsType &MutableExpandDimsType()
```

## 参数说明

无

## 返回值

补维规则引用。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. ExpandDimsType new_dim_type("1010");
4. format.SetExpandDimsType(new_dim_type);
5. auto &fmt_dim_type = format.MutableExpandDimsType();
```
