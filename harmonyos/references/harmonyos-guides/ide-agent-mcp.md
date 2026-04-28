---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp
title: 模型上下文协议（MCP）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 模型上下文协议（MCP）配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:81f2f4d4edcf05c1bae672fac242878786b60ab1c1ff1c700ba1fc637c93cdc7
---

## 功能介绍

模型上下文协议（Model Context Protocol，简称MCP）是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置MCP。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，支持从MCP市场添加MCP工具。

## 环境约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

* npx：依赖于Node.js，建议使用Node.js的LTS版本。
* uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/4SowuORxR_GZwyFCSa5hyg/zh-cn_image_0000002561752883.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=E62D18C04754DABDA171158F018CC96746A1FEDA43F0830B6E48F1CADA29AEE5)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/S3pqBNxNQXG5O2gvMmupWA/zh-cn_image_0000002530912934.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=016F1FA97855E9F93410ADD538B8EC31A373C6643AE85275E2B7A255141F1633)按钮，选择**MCP**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/E1sygFFOQ_afjbfpa7MLig/zh-cn_image_0000002575045063.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=21A300896118BECBA58D9095C1FA1F4010428D94353F0BD939410F10C34A2E01 "点击放大")
2. 添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/DUh_MO49S9GnhpXsRaq60A/zh-cn_image_0000002561832863.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=CACB3304920FB5515B61B63BCB3745FE0B08FF4EA72C8C601B4E5F67D4E6455E)按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP市场添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/a6vDRIaGRBCG4zo1QYoX8w/zh-cn_image_0000002544364856.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=420DB9B169F13EAE50F7A34A6AEE41EF2BF7E7997A4CB63AEA3FF95CEA051C24 "点击放大")

   * **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

     说明

     MCP Server支持三种通信方式：Stdio 、Server-Sent Events (SSE) 和Streamable HTTP。

     Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/p8A0yykVRUK3XUDYqczBZQ/zh-cn_image_0000002544205206.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=97CE4519ACA338CF88B90B3909AF03D7F894A5844FCC9D92D49168C5B4E16C23 "点击放大")
   * **从MCP市场添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/dEmXeqf9TLixK736RL9g4A/zh-cn_image_0000002530912938.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=969120563DD2E4E78C2AF49ACB8A94E334E48EED371C7ADCDB1E0CF928A66FB1)按钮添加。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/DqzSY1k1SUC97a8H4cVbnw/zh-cn_image_0000002574885083.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=2D89988E852BC9C13776DACC558B82E413B262E869087BBEFC0D10A655635E5B "点击放大")
3. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/tQfH8xJWQ4SxEPvN2t69Tg/zh-cn_image_0000002575045065.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=06437DD17B8F4A2C037AFAEB45A5BD14BD4A9CA597DA800AEF8F8F250ED6263C "点击放大")
   * 名称：MCP工具名称，如everything、time。
   * 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
   * 启用状态：工具是否已启用。
