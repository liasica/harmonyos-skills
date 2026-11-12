---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp
title: 模型上下文协议（MCP）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 模型上下文协议（MCP）配置
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:b30cda28ad57c0442adb9d3dc8d2772c9fac5d1c77cfcad50210490d458c590c
---

## 功能介绍

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置模型上下文协议（Model Context Protocol，简称MCP）。MCP是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，以及支持从MCP Market添加MCP工具。

### 使用约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

* npx：依赖于Node.js，建议使用Node.js的LTS版本。
* uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/NAdhUuFvRtC6SZ1vh-TXAA/zh-cn_image_0000002779566794.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=890295C365661B601032A4322F5B5D67A32BADADF3073FEAB26C92218FFFA7B1 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/YJP-4kZlRq-zH01-tpMsgA/zh-cn_image_0000002779406806.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFA2BDCAB1B14A33F7F4AA3C6A41026EDE0930CB915D12479E29B8437CD89DD9)按钮，选择**MCP**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/5gHJP6AhRoS1X6Iy59d9eQ/zh-cn_image_0000002779406816.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF6276A4F113AF21138FB1C633C2E2A9F85D7A0BBBA9528832D34F722CD55E7F "点击放大")
2. 添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/17DzSK8TSiapcOxVfIleRg/zh-cn_image_0000002779566792.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=30644CD288EF95E1E99882BAA9B7E2610D2BFFA4D4E7E29131CED713F358560A "点击放大")按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP Market添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/GH_pyHDpT_ignd3xw81VfQ/zh-cn_image_0000002808766381.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=25FCCCEE97BE2957EF54893E0ECE3A91BCE9907198E1C8643B5C01ECEF807B48 "点击放大")

   * **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。

     **说明** 

     MCP Server支持三种通信方式：Stdio、Server-Sent Events (SSE) 和Streamable HTTP。

     Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/trwPvBe9QS-8U5wbatByvQ/zh-cn_image_0000002808886459.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEE6B99E25978545002896521DDE968DDCB58718DC82C8A1FF0CCF605C02BF08 "点击放大")
   * **从MCP Market添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/rv-LfvhxTfepu1636bsJMw/zh-cn_image_0000002779406814.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=724EE2DF5565D047B7AF3FC06EA5A747F10DA2E22007228571DDD758FE0C5832 "点击放大")按钮添加。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/B8R_S2hWQIiWEtoYm2Ib0Q/zh-cn_image_0000002779566800.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A3BFC4CED0E2B06B20A0665FDFBE16002255726C77C820D3696ECB7FBE0AE51 "点击放大")
3. 在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/P-kdc3opQ_-vomFTY6O0-g/zh-cn_image_0000002779406820.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=667DE5B125A974D2163407E7E823355B1ED74B6BAF8A19F1754D5E06AF96AB30 "点击放大")
   * 名称：MCP工具名称，如time。
   * 连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
   * 启用状态：工具是否已启用。
