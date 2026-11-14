---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-models
title: 配置Models
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 操作指南 > 配置Models
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:22+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3430b9411537e75359ad1ebae827ac95e2bfb7f6d90758d304a2bc70e09fa017
---

DevEco Code支持通过服务提供商添加和手动添加第三方模型，为自定义Agent提供多样化的模型选择。

## 操作步骤

1. 可通过如下三种方式进入配置页面：
   * 点击菜单栏**File > Settings > AI > Models**。
   * 点击DevEco Code界面的Menu中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/HkOR9_zqR6i1bLEHhU96ig/zh-cn_image_0000002808766641.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=53544D35C24AB2EABAB59A65693A179BC30BB79CA6D24E768E45D8A28EE43161)Models卡片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/-FjTjdUNSNaPnr5Us65Glw/zh-cn_image_0000002808766643.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=08BC27B88BCE248A3D1347E15A3D4A1E6465758F1AE89C87FCF494DB21BB6538 "点击放大")
   * 在输入框的模型下拉框中点击**Add model**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/JkySLWsSSpq9w66qLcs2PA/zh-cn_image_0000002808766645.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=2693A321173C3486BA3D681AB4996E4E5C2163D0BC5D89F44CFF5277EC05A974 "点击放大")
2. 进入配置页面后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Kn5NcvudR-qPVeqdIXN1bQ/zh-cn_image_0000002808886721.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA6F7D84A44427A60E836A318554A1354406069DA6F6FDF161DC14D8CD20243B "点击放大")添加模型，支持通过服务提供商添加和手动添加。
   * 通过服务提供商添加。DevEco Code已预置主流模型服务提供商的配置信息，选择服务提供商，填写对应API Key，选择要对接的模型，点击**Confirm**即可快速接入。
     + **Provider**：必填，服务提供商名称。
     + **API Key**：必填，模型的访问密钥，在服务提供商网站申请。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/6Gcy477ZTFShGmb4AN5g0g/zh-cn_image_0000002808886725.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FCF7E92C47C953EF95BA833AACF973CB5B3E53D5E0630071C7CE83246C99606 "点击放大")
   * 手动添加。填写Provider Name、URL、Protocol、API Key、model-id、model-name后，点击**Confirm**，模型将被添加到列表中。同时，点击**Add Model**可添加多个model-id和model-name。
     + **Provider Name**：必填，服务提供商名称。
     + **URL**：必填，模型的访问地址。
     + **Protocol：**必填，模型的协议，协议类型包括：OpenAI Compatible、OpenAI、Anthropic。
     + **API Key**：选填，模型的访问密钥，在提供商网站申请。
     + **model-id**：必填，模型ID。
     + **model-name**：选填，模型名称。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/l3EXnQ4SSqCeZGdZbEFswQ/zh-cn_image_0000002808886729.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=0720A2CB4603D3A010D9713382EDD6A6959E82858D1AA0825D1F31992371AF85 "点击放大")
3. 在模型设置页展示添加成功的所有服务提供商和模型，服务提供商名称为DevEco Code的模型列表是内置模型，当前内置模型为GLM-5.1和GLM-5.3。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/6En3dnPsRaKtt0m36BrZTA/zh-cn_image_0000002808766647.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECBD2786CF9CD4290FA2B1577F811E3921FA92EE2F110D234CD1CCF03532CC6F "点击放大")
4. 对添加的模型进行编辑或删除。
   * 对于通过服务商添加的模型，将鼠标悬浮或者点击服务提供商时，会显示删除按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/hTUwd9Z5TBaO57zRBH4f5A/zh-cn_image_0000002808886723.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=137AA1AFE9C2F4341EA5318DD68EBCE6F2610BE4E4ABC0BC55D0C088C21C5DA4 "点击放大")

     同时，点击**Add model**进入配置界面后，支持通过**Reset**重置API Key，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/vzy6HlFoTQq7mevOVpwSuA/zh-cn_image_0000002808886727.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=339A1B6CFF9C1456FF5F56D3FBFDE4480EF956B246508E61D1A1DC006F6EED05 "点击放大")
   * 对于手动添加的模型，将鼠标悬浮或者点击服务提供商和模型时，会显示编辑、删除操作按钮，支持编辑或删除服务提供商和模型，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/maMVwJOdS8usRMDSHZk1hQ/zh-cn_image_0000002779567058.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7856726D0EBC655B4E4876D572646072B02AEFD294A35B89C10FC740D94206C "点击放大")
5. 添加完成后返回DevEco Code，在输入框的模型下拉框中选择已配置的模型，进行问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/NJZ3ljqXS52u7OiBlOxvAw/zh-cn_image_0000002808766649.png?HW-CC-KV=V1&HW-CC-Date=20261114T004733Z&HW-CC-Expire=31536000000&HW-CC-Sign=C0C31EB506D71AD50FA4CFA8C5E218EA87091D05741A6D774F52D8ED3FD7C657 "点击放大")
