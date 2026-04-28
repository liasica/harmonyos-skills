---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploycloudobj
title: 部署云对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:06+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:20c0f30ae46d9b9aa39627ae17d6a0812079ff437ff2afb2337f2a0687423476
---

完成云对象代码开发后，您可将云对象部署到AGC云端，支持单个部署和批量部署。

单个部署仅部署选中的云对象，批量部署则会将整个“cloudfunctions”目录下的所有云对象同时部署到AGC云端。

下文以部署单个云对象“my-cloud-object”为例，介绍如何部署云对象。

1. 右击“my-cloud-object”云对象目录，选择“Deploy 'my-cloud-object'”。

   说明

   如需批量部署多个云对象，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有云对象。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到AGC云端。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/vfvfuFaLTRu_wV3BJ7gR-w/zh-cn_image_0000002179338528.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=53DE93E3236AEA93F816D5C0AC12BB8C7C819710D23C5E0E4E25B99B4CD25851)
2. 您可在底部状态栏右侧查看云对象打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前云对象已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/i4Y-f12AQBaP0XH7ZR9AYQ/zh-cn_image_0000002214704473.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=FB398538E1704E3C2B8EA3D714801AD80AFFA4672054B29EFC222CBB32BD24B5)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/SWSah6UfQuGlYIlwD0yFQw/zh-cn_image_0000002179498224.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=9FC1A91D43FDCD8BF9BE0753451B185A215201886108EC5796B3AA8BEADF4889)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/F8XayHGPRSimEAPdjXHjqA/zh-cn_image_0000002214858857.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=6B13071A0134B52B3B4CD6A4F7178C8369426366E4656B70A94C45B3D3C8B088)
5. 查看到“my-cloud-object”云对象已成功部署至AGC云端，云对象名称与本地工程的云对象目录名相同。

   部署成功后，您便可以从端侧调用云对象了，具体请参见[在端侧调用云对象](agc-harmonyos-clouddev-invokecloudobj.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/lOAM5H74QJOTC0ZC2HfVdg/zh-cn_image_0000002179338540.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=ABD210691DE4A4E89D07EBF1F9028536C1273866FF35FDFD48C59DF7BEEEE19B)
