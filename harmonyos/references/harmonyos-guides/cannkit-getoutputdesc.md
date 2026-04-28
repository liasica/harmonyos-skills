---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputdesc
title: GetOutputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetOutputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb1fed6e5d8cd897154e7497426e6af771cdfb2a48c9593c2166101d6d1c9cd4
---

## 函数功能

根据算子输出索引获取对应输出的tensor描述信息。这里的输出索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```
1. const CompileTimeTensorDesc *GetOutputDesc(const size_t index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输出索引，从0开始计数。 |

## 返回值

输出TensorDesc的指针，当输入index非法时，返回空指针。

关于CompileTimeTensorDesc的定义，请参见[CompileTimeTensorDesc](cannkit-compiletimetensordesc-constructor.md)。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. for (size_t idx = 0; idx < extend_context->GetComputeNodeInfo()->GetOutputsNum(); ++idx) {
4. auto output_td = extend_context->GetOutputDesc(idx);
5. // ...
6. }
```
