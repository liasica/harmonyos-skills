---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-dataentry
title: 添加数据条目
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 添加数据条目
category: harmonyos-guides
scraped_at: 2026-04-29T13:45:02+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:93bc55f202cbb0c9581fc169e1d3ff1fa14f275f0ae62971571d1a8e75f3d117
---

创建完对象类型后，您可在对象类型内添加数据条目（DataEntry），并配置数据所在的存储区。

支持手动创建和自动生成数据条目文件。

## 手动创建数据条目文件

1. 右击“clouddb/dataentry”目录，选择“New > Cloud DB Data Entry”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/cT-xc8TqRYGmKDCXRfm9AQ/zh-cn_image_0000002416495669.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=2A597706B3DA127DCC398DA314A6A916EFA6EF3A982DF185ACAE95E39D750C07)

2. 在“Associated Cloud DB Object Type”栏选择需添加数据条目的对象类型，在“Enter Cloud DB Data Entry Name”栏定义数据条目文件名，完成后点击“OK”。

   例如，选择刚刚创建的对象类型“objecttype1”，数据条目文件取默认名“d\_objecttype1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/HX0V8-NPTOOqDpFocU1oBQ/zh-cn_image_0000002214858965.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=83A9D70FE42CB2A84C416CD33413DC06B5A0D23DFFABA7C1FCAF5D637D49E043)

   如下图，“clouddb/dataentry”目录下生成并打开新建的数据条目JSON文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/WsYH8qHBSyuF8hDEpijN8g/zh-cn_image_0000002214858961.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=B033A2E0F05D4DBF6ED60B0F30F8773A7555FEF44C3F401337EBB7EAB1E69DC4)
3. 配置存储区和字段的值（即数据）。
   * “cloudDBZoneName”：配置存储区名称。上图示例中的“default”表示添加数据条目至default存储区。支持修改，如下图“cloudDBZoneName1”。另外，在使用API访问云数据库编码时需要引用该字段。
   * “objects”：配置当前对象类型中所有字段的值，即写入数据。一个对象（object）即为一条数据，您可以通过新建一个对象（object）来为字段赋新值，也可以修改某个对象（object）下字段的值（主键或加密字段的值不支持修改）。如下图，写入了两条数据。

     | 字段 | 数据条目1 | 数据条目2 |
     | --- | --- | --- |
     | author | Nancy | Peter |
     | shadowFlag | true | false |
     | bookName | My Favorite Book | Your First English Book |
     | id | 10 | 20 |
     | price | 10.5 | 20.5 |
     | publishTime | 19961007 | 19961007 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/5yRNBTbDR5iE8sxdwPBI-A/zh-cn_image_0000002179338640.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=37500270303F4C0F31C4C1A9069F451EE26C84DA9B66F9FC9FE48B6DB7FC7B45)

## 自动生成数据条目文件

1. 右击对象类型JSON文件，选择“Generate Data Entry”。

   依旧以对象类型“objecttype1”为例，其包含了“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”六个字段。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/khN1_Qb8RrqwwOrP3_-cpQ/zh-cn_image_0000002485251140.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=36F5482215EDFDED5DD3D898ACC6825B7F99E183B2E003A645A056296849847D)

2. 在弹出的“New Cloud DB Data Entry”框内，为即将生成的数据条目文件定义名称。此处取默认值“d\_objecttype1”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/hs_8oopDR7-DwFHECQlUTA/zh-cn_image_0000002179498336.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=CD6E91A689F13A1F01DC1BA8C50FA116A7C431C1A942C506A587465DADEDABCF)

   如下图，“clouddb/dataentry”目录下自动为对象类型“objecttype1”生成数据条目文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/IOYetmrbQkmVZ-PRvGFVWw/zh-cn_image_0000002179338636.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=DB9A23C672A4E063E471787CD580704ACC0A5BF8FE96408A8ED12368CD38E897)
3. 配置存储区和字段的值（即数据）。
   * “cloudDBZoneName”：配置存储区名称。上图示例中的“default”表示添加数据条目至default存储区。支持修改，如下图“cloudDBZoneName1”。另外，在使用API访问云数据库编码时需要引用该字段。
   * “objects”：配置当前对象类型中所有字段的值，即写入数据。一个对象（object）即为一条数据，您可以通过新建一个对象（object）来为字段赋新值，也可以修改某个对象（object）下字段的值（主键或加密字段的值不支持修改）。如下图，写入了两条数据。

     | 字段 | 数据条目1 | 数据条目2 |
     | --- | --- | --- |
     | author | Nancy | Peter |
     | shadowFlag | true | false |
     | bookName | My Favorite Book | Your First English Book |
     | id | 10 | 20 |
     | price | 10.5 | 20.5 |
     | publishTime | 19961007 | 19961007 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/mMhVk7TSRbuD7yJqu51bHg/zh-cn_image_0000002179338640.png?HW-CC-KV=V1&HW-CC-Date=20260429T054501Z&HW-CC-Expire=86400&HW-CC-Sign=010D593BB1C6EE0579A31A8A95E2919F8D0F3DB1F1013088A6EEEF953D1A5BD2)
