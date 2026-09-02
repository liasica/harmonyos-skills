---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-tensor-getoriginformat
title: GetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetOriginFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:12b3636c38e89780c94fea5bd2b2b014cb2fa5e0cb49c7838c93540710acb99c
---

## 函数功能

获取Tensor的原始format。

## 函数原型

```cpp
ge::Format GetOriginFormat() const
```

## 参数说明

无

## 返回值

原始format。

关于ge::Format类型的定义，请参见[Format](cannkit-ge-format.md)。

## 约束说明

无

## 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
t.SetOriginFormat(ge::FORMAT_NHWC);
t.SetStorageFormat(ge::FORMAT_NC1HWC0);
auto fmt = t.GetOriginFormat(); // ge::FORMAT_NHWC
```
