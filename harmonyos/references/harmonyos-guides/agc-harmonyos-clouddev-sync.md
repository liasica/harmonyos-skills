---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-sync
title: （可选）同步云端代码至DevEco Studio工程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > （可选）同步云端代码至DevEco Studio工程
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:08+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:88a7df9d1084f87daeb79531cf81d3c02f97f38cad2bdaeb3e54c398d9d9b8d2
---

DevEco Studio还支持您将AGC云端当前项目下的代码同步至本地工程，包括之前从本地部署到AGC云端的代码、以及在AGC云端编写的代码，以保证云端和本地的版本一致性，方便您的日常开发。

云端代码同步目前支持以下模式：[仅同步云函数/云对象](agc-harmonyos-clouddev-sync.md#section588213529814)、[仅同步云数据库](agc-harmonyos-clouddev-sync.md#section474014335350)、[一键同步云侧代码](agc-harmonyos-clouddev-sync.md#section1198316575339)。

## 同步云函数/云对象

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

### 同步单个云函数/云对象

云函数/云对象部署到AGC云端后，如在云端又进行了新改动，您可再将云端的云函数/云对象同步到本地工程。云函数/云对象的同步方式一致，下文以云对象为例进行说明。

1. 右击云对象目录，选择“Sync '*云对象名*'”。下文以云对象“id-generator”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/NIZlr35DTHiGwcQxkN1yLw/zh-cn_image_0000002214704461.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=CA9225543F1765F6E82978E25BBA8D3BC3DA9078EE48A39ABBE6D57ACB3E6A7E)
2. 在确认弹框中点击“Overwrite”，AGC云端的云对象“id-generator”将覆盖更新本地云对象“id-generator”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/8HsSTkbtS_S6RW9swBCpXw/zh-cn_image_0000002214704477.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=4BF64D7EBBD2E8CF32F5692B4F40D8D8A7F7D4C9ED6B1AB483122AC23D820EED)
3. 等待同步完成，“cloudfunctions”目录下将生成从云端同步下来的云对象“id-generator”，同时将本地原云对象“id-generator”备份在同路径下。

   说明

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/q08AHrYUTf-caL5NY7cgLg/zh-cn_image_0000002179498228.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=F83052BAE2E0B97EC2F0E16252ACD117051B5551700A6E6273A8C04DC98E6F23)

### 批量同步云函数/云对象

批量同步云函数/云对象即将AGC云端当前项目下的所有云函数/云对象同步至本地工程。

1. 右击“cloudfunctions”目录，选择“Sync Cloud Functions”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/iup9ueR3SHKSoPOrYrA3oQ/zh-cn_image_0000002179338512.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=F99BB869E93182245C44D2C3A8D51A2E4F424174F0A944A00B82699578A67F10)
2. 弹窗提示您本地工程下存在同名云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名云函数/云对象。
   * 选择“Overwrite”，AGC云端的云函数/云对象将覆盖更新本地同名云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/p-8ssaACQB6MYZ5LYvSmjA/zh-cn_image_0000002214704441.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=CAA9230D8F963D1834F25D8E29D0EC2E5647C4E9A3F378FECDBEFAAFAD3D47F3)
3. 如选择“Skip”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的不同步。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，上图中本地已存在的云函数/云对象未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/m46v2aXFR9ysdr-NG-ZR8Q/zh-cn_image_0000002214704485.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=6865950AE2100FDA99D92A5CF24E20496F3D124C7D769C2E6F0D706829722FC7)
4. 如选择“Overwrite”，等待同步完成后，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象；本地同名云函数/云对象也被覆盖更新，同时更新前的原云函数/云对象会备份在同路径下。

   如下图，“cloudfunctions”目录下新增了云端同步下来的“test-cloud-function”，本地已存在的几个云函数/云对象也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

   说明

   后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/fvo8ZOOARvWEU3nPS4qdVg/zh-cn_image_0000002179338508.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=87A686670305AC3E2B32EED101082D3A1D17923DA4621C6D5AE5D0085D01CB23)

## 同步云数据库

说明

目前仅支持同步对象类型。

### 同步单个对象类型

对象类型部署到AGC云端后，如又发生了新改动，您可再将云端的对象类型同步到本地。

1. 右击对象类型JSON文件（以“objecttype1.json”为例），选择“Sync 'objecttype1.json'”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/dSeuVUNkTiuEb1V_osbRUQ/zh-cn_image_0000002179498216.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=FABBB445852D3F0AF2B766535D78477FAF48C33DE91C84D128C9B930B855D093)
2. 在确认弹框中点击“Overwrite”，AGC云端的对象类型“objecttype1.json”将覆盖更新本地对象类型“objecttype1.json”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/YgDWjgyqSJ6WMR1zo0VKHg/zh-cn_image_0000002214704465.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=A8C254D8A907F5E25BE0229DC2F0EB5151A3CACB685DE1B7896ACF6F034E96B2)
3. 等待同步完成，“objecttype”目录下将生成从云端同步下来的对象类型“objecttype1.json”。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   说明

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/VUOoA7wvRVuLdyEH5l1t3g/zh-cn_image_0000002214704445.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=16EE36421654EF7E1C7A47175C418D4021C088A15A7BC37A2C2ACEE621B6CD16)

