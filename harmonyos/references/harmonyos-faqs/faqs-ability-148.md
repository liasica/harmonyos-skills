---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-148
title: 如何解决在真机上点击桌面App启动但跳转到了通知页的问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何解决在真机上点击桌面App启动但跳转到了通知页的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f043a1a9a24a6e4952a4191a32dda9c0363ac6c0d74466782ea3ce0d124946db
---

## 问题现象

在真机上，单击应用图标，没有按预期打开对应的应用的启动页并进入APP主页，而是点击后直接跳转到系统设置中被点击应用的通知设置页面。

同时可以看到后台的APP是白屏状态（深色模式下为黑屏），并且点击后仍会继续跳转到设置页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/vML3YGvFQSKkF6xsiwmX1A/zh-cn_image_0000002628629348.png "点击放大")

## 背景知识

[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)：标识当前UIAbility组件或ExtensionAbility组件能够接收的[Want](../harmonyos-guides/want-overview.md)特征集，为数组格式。

配置规则：

* 对于Entry类型的HAP，应用可以配置多个具有入口能力的skills标签（即配置了ohos.want.action.home和entity.system.home）。
* 对于Feature类型的HAP，只有应用可以配置具有入口能力的skills标签，服务不允许配置。

## 问题定位

根据问题现象，发现点击应用图标后实际并未运行APP，而是直接跳转到系统设置页。且任务视图中，APP处于白屏状态，点击仍跳转设置。因此可确定该应用实际未进入代码执行层级，初步判断为项目配置问题。需要检查Entry模块下module.json5的[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)配置项是否正确。

## 分析结论

该问题是由于配置文件错误导致的启动异常，可通过对比新建项目的标准配置文件，精准定位差异项并修复。

## 修改建议

参照[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)进行修改，确保[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)配置正确。
