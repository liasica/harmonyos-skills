---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-models
title: 配置Models
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 操作指南 > 配置Models
category: harmonyos-guides
scraped_at: 2026-11-28T10:35:01+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:48366cffe634b475164ac4023eea335b08f9545dea814a3f33a11748f7930f63
---

DevEco Code支持通过服务提供商添加和手动添加第三方模型，为自定义Agent提供多样化的模型选择。

## 操作步骤

1. 可通过如下三种方式进入配置页面：
   * 点击菜单栏**File > Settings > AI > Models**（鸿蒙电脑版DevEco Code为**File > Settings > Extensions > AI > Deveco Code Setting** **> Models**）。
   * 点击DevEco Code界面的Menu中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/BPb8ftXFQcSQsPiAipuqBA/zh-cn_image_0000002808766641.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=01857CB1874F8CB7208B2CEFA3207EC8D9E0FD74EB2D8F5169E5FDE68ECD16A2)Models卡片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/JKQwf7ftQBe0_NyK-gKUAw/zh-cn_image_0000002808766643.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=56BD219C9B359C3C9D6E5777CF1D0BE87A6E3079A545F76D12EFD0518445FD12 "点击放大")
   * 在输入框的模型下拉框中点击**Add model**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/qFvJ2rlvRhGvdFu1XKvMow/zh-cn_image_0000002808766645.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C894FB5B84D8FC03C202B14D84A0B0FF7D7092CE2DB4DB97B05EE8CFDF07965 "点击放大")
2. 进入配置页面后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/hUYJf9ynT6u1cF0GO288Jg/zh-cn_image_0000002808886721.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=30D0E3324C45E980E5E4341D468448D528961CD4973CB4D1EFC0B1D1950AC352 "点击放大")添加模型，支持通过服务提供商添加和手动添加。
   * 通过服务提供商添加。DevEco Code已预置主流模型服务提供商的配置信息，选择服务提供商，填写对应API Key，选择要对接的模型，点击**Confirm**即可快速接入。
     + **Provider**：必填，服务提供商名称。
     + **API Key**：必填，模型的访问密钥，在服务提供商网站申请。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/4rnkQZ84SR-pFyponQx3Dw/zh-cn_image_0000002808886725.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=8ECA1025130690601BE5FCF24D3E2D92AE2E8C5F2486D067D3142F10541B88C8 "点击放大")
   * 手动添加。填写Provider Name、URL、Protocol、API Key、model-id、model-name后，点击**Confirm**，模型将被添加到列表中。同时，点击**Add Model**可添加多个model-id和model-name。
     + **Provider Name**：必填，服务提供商名称。
     + **URL**：必填，模型的访问地址。
     + **Protocol：**必填，模型的协议，协议类型包括：OpenAI Compatible、OpenAI、Anthropic。
     + **API Key**：选填，模型的访问密钥，在提供商网站申请。
     + **model-id**：必填，模型ID。
     + **model-name**：选填，模型名称。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/OpiFTmFtQdCUmaBPYDSz6Q/zh-cn_image_0000002808886729.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B6BF47549AAAF7B87A1E41939584B270A0857A1F7916CE2805A5A3DE33E25B5 "点击放大")
3. 在模型设置页展示添加成功的所有服务提供商和模型，服务提供商名称为DevEco Code的模型列表是内置模型，当前内置模型为GLM-5.1和GLM-5.3。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/61A6sj1kQKGt-5ECMoxLrQ/zh-cn_image_0000002808766647.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=59C0D9FD4D2C4F7888A00A9CDA59C09D90EABBB9DB724078B980D94B9D8D706E "点击放大")
4. 对添加的模型进行编辑或删除。
   * 对于通过服务商添加的模型，将鼠标悬浮或者点击服务提供商时，会显示删除按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/4iUqKk-SQPC2kMXvfOCw3Q/zh-cn_image_0000002808886723.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C1135CFEEF34F0C31165F9F4F67341089443284CB522BA290099DFE4FA09D70 "点击放大")

     同时，点击**Add model**进入配置界面后，支持通过**Reset**重置API Key，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/uFDUoRBnTfC1UzglF6ZVNA/zh-cn_image_0000002808886727.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=71298A4AF1D9A4998AD685FF7D86812E68C84F0A250EE5F10F51C1491FC60C0B "点击放大")
   * 对于手动添加的模型，将鼠标悬浮或者点击服务提供商和模型时，会显示编辑、删除操作按钮，支持编辑或删除服务提供商和模型，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Dd2cZe42R7Oz-bn3OWnNzg/zh-cn_image_0000002779567058.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=30C3D811E616F64A2ABEB20A2344664BBA4D74DC756F50E69EA9E1C7BFEE7A96 "点击放大")
5. 添加完成后返回DevEco Code，在输入框的模型下拉框中选择已配置的模型，进行问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/OEJDOZdxTwOvotH8JBxVaw/zh-cn_image_0000002808766649.png?HW-CC-KV=V1&HW-CC-Date=20261128T023500Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F36F7FAE500D00D821EABDA549D7CC626752A6ACD95B012A1C29A1F8696B417 "点击放大")
