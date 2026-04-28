---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-database-inspector
title: 数据库调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 数据库调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:98c82160349dedc33aa6dc60d947618ea3223579027b089c820c0ee938615003
---

从DevEco Studio 6.0.2 Beta1版本开始，新增Database Inspector，支持在DevEco Studio上执行SQL语句查看、修改应用数据库，无需将应用数据库先导出到本地，提升开发调试效率，当前支持SQLite和向量数据库。

开发者也可以通过命令行工具调试数据库，具体操作方式请参考[vector-store数据库调试工具指导](vector-store-debug-tool.md)、[SQLite调试工具指导](sqlite-database-debug-tool.md)。

## 使用场景

* 应用某个操作会修改数据库内容，可以实时查看修改后的内容是否符合预期。
* 可以实时修改数据库内数据，构造测试场景，提升测试效率。

## 使用约束

* 设备系统需要不低于API 22。低于API 22时，SQLite数据库仅支持查看，不支持修改，向量数据库无法使用。
* 不支持使用release签名的应用。
* 仅支持调试database目录下的数据库。
* 不支持调试加密数据库，建议使用非加密库。
* 不支持调试隐私用户、多用户数据库，建议使用默认用户。
* 不支持导入导出数据库。
* 执行SQL时，存在以下约束：
  + 不支持执行多条SQL。
  + 存在多条SQL时，不支持高亮选择后执行单条SQL。
  + SQL执行不支持历史记录。
  + SQL执行不支持事务。

## 操作步骤

1. 点击菜单栏**View > Tool Windows > Database Inspector**，打开Database Inspector。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/nOj-6sj_Tiye6wTAzX1dkg/zh-cn_image_0000002561752909.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=F8BCBE6CEE3845E9C9D957F85AC8E133BC0B359BDA1949373AA1B3FF837E7508)

   Database Inspector打开后，页面各区域作用如下：①选择设备，②选择应用包名，③数据库和表信息展示，④SQL执行和数据查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/um66Hb7yTTG8sBXrHvjD1w/zh-cn_image_0000002561832887.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=51CD2E2DCB31044C726D9A674A26BC910F966A7B28CBBDDBCFE1F7A599022BFF)
2. 从设备下拉列表中选择设备（设备需已连接）。
3. 选择包名，点击右侧的**Connect to Databases**按钮，即可查看数据库相关信息。（如果使用DevEco Studio 6.0.2 Beta1版本，按钮名称是**Execute**）。

   说明

   设备系统版本低于API 22时，Database Inspector会将数据库下载到本地计算机，界面上显示的是本地计算机路径，设备系统为API 22及以上版本时，界面上显示的是设备上的数据库路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/aQRWv3p_Sn2MYGdYF4TdbA/zh-cn_image_0000002530752962.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=151248DACCA488817C6C0A2FFBC53D2479A7F40A8554E4410A57BBA7577A5D03)
4. 双击数据库表名，右侧区域展示表数据，默认按照20条/页展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/yCnjnIYsQO6334XYx69MTg/zh-cn_image_0000002561752907.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=29ADEEF0F90EEA0D1E9F1F3F855581D1E6272ADEDB55D935B756FBB27BD0B9BC)
5. 左侧区域点击**New Query**后，右侧会出现**SQL Editor**页签，根据需要选择数据库，并输入SQL后，点击**Execute**按钮即可查看或修改数据。

   修改数据后，点击SQL输入框下方的**Refresh Table**刷新页面上的数据。

   说明

   * 通过SQL修改数据或应用更新数据后，数据展示页面不支持自动刷新，需要重新执行查询语句或者点击刷新按钮。
   * 数据展示页面不支持可视化修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/JZw95IiWS2CLOqUDaygEpg/zh-cn_image_0000002530912962.png?HW-CC-KV=V1&HW-CC-Date=20260427T235654Z&HW-CC-Expire=86400&HW-CC-Sign=1C31248F6E17BBD94D7E9B5058B87333CF22D9C1DE4CB449A1C4A519E5B16174)
