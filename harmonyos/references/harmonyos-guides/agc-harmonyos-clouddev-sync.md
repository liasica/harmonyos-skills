---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync
title: （可选）同步云端代码至DevEco Studio工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > （可选）同步云端代码至DevEco Studio工程
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:8529f1f0c31616d44fd6c491ae0c34b9f478650fb338ad7c915ac112949f8783
---

DevEco Studio还支持您将HarmonyOS 开发者中心当前项目下的代码同步至本地工程，包括之前从本地部署到HarmonyOS 开发者中心的代码、以及在HarmonyOS 开发者中心编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](agc-harmonyos-clouddev-sync.md#section588213529814)、[仅同步云数据库](agc-harmonyos-clouddev-sync.md#section474014335350)、[一键同步云侧代码](agc-harmonyos-clouddev-sync.md#section1198316575339)。

## 同步云函数/云对象

**说明** 

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

### 同步单个云函数/云对象

云函数/云对象部署到HarmonyOS 开发者中心后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1. 右击云对象目录，选择“Sync '*云对象名*'”。下文以云对象“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/oyHVZk8nRguvVkGi3wnAQQ/zh-cn_image_0000002214704461.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A63DFFC69B7C0E62873D1E862A3E7221662CBFB2B4673F9E22F90E1CA7D34143)
2. 在确认弹框中点击“Overwrite”，HarmonyOS 开发者中心的云对象“id-generator”将覆盖更新本地云对象“id-generator”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/c51BdsFcQfKZA2xJhbssOA/zh-cn_image_0000002214704477.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=0958C1DB5532188C9AFA1DC1CF5B8FB6637A8DC2ACC7E977C6D9926E2B38421A)
3. 等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。

   **说明** 

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/ifYJO9cCSGaMUhlhsJN0eQ/zh-cn_image_0000002179498228.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E74A52848738758C183CBCF74726E9ADDA4D1AD84CDD0F034B08191040864189)

### 批量同步云函数/云对象

批量同步云函数/云对象即将HarmonyOS 开发者中心当前项目下的所有云函数/云对象同步至本地工程。

1. 右击“cloudfunctions”目录，选择“Sync Cloud Functions”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/Zus566EBRnmmSxOy4uD0ww/zh-cn_image_0000002179338512.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFC865CC836BE32CDBB88032DD4EC53D4F4E23E6CD20E93E116206BF9157F379)
2. 弹窗提示您本地工程下存在同名云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名云函数/云对象。
   * 选择“Overwrite”，HarmonyOS 开发者中心的云函数/云对象将覆盖更新本地同名云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/mn0hGDXpRqa9fjsuUVc-Jw/zh-cn_image_0000002214704441.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C25473A1F7D71B11B5F8EB83A05D097AD74629B3A664271226AF3B1E1AEFCB1A)
3. 如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/HO3F-9bARzWEx3XYMUIAKg/zh-cn_image_0000002214704485.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E707B9B21E766F053F71DB20B31C3D44DF79B6EACE2B4FEFCF303DAB538C4761)
4. 如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

   **说明** 

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Sz0n1VT9SxSWvu71v4MABw/zh-cn_image_0000002179338508.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=28569990783E832AC488F99911C1C2CB5A12A0AD4E7139DA8B0D7991A61ABB54)

## 同步云数据库

**说明** 

目前仅支持同步对象类型。

### 同步单个对象类型

对象类型部署到HarmonyOS 开发者中心后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1. 右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/Uvm8rwRmQxCkz9IBax-42A/zh-cn_image_0000002179498216.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B94F3C42297784853724B5BB006EB81230A492C0CA93CB8380E0B181373C5EC)
2. 在确认弹框中点击“Overwrite”，HarmonyOS 开发者中心的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/tkSiTPbgR0OMKxEHvAUiGA/zh-cn_image_0000002214704465.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A957A5D24CBB91CA296304970B171CD14F17743A86B6E100CD494121F9734E1)
3. 等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   **说明** 

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/TzwU-GpIT222ZcY-2OccLQ/zh-cn_image_0000002214704445.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8D8C86C89BF7CFEF3CCC039B0AA28577C36A3F8177BFF97DB6AC25006D70D86)

### 批量同步对象类型

您可以将HarmonyOS 开发者中心当前项目下所有的对象类型一键同步至本地。

1. 右击“objecttype”目录，选择“Sync Object Type”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/QWB3iQOKT6y0h_1pQAltyQ/zh-cn_image_0000002179338532.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BF3B638020BCF329746B5B68FF4DF93F0BC32FD24B07CDDC0359301F34722F4)

2. 弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。
   * 选择“Skip”，同步时将跳过本地同名对象类型。
   * 选择“Overwrite”，HarmonyOS 开发者中心的对象类型将覆盖更新本地同名对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/W73wZzMFQieLWcbl102UgQ/zh-cn_image_0000002179498208.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A66FBB5AB038761DC8245B8645625399485F4905D48E75B09E6A57A301BA4B9B)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。

   如下图，“objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/SHih5bc7R1i9qSAAGrMrNA/zh-cn_image_0000002179498196.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4625923ED2D1170587B03FDF4E8D1919A8A9B629C927CE12269D1EBAB589DDBC)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   如下图，“objecttype”目录下生成了“test\_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test\_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-*备份时间*.backup”。

   **说明** 

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/c7pPQIUdShCMg1lYAWllnA/zh-cn_image_0000002214704489.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2116EEC9075B1C21526BCD0942FBBEE2E8DF14C8AEE6A7A750F307267A558933)

## 一键同步云侧代码

**说明** 

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1. 右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/myD8XGThTgKEqHAOs5vxpA/zh-cn_image_0000002214858849.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4624D15D7CE44896423020CB2F5182CC5802C45A13FEC9823D67CADFE6080C3E)
2. 弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
   * 选择“Overwrite”，HarmonyOS 开发者中心的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/MeI7KKZVSs20a4CGpH7fKw/zh-cn_image_0000002214858861.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=28BF6F5ABD6D1FF9478BFA1DAECDDA99A7B4099110400C3A490B16303CA3EE5D)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。

   如下图：

   * “objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/KCmVKhm_QcChUYrs-OWDtQ/zh-cn_image_0000002179498236.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CDF16977F4E00FCD7ABB14A568650634758302DCF553FC2DF5257A0856FDB8B)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。
   * 无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。

   如下图：

   * “objecttype”目录下生成了“test \_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test \_object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-*备份时间*.backup”。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

     **说明** 

     后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/9Q_5uVXNSau-ii5H_iqn4Q/zh-cn_image_0000002179338516.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DA40CE360A8AC581963DB5F25D839AD65ACBBC02076AF78F14CBC63E416A9F6)
