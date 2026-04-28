---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-172
title: 在容器组件嵌套的场景下，如何解决手势拖拽事件出现错乱的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 在容器组件嵌套的场景下，如何解决手势拖拽事件出现错乱的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:18cb8f78ae96d76f65dc9187847a54cbe172969facedbab04b797daed73fdf21
---

PanGesture用于触发拖动手势事件。滑动的最小距离distance默认为5vp，设置distance值为1可提高灵敏度，防止事件错乱。

**参考链接**

[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)
