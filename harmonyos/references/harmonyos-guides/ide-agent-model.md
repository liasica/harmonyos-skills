---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model
title: 模型（Model）配置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 使用AI智能辅助编程（不推荐） > 自定义智能体配置 > 模型（Model）配置
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:09+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:dc95242fe30b5b55c6f4031d80a8b1ceb986d2029f25fc5a79cc0b52c19e366b
---

CodeGenie支持通过Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

## 操作步骤

1. 点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/n2E_gmwNRqejwCE2wk_-Gg/zh-cn_image_0000002808766565.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=594A6E2F095C58E98E15E75CEB756ABC4B66E4BE4B1533EFDDFDD06C31667313 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/44RmpbuSSNCNZNeKlac53Q/zh-cn_image_0000002808766563.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E502247C368FAF091522377804480B3627498ACDE3EB52275D5DB2617D0A2E2)按钮，选择**Model**，进入配置页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/LiYPhKiMR-iikbgBfBsSRQ/zh-cn_image_0000002808886645.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5651586056E703B254DE816138E324C7CE4D789FB5498C7B40E173E0800FC07 "点击放大")
2. 点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/5dFItG8LSRevhdoBejDbcw/zh-cn_image_0000002779566988.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9F24458D5F9EA80AA2E7B473D65BAB61DC81E92BA71D236E69F4599C8A6D7FB "点击放大")按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加，推荐使用Service Provider方式。
   * 通过服务提供商添加。CodeGenie已预置主流模型服务商的配置信息，填写API Key即可快速接入。

     填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
     + **Name**：模型名称。
     + **Provider**：模型的提供商，可选项包括OpenAI、Gemini、DeepSeek、Alibaba Cloud、Z.ai。
     + **API Key**：模型的访问密钥，在提供商网站申请。
     + **Model**：模型的标识。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/wMOIRgzLQJWfdcfJ4q2bhQ/zh-cn_image_0000002808886647.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=34C74F25465C553794EC83AAB6640BE26BF00A20905A9C0B3EA61589CDB1D899 "点击放大")

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/N2gIhjoyTmi4fso-RoMt0Q/zh-cn_image_0000002779566986.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=8906E394B6940D794AAE07B1D142E386C77A45ACDD1C72F2D9B6D03A8DA15BA0 "点击放大")

     **说明** 

     配置说明、URL配置示例等内容请参考[通过URL添加模型](ide-agent-model.md#section1684210554158)。
3. 在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/NZjUJoXERQCxD92EWZKhyg/zh-cn_image_0000002779407008.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=7F67417E4F2E1540566B8182CE2DF3A9DFD660E220466F2F07FBB95E03374098)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/UrnBJIkqQRCyC3Kp1LiiQg/zh-cn_image_0000002808766569.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=DBC063F20E657C3FD20C5C5A0BD538641C49BE2803A0AC4DCFACDA5EBE2E3779)

* 添加DeepSeek模型（OpenAI协议）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/G8Cc6uiIR4eRX3cXzjd8zg/zh-cn_image_0000002808886649.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD37270E7279926516E215F848F80B11429176D01AB26A13AD81ECBBFE34103B)
