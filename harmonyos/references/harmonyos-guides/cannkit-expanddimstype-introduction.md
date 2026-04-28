---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-expanddimstype-introduction
title: 简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > 简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f1eab824f10be9691578b1dcd62637eb52ad32d3db127cc2ce9090ce1f085c3
---

ExpandDimsType类基于补维后的shape，描述了补维规则。

补维的含义为：在原有shape的基础上，添加一到多个维度，例如原shape[2,2]有两根轴，那么在两根轴中间补两维后的shape为[2,1,1,2]。 补维后shape的第0、3根轴被称为原始轴，第1、2根轴被称为补维轴。

ExpandDimsType类通过“1”和“0”描述补维规则，“1”代表当前轴为补维轴，“0”代表当前轴为原始轴，从左到右依次代表当前shape每根轴的来源，例如：

**表1** 补维规则描述

| 补维规则 | 补维前shape | 补维后shape |
| --- | --- | --- |
| 0110 | [2, 2] | [2, 1, 1, 2] |
| 100 | [2, 3] | [1, 2, 3] |
| 1000 | [2, 3] | 补维规则与补维前shape不匹配，规则指定原始轴有3根，但原始shape只有2根轴，补维报错。 |
