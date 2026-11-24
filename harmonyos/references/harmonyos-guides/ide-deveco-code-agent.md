---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-agent
title: Agent模式
breadcrumb: 指南 > DevEco Code > DevEco Code TUI > Agent模式
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:51+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fbe1a73c8872088819785b3bc3d08155affd77f1b03c97dfe3f66768c1d5a4c7
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/a3R-UJPBTNi5b_qKTZN4YQ/zh-cn_image_0000002779567392.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=D38DFD35CDC7355BD2B41BC50AF606388CBEBD8EC3688170D66D7533D55C0F87 "点击放大")

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/a8/v3/LmxuarVmQUeryASWkLqRnQ/zh-cn_media_0000002808887057.mp4?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=374F58FAE45D3045C0D61F6EBD8394AA47F093BD0B323971628957751349BC4C)

## Plan + Build模式

该模式面向复杂的任务需求，可深度理解开发者意图，实现从需求理解、自动编码、编译、构建、推包到模拟器/预览器的全流程开发。

使用时需先选择Plan模式，通过交互方式规划可执行的任务列表，此时仅读取和分析代码，不修改文件；然后，再切换至Build模式，Agent按照任务列表开始自动执行流水线。

### 约束与限制

* Windows/macOS版DevEco Code可配置模拟器进行推包验证。
* 鸿蒙电脑版DevEco Code可使用本地真机进行推包验证。

### 实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/gMaRGQ3JT2WYHU9nlFdp9w/zh-cn_image_0000002808766971.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=C96E451121FDB71EFA6CB6B979416A0106F85F7B5D27FCBF4FD010DF4AA17BB6 "点击放大")

Plan + Build模式实现流程分为三大阶段：

1. 任务列表制定阶段，开发者输入需求描述后，Agent结合用户需求、工程目录结构、代码文件、依赖关系和技术约束等理解需求背景，主动识别需求描述的模糊点、缺失信息和潜在约束，并通过Question工具与用户交互，补全信息。
2. 计划执行阶段，基于制定的任务列表，Agent自动进行代码生成、语法检查和代码修复，以及自动构建出包、推送至模拟器/预览器。
3. 用户自测阶段，开发者对实现结果测试验证，输入指令后可继续修改。

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/30/v3/32X4uRrESxiMf3zLtV1eJQ/zh-cn_media_0000002779567394.mp4?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE328AF365401F596A454AAF0789EBEE9F5477F8611CB00F91F0530CDDD6BFAC)

## Goal模式

该模式是从需求到验证的全自动流水线，适用于完整的特性开发、关键质量模块开发、多人协作开发和从零搭建项目的场景。

用户输入需求描述后，通过交互的方式进行需求分析、架构设计和任务拆分，并生成结构化文档。Agent按照结构化文档闭环代码生成、语法校验、编译打包、模拟器部署、自动化验证与问题修复的全链路迭代，达成用户目标。

### 约束与限制

* 需要使用DevEco Studio 6.1.0及以上版本。
* Windows/macOS版DevEco Code可配置模拟器进行推包验证。
* 鸿蒙电脑版DevEco Code可使用本地真机进行推包验证。

### 实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/MR3_ZrYtRpCKfBO9tORJEQ/zh-cn_image_0000002779407414.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=72054497BB4F718CC6CF889CB1BE08E3D6631FCE487B985FCB178D9420DADD8F "点击放大")

Goal模式实现流程分为两大阶段：

1. 人机交互阶段：需求分析时，结合用户需求、工程目录结构、代码文件、依赖关系和技术约束等理解需求背景，主动识别需求中的模糊点，通过Question工具以交互的方式补全需求信息，确认设计方案、验收标准和任务列表等。
2. 自主迭代阶段：Agent自动进行代码开发、检查语法错误并修复，自动构建出包、推送到模拟器，自动验证功能的正确性，发现问题后自动修复代码，持续迭代直到完成用户的需求。

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/1/v3/HzsE8vm2S--dOlbOU-beCg/zh-cn_media_0000002779407416.mp4?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0A35D974C2C9532E92A17AD8DE1C6F69991ADBF7E2B041F9AC711FC863636F0)
