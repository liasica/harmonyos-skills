---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getstorageformat
title: GetStorageFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetStorageFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:98c6a5ce904d037f44faf059c14d1c4bfbe4a7d7e60ea57631a9874706935c17
---

## 函数功能

获取运行时Tensor的format。

## 函数原型

```cpp
ge::Format GetStorageFormat() const
```

## 参数说明

无

## 返回值

返回运行时format。

关于ge::Format类型的定义，请参见[Format](cannkit-ge-format.md)。

## 约束说明

无

## 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
t.SetOriginFormat(ge::FORMAT_NHWC);
t.SetStorageFormat(ge::FORMAT_NC1HWC0);
auto fmt = t.GetStorageFormat(); // ge::FORMAT_NC1HWC0
```
