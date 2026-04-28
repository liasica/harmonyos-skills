---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-dataentry
title: 添加数据条目
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 添加数据条目
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:06+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:b40c68e3935ed2bdb693cc78084bd4c8dd3d33a8674207a39112ba90c9edd587
---

创建完对象类型后，您可在对象类型内添加数据条目（DataEntry），并配置数据所在的存储区。

支持手动创建和自动生成数据条目文件。

## 手动创建数据条目文件

1. 右击“clouddb/dataentry”目录，选择“New > Cloud DB Data Entry”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/KNJBwZeBTAC7BxcGkDV4Jg/zh-cn_image_0000002416495669.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=A51E73B319F89EA494E7A80F154E670F5CFF654E3029D616E0D71CCD154F2B04)

2. 在“Associated Cloud DB Object Type”栏选择需添加数据条目的对象类型，在“Enter Cloud DB Data Entry Name”栏定义数据条目文件名，完成后点击“OK”。

   例如，选择刚刚创建的对象类型“objecttype1”，数据条目文件取默认名“d\_objecttype1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/0yGTWxdqQsCEM8c5tB005Q/zh-cn_image_0000002214858965.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=FCA63B3B2C679A67D918A1C9C20A2A04E9F4A84E504D17C9999A2D3A939B9176)

   如下图，“clouddb/dataentry”目录下生成并打开新建的数据条目JSON文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/zYN1WLaVR5OX_A2pqa4YqQ/zh-cn_image_0000002214858961.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=1B1C86F4DE7986BF2AA5939442B4C16D709BDF29B1D0D12CC263E5E2AA9AA81B)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/KiDjyywUTv-ZYmjoppR5rg/zh-cn_image_0000002179338640.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=B0A5843024D94AB8B52404870491611B098F1E47DA76BFBAE65435709BD22DCE)

## 自动生成数据条目文件

1. 右击对象类型JSON文件，选择“Generate Data Entry”。

   依旧以对象类型“objecttype1”为例，其包含了“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”六个字段。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/z9U7WPYhQ4iniJJMNwxNZw/zh-cn_image_0000002485251140.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=59296509C85EFEC7EBEAD67BCD24228060174BA65F4B54F49495FCD2BA5EAAD9)

2. 在弹出的“New Cloud DB Data Entry”框内，为即将生成的数据条目文件定义名称。此处取默认值“d\_objecttype1”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ourYmV73TR2Hd_BOoE8Pjw/zh-cn_image_0000002179498336.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=5F13A35221A6C1560619E09A6B5206A5D33937AD509D7ECDC56B4ADB525A0F2D)

   如下图，“clouddb/dataentry”目录下自动为对象类型“objecttype1”生成数据条目文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/krAnytpsQ2mhWv5pdqgckQ/zh-cn_image_0000002179338636.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=173CB55E490EE69A0CCA11A1A010D73343E1DB978FB030D3A2F8BB34FAF17B6C)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/4mRbv-GETF-be6B5O1zVuw/zh-cn_image_0000002179338640.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=0D9C229ECF4D9B7879585B26F3BE9B514CA88971D834453E1C510A52CF1B9910)
