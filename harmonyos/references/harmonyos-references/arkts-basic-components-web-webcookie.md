---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcookie
title: Class (WebCookie)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebCookie)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ba7aee31d196421cb3e6e785c9de5bbbccad5f5af17a084f955584a397eb04ba
---

通过WebCookie可以控制Web组件中的cookie的各种行为，其中每个应用中的所有Web组件共享一个WebCookie。通过controller方法中的getCookieManager方法可以获取WebCookie对象，进行后续的cookie管理操作。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 从API version 8开始支持，从API version 23开始不再维护，建议使用[WebCookieManager](arkts-apis-webview-webcookiemanager.md)代替。
* 示例效果请以真机运行为准。

## constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor()

WebCookie的构造函数。

说明

从API version 8开始支持，从API version 23开始废弃。且不再提供新的接口作为替代。

**系统能力：** SystemCapability.Web.Webview.Core

## setCookie(deprecated)

PhonePC/2in1TabletTVWearable

setCookie()

设置cookie，该方法为同步方法。设置成功返回true，否则返回false。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[setCookie9+](arkts-apis-webview-webcookiemanager.md#setcookiedeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core

## saveCookie(deprecated)

PhonePC/2in1TabletTVWearable

saveCookie()

将当前存在内存中的cookie同步到磁盘中，该方法为同步方法。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[saveCookieAsync9+](arkts-apis-webview-webcookiemanager.md#savecookieasync)代替。

**系统能力：** SystemCapability.Web.Webview.Core
