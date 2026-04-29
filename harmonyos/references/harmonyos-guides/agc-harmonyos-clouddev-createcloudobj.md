---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createcloudobj
title: 创建云对象
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 创建云对象
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:af7ef4ae54d24b2c4059535f90daf2950de05ca75874b83573e710763bab1cd6
---

首先您需要在云侧工程下创建云对象。

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ecwj2j7FQYu7KdB8oGHRjw/zh-cn_image_0000002383015456.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=0B9B59DF3ED7467AE7683222FA75BBE3E34D7AC0FFB474349D4041616028DBD6)
2. 在“Select the Cloud Function Type”栏选择“Cloud Object”，输入云对象名称（如“my-cloud-object”），点击“OK”。

   与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ymbovjrvQ5WKhC_fHZmxzA/zh-cn_image_0000002179498304.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=E6A982C594AE48E17A9D8306E790A9F4B96001569BA037F0533777CAD9303B56)

   “cloudfunctions”目录下生成新建的云对象目录，目录下主要包含如下文件：
   * 云对象配置文件“function-config.json”：包含handler、触发器等信息。
     + handler: 云对象的入口模块及云对象导出的类，通过“.”连接。
     + functionType：表示函数类型，“0”表示云函数，“1”表示云对象。
     + triggers：定义了云对象使用的触发器类型，当前云对象仅支持HTTP触发器。

     说明

     云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/mT7H8LuISRS6im9VCQPvpw/zh-cn_image_0000002214858949.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=C60E60403C12357B80DC5804484FBB1C2AFDC3291F0FBA20BC80C3B09743A763)
   * 云对象入口文件“*xxx*.ts”（如“myCloudObject.ts”）：在此文件中编写云对象代码。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/OzujUvGkQ-yhj-o19B0kGg/zh-cn_image_0000002214704565.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=62E990F162FC77A2E50E4F914D37443D21644F8AADB398ED94DA1F9D262AD952)
   * 云对象依赖配置文件“package.json”：在此文件中添加依赖。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/-tqsfynaTxmAIZYuC5UVlQ/zh-cn_image_0000002179338620.png?HW-CC-KV=V1&HW-CC-Date=20260429T054500Z&HW-CC-Expire=86400&HW-CC-Sign=4F93DDF074826A7A359204D6F8214C4C1C3FCAD6925FF1E13A8499207251D3E1)