### 批量同步对象类型

您可以将AGC云端当前项目下所有的对象类型一键同步至本地。

1. 右击“objecttype”目录，选择“Sync Object Type”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/T_lFFItYSGmOXOm3XoNvpg/zh-cn_image_0000002179338532.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=99E45280565EB9C3F25C54EDC27C1647A54C33AFA6F94EA1F81E1EC276D54B53)

2. 弹窗提示您本地工程下已存在同名对象类型，如下图“Post.json”与“objecttype1.json”。
   * 选择“Skip”，同步时将跳过本地同名对象类型。
   * 选择“Overwrite”，AGC云端的对象类型将覆盖更新本地同名对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/p3hg6m5CS9u1yQiN0ARDGA/zh-cn_image_0000002179498208.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=4F12687F7E68A48E3630D81A4C3C4DAA2B786500673FAFEEB7307B049DF6DEE1)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，本地已存在的不同步。

   如下图，“objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/jB3nHl7vSK2DlJFjvURZ_w/zh-cn_image_0000002179498196.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=CA41C1A1FEA10210C0269D4905BCFFE450CC5D86C49B4AC79157B494352AB1C6)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的所有对象类型，本地已存在的对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。

   如下图，“objecttype”目录下生成了“test\_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test\_object.json”为从云端新同步下来的对象类型；“objecttype1.json”本地已存在且与云端内容一致，不生成备份；“Post.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“Post.json”备份为“Post.json-*备份时间*.backup”。

   说明

   后续如执行部署，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/ZZanV5DDTv6JUhyTWv7vFA/zh-cn_image_0000002214704489.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=17C918A9EC18A8513D632ECA2878617407E5E3C3B8EFD8E60244B8A0E7EFF322)

## 一键同步云侧代码

说明

对于使用DevEco Studio 4.1 Canary 2之前的版本部署的函数，同步下来的是JavaScript代码。

1. 右击云开发工程（“CloudProgram”），选择“Sync Cloud Program”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/_opT-eO8SoWjdf2ktTBkZA/zh-cn_image_0000002214858849.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=965B2DB4260A37FD558811632F6A51778A18919C8F957D319AFE720EF10B5750)
2. 弹窗提示您本地工程下已存在同名对象类型/云函数/云对象。
   * 选择“Skip”，同步时将跳过本地同名对象类型/云函数/云对象。
   * 选择“Overwrite”，AGC云端的对象类型/云函数/云对象将覆盖更新本地同名对象类型/云函数/云对象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/oFZ-yU6LQM-3wZkumkJt4Q/zh-cn_image_0000002214858861.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=1AB3FABE78945A40869524FA4E8B0902BC497E59A0955E6AF8D38BB4CF1E1F3E)
3. 如选择“Skip”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型均不同步。

   如下图：

   * “objecttype”目录下新增了云端同步下来的“test\_object.json”，本地已存在的“Post.json”与“objecttype1.json”未被覆盖更新。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”未被覆盖更新。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/3X3A0VcWSnuephIwqso9_A/zh-cn_image_0000002179498236.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=F157013CAEBF43200FA2EDD93A6EE7918F1BC52E5DC7E75CD59E84238CC5FFFB)
4. 如选择“Overwrite”，等待同步完成后，“objecttype”目录下将生成从云端同步下来的本项目下所有对象类型，“cloudfunctions”目录下将生成从云端同步下来的本项目下所有云函数/云对象，本地已存在的云函数/云对象/对象类型也被覆盖更新。
   * 如果云端和本地的同名对象类型内容存在差异，则还会将本地原对象类型备份在同路径下。
   * 如果云端和本地的同名对象类型内容完全一致，则不生成备份。
   * 无论云端和本地的同名云函数/云对象代码是否一致，均会将本地原云函数/云对象备份在同路径下。

   如下图：

   * “objecttype”目录下生成了“test \_object.json”、“Post.json”与“objecttype1.json”三个对象类型文件，其中：“test \_object.json”为从云端新同步下来的对象类型；“Post.json”本地已存在且与云端内容一致，不生成备份；“objecttype1.json”本地已存在但与云端内容存在差异，因此被覆盖更新，同时原“objecttype1.json”备份为“objecttype1.json-*备份时间*.backup”。
   * “cloudfunctions”目录下生成了从云端同步下来的“test-cloud-function”，本地已存在的“id-generator”、“my-cloud-function”与“my-cloud-object”也被覆盖更新，并且均生成了备份文件“xxxx-*备份时间*.backup”。

     说明

     后续如执行部署或调试，DevEco Studio会自动跳过备份数据。但出于精简包的考虑，建议您在对比代码差异后，及时将无用的备份数据删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/HBuGvpjTS0i_99ncePqesg/zh-cn_image_0000002179338516.png?HW-CC-KV=V1&HW-CC-Date=20260427T235506Z&HW-CC-Expire=86400&HW-CC-Sign=17B83A316B64488F21C3CEA696D2D9AC994D836A1E91B29BFEE8841A98A2E7D8)
