---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploydatabase
title: 部署云数据库
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 部署云数据库
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:06e3112a383549b9dc7a70d59399e2d5aaca1aca8d64b9a92910c4bf56c1d931
---

完成数据条目创建后，您可以直接部署该数据条目。您也可以等所有对象类型和数据条目开发完成后，再统一批量部署到HarmonyOS 开发者中心。

**说明** 

* 部署到HarmonyOS 开发者中心的存储区数量不得超过4个，否则会导致部署失败，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”错误。如HarmonyOS 开发者中心当前已存在4个存储区，请将数据部署到已有的存储区，或者删除已有存储区后再部署新的存储区。**需要注意的是，删除存储区，该存储区内的数据也将一并删除，且不可恢复。**
* 对象类型中的fieldType等字段信息，部署到HarmonyOS 开发者中心后，请勿在本地再做修改。例如，fieldType设置为String，对象类型部署成功后，又在本地修改fieldType为Integer，再次部署将失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”错误。如需更改fieldType等字段信息，请先删除云端部署的对象类型。**需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。**

部署云数据库的操作如下：

1. 右击“clouddb”目录，选择“Deploy Cloud DB”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/Bmnu6h5KTTCCV98qmfVFpg/zh-cn_image_0000002179338588.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=275A578E29592D802C9026A799CB1C75601DB90546E7E8BA2680DA5E8AC9A35D)
2. 您可在底部状态栏右侧查看云数据库打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示云数据库已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/mjjUwY1fQhOu6Nl5UDi-pA/zh-cn_image_0000002179338568.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=11C717FA22F816CA7C03127066D8410CEE45FC95F6EF64F317CFDB7FC9ABE34B)

   **注意** 

   云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。

   如果后续又在本地工程修改了对象类型，请重新部署云数据库，DevEco Studio将自动更新schema.json文件；如果后续在HarmonyOS 开发者中心修改了对象类型，您需[手动从HarmonyOS 开发者中心导出schema.json文件](../AppGallery-connect-Guides/agc-clouddb-agcconsole-objecttypes-0000001127675459.md#section1558018208151)，拷贝至本地工程的“AppScope/resources/rawfile”目录下。否则，可能导致schema.json文件中的对象类型和代码中的对象类型不一致，端侧访问云数据库时提示[1008230002](../harmonyos-references/errorcode-cloudfoundation.md#section1008230002-云数据库schema配置错误)错误。
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/1Ahin04OSGCYNdUdhlHWzg/zh-cn_image_0000002179338580.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=81D0752FCFB61D4EEC9F3FA6AC8313FBD042DBC0A61032AB543804A232A8D8EF)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud DB”下的“Go to console”，进入当前项目的云数据库服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/PWKHclZvTyqFX-SuXZCrGw/zh-cn_image_0000002179338576.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=099D6BFE1ABD92F4A2A09D9E9590670AFDC2D7667D02F9FFD18AA3F0E514C728)
5. 分别点击“对象类型”、“存储区”与“数据”页签，可查看到本地开发的云数据库资源均已成功部署至HarmonyOS 开发者中心。

   部署成功后，您便可以从端侧访问云数据库了，具体请参见[在端侧访问云数据库](agc-harmonyos-clouddev-invokeclouddatabase.md)。

   您还可以在HarmonyOS 开发者中心继续编辑以上部署的云数据库资源，具体操作请参考[管理数据库](../AppGallery-connect-Guides/agc-clouddb-managingclouddb-0000001080815650.md)。

   对象类型“Post”与“objecttype1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/MYmUGzZFSCabR2QM5OiC-w/zh-cn_image_0000002214704533.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=A21F947ED6CCF98C5027BFBAD36F35AEBDA95A89708BC329B5E0300BC26FC6C8)

   对象类型“Post”所属存储区“Demo”、“objecttype1”所属存储区“cloudDBZoneName1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/1KcS8tpnRje9hkHcjyHeyA/zh-cn_image_0000002179498272.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA0A8E9FB1EB9B64F36583C3953C6F9E5BA92B7BCEFE19445D6A393E8B6EFFCB)

   “d\_Post.json”内的数据条目、“d\_objecttype1.json”内的数据条目：

   **说明** 

   部署对象类型或数据条目JSON文件，实际是部署JSON文件内包含的对象类型或数据条目。因此，您在HarmonyOS 开发者中心查看到的将是一个个对象类型或者一条条数据，而非JSON文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/y711zymOQ0SOxQXAsSFq1w/zh-cn_image_0000002214704537.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=612CDC6471E2156FEBC67F9465AEAE144BB6A1672B86958A80E882275C044174)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/c5MCktg2R-Op50xKcyFzqw/zh-cn_image_0000002179338572.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB10520D1C9E0F9DA11D3CDD59180B34FB5C14E6885F8A306CC3250E0CDD97DB)
