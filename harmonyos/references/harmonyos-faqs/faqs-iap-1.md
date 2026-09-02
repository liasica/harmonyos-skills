---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-1
title: 数字商品配置后如何生效与测试
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 数字商品配置后如何生效与测试
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:247eac6b80793b4061edab1f0fd8b47a5d22093652e64c4302d85ed9b66605f3
---

## 问题现象

1. 数字商品配置完成后如何生效，是否一定要跟随应用版本提交审核？
2. 数字商品和应用版本一起关联提交审核，是否会因无测试条件等原因而审核驳回？
3. 数字商品测试是否可以使用邀请测试或者公开测试进行测试而不提交正式版本审核？

## 背景知识

[提交数字商品审核](../app/submit-digital-products-for-review-0000002107823817.md)：在为应用提交首个数字商品或新增数字商品类型时，必须同时提交新的应用版本。提交数字商品至审核前，请确保其处于“待提交”状态；否则，请先完善所有缺失信息。

[测试数字商品服务](../harmonyos-guides/store-iap-sandbox.md)：数字商品正式上架前可以通过沙盒测试来进行商品测试。

## 解决方案

1. 数字商品审核分为两种类型[首次提交数字商品或新增数字商品类型](../app/first-digital-products-for-review-0000002071877226.md)和[提交已生效类型的数字商品](../app/effective-digital-products-for-review-0000002107756845.md)：
   * 首次提交数字商品或新增数字商品类型：如果一个应用首次提交数字商品审核应跟随应用版本一起提交或者该应用版本新增数字商品类型（如已有消耗型商品，新增非消耗型商品），新增的非消耗型的数字商品应跟随应用版本一起提交，商品添加路径可以参考如下图片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/kMJCFJZ2Qjy_iSei4V18Jw/zh-cn_image_0000002658913787.png "点击放大")
   * 提交已生效类型的数字商品：应用已有某类型的一个或多个数字商品通过审核，后续该类型的数字商品可以直接提交，无需随新的应用版本一同提交，可以在商品列表页面直接提交审核或者编辑商品信息后再提交审核，具体可以参考如下图片。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/5MusiQbVRlC4DWSnELA0KQ/zh-cn_image_0000002658793843.png "点击放大")
2. 不会的，审核侧在审核应用版本的时候会关注该版本是否有关联数字商品，有关联数字商品的话，会先将应用版本审核通过，然后再进行数字商品测试审核的，不会因无测试条件而将该版本驳回，仍被驳回可能是商品类型配置之类错误（如永久类的商品配置为非续期类的商品），该类问题请参考审核意见进行修改后再重新提交审核。
3. 不能的，数字商品正式环境测试，必须要跟随应用版本审核通过后才能使用，前期测试商品服务建议使用应用内支付服务提供的[沙盒测试](../harmonyos-guides/iap-sandbox.md)来调测。

## 常见FAQ

Q：沙盒测试是否可以通过邀请测试或者公开测试来进行测试？

A：不能的，沙盒测试是需要使用调试证书来打包应用的，而邀请测试或者公开测试都是发布证书打包的。

Q：数字商品配置有哪几种方式？

A：两种，可以[通过AppGallery Connect配置数字商品](../harmonyos-guides/store-iap-product-agc.md)和[通过Server API配置数字商品](../harmonyos-guides/store-iap-product-server.md)来配置商品信息。
