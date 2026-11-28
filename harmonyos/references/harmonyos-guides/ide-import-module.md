---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-module
title: 导入和引用模块
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 导入和引用模块
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:26+08:00
doc_updated_at: 2026-06-24
content_hash: sha256:2b6d5561b0673d240a7e7565f9af5817779babc87e9a9e1d4174863ee96389a1
---

DevEco Studio支持通过以下两种方式导入其他工程下的模块：

1. 通过[Import Module](ide-import-module.md#section14353041183813)功能，将其他HarmonyOS模块的功能代码复制到当前工程中；当前仅支持FA模型的模块导入到FA模型，Stage模型的模块导入到Stage模型。不支持FA模型的模块导入到Stage模型，或Stage模型的模块导入到FA模型。
2. 通过在[srcPath字段下配置相对路径](ide-import-module.md#section12737181153918)的方式引用其他工程下的模块，该方式仅引用模块相关信息，不会将模块代码完全复制至本地。当前支持引用其他工程下的HAR和HSP模块。

## 导入模块

1. 在菜单栏单击**File > New > Import... > Import Module。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/VTrBhhHYRwKK55mkdiRssg/zh-cn_image_0000002808766521.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=56E3FA96CD11ACF1826CD9E4341077567D009656C620EC77524B1DE38CCFC975)
2. 选择导入的模块。

   在指定路径下，选择导入的模块，单击**OK**。导入的模块可以为文件夹，也可以为zip格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/nMtqSWqSRc-2sUr5cp8_6g/zh-cn_image_0000002808766519.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF6E89D236E34ABA9DC4B04F4288CB7FC27F4ADAA17AE839D2F364412D1CB686)

## 引用模块

在工程级build-profile.json5文件中，如下图所示在modules > srcPath字段下配置工程外模块的相对路径，即可引用模块相关信息，不会将模块代码完全复制至本工程中。当前支持引用其他工程下的HAR和HSP模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/ZglGpwpLQT-Bt-03MMr-LQ/zh-cn_image_0000002808886601.png?HW-CC-KV=V1&HW-CC-Date=20261128T023426Z&HW-CC-Expire=31536000000&HW-CC-Sign=B39FAC1AC08BE53E5B7D78E0EC4E04DE75AAD4E53455BEBB1F4A14787A53C445)
