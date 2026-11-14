---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:e9e6bae1ee2478bcfcb208467924c01f97f17874c3ca2b73fa1ed763e2ae6782
---

完成函数代码开发后，您可将函数部署到HarmonyOS 开发者中心，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到HarmonyOS 开发者中心。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   **说明** 

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到HarmonyOS 开发者中心。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/fZyx96o9RtiVmzyeO4a_4Q/zh-cn_image_0000002179498368.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=75CACB2FE5CAEF3D67BDCCC29195CBAC3E7E6465520EC75444678A05BD0257B5)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/KLIOKk_kTOa-5zSDrAo1Lg/zh-cn_image_0000002179498360.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAC861DA5A57C9A40D9ADA37D0F70C3EA28BF9548C5124C20D14579446065753)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/vAm71UrPRQqvZlGhJLuzbA/zh-cn_image_0000002214858997.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=50ABDA1449A14991F008DB3F94C52DE535394462D3D1A033183566B4E6C85DD6)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/Go9jW0nkRRyjL-5A5LyqxA/zh-cn_image_0000002214704617.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED02AD12B41B06299980BFDC29F520CAB5AE1DF57D0BCBA5E4164A63F2D506F6)
5. 查看到“my-cloud-function”函数已成功部署至HarmonyOS 开发者中心，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](agc-harmonyos-clouddev-invokecloudfunc.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/5RuGNhwnQ0SxWEFYbc8dyA/zh-cn_image_0000002179338680.png?HW-CC-KV=V1&HW-CC-Date=20261114T004849Z&HW-CC-Expire=31536000000&HW-CC-Sign=44C39F3E843DC336B437CC91D2835B3D5C53E1CA6F80B36363CA313D0420A556)
