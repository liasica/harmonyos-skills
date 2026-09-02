---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-160
title: 应用内点击拉起第三方应用失败
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用内点击拉起第三方应用失败
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:87e9e268c799b1c7ceb33542df2a6e4654ccd48674bb90c4f129c89f8559381d
---

## 问题现象

应用内点击第三方应用图标，出现短暂loading后，没有成功拉起跳转到第三方应用。

## 背景知识

* [拉起指定应用](../harmonyos-guides/app-startup-overview.md)：发起方应用明确指定跳转的目标应用，来实现应用跳转。指向性跳转可以分为指定应用链接、指定Ability两种方式。指定应用链接（推荐）：通过[openLink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)或[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口来指定[应用链接](../harmonyos-guides/app-startup-overview.md#应用链接)，拉起目标应用页面。
  + Deep Linking：是一种通过链接跳转至应用特定页面的技术，其特点是支持开发者定义任意形式的scheme。由于缺乏域名校验机制，容易被其他应用所仿冒。
  + App Linking：其限定了scheme必须为https，同时通过增加域名校验机制，可以从已匹配到的应用中筛选过滤出目标应用，消除应用查询和定位中产生的歧义，直达受信的目标应用。
* [startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)：启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。
* [Want.flags](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags)字段常用的系统预置关键字。开发者可以通过这些预置关键字设置或获取应用跳转等场景中额外携带的标志位信息。其中FLAG\_START\_WITHOUT\_TIPS表示是否关闭匹配失败弹窗功能。

## 场景一

### 问题定位

排查context.openLink(link, { appLinkingOnly: true })中使用的link链接是否正确。

### 分析结论

context.openLink(link, { appLinkingOnly: true })中使用的link链接不是https的链接。

### 修改建议

context.openLink(link, { appLinkingOnly: true })中使用的link链接，必须为https开头的链接，参考如下：

```txt
let link: string = "https://www.example.com/programs?action=showall";
```

## 场景二

### 问题定位

排查Want中的flags字段是否设置为FLAG\_START\_WITHOUT\_TIPS。

### 分析结论

Want中的flags字段设置为FLAG\_START\_WITHOUT\_TIPS，导致没有能够匹配的应用，没有弹框提示。

### 修改建议

flags字段非必填字段可省略，参考如下：

```txt
let want: Want = { uri: "link://www.example.com" };
```
