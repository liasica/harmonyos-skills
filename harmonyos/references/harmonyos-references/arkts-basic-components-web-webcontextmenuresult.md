---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuresult
title: Class (WebContextMenuResult)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS 组件 > Web > Class (WebContextMenuResult)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4c611d9e01b087e0158306b28b96a2a9f86bddce5a551addb1c836599918b397
---

WebContextMenuResult是ArkWeb组件中用于处理上下文菜单（长按页面元素或鼠标右键弹出菜单）事件的类。它为开发者提供了一系列菜单操作的执行能力，包括文本编辑操作（复制、粘贴、剪切、全选、撤销、重做、粘贴并匹配样式）、图片操作（复制图片、保存图片）、菜单控制（关闭菜单）以及密码自动填充功能。

开发者通常在需要自定义Web组件上下文菜单行为时使用WebContextMenuResult。通过onContextMenuShow事件回调获取WebContextMenuResult实例，结合WebContextMenuParam提供的菜单上下文信息，判断用户操作场景并调用相应的响应方法，从而实现自定义菜单交互逻辑。若开发者不执行任何菜单响应操作，则必须调用closeContextMenu方法关闭菜单。

示例代码参考[onContextMenuShow9+](arkts-basic-components-web-events.md#oncontextmenushow9)。

**说明** 

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class从API version 9开始支持。
* 示例效果请以真机运行为准。

## constructor9+

constructor()

WebContextMenuResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

## closeContextMenu9+

closeContextMenu(): void

不执行WebContextMenuResult其他接口操作时，需要调用此接口关闭菜单。

**调用说明：**

* 调用WebContextMenuResult的其他方法（如copy、paste、cut等）完成操作后，应调用此方法关闭菜单。
* 如果不再需要执行其他菜单操作，也应及时调用此方法关闭菜单。
* 未调用此方法可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## copyImage9+

copyImage(): void

当WebContextMenuParam包含图片内容时，用于复制该图片到剪贴板，从API version 24开始支持对canvas图片进行复制。若需保存图片到本地文件，应使用saveImage()方法。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## copy9+

copy(): void

执行复制文本操作。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## paste9+

paste(): void

执行粘贴操作，保留原始格式。若需粘贴纯文本并匹配目标格式，应使用pasteAndMatchStyle()方法。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

需要配置权限：[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)。

**系统能力：** SystemCapability.Web.Webview.Core

## cut9+

cut(): void

执行剪切操作。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## selectAll9+

selectAll(): void

执行全选操作。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## undo20+

undo(): void

执行撤销操作，撤销上一次的编辑操作。

**配合关系：**

* 与redo()方法配合使用，调用undo()后，可以通过redo()重新执行被撤销的操作。
* 如果用户未执行过撤销操作，则无法使用redo()方法。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## redo20+

redo(): void

执行重做操作，重新执行被撤销的操作。

**配合关系：**

* 与undo()方法配合使用，调用undo()后，可以通过redo()重新执行被撤销的操作。
* 如果用户未执行过撤销操作，则无法使用redo()方法。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## pasteAndMatchStyle20+

pasteAndMatchStyle(): void

执行与此上下文菜单相关的粘贴操作，粘贴的内容会匹配目标格式，以纯文本形式呈现。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

需要配置权限：[ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)。

**系统能力：** SystemCapability.Web.Webview.Core

## requestPasswordAutoFill23+

requestPasswordAutoFill(): void

请求密码保险箱中的用户名或密码数据自动填充到当前获得焦点的输入框中。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**系统能力：** SystemCapability.Web.Webview.Core

## saveImage24+

saveImage(): void

保存上下文菜单相关的图片，调用后将触发下载流程。

**说明** 

完成操作后，应调用[closeContextMenu](arkts-basic-components-web-webcontextmenuresult.md#closecontextmenu9)关闭菜单，未调用可能导致菜单资源未正确释放。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core
