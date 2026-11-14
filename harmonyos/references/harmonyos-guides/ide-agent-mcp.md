---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp
title: 模型上下文协议（MCP）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 模型上下文协议（MCP）配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:e401f36cccca87b78d9b07901205371db5abeaee83728077e43c061cfd1ec8b4
---

## 功能介绍

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置模型上下文协议（Model Context Protocol，简称MCP）。MCP是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，以及支持从MCP Market添加MCP工具。

### 使用约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

* npx：依赖于Node.js，建议使用Node.js的LTS版本。
* uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/7bkHxJ7qTu27gVLKEiKOsA/zh-cn_image_0000002779566794.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F165FAF4BBDCDB1BF03688D1F053147E1F97D6FC31C55D4BD3BF20814BAFA4F "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/nbjH3qbOSruYU3vCy57t2g/zh-cn_image_0000002779406806.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEA7AFB0B14A8C16AA59B28F5B1A6E8AD07E9A30DDAA52F445E9AC0B8825278B)按钮，选择**MCP**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/HDGu_xbjSVK0I-Ax9ADZEA/zh-cn_image_0000002779406816.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=38508435250CDA0955A777DF669EE2341D9595D39EF072301B49106DCCD74AC5 "点击放大")
2. 添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/yM0Lcy3vQYm0_0OKSouZ0Q/zh-cn_image_0000002779566792.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=48724A322BBEFCF46C34B04D1B004CA173E100E5FB056A32106667C3EBB750B0 "点击放大")按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP Market添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Xnn-8Z8XReu-uAbPPOADbg/zh-cn_image_0000002808766381.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=7094C131C8D236713B2C12B042FB635F39D9A97BB2619C656ECAFDEA87868267 "点击放大")

   * **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

     **说明** 

     MCP Server支持三种通信方式：Stdio、Server-Sent Events (SSE) 和Streamable HTTP。

     Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/6gxs8L52QQ2U1LshNK8PMw/zh-cn_image_0000002808886459.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=4978FF2F1367BB2149CA534EE78B388866ED803E904BA3DDB6C66BBBF48F3585 "点击放大")
   * **从MCP Market添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/pf04XspeRS2oXePy8z18cQ/zh-cn_image_0000002779406814.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBE261D9E7653DB617234C529D1C5B1DBDC8964BFC0EDC460AA791ED940E79D3 "点击放大")按钮添加。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/gg3H8LGcSQuFV0I3OS-QQg/zh-cn_image_0000002779566800.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC73639AA17F01523AE71F1D9745F865D42AB4C3468574C22E093E77417C0A14 "点击放大")
3. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/ju9QfU5GQTCuadnJ6HHdEA/zh-cn_image_0000002779406820.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=42C33E83FF24821A9C195DA882C633FEC816808645DEB93FC9EC1905AC7E9E7E "点击放大")
   * 名称：MCP工具名称，如time。
   * 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
   * 启用状态：工具是否已启用。
