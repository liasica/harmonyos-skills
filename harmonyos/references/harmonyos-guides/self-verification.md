---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification
title: 开发者自验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 开发者自验证
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e0496dcfaeb1bb325acfba872c4ac64cd4b51022f11bf2f9cc889ef31a746a32
---

## 简介

在开发的过程中，当开发者完成所需[适配流程](adaptation-process.md)后，可导入提前准备好的APK应用沙箱数据，自验证HarmonyOS应用数据迁移适配结果。

在HarmonyOS应用适配完成并上架到华为应用市场之后，开发者仍需要将终端设备从HarmonyOS升级到HarmonyOS NEXT，[端到端验证](e2e-verification.md)应用数据迁移结果。

## 开发者自验证流程

### 应用沙箱数据准备

请自行构造APK应用沙箱数据，并将构造好的APK应用沙箱数据按指定格式打包成“{APK包名}.zip”。

**说明** 

在打包‘{APK包名}.zip’文件时，必须使用UTF-8编码格式进行压缩，否则压缩中文命名的文件时，文件名会出现乱码。

| **APK应用沙箱目录** | {APK包名}.zip目录 |
| --- | --- |
| /data/user\_de/{userId}/{APK包名}/ | {APK包名}/de |
| /data/user/{userId}/{APK包名}/ | {APK包名}/ce |
| /data/media/{userId}/Android/data/{APK包名}/ | {APK包名}/A/data |
| /data/media/{userId}/Android/obb/{APK包名}/ | {APK包名}/A/obb |

打包好的“{APK包名}.zip”解压后，要满足包含一个“APK包名”根目录，根目录下包含对应沙箱目录文件夹，文件结构如下。

```text
─com.demo.demo
    ├─A
    │  ├─data
    │  └─obb
    ├─ce
    └─de
```

1. 将打包好的“{APK包名}.zip”推送到外部存储设备（U盘或者移动硬盘），连接终端设备和外部存储设备。

   **说明** 

   当前终端设备支持识别NTFS格式的外部存储设备，请使用NTFS格式的外部存储设备连接终端设备。
2. 在终端设备中，打开“文件管理”应用，长按选中外部存储设备中的“{APK包名}.zip”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xdGiiMixR-miRQMa5saDaA/zh-cn_image_0000002821837115.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC24466EFBADF47B30ED104F665263CF13E08B7AF63F005ACA24014BA2E3CADF)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/EdNvBxfgSvKaE0SrSqQhTA/zh-cn_image_0000002821757117.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0F8C0E77BAC167C44D04E93D88BEF53C9E70BC4477D8D71E1588B10217C0DBC)
3. 单击“复制”按钮，将数据复制到文件管理器的“下载”目录下，作为后续自验证的测试数据源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/0jRWbrE2SueUbzSncCcIQw/zh-cn_image_0000002793037180.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=5286CD82C0EA91DAB8B5D59138CCDCDD703BBE1128ECBEF7D93A7CD3DD46F4B4) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Nea9Yzs2T-6eueIyINaG-A/zh-cn_image_0000002792877210.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=82FF25771B2A811539116F9D5F8FAEB3B305054CC9510B3DC3248C9AED3EA0FE)

## HarmonyOS NEXT上模拟验证应用数据迁移

在应用沙箱数据准备好之后，开发者需要先完成所需[适配流程](adaptation-process.md)，再模拟验证应用数据迁移。

1. 安装目标HarmonyOS应用到终端设备。

   **注意** 

   “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。

   从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。

   “迁移调试”工具版本查看方式：**设置**>**应用和元服务**>**MigrateTool**>**版本**
