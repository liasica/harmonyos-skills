---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-137
title: 应用和元服务列表中无图标显示
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用和元服务列表中无图标显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:79678ea4cd6c0877f2a81774c80014661dc57fb4d5d531fffbd573895bc6947b
---

## 问题现象

在系统的“设置->应用和元服务”中，列表中无图标显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xGNLiYspT9CdVZ3m25bulw/zh-cn_image_0000002628789134.png "点击放大")

## 背景知识

* [应用图标](../design-guides/application-icon-0000001953444009.md)设计的核心是简洁、高效和品牌识别度。一个好的图标可以准确传达应用相关信息，也可以帮助用户快速定位你的应用。应用图标分为[分层图标](../harmonyos-guides/ui-design-layered-process.md)和[单层图标](../harmonyos-guides/ui-design-normal-process.md)，分层图标包括前景图和背景图两层。
* [应用图标和名称配置](../harmonyos-guides/application-component-configuration-stage.md#应用图标和名称配置)通常一起配置，对应app.json5配置文件和module.json5配置文件中的icon和label。

## 问题定位

查看工程代码的app.json5文件，app->icon配置项是否配置错误，配置的图片资源是否仅仅是白色背景。

## 分析结论

工程代码的app.json5文件，配置项app->icon配置错误，配置的图片资源仅仅是白色背景，不是带有前景图和背景图的分层图标。

## 修改建议

参考[分层图标-开发步骤](../harmonyos-guides/ui-design-layered-process.md#开发步骤)，在工程代码的app.json5文件，正确配置app->icon配置项为带有前景图和背景图的资源变量。

工程AppScope路径文件结构如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/XB7YVWucQdyMH80Il1gcKg/zh-cn_image_0000002658988445.png "点击放大")
