---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-models
title: 配置Models
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 操作指南 > 配置Models
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:51+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:252dd9ae932c443ec26237891d7124716ed30befef6e2a1f30fb3e5f47c94e83
---

DevEco Code支持通过服务提供商添加和手动添加第三方模型，为自定义Agent提供多样化的模型选择。

## 操作步骤

1. 可通过如下三种方式进入配置页面：
   * 点击菜单栏**File > Settings > AI > Models**（鸿蒙电脑版DevEco Code为**File > Settings > Extensions > AI > Deveco Code Setting** **> Models**）。
   * 点击DevEco Code界面的Menu中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/0qbI16XeR8mhCmwQIYz35g/zh-cn_image_0000002808766641.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9EB8BD1AB8A3BCE55BAB7F35483FC49C2DA208DE307EDDABC92689AF246A91D)Models卡片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/HSEHOnIaTKCLpV_AFuNt4w/zh-cn_image_0000002808766643.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=434E05FC82F17FFB6CECFE41094AFBE35E9F3869DE4283FEBAEDFC4BB055A838 "点击放大")
   * 在输入框的模型下拉框中点击**Add model**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/_WfNcYC7T0eHq238uVaINQ/zh-cn_image_0000002808766645.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E461AB67FD2D84A77EAD30284405254B388F9B3DE8D8AB5B9C21CACA055AEF3 "点击放大")
2. 进入配置页面后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/KVb2QNHvQ-uVAAR87c3-dQ/zh-cn_image_0000002808886721.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FE8235A45311E0F385EAFCBD34C0F42B0E403C65A877DF42326A0C46EE47C04 "点击放大")添加模型，支持通过服务提供商添加和手动添加。
   * 通过服务提供商添加。DevEco Code已预置主流模型服务提供商的配置信息，选择服务提供商，填写对应API Key，选择要对接的模型，点击**Confirm**即可快速接入。
     + **Provider**：必填，服务提供商名称。
     + **API Key**：必填，模型的访问密钥，在服务提供商网站申请。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/qPeZgjOfQcyTOBK_2hHm8Q/zh-cn_image_0000002808886725.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=734E0328DCB7689686D12622C8A64F5E3A367F321ABBAE58FD100EF1E183978E "点击放大")
   * 手动添加。填写Provider Name、URL、Protocol、API Key、model-id、model-name后，点击**Confirm**，模型将被添加到列表中。同时，点击**Add Model**可添加多个model-id和model-name。
     + **Provider Name**：必填，服务提供商名称。
     + **URL**：必填，模型的访问地址。
     + **Protocol：**必填，模型的协议，协议类型包括：OpenAI Compatible、OpenAI、Anthropic。
     + **API Key**：选填，模型的访问密钥，在提供商网站申请。
     + **model-id**：必填，模型ID。
     + **model-name**：选填，模型名称。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/uHaoGmyeRHytZV2PcEucfQ/zh-cn_image_0000002808886729.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=30AE7207C7E5E44E14D2F6E8BF87D490321A63D3F2871D6A265CA03627BF95C7 "点击放大")
3. 在模型设置页展示添加成功的所有服务提供商和模型，服务提供商名称为DevEco Code的模型列表是内置模型，当前内置模型为GLM-5.1和GLM-5.3。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/cdTLpL-mR0-ukjMts3dxhw/zh-cn_image_0000002808766647.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=D36522584A42EE5A78903E0B2D168AC5AEFA0628AE0A4A5F3E140BCE1FE06337 "点击放大")
4. 对添加的模型进行编辑或删除。
   * 对于通过服务商添加的模型，将鼠标悬浮或者点击服务提供商时，会显示删除按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Ax70KCs1T9GiGm1UePpyeA/zh-cn_image_0000002808886723.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=0AB936B20D095E32C6A9E1103ACDF8A836074F89CD60BF8B7E15695EDE209F11 "点击放大")

     同时，点击**Add model**进入配置界面后，支持通过**Reset**重置API Key，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/xP9vLjJnT7iDiNyGakuhTw/zh-cn_image_0000002808886727.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=56112952E627B9FC2FA3C01825B8380437671369FFA6E13DA4C2E813BB8E3669 "点击放大")
   * 对于手动添加的模型，将鼠标悬浮或者点击服务提供商和模型时，会显示编辑、删除操作按钮，支持编辑或删除服务提供商和模型，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/RrOOQWVaTTiKtD0MLRzz4w/zh-cn_image_0000002779567058.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=779CBC43B4A0BC3197237944A6086404F7BC268EE234D56408D2179525F7E93C "点击放大")
5. 添加完成后返回DevEco Code，在输入框的模型下拉框中选择已配置的模型，进行问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/URNVhg2dT0CzZZeU2zovrA/zh-cn_image_0000002808766649.png?HW-CC-KV=V1&HW-CC-Date=20261124T044251Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3BB6A50FFF79FB50A936F97CFEB2EEDE78F655AEE190E368CA16630B5005F99 "点击放大")
