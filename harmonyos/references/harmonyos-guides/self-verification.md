---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/self-verification
title: 开发者自验证
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 验证应用数据迁移 > 开发者自验证
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:822b403d09a0462130f749e4758078cb130929442a997ce3582342cb1bb55a6d
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/sk8K3-aPRQqSSyn1TE83LQ/zh-cn_image_0000002742123273.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/XmQYSuONQfinWc0Y5RBGgQ/zh-cn_image_0000002712244360.png)
3. 单击“复制”按钮，将数据复制到文件管理器的“下载”目录下，作为后续自验证的测试数据源。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/CQqZaHboSu2-NFnA2RtO6A/zh-cn_image_0000002742003313.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/BriBk0QdQeSvNhFZckTuIw/zh-cn_image_0000002712404326.png)

## HarmonyOS NEXT上模拟验证应用数据迁移

在应用沙箱数据准备好之后，开发者需要先完成所需[适配流程](adaptation-process.md)，再模拟验证应用数据迁移。

1. 安装目标HarmonyOS应用到终端设备。

   **注意** 

   “迁移调试”工具“205.0.0.110”之前的版本，仅支持调试release签名的应用。

   从“205.0.0.110”版本开始，“迁移调试”工具仅支持调试debug签名的应用。请开发者升级到最新版本，并使用debug签名的包验证。

   “迁移调试”工具版本查看方式：**设置**>**应用和元服务**>**MigrateTool**>**版本**
2. 打开迁移调试工具。迁移调试工具图标如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/_BhNqvPLS_-pMxCyzxOtAA/zh-cn_image_0000002742123275.png)
3. 在“迁移工具”应用的首页，开发者通过单击“选择”按钮进入设备文件管理界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/-rrhw_ncSgyw1LREJYmWsQ/zh-cn_image_0000002712244362.png)
4. 在设备文件管理界面，单击“浏览”按钮，进入浏览手机内部存储界面。单击“我的手机”，根据之前导入数据的路径，进入手机存储的相应路径，选择需要导入的APK应用数据zip包。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/rPxwUmGBSMW0yXOPjBfykw/zh-cn_image_0000002742003315.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/_9xuGLYpQHSBiaaPdRwgPg/zh-cn_image_0000002712404328.png)
5. 单击需要导入的APK应用数据zip包后，会返回“迁移调试”工具首页，已选择的需要导入的APK应用数据会显示在第一栏中。选择好需要导入的APK应用数据后，单击“请输入应用包名”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/6xFNbuh5Qh-lLlBnfdgO1g/zh-cn_image_0000002742123277.png)
6. 输入需要验证的目标HarmonyOS应用包名，目标HarmonyOS应用会显示在“迁移调试”工具首页的第二栏中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/GpkvHIlRSNG0yf-MSEyIdQ/zh-cn_image_0000002712244364.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/KxjK0AwySn6bQMS6PNJVNQ/zh-cn_image_0000002742003317.png)
7. 选择需要导入的APK数据和目标HarmonyOS应用后，单击“启动迁移”按钮，开始模拟数据迁移，页面切换为数据优化界面，应用数据迁移的进度在数据迁移进度条中显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/YIM_qkcARPCtP1iCIqPw8w/zh-cn_image_0000002712244364.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/PpB015NIRXST25FvC_Oh5A/zh-cn_image_0000002712404330.png)
8. 应用数据迁移完成之后，数据迁移进度条上方显示“已优化完成”，进度更新为100%。数据迁移成功的情况下，界面中无异常提示。单击“完成”按钮，切换回“迁移调试”工具首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   **注意** 

   **1、此处的数据迁移成功，仅表示“备份恢复框架”接入成功，APK应用的数据成功迁移到“备份恢复框架”需要的指定目录。开发者需要通过从应用的沙箱中获取数据并解析，判断应用适配“备份恢复框架”的结果**。

   **2、单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，会导致任务执行失败。开发者需要优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/Jb6qmkz6QU2FN_3EfJQk5A/zh-cn_image_0000002742123279.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/16Hl2INnTFmIaE9KGwRZzg/zh-cn_image_0000002712244366.png)
9. 数据迁移失败的情况下，应用图标上方的状态显示“优化失败”。单击“完成”按钮，切换回“迁移工具”应用首页，在下方的“迁移日志”版块中显示详细迁移信息。result字段表示数据迁移结果，costTime字段表示数据迁移时长（单位ms）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/zbS2lTfTTzu5Irol7JGJAw/zh-cn_image_0000002742003319.png) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/7u9uOO3XSCWGj4GQUCqfZg/zh-cn_image_0000002712404332.png)
