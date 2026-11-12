---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:cc335ab485672a5ee2ae9aa209a0583db325823359902e138b360741bd48255b
---

完成函数代码开发后，您可将函数部署到HarmonyOS 开发者中心，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到HarmonyOS 开发者中心。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   **说明** 

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到HarmonyOS 开发者中心。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/4GLc_368TUCyeNR-oG8ZFQ/zh-cn_image_0000002179498368.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=83FCB981245BCE091C4B765127A4FDB5E73347F6BE4F5E0521CFEF575FBFD7E3)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/s62_ukLRSnuALMI2LK_q8w/zh-cn_image_0000002179498360.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC1895881458FBE663D3DEFBB02457D1495248F146C4BBD85B82632C02801187)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/QFNUgIQAT2yAbPFWkBlQQA/zh-cn_image_0000002214858997.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=0231134CE5DB66EE4CDDA54BB28BECEA1C3920934B5C41C65566E94D99A174EE)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/CfUxTAIZTFi83ff-irorIg/zh-cn_image_0000002214704617.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=644D1E46143DDBED0F71922A0B67CB0640D0D0A0F9D81524DDE5F8C729E798AD)
5. 查看到“my-cloud-function”函数已成功部署至HarmonyOS 开发者中心，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](agc-harmonyos-clouddev-invokecloudfunc.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/H-fUW_JlSlOGqv6eXoNN2A/zh-cn_image_0000002179338680.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1626E1D7834EEBDED095252F5B54FFEE089E2ED96BB9948DF22B1A297A76197C)
