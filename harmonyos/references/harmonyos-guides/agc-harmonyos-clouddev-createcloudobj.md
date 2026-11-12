---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createcloudobj
title: 创建云对象
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 创建云对象
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:6ecc59f5da9f05ad870baf2b2d3be8444c4b17ef47c43ed49586af13485f02a6
---

首先您需要在云侧工程下创建云对象。

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/FC5jKsu5QoapKz2riOX3tw/zh-cn_image_0000002383015456.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4D10EC87FEA297BC6681493ED9CAF6C279D95AE38A26369450D433FC48042F8C)
2. 在“Select the Cloud Function Type”栏选择“Cloud Object”，输入云对象名称（如“my-cloud-object”），点击“OK”。

   与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/7ONfLyMmQ6-xmUxCGpFXmQ/zh-cn_image_0000002179498304.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=668958178DEC81DB271F98B0DAF3A9D30BF3E601AAC6BC1DBAEDAF1DA170B8BC)

   “cloudfunctions”目录下生成新建的云对象目录，目录下主要包含如下文件：
   * 云对象配置文件“function-config.json”：包含handler、触发器等信息。
     + handler: 云对象的入口模块及云对象导出的类，通过“.”连接。
     + functionType：表示函数类型，“0”表示云函数，“1”表示云对象。
     + triggers：定义了云对象使用的触发器类型，当前云对象仅支持HTTP触发器。

     **说明** 

     云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/oVRIRQWBSJi2FTpp9EU99Q/zh-cn_image_0000002214858949.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3E21D84912A7BC5AA9A1954DF611128754B8FDDBEEAB7F4F7B23C797FE5B576)
   * 云对象入口文件“*xxx*.ts”（如“myCloudObject.ts”）：在此文件中编写云对象代码。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/_EA_eoPSTqKBV2t7roKhsw/zh-cn_image_0000002214704565.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3B29E875067D2BE2A71A3F4660B894A0C9C29C4C88D4ACFBCFA0A7E3A57813D)
   * 云对象依赖配置文件“package.json”：在此文件中添加依赖。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/JeZnA2yxT4qbM0rsHyL_YA/zh-cn_image_0000002179338620.png?HW-CC-KV=V1&HW-CC-Date=20261112T233220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BDBD0896318B8D2C42E906FE7A120A2FFEDFBEACB4880DE8726585A5A920963)
