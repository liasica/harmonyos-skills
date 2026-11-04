---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploycloudobj
title: 部署云对象
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 部署云对象
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:19+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:9596b6db62c8d4f2b535591a34c4d219323c211c14a97ce4aa59e9d6dbf49275
---

完成云对象代码开发后，您可将云对象部署到HarmonyOS 开发者中心，支持单个部署和批量部署。

单个部署仅部署选中的云对象，批量部署则会将整个“cloudfunctions”目录下的所有云对象同时部署到HarmonyOS 开发者中心。

下文以部署单个云对象“my-cloud-object”为例，介绍如何部署云对象。

1. 右击“my-cloud-object”云对象目录，选择“Deploy 'my-cloud-object'”。

   **说明** 

   如需批量部署多个云对象，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有云对象。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到HarmonyOS 开发者中心。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/cM-7hVGETXGs1pzrMarimg/zh-cn_image_0000002179338528.png)
2. 您可在底部状态栏右侧查看云对象打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前云对象已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/DOgnhN5HTN291yGk3-28gA/zh-cn_image_0000002214704473.png)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/9OObWj3uTRiM98n6QFB3kA/zh-cn_image_0000002179498224.png)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/Tffi1QnfSueq_KrKuIX33g/zh-cn_image_0000002214858857.png)
5. 查看到“my-cloud-object”云对象已成功部署至HarmonyOS 开发者中心，云对象名称与本地工程的云对象目录名相同。

   部署成功后，您便可以从端侧调用云对象了，具体请参见[在端侧调用云对象](agc-harmonyos-clouddev-invokecloudobj.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/FiW5aGXYQFqFiWY89WG9vA/zh-cn_image_0000002179338540.png)
