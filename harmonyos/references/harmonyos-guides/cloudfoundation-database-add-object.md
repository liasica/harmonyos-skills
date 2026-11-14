---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-object
title: 新增对象类型
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 新增对象类型
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20ac9112301e89119762f7bf2aa969866c1744ee00f3f9d2318c6f6c26d08fc7
---

开发者需要基于AGC控制台创建对象类型。

## 前提条件

已[开通云数据库服务](cloudfoundation-enable-database.md)。

## 操作步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击需要创建对象类型的项目。
3. 在左侧导航栏选择“云开发（Serverless）> 云数据库”，进入云数据库页面。
4. 点击“新增”，创建新的对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/rfpeX18MR46TrTIZNEX0Tw/zh-cn_image_0000002817427349.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1C607DB6CF4863026EBD7110A0620FCF454731E25A88723691499E6162B5558)
5. 输入“对象类型名”为“BookInfo”后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/kHCehjvMQA2SM4oL5jakxg/zh-cn_image_0000002788467930.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB93C49EA3884CDCED7C92233D14D56AE3E8E18CB9B6D772CB20187D6ED6154F)
6. 点击“+新增字段”，新增如下表字段后，点击“下一步”。

   | 字段名称 | 类型 | 主键 | 非空 | 加密 | 默认值 |
   | --- | --- | --- | --- | --- | --- |
   | id | Integer | ✓ | ✓ | – | – |
   | bookName | String | – | ✓ | – | – |
   | author | String | – | – | – | – |
   | price | Double | – | – | – | – |
   | borrowerId | Integer | – | – | – | – |
   | borrowerName | String | – | – | – | – |
   | borrowerTime | Date | – | – | – | – |
7. 点击“+”新增索引，设置“索引名”为“bookName”，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/a_cVpVh4Raqz1-b7Lq1v-Q/zh-cn_image_0000002817507419.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6FAA003E776203AFFC940DDB53EA5BBBA730E69FF01AB34EA0B132EBDC67664)
8. 按照如下要求设置各角色权限后，点击“确定”。

   | 角色 | query | upsert | delete | 说明 |
   | --- | --- | --- | --- | --- |
   | 所有人 | ✓ | ✓ | ✓ | 代表所有用户，包含认证和非认证用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  但是，不建议将upsert和delete权限配置给所有人角色。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**所有人**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 认证用户 | ✓ | ✓ | ✓ | 经过AGC登录认证的用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**认证用户**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 数据创建者 | ✓ | ✓ | ✓ | 经过认证的数据创建用户。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  每条数据都有其对应的数据创建人（即应用用户），每个数据创建者仅可以upsert或者delete自己创建的数据，不能upsert或者delete他人创建的数据。  数据创建者的信息保存在数据记录的系统表中。 |
   | 管理员 | ✓ | ✓ | ✓ | 应用开发者，主要是指通过AGC控制台或FaaS（Function as a Service，函数即服务）侧访问云数据库的角色。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  管理员可以管理并配置其他角色的权限。 |
9. 创建完成后返回对象类型列表，可以查看已创建的对象类型。
10. 勾选创建的BookInfo对象类型，点击“导出”。若不勾选对象类型，默认导出所有对象类型。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/YkesvYm8SDS2Si6pjhNbEg/zh-cn_image_0000002788307988.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=69004D83D7A5CA988C59B1DFBF5E0E0B153040FE3DD5DB559B5D0EB0B1DB59D5)
11. 导出“json格式”文件，点击“确定”。后续[引入对象类型文件](cloudfoundation-database-add-file.md)时，需要使用此文件。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/GWcJ5FTzQf-IpBQNLa7SzA/zh-cn_image_0000002817427351.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=6127805776E10EC93BC6A0F547B78F1A828594998EBF07EC16330735653E12DC)
