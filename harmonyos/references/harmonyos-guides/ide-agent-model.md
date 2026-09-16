---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model
title: 模型（Model）配置
breadcrumb: 指南 > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 模型（Model）配置
category: harmonyos-guides
scraped_at: 2026-09-17T06:47:17+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:976de34c7377329a24959836b022f2b1ce7224cd296f60543fb0c9070918fd6c
---

CodeGenie支持通过Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/9CyJzhlSQ02KKRkmT7EX_w/zh-cn_image_0000002701822998.png "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Ke8zO4tvTW68lSUJYd8pBw/zh-cn_image_0000002701822994.png)按钮，选择**Model**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/OSxOPdWZQ2qq3rTgjZagIw/zh-cn_image_0000002701663074.png "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/TykFT5OJQE22W_xea3E9WA/zh-cn_image_0000002701663088.png "点击放大")按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加，推荐使用Service Provider方式。
   * 通过服务提供商添加。CodeGenie已预置主流模型服务商的配置信息，填写API Key即可快速接入。

     填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Provider**：模型的提供商，可选项包括OpenAI、Gemini、DeepSeek、Alibaba Cloud、Z.ai。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/l1YA-HWOQMmxUHL1l3v7Bg/zh-cn_image_0000002701663078.png "点击放大")

     不同Service Provider的API Key和支持的模型如下：

     | Provider | API Key获取地址 | Model示例 |
     | --- | --- | --- |
     | OpenAI | https://platform.openai.com/api-keys | gpt-5.3-codex、gpt-5.4、gpt-5.5、gpt-5.6 |
     | Gemini | https://aistudio.google.com/apikey | gemini-3-pro-preview、gemini-3-flash-preview、gemini-3-pro-image-preview |
     | DeepSeek | https://platform.deepseek.com | deepseek-v4-pro |
     | Alibaba Cloud | https://dashscope.console.aliyun.com | qwen3-coder-plus |
     | Z.ai | https://open.bigmodel.cn | glm-5 |
   * 通过URL添加。

     填写**Name**、**Protocol**、**Url**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Url**：模型的访问地址。
     + **Protocol**：模型的协议，可选项包括OpenAI、Gemini、Ollama。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/MU8o5o9SSaeYvbXy42lV3Q/zh-cn_image_0000002701823002.png "点击放大")

     **说明** 

     配置说明、URL配置示例等内容请参考[通过URL添加模型](ide-agent-model.md#section1684210554158)。
3. 在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/DKOmJBmLQFKbaClm5a2eeQ/zh-cn_image_0000002701663084.png)

## 附录

### 通过URL添加模型

**约束与限制**

* 暂不支持开启深度思考（Deep Thinking）功能和多模态图片处理功能。

**配置说明**

* 代理配置：为了避免代理问题造成的请求超时，将内网模型服务域名添加到[HTTP代理的No proxy for](ide-environment-config.md#section10369436568)中。
* URL：填写URL时，若URL中包含"/chat/completions"后缀，请删除该部分，CodeGenie在请求时会自动拼接。示例如下：
  + 原URL： https://api.deepseek.com/chat/completions
  + 填写为： https://api.deepseek.com
* API Key：填写模型的访问密钥时不需要添加"Bearer"前缀。示例如下：
  + 原API Key：Bearer sk-f9e98c\*\*\*\*\*\*8
  + 填写为：sk-f9e98c\*\*\*\*\*\*8

**配置示例**

* 添加本地Ollama部署的模型

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/n6sxLY2fT_qskd1pDbk8fA/zh-cn_image_0000002731382313.png)

* 添加DeepSeek模型（OpenAI协议）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/a2c_dCVwRhaOPga2T52v2A/zh-cn_image_0000002701823006.png)
