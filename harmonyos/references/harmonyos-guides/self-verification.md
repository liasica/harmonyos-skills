---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification
title: 开发者自验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 开发者自验证
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a451f7f6f1011f8bc1b7b9c45bdf602cfb2b355cc7e0a346985ea7f3fe53ccf
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/x1BF4JYnTjCEhzX31x05Yg/zh-cn_image_0000002791725528.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=1727D627385DD5DFDBCD0AA62AAC1E9080C033D9E4E5E5BAE6D03E72456A0DE8)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/lxs6n2llQdSXB5WMFAozJA/zh-cn_image_0000002791565556.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=EDAEE45FAA8B12DE8F209EA39FF59AE8A1774AB5A3DF7CC9D14E9C8113E14084)
3. 单击“复制”按钮，将数据复制到文件管理器的“下载”目录下，作为后续自验证的测试数据源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bt4fHBQ7TdaQjQm7U_TjHw/zh-cn_image_0000002820525509.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6FBA4576AB3DD025C227F3A4ADB104E5EEED2B9125BF5209A5883F2F65C9775) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/0bcyirZHQE-6BaEVDn6Qyw/zh-cn_image_0000002820405509.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C2A9AE55EB53E275FDADD41051775A7F20D1E01260E9E876065A1FE3D59025B)

## HarmonyOS NEXT上模拟验证应用数据迁移

在应用沙箱数据准备好之后，开发者需要先完成所需[适配流程](adaptation-process.md)，再模拟验证应用数据迁移。

1. 安装目标HarmonyOS应用到终端设备。

   **注意** 

   “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。

   从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。

   “迁移调试”工具版本查看方式：**设置**>**应用和元服务**>**MigrateTool**>**版本**
2. 打开迁移调试工具。迁移调试工具图标如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/fyKw4GVURPu4ho_NlNFLLA/zh-cn_image_0000002791725530.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C894195335A8C036DA3AACCFD94EE87DBE958BAF4216DE62DE4728C24CE0240)
3. 在“迁移工具”应用的首页，开发者通过单击“选择”按钮进入设备文件管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/SgECNTQkRzWDuKQBGfxZvg/zh-cn_image_0000002791565558.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2BD67185FA0DEFCD478D1C374BB035830204BA6FFD82A11925AF495321C630E)
4. 在设备文件管理界面，单击“浏览”按钮，进入浏览手机内部存储界面。单击“我的手机”，根据之前导入数据的路径，进入手机存储的相应路径，选择需要导入的APK应用数据zip包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/NYgEmL85Q2a0gzDRj4LmxQ/zh-cn_image_0000002820525511.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=2669C2B47D3BB4B629A9D6A8CE54AAF74913655039CEED5ECA91CC3E765266BF) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/pQmMKscqSQuTorcDyFa4Xw/zh-cn_image_0000002820405511.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=43C2F3330175B16725327F68D01C38BAF606556246FAE52DD9A8B659E11CD174)
5. 单击需要导入的APK应用数据zip包后，会返回“迁移调试”工具首页，已选择的需要导入的APK应用数据会显示在第一栏中。选择好需要导入的APK应用数据后，单击“请输入应用包名”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/tZ677SHOTiyCL_mrzzOgpA/zh-cn_image_0000002791725532.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2A6D84E7DDD08636747AEE217BE02DA0371BF318002531117080F73597493C6)
6. 输入需要验证的目标HarmonyOS应用包名，目标HarmonyOS应用会显示在“迁移调试”工具首页的第二栏中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/KsHr50UMTvWtSPzBkWcFvA/zh-cn_image_0000002791565560.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8899F7AC02F317E621B98BB53F6DBC6409E94600F2580D6CF884778D545BE66)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Yz5SEyBhRMyXXBj95K-hjA/zh-cn_image_0000002820525513.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=D018F1C71AD0F23AEBFEB175F4495D2024F83FDE5798E2EB5BBF502146042EF9)
7. 选择需要导入的APK数据和目标HarmonyOS应用后，单击“启动迁移”按钮，开始模拟数据迁移，页面切换为数据优化界面，应用数据迁移的进度在数据迁移进度条中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Bze2eZq9RIOrd7Eh99OhEg/zh-cn_image_0000002791565560.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD35F17CD53ADEFFBC82E6E9EE4847466370605736BEDEC4F3E48913123E00A2) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/0VnxJrrGSbGNLOepTxBOUg/zh-cn_image_0000002820405513.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF40422343F5940B22D5E096DB79B4248E96F29C27A77EF8EEC84AD1A482FA3A)
8. 应用数据迁移完成之后，数据迁移进度条上方显示“已优化完成”，进度更新为100%。数据迁移成功的情况下，界面中无异常提示。单击“完成”按钮，切换回“迁移调试”工具首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   **注意** 

   **1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果**。

   **2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Vsc4QZ_PSrC0zNGYgKtpOw/zh-cn_image_0000002791725534.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=94F5713432BF94EE4594737A467CC4E5BA39246997A03800308004C8D735E71A) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/sxCkavNaRgiaE8UvnrixWQ/zh-cn_image_0000002791565562.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=009607A2FCE4F76EDBC8133AA83D5CAFB7E1DEB68E8B573208F07888FFCA6FC9)
9. 数据迁移失败的情况下，应用图标上方的状态显示“优化失败”。单击“完成”按钮，切换回“迁移工具”应用首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/JwTyDIKWSWSv2N-UOp3ENA/zh-cn_image_0000002820525515.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=126FF8B05C77B7A1423451802CE5DB0CCFC7575F765BCB6488A0B6A778978449) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/D_vLmziERIa92TTTkxqTWw/zh-cn_image_0000002820405515.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=4805827F07BD0DDF8631C525A9981A3C9950DD92A1B09A68FAC372095D6BA604)