2. 打开迁移调试工具。迁移调试工具图标如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/x0hgD8fHSCCtiyLc2szcuw/zh-cn_image_0000002821837117.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=306F3A60140F627B6FDF3AACB8805C5E9272BE05687A74C5CDCF60334646EC23)
3. 在“迁移工具”应用的首页，开发者通过单击“选择”按钮进入设备文件管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/aKzamS-oSC67co-JX3zDFA/zh-cn_image_0000002821757119.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=69D4E9041168B8238FF0481A4198AD39DC21C126DF896E697F13C995BCF611F4)
4. 在设备文件管理界面，单击“浏览”按钮，进入浏览手机内部存储界面。单击“我的手机”，根据之前导入数据的路径，进入手机存储的相应路径，选择需要导入的APK应用数据zip包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/SHOUhU-UTw2HW7gyikRMSA/zh-cn_image_0000002793037182.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=56E33B028D997178505A7787247B36B32C1CE4FE2A0F0F8140504E3A96DF5634) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/cEO0WDjlT7uIAllA-1qVGg/zh-cn_image_0000002792877212.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CD60D0B1FE8D3BFE470796261863806F9B20A7DC654AF49353778D017B7982C)
5. 单击需要导入的APK应用数据zip包后，会返回“迁移调试”工具首页，已选择的需要导入的APK应用数据会显示在第一栏中。选择好需要导入的APK应用数据后，单击“请输入应用包名”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/0_gi4svTT02s_NfOZlWwvw/zh-cn_image_0000002821837119.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BDB374949DD9D85608F9D853EACC267925587904A43B43D4C64FB361F1B95A1)
6. 输入需要验证的目标HarmonyOS应用包名，目标HarmonyOS应用会显示在“迁移调试”工具首页的第二栏中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Wo01V2TSQlqd3uZBOjnY_g/zh-cn_image_0000002821757121.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=C6689E9074E806390232E0FD162A073A30DE7BFB77223B39AB8ED5072B637484)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/8BfVZN7oT-OBGfflVJahjA/zh-cn_image_0000002793037184.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBBF9716AEDFDDF0510173D9B64F0FCCE6C6B28CEB750DCEB1672B05C75D0CFA)
7. 选择需要导入的APK数据和目标HarmonyOS应用后，单击“启动迁移”按钮，开始模拟数据迁移，页面切换为数据优化界面，应用数据迁移的进度在数据迁移进度条中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/YgkrwX01Sn2djI1XPqe0hw/zh-cn_image_0000002821757121.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AF54CD4FF0B2617256E88C4C41D55BC493FC31300675CED62755C8B3458DB10) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ZdolLjc8Tpy4C1JXEvkAkQ/zh-cn_image_0000002792877214.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=19767266620A5C69C3DC254A1B43224BE11AE5FEBC7171778848FCEC6D789D30)
8. 应用数据迁移完成之后，数据迁移进度条上方显示“已优化完成”，进度更新为100%。数据迁移成功的情况下，界面中无异常提示。单击“完成”按钮，切换回“迁移调试”工具首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   **注意** 

   **1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果**。

   **2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/VEPkix3FR0O1Bs1Z_zBpsg/zh-cn_image_0000002821837121.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=435B4DA81DAAA650E9393729A80B998FFB7D6FB6F44162DD09F22BDC8BE33104) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/panOHGsMQ2WHKVP_IsPDHg/zh-cn_image_0000002821757123.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5680347EC63372C8558901E838F4F1B0F0DA0CD3217CE51D476762A039A503F)
9. 数据迁移失败的情况下，应用图标上方的状态显示“优化失败”。单击“完成”按钮，切换回“迁移工具”应用首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/_bS-llV2Tz2jXSxjnWuY-w/zh-cn_image_0000002793037186.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD066B0D62BB04C9628BA8B14E5E2A2672C402F4EDE41109F8688BA044E9E3DC) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/Zvq20ZbcTPi4PhZXc1KV0A/zh-cn_image_0000002792877216.png?HW-CC-KV=V1&HW-CC-Date=20261121T010956Z&HW-CC-Expire=31536000000&HW-CC-Sign=A984698B0F2FE600A5B8C086F1D4EFD83379BD92A9332530723AEFC1C8783A1E)
