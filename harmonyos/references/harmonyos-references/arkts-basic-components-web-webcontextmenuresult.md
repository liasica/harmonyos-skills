---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuresult
title: Class (WebContextMenuResult)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebContextMenuResult)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94a887c532a827a8014903ed86d77c3b482850370ddafc817c26acd0eda3286e
---

实现长按页面元素或鼠标右键弹出来的菜单所执行的响应事件。示例代码参考[onContextMenuShow事件](arkts-basic-components-web-events.md#oncontextmenushow9)。

说明

* 该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

PhonePC/2in1TabletTVWearable

constructor()

WebContextMenuResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## closeContextMenu9+

PhonePC/2in1TabletTVWearable

closeContextMenu(): void

不执行WebContextMenuResult其他接口操作时，需要调用此接口关闭菜单。

**系统能力：** SystemCapability.Web.Webview.Core

## copyImage9+

PhonePC/2in1TabletTVWearable

copyImage(): void

当WebContextMenuParam包含图片内容时，用于复制该图片。

**系统能力：** SystemCapability.Web.Webview.Core

## copy9+

PhonePC/2in1TabletTVWearable

copy(): void

执行复制文本操作。

**系统能力：** SystemCapability.Web.Webview.Core

## paste9+

PhonePC/2in1TabletTVWearable

paste(): void

执行粘贴操作。

说明

需要配置权限：[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)。

**系统能力：** SystemCapability.Web.Webview.Core

## cut9+

PhonePC/2in1TabletTVWearable

cut(): void

执行剪切操作。

**系统能力：** SystemCapability.Web.Webview.Core

## selectAll9+

PhonePC/2in1TabletTVWearable

selectAll(): void

执行全选操作。

**系统能力：** SystemCapability.Web.Webview.Core

## undo20+

PhonePC/2in1TabletTVWearable

undo(): void

执行撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core

## redo20+

PhonePC/2in1TabletTVWearable

redo(): void

执行重做操作，即取消用户上一次的撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core

## pasteAndMatchStyle20+

PhonePC/2in1TabletTVWearable

pasteAndMatchStyle(): void

执行与此上下文菜单相关的粘贴操作，粘贴的内容会匹配目标格式，以纯文本形式呈现。

说明

需要配置权限：[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)。

**系统能力：** SystemCapability.Web.Webview.Core

## requestPasswordAutoFill23+

PhonePC/2in1TabletTVWearable

requestPasswordAutoFill(): void

请求密码保险箱中的用户名或密码数据自动填充到当前获得焦点的输入框中。

**系统能力：** SystemCapability.Web.Webview.Core
