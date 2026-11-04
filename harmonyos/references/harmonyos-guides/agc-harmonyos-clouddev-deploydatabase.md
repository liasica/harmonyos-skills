---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-deploydatabase
title: 部署云数据库
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 部署云数据库
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:19+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:dd691c50f94372e3f18745227d086113ce5a86d134f8ac1b22a4a0f7e36677d1
---

完成数据条目创建后，您可以直接部署该数据条目。您也可以等所有对象类型和数据条目开发完成后，再统一批量部署到HarmonyOS 开发者中心。

**说明** 

* 部署到HarmonyOS 开发者中心的存储区数量不得超过4个，否则会导致部署失败，提示“clouddb deploy failed. Reason is the number of CloudDBZone exceeds the limit.”错误。如HarmonyOS 开发者中心当前已存在4个存储区，请将数据部署到已有的存储区，或者删除已有存储区后再部署新的存储区。**需要注意的是，删除存储区，该存储区内的数据也将一并删除，且不可恢复。**
* 对象类型中的fieldType等字段信息，部署到HarmonyOS 开发者中心后，请勿在本地再做修改。例如，fieldType设置为String，对象类型部署成功后，又在本地修改fieldType为Integer，再次部署将失败，提示“clouddb deploy failed. Reason is existing fields cannot be modified.”错误。如需更改fieldType等字段信息，请先删除云端部署的对象类型。**需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。**

部署云数据库的操作如下：

1. 右击“clouddb”目录，选择“Deploy Cloud DB”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ECNmG0e7Rvq_bywELeEp2A/zh-cn_image_0000002179338588.png)
2. 您可在底部状态栏右侧查看云数据库打包与部署进度。

   请您耐心等待，直至出现“Deploy successfully”消息，表示云数据库已成功部署。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/pSGT8cX_SJ6EaPjjR-GlJw/zh-cn_image_0000002179338568.png)

   **注意** 

   云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。

   如果后续又在本地工程修改了对象类型，请重新部署云数据库，DevEco Studio将自动更新schema.json文件；如果后续在HarmonyOS 开发者中心修改了对象类型，您需[手动从HarmonyOS 开发者中心导出schema.json文件](../AppGallery-connect-Guides/agc-clouddb-agcconsole-objecttypes-0000001127675459.md#section1558018208151)，拷贝至本地工程的“AppScope/resources/rawfile”目录下。否则，可能导致schema.json文件中的对象类型和代码中的对象类型不一致，端侧访问云数据库时提示[1008230002](../harmonyos-references/errorcode-cloudfoundation.md#section1008230002-云数据库schema配置错误)错误。
3. 在菜单栏选择“Tools > CloudDev”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/tifnvp47QFir6f2l4QP5ow/zh-cn_image_0000002179338580.png)
4. 在打开的CloudDev面板中，点击“Serverless > Cloud DB”下的“Go to console”，进入当前项目的云数据库服务页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Mi9UvVSgR8e7khkq6TTiNQ/zh-cn_image_0000002179338576.png)
5. 分别点击“对象类型”、“存储区”与“数据”页签，可查看到本地开发的云数据库资源均已成功部署至HarmonyOS 开发者中心。

   部署成功后，您便可以从端侧访问云数据库了，具体请参见[在端侧访问云数据库](agc-harmonyos-clouddev-invokeclouddatabase.md)。

   您还可以在HarmonyOS 开发者中心继续编辑以上部署的云数据库资源，具体操作请参考[管理数据库](../AppGallery-connect-Guides/agc-clouddb-managingclouddb-0000001080815650.md)。

   对象类型“Post”与“objecttype1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/UbTcHV65R_yXDjTlY3OdCw/zh-cn_image_0000002214704533.png)

   对象类型“Post”所属存储区“Demo”、“objecttype1”所属存储区“cloudDBZoneName1”：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/A330T74QQBuR1n5G3xNjDw/zh-cn_image_0000002179498272.png)

   “d\_Post.json”内的数据条目、“d\_objecttype1.json”内的数据条目：

   **说明** 

   部署对象类型或数据条目JSON文件，实际是部署JSON文件内包含的对象类型或数据条目。因此，您在HarmonyOS 开发者中心查看到的将是一个个对象类型或者一条条数据，而非JSON文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Ygam8XI7Q6OpwhP996o8aA/zh-cn_image_0000002214704537.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/igX6POtXTGinRNU4Ff5j8w/zh-cn_image_0000002179338572.png)
