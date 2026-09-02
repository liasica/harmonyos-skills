---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeinputnum
title: GetComputeNodeInputNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetComputeNodeInputNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f4115303ddc66e3028a18a910d0136543e3a24beae0c585f6258cdd3f39b045
---

## 函数功能

获取算子的输入个数。

## 函数原型

```cpp
size_t GetComputeNodeInputNum() const
```

## 参数说明

无

## 返回值

算子的输入个数。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
for (size_t idx = 0; idx < extend_context->GetComputeNodeInputNum(); ++idx) {
  auto input_td = extend_context->GetInputDesc(idx);
  // ...
}
```
