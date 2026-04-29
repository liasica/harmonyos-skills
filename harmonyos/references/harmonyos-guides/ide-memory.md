---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-memory
title: 记忆（Memory）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 记忆（Memory）配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:15+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:939b269ef8715bd8014c8d150a7e23c799b97d5d92d5d28058006fb0c39471c6
---

## 功能介绍

CodeGenie搭载长期记忆功能，在应用开发过程中，会学习和提取个人偏好、项目细节等有价值的信息，进行主动记忆或自动记忆。伴随开发者的持续使用，逐步形成覆盖开发者信息、项目场景、问题沉淀的全域记忆体系。在长期交互中，记忆也会随时间更新。

依托这一核心能力，CodeGenie能够精准理解和生成符合开发者需求的代码、回答等，与开发者实现更高效的协作。

### 基本概念

* 主动记忆：开发者要求CodeGenie记住输入的内容，CodeGenie会保存这些信息。
* 自动记忆：自动提取对话中有价值的信息，记录任务执行进度，随时间推移学习开发者的编码风格和项目细节等。

### 使用约束

* 当前仅自定义Agent支持长期记忆检索和生成。
* 当CodeGenie记忆与[规则（Rules）](ide-agent-rules.md)发生冲突时，以规则为准。
* Mac(64-bit)架构的MacOS操作系统不支持记忆能力。

## 操作步骤

1. 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/AQXod1vgQ061x1S9hR4SCA/zh-cn_image_0000002530913008.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=3A41279FBC24EEDEB502F61548177E72DD86A9269B684A7F1C1668A2C1FB112E)按钮，选择**Memory**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/tp1c9PHuTlusd88MNnPuXA/zh-cn_image_0000002544419464.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=F29DC53FBB313FBED9D1D7C3FA89A8D7E809690B3F7CE67117DF4A7B13F4A022)
2. 点击Memory后开关，开启和关闭记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/JlYTl2i9T0Cnnhnj8YIn_A/zh-cn_image_0000002574940769.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=07154400A5277B628C56428AD834BC51C86F1D68C64B4E8C4C8D4C281A4DFE35)
3. 在**Memory List**（记忆列表）下展示所有记忆，包括**Global**（记录用户相关信息）、**Project**（记录项目相关信息）。将鼠标悬浮在记忆上会显示具体信息，以及出现编辑、删除按钮，方便开发者管理记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/a77q0VFkRp-5Trbq99NiUw/zh-cn_image_0000002547833062.png?HW-CC-KV=V1&HW-CC-Date=20260429T054514Z&HW-CC-Expire=86400&HW-CC-Sign=577D0C59F7A437B7ABFA61008BB997FAE51829C84D585024C88F97F5F4279FC9 "点击放大")
