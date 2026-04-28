---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-httpauthhandler
title: Class (HttpAuthHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (HttpAuthHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:92aa5406682bba2a5caa4912d8b1911a28915ce8cc046376686d6c38f6bd628a
---

Web组件返回的http auth认证请求确认或取消和使用缓存密码认证功能对象。示例代码参考[onHttpAuthRequest事件](arkts-basic-components-web-events.md#onhttpauthrequest9)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

HttpAuthHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## cancel9+

PhonePC/2in1TabletTVWearable

cancel(): void

通知Web组件用户取消HTTP认证操作。

**系统能力：** SystemCapability.Web.Webview.Core

## confirm9+

PhonePC/2in1TabletTVWearable

confirm(userName: string, password: string): boolean

使用用户名和密码进行HTTP认证操作。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userName | string | 是 | HTTP认证用户名。 |
| password | string | 是 | HTTP认证密码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 认证成功返回true，失败返回false。 |

## isHttpAuthInfoSaved9+

PhonePC/2in1TabletTVWearable

isHttpAuthInfoSaved(): boolean

通知Web组件用户使用服务器缓存的账号密码认证。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 存在密码认证成功返回true，其他返回false。 |
