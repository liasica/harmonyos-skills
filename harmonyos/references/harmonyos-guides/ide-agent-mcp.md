---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp
title: 模型上下文协议（MCP）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 模型上下文协议（MCP）配置
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:39+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:4b058039a21f97cd0c7a5b897bbd3071f464c3bcd0b709905b39864fe7c1e872
---

## 功能介绍

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置模型上下文协议（Model Context Protocol，简称MCP）。MCP是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，以及支持从MCP Market添加MCP工具。

### 使用约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

* npx：依赖于Node.js，建议使用Node.js的LTS版本。
* uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/_IxsBnXpS8CPTIe9PKfotw/zh-cn_image_0000002779566794.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=F726273C350255BD2EA87FA66E3DA3EC54B9D0A6269F5CBD356FC8C130B571A8 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/GzZkFh7XRWOivl53TPw0tA/zh-cn_image_0000002779406806.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7AFD24551AC0A36D6BE35C89D7BFEF9338C29ED2E111E02ED8890AF1D7648AC)按钮，选择**MCP**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/FYogZMzRTPGsA2uC7Pv05g/zh-cn_image_0000002779406816.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=7397BF53F841B46735C9FE6DC75228E871A53B1A3BD3178529810D50B80C4809 "点击放大")
2. 添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/vRg1by0nSxaFM_DjMy5g1Q/zh-cn_image_0000002779566792.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E29E0DEADF620889B7E24DAEB81C065246699793BF05E6560F036827D05D677 "点击放大")按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP Market添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/jsWJ3volQ_62eh7Pu7ApNg/zh-cn_image_0000002808766381.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B60CD75E9E5C4C476561BC414920DD85588B34043417ADF45CA0C41187708E3 "点击放大")

   * **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

     **说明** 

     MCP Server支持三种通信方式：Stdio、Server-Sent Events (SSE) 和Streamable HTTP。

     Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/10aGy63VSqqqSCaH2kORfg/zh-cn_image_0000002808886459.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=04E1E758824C1D64EA49E2B051EAC8D465C483E3E28064C9CB2D183E3B6DC0E2 "点击放大")
   * **从MCP Market添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/tf8flwqYRaqblHnNNJYBKg/zh-cn_image_0000002779406814.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EEAECC54C962DA5BC258FB6294647240EA6BBF004CB3BADB2E0D62054DBE927 "点击放大")按钮添加。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/J3-xZaLgQfeqdEdHD-mVew/zh-cn_image_0000002779566800.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B5BCFC5CA95BF5ECB6AAE89B8A08D006B2F0DD09A73E6C61075A1DB9C75C689 "点击放大")
3. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/L7p4He9iRpOzbolw_opHWw/zh-cn_image_0000002779406820.png?HW-CC-KV=V1&HW-CC-Date=20261124T044239Z&HW-CC-Expire=31536000000&HW-CC-Sign=68D0D44CC03399DC4EC3362D7016EF63FF6E968C1DA5B028D084CC5C08007F3B "点击放大")
   * 名称：MCP工具名称，如time。
   * 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
   * 启用状态：工具是否已启用。
