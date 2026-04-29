---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-database-add-object
title: 新增对象类型
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云数据库 > 新增对象类型
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f88cd5d0d2676315f28fff0be90d1135af3d96625ec1effba718bb25c7aecdf
---

开发者需要基于AGC控制台创建对象类型。

## 前提条件

已[开通云数据库服务](cloudfoundation-enable-database.md)。

## 操作步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，点击“开发与服务”。
2. 在项目列表中点击需要创建对象类型的项目。
3. 在左侧导航栏选择“云开发（Serverless）> 云数据库”，进入云数据库页面。
4. 点击“新增”，创建新的对象类型。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/uQ_B7wp2ROyFyUJZVPeeQA/zh-cn_image_0000002589325231.png?HW-CC-KV=V1&HW-CC-Date=20260429T053744Z&HW-CC-Expire=86400&HW-CC-Sign=5F778EC96560A54E8C10125A68AF52AF5982F6AE79C182E00E841ED2EAB9B09B)
5. 输入“对象类型名”为“BookInfo”后，点击“下一步”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/fHXkaeMsQuCj_jrOLX7XMg/zh-cn_image_0000002589245167.png?HW-CC-KV=V1&HW-CC-Date=20260429T053744Z&HW-CC-Expire=86400&HW-CC-Sign=60FDD1A58070BE893296F4DEAA8007C151250E4B2081BBDBC8311C1A2E5A530C)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/hILWzs2XSoW-Fzwp02QSVg/zh-cn_image_0000002558765362.png?HW-CC-KV=V1&HW-CC-Date=20260429T053744Z&HW-CC-Expire=86400&HW-CC-Sign=D2310AA04F4CC2BEF62704C186B5B3E83B29539A4A53B79975704472DE50589A)
8. 按照如下要求设置各角色权限后，点击“确定”。

   | 角色 | query | upsert | delete | 说明 |
   | --- | --- | --- | --- | --- |
   | 所有人 | ✓ | ✓ | ✓ | 代表所有用户，包含认证和非认证用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  但是，不建议将upsert和delete权限配置给所有人角色。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**所有人**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 认证用户 | ✓ | ✓ | ✓ | 经过AGC登录认证的用户。  该角色默认拥有query权限，可自定义配置upsert和delete权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  当对象类型中设置了加密字段之后，表示开启全程加密功能，此时**认证用户**角色将不会拥有query、upsert和delete权限，且不允许修改。 |
   | 数据创建者 | ✓ | ✓ | ✓ | 经过认证的数据创建用户。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  每条数据都有其对应的数据创建人（即应用用户），每个数据创建者仅可以upsert或者delete自己创建的数据，不能upsert或者delete他人创建的数据。  数据创建者的信息保存在数据记录的系统表中。 |
   | 管理员 | ✓ | ✓ | ✓ | 应用开发者，主要是指通过AGC控制台或FaaS（Function as a Service，函数即服务）侧访问云数据库的角色。  该角色默认拥有所有权限，且可自定义配置所有权限。如：角色勾选了upsert权限，该角色可在本对象类型中写入数据。  管理员可以管理并配置其他角色的权限。 |
9. 创建完成后返回对象类型列表，可以查看已创建的对象类型。
10. 勾选创建的BookInfo对象类型，点击“导出”。若不勾选对象类型，默认导出所有对象类型。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/QGQ3F1bLQD-gTbsOet0QiA/zh-cn_image_0000002558605706.png?HW-CC-KV=V1&HW-CC-Date=20260429T053744Z&HW-CC-Expire=86400&HW-CC-Sign=6805E910450179927CC9DDF21539F8BA8853DB0025F2E28CF988C3AD2BB59FBF)
11. 导出“json格式”文件，点击“确定”。后续[引入对象类型文件](cloudfoundation-database-add-file.md)时，需要使用此文件。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/P2glwxgYRmCJHTbBVujy4A/zh-cn_image_0000002589325233.png?HW-CC-KV=V1&HW-CC-Date=20260429T053744Z&HW-CC-Expire=86400&HW-CC-Sign=4D59235517A8AB68FFD0F536056D1F8DAB1C0ADA0FD5C8A2985724F73986FEEB)
