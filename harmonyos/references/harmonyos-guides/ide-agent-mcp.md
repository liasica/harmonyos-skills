---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp
title: 模型上下文协议（MCP）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 模型上下文协议（MCP）配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:14+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:0f3d6fa165089fe7b6e06fc0f7ae6606100140feda6d928562770a607b4b85c7
---

## 功能介绍

模型上下文协议（Model Context Protocol，简称MCP）是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置MCP。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，支持从MCP市场添加MCP工具。

### 使用约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

* npx：依赖于Node.js，建议使用Node.js的LTS版本。
* uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/sX1sBZjrTIuq80SDBkVilA/zh-cn_image_0000002561752883.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=9ED20833BCA2E5CAC772AD356D4E254B91E60A2CFD80F8CE67C4759865798C28)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/SazIFNdbQTijmDj3pxI5Sg/zh-cn_image_0000002530912934.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=9375253DE35454CE4D21D8233D0EA1E9AA32AD018222CBC6FE1BA0E5F8786E67)按钮，选择**MCP**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/grHDIhhqTQqspBMuoLw_ug/zh-cn_image_0000002575045063.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=28B421A414414418AB19E591A0370B3EF296A7A468F52BC3B8CF9AA6D0ADD7C9 "点击放大")
2. 添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/uqkGbqj8Tk6p9MqHX9BFwg/zh-cn_image_0000002561832863.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=CCF4C2D6A81FF1C0521299DE965D2031820C2C499B05D959724D6091B145123C)按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP市场添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/1Xi6MSkbQS6levHmz5UtKw/zh-cn_image_0000002544364856.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=601668B94092C3EE57852F2C7765264183B6489D8696F257CA968E354F8ABA1A "点击放大")

   * **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

     说明

     MCP Server支持三种通信方式：Stdio 、Server-Sent Events (SSE) 和Streamable HTTP。

     Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/S_uoSBMCQRSoye9ixU8LnA/zh-cn_image_0000002544205206.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=4997870445B5D8801785E94C99DDC55E6365DD5B401C8104BF6C6DA21612E373 "点击放大")
   * **从MCP市场添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/FRFanQLERWyMqSO3pzsaRw/zh-cn_image_0000002530912938.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=06A906449DB1130C48FB95D491AD17355167653D1D8632D62282DC206346EB5E)按钮添加。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/HefGwXdjRL6C0XA_RZtVeQ/zh-cn_image_0000002574885083.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=1F6DC34D4922AC2E7DBA95179699CB26A28F9295D2315695D41C863D0DEA64B2 "点击放大")
3. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/wMiqWvzyRdmnYlEKs4bx_w/zh-cn_image_0000002575045065.png?HW-CC-KV=V1&HW-CC-Date=20260429T054512Z&HW-CC-Expire=86400&HW-CC-Sign=C9C7D18F485113A50AA6D4A9DA998831F4A2F542AEF22B87022548CD349BD3EA "点击放大")
   * 名称：MCP工具名称，如everything、time。
   * 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
   * 启用状态：工具是否已启用。
