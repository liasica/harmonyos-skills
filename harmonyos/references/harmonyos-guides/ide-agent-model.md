---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model
title: 模型（Model）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 模型（Model）配置
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b6ee4c1d3308e68c1d92b01a6783698c0228c29865ebfbd00140f415ecf90806
---

CodeGenie支持通过Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/yuki6Uq7TqS1KEAAmz6Y-A/zh-cn_image_0000002808766565.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=562416EB89FB11102E25F484F494D606ABE84DE06F14A78F8C8DFA61B96B50A7 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/qyLGwDXLSHiW2aFDE736Uw/zh-cn_image_0000002808766563.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6EA95B2D99A2BCD9B27172C608E8BA670A6359273B643CED7AE1AFD06501940)按钮，选择**Model**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/0gSQoKkwRJyp5kPX8lKpXg/zh-cn_image_0000002808886645.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=A03AABE8C3CD546231D1ED0B6A20E1517C2732AF9838B3FDAD670918E2C64A3C "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/P1PiBJx3QKyKdaovdMHjIw/zh-cn_image_0000002779566988.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=D94D54B96D67579EF063411C404705700B9DB5F15E4B44EDA9F7B21AEB9D41D7 "点击放大")按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加，推荐使用Service Provider方式。
   * 通过服务提供商添加。CodeGenie已预置主流模型服务商的配置信息，填写API Key即可快速接入。

     填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Provider**：模型的提供商，可选项包括OpenAI、Gemini、DeepSeek、Alibaba Cloud、Z.ai。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Aov9WryXQIWKXVkHKnI9fw/zh-cn_image_0000002808886647.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD3F111BBDCBBEC49D272E0ECC25DDF25249BC21B7A4EEC3A32FAA1E1908551B "点击放大")

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Y3SLQI0pQm2G92kVOuB-zA/zh-cn_image_0000002779566986.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDB6945549A0455471690D80EE9076D2FE406ADB8DE5CF86AE7FABC62CD1EA60 "点击放大")

     **说明** 

     配置说明、URL配置示例等内容请参考[通过URL添加模型](ide-agent-model.md#section1684210554158)。
3. 在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/tb3hZlPRR-q4W80IJ3lRxg/zh-cn_image_0000002779407008.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AF14E12416CBC1F067C48B4B71A343E20CF5ACB07F59FE9253FA94A91024433)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/Sqhq9bJkS5i5Q5WfQ7-YVg/zh-cn_image_0000002808766569.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=56A4DFE9582EC3A4033EB6355EA7E52219A96435840DA60E69031C94B5AE90DF)

* 添加DeepSeek模型（OpenAI协议）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Hcq7k-fSTuOmygAqjSmbtw/zh-cn_image_0000002808886649.png?HW-CC-KV=V1&HW-CC-Date=20261128T023448Z&HW-CC-Expire=31536000000&HW-CC-Sign=25BD1002C311AF76AC0D785E48B98E652E85E0C6D0E4C21D58D5E7626350751B)
