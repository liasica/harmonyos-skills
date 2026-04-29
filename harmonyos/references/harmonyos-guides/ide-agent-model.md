---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model
title: 模型（Model）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 模型（Model）配置
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d5a2fab7ce4d593787e188514538f593f422b879b4a97dae3625d7fd43e26b91
---

CodeGenie支持通过Anthropic-API、Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Anthropic-API、Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/BNoj6NzAR-GUVRA3LusliQ/zh-cn_image_0000002530753022.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=9C9A24AE3AF9ACAF675D9CF6325761253B2CB39E01E6816C3AA6388CDD2D820B)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/ajtYeux9QxSQIsR9FbOjaw/zh-cn_image_0000002561832939.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=7E1F1EB1AD0699357FC5D4F815CDF5356B576CC7FEAA0D37686A681B7D92B8E3)按钮，选择**Model**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/M7CBOg8CR8CA5DjRQg_eUw/zh-cn_image_0000002574886089.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=97554C880369FB10792418D25947E2550485CB81A7280E42A4EB43D88FB3C7DF "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/I8OZ2EenT1KUW2yDXIqs7g/zh-cn_image_0000002561752963.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=1C6C27B310129C7EFBCD01373DEF9C177566B215960DDB3E5345FD332AB9CA71)按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加。
   * 通过服务提供商添加。填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Provider**：模型的提供商，可选项包括OpenAI、Gemini、Anthropic、DeepSeek、Alibaba Cloud、Z.ai。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/azqTx_4TRnGPlForNVecGg/zh-cn_image_0000002544365866.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=890DC5FBCE4278764743966FACC898D3F8C2A2B1091B46515DA57F2C04E3ADF6 "点击放大")
   * 通过URL添加。填写**Name**、**Protocol**、**Url**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Url**：模型的访问地址。
     + **Protocol**：模型的协议，可选项包括OpenAI、Anthropic、Gemini、Ollama。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/WDoTL22CRKeCzs_87Yrz-Q/zh-cn_image_0000002575046075.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=FC6AABD1CB340BD7F19021626B422941DDB2DB04F95F789308B0D1EEF0D7A8CF "点击放大")
3. 在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/kwRRyTZYTsmfbJ5DBXo_DQ/zh-cn_image_0000002544206214.png?HW-CC-KV=V1&HW-CC-Date=20260429T054513Z&HW-CC-Expire=86400&HW-CC-Sign=629FCB87F232FE34A937FB9901C4325BB57F491C8FA6007E6FB971B4E7548435 "点击放大")
