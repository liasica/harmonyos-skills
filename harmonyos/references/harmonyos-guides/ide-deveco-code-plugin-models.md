---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-models
title: 配置Models
breadcrumb: 指南 > DevEco Code > DevEco Code Plugin > 操作指南 > 配置Models
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f63de0cdc67dd8b036b3d623c518856a60056aff94042f6a3aa4b23b31169553
---

DevEco Code支持通过服务提供商添加和手动添加第三方模型，为自定义Agent提供多样化的模型选择。

## 操作步骤

1. 可通过如下三种方式进入配置页面：
   * 点击菜单栏**File > Settings > AI > Models**。
   * 点击DevEco Code界面的Menu中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/dxRaQR_WTe2fOPfJb-hXCQ/zh-cn_image_0000002808766641.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5B7B1AE6B3ED1FB6C2D5EFC93D9611F97FFF3BAB03360468EFDDACA4C1F6694)Models卡片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/HpfMMjIhTz-Tq3KJfI4oxQ/zh-cn_image_0000002808766643.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDCA2AB01FC0D0F4F593935C713854289C51D5115E736643611903C2C09137F1 "点击放大")
   * 在输入框的模型下拉框中点击**Add model**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/pKSwu9Z_QJuQmy-HpjlzTg/zh-cn_image_0000002808766645.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6464D25A8BBC0F42182A1F0BB4D487B9643656E165DBF8E47330B5108A683001 "点击放大")
2. 进入配置页面后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/B3jBlm45SPCRrxDLHofj1A/zh-cn_image_0000002808886721.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=496B45FDD3F0A19A161AE830C39E5FC4A15F1B6497BD1EEABE292A9669CD9D8B "点击放大")添加模型，支持通过服务提供商添加和手动添加。
   * 通过服务提供商添加。DevEco Code已预置主流模型服务提供商的配置信息，选择服务提供商，填写对应API Key，选择要对接的模型，点击**Confirm**即可快速接入。
     + **Provider**：必填，服务提供商名称。
     + **API Key**：必填，模型的访问密钥，在服务提供商网站申请。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Qy091QwDTt2dbFaoerw-eg/zh-cn_image_0000002808886725.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9784AE5233B4C10CB72E97CEE4EB1BA7271AC9B2D63B22F16CF996B0F307FAA0 "点击放大")
   * 手动添加。填写Provider Name、URL、Protocol、API Key、model-id、model-name后，点击**Confirm**，模型将被添加到列表中。同时，点击**Add Model**可添加多个model-id和model-name。
     + **Provider Name**：必填，服务提供商名称。
     + **URL**：必填，模型的访问地址。
     + **Protocol：**必填，模型的协议，协议类型包括：OpenAI Compatible、OpenAI、Anthropic。
     + **API Key**：选填，模型的访问密钥，在提供商网站申请。
     + **model-id**：必填，模型ID。
     + **model-name**：选填，模型名称。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/JdtWF_jdRMKKrZUkR3spRg/zh-cn_image_0000002808886729.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6BA17FE084E2498C5946BC0FCA5EA8BC8615773E58E42FDE3778C50F7FFA5948 "点击放大")
3. 在模型设置页展示添加成功的所有服务提供商和模型，服务提供商名称为DevEco Code的模型列表是内置模型，当前内置模型为GLM-5.1和GLM-5.3。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ZFVcTf-kT5SzHVurNUSMlQ/zh-cn_image_0000002808766647.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF19099518EFC8170384C34519D6BE883530AF8507FAB6942A97DC42FCE7409D "点击放大")
4. 对添加的模型进行编辑或删除。
   * 对于通过服务商添加的模型，将鼠标悬浮或者点击服务提供商时，会显示删除按钮。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/POPAM_TQQRabZSXCvRfXpw/zh-cn_image_0000002808886723.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A53AC1B3EBB5E1A5EA50B4CE0972425827071B294DC94FAD94D57127604460C "点击放大")

     同时，点击**Add model**进入配置界面后，支持通过**Reset**重置API Key，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/NAo7RHD4Ty2J7U7CSkf89g/zh-cn_image_0000002808886727.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D274A35203A94C21018B2F8F4788482CE4A2182CBECA4287F78CDA6FDB83EB7 "点击放大")
   * 对于手动添加的模型，将鼠标悬浮或者点击服务提供商和模型时，会显示编辑、删除操作按钮，支持编辑或删除服务提供商和模型，方便开发者管理。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/_J6Mj8eHQQ6RAZv16lTqEQ/zh-cn_image_0000002779567058.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=98D2644CB48919CFDDDDAD1930F0BA73AFBFE2186A817E9DA20D2C86E7EE5504 "点击放大")
5. 添加完成后返回DevEco Code，在输入框的模型下拉框中选择已配置的模型，进行问答。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/f4wstzP4QMKYrxWcATBSJg/zh-cn_image_0000002808766649.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=86119F4BD55F95B2625BBE6953B7FA6DA8C596DECAEE13C53468BE4877329227 "点击放大")
