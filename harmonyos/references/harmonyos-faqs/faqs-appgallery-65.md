---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-65
title: 邀请测试时无法选取上传的软件包怎么办
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 邀请测试时无法选取上传的软件包怎么办
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7997b69e815defbe62733318770c151d4d09c660ee418a54e233572222b317d4
---

## 问题现象

* 场景一，软件包已上传并通过检测，但在发布邀请测试时所有软件包选项均显示为灰色不可选状态。如下，已上传软件包：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/DU_Dk5O1TwaxXCA8dl3o1A/zh-cn_image_0000002628554520.png "点击放大")

  版本选项全是灰色的，无法选取：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/I2cWvfmARHuxu1jO6WR7-A/zh-cn_image_0000002658913841.png "点击放大")
* 场景二，在发布环节版本选取界面，选择的待发布软件包提示该状态为较低版本，不能选择使用。

  问题截图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/I-qHGXIqSGaokfyuXjk4jA/zh-cn_image_0000002658793899.png "点击放大")

## 解决方案

* 场景一问题可能由以下两种情况导致：

  1、构建的软件包不支持邀请测试，比如软件包仅支持HarmonyOS 3.0/4.3以下版本。邀请测试软件包的API版本至少需要10或以上，支持的应用类型需为HarmonyOS 5或以上版本，具体可参见邀请[业务介绍](../app/agc-help-invite-test-overview-0000002287701773.md)。

  2、若软件包的发布国家或地区未包含中国大陆地区，需在版本信息中勾选中国大陆地图，并重新创建测试任务。
* 场景二可按照以下途径排查：

  检查工程app.json5中versionName和versionCode格式是否正确，其次新包versionCode必须同时高于全网正式版和所有分阶段版本。

  登录AppGalleryConnect→APP与元服务→进入应用→查看“版本信息”，确认正式环境中最新的版本号，如果待发布版本号确实高于正式版本，尝试刷新页面，清除浏览器缓存。

## 总结

版本号是在上传的软件包中自动解析的，对应工程中的app.json5中的versionCode和versionName字段。AGC操作界面上的版本对应versionName，版本号对应versionCode。

版本号规范：

* 测试版本的versionCode必须高于发布过的全网版本的versionCode。
* 测试版本的versionCode不能低于发布过的测试版本的versionCode。
* 如已安装的测试版本的versionCode和正式版本的versionCode相同，则当测试版本转为正式发布后，会自动更新到正式版本。
* 正式版本上架后，同版本名称（versionName）同版本号（versionCode）的公开测试版本会自动下架。
