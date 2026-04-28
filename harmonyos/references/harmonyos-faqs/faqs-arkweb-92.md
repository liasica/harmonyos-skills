---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-92
title: ArkWeb如何适配多种设备
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > ArkWeb如何适配多种设备
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e987967f9d22cc15c0b273ea6714f8d15b5c92e4cae6c700527673114fb32a09
---

在进行Web页面开发时，可以采用CSS中的媒体查询，使用 @media 查询根据不同的屏幕尺寸设置不同的样式。此外，参考响应式设计(Responsive Web Design, RWD)的相关知识，如使用百分比单位和视口单位。同时，可以使用成熟的前端框架，这些框架中的组件实现内容已经考虑了多端适配场景。详情可参考[Web响应式布局](../best-practices/bpta-web-adaptation.md)。

如果三方网页已经使用UA标识适配了移动端设备，但在HarmonyOS设备上效果错误，可能的原因是没有适配HarmonyOS设备的UA标识。开发者可以在ArkTS侧使用[getUserAgent()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getuseragent)来查看HarmonyOS设备的UA标识，从而进行补充适配。另外，开发者也可以使用[setCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)自定义UA标识。

参考链接：

[默认UserAgent结构](../harmonyos-guides/web-default-useragent.md#默认user-agent结构)

[setCustomUserAgent](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setcustomuseragent10)
