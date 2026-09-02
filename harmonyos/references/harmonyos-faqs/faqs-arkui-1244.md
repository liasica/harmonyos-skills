---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1244
title: 自由多窗模式下，应用最大化时顶部未避让挖孔区
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自由多窗模式下，应用最大化时顶部未避让挖孔区
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:460cd86f7998d18d4c3d9f094d681500904ad9c7573f2bd9ce053d1a017bb7bd
---

## 问题现象

应用在平板自由多窗模式下启动并最大化后，顶部被挖孔区遮挡。

## 背景知识

[安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)：安全区域是指页面的显示区域，默认不与系统设置的非安全区域比如状态栏、导航栏区域重叠，默认情况下开发者开发的界面都布局在安全区域内。挖孔区域不属于避让区，页面默认不会避让挖孔区域。从API Version 12开始，可在[module.json5](../harmonyos-guides/module-configuration-file.md)中添加配置项[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)，将挖孔区域会视为避让区，实现页面默认避让挖孔区域。

## 问题定位

建议检查代码中module.json5中配置项是否添加了metadata配置项，将挖孔区添加为默认避让区域。

## 分析结论

代码中module.json5没有添加配置项metadata，导致挖孔区域未被视为避让区，页面默认不进行避让。

## 修改建议

在module.json5文件中增加配置项metadata，将挖孔区域视为非安全区，实现页面默认避让挖孔，具体可参考官方文档安全区域顶部的[说明](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)，或参考官网[挖孔避让案例](../best-practices/bpta-multi-device-window-immersive.md#section35561799107)。
