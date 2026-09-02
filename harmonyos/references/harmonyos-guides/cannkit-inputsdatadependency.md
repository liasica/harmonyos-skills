---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inputsdatadependency
title: InputsDataDependency
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > InputsDataDependency
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9719066a8bf71f3a9cb199abcfe8a7d15c52b7d631f47cf87afacd799cdef075
---

## 函数功能

设置算子计算依赖第几个输入tensor的值。

所谓的数据依赖，是指算子的计算不仅依赖于输入tensor的shape，还依赖输入tensor的具体值。

## 函数原型

```cpp
OpImplRegisterV2 &InputsDataDependency(std::initializer_list<int32_t> inputs);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| inputs | 输入 | 指定算子计算需要依赖的输入index列表。举例来说，inputs={0, 3}，说明该算子的计算需要依赖第0、3个输入的tensor值。 |

## 返回值

返回算子的OpImplRegisterV2 对象，该对象新增设置算子计算依赖第几个输入tensor的值。

## 约束说明

无
