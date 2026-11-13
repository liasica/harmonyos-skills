---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-agent
title: Agent模式
breadcrumb: 指南 > DevEco Code > DevEco Code TUI > Agent模式
category: harmonyos-guides
scraped_at: 2026-11-13T09:00:03+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3c6d8ab96e71e5b47d15b96ee27a627a3249da0a6f48883fabb007fd8a9ccaf0
---

## 功能概述

DevEco Code支持三种Agent模式，分别为Build模式、Plan模式、Goal模式。

在DevEco Code对话框输入**/agents**，可查看当前可用的Agent模式，按**Tab****键**可快速切换不同模式。

## Build模式

开发者输入需求描述后，Agent直接进入任务执行阶段，自动完成需求理解、代码生成（如添加一个跳转按钮）、代码修复、构建出包和推送至模拟器的操作。然后，用户对实现结果测试验证，输入指令后可继续修改。

### 约束与限制

* Windows/macOS版DevEco Code可配置模拟器进行推包验证。
* 鸿蒙电脑版DevEco Code可使用本地真机进行推包验证。

### 实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/oHLpJaPJRBiQl09VY9W_Gw/zh-cn_image_0000002779567392.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C65D836101D0938118475938CB93367C6F38B4CD95D7BE7C9972C28E7FC26A21 "点击放大")

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/07/v3/OLbv4sHyRDm2n1_gmuBdWQ/zh-cn_media_0000002808887057.mp4?HW-CC-KV=V1&HW-CC-Date=20261113T010003Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A7ACEA8B94C43123616FBA064284BFF8C5B65BFB0BD1C407464BCAD766D7537)

## Plan + Build模式

该模式面向复杂的任务需求，可深度理解开发者意图，实现从需求理解、自动编码、编译、构建、推包到模拟器/预览器的全流程开发。

使用时需先选择Plan模式，通过交互方式规划可执行的任务列表，此时仅读取和分析代码，不修改文件；然后，再切换至Build模式，Agent按照任务列表开始自动执行流水线。

### 约束与限制

* Windows/macOS版DevEco Code可配置模拟器进行推包验证。
* 鸿蒙电脑版DevEco Code可使用本地真机进行推包验证。

### 实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/7_eUsqcET8W3MKujbEOaAg/zh-cn_image_0000002808766971.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A2A7757BD7CE5C12F6DAA5B1F1E214A04941CAF986FE7AF4EF0DB3D8BDC121E "点击放大")

Plan + Build模式实现流程分为三大阶段：

1. 任务列表制定阶段，开发者输入需求描述后，Agent结合用户需求、工程目录结构、代码文件、依赖关系和技术约束等理解需求背景，主动识别需求描述的模糊点、缺失信息和潜在约束，并通过Question工具与用户交互，补全信息。
2. 计划执行阶段，基于制定的任务列表，Agent自动进行代码生成、语法检查和代码修复，以及自动构建出包、推送至模拟器/预览器。
3. 用户自测阶段，开发者对实现结果测试验证，输入指令后可继续修改。

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/68/v3/qld7SLtFRSezX7zEUZu-ew/zh-cn_media_0000002779567394.mp4?HW-CC-KV=V1&HW-CC-Date=20261113T010003Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC6DFFABFB5ED8AA34B5F667CF993BC8B9D54FE8A6D8255ED42507FB4387A9D5)

## Goal模式

该模式是从需求到验证的全自动流水线，适用于完整的特性开发、关键质量模块开发、多人协作开发和从零搭建项目的场景。

用户输入需求描述后，通过交互的方式进行需求分析、架构设计和任务拆分，并生成结构化文档。Agent按照结构化文档闭环代码生成、语法校验、编译打包、模拟器部署、自动化验证与问题修复的全链路迭代，达成用户目标。

### 约束与限制

* 需要使用DevEco Studio 6.1.0及以上版本。
* Windows/macOS版DevEco Code可配置模拟器进行推包验证。
* 鸿蒙电脑版DevEco Code可使用本地真机进行推包验证。

### 实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/iORykznEShKR7FQNdrXJNA/zh-cn_image_0000002779407414.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=64F030EAA7DBEB3C2C101105DE574E7BF77CE797D26A3431BF82A40685C5D69C "点击放大")

Goal模式实现流程分为两大阶段：

1. 人机交互阶段：需求分析时，结合用户需求、工程目录结构、代码文件、依赖关系和技术约束等理解需求背景，主动识别需求中的模糊点，通过Question工具以交互的方式补全需求信息，确认设计方案、验收标准和任务列表等。
2. 自主迭代阶段：Agent自动进行代码开发、检查语法错误并修复，自动构建出包、推送到模拟器，自动验证功能的正确性，发现问题后自动修复代码，持续迭代直到完成用户的需求。

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/2a/v3/xccSMU6oTlqGsL0tdfaw6A/zh-cn_media_0000002779407416.mp4?HW-CC-KV=V1&HW-CC-Date=20261113T010003Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF9715C306941CB0EC6ED00D755221C72BAA0888B4D6F010E234A5D7DC43FE1C)
