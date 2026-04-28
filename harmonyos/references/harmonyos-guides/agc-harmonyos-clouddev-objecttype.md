---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-objecttype
title: 创建对象类型
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:06+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:98157e87c0945c7ca879ee26284650569925895257015fd750488b24ac635e0e
---

对象类型（ObjectType）用于定义存储对象的集合，不同的对象类型对应的不同数据结构。每创建一个对象类型，云数据库会在每个存储区实例化一个与之结构相对应的对象类型，用于存储对应的数据。

创建对象类型的操作如下：

1. 右击“clouddb/objecttype”目录，选择“New > Cloud DB Object Type”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/WTA449nvTSypXWM2nfavHQ/zh-cn_image_0000002416494957.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=9346BECDB88DCCE63DF6A505E363B90148FDF8CC19BADF4785AC604F897B6290)

2. 输入对象类型名称（下文以“objecttype1”为例）后，点击“OK”。

   说明

   对象类型名称必须符合如下规范：

   * 只能包含字母（A-Z或a-z）、数字（0-9）和下划线（\_），并且至少包含字母类型。
   * 必须以字母开头，以字母或者数字结尾，不允许以“sqlite\_”开头，不允许以下划线（\_）结尾。
   * 不允许使用如下系统保留名称： naturalbase\_metadata、objecttypeinfohelper、t\_data\_upgrade\_info、t\_index\_schema、t\_nstore\_config、t\_schema\_negotiate\_info、t\_metadata\_schema、t\_nstore\_permission、t\_system\_config。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/lBqXMlEqRt-Lk8hhu-E-VQ/zh-cn_image_0000002179498152.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=DFED4B5447164240D706748B51C6D7A7EA25205BEFFDC1283EA38AE47D65BB64)

   “clouddb/objecttype”目录下生成并打开新建的对象类型JSON文件“objecttype1.json”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/ca3CFGhwRnuGM5PFTf6q6Q/zh-cn_image_0000002179338468.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=E0438B1020BD90FCAC55941A667A72E87D69F7E830EFE6D87BF4C9AD708316CD)
3. 在“fields”中为该对象类型配置字段信息。

   | 参数 | 必选(M)/可选(O) | 说明 |
   | --- | --- | --- |
   | fieldName | M | 字段名称。  输入要求具体如下：  * 字段的名称长度必须大于或等于1个字符，小于或等于30个字符，只能包含以下3种类型，并且至少包含“字母”类型：   + 字母（A-Z或a-z）   + 数字（0-9）   + 特殊字符：\_ * 字段名称必须以字母开头，以字母或者数字结尾。 * 字段名称中不区分字母的大小写。 * 修改对象类型时，支持删除字段。 * 字段名称不允许使用系统保留字段名称： naturalbase\_version、naturalbase\_deleted、naturalbase\_operationtype、naturalbase\_creator、naturalbase\_accesstime、naturalbase\_operationtime、naturalbase\_syncstatus、naturalbase\_changedfieldsbitmap、naturalbase\_lastmodifier、cmin、cmax、xmin、xmax、ctid、oid、tableoid、xc\_node\_id、tablebucketid、rowid。 说明  当前Cloud Foundation Kit暂不支持自增类型字段IntAutoIncrement或LongAutoIncrement。 |
   | fieldType | M | 字段的数据类型。  当前支持的数据类型：String、Boolean、Byte、Short、Integer、Long、Float、Double、ByteArray、Text、Date。 |
   | belongPrimaryKey | O | 设置该字段是否为对象类型的主键，默认值为false。  * 至少设置一个字段为主键。 * 支持设置复合主键，由多个字段组合成为主键，一个复合主键包含的字段小于等于5个，复合主键字段顺序与字段的顺序一致。 * 数据类型为ByteArray、Text、Date、Double、Float和Boolean的字段不支持设置为主键。 * 主键的值不允许更改。 |
   | notNull | O | 设置字段值是否为非空，默认值为false。  * 数据类型为ByteArray和Date的字段不支持设置为非空。 * 主键默认非空，且不允许更改。 * 设置为非空的字段不支持加密和敏感。 |
   | isNeedEncrypt | O | 设置字段是否需要加密，开启全程加密数据管理功能，默认值为false。  选择加密后，该字段对应的数据会加密存储在存储区中。  * 主键字段不支持加密。 * 加密的字段不支持设置为非空。 * 加密的字段不支持设置为敏感字段。 * 一个对象类型中包含的加密字段和敏感字段的总数需小于或等于5个。 * 字段设置为加密后，不支持导出该字段的数据值。 * 数据类型为ByteArray、Text的字段不支持加密。 * 对象类型创建成功后，不支持修改加密属性。 |
   | isSensitive | O | 设置字段是否为敏感字段，默认值为false。  选择敏感后，该字段对应的数据会加密存储在存储区中。  * 敏感字段不支持设置为主键。 * 敏感字段不支持设置为非空。 * 敏感字段不支持设置为加密。 * 敏感字段不支持设置为默认值。 * 对象类型创建成功后，不支持修改敏感属性。 * 仅支持数据类型为Byte、Short、Integer、Long、Float、Double、String和Date的字段设置为敏感字段。 * 敏感字段不支持设置为索引。 * 一个对象类型中包含的加密字段和敏感字段的总数需小于或等于5个。 |
   | defaultValue | O | 字段为非空时，必须设置默认值。  * 主键不支持设置默认值。 * 加密字段和敏感字段不支持设置默认值。 * 数据类型为ByteArray、Date不支持为其设置默认值。 * 数据类型为Text的字段设置默认值时，默认值的长度小于或等于200个字符。 |

   例如，我们可为“objecttype1”对象类型配置如下字段。

   | fieldName | fieldType | belongPrimaryKey | notNull | isNeedEncrypt | defaultValue |
   | --- | --- | --- | --- | --- | --- |
   | author | String | true | true | - | - |
   | shadowFlag | Boolean | - | true | - | true |
   | bookName | String | - | - | - | - |
   | id | Integer | - | - | - | - |
   | price | Double | - | - | - | - |
   | publishTime | Date | - | - | - | - |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/F2DVhqD_QiK4kWaS1B5PaQ/zh-cn_image_0000002214858781.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=7BA240550E2434C21EB63B264ED26C2ED38C96A98357700A52F561F2F509CE14)
