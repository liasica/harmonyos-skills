---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult
title: Class (JsResult)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (JsResult)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3b6b6fa28470ac735b03cda07126428c0b9610b2f34c13eda18a2f2f971bc067
---

Web组件返回的弹窗确认或弹窗取消功能对象。示例代码参考[onAlert事件](arkts-basic-components-web-events.md#onalert)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 8开始支持。
* 示例效果请以真机运行为准。

## constructor

PhonePC/2in1TabletTVWearable

constructor()

JsResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## handleCancel

PhonePC/2in1TabletTVWearable

handleCancel(): void

通知Web组件用户取消弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

## handleConfirm

PhonePC/2in1TabletTVWearable

handleConfirm(): void

通知Web组件用户确认弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

## handlePromptConfirm9+

PhonePC/2in1TabletTVWearable

handlePromptConfirm(result: string): void

通知Web组件用户确认弹窗操作及对话框内容。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | string | 是 | 用户输入的对话框内容。 |
