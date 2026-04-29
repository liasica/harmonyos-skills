---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploycloudobj
title: 部署云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 部署云对象
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:34c73207f9d3c8016f88732669b2340438d63e05c38bb15e4bbc16064b412124
---

完成云对象代码开发后，您可将云对象部署到AGC云端，支持单个部署和批量部署。

单个部署仅部署选中的云对象，批量部署则会将整个“cloudfunctions”目录下的所有云对象同时部署到AGC云端。

下文以部署单个云对象“my-cloud-object”为例，介绍如何部署云对象。

1. 右击“my-cloud-object”云对象目录，选择“Deploy 'my-cloud-object'”。

   说明

   如需批量部署多个云对象，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有云对象。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/bKhnm3kfT-eX70EJwlC6Pw/zh-cn_image_0000002179338528.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=8AAFB149AADFC90EA88EC1E53DBDB79331E4AD305B7A8E717A3F374994DA4813)
2. 您可在底部状态栏右侧查看云对象打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前云对象已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/sJGzveMTTWSnex5kofw_zQ/zh-cn_image_0000002214704473.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=01267425735898B84F632D7301D0AED93FF8C44CA1F7426E31025A3205EC6173)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/AQEHUpzBSuq61AeU9IcQ6w/zh-cn_image_0000002179498224.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=C83E47908339D8F7B83CC32A4CEFE99EB3621E12E29EA46AF8EDF3276FA99457)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/31sWt2bDT72GfhY-PzUXZg/zh-cn_image_0000002214858857.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=BC7F2043A72267C9F28CF6046CBF427903B251A09CA3542F2F4FCA64B7E074A8)
5. 查看到“my-cloud-object”云对象已成功部署至AGC云端，云对象名称与本地工程的云对象目录名相同。

   部署成功后，您便可以从端侧调用云对象了，具体请参见[在端侧调用云对象](agc-harmonyos-clouddev-invokecloudobj.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/3BB1ivYkRdyEkiIQQKq4Mw/zh-cn_image_0000002179338540.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=A7FA8FFD60EF3FD8C7FCB7AE8187993E05BA8CAEFC420D7CB983E6A8990A955F)
