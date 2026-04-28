---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification
title: 开发者自验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 开发者自验证
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f46374db7766d076f59b3f9c0b96726f90716d44b7e88c2cfe93b49af400b2e
---

## 简介

在开发的过程中，当开发者完成所需[适配流程](adaptation-process.md)后，可导入提前准备好的APK应用沙箱数据，自验证HarmonyOS应用数据迁移适配结果。

在HarmonyOS应用适配完成并上架到华为应用市场之后，开发者仍需要将终端设备从HarmonyOS升级到HarmonyOS NEXT，[端到端验证](e2e-verification.md)应用数据迁移结果。

## 开发者自验证流程

### 应用沙箱数据准备

请自行构造APK应用沙箱数据，并将构造好的APK应用沙箱数据按指定格式打包成“{APK包名}.zip”。

说明

在打包‘{APK包名}.zip’文件时，必须使用UTF-8编码格式进行压缩，否则压缩中文命名的文件时，文件名会出现乱码。

| **APK应用沙箱目录** | {APK包名}.zip目录 |
| --- | --- |
| /data/user\_de/{userId}/{APK包名}/ | {APK包名}/de |
| /data/user/{userId}/{APK包名}/ | {APK包名}/ce |
| /data/media/{userId}/Android/data/{APK包名}/ | {APK包名}/A/data |
| /data/media/{userId}/Android/obb/{APK包名}/ | {APK包名}/A/obb |

打包好的“{APK包名}.zip”解压后，要满足包含一个“APK包名”根目录，根目录下包含对应沙箱目录文件夹，文件结构如下。

```
1. ─com.demo.demo
2. ├─A
3. │  ├─data
4. │  └─obb
5. ├─ce
6. └─de
```

1. 将打包好的“{APK包名}.zip”推送到外部存储设备（U盘或者移动硬盘），连接终端设备和外部存储设备。

   说明

   当前终端设备支持识别NTFS格式的外部存储设备，请使用NTFS格式的外部存储设备连接终端设备。
2. 在终端设备中，打开“文件管理”应用，长按选中外部存储设备中的“{APK包名}.zip”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/fGp8Q296TKiG8KlTOZYO3A/zh-cn_image_0000002583478269.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=8025303CB9A335E9C617BA60BCCC0D15B437D2021D42580CC2E81AE4DCC2FED2)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/H7z9A87BRnG8CwSot-nzgQ/zh-cn_image_0000002552798620.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=CB510A08417E3B77DE78F08E41C50B99ACF18A7877709364EDD1538D5596FCAB)
3. 单击“复制”按钮，将数据复制到文件管理器的“下载”目录下，作为后续自验证的测试数据源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/8bM_zO2EQn2ruRFZQbM_9g/zh-cn_image_0000002583438315.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=FE3253880A7D08CCDEA84362B186BD69FA8DE1C89631A92BF1CA68F90B48D7A0) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/YbSZRMkbRn6Y1xeD2rkPig/zh-cn_image_0000002552958270.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=8BCBD53D91976A28660ECF64C9D600AB1F2A796800FF6C60E872D2AFFA28B171)

## HarmonyOS NEXT上模拟验证应用数据迁移

在应用沙箱数据准备好之后，开发者需要先完成所需[适配流程](adaptation-process.md)，再模拟验证应用数据迁移。

1. 安装目标HarmonyOS应用到终端设备。

   注意

   “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。

   从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。

   “迁移调试”工具版本查看方式：**设置**>**应用和元服务**>**MigrateTool**>**版本**
