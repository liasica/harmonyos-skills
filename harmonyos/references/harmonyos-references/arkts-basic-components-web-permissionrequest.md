---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-permissionrequest
title: Class (PermissionRequest)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (PermissionRequest)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:18+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:7975e4798aa738877b34659ef3ed2b0b78cddc473de3df739ba36932bd4c2c74
---

Web组件返回授权或拒绝权限功能的对象。示例代码参考[onPermissionRequest事件](arkts-basic-components-web-events.md#onpermissionrequest9)。

说明

* 该组件首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

PermissionRequest的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## deny9+

PhonePC/2in1TabletTVWearable

deny(): void

拒绝网页所请求的权限。

**系统能力：** SystemCapability.Web.Webview.Core

## getOrigin9+

PhonePC/2in1TabletTVWearable

getOrigin(): string

获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前请求权限网页的来源。 |

## getAccessibleResource9+

PhonePC/2in1TabletTVWearable

getAccessibleResource(): Array<string>

获取网页所请求的权限资源列表，资源列表类型参考[ProtectedResourceType](arkts-basic-components-web-e.md#protectedresourcetype9)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 网页所请求的权限资源列表。 |

## grant9+

PhonePC/2in1TabletTVWearable

grant(resources: Array<string>): void

对网页访问的给定权限进行授权。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resources | Array<string> | 是 | 授予网页请求的权限的资源列表。 |
