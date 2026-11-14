---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification
title: 开发者自验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 开发者自验证
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d8f884581884c3c68fc2da79a54c648f9a8ac3941b2903bf22fdbe0ecba2f091
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/tdvJGXXmTtWjiLOh0nmV1Q/zh-cn_image_0000002817426591.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=393FC49B931786B51BD548090842CC5F3AEFC82897B86296316B3663B3E782C7)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/4nfcbKmQQkaN0KYB1tdeHA/zh-cn_image_0000002788467172.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=12EF356B4C0CA2CCE8FEF04199048B1AFA5B707A2444CE35C78AE314251B16D0)
3. 单击“复制”按钮，将数据复制到文件管理器的“下载”目录下，作为后续自验证的测试数据源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/DERCLvMwSWaRTvmhE7hUYQ/zh-cn_image_0000002817506661.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A782C068625EB4795DAC29785D2E62658AA1EBE3535694406C6C88F6D6B460F) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/KXSGLdpjSASgJSgrLKcsSA/zh-cn_image_0000002788307230.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=290A7360DFCB4E8C936BE4830CFDAA1F9CDE71368214924B1F954B4CD68D109E)

## HarmonyOS NEXT上模拟验证应用数据迁移

在应用沙箱数据准备好之后，开发者需要先完成所需[适配流程](adaptation-process.md)，再模拟验证应用数据迁移。

1. 安装目标HarmonyOS应用到终端设备。

   **注意** 

   “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。

   从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。

   “迁移调试”工具版本查看方式：**设置**>**应用和元服务**>**MigrateTool**>**版本**
2. 打开迁移调试工具。迁移调试工具图标如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/kVD7tH9LQv6A6-Qqkl7mVw/zh-cn_image_0000002817426593.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=546D11447FD4964DDFDB2BAEFAC3070C4691525AD408F0ABF8F1440A6B43A458)
3. 在“迁移工具”应用的首页，开发者通过单击“选择”按钮进入设备文件管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/zU0w4TdpSMOO1Xd8I36wEw/zh-cn_image_0000002788467174.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCCFCCACE8B7862F47076596286DCED33AB0ACECAE1418FE937294EDB939F22E)
4. 在设备文件管理界面，单击“浏览”按钮，进入浏览手机内部存储界面。单击“我的手机”，根据之前导入数据的路径，进入手机存储的相应路径，选择需要导入的APK应用数据zip包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/t-2ei59wQ66emdPNkfoahQ/zh-cn_image_0000002817506663.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=769B0834CB6F92865D0C23D1022EB552C43E6CB550F506D83B7B49AC443E1390) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/7zl4122TRqKpVvLqf9j2iQ/zh-cn_image_0000002788307232.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFD7522E257A8FB1135AEEAD7DDDB1B131663ACA28F219BCD29EB33BABFCA8EA)
5. 单击需要导入的APK应用数据zip包后，会返回“迁移调试”工具首页，已选择的需要导入的APK应用数据会显示在第一栏中。选择好需要导入的APK应用数据后，单击“请输入应用包名”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/rF_hr8I5RaaUd28k_EFKtg/zh-cn_image_0000002817426595.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB8ABEDC2D36716F50EBAC5EA035035112D59966423AF5DD40083CA1A83183E6)
6. 输入需要验证的目标HarmonyOS应用包名，目标HarmonyOS应用会显示在“迁移调试”工具首页的第二栏中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/_L9GwTFFRQ6aLGCwEYD-cA/zh-cn_image_0000002788467176.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=F28BF93B2C754D47B467026AE18F124135334061033A6263D6D0EE95C5C23DDD)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/FqxqG--ESgyjNDAHa9CBfQ/zh-cn_image_0000002817506665.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=B268DDE3ADE33AEB76140F1807BDF8E038AB59883FE747F4E9EEF79E929B0FA2)
7. 选择需要导入的APK数据和目标HarmonyOS应用后，单击“启动迁移”按钮，开始模拟数据迁移，页面切换为数据优化界面，应用数据迁移的进度在数据迁移进度条中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/hrsGdUtPRjSoxd71sr7ZLA/zh-cn_image_0000002788467176.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E1DF2F8DC1B9907FB5A0B281D51B28081AA3C58091A4CB25197CEA43318EAF3) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/9SQ5a8CQSe-MC4I7Lad9xA/zh-cn_image_0000002788307234.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBDE9253BA466AB332A6AE02316B3823B4E8FA4ABF5EA6A9599ACF293EA519E0)
8. 应用数据迁移完成之后，数据迁移进度条上方显示“已优化完成”，进度更新为100%。数据迁移成功的情况下，界面中无异常提示。单击“完成”按钮，切换回“迁移调试”工具首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   **注意** 

   **1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果**。

   **2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/IPzAiFc1RxW7CbZD4g0YOQ/zh-cn_image_0000002817426597.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5CF6323AF3328E32F7A96EDFA24A7B422460E8D66C371001A08D782D16B0403) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/3CFdf1HXSrmspoJoadh74g/zh-cn_image_0000002788467178.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=62AB8A6AC47358EE2E1C844838AF74F3A1080014ADCCC7050B2CBB35A90EB5CB)
9. 数据迁移失败的情况下，应用图标上方的状态显示“优化失败”。单击“完成”按钮，切换回“迁移工具”应用首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/UBs3iCftSh6Q1f79rOsISg/zh-cn_image_0000002817506667.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEC8D7849E883764AAC97661FEF47534EC339312E06320CAE8F8EA2C0409EFF0) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/VTsT_WXfR7afylP6dotDTQ/zh-cn_image_0000002788307236.png?HW-CC-KV=V1&HW-CC-Date=20261114T004538Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B60CDB96F1C1277B621E00377D7FFB557F50C391EFFB12278311C85CC866D7C)
