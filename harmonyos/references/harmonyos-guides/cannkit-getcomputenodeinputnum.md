---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeinputnum
title: GetComputeNodeInputNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetComputeNodeInputNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8810c0e16bf54e52daa9a9019f9f356ba70503add6799bbb28aab2e1eb8605f8
---

## 函数功能

获取算子的输入个数。

## 函数原型

```
1. size_t GetComputeNodeInputNum() const
```

## 参数说明

无

## 返回值

算子的输入个数。

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
