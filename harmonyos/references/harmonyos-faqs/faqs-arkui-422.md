---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-422
title: Navigation如何在自定义组件之间传递NavPathStack实例
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation如何在自定义组件之间传递NavPathStack实例
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b30e61fd24ca5b8628f7ac759f359e6b5ac21aedc2397c1a913993580dbb6796
---

* 方式一：通过@Provide和@Consume装饰器，将NavPathStack实例传递给子页面。
* 方式二：子页面通过[OnReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)回调获取。
* 方式三：通过全局的AppStorage接口设置获取。
* 方式四：通过自定义组件查询接口获取，参考[queryNavigationInfo](../harmonyos-references/ts-custom-component-api.md#querynavigationinfo12)。
