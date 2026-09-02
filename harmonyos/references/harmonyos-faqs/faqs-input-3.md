---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-input-3
title: 如何设置鼠标指针样式和光标大小
breadcrumb: FAQ > 系统开发 > 基础功能 > 多模输入（Input） > 如何设置鼠标指针样式和光标大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ce871ef49eb8fbee19e440607ebdad73229ceb8c9faf4e968f460c8f3109529e
---

## 问题现象

如何修改鼠标指针的样式（例如更改为手形指针）以及调整鼠标光标的大小？

## 解决方案

通过[pointer.setPointerStyle](../harmonyos-references/js-apis-pointer.md#pointersetpointerstyle)设置鼠标样式类型为手形指针，另外模拟器没有鼠标，使用的是系统的鼠标，即[模拟器上不支持此能力](../harmonyos-guides/ide-emulator-specification.md)。

使用pointer.setCustomCursor设置指定窗口的自定义光标样式，可通过修改自定义光标资源CustomCursor的pixelMap修改光标大小，例如修改[setCustomCursor](../harmonyos-references/js-apis-pointer.md#pointersetcustomcursor15)示例代码中的desiredSize可改变光标大小。
