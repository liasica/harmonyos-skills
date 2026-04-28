---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model
title: 模型（Model）配置
breadcrumb: 指南 > 使用AI智能辅助编程 > 自定义智能体配置 > 模型（Model）配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4501b7155daf2c657865397093a4a51e20d62b4498eff6f5f1444d75b8d369dd
---

CodeGenie支持通过Anthropic-API、Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Anthropic-API、Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/wRu7_T_xRbKxibjsOhwZcg/zh-cn_image_0000002530753022.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=4CC66537192FF2807B852D5F408B639B3984A89C2D9D9762C87850637CBBC9DB)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/lK3WGWtdQ2esLx6Z8HdgDw/zh-cn_image_0000002561832939.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=C2511A0BAEAC5FE9F7EE68D9AB090913492C8C20CFAFE49FFB56A2DCBEA7CAEF)按钮，选择**Model**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/Lt2XrV50SHS8oW1OUqLcWA/zh-cn_image_0000002574886089.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=FFC6FD52E07598451BBD06FF1A2102C6925CD9DCBDA75564FF478E7CF9B750C8 "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/31x5kfxgSaa-LyUlFiyZcQ/zh-cn_image_0000002561752963.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=D979079B179F46D5ED2275C8EF5C0815BA011AB78B637D3935ED17F6BC8E3A0E)按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加。
   * 通过服务提供商添加。填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Provider**：模型的提供商，可选项包括OpenAI、Gemini、Anthropic、DeepSeek、Alibaba Cloud、Z.ai。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/sV4BMKLFRUKURs8uccDzEg/zh-cn_image_0000002544365866.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=7FAE7A39E60C6E74BC95CE4431BECBC96EF20A97ECA2C934BEB2B3E901ECDEB1 "点击放大")
   * 通过URL添加。填写**Name**、**Protocol**、**Url**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Url**：模型的访问地址。
     + **Protocol**：模型的协议，可选项包括OpenAI、Anthropic、Gemini、Ollama。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/PFVtqA6xQX-FHTPT4ziECw/zh-cn_image_0000002575046075.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=FE8E00966F83B5F7EA6E56B14C5CB32525DE81EDFE4D8A79A074BED3B51F17E9 "点击放大")
3. 在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/f7e_X_Z8TDKB-gJ0bFzrsA/zh-cn_image_0000002544206214.png?HW-CC-KV=V1&HW-CC-Date=20260427T235516Z&HW-CC-Expire=86400&HW-CC-Sign=8605AAC08EF833239F91CAACD7C368CA9FC04F47EA39D1ABCE192E567FC10938 "点击放大")
