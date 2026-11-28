---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createcloudobj
title: 创建云对象
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 创建云对象
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:29+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:6a77f0a92de79638e625a2c5aa376ef22b2e572c97fdcd6478355cd9a8662019
---

首先您需要在云侧工程下创建云对象。

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/7tk42sfBTWKOmeLE6BD0XQ/zh-cn_image_0000002383015456.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=B9D539DF509AA4B70D9591E18BC4B8DBCD32706E57F1B24A80837C0AB4649CBC)
2. 在“Select the Cloud Function Type”栏选择“Cloud Object”，输入云对象名称（如“my-cloud-object”），点击“OK”。

   与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/cNHf7v42Ru642kqDK7sSTw/zh-cn_image_0000002179498304.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=220A52E961370524BF2912E20123108219371CC33798A3F0FF66AF4D6F4DCADC)

   “cloudfunctions”目录下生成新建的云对象目录，目录下主要包含如下文件：
   * 云对象配置文件“function-config.json”：包含handler、触发器等信息。
     + handler: 云对象的入口模块及云对象导出的类，通过“.”连接。
     + functionType：表示函数类型，“0”表示云函数，“1”表示云对象。
     + triggers：定义了云对象使用的触发器类型，当前云对象仅支持HTTP触发器。

     **说明** 

     云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Tmys3Ly7TzudWn37eP6IWg/zh-cn_image_0000002214858949.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0ADEF193E3100DBEAA1AA26CE345BE2257D0D7689497C5D2FBD03002CEAA2E9)
   * 云对象入口文件“*xxx*.ts”（如“myCloudObject.ts”）：在此文件中编写云对象代码。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/DcIvnivAQ9mYMG3pirJhRg/zh-cn_image_0000002214704565.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C2607B1C3FC3C8DCDE8AE534F66E8D094A3186A24A5FF2D59971DCA971064E5)
   * 云对象依赖配置文件“package.json”：在此文件中添加依赖。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/-1LRk5h_QCSMEr92WpNDVw/zh-cn_image_0000002179338620.png?HW-CC-KV=V1&HW-CC-Date=20261128T023429Z&HW-CC-Expire=31536000000&HW-CC-Sign=2993D46A0F74794AC19095E71D4D827034939F0D8052110C2AB827699B7A373F)
