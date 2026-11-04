---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:19+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:3c2dd342252d42e8fd365cf38d0e91b65f55ac3ef053e490f3f8dbae2dfe6d55
---

完成函数代码开发后，您可将函数部署到HarmonyOS 开发者中心，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到HarmonyOS 开发者中心。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   **说明** 

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到HarmonyOS 开发者中心。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/phnw8O_TTvqtb4OBblDntA/zh-cn_image_0000002179498368.png)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/chtWrvIpRaeLrLM1xvcyZw/zh-cn_image_0000002179498360.png)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/x-7tE5l4STei7iiOl556HQ/zh-cn_image_0000002214858997.png)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/4Hz5PC-nTWqR7SseZLqd5Q/zh-cn_image_0000002214704617.png)
5. 查看到“my-cloud-function”函数已成功部署至HarmonyOS 开发者中心，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](agc-harmonyos-clouddev-invokecloudfunc.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/ENTz9acGSK2aNQc9wzF6_A/zh-cn_image_0000002179338680.png)
