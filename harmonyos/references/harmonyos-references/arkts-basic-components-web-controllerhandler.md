---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-controllerhandler
title: Class (ControllerHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (ControllerHandler)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99bab8fc78f8f2e83b0582556566c9af62ee3f740c5df4daa2deaf02642b6ba3
---

ControllerHandler是ArkWeb提供的处理新建Web组件控制器分配的帮助类。当Web页面通过window.open等方式请求创建新窗口，且Web组件已开启[multiWindowAccess](arkts-basic-components-web-attributes.md#multiwindowaccess9)能力时，系统通过[onWindowNew](arkts-basic-components-web-events.md#onwindownew9)事件将ControllerHandler对象提供给应用。开发者需调用其[setWebController](arkts-basic-components-web-controllerhandler.md#setwebcontroller9)方法为新窗口设置有效的[WebviewController](arkts-apis-webview-webviewcontroller.md)对象，将新窗口与页面中实际创建的Web组件关联；Web内核在等待setWebController调用期间会阻塞渲染进程，若应用决定不创建新窗口，必须调用setWebController(null)通知Web内核，否则渲染进程会持续阻塞。典型使用场景是在自定义弹窗、新页面或分屏中打开Web新窗口，并需要应用侧显式管理新窗口的URL展示与安全隔离。

**说明** 

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

constructor()

ControllerHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## setWebController9+

setWebController(controller: WebviewController): void

设置新创建Web组件的WebviewController对象；若应用决定不创建新窗口，必须设置为null通知Web内核，否则会造成渲染进程阻塞。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [WebviewController](arkts-apis-webview-webviewcontroller.md) | 是 | 新建Web组件的WebviewController对象，如果不需要打开新窗口请设置为null。 |
