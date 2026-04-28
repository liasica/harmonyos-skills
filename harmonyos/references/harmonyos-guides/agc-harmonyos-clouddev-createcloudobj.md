---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createcloudobj
title: 创建云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 创建云对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:03+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:bbd4db657a53c3bf8c4b89ebf25fde0d993156c7bbe1d34fab95f69e77984474
---

首先您需要在云侧工程下创建云对象。

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/QCs1eDyoRlyWaRU2_miSRg/zh-cn_image_0000002383015456.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=EABD4FD39EA01B6396DF8B681E3CAFDD48312D82F39A18BF98FC3DADC33FA692)
2. 在“Select the Cloud Function Type”栏选择“Cloud Object”，输入云对象名称（如“my-cloud-object”），点击“OK”。

   与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/tKnRMUhFSKGM-ZffZPJuWw/zh-cn_image_0000002179498304.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=07FC283AADE810C6E7B1907C63AEB351D4E3D3216025B6082AD86DA666342D25)

   “cloudfunctions”目录下生成新建的云对象目录，目录下主要包含如下文件：
   * 云对象配置文件“function-config.json”：包含handler、触发器等信息。
     + handler: 云对象的入口模块及云对象导出的类，通过“.”连接。
     + functionType：表示函数类型，“0”表示云函数，“1”表示云对象。
     + triggers：定义了云对象使用的触发器类型，当前云对象仅支持HTTP触发器。

     说明

     云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/cUpi4a8FQGSpAoT0GHUHsQ/zh-cn_image_0000002214858949.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=6BF75BC7890F49EE43DEF0FE15AE715AAB10F064860BCE80FB470A6CEFA9CBA5)
   * 云对象入口文件“*xxx*.ts”（如“myCloudObject.ts”）：在此文件中编写云对象代码。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/H_xXMHhDRoKfVl2rMbfcqg/zh-cn_image_0000002214704565.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=D2CA6AC61711FB4750AD02864C6C27DA6911270771D1749D82F35D4CFC4EDA0C)
   * 云对象依赖配置文件“package.json”：在此文件中添加依赖。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/JleBntpkRqW2onqNTxON1A/zh-cn_image_0000002179338620.png?HW-CC-KV=V1&HW-CC-Date=20260427T235502Z&HW-CC-Expire=86400&HW-CC-Sign=A3CAB9458751729F458D056702FD1EA3FC160BD8549517ECA67ED7BED551640E)
