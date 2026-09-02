---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-96
title: 如何查看和管理HarmonyOS Next应用市场的用户评论数据
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何查看和管理HarmonyOS Next应用市场的用户评论数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4fe7378a9c768c8e6ef3a518f2b6d583a0ad1d7419aa43379ce52e0896703695
---

## 问题现象

HarmonyOS Next应用上架应用市场后，用户在应用市场的评论数据如何在后台进行集中的查看，同时进行导出、回复、删除等操作？

## 背景知识

1. HarmonyOS Next应用市场评论评分系统已完成升级，新的评论评分系统已经接入到[应用推广引擎](https://developer.huawei.com/consumer/cn/service/apcs/aggrowth/chassis/resources/interactiveTools)新平台。开发者可以通过新平台，查看和管理HarmonyOS Next应用的评论评分数据。
2. HarmonyOS 5.0以下应用仍然在AGC平台进行应用评论评分数据查看和管理。入口为：AGC平台-运营-用户运营-互动评论。具体可参见[互动评论](../app/game-center-interaction-comments-0000001239182361.md)。

## 解决方案

1. 操作路径：登录[应用推广引擎](https://developer.huawei.com/consumer/cn/service/apcs/aggrowth/chassis/resources/interactiveTools)，选择“用户经营-用户互动”，即可进入“评论评分”页面。默认展示“用户评论”数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/Tf6S4Cx8ROWZ4Mmk5fHMzw/zh-cn_image_0000002628394704.png "点击放大")
2. 除了查看评论数据，还可以进行评论数据的导出、回复等操作。具体参见[评论与评分](../app/comment-management-0000002246992933.md)。

## 常见FAQ

Q：评论数据切换到应用推广引擎了，是不是老的AGC平台中互动评论不能使用了？

A：HarmonyOS Next应用在应用推广引擎进行评论数据管理；HarmonyOS 5.0以下应用仍然在AGC平台中的互动评论模块进行评论数据管理。HarmonyOS Next游戏既可以在AGC互动评论模块，也可以在应用推广引擎进行评论数据管理。

Q：为什么登录应用推广引擎时，提示账号未实名？

A：首次登录应用推广引擎时，必须使用账号持有者关联的华为账号（即主账号）登录，不能使用团队子账号登录。但账号持有者登录后可在“账号管理”对协作者进行授权使用，即可以授权子账号进行评论数据管理。

Q：除了页面进行评论数据的管理，是否有API可以调用查看？

A：可以通过[Comments API](../AppGallery-connect-References/agcapi-commentapi-0000001115868340.md)，高效管理您的HarmonyOS应用评分数据，支持查询应用的评论评分列表，回复用户的评论。

Q：是否可以在HarmonyOS Next应用内实现评论和评分？

A：可以接入[应用评论服务](../harmonyos-guides/appgallery-comment.md)，用户无需进入应用市场应用详情页，可以直接在应用内进行评论。

Q：在应用市场评论的数据为什么其他人看不到，管理台也看不到？

A：为了防止恶意刷屏，评论是需要审核的，只有通过审核的评论才会显示。