2. 打开迁移调试工具。迁移调试工具图标如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/9vXSgb82Rdqzk_W33T8OyQ/zh-cn_image_0000002583478271.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=21D4E651B7B092FE880255064D5C1A5DC584B3017DFBBDDC80E3819F57882B89)
3. 在“迁移工具”应用的首页，开发者通过单击“选择”按钮进入设备文件管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/zDGqJnJGRMuxMbXTtJO-ww/zh-cn_image_0000002552798622.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=51BD1EA66E5915FF90587FD79C658AAA956084CEDBC5FDBE75E2240FB53DACC5)
4. 在设备文件管理界面，单击“浏览”按钮，进入浏览手机内部存储界面。单击“我的手机”，根据之前导入数据的路径，进入手机存储的相应路径，选择需要导入的APK应用数据zip包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/sS982RPHRi2I3v59GZx1nw/zh-cn_image_0000002583438317.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=D6C541A77603D46464749D8FCB5AB45CC9DB4B5D242FE780E1C6D3ED58976DA1) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/aZWqGECSTuOeRA0E4kDang/zh-cn_image_0000002552958272.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=165D2D82E8376825CB747CED95AED8240F8D930C283EEB37003C14AC65847A58)
5. 单击需要导入的APK应用数据zip包后，会返回“迁移调试”工具首页，已选择的需要导入的APK应用数据会显示在第一栏中。选择好需要导入的APK应用数据后，单击“请输入应用包名”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/f6ldYKblTsG5T9sx82KLxg/zh-cn_image_0000002583478273.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=EE6A60936860192AC32E294FC7B66FD70B925970BD63AE5A02FBDC76FA330DB1)
6. 输入需要验证的目标HarmonyOS应用包名，目标HarmonyOS应用会显示在“迁移调试”工具首页的第二栏中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/7_GbSmKgRv2p5FvPtepLuA/zh-cn_image_0000002552798624.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=FE4B3C48EA789581E43C5A2D6D706EC571F19E556419581F0505E1602BB154D5)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/S6WYt2CHRsCYbtY2VpCP6w/zh-cn_image_0000002583438319.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=99C73EC7F3B0A5F47A77A6BBAAC61743A8D9C327DF443EAD1B1107EA4FE6D926)
7. 选择需要导入的APK数据和目标HarmonyOS应用后，单击“启动迁移”按钮，开始模拟数据迁移，页面切换为数据优化界面，应用数据迁移的进度在数据迁移进度条中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/8aXbWG4OSOmj_0o_YsStig/zh-cn_image_0000002552798624.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=9681C342EF5381BB2DBFC826F8543AA7633819127678209E12BB002D1221B7E6) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/xWuUZdB-SxS2vqpuRuM_kA/zh-cn_image_0000002552958274.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=6B5207C3DCA9B547D037A2F607333734FBE27EC4371D0135AC94EA915D14F8CC)
8. 应用数据迁移完成之后，数据迁移进度条上方显示“已优化完成”，进度更新为100%。数据迁移成功的情况下，界面中无异常提示。单击“完成”按钮，切换回“迁移调试”工具首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   注意

   **1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果**。

   **2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/xkhdHSa9SRCF9fgSsBE0BA/zh-cn_image_0000002583478275.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=603305CCA1B9FF864574574162A476850D204CEB4234EFD41BEACCFF564861ED) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Y971l6m5SY6f95zwuGk0jA/zh-cn_image_0000002552798626.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=8F85DD9F503F4ABCB0E2E88806F99F23746D1CC7D78FA6D42A29669CD2EA05F6)
9. 数据迁移失败的情况下，应用图标上方的状态显示“优化失败”。单击“完成”按钮，切换回“迁移工具”应用首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/7LKZBB-GQlmimQzimt6zfw/zh-cn_image_0000002583438321.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=762C329951A8E4A29908040A75C753AA1D44FD41C1AD273D6F7CC4862A9E3944) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/heYOWC2mRgmrh-hOpkVhxg/zh-cn_image_0000002552958276.png?HW-CC-KV=V1&HW-CC-Date=20260427T234114Z&HW-CC-Expire=86400&HW-CC-Sign=D2A2862986E087FEC77967538AAD36BB44A5D742751318FD7F6DA4B6311219EE)
