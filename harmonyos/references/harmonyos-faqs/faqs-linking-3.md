---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-linking-3
title: 如何在上架之前测试AppLinking导向自己App的链接
breadcrumb: FAQ > 应用服务开发 > 应用链接跳转服务（App Linking Kit） > 如何在上架之前测试AppLinking导向自己App的链接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ef2ac6cbbd86d68fa7e5be3b44c6ec869db6526f17e63e4f5b59f33534773295
---

## 问题现象

应用还未上架，无法在应用商店找到，如何测试AppLinking拉起应用的功能？

## 解决方案

* **App Linking应用链接按角色分为三种类型：**
  1. 云端开发：[开通App Linking服务](../harmonyos-guides/applinking-enable-applinking.md)、[建立域名与应用关联关系](../harmonyos-guides/app-linking-startupapp.md#建立域名与应用关联关系)、[在AGC为应用创建关联的网址域名](../harmonyos-guides/app-linking-startupapp.md#在agc为应用创建关联的网址域名)。
  2. 客户端开发：[在module.json5中配置关联的网址域名](../harmonyos-guides/app-linking-startupapp.md#在modulejson5中配置关联的网址域名)、[处理传入的链接](../harmonyos-guides/app-linking-startupapp.md#处理传入的链接)、[验证应用被拉起效果](../harmonyos-guides/app-linking-startupapp.md#验证应用被拉起效果)。
  3. 前端开发：开发链接对应的H5网页，应用未安装时呈现Web版内容。
* **App Linking链接类型能力不同对上架应用市场的要求不同：**
  + 普通App Linking链接：验证跳转App不需要应用上架应用市场。
  + [直达应用市场能力](../harmonyos-guides/applinking-direct-to-ag.md)的App Linking链接：必须要求应用已上架，才能实现直达能力。
  + 对于应用市场详情页的App Linking链接：格式如https://appgallery.huawei.com/app/detail?id={bundleName}，必须应用上架以后才有对应落地页面。
* **普通App Linking链接未上架测试拉起步骤如下：**
  1. 确认已完成云端开发、客户端网址域名关联配置与处理传入的链接。
  2. 目标方应用必须使用手动签名完成应用证书签名，不能使用DevEco Studio的自动签名功能，否则无法拉起应用。可以使用手动签名调试证书本地安装方式或发布邀请测试验证应用拉起。
  3. 拉起方应用可以通过[UIAbilityContext.openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口等方式测试应用拉起，详情参考[验证应用被拉起效果](../harmonyos-guides/app-linking-startupapp.md#验证应用被拉起效果)。也可以使用命令行模拟点击链接方式测试拉起应用hdc shell aa start -U "App Linking链接" --pb appLinkingOnly true。
