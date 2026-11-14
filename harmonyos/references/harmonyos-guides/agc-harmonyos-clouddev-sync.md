---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync
title: （可选）同步云端代码至DevEco Studio工程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > （可选）同步云端代码至DevEco Studio工程
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:121388638d48713450e709c5b47a9a0ec56306ff7332f0de427a406d3dbeaa11
---

DevEco Studio还支持您将HarmonyOS 开发者中心当前项目下的代码同步至本地工程，包括之前从本地部署到HarmonyOS 开发者中心的代码、以及在HarmonyOS 开发者中心编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](agc-harmonyos-clouddev-sync.md#section588213529814)、[仅同步云数据库](agc-harmonyos-clouddev-sync.md#section474014335350)、[一键同步云侧代码](agc-harmonyos-clouddev-sync.md#section1198316575339)。

## 同步云函数/云对象

**说明** 

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

### 同步单个云函数/云对象

云函数/云对象部署到HarmonyOS 开发者中心后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1. 右击云对象目录，选择“Sync '*云对象名*'”。下文以云对象“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_vP8McIbTxqyDvJ8VhBcUQ/zh-cn_image_0000002214704461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B4BB29651A809CFE7B21D781DD55092049ABBAD7254D6C03B3DD898798ADF01)
2. 在确认弹框中点击“Overwrite”，HarmonyOS 开发者中心的云对象“id-generator”将覆盖更新本地云对象“id-generator”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/XsUCcpPkTA-2SrmeqIO7jA/zh-cn_image_0000002214704477.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=0069C56F185A241037419B5B107360A411EAA45C1D5AFEFE6A420ABA995DA9A6)
3. 等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。

   **说明** 

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/y6Qa9QcmRxqKt_ZXQkDUEg/zh-cn_image_0000002179498228.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BD1B7898791C23ABCE9ED77F714576C2A8400BAAAFE0FDC23C517B19BCF0962)

### 批量同步云函数/云对象

批量同步云函数/云对象即将HarmonyOS 开发者中心当前项目下的所有云函数/云对象同步至本地工程。

1. 右击“cloudfunctions”目录，选择“Sync Cloud Functions”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/P-RN7OBJQIuIdrvEl6CSqw/zh-cn_image_0000002179338512.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=6956182304911AFA2991CED3B48D7001BBDFE9415AC3F9D542D53AFEA2773006)
2. 弹窗提示您本地工程下存在同名云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名云函数/云对象。
   * 选择“Overwrite”，HarmonyOS 开发者中心的云函数/云对象将覆盖更新本地同名云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/UWkYuC1ZSvqMV5Q9qou2Ew/zh-cn_image_0000002214704441.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=C152455866EB0A9ADB22FC0142B4D51454A8B3037865069B6C6D6FFA1AFB418B)
3. 如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/m50HHt2IS4GwR3jwxMABLw/zh-cn_image_0000002214704485.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=D75D6B7BDBD95BE835A68EA85F321D310ABD4AD3758FD492E86EEF2DA6D763BA)
4. 如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

   **说明** 

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/8BnSM51JR1ONFJPTGD5S8Q/zh-cn_image_0000002179338508.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=1892155949D5D28ECBEF0AB0106B015D02DB268915AD1DFB99501FAC56E5178A)

## 同步云数据库

**说明** 

目前仅支持同步对象类型。

### 同步单个对象类型

对象类型部署到HarmonyOS 开发者中心后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1. 右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/xF1ecemHRpOkBHXHYB-MQQ/zh-cn_image_0000002179498216.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACB1700639E2668A7B3CA2D01AD1F7D6FF433336068C0A5C9CB267B76975B8C1)
2. 在确认弹框中点击“Overwrite”，HarmonyOS 开发者中心的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/-zMQArIGQ5eHFh7c0TS7zg/zh-cn_image_0000002214704465.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=94C64D9A826EE943BDF910664C42956AABD3E9029B698EE94988341AB7831212)
3. 等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   **说明** 

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/OCg5jhMwR9qztVBzyn2zpw/zh-cn_image_0000002214704445.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA09EA3E8E4EEC86042B0AC5548EC2D8A0C8088B057BEC7A576A06B1E404BB03)

### 批量同步对象类型

您可以将HarmonyOS 开发者中心当前项目下所有的对象类型一键同步至本地。

1. 右击“objecttype”目录，选择“Sync Object Type”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/FJG-WkLwRgKAOqyx-vBcBw/zh-cn_image_0000002179338532.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EFEFDF6448D965F6EE1F8A2FF67869D7117C242A953F5D526ACDED179EF3CD9)

2. 弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。
   * 选择“Skip”，同步时将跳过本地同名对象类型。
   * 选择“Overwrite”，HarmonyOS 开发者中心的对象类型将覆盖更新本地同名对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/KbO2HGgQSl2n3Ny8_E0iLA/zh-cn_image_0000002179498208.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A5D95B6A63472329862EBC0DCE516A47A42A899F3D98C69DCC76D11E803A6AE)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。

   如下图，“objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/PhPKfQeuRA6T6q285dK9JA/zh-cn_image_0000002179498196.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EC4082AB4FD05A4E75776ADE81BF89D9D768B5819BB1A38980A4AEC58FF7210)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   如下图，“objecttype”目录下生成了“test\_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test\_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-*备份时间*.backup”。

   **说明** 

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/MtNqklryQzyt5Xo8lATH1w/zh-cn_image_0000002214704489.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=31FB454D55510F6F912B9BE788A1D07D8800EED2EE35FE116C7CB90473BE3798)

## 一键同步云侧代码

**说明** 

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1. 右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/E4G-B9cRTsqEebV_8Gbhfg/zh-cn_image_0000002214858849.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B1AF145A1BE4AE6C5019852D84E172E1296EF8FF892A1114D295CDE1B0F54DA)
2. 弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
   * 选择“Overwrite”，HarmonyOS 开发者中心的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/LkkDIo7jQbS_I66HkT7WxA/zh-cn_image_0000002214858861.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=2366175E8EB1B50CF0E74FD0AF4878B8EEF023CA67DF827EFCED68339426A178)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。

   如下图：

   * “objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/EQ-ovrgVRrG7Q483yofx_Q/zh-cn_image_0000002179498236.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=B65CC9439DF507C599E29BABD970A1C8122D8B7E0F4DEBBE6659B79CFC84BA9C)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。
   * 无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。

   如下图：

   * “objecttype”目录下生成了“test \_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test \_object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-*备份时间*.backup”。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

     **说明** 

     后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/tFd4aT98Sm-YfA2mqA0CLA/zh-cn_image_0000002179338516.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=E72FC356F1D8512264F150AC44FE415B585A7879F72DDD717FBDF26E86E3A55A)
