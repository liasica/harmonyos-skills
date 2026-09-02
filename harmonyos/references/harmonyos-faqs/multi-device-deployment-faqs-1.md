---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/multi-device-deployment-faqs-1
title: 应用在平板桌面和手机桌面显示的图标不一样
breadcrumb: FAQ > 多设备场景 > 一次开发多端部署 > 应用在平板桌面和手机桌面显示的图标不一样
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:855397f1fa90f7041cffea0c204a0af8250637c42cda87b332bb20604cdd9fe6
---

## 问题现象

应用在平板上桌面图标和在手机上的桌面图标不一样。

## 背景知识

* [资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)：应用开发过程中，需要使用字符串、颜色、字体、间距和图标等资源。不同设备或配置下，这些资源的值会有所不同。
* [图标和名称配置](../harmonyos-guides/application-component-configuration-stage.md#应用图标和名称配置)：图标和名称通常一起配置，对应app.json5配置文件和module.json5配置文件中的icon和label。

## 问题定位

1. 应用可以根据不同设备配置不同图标，建议检查代码中entry->src->main->resources文件夹以及AppScope->resources文件夹中是否有限定词目录phone（手机）/tablet（平板）目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/KOrGsmiKSu-by7uYdJ-i7w/zh-cn_image_0000002628392498.png "点击放大")
2. 建议检查module.json5配置文件的abilities标签中未设置icon，和app.json5中的icon，是否仅仅在phone目录中添加了图标图片，当应用只配置了phone手机端图标，未配置tablet平板图标并且base目录下也未放置图标的图片时，会导致应用在平板打开，图标显示异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/0A4uekLoQu64A_rYzFF0Jw/zh-cn_image_0000002658791769.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/UM_dGcVkRteVAzGMB2F60Q/zh-cn_image_0000002628552390.png "点击放大")

## 分析结论

应用仅配置了手机端图标，未配置平板端图标，且base目录下也未配置图片，导致应用在平板上，系统读取不到图片资源，就展示了默认图标。

## 修改建议

在entry->src->main->resources文件夹以及AppScope->resources文件夹中添加tablet（平板）目录。或者在base目录中添加对应图标图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/SLcwkb2jRUyuEUtOAZrupQ/zh-cn_image_0000002658911717.png "点击放大")
