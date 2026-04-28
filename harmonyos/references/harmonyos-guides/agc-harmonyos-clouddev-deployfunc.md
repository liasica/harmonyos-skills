---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:03+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:117ad54c0173378323615be6d912ae4740aa3a8c84ad6b0fb2138e8ebcf56a39
---

完成函数代码开发后，您可将函数部署到AGC云端，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到AGC云端。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   说明

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/qyavU154TkiIK1cSXA-EjQ/zh-cn_image_0000002179498368.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=9320BEA154468D72A2E5996C7903064994592FF8053F577A342A7C0029465BC4)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/1vJxEF_EQBWQC5k0VPbsTg/zh-cn_image_0000002179498360.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=3F93CA6DAE75A952E44D649C50D1BA99EFC42CC3E15CB97D7612A9B3D262DB01)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/NaUXb5oESP2mDrsfA4AQlQ/zh-cn_image_0000002214858997.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=008DD6DE0FAF1066928B2617287F19AF8CB5F7A193B7B07C3B7EF88C40B75805)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/TRy7XPC5T4enpC6M9AIWRA/zh-cn_image_0000002214704617.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=06B9D4CB912CA1EDDADFA8B86A3D87F0D3C0A82631AF6ED2834FD5A1251BB0F2)
5. 查看到“my-cloud-function”函数已成功部署至AGC云端，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](agc-harmonyos-clouddev-invokecloudfunc.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ikklhqqwQTW9g1w0jgnMLg/zh-cn_image_0000002179338680.png?HW-CC-KV=V1&HW-CC-Date=20260427T235501Z&HW-CC-Expire=86400&HW-CC-Sign=306D1A0D6F0F7B0C3AC4B94F3B0816A0AEC547C72970EB508CF67E4E36C9932A)
