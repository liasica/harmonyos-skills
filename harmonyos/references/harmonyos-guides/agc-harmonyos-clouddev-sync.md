---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync
title: （可选）同步云端代码至DevEco Studio工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > （可选）同步云端代码至DevEco Studio工程
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:04+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:26c3c1a9941fe71a9c995044754d4d5050a5389e8f1b79af31ac606773648546
---

DevEco Studio还支持您将AGC云端当前项目下的代码同步至本地工程，包括之前从本地部署到AGC云端的代码、以及在AGC云端编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](agc-harmonyos-clouddev-sync.md#section588213529814)、[仅同步云数据库](agc-harmonyos-clouddev-sync.md#section474014335350)、[一键同步云侧代码](agc-harmonyos-clouddev-sync.md#section1198316575339)。

## 同步云函数/云对象

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

### 同步单个云函数/云对象

云函数/云对象部署到AGC云端后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1. 右击云对象目录，选择“Sync '*云对象名*'”。下文以云对象“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/1bRNfv-mSUSnC1fuGhKqHw/zh-cn_image_0000002214704461.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=B9A573C0201D49766D921BA0F54D8C529DDE2047F71C8A094CEDE32B125ABF48)
2. 在确认弹框中点击“Overwrite”，AGC云端的云对象“id-generator”将覆盖更新本地云对象“id-generator”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/AqStiJ7kQZmWfrOfT54xrw/zh-cn_image_0000002214704477.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=FF90B47232843702D3D93B0ADF55197D2047258643EE83F6D6E812B1CA76484E)
3. 等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。

   说明

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/apYZ8D2qT4ymcnG92nT_Xw/zh-cn_image_0000002179498228.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=38368CAFFC8A18743DD522AA18DE2226F714185BF4AB0FE8DA7BBDDB451A4549)

### 批量同步云函数/云对象

批量同步云函数/云对象即将AGC云端当前项目下的所有云函数/云对象同步至本地工程。

1. 右击“cloudfunctions”目录，选择“Sync Cloud Functions”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/l_YH1V4ySb2LgKKjWo-6vg/zh-cn_image_0000002179338512.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=9AF8B09E1D3910CC4AD84521B8A5F8F549614E82DF48C778C0BFC1DC62274D50)
2. 弹窗提示您本地工程下存在同名云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名云函数/云对象。
   * 选择“Overwrite”，AGC云端的云函数/云对象将覆盖更新本地同名云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/N7GGID4PQn2BMFMt-NJp6A/zh-cn_image_0000002214704441.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=9F275D874FB2ABAB1B845698175651768615FBC4E3D94F6A0DEB9EE4998BBD89)
3. 如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/I2TgWvaPSbeVqYa01_su9Q/zh-cn_image_0000002214704485.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=4AA6033412AFC40E78CD845A727E8808B9A3458F7A80831B5F04C3FF91231395)
4. 如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

   说明

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/ST7BD5jAQdGhjsKkLYo0TQ/zh-cn_image_0000002179338508.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=8791A26DD57899C8ECF9A818EB308A23A079B027FB42DD9A5BAACCE17BC7CC2B)

## 同步云数据库

说明

目前仅支持同步对象类型。

### 同步单个对象类型

对象类型部署到AGC云端后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1. 右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/A1Sd6lFOTvCIfeiVrGkAjw/zh-cn_image_0000002179498216.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=DDA8BD1ECC911B3065068BB234DDE630AB0E443F5CB8A1DF0972E4A6C7A2B627)
2. 在确认弹框中点击“Overwrite”，AGC云端的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/kVuDkyp5SGilvt_Uv6pwqw/zh-cn_image_0000002214704465.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=03A636C4F36443C912E40579E05A5DC425EC416FE7EBF79A30929F2B9D07BAE1)
3. 等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   说明

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8s9pVHKGQ4SSJf_PvyWZCQ/zh-cn_image_0000002214704445.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=B350B3F758213BC6A596DCD574A3A158FFA58F99D1B6E9DAE2E5451814D17DC2)

### 批量同步对象类型

您可以将AGC云端当前项目下所有的对象类型一键同步至本地。

1. 右击“objecttype”目录，选择“Sync Object Type”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Jrd-JYvuRNqoaoDyYc706Q/zh-cn_image_0000002179338532.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=26ABCEA44C92E3D54AA351059F9F8ABEAC0ABA624B9399D329C9630162822FF3)

2. 弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。
   * 选择“Skip”，同步时将跳过本地同名对象类型。
   * 选择“Overwrite”，AGC云端的对象类型将覆盖更新本地同名对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/upzNkbidTYihL8yO4u5rgQ/zh-cn_image_0000002179498208.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=BAA5FF016F4472ED2EFFCB90BE07CDE55C964EFAD66406F7067FBA739CB83254)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。

   如下图，“objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/0Z9AhlP_SI2DUlsWdYNPrQ/zh-cn_image_0000002179498196.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=4501FCBA79F477CAFBFB4274765E841134CA7B15AA984220980DA96EEEE84A38)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   如下图，“objecttype”目录下生成了“test\_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test\_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-*备份时间*.backup”。

   说明

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Ti5KR8-EToymzT8Cb1R3iA/zh-cn_image_0000002214704489.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=32186EA4A0B48135DA40E349D517DBCD8641E6B02E045912A969D5E491B40488)

## 一键同步云侧代码

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1. 右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/8gcFLA8RRTCVjVy6PFGprg/zh-cn_image_0000002214858849.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=F814A36565B7F79B4458512AEE95881D96A5C8F659EEFB04E632C412E3D920DA)
2. 弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
   * 选择“Overwrite”，AGC云端的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/P8-PlrYGRtiORGRzpmp1dA/zh-cn_image_0000002214858861.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=87B73760F1F96DE7D054DE654FCD7F97127401971469FBF59601594FCB0CEB51)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。

   如下图：

   * “objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zbCbgcnWQYq8zU3A-Y3k7Q/zh-cn_image_0000002179498236.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=683036E8C38271C798A79F9D4C53E905C0BD433872277CB20AED46D25A5C03FA)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。
   * 无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。

   如下图：

   * “objecttype”目录下生成了“test \_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test \_object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-*备份时间*.backup”。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

     说明

     后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/jiLFpqIXQjqQ64eCLynOBA/zh-cn_image_0000002179338516.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=6786C70E5258B80531323A662C1560A38808FF79A083B47EE1712849F520B2CE)
