---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-9
title: 如何处理部署云数据库对象失败：clouddb deploy failed. Reason is the index cannot be modified.
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 如何处理部署云数据库对象失败：clouddb deploy failed. Reason is the index cannot be modified.
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d658f142eea77fe2867ec5b059903e069db9e3d0cca95cb6a98e67ac18766016
---

## 问题现象

在DevEco新创建的云数据库对象类型，部署失败“clouddb deploy failed. Reason is the index cannot be modified”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/M5fdJKSYTR-ZNc2Rgbf2Zw/zh-cn_image_0000002628554626.png)

## 背景知识

* [云数据库](../harmonyos-guides/agc-harmonyos-clouddev-dbprocess.md)是一款端云协同的数据库产品，提供端云数据的协同管理、统一的数据模型和丰富的数据管理API接口等能力。云数据库采用基于对象模型的数据存储结构。
* [部署云数据库](../harmonyos-guides/agc-harmonyos-clouddev-deploydatabase.md)对象类型中的fieldType等字段信息，部署到AGC云端后，请勿在本地再做修改。如需更改fieldType等字段信息，请先删除云端部署的对象类型。需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。

## 问题定位

1. 直接修改对象类型中的indexName字段后，重新部署该对象类型后报错“clouddb deploy failed. Reason is the index cannot be modified”。
2. 在修改原对象类型中的indexName字段后，新创建对象类型再部署云数据库后，同样提示“clouddb deploy failed. Reason is the index cannot be modified”，在原对象类型中的indexName字段还原后再部署新对象类型成功。

## 分析结论

对象类型部署到AGC云端后，请勿在本地再做修改。否则原对象类型或者新创建数据类型将再次部署失败。

## 修改建议

1. 恢复被修改的indexName字段后，重新部署新创建的对象类型。
2. 如需更改indexName等字段信息，请先删除云端部署的对象类型。再重新部署修改后的对象类型。需要注意的是，删除云端对象类型，对象类型内添加的数据也将一并删除，且不可恢复。
