---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-dataentry
title: 添加数据条目
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云数据库 > 添加数据条目
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:49+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:8213eab6b3bc1829bfbf8b302077135c736c35eacc20e301447fc1deceb2d65f
---

创建完对象类型后，您可在对象类型内添加数据条目（DataEntry），并配置数据所在的存储区。

支持手动创建和自动生成数据条目文件。

## 手动创建数据条目文件

1. 右击“clouddb/dataentry”目录，选择“New > Cloud DB Data Entry”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/V3jM6mTaSqqCb-sKu0DZPQ/zh-cn_image_0000002416495669.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AA6096DE101F8FFDD290E21C3916D32788E200BEA2845555D9C9E5F8E4AADF7)

2. 在“Associated Cloud DB Object Type”栏选择需添加数据条目的对象类型，在“Enter Cloud DB Data Entry Name”栏定义数据条目文件名，完成后点击“OK”。

   例如，选择刚刚创建的对象类型“objecttype1”，数据条目文件取默认名“d\_objecttype1”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/LumZjS7GRB6aDzy6G20wrw/zh-cn_image_0000002214858965.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=764BCFE43207B9BF9126D0CFB1EE5FC3C152B316A42F9C187269E573AFE5639F)

   如下图，“clouddb/dataentry”目录下生成并打开新建的数据条目JSON文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/-JnDFHF-Ra2mgXiKlblvkg/zh-cn_image_0000002214858961.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=E79C5E10DFDEFC2D403BC952CDA81DBB17FEB4C0E82382371EAE27828B2AB5BA)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/G5QNbBgQRwCtVRdMPOo7Pw/zh-cn_image_0000002179338640.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE7386B9FA3E47F965BF9AB780B472C1CEF7E74C184CDD99C8F9AE7F94F38DFC)

## 自动生成数据条目文件

1. 右击对象类型JSON文件，选择“Generate Data Entry”。

   依旧以对象类型“objecttype1”为例，其包含了“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”六个字段。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/nPI46O0rQbiRNihvsuUhaw/zh-cn_image_0000002485251140.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=9FDEF480B0C71FB0937316DCE70BE3019FFFDF6CFBD03D8CC5628F4173AEABC4)

2. 在弹出的“New Cloud DB Data Entry”框内，为即将生成的数据条目文件定义名称。此处取默认值“d\_objecttype1”为例。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/CpUpMBxyT7u8IH3FhSi_Lg/zh-cn_image_0000002179498336.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2A99B9956966AA55F8B6CB48B5F6AEA4D78A4CA3F4BD297EC8FF9B82206991A)

   如下图，“clouddb/dataentry”目录下自动为对象类型“objecttype1”生成数据条目文件“d\_objecttype1”，该文件中已为您预置好所属对象类型名称（“objecttype1”）与对象类型的字段名（“id”、“bookName”、“author”、“price”、“publishTime”、“shadowFlag”）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/OlN_Smv9QvOJygKRoANU8A/zh-cn_image_0000002179338636.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3F08126E4CBEB42ABC242B8D343C7FEB085C22A85C6F863AA723ABF068ED23E)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/jPhUzJctTwuWFU2kQNYqvA/zh-cn_image_0000002179338640.png?HW-CC-KV=V1&HW-CC-Date=20261114T004703Z&HW-CC-Expire=31536000000&HW-CC-Sign=1931534DB4E5ACBE62B3978820332DA63EF34E7D4661EA93473D2494306560D0)
