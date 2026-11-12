---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification
title: 开发者自验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 开发者自验证
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c032c41e69cd00fba4a16dde084498cb13999618f6039ca3b034fe1c756f8a3
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/uD7vpyVKSIu1xyykn21L5Q/zh-cn_image_0000002786359496.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=33076D833D5A56B0AE63D7D4B644D76676DC0FA3B2C27420C0AF7508A1580CAE)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/aQ_EdjqbQ1KFNSBr6QF6fg/zh-cn_image_0000002815558917.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D3504056CC92E0D940894941F4053F9A2711B627BDBCA1C92E7C8F13BF42782)
3. 单击“复制”按钮，将数据复制到文件管理器的“下载”目录下，作为后续自验证的测试数据源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/_DJiu71wTyqNAJ-BgdRXAg/zh-cn_image_0000002815399001.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFD4E066B421F53E9301520442A289A8EB0038AC85B213621695C9AA3AFCAE23) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/WpV3wh6YS4GxiufxD4CNKw/zh-cn_image_0000002786519426.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=16BC6F20C86C2BB75F11A51072A2ABB5B678D9709D8BF10F5F0E43B614B98E54)

## HarmonyOS NEXT上模拟验证应用数据迁移

在应用沙箱数据准备好之后，开发者需要先完成所需[适配流程](adaptation-process.md)，再模拟验证应用数据迁移。

1. 安装目标HarmonyOS应用到终端设备。

   **注意** 

   “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。

   从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。

   “迁移调试”工具版本查看方式：**设置**>**应用和元服务**>**MigrateTool**>**版本**
2. 打开迁移调试工具。迁移调试工具图标如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/ixHqoQfrToy2pIyQcnH8Ag/zh-cn_image_0000002786359498.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=3597EEF2CD350BB0D1969D806A6581CD761CD21B362C9298397AF7F6C474ED6A)
3. 在“迁移工具”应用的首页，开发者通过单击“选择”按钮进入设备文件管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/OZajv5zHR-OLF-jKC5Z5BQ/zh-cn_image_0000002815558919.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C15252F9D49135F7A4E8946F3934865ED17C0680EB027AFDBD457FB4C504920)
4. 在设备文件管理界面，单击“浏览”按钮，进入浏览手机内部存储界面。单击“我的手机”，根据之前导入数据的路径，进入手机存储的相应路径，选择需要导入的APK应用数据zip包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/EF7PYuSnTFaY_V_8Y2REdw/zh-cn_image_0000002815399003.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFAB8072722FBD71D00F10AC8DFABCF4F4CE91FB59749AF83C85C083F1587752) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/8pdbBvC8SHq87D1POjgCzA/zh-cn_image_0000002786519428.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=210788D4DEB0005A4CCF8BA5146B534B33E779D6CC4272ACF4073D0FC707198F)
5. 单击需要导入的APK应用数据zip包后，会返回“迁移调试”工具首页，已选择的需要导入的APK应用数据会显示在第一栏中。选择好需要导入的APK应用数据后，单击“请输入应用包名”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Y4wID5FWSU6VrV1wWUqXZQ/zh-cn_image_0000002786359500.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3A4D6D991BD20140F06C5F9AA1D218A43A7A03E1BDED1F497EAB1CCB3BDD492)
6. 输入需要验证的目标HarmonyOS应用包名，目标HarmonyOS应用会显示在“迁移调试”工具首页的第二栏中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/lTsw0vFwT1OJxmC-wfu23Q/zh-cn_image_0000002815558921.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B42ABD92E5171B5CC4E44E5639DEDD001B30A78B4517DB7123DB67C321C0B0F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/-9sfCsPQS06VDnCgbkcWag/zh-cn_image_0000002815399005.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=D71A2CC9776F434E0B3DDCF10DAC145ED5E7C26B98E4FD36FA1998B51DB340C6)
7. 选择需要导入的APK数据和目标HarmonyOS应用后，单击“启动迁移”按钮，开始模拟数据迁移，页面切换为数据优化界面，应用数据迁移的进度在数据迁移进度条中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/3HimYEx-R2OYVhoRs3CqWw/zh-cn_image_0000002815558921.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=52CAEBDCC27CC1CC0CFB2583105D5F5E54DA0EA19C09F082001070F9C70D39B2) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/h1T-bcxWTW2hZN9zhSK7og/zh-cn_image_0000002786519430.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDF02E3718487DEEEF46E371C2480FA58297F2A9D6441184A362114566AE3398)
8. 应用数据迁移完成之后，数据迁移进度条上方显示“已优化完成”，进度更新为100%。数据迁移成功的情况下，界面中无异常提示。单击“完成”按钮，切换回“迁移调试”工具首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   **注意** 

   **1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果**。

   **2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/GWHO53m5RLSnhqQTkUhf0g/zh-cn_image_0000002786359502.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=164FAFAE2C34979B1DA3693D4B96C0AD860F8A9EC3B90F823E40A216152678DB) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/3lNCBX0YT8KRlP62Z-2OdQ/zh-cn_image_0000002815558923.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=8394ECAE94FBE5930E796A43BF6CE9E2CD251E2329D4A0F9BCC6A21EC5C38839)
9. 数据迁移失败的情况下，应用图标上方的状态显示“优化失败”。单击“完成”按钮，切换回“迁移工具”应用首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/NgqswVcUQrOO4mQdMZBlgw/zh-cn_image_0000002815399007.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A85919862FBD87CC9AE2FF216670A5C2ED740D2CB2BC6E0051B9B2B27F8BD93) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/dZjHXwz7QcmKWJXz8QPFrw/zh-cn_image_0000002786519432.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A1F55B079427117C63E643B990E6412DFF5E2F888E3BE677A1B74BBD7F783C7)
