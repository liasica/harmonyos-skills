---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokeclouddatabase
title: 在端侧访问云数据库
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:08+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:45485ce5f13d2c6999551e25e4680030798b4bcd7036b797475f4f5f0c27b918
---

## 前提条件

* 请确保[云数据库已正确开发并部署](agc-harmonyos-clouddev-deploydatabase.md)。
* 请确保“AppScope/resources/rawfile/schema.json”文件已存在。

  注意

  云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。

  如果后续又在本地工程修改了对象类型，请重新部署云数据库，DevEco Studio将自动更新schema.json文件；如果后续在AGC云侧修改了对象类型，您需[手动从AGC控制台导出schema.json文件](../AppGallery-connect-Guides/agc-clouddb-agcconsole-objecttypes-0000001127675459.md#section1558018208151)，拷贝至本地工程的“AppScope/resources/rawfile”目录下。否则，可能导致schema.json文件中的对象类型和代码中的对象类型不一致，端侧访问云数据库时提示[1008230002](../harmonyos-references/cloudfoundation-arkts-error-code.md#section1008230002-云数据库schema配置错误)错误。

* 检查您的角色拥有的对象类型操作权限。如果未[配置AccessToken](../harmonyos-references/cloudfoundation-cloudcommon.md#getaccesstoken)，需要给World角色添加Upsert和Delete权限。

## 生成Client Model

在端侧通过Cloud Foundation Kit访问云数据库，需先引入对应云数据库对象类型的Client Model。

参考[生成Client Model](agc-harmonyos-clouddev-modelclass.md#section1037851593420)生成云数据库对象类型的端侧模型，如下图初始化代码中的Client Model示例“ets/pages/CloudDb/Post.ts”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/MBNStfIdSk2oI2bUA9AW8g/zh-cn_image_0000002295988348.png?HW-CC-KV=V1&HW-CC-Date=20260427T235507Z&HW-CC-Expire=86400&HW-CC-Sign=36DEABDAA20CAC2237AF056C2C3179F7A50AD99960A2A911405F7062FA37EE74)

## 访问数据库

接下来您便可参考[初始化数据库访问](cloudfoundation-database-initialize.md)、[查询数据](cloudfoundation-database-query.md)、[写入数据](cloudfoundation-database-upsert.md)、[删除数据](cloudfoundation-database-delete.md)等访问数据库。

“src/main/ets/pages/CloudDb”目录下提供了部分示例代码，更完整的接口信息请参考[Cloud Foundation Kit API参考-云数据库模块](../harmonyos-references/cloudfoundation-clouddatabase.md)。
