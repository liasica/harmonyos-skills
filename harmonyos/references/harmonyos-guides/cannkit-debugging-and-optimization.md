---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-debugging-and-optimization
title: 维测调优
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > 维测调优
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5a389f3e89498706f33e6a7f4983ad85a99b51c5e033cc7e765c46af92626b81
---

## 概述

维测调优是CANN Kit提供的对AI模型进行性能统计，并获取性能数据的能力。当前[HiAI\_OmType](../harmonyos-references/cannkit.md#hiai_omtype)接口支持通过AI模型和随机构造的输入文件快速获取Profiling/Dump数据，开发人员可分析模型和单算子的性能数据，并通过模型的层级输出对比精度来完成问题定位。

## 能力简介

**Profiling模式**：

* 支持单算子及整网模型的Profiling性能数据获取，从而分析单算子及整网的执行耗时。
* 支持Profiling性能数据可视化。

**Dump模式**：

* 获取模型的层级输出。

## 使用说明

开发者可参考[CANN Kit Codelab](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_CANNKit-Optimize)示例完成性能数据获取。当前仅支持HarmonyOS 6.0.0(20)及以上版本的华为手机使用，可在[版本说明](../harmonyos-releases/overview-allversion.md)获取匹配的开发者套件，包含DevEco Studio和SDK。
