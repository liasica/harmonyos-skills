---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deployfunc
title: 部署函数
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 部署函数
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:1822de174894a57277a911bba24e386c2685feff29e1aa948ffec06413688bf4
---

完成函数代码开发后，您可将函数部署到HarmonyOS 开发者中心，支持单个部署和批量部署。

单个部署仅部署选中的函数，批量部署则会将整个“cloudfunctions”目录下的所有函数同时部署到HarmonyOS 开发者中心。

下文以部署单个函数“my-cloud-function”为例，介绍如何部署函数。

1. 右击“my-cloud-function”函数目录，选择“Deploy 'my-cloud-function'”。

   **说明** 

   如需批量部署多个函数，右击“cloudfunctions”目录，选择“Deploy Cloud Functions”即可部署该目录下所有函数。如“cloudfunctions”目录下同时存在云函数和云对象，云函数和云对象将会被一起部署到HarmonyOS 开发者中心。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/_ABD2bvvRDWntKE7TEq3nw/zh-cn_image_0000002179498368.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=93B1C7376451BB78E2351362070CEC8E56B1DC594B55ADCE81B1A9FA65FAEC7F)
2. 您可在底部状态栏右侧查看函数打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示当前函数已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/U6pa8DOcT6yEJqyJ6dpWOQ/zh-cn_image_0000002179498360.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B7F1E4DC6BB029DD5B4BB0B660E2D84FD162E20B25D08A138AA01AA2311C7E9)
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/fQXhMHRyQP66CHyprTIlGA/zh-cn_image_0000002214858997.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD2F8A3E571AD2627B3E4BD7DA5F019BFC5F6583E51D86DD621AE51714C0EB00)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud Functions”下的“Go to console”，进入当前项目的云函数服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/yNUmb5LbTQqqxSeQr8QSOg/zh-cn_image_0000002214704617.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=C779A43680B9FADCE5D91202B3F22145156155C729C1EC15BBEA38CE8E63898A)
5. 查看到“my-cloud-function”函数已成功部署至HarmonyOS 开发者中心，函数名称与本地工程的函数目录名相同。

   部署成功后，您便可以从端侧调用云函数了，具体请参见[在端侧调用云函数](agc-harmonyos-clouddev-invokecloudfunc.md)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/mIxT2kK-S26K1sqyuTnCEg/zh-cn_image_0000002179338680.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=B1F8C6D640FEA5A7A1A1FB982AF063F0CEA5FAF25E1C51728F85033EA9F1BA72)
