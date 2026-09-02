---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult
title: Class (JsResult)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (JsResult)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d2338af0698246815b59166d2f0a7574d650d0074c8930aaabf05969ab40f218
---

JsResult是Web组件在处理JavaScript弹窗事件时返回的结果处理对象，适用于开发者拦截并自定义处理window.alert、window.confirm、window.prompt等弹窗场景。开发者可在[onAlert](arkts-basic-components-web-events.md#onalert)、[onConfirm](arkts-basic-components-web-events.md#onconfirm)或[onPrompt](arkts-basic-components-web-events.md#onprompt9)等事件回调中，通过该对象向Web组件反馈用户的确认、取消或输入内容等操作结果，从而控制弹窗的后续行为。

**说明** 

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor

constructor()

JsResult的构造函数。用于处理JavaScript弹窗事件。

**系统能力：** SystemCapability.Web.Webview.Core

## handleCancel

handleCancel(): void

通知Web组件用户取消弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

## handleConfirm

handleConfirm(): void

通知Web组件用户确认弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

## handlePromptConfirm9+

handlePromptConfirm(result: string): void

通知Web组件用户确认弹窗操作并传递对话框内容。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | string | 是 | 用户输入的对话框内容。 |
