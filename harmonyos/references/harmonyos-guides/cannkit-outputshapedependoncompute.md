---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-outputshapedependoncompute
title: OutputShapeDependOnCompute
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > OutputShapeDependOnCompute
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:2ed2492d7a9eee9475434328a44b4cc80c9014cbc25c50ce57962a3f9a96c157
---

## 函数功能

注册shape依赖于计算得到的输出列表。某些算子，比如NonZero（统计tensor中非零值的个数），计算完成前无法得知算子输出的shape信息，算子计算完成后才能获取。该类算子在原型定义时，需要使用OutputShapeDependOnCompute接口进行标识，同时在算子核函数中将实际输出shape写入到出参中，便于框架侧基于该信息进行输出内存的管理。

## 函数原型

```cpp
OpImplRegisterV2 &OutputShapeDependOnCompute(std::initializer_list<int32_t> outputs);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| outputs | 输出 | 指定输出index列表。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了shape依赖于计算得到的输出列表。

## 约束说明

* 只能用于标识算子输出。
* 暂不支持算子入图。
