---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-controllerhandler
title: Class (ControllerHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (ControllerHandler)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:12621c679f3c55ec3cf72d032cd9a54aad82672740462e8b087615c1e7eb4868
---

设置用户新建Web组件的WebviewController对象。示例代码参考[onWindowNew事件](arkts-basic-components-web-events.md#onwindownew9)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

ControllerHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## setWebController9+

PhonePC/2in1TabletTVWearable

setWebController(controller: WebviewController): void

设置WebviewController对象，如果不需要打开新窗口请设置为null。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [WebviewController](arkts-apis-webview-webviewcontroller.md) | 是 | 新建Web组件的WebviewController对象，如果不需要打开新窗口请设置为null。 |
