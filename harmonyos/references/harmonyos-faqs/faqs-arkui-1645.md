---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1645
title: 设置Text字体颜色后，手机运行项目，字体仍显示为黑色
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 设置Text字体颜色后，手机运行项目，字体仍显示为黑色
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:988bdf66357f56c3ed221ad7c196d44c3afd8637279e56d03fd8382d4b086175
---

## 问题现象

在ArkTS项目中设置Text字体颜色[fontColor](../harmonyos-references/ts-basic-components-text.md#fontcolor)为蓝色后，手机运行项目，字体仍显示为黑色。多台同型号手机运行同一项目，只有一台出现该问题。

## 解决方案

该问题的出现是由于问题手机开启了“高对比度文字”开关，开启“高对比度文字”后，所有应用的浅色背景字体均会显示为黑色。

解决方案：

* 关闭“设置”-“辅助功能”-“高对比度文字”开关。
* 如需配置应用字体颜色不跟随系统“高对比度文字”变化，可设置[text.setTextHighContrast](../harmonyos-references/js-apis-graphics-text.md#textsettexthighcontrast20)模式为TEXT\_APP\_DISABLE\_HIGH\_CONTRAST，关闭应用的文字渲染高对比度配置，该模式的优先级高于系统设置中的高对比度文字配置。此方法从HarmonyOS 6.0.0（API version 20）开始支持。

  配置方法：text.setTextHighContrast(text.TextHighContrast.TEXT\_APP\_DISABLE\_HIGH\_CONTRAST)。
