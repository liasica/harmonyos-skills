---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createcloudobj
title: 创建云对象
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 创建云对象
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:2e9651eaba3b3befebdd130e15bc6a1440ba3a82438f0c551239fa66089f43dd
---

首先您需要在云侧工程下创建云对象。

1. 右击“cloudfunctions”目录，选择“New > Cloud Function”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/X1J1ePZfSO6a5ewFidGjHA/zh-cn_image_0000002383015456.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=06C38006700EEC8C252198D4495DAD4DE0E9DFC01C34629FAAAE28C052F81CCF)
2. 在“Select the Cloud Function Type”栏选择“Cloud Object”，输入云对象名称（如“my-cloud-object”），点击“OK”。

   与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/CR4e34EFThWl8i1zeItdqQ/zh-cn_image_0000002179498304.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=4DA27DA9AEBA70B90E1DBAD75082057C2632BA9B7FB2E7EAD080965CA15BC71E)

   “cloudfunctions”目录下生成新建的云对象目录，目录下主要包含如下文件：
   * 云对象配置文件“function-config.json”：包含handler、触发器等信息。
     + handler: 云对象的入口模块及云对象导出的类，通过“.”连接。
     + functionType：表示函数类型，“0”表示云函数，“1”表示云对象。
     + triggers：定义了云对象使用的触发器类型，当前云对象仅支持HTTP触发器。

     **说明** 

     云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/96AgOWiQRKqrrk1eXp4nqA/zh-cn_image_0000002214858949.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=2AD7E6D26FDE0BF746E8C7DF38E260A0BC7ACCB36FC6A6FFA138997338194280)
   * 云对象入口文件“*xxx*.ts”（如“myCloudObject.ts”）：在此文件中编写云对象代码。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/27piCQcNTKmJQe4LLujPnQ/zh-cn_image_0000002214704565.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=B686533E050DF8AC0C5B92318EBC1B40986210E1813FA6B3C05E89C08232E426)
   * 云对象依赖配置文件“package.json”：在此文件中添加依赖。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xA3sN0glS9aECIO2ve35iA/zh-cn_image_0000002179338620.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BDF47527084EB064C91165D26AD6EBAD7577941B3B3F9C25F5BB122A31424F9)
