---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-import-module
title: 导入和引用模块
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 导入和引用模块
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:46+08:00
doc_updated_at: 2026-06-24
content_hash: sha256:c9a908090f1340dedef6f88bf582e945dea9c0947ba67e15bb366e19a3afa9f4
---

DevEco Studio支持通过以下两种方式导入其他工程下的模块：

1. 通过[Import Module](ide-import-module.md#section14353041183813)功能，将其他HarmonyOS模块的功能代码复制到当前工程中；当前仅支持FA模型的模块导入到FA模型，Stage模型的模块导入到Stage模型。不支持FA模型的模块导入到Stage模型，或Stage模型的模块导入到FA模型。
2. 通过在[srcPath字段下配置相对路径](ide-import-module.md#section12737181153918)的方式引用其他工程下的模块，该方式仅引用模块相关信息，不会将模块代码完全复制至本地。当前支持引用其他工程下的HAR和HSP模块。

## 导入模块

1. 在菜单栏单击**File > New > Import... > Import Module。**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/JwRAZUgyRsSd20SnMVH2NA/zh-cn_image_0000002808766521.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=22AF3EA385AA49A2F1A45E7AF5E5475327F5FEAB2C3FCF1E42A67E7CB832D9A8)
2. 选择导入的模块。

   在指定路径下，选择导入的模块，单击**OK**。导入的模块可以为文件夹，也可以为zip格式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/TzwklLpPSYqQmtTBAXMfVw/zh-cn_image_0000002808766519.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=30FED4A3AA08BCAC9D62B099BC72AED3E2CF68A3B8F4CA8CF39ACA3557D40424)

## 引用模块

在工程级build-profile.json5文件中，如下图所示在modules > srcPath字段下配置工程外模块的相对路径，即可引用模块相关信息，不会将模块代码完全复制至本工程中。当前支持引用其他工程下的HAR和HSP模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/DxrOBHGvSRWEN5F10vqa5g/zh-cn_image_0000002808886601.png?HW-CC-KV=V1&HW-CC-Date=20261114T004700Z&HW-CC-Expire=31536000000&HW-CC-Sign=7787A19598253ECD55F652C12BEA8CA871C75E3C5D8774ACB3C3F229579ED791)
