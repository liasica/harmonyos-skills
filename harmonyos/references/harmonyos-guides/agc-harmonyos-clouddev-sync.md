---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync
title: （可选）同步云端代码至DevEco Studio工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > （可选）同步云端代码至DevEco Studio工程
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:22+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:3b2807dc025d087073206f6e6fa6c9b539871a9692b620e56921122be231cbe0
---

DevEco Studio还支持您将HarmonyOS 开发者中心当前项目下的代码同步至本地工程，包括之前从本地部署到HarmonyOS 开发者中心的代码、以及在HarmonyOS 开发者中心编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](agc-harmonyos-clouddev-sync.md#section588213529814)、[仅同步云数据库](agc-harmonyos-clouddev-sync.md#section474014335350)、[一键同步云侧代码](agc-harmonyos-clouddev-sync.md#section1198316575339)。

## 同步云函数/云对象

**说明** 

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

### 同步单个云函数/云对象

云函数/云对象部署到HarmonyOS 开发者中心后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1. 右击云对象目录，选择“Sync '*云对象名*'”。下文以云对象“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/kb1bGgQeQ9GzyePBtwfHnQ/zh-cn_image_0000002214704461.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E8347D3F3DE4508820E74F455940AE66481274C653EC9214CA9205C9AFA1F4E)
2. 在确认弹框中点击“Overwrite”，HarmonyOS 开发者中心的云对象“id-generator”将覆盖更新本地云对象“id-generator”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/DXaCSsTWQcWytmxdJTc_ig/zh-cn_image_0000002214704477.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=30AAE51BD4B125DE733C1AB19B06A83241F21A8D3DFE26E1986F902D7EC7A957)
3. 等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。

   **说明** 

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/6PrGP_-VTzy8_2Gbpw3Nqg/zh-cn_image_0000002179498228.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3B581C8CC957E8507687B484D9237393B66425D2B5B63702A86989782286D2C)

### 批量同步云函数/云对象

批量同步云函数/云对象即将HarmonyOS 开发者中心当前项目下的所有云函数/云对象同步至本地工程。

1. 右击“cloudfunctions”目录，选择“Sync Cloud Functions”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/8GZhwEZ7RbSGk3bzQZUPEA/zh-cn_image_0000002179338512.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BDB5357305E78431ED213AD6346199EDC50C7B379892FC5B79808DB4F522725)
2. 弹窗提示您本地工程下存在同名云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名云函数/云对象。
   * 选择“Overwrite”，HarmonyOS 开发者中心的云函数/云对象将覆盖更新本地同名云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/DEFQ3AkPTs60lPQAX-afMQ/zh-cn_image_0000002214704441.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D6F77A388EDBD607AF9A14D424B02BD47ABD33AA82952DED7A8052A693156AC)
3. 如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/KoHuUKMtSWaztx6Ah1DwxQ/zh-cn_image_0000002214704485.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F90AFFA8F9B0B42C169106A80EF8A37C76B5F88B37950EAF3F93CDD14B7D10D)
4. 如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

   **说明** 

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/lMLBBa5kTxu_Do9tqaEFmw/zh-cn_image_0000002179338508.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1633421DCA5EF4053289A863D1DB983C1784E4A6682A37A82C9A6E3896F4A29)

## 同步云数据库

**说明** 

目前仅支持同步对象类型。

### 同步单个对象类型

对象类型部署到HarmonyOS 开发者中心后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1. 右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/HFxvza2RTN24290eGGqnPg/zh-cn_image_0000002179498216.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A5E0D41C0A054F809D3BC4FC95729557C38F6AE70713D24F57C4950BFFDE084)
2. 在确认弹框中点击“Overwrite”，HarmonyOS 开发者中心的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/hEhPSRZ7QNGEae7qkXlJjw/zh-cn_image_0000002214704465.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD728490569687B2898F84AE3B35B093D3F01BD60788AA2DC20F62EEE396DFA2)
3. 等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   **说明** 

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/lGUfVwFQSWurDYkWaAKpfQ/zh-cn_image_0000002214704445.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B9A6D069DF62EB27E4D8720464704B4D5EE657573DEB3C0BB97F5E9C68E1A27)

### 批量同步对象类型

您可以将HarmonyOS 开发者中心当前项目下所有的对象类型一键同步至本地。

1. 右击“objecttype”目录，选择“Sync Object Type”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/kSJvW0Z9QuWXWN89gMr62Q/zh-cn_image_0000002179338532.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE00353AE035E6435D43EFD70462DC4CE6491E362D3355DFCC8A357C81F6ED76)

2. 弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。
   * 选择“Skip”，同步时将跳过本地同名对象类型。
   * 选择“Overwrite”，HarmonyOS 开发者中心的对象类型将覆盖更新本地同名对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/RYZ_YdQbSQahSXVJSQ5StA/zh-cn_image_0000002179498208.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=49DA8A8D439D522108A9C0AF6BE0E66CF2CB7328442CDE0406503301F5867EF2)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。

   如下图，“objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/d7x1zOSpSdmiCBQE82ti8w/zh-cn_image_0000002179498196.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C12C2F4893DF84A6A36C7DCF5BE6B288DD6254AFCC486E3249B4F1FF57AC3650)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   如下图，“objecttype”目录下生成了“test\_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test\_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-*备份时间*.backup”。

   **说明** 

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/pOLMWEoPQ2Woca-xzXFH6Q/zh-cn_image_0000002214704489.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4803BBA9BEE3F31EC5C44A3E6F290CB5B5C07A003A29652C0694CC9600071B1)

## 一键同步云侧代码

**说明** 

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1. 右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/1clT5O_aRLSwumhBzJvbTg/zh-cn_image_0000002214858849.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E6DA19DB41ABBE4C8D2380477130CDE64165CC394F4F97C5219D3C0B2A19D77)
2. 弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
   * 选择“Overwrite”，HarmonyOS 开发者中心的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Lj8_e2pHRjC9J_bLXm7NZw/zh-cn_image_0000002214858861.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=82DF4374B594B2E62527E9D5D698DB9DCB6F060AF133449194D1DC2F495B63C8)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。

   如下图：

   * “objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Vl7c5sXVSDed5erk4QPYAA/zh-cn_image_0000002179498236.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=65052A9004EA28F5AEA041643CD9AA2B209BB2957984D529FFD435B2889DE366)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。
   * 无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。

   如下图：

   * “objecttype”目录下生成了“test \_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test \_object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-*备份时间*.backup”。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

     **说明** 

     后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/utG6VXivSMOntCz6ZeGESw/zh-cn_image_0000002179338516.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C59F9BAD4C35F53B8C356691D24633DA0824C1AD6ADBF1F8AA581E69D1EDF398)
