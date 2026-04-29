---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-parsesubgraphpostfn
title: ParseSubgraphPostFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > ParseSubgraphPostFn
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8ac5c740051155c5c47786b7eca68431f8430a1867d145d7fd7c41aeaff35f7
---

## 函数功能

根据算子类型，注册算子的子图中输入输出节点跟算子的输入输出的对应关系函数实现。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. OpRegistrationData &ParseSubgraphPostFn(const ParseSubgraphFunc &subgraph_post_fn)
2. OpRegistrationData &ParseSubgraphPostFn(const ParseSubgraphFuncV2 &subgraph_post_fn);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| subgraph\_post\_fn | 输入 | 子图中输入输出节点跟算子的输入输出的对应关系函数对象。  详见[回调函数ParseSubgraphFuncV2](cannkit-parsesubgraphpostfn.md#回调函数parsesubgraphfuncv2) **。** |

## 约束说明

无

## 回调函数ParseSubgraphFuncV2

开发者自定义并实现ParseSubgraphFuncV2函数，完成解析子图中输入输出节点跟算子的输入输出的对应关系功能，回调函数原型定义如下。

```
1. Status ParseSubgraphFuncV2(const ge::AscendString &subgraph_name, const ge::Graph &graph)
```

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| subgraph\_name | 输入 | 子图名字。 |
| graph | 输出 | 构造的子图。 |
