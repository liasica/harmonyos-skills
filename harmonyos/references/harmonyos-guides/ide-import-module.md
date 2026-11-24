---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-module
title: 导入和引用模块
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 导入和引用模块
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:19+08:00
doc_updated_at: 2026-06-24
content_hash: sha256:230e93ecbaae4f8c131f5ad4ab2947d5a7605030a1a36f1e405cb52f6fb8cedc
---

DevEco Studio支持通过以下两种方式导入其他工程下的模块：

1. 通过[Import Module](ide-import-module.md#section14353041183813)功能，将其他HarmonyOS模块的功能代码复制到当前工程中；当前仅支持FA模型的模块导入到FA模型，Stage模型的模块导入到Stage模型。不支持FA模型的模块导入到Stage模型，或Stage模型的模块导入到FA模型。
2. 通过在[srcPath字段下配置相对路径](ide-import-module.md#section12737181153918)的方式引用其他工程下的模块，该方式仅引用模块相关信息，不会将模块代码完全复制至本地。当前支持引用其他工程下的HAR和HSP模块。

## 导入模块

1. 在菜单栏单击**File > New > Import... > Import Module。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/aJHSl34LT4i3dUGuJroXYQ/zh-cn_image_0000002808766521.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C9CBDD1EB004B439C8308845E4948DE99BE3C07CFEE26033B8444642B35C416)
2. 选择导入的模块。

   在指定路径下，选择导入的模块，单击**OK**。导入的模块可以为文件夹，也可以为zip格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/QDLCBVcXRw-yM1v7gA8qow/zh-cn_image_0000002808766519.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=45A8F4A3AB1817AAAB1619033994E2C3F3FC820188EAF469BA70AD832D62B87A)

## 引用模块

在工程级build-profile.json5文件中，如下图所示在modules > srcPath字段下配置工程外模块的相对路径，即可引用模块相关信息，不会将模块代码完全复制至本工程中。当前支持引用其他工程下的HAR和HSP模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ZLK26R7hS2mLPzeuSwiguQ/zh-cn_image_0000002808886601.png?HW-CC-KV=V1&HW-CC-Date=20261124T044219Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBE174D6286BA965DE1054799CCD6A10B36BF26B2C00930BEEF18A70ECBE1B97)
