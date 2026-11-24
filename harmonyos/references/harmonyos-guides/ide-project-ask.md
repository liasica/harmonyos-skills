---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-ask
title: 工程问答
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 智能问答 > 工程问答
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:38+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:22bde9e24b3bb213688252860b96949c916ecc4119d105f497cd2186a7442ff8
---

从DevEco Studio 6.1.0 Beta2 版本开始，CodeGenie 新增工程问答能力。工程问答能够基于当前本地工程进行代码理解与分析，帮助开发者快速完成代码检索、定位和解读等工作。系统可自动分析工程结构，精准定位文件、类、函数、变量、常量、UI 元素等代码实体，并针对开发者提出的问题给出准确回答。

从26.0.0 Beta1版本开始，对于HarmonyOS应用开发相关问题，工具会自动检索HarmonyOS应用开发文档，提升问答的准确性，以及在同一会话中，支持多轮对话，实现深入问答。同时，支持在工程问答时调用MCP Market工具，问答时可自动调用相关MCP工具，实现更多功能；支持调用LSP（Language Server Protocol，语言服务器协议）工具，进行代码查找和引用查找；支持ArkTS和C++代码语义检索能力，用于跨文件、跨模块的代码搜索，有效提升查全率和准确率。调用MCP工具、LSP工具、开启语义检索的操作和示例如下。

## 调用MCP工具

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/SvfqurxzT0-lDlqeqOS_kA/zh-cn_image_0000002779407190.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=04F72D30657125B59E39A5276EC5F9A18F2FB3B9AE82C7A8E2418392EA74C1C2 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/XK7-I0fqSZaUm43MZdHIVg/zh-cn_image_0000002779567164.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=36EDA3787C1B47A5EF01576902BAEB5762711DE95BB1B82E3C4C0D9C52C53BD6)按钮，选择**MCP > MCP Market**。
2. 添加和开启所需的MCP工具。
3. 返回到CodeGenie首页，在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/8OZxLF5mTxmH1u_JUtuKrQ/zh-cn_image_0000002779567166.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=2928313337CD57626AF137F93B2787AE8D30E9947C70746E2EA33CA2CC2B7490)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/lIKT8m_zSlWewtOigw0dxw/zh-cn_image_0000002808886833.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAB7CDF87073920E8F1B4758316AD212F8738CA4D0F977B3FEFE7BF521C697BA "点击放大")

## 调用LSP工具

在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/-23kDs0wSKSWZP8uZsdC9A/zh-cn_image_0000002808766751.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD6A80501351C9BDFA26EE0574448981B660A809E7DEF7225CDD7D4744096C74)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/cRo2In5DRS6ljhi-1ydROA/zh-cn_image_0000002779407188.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=598E69C6E132739B446E812999F2A10D54D768D571D6ACCE6512496C9DC268C0 "点击放大")

## 语义检索

1. 在菜单栏点击**File > Settings...（macOS为DevEco Studio > Preferences/Settings） > CodeGenie > General**，勾选Project Semantic Index下的**Enable**选项。
2. 点击**Apply**或点击**OK**，开启语义检索功能。
3. 在对话区域输入“**/**”，在弹出的菜单中选择“**Project** ”，输入所需的描述，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/SwAVrsdZSaqUfPRtR2IoRA/zh-cn_image_0000002779407186.png?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=CACF30BD76C66C8D264A686DC0BFAE7A89A4B6996D0405075D94C49EBB71DE77)发送后等待回复。

**示例：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/xTLqvZVwRTuJ8Qq5FfxwkA/zh-cn_image_0000002779567168.gif?HW-CC-KV=V1&HW-CC-Date=20261124T044238Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0091774B40AE75282674678584407A141E5EB64834D748437CA77A5093A800D "点击放大")
