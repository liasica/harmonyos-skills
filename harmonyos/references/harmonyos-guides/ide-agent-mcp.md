---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp
title: 模型上下文协议（MCP）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 模型上下文协议（MCP）配置
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:26+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:ed8bc871d0809865d95da6a8a0c758663e45236d0bdfe1eaa41d5c4643555c46
---

## 功能介绍

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置模型上下文协议（Model Context Protocol，简称MCP）。MCP是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，以及支持从MCP Market添加MCP工具。

### 使用约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

* npx：依赖于Node.js，建议使用Node.js的LTS版本。
* uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/giDwX6WCTcuS3xuUMpR9ZQ/zh-cn_image_0000002731542273.png "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/13KeDot6TmOMoo4jgbQUDA/zh-cn_image_0000002701663072.png)按钮，选择**MCP**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/Z-tRQQJ2SNixAaNR-pSZug/zh-cn_image_0000002731382299.png "点击放大")
2. 添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/SK0LNvhHRN6B_O5UBbacuw/zh-cn_image_0000002731542269.png "点击放大")按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP Market添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/LKHpME_iQ7WnOZbZaUFdOg/zh-cn_image_0000002731382309.png "点击放大")

   * **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

     **说明** 

     MCP Server支持三种通信方式：Stdio、Server-Sent Events (SSE) 和Streamable HTTP。

     Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/XMTIUoz7Qj6Eb3Cw_4N_GQ/zh-cn_image_0000002731382305.png "点击放大")
   * **从MCP Market添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/-Tc-KlIRQguVzxHtYrtWuw/zh-cn_image_0000002731382297.png "点击放大")按钮添加。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/xqMY2ADDQV2OaVe3B2KmKw/zh-cn_image_0000002731542281.png "点击放大")
3. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/LP7ehDQ7T0uZWU1gQ0-Oog/zh-cn_image_0000002731542277.png "点击放大")
   * 名称：MCP工具名称，如time。
   * 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
   * 启用状态：工具是否已启用。
