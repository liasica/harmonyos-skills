---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-agent
title: Agent模式
breadcrumb: 指南 > DevEco Code > DevEco Code TUI > Agent模式
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:867014ea90de79ac46075c73eb9d967e5c35e53bf52d3ca778b2400b93b67ac5
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Jnv4OgDcSneU6lzK4hGf1A/zh-cn_image_0000002779567392.png?HW-CC-KV=V1&HW-CC-Date=20261114T004921Z&HW-CC-Expire=31536000000&HW-CC-Sign=21CEAC142DF71F0E70D39D1189DD11B41964E0312DA0917A29C460842EDE9D71 "点击放大")

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/2e/v3/hZJrQ_zzSLyEhc3NX2gPOw/zh-cn_media_0000002808887057.mp4?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A9DDB8D830CB0676D89A249F07DF5AA17412B9BA20C7C7155019F4CF4903CE0)

## Plan + Build模式

该模式面向复杂的任务需求，可深度理解开发者意图，实现从需求理解、自动编码、编译、构建、推包到模拟器/预览器的全流程开发。

使用时需先选择Plan模式，通过交互方式规划可执行的任务列表，此时仅读取和分析代码，不修改文件；然后，再切换至Build模式，Agent按照任务列表开始自动执行流水线。

### 约束与限制

* Windows/macOS版DevEco Code可配置模拟器进行推包验证。
* 鸿蒙电脑版DevEco Code可使用本地真机进行推包验证。

### 实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/W5vMjRtwTd20i9UEmREEkQ/zh-cn_image_0000002808766971.png?HW-CC-KV=V1&HW-CC-Date=20261114T004921Z&HW-CC-Expire=31536000000&HW-CC-Sign=1323C49E43B335D2CD26C8F376295FD9AC8B2A8AAECF5C22E747FAEF093D1788 "点击放大")

Plan + Build模式实现流程分为三大阶段：

1. 任务列表制定阶段，开发者输入需求描述后，Agent结合用户需求、工程目录结构、代码文件、依赖关系和技术约束等理解需求背景，主动识别需求描述的模糊点、缺失信息和潜在约束，并通过Question工具与用户交互，补全信息。
2. 计划执行阶段，基于制定的任务列表，Agent自动进行代码生成、语法检查和代码修复，以及自动构建出包、推送至模拟器/预览器。
3. 用户自测阶段，开发者对实现结果测试验证，输入指令后可继续修改。

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/af/v3/hhTa1H7kQXGlNeU_Ob64XQ/zh-cn_media_0000002779567394.mp4?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB0E59E41174FED78E7261ADF2AE8B8E006BEECBE51E7E9E0A72FB8C9C0ACA02)

## Goal模式

该模式是从需求到验证的全自动流水线，适用于完整的特性开发、关键质量模块开发、多人协作开发和从零搭建项目的场景。

用户输入需求描述后，通过交互的方式进行需求分析、架构设计和任务拆分，并生成结构化文档。Agent按照结构化文档闭环代码生成、语法校验、编译打包、模拟器部署、自动化验证与问题修复的全链路迭代，达成用户目标。

### 约束与限制

* 需要使用DevEco Studio 6.1.0及以上版本。
* Windows/macOS版DevEco Code可配置模拟器进行推包验证。
* 鸿蒙电脑版DevEco Code可使用本地真机进行推包验证。

### 实现流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ewn_iHFcSQeEKkyZc5qMMA/zh-cn_image_0000002779407414.png?HW-CC-KV=V1&HW-CC-Date=20261114T004921Z&HW-CC-Expire=31536000000&HW-CC-Sign=427ABCC4E9906B743F1F09B5EC3301F2AA87E88C3F160C74863F568752B551D5 "点击放大")

Goal模式实现流程分为两大阶段：

1. 人机交互阶段：需求分析时，结合用户需求、工程目录结构、代码文件、依赖关系和技术约束等理解需求背景，主动识别需求中的模糊点，通过Question工具以交互的方式补全需求信息，确认设计方案、验收标准和任务列表等。
2. 自主迭代阶段：Agent自动进行代码开发、检查语法错误并修复，自动构建出包、推送到模拟器，自动验证功能的正确性，发现问题后自动修复代码，持续迭代直到完成用户的需求。

### 示例

[视频](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/d7/v3/tWgNUHU-QI-byk2LuZAdfg/zh-cn_media_0000002779407416.mp4?HW-CC-KV=V1&HW-CC-Date=20261114T004922Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EEB1AAC63F74E3F02A989199D9BE16E5B18EC6B233350535DEC1F6D5A8B02F3)
