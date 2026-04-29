---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getparsesubgraphpostfn
title: GetParseSubgraphPostFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetParseSubgraphPostFn
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ea91641f347aa1ee2c100000e51667984d5f703bd3ad25c8a4686213f5f06a57
---

## 函数功能

根据算子类型，获取算子注册的子图中输入输出节点跟算子的输入输出的对应关系实现的函数对象。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

* **ParseSubgraphFunc GetParseSubgraphPostFn() const**

  该函数会返回ParseSubgraphFunc类型的函数对象，ParseSubgraphFunc函数的声明如下。

  ```
  1. using ParseSubgraphFunc = std::function<Status(const std::string &subgraph_name, const ge::Graph &graph)>
  ```
* **Status GetParseSubgraphPostFn(ParseSubgraphFuncV2 &func) const**

  该函数会返回ParseSubgraphFuncV2类型的函数对象，ParseSubgraphFuncV2函数的声明如下。

  ```
  1. using ParseSubgraphFuncV2 = std::function<Status(const ge::AscendString &subgraph_name, const ge::Graph &graph)>
  ```

## 参数说明

* GetParseSubgraphPostFn()函数

  无
* GetParseSubgraphPostFn(ParseSubgraphFuncV2 &func)函数

  | 参数 | 输入/输出 | 说明 |
  | --- | --- | --- |
  | func | 输出 | 实现算子注册的子图中输入输出节点跟算子的输入输出对应关系的函数对象。 |

## 约束说明

无
