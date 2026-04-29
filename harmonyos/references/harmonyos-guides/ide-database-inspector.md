---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-database-inspector
title: 数据库调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 数据库调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:65bbab68affd71903a58579f37cc771f4da98e7c0876bf9d03eff9b05d0e7886
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/9Opn4XeAThmeN61KkZFCNw/zh-cn_image_0000002561752909.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=51B3BE03F3CEB1C749FA0C8983E4332C0FF2845F04AD1C314649C8129A922A59)

   Database Inspector打开后，页面各区域作用如下：①选择设备，②选择应用包名，③数据库和表信息展示，④SQL执行和数据查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/1XMrE2LJTeeTpD4-2MOoVw/zh-cn_image_0000002561832887.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=694A950244916D84E65F0555B9E886091C17DA7F81F44A169DA4CDEC8C2CED73)
2. 从设备下拉列表中选择设备（设备需已连接）。
3. 选择包名，点击右侧的**Connect to Databases**按钮，即可查看数据库相关信息。（如果使用DevEco Studio 6.0.2 Beta1版本，按钮名称是**Execute**）。

   说明

   设备系统版本低于API 22时，Database Inspector会将数据库下载到本地计算机，界面上显示的是本地计算机路径，设备系统为API 22及以上版本时，界面上显示的是设备上的数据库路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/H1LmMCKpT6CiMFSi-_dRIA/zh-cn_image_0000002530752962.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=2EF1DF7E29B3F772711742178C64E8267FB76E27D65E7FB857ABC9BFD605540C)
4. 双击数据库表名，右侧区域展示表数据，默认按照20条/页展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Lr3ybQxZTMCq6Pd8KySQMw/zh-cn_image_0000002561752907.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=CF59DA66B0DDAA3BC57872C73413E1934047E514A9B26D1467DACD5FDCB20ECE)
5. 左侧区域点击**New Query**后，右侧会出现**SQL Editor**页签，根据需要选择数据库，并输入SQL后，点击**Execute**按钮即可查看或修改数据。

   修改数据后，点击SQL输入框下方的**Refresh Table**刷新页面上的数据。

   说明

   * 通过SQL修改数据或应用更新数据后，数据展示页面不支持自动刷新，需要重新执行查询语句或者点击刷新按钮。
   * 数据展示页面不支持可视化修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/UIaHkNP8T7q5k9YkSXR2nQ/zh-cn_image_0000002530912962.png?HW-CC-KV=V1&HW-CC-Date=20260429T054649Z&HW-CC-Expire=86400&HW-CC-Sign=4F405DAE680967BE987975ED15ED2E734AA0334C1F93F6D48782725E69521BE1)
