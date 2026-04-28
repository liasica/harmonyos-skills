---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getexpanddimstype
title: GetExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > GetExpandDimsType
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bbfbc6c5f6dfbfc1c6b517787e6d4ab7d73b58eff961bfce18d3cc880319e3e7
---

## 函数功能

获取补维规则。

## 函数原型

```
1. ExpandDimsType GetExpandDimsType() const
```

## 参数说明

无

## 返回值

补维规则。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType dim_type("1100");
2. StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
3. auto fmt_dim_type = format.GetExpandDimsType();
```
