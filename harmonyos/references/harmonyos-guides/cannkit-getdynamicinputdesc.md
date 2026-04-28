---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicinputdesc
title: GetDynamicInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetDynamicInputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ad9132145b433d071ab97493d4f7c03f846ef8c088dbe7bff7af116108923491
---

## 函数功能

根据算子原型定义中的输入索引获取对应动态输入的tensor描述信息。

## 函数原型

```
1. const CompileTimeTensorDesc *GetDynamicInputDesc(const size_t ir_index, const size_t relative_index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 算子IR原型定义中的输入索引，从0开始计数。 |
| relative\_index | 输入 | 该输入实例化后的相对index，例如某个DYNAMIC\_INPUT实例化了3个输入，那么relative\_index的有效范围是[0,2]。 |

## 返回值

CompileTimeTensorDesc指针，index或relative\_index非法时，返回空指针。

关于CompileTimeTensorDesc的定义，请参见[CompileTimeTensorDesc](cannkit-compiletimetensordesc-constructor.md)。

## 约束说明

无