4. 在“indexes”中为该对象类型配置索引、索引包含的字段、以及索引包含的字段的排序方式。

   | 参数 | 必选(M)/可选(O) | 说明 |
   | --- | --- | --- |
   | indexName | M | 索引名称。  输入要求具体如下：  * 索引的名称长度必须大于或等于1个字符，小于或等于30个字符，只能包含以下3种类型，并且至少包含“字母”类型：   + 字母（A-Z或a-z）   + 数字（0-9）   + 特殊字符：\_ * 索引名称必须以字母开头。 * 索引名称中不区分字母的大小写。 * 修改对象类型时，仅支持新增或者删除索引。当删除索引后，本次提交前不允许新增同名索引。 * 每个对象类型可以设置小于或等于16个索引。 * 数据类型为ByteArray和Text的字段不支持设置为索引。 |
   | indexList > fieldName | M | 索引包含的字段。  支持设置组合索引，由多个字段组合成为索引，一个组合索引包含的字段不超过5个。 |
   | indexList > sortType | M | 索引包含的字段的排序方式，支持升序或降序。 |

   例如，我们可为“objecttype1”对象类型配置如下两个索引。

   | indexName | fieldName | sortType |
   | --- | --- | --- |
   | id\_Index | id | ASC |
   | price\_Index | price | DESC |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/xNtBHNL6S5KCGM4w9TQvug/zh-cn_image_0000002179338460.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=F2424F9A7BD399D32D7A6EC3FD4DB9A4DF133CAE0F85413E91F07A63D09C3685)
5. 在“permissions”中设置各角色是否具有该对象类型的Read、Upsert（包含新增和修改）和Delete权限。

   | 参数 | 必选(M)/可选(O) | 说明 |
   | --- | --- | --- |
   | role | M | 用户角色，包括：  * World：代表所有用户，包含认证和非认证用户。该角色默认拥有Read权限，可自定义配置Upsert和Delete权限。但是，不建议将Upsert和Delete权限配置给所有人角色。当对象类型中设置了加密字段之后，表示开启全程加密功能，此时所有人角色将不会拥有Read、Upsert和Delete权限，且不允许修改。 * Authenticated：经过AGC登录认证的用户。该角色默认拥有Read权限，可自定义配置Upsert和Delete权限。当对象类型中设置了加密字段之后，表示开启全程加密功能，此时认证用户角色将不会拥有Read、Upsert和Delete权限，且不允许修改。 * Creator：经过认证的数据创建用户。该角色默认拥有所有权限，且可自定义配置所有权限。每条数据都有其对应的数据创建人（即应用用户），每个数据创建者仅可以Upsert或者Delete自己创建的数据，不能Upsert或者Delete他人创建的数据。数据创建者的信息保存在数据记录的系统表中。 * Administrator：应用开发者，主要是指通过AGC控制台或FaaS（Function as a Service，函数即服务）侧访问云数据库的角色。该角色默认拥有所有权限，且可自定义配置所有权限。Administrator可以管理并配置其他角色的权限。 |
   | rights | M | 授予角色的权限，包括Read、Upsert（包含新增和修改）和Delete权限。 |

   说明

   各角色只能完成对应权限的操作，超出权限范围的操作云侧将返回“permission denied”错误。由于端云一体化工程的初始化代码未[配置AccessToken](../harmonyos-references/cloudfoundation-cloudcommon.md#getaccesstoken)，故“CloudProgram/clouddb/objecttype/Post.json”中给World角色添加了Upsert和Delete权限。

   例如，我们可按下表为各个角色配置“objecttype1”对象类型的权限。

   | 角色 | Read | Upsert | Delete |
   | --- | --- | --- | --- |
   | World | √ | – | – |
   | Authenticated | √ | √ | – |
   | Creator | √ | √ | √ |
   | Administrator | √ | √ | √ |

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Oiks_HqoQje85UIa8ulnjw/zh-cn_image_0000002214858785.png?HW-CC-KV=V1&HW-CC-Date=20260427T235504Z&HW-CC-Expire=86400&HW-CC-Sign=1A5183A5834E9750614F8F262A443BFC0CAA7AC13E9BC6EF09E2B005DEC0633A)
