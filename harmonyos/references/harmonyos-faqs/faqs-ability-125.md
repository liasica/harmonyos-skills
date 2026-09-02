---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-125
title: 点击短信中的链接无法跳转至目标应用的页面
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 点击短信中的链接无法跳转至目标应用的页面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:32+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:902e05199a8d49fce256740922f838374e8aae98f6749506b1ad995c364a245a
---

## 问题现象

用户点击短信中的链接，未正确进行跳转：

1. 点击链接后无法导向应用程序。
2. 虽然链接可以被打开，但显示的页面并非预期内容。

## 背景知识

按照应用链接的scheme以及校验机制的不同，可以分为[Deep Linking](../harmonyos-guides/knock-share-between-phones-content.md#deep-linking)与[App Linking](../harmonyos-guides/knock-share-between-phones-content.md#app-linking)两种方式。

* Deep Linking：是一种通过链接跳转至应用特定页面的技术，其特点是支持开发者定义任意形式的scheme。由于缺乏域名校验机制,容易被其他应用所仿冒。
* App Linking：其限定了scheme必须为https，同时通过增加域名校验机制,可以从已匹配到的应用中筛选过滤出目标应用，消除应用查询和定位中产生的歧义，直达受信的目标应用。

## 问题定位

1. 查看[module.json](../harmonyos-guides/module-configuration-file.md)文件，可搜索对应关键词进行排查：
   * 搜索exported：exported配置应为true，如果exported为false，仅具有权限的系统应用能够拉起该应用，否则无法拉起应用。
   * 搜索scheme：scheme须配置为https，host须配置为关联的域名，path可选，表示域名服务器上的目录或文件路径。
2. 在应用EntryAbility中，可搜索[onCreate()](../harmonyos-guides/uiability-lifecycle.md#oncreate)或者[onNewWant()](../harmonyos-guides/uiability-lifecycle.md#onnewwant)，查看生命周期回调，检查处理传入的链接。
3. 检查链接的有效性，通过将其复制到浏览器中进行验证。

## 分析结论

### 场景一

配置文件与Ability中生命周期回调均无问题，链接无法打开，为无效链接。

### 场景二

应用在module.json中配置了"scheme": "https"，在隐式拉起不传入具体entities的情况下会被系统识别为浏览器一类应用。

```screen
let want: Want = { 
    action: 'ohos.want.action.viewData', 
  }; 
context.startAbility(want)
```

## 修改建议

### 场景一

提供正确有效的链接地址。

### 场景二

* 如果无特殊的场景要求，即非浏览器应用。建议去掉"scheme": "https"字段。
* 应用在跳转时应传入指定entities: ['entity.system.browsable']为系统浏览器。
