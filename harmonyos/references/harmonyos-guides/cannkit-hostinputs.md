---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hostinputs
title: HostInputs
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > HostInputs
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7318a5c87bcd21d7bb44156ea38ef1e576bac1b454f5b36c422bf7926837c25
---

## 函数功能

当算子输入中存在标量输入时，需要传入host侧地址。该接口用于标记算子的第几个输入的地址是host侧地址。

## 函数原型

```cpp
OpImplRegisterV2 &HostInputs(std::initializer_list<int32_t> inputs);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| inputs | 输入 | 指定输入index列表。举例来说，inputs={0, 3}，说明算子的第0、3个输入的地址是host侧地址。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了标记算子的第几个输入的地址是host侧地址。

## 约束说明

无
