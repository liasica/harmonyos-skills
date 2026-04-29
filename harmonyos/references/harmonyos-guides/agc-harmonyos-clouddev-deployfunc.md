---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:00+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:1aea8cf6222ff47938e62ed9c9df00d5ec391ddd824c176f9df53718b5da3c71
---

完成函数代码开发后，您可将函数部署到AGC云端，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到AGC云端。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   说明

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/W1EL6ve1SLGH6YGpFI8nUw/zh-cn_image_0000002179498368.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=F0EF7486E930FA7FB15D15A9276BB30993DFD2DB3FC4520EA4C3027B737AED39)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/hk25xhH_R7e17iIxNy3c6A/zh-cn_image_0000002179498360.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=B4DE55D8085030FBCE9420FD1B82AF67044C8860D9F8B0E4B3F2641F96218EF8)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/AOe48WAmRTKiWA7Uor6dKw/zh-cn_image_0000002214858997.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=1330D2C09EE5CFC7A45303654265C7CDD6091FFC8023C6AF1BC451126AE55A0F)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/7_db1Ew5Qe6g24uqLvAuRA/zh-cn_image_0000002214704617.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=4CCF8E90B9C27F354B3F279EE0DA00A7DA762835AD5EA813D25D1D020D3F57CD)
5. 查看到“my-cloud-function”函数已成功部署至AGC云端，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](agc-harmonyos-clouddev-invokecloudfunc.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/W8HVu3VzQJi6ziAA5d-48Q/zh-cn_image_0000002179338680.png?HW-CC-KV=V1&HW-CC-Date=20260429T054458Z&HW-CC-Expire=86400&HW-CC-Sign=B364FAC560C19B17321F1A3B5C45C3EEF74E6ACA6D6D06078FDE0C663BBE6684)
