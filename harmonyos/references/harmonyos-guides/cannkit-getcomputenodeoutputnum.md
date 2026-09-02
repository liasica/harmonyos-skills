---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeoutputnum
title: GetComputeNodeOutputNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetComputeNodeOutputNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2820a2981851eb6a3b895f5d6db30ce34f3a8862f0298ec4c2694be0a07d46af
---

## 函数功能

获取算子的输出个数。

## 函数原型

```cpp
size_t GetComputeNodeOutputNum() const;
```

## 参数说明

无

## 返回值

算子的输出个数。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
for (size_t idx = 0; idx < extend_context->GetComputeNodeOutputNum(); ++idx) {
  auto input_td = extend_context->GetOutputDesc(idx);
  // ...
}
```
