---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getexpanddimstype
title: GetExpandDimsType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageFormat > GetExpandDimsType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94a1b55b4e685402761e88cfe2c35517599c61c1e7c1fea97364c9a4818531b9
---

## 函数功能

获取补维规则。

## 函数原型

```cpp
ExpandDimsType GetExpandDimsType() const
```

## 参数说明

无

## 返回值

补维规则。

## 约束说明

无

## 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto fmt_dim_type = format.GetExpandDimsType();
```
