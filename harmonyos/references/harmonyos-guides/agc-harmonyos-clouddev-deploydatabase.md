---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploydatabase
title: 部署云数据库
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 部署云数据库
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:0aa64543b7101cef89cbad9384e3f60e1a9da19123f86db0ee22b0b5ff8d248f
---

完成数据条目创建后，您可以直接部署该数据条目。您也可以等所有对象类型和数据条目开发完成后，再统一批量部署到HarmonyOS 开发者中心。

**说明** 

* 部署到HarmonyOS 开发者中心的存储区数量不得超过4个，否则会导致部署失败，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”错误。如HarmonyOS 开发者中心当前已存在4个存储区，请将数据部署到已有的存储区，或者删除已有存储区后再部署新的存储区。**需要注意的是，删除存储区，该存储区内的数据也将一并删除，且不可恢复。**
* 对象类型中的fieldType等字段信息，部署到HarmonyOS 开发者中心后，请勿在本地再做修改。例如，fieldType设置为String，对象类型部署成功后，又在本地修改fieldType为Integer，再次部署将失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”错误。如需更改fieldType等字段信息，请先删除云端部署的对象类型。**需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。**

部署云数据库的操作如下：

1. 右击“clouddb”目录，选择“Deploy Cloud DB”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/nsI4xzHISP6hqGFiY-Uv5Q/zh-cn_image_0000002179338588.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=35C878B627174F967BBF41E9B564E8F2E9415DF1571E041242AE4177D2751DD1)
2. 您可在底部状态栏右侧查看云数据库打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示云数据库已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/N3AcmIMGS9eBO3mpWSj6Cw/zh-cn_image_0000002179338568.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F14E76EBEAE9FC1CE651361670AA67ED1FA57C00F03C39DB92843CAD46C2045)

   **注意** 

   云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。

   如果后续又在本地工程修改了对象类型，请重新部署云数据库，DevEco Studio将自动更新schema.json文件；如果后续在HarmonyOS 开发者中心修改了对象类型，您需[手动从HarmonyOS 开发者中心导出schema.json文件](../AppGallery-connect-Guides/agc-clouddb-agcconsole-objecttypes-0000001127675459.md#section1558018208151)，拷贝至本地工程的“AppScope/resources/rawfile”目录下。否则，可能导致schema.json文件中的对象类型和代码中的对象类型不一致，端侧访问云数据库时提示[1008230002](../harmonyos-references/errorcode-cloudfoundation.md#section1008230002-云数据库schema配置错误)错误。
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Ddt2JFP2S_CB6YmuYJzFrA/zh-cn_image_0000002179338580.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=6830BE33D7C20ABF2BAA797BC7A07E7F0D21BD3CC3975D25D39F04C10989047D)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud DB”下的“Go to console”，进入当前项目的云数据库服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Q8ZpkQeAQwyceze_V87-VQ/zh-cn_image_0000002179338576.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=38751D3ADB0283D80713AC2192A58CEE7B01B5C993A191A3CFD1AB0F1F49EBB1)
5. 分别点击“对象类型”、“存储区”与“数据”页签，可查看到本地开发的云数据库资源均已成功部署至HarmonyOS 开发者中心。

   部署成功后，您便可以从端侧访问云数据库了，具体请参见[在端侧访问云数据库](agc-harmonyos-clouddev-invokeclouddatabase.md)。

   您还可以在HarmonyOS 开发者中心继续编辑以上部署的云数据库资源，具体操作请参考[管理数据库](../AppGallery-connect-Guides/agc-clouddb-managingclouddb-0000001080815650.md)。

   对象类型“Post”与“objecttype1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/GusVTYZCRFSIYPg7ZDpvPA/zh-cn_image_0000002214704533.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BCC0399D8D742AF393CB5437FFAB3B345CFF2A376941BF5D4C0DCE954092876)

   对象类型“Post”所属存储区“Demo”、“objecttype1”所属存储区“cloudDBZoneName1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/EIAguD5bTPepS7Te5jAjfA/zh-cn_image_0000002179498272.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEF78F81BA2938B89637B49AB82AE6EC26287C53B1CA308B5EA6E020CF6E3B23)

   “d\_Post.json”内的数据条目、“d\_objecttype1.json”内的数据条目：

   **说明** 

   部署对象类型或数据条目JSON文件，实际是部署JSON文件内包含的对象类型或数据条目。因此，您在HarmonyOS 开发者中心查看到的将是一个个对象类型或者一条条数据，而非JSON文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/suyZRZInSwSm-RpGaAJ2pQ/zh-cn_image_0000002214704537.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C9E38A456D7B55BE70A1C47B01033DDD019B46B97CDBB88078A26D679A02DAD)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/hZkNbeD9Skafk-BDe1tMEw/zh-cn_image_0000002179338572.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=1503F1E919F91C4BD3E2140063D9EDF87553DED940B7BE6AED5CAA8140056A21)
