---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-126
title: 启动页展示系统默认图标问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 启动页展示系统默认图标问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:97bd8d41f79feef81dabcd8aeaeed2e09cf0e8f8ae6db944a8ef393c39cb5e88
---

## 问题现象

应用启动页图标展示的是系统默认图标，如何修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/1tk1mlIxTwmKLr4-E0QxYQ/zh-cn_image_0000002628629222.png "点击放大")

## 背景知识

启动页是应用冷启动时显示的第一个页面，在应用进程没有运行或者应用内容没有加载完成前，都将显示启动页，应用可以根据自己的设计[配置应用启动页](../harmonyos-guides/launch-page-config.md)。

## 问题定位

查看module.json5配置文件中是否配置了启动页图标startWindowIcon或启动页资源startWindow，并确认启动页图标是否按预期配置期望的图标资源。

## 分析结论

module.json5配置文件的startWindowIcon字段未设置期望的应用图标资源，导致启动页图标展示的是系统默认图标。

## 修改建议

根据应用的设计理念，在module.json5配置文件的startWindowIcon字段设置期望的应用图标资源，可以通过Image Asset[生成单层图标](../harmonyos-guides/ide-apply-generated-icon.md)功能生成；如果不需要单独图标的启动页，需要更复杂的启动页配置，如全屏资源展示等，可以使用startWindow字段[配置增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)。
