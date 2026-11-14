---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-database-inspector
title: 数据库调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 数据库调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:00+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:870f46e3f9cf0dc6394a56b9008b8f506d18ef94986f791ae67b6baf11ab77cf
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
  + SQL执行不支持历史记录。
  + SQL执行不支持事务。
* 从26.0.0版本开始，支持SQLite数据库语法高亮和关键词、表字段的自动联想补全。
* 从26.0.0版本开始，SQL编辑窗口支持执行多条SQL（以分号分隔），或者选中单条或者多条SQL后点击右键执行。

## 操作步骤

1. 点击菜单栏**View > Tool Windows > Database Inspector**，打开Database Inspector。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/v8RvFU1IRUWqPacG8Xej-Q/zh-cn_image_0000002808886583.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C222D3A9F7D9104362774B011692DFAFEB8FF74F9CB679D61562CC417D2C5CA)

   Database Inspector打开后，页面各区域作用如下：①选择设备，②选择应用包名，③数据库和表信息展示，④SQL执行和数据查看。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/KPfFK_JuTHmJj_KAl8Kb6w/zh-cn_image_0000002808766499.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=A152A18DA6D19EF665D43169A42A54A9C461FD8877FBE0A1A02B701CBE8E1F7A)
2. 从设备下拉列表中选择设备（设备需已连接）。
3. 选择包名，点击右侧的**Connect to Databases**按钮，即可查看数据库相关信息。

   **说明** 

   设备系统版本低于API 22时，Database Inspector会将数据库下载到本地计算机，界面上显示的是本地计算机路径，设备系统为API 22及以上版本时，界面上显示的是设备上的数据库路径。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/pKy3Ek4jQ9u2vK-5MeJAoA/zh-cn_image_0000002779406938.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=F196F1A2B9180549E7319140D74C0F28294A901FCDED16B264F10EB5AA553D89)
4. 双击数据库表名，右侧区域展示表数据，默认按照20条/页展示。

   从26.0.0版本开始，支持可视化修改表中的数据（仅支持常规基础数据类型：字符串、数值、布尔等，不支持二进制数据类型）。双击单元格，输入数据后，按Enter键或点击其他区域提交。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/UnkcRzyQRce0aMH3q8h1JQ/zh-cn_image_0000002808766501.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=C49D6CF948D38AACEC7E76111E30046E9812D9C248C22781A96EBE46AF3A4240)
5. 左侧区域点击**New Query**后，右侧会出现**SQL Editor**页签，根据需要选择数据库，并输入SQL后，点击**Execute**按钮即可查看或修改数据。

   修改数据后，点击SQL输入框下方的**Refresh Table**刷新页面上的数据。

   **说明** 

   * 通过SQL修改数据或应用更新数据后，数据展示页面不支持自动刷新，需要重新执行查询语句或者点击刷新按钮。
   * 数据展示页面不支持可视化修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ORtsT7ehQtG_SKenYl0lIg/zh-cn_image_0000002779566916.png?HW-CC-KV=V1&HW-CC-Date=20261114T004713Z&HW-CC-Expire=31536000000&HW-CC-Sign=8871581AEC21FF4E1FF6B106DB34EE7A2A5AF8958DDC10A8F504B3CB8909FD58)
