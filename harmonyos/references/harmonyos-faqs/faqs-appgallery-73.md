---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-73
title: 应用市场提交版本时报错，软件包中含有不允许使用的权限，怎么定位
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用市场提交版本时报错，软件包中含有不允许使用的权限，怎么定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:33+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:10d58a3411acb29a07353e78b8b8c384207840ada7f3219777ce7dbc820e865d
---

## 问题现象

应用市场提交版本时报错"软件包中含有不允许使用的权限"，如何获知是什么权限有问题？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/0IE7_J5sQSuBBoiYwqy-vw/zh-cn_image_0000002628554524.png "点击放大")

## 背景知识

开发者[上传软件包](../app/agc-help-release-atomic-upload-pkg-0000002293811142.md)时，HarmonyOS 开发者中心会对上传的包进行基础合法检测并展示检测结果。

## 问题定位

开发者可通过软件包管理页面，点击**报告**，查询详细的检测报告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/se82f1xCT8SOozbIttRTng/zh-cn_image_0000002658913843.png "点击放大")

在检测结果页面，鼠标放置或点击修改意见一栏，即可看到详细的修改意见。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/r-igjVm_RF24njrSLG9huA/zh-cn_image_0000002658793901.png "点击放大")

## 分析结论

元服务软件包审核，扫描出权限ohos.permission.APP\_TRACKING\_CONSENT不允许使用。

## 修改建议

项目工程中移除权限ohos.permission.APP\_TRACKING\_CONSENT。
