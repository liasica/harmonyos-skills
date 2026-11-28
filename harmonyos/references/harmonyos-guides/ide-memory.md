---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-memory
title: 记忆（Memory）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 记忆（Memory）配置
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3fd99d86d713fb4af011f1f728c84817c0042ca6fcb392c558405766736e9edd
---

## 功能介绍

从 DevEco Studio 6.1.0 Beta2 版本开始，CodeGenie搭载长期记忆功能，在应用开发过程中，会学习和提取个人偏好、项目细节等有价值的信息，进行主动记忆或自动记忆。伴随开发者的持续使用，逐步形成覆盖开发者信息、项目场景、问题沉淀的全域记忆体系。在长期交互中，记忆也会随时间更新。

依托这一核心能力，CodeGenie能够精准理解和生成符合开发者需求的代码、回答等，与开发者实现更高效的协作。

### 基本概念

* 主动记忆：开发者要求CodeGenie记住输入的内容，CodeGenie会保存这些信息。
* 自动记忆：自动提取对话中有价值的信息，记录任务执行进度，随时间推移学习开发者的编码风格和项目细节等。

### 使用约束

* 当前仅自定义Agent和HarmonyOS Act智能体支持长期记忆检索和生成。其中HarmonyOS Act智能体从26.0.0 Beta1版本开始支持。
* 当CodeGenie记忆与[规则（Rules）](ide-agent-rules.md)发生冲突时，以规则为准。
* Mac(64-bit)架构的MacOS操作系统不支持记忆能力。

## 操作步骤

1. 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ZJRlCzUeSbWIySt-dnKP_w/zh-cn_image_0000002779566788.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=943F5E40D0E65C3DB277A7B09CC34EC4D84A3950013AD408F7EA78541A0E2C19)按钮，选择**Memory**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/j8mexXeEQ2i4fQ2o1q5T4g/zh-cn_image_0000002808886451.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=56D1176CB5919E6EF34F76B29F7B101DAC82BB1D899F89DDF80C382D753CBAFE)
2. 点击Memory后开关，开启和关闭记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/6GoEzQHrSLy7xIMIACfmpw/zh-cn_image_0000002808766371.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0D479478DCCEEE97F1EF67ADF7AF581810AC163C4741B5F0292B3AB79F416E9 "点击放大")
3. 在**Memory List**（记忆列表）下展示所有记忆，包括**Global**（记录用户相关信息）、**Project**（记录项目相关信息）。将鼠标悬浮在记忆上会显示具体信息，以及出现编辑、删除按钮，方便开发者管理记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/MEcgWyyNSAK3emHp_qtdCw/zh-cn_image_0000002808886453.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=50970AC0B22D01AB5EE1848AA3B8B9C855ACA6E35EB9DD78A31B29036238447E "点击放大")
