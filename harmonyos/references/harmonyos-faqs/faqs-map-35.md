---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-35
title: 如何解决模拟器加载地图显示空白
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何解决模拟器加载地图显示空白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:2e521c3a067b2528c3249e0a045277d9cc24cc924d068f49e69be7e8a4f51fdf
---

## 问题现象

DevEco Studio支持使用模拟器实现Map Kit地图服务的地图加载，但实际使用模拟器加载地图时，经常出现地图显示空白情况，如何解决？

## 背景知识

* 模拟器：模拟器是开发和调试HarmonyOS应用/元服务的便捷工具，模拟器使用指导请参见[使用模拟器运行应用](../harmonyos-guides/ide-run-emulator.md)。
* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。

## 解决方案

模拟器加载地图显示空白请参考以下步骤进行排查和处理：

1. 是否DevEco Studio版本低于DevEco Studio 5.1.0 Release。

   DevEco Studio从DevEco Studio 5.1.0 Release版本开始支持模拟器加载地图，如果版本低于DevEco Studio 5.1.0 Release，请至官网下载[最新版本](https://developer.huawei.com/consumer/cn/download/)。
2. 是否进行了签名。

   HarmonyOS部分特性使用模拟器时，不需要进行签名。但地图服务需要签名后才能使用，请参见[配置调试签名](../harmonyos-guides/ide-signing.md)。
3. 是否开通了地图服务。

   使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)，通过DevEco Studio开通地图服务时，可以使用自动签名；通过AppGallery Connect网站开通地图服务时，需要使用手动签名。
4. 是否使用了内部网络环境。

   有些公司内部网络环境对网络访问能力做了限制，建议使用外网环境或者在模拟器上配置网络代理。参见[网络代理](../harmonyos-guides/ide-emulator-more-features.md#section206461549731)。
