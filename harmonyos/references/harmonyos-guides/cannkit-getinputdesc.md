---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputdesc
title: GetInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetInputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a2817c8807bfbe6056df52ad1ac6b22e41301ce02ecb9ae6ce350289fab7c4e4
---

## 函数功能

根据算子输入索引获取对应输入的tensor描述信息。这里的输入索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```
1. const CompileTimeTensorDesc *GetInputDesc(const size_t index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输入索引，从0开始计数。 |

## 返回值

输入TensorDesc的指针，当输入index非法时，返回空指针。

关于CompileTimeTensorDesc的定义，请参见[CompileTimeTensorDesc](cannkit-compiletimetensordesc-constructor.md)。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. for (size_t idx = 0; idx < extend_context->GetComputeNodeInputNum(); ++idx) {
4. auto input_td = extend_context->GetInputDesc(idx);
5. // ...
6. }
```
