---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fullscreenexithandler
title: Class (FullScreenExitHandler)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (FullScreenExitHandler)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a3a5f4e5b7723ca2b1b9d2b75dee3930f59b748dbe61d7ba94509a79f73b1f5c
---

FullScreenExitHandler 是 Web 组件提供的全屏退出处理类，用于响应网页退出全屏模式的事件。该类通过 exitFullScreen 方法通知开发者 Web 组件已退出全屏状态，帮助开发者及时处理全屏状态变化，调整应用界面布局或执行相应逻辑。示例代码参考[onFullScreenEnter](arkts-basic-components-web-events.md#onfullscreenenter9)。

**说明** 

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

constructor()

FullScreenExitHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## exitFullScreen9+

exitFullScreen(): void

通知开发者Web组件退出全屏。

**系统能力：** SystemCapability.Web.Webview.Core
