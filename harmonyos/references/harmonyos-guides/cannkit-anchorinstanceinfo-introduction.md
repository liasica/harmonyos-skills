---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-anchorinstanceinfo-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > 简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b8f31f0d4b60b6bfa2b56c92ca2a807d4fc30ddcb5c9d2bc4bf1963e038c0af1
---

本类用于描述算子IR定义原型的输入信息与实际输入之间的关系，每个AnchorInstanceInfo对象对应一个IR输入，并记录两个描述信息：instantiation\_num\_和instance\_start\_。其中，instantiation\_num\_描述某个IR输入对应的实际输入个数；instance\_start\_描述某个IR输入在实际输入中的起始序号。当前IR定义提供了三种类型的输入：必选输入、可选输入、动态输入，如下

| 输入类型 | instantiation\_num\_ | instance\_start\_ |
| --- | --- | --- |
| 必选输入 | 必为1，否则报错 | 起始索引从0开始，instance\_start\_[i] = instance\_start\_[i-1] + instantiation\_num\_[i-1] |
| 可选输入 | 有实际输入时为1，否则为0 | 起始索引从0开始，instance\_start\_[i] = instance\_start\_[i-1] + instantiation\_num\_[i-1] |
| 动态输入 | 根据实际输入个数对应0~N个。 | 起始索引从0开始，instance\_start\_[i] = instance\_start\_[i-1] + instantiation\_num\_[i-1] |
