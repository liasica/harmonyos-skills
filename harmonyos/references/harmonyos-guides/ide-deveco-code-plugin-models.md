---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-models
title: 配置Models
breadcrumb: 指南 > DevEco Code > DevEco Studio Plugin > 操作指南 > 配置Models
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:55+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:035397be708f15403991801f5acb95dc0c1e7dcba57495098209be89b7675c44
---

DevEco Code支持通过服务提供商添加和手动添加第三方模型，为自定义Agent提供多样化的模型选择。

## 操作步骤

1. 可通过如下三种方式进入配置页面：
   * 点击菜单栏**File > Setti**n**gs > AI > Models**。
   * 点击DevEco Code界面的Menu中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/V86nrsPqSESHTSHL4BrTaQ/zh-cn_image_0000002776953474.png)Models卡片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/DHEQsi3iTXSF-hNAaC7pUw/zh-cn_image_0000002806334151.png "点击放大")
   * 在输入框的模型下拉框中点击**Add model**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/VSCV6n_0TXiMiLg97FPFXg/zh-cn_image_0000002806334247.png "点击放大")
2. 进入配置页面后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Hqmzs3UySNSuglCODTfkBQ/zh-cn_image_0000002806073199.png "点击放大")添加模型，支持通过服务提供商添加和手动添加。
   * 通过服务提供商添加。DevEco Code已预置主流模型服务提供商的配置信息，选择服务提供商，填写对应API Key，选择要对接的模型，点击**Confirm**即可快速接入。
     + **Provider**：必填，服务提供商名称。
     + **API Key**：必填，模型的访问密钥，在服务提供商网站申请。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/rR3n2pxwTza7UtiX2dP3vw/zh-cn_image_0000002806254593.png "点击放大")
   * 手动添加。填写Provider Name、URL、Protocol、API Key、model-id、model-name后，点击**Confirm**，模型将被添加到列表中。同时，点击**Add Model**可添加多个model-id和model-name。
     + **Provider Name**：必填，服务提供商名称。
     + **URL**：必填，模型的访问地址。
     + **Protocol：**必填，模型的协议，协议类型包括：OpenAI Compatible、OpenAI、Anthropic。
     + **API Key**：选填，模型的访问密钥，在提供商网站申请。
     + **model-id**：必填，模型ID。
     + **model-name**：选填，模型名称。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/qIxFcP3CQiG4jLx26EoQjg/zh-cn_image_0000002777015056.png "点击放大")
3. 在模型设置页展示添加成功的所有服务提供商和模型，服务提供商名称为DevEco Code的模型列表是内置模型，当前内置模型为GLM-5.1和GLM-5.3。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/BMd8CQDYSzuvPGtRTeLhOQ/zh-cn_image_0000002777015308.png "点击放大")
4. 对添加的模型进行编辑或删除。
   * 对于通过服务商添加的模型，将鼠标悬浮或者点击服务提供商时，会显示删除按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/4eMhw7opRj-MHaYrUaBynQ/zh-cn_image_0000002776855498.png "点击放大")

     同时，点击**Add model**进入配置界面后，支持通过**Reset**重置API Key，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ISU8BWa3T0W-eiQ9vW6Gcg/zh-cn_image_0000002806255321.png "点击放大")
   * 对于手动添加的模型，将鼠标悬浮或者点击服务提供商和模型时，会显示编辑、删除操作按钮，支持编辑或删除服务提供商和模型，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/J400X79JQF-k6Xo-7Us1iQ/zh-cn_image_0000002806335387.png "点击放大")
5. 添加完成后返回DevEco Code，在输入框的模型下拉框中选择已配置的模型，进行问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/7OUk6V-FSvqA7nxXjHKQEA/zh-cn_image_0000002776855856.png "点击放大")
