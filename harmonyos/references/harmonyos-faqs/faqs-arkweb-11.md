---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-11
title: WebView中，双向交互可以使用JSBridge技术，也可以使用端口通信技术，这两者有什么区别
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > WebView中，双向交互可以使用JSBridge技术，也可以使用端口通信技术，这两者有什么区别
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c66076a2a88ca7c216c5224257be59347e7ecd7708a85944a570eea1631fdb67
---

**场景描述**

1. 通过WebMessagePort可以进行消息的发送以及接收。
2. 通过runJavaScript、registerJavaScriptProxy的JSBridge技术也能实现消息的收发。

这两者的主要区别在于数据量的传递规格和适用场景。选择方案时，需要根据具体需求来决定：

**解决措施**

JSBridge是一种JavaScript与Web客户端之间的通信机制。通过JSBridge，可以在WebView中调用客户端提供的功能，也可以从客户端调用JavaScript函数。对于复杂的通信需求，可以使用端口通信技术实现更灵活的跨平台通信。

* 使用runJavaScript与registerJavaScriptProxy的JSBridge技术：
  + 特点：调用函数，不需要一直保持通道。
  + 使用场景：对于函数调用的场景，可以选择runJavaScript或者registerJavaScriptProxy实现。
* 使用WebMessagePort建立端口通信：
  + 特点：建立通道，实时监听，持续消耗资源。
  + 使用场景：对于需要双向通信、数据实时更新、聊天应用以及传输大文件（如图片）等场景，建议选择端口通信技术，以确保更稳定的通信。

**参考链接**

[应用侧调用前端页面函数](../harmonyos-guides/web-in-app-frontend-page-function-invoking.md)

[前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)

[建立应用侧与前端页面数据通道](../harmonyos-guides/web-app-page-data-channel.md)
