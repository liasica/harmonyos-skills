---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-82
title: 在onInterceptRequest接口中，如何异步处理响应数据
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 在onInterceptRequest接口中，如何异步处理响应数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bdf7bee55e20aa2bcaa657ba41524d942a2d4d77590034cc2f5e770c4898faa3
---

可以使用[setResponseIsReady](../harmonyos-references/arkts-basic-components-web-webresourceresponse.md#setresponseisready9)设置资源响应数据是否已经就绪。例如，在异步获取数据后，需调用`setResponseIsReady(true)`通知系统响应数据已准备就绪，具体可参考[onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)示例代码。
