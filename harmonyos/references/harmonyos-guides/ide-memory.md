---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-memory
title: 记忆（Memory）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 记忆（Memory）配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:da714487c62234be1ea53cb5f4b486c8cd4741139bec64b12c6ae80196193241
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

## 操作步骤

1. 点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/PV8pkBGgSFaWQtNsP0bn7Q/zh-cn_image_0000002530913008.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=F814A5FB6F42BA16A6D7AEEF82A5B7991F9190ECD4237D5C36AC86464B398305)按钮，选择**Memory**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/8e6fk5SsQiukDOOBr_ju8g/zh-cn_image_0000002544419464.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=D1D2489D926FCB824633BB710F2FE8310CB68D55109CD26DE95F5FB71A5DA834)
2. 点击Memory后开关，开启和关闭记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/SY_aEenhREqGJxOT-3bVtg/zh-cn_image_0000002574940769.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=979F606CE535CFD4452A81479AEF156BCBC99FC5C012C8C92C60DD182D4CD160)
3. 在**Memory List**（记忆列表）下展示所有记忆，包括**Global**（记录用户相关信息）、**Project**（记录项目相关信息）。将鼠标悬浮在记忆上会显示具体信息，以及出现编辑、删除按钮，方便开发者管理记忆。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/aS3XbzbSSHOM_QKzqLJHlQ/zh-cn_image_0000002547833062.png?HW-CC-KV=V1&HW-CC-Date=20260427T235519Z&HW-CC-Expire=86400&HW-CC-Sign=2BD69ECF2048339A688EBDBCC6D97F2868861575EABCCF8D1E405ED58C289BC0 "点击放大")
