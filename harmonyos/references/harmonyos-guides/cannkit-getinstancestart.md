---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinstancestart
title: GetInstanceStart
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > GetInstanceStart
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55c0e3a74784faea65c20c5f4cca09063ac4e35d40354b2f99c64583ca26df93
---

## 函数功能

获取算子某个IR输入在实际输入中的起始序号（index）。

## 函数原型

```cpp
uint32_t GetInstanceStart() const
```

## 参数说明

无

## 返回值

算子某个IR输入在实际输入中的起始序号（index）。

## 约束说明

无

## 调用示例

```cpp
AnchorInstanceInfo anchor_0(0, 10); // IR定义的第1个输入是动态输入，且有10个实际输入
AnchorInstanceInfo anchor_1(10, 1); // IR定义的第2个输入是必选输入，且有1个实际输入，排在实际输入的第10个
auto input_num_1 = anchor_1.GetInstanceStart(); // input_num_1 = 10
```
