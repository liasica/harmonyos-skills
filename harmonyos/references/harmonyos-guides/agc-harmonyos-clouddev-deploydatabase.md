---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploydatabase
title: 部署云数据库
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 部署云数据库
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:03+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3b9ee54387eab9c176f95361dc7a3cfe1e8888559f717b972304c895f6758c14
---

完成数据条目创建后，您可以直接部署该数据条目。您也可以等所有对象类型和数据条目开发完成后，再统一批量部署到AGC云端。

说明

* 部署到AGC云端的存储区数量不得超过4个，否则会导致部署失败，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”错误。如AGC云端当前已存在4个存储区，请将数据部署到已有的存储区，或者删除已有存储区后再部署新的存储区。**需要注意的是，删除存储区，该存储区内的数据也将一并删除，且不可恢复。**
* 对象类型中的fieldType等字段信息，部署到AGC云端后，请勿在本地再做修改。例如，fieldType设置为String，对象类型部署成功后，又在本地修改fieldType为Integer，再次部署将失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”错误。如需更改fieldType等字段信息，请先删除云端部署的对象类型。**需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。**

部署云数据库的操作如下：

1. 右击“clouddb”目录，选择“Deploy Cloud DB”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/ZuI4R4TZSgew70dKEQerww/zh-cn_image_0000002179338588.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=A39A8A671712C59EE5538262E4527CF87FA9BEE03C957BFABFDDE2A0DFFA46BB)
2. 您可在底部状态栏右侧查看云数据库打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示云数据库已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/EwR--E2nREG7C-EEn3HqiQ/zh-cn_image_0000002179338568.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=FDE827F4FAB5B0E13A7BBA8185D0BC91E95CCBC39BA69B20C1EE248A1D29C400)

   注意

   云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。

   如果后续又在本地工程修改了对象类型，请重新部署云数据库，DevEco Studio将自动更新schema.json文件；如果后续在AGC云侧修改了对象类型，您需[手动从AGC控制台导出schema.json文件](../AppGallery-connect-Guides/agc-clouddb-agcconsole-objecttypes-0000001127675459.md#section1558018208151)，拷贝至本地工程的“AppScope/resources/rawfile”目录下。否则，可能导致schema.json文件中的对象类型和代码中的对象类型不一致，端侧访问云数据库时提示示[1008230002](../harmonyos-references/errorcode-cloudfoundation.md#section1008230002-云数据库schema配置错误)错误。
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/6F1ryzLERTa_wdONwSyZ2w/zh-cn_image_0000002179338580.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=153DF5F0124DA527520779B598930898E714A6112217748C9EBD9AEAD00A4913)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud DB”下的“Go to console”，进入当前项目的云数据库服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/oRHR_vBlSj2mzH5NlS5IfA/zh-cn_image_0000002179338576.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=5C323B76AE6E55F08BCD59B3348F8BD672FB0346F012EFE63B1B43F8E6C41924)
5. 分别点击“对象类型”、“存储区”与“数据”页签，可查看到本地开发的云数据库资源均已成功部署至AGC云端。

   部署成功后，您便可以从端侧访问云数据库了，具体请参见[在端侧访问云数据库](agc-harmonyos-clouddev-invokeclouddatabase.md)。

   您还可以在AGC控制台继续编辑以上部署的云数据库资源，具体操作请参考[管理数据库](../AppGallery-connect-Guides/agc-clouddb-managingclouddb-0000001080815650.md)。

   对象类型“Post”与“objecttype1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/UaSiegjoRzKtFy-FaaQ52Q/zh-cn_image_0000002214704533.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=969B69DFB73D85BEC06508823973829056A20398B5A04D4A46F1CE325C40FC73)

   对象类型“Post”所属存储区“Demo”、“objecttype1”所属存储区“cloudDBZoneName1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/7-9pZwVwSLKJQAH332hs-A/zh-cn_image_0000002179498272.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=6534D34F05AD0E4318309B8031560736E378E5F34BA3E9153944BDFBB484D30A)

   “d\_Post.json”内的数据条目、“d\_objecttype1.json”内的数据条目：

   说明

   部署对象类型或数据条目JSON文件，实际是部署JSON文件内包含的对象类型或数据条目。因此，您在AGC控制台查看到的将是一个个对象类型或者一条条数据，而非JSON文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/gjbag2COQRaYOHIfnYVXhA/zh-cn_image_0000002214704537.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=DAC578D21058591798B8DFB2DEC6114AD44FC6A9F6C55AD457204E2A02AB5837)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/IBVTLSkJSzaTiDX_mCASJQ/zh-cn_image_0000002179338572.png?HW-CC-KV=V1&HW-CC-Date=20260429T054502Z&HW-CC-Expire=86400&HW-CC-Sign=ACEB2393F9325E4562311BC2A01A6F5691CAC393393884EDF3B52AEE082E7BA1)
