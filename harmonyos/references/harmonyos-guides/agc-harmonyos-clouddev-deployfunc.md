---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:a9eb3d6a06417ed55d5b436769a386d712bb6b57eb05c9b54c7a21f2fbc60144
---

完成函数代码开发后，您可将函数部署到HarmonyOS 开发者中心，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到HarmonyOS 开发者中心。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   **说明** 

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到HarmonyOS 开发者中心。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/1Wolv2EyQmemYIOTfVSNxg/zh-cn_image_0000002179498368.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=44AD0B2E59584BB47AFF88C8C5E00B132763384D5BA3C36F91854A16EEC335C1)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/pkVZcVJHRU6uDRDXufVXIw/zh-cn_image_0000002179498360.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0375A15A3F187745468E3BCCA70365ABCCC961512545033EEA3466E228B6872)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/5toXyj-9Q0ycN0Nsqs5cTg/zh-cn_image_0000002214858997.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C5E3B1CD1C0BC7FC2FD468E87A5055E107B43BBD98C0B4387F13AD17CFD3CE9)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/k__TaQVlQqyn7dMg988w_g/zh-cn_image_0000002214704617.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5C1BB1A2D907E399296BB49613142041917172DCBC663723A5F386CAE87DBF0)
5. 查看到“my-cloud-function”函数已成功部署至HarmonyOS 开发者中心，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](agc-harmonyos-clouddev-invokecloudfunc.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/KXTY602YSzShlN7fPxYkEg/zh-cn_image_0000002179338680.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=B00A85C7F5827ED95FFBF93B7D2BE9A39EC9D451938522D35F155DC66B3983CC)
