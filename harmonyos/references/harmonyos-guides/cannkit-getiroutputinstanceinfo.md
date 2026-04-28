---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getiroutputinstanceinfo
title: GetIrOutputInstanceInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetIrOutputInstanceInfo
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48234ec4272e733ba46cc215556baf61602546e9a59c9eb11087c88e6bd58205
---

## 函数功能

根据算子原型定义中的输出索引获取对应输出的实例化信息。

## 函数原型

```
1. const AnchorInstanceInfo *GetIrOutputInstanceInfo(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 算子IR原型定义中的输出索引，从0开始计数。 |

## 返回值

指定输出的实例化信息。

关于AnchorInstanceInfo的定义，请参见[AnchorInstanceInfo](cannkit-anchorinstanceinfo-introduction.md)。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. for (size_t idx = 0; idx < extend_context->GetComputeNodeInfo()->GetOutputsNum(); ++idx) {
4. auto output_td = extend_context->GetIrOutputInstanceInfo(idx);
5. // ...
6. }
```
