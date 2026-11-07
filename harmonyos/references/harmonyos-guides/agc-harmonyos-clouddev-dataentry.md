---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-dataentry
title: 添加数据条目
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 添加数据条目
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:8db87e34b1a885abc5aeb55b9241be19c12760cda25d0474d7d6796340ad6b66
---

创建完对象类型后，您可在对象类型内添加数据条目（DataEntry），并配置数据所在的存储区。

支持手动创建和自动生成数据条目文件。

## 手动创建数据条目文件

1. 右击“clouddb/dataentry”目录，选择“New > Cloud DB Data Entry”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/KjTQSKqRSq2ueCgs_FjbUw/zh-cn_image_0000002416495669.png)

2. 在“Associated Cloud DB Object Type”栏选择需添加数据条目的对象类型，在“Enter Cloud DB Data Entry Name”栏定义数据条目文件名，完成后点击“OK”。

   例如，选择刚刚创建的对象类型“objecttype1”，数据条目文件取默认名“d\_objecttype1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/5gEh2MqxSUqzyUW0ONgRBw/zh-cn_image_0000002214858965.png)

   如下图，“clouddb/dataentry”目录下生成并打开新建的数据条目JSON文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/oa4rOgqpTVGNA4-9p4iLQg/zh-cn_image_0000002214858961.png)
3. 配置存储区和字段的值（即数据）。
   * “cloudDBZoneName”：配置存储区名称。上图示例中的“default”表示添加数据条目至default存储区。支持修改，如下图“cloudDBZoneName1”。另外，在使用API访问云数据库编码时需要引用该字段。
   * “objects”：配置当前对象类型中所有字段的值，即写入数据。一个对象（object）即为一条数据，您可以通过新建一个对象（object）来为字段赋新值，也可以修改某个对象（object）下字段的值（主键或加密字段的值不支持修改）。如下图，写入了两条数据。

     **说明** 

     + 如果字段的数据类型为“String”，字段值最大长度为200个字符。
     + 如果字段的数据类型为“Text”，字段值最大长度为100000000个字符。

     | 字段 | 数据条目1 | 数据条目2 |
     | --- | --- | --- |
     | author | Nancy | Peter |
     | shadowFlag | true | false |
     | bookName | My Favorite Book | Your First English Book |
     | id | 10 | 20 |
     | price | 10.5 | 20.5 |
     | publishTime | 19961007 | 19961007 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Cd6w9PYtQ6q-Jm4QGJLv8A/zh-cn_image_0000002179338640.png)

## 自动生成数据条目文件

1. 右击对象类型JSON文件，选择“Generate Data Entry”。

   依旧以对象类型“objecttype1”为例，其包含了“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”六个字段。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Oz4e0PX_RemeycF4nZhcxA/zh-cn_image_0000002485251140.png)

2. 在弹出的“New Cloud DB Data Entry”框内，为即将生成的数据条目文件定义名称。此处取默认值“d\_objecttype1”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/qmmpPYywT1az8Gb-L_Dvlg/zh-cn_image_0000002179498336.png)

   如下图，“clouddb/dataentry”目录下自动为对象类型“objecttype1”生成数据条目文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/lhW_SrYLRl2UjaY5dKj1uw/zh-cn_image_0000002179338636.png)
3. 配置存储区和字段的值（即数据）。
   * “cloudDBZoneName”：配置存储区名称。上图示例中的“default”表示添加数据条目至default存储区。支持修改，如下图“cloudDBZoneName1”。另外，在使用API访问云数据库编码时需要引用该字段。
   * “objects”：配置当前对象类型中所有字段的值，即写入数据。一个对象（object）即为一条数据，您可以通过新建一个对象（object）来为字段赋新值，也可以修改某个对象（object）下字段的值（主键或加密字段的值不支持修改）。如下图，写入了两条数据。

     **说明** 

     + 如果字段的数据类型为“String”，字段值最大长度为200个字符。
     + 如果字段的数据类型为“Text”，字段值最大长度为100000000个字符。

     | 字段 | 数据条目1 | 数据条目2 |
     | --- | --- | --- |
     | author | Nancy | Peter |
     | shadowFlag | true | false |
     | bookName | My Favorite Book | Your First English Book |
     | id | 10 | 20 |
     | price | 10.5 | 20.5 |
     | publishTime | 19961007 | 19961007 |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/5ssTMRqDRf67ehnoTUayzg/zh-cn_image_0000002179338640.png)
