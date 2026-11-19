---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-object
title: 新增对象类型
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 新增对象类型
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b7323cf2275cfd07d1eba2ae9f3d15f17fbd22ed9ffa59408be9759f11d51b30
---

开发者需要基于AGC控制台创建对象类型。

## 前提条件

已[开通云数据库服务](cloudfoundation-enable-database.md)。

## 操作步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击需要创建对象类型的项目。
3. 在左侧导航栏选择“云开发（Serverless）> 云数据库”，进入云数据库页面。
4. 点击“新增”，创建新的对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/8eUmjvzYQvC0o4e8mukHcQ/zh-cn_image_0000002791726288.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA1B8229036AC63728C0A143A37F5D8ED9B02E9BA04DF051D3C53BDEDCF7A705)
5. 输入“对象类型名”为“BookInfo”后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/9VR5DYr1RUyMldiGb_R5Eg/zh-cn_image_0000002791566316.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD1BC664302A2FF17F4DC0A62BF065FD7B3BCFDE0BEC6A3F9767DE1842ACF454)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/reGqt7H5TQyYi7L-v5ovKg/zh-cn_image_0000002820526269.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E93C812107829023F25817148002F6B13535937E4681F9C1E601000445B52BC)
8. 按照如下要求设置各角色权限后，点击“确定”。

   | 角色 | query | upsert | delete | 说明 |
   | --- | --- | --- | --- | --- |
   | 所有人 | ✓ | ✓ | ✓ | 代表所有用户，包含认证和非认证用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  但是，不建议将upsert和delete权限配置给所有人角色。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**所有人**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 认证用户 | ✓ | ✓ | ✓ | 经过AGC登录认证的用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**认证用户**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 数据创建者 | ✓ | ✓ | ✓ | 经过认证的数据创建用户。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  每条数据都有其对应的数据创建人（即应用用户），每个数据创建者仅可以upsert或者delete自己创建的数据，不能upsert或者delete他人创建的数据。  数据创建者的信息保存在数据记录的系统表中。 |
   | 管理员 | ✓ | ✓ | ✓ | 应用开发者，主要是指通过AGC控制台或FaaS（Function as a Service，函数即服务）侧访问云数据库的角色。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  管理员可以管理并配置其他角色的权限。 |
9. 创建完成后返回对象类型列表，可以查看已创建的对象类型。
10. 勾选创建的BookInfo对象类型，点击“导出”。若不勾选对象类型，默认导出所有对象类型。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/Y8nsXlxURNSpZb4wREdE9w/zh-cn_image_0000002820406269.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD449B25E00F6E26D9F8D20DA7EAA5F3EF19F0359E534F90A3F13CC451707BFE)
11. 导出“json格式”文件，点击“确定”。后续[引入对象类型文件](cloudfoundation-database-add-file.md)时，需要使用此文件。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/rh_dvQ8wTm-6G5df5iWIVg/zh-cn_image_0000002791726290.png?HW-CC-KV=V1&HW-CC-Date=20261119T014855Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD6C07FFE7927B60AD93510E922DF1C74FD89DF5AB2E4A0B77D378ADB2010351)
