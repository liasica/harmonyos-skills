---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-501
title: 平板上应用启动页显示不全
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 平板上应用启动页显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a02fff14883916a70611bc16e5bb57e58e0480fad4cafbb43c3906a9ec481d5b
---

## 问题现象

平板上应用启动时，启动页底部图标显示不全，有截断现象。

## 背景知识

启动页分为[简易启动页](../harmonyos-guides/launch-page-config.md#配置简易启动页)和[增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)，开发者通过在module.json5配置文件中的[abilities](../harmonyos-guides/module-configuration-file.md#abilities标签)标签配置启动页资源。

* startWindowIcon字段，标识当前UIAbility组件简易启动页面图标资源文件的索引，此图标资源会在启动页面上按实际大小居中显示，不会随窗口尺寸进行缩放，当startWindow被配置时该字段失效。
* startWindow字段，标识当前UIAbility组件增强启动页面配置资源json文件的索引，以提供更丰富的启动页资源配置项，具备根据窗口尺寸进行缩放的能力，更易于多设备适配设计，更有利于“一次开发，多端部署”。

## 问题定位

排查代码module.json5文件中的abilities标签，配置的启动页资源，是配置的startWindowIcon字段还是startWindow字段。

## 分析结论

代码中module.json5文件中abilities标签配置的是startWindowIcon，且未配置startWindow。

这时应用启动页的图标，会采用startWindowIcon索引指向的图标资源，该图标不会随窗口尺寸进行缩放，导致平板上启动页的图标未能很好的适配，出现显示不全的问题。

## 修改建议

1. 应用配置简易启动页，应用图标不会随窗口尺寸进行缩放，为避免在其他尺寸设备上的显示效果无法自动适配，建议开发者避免设计针对单个产品的图标资源，可以使用具备普适性的图标资源。
2. 应用配置增强启动页，应用图标具备根据窗口尺寸进行缩放的能力，平板上启动应用时，启动页图标会根据当前窗口尺寸自动进行缩放，避免启动页显示不全的问题。
