---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-5
title: 弹窗在平板横竖屏切换后不显示
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 弹窗在平板横竖屏切换后不显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:080aeb14b01c14782b151c9342045030a691ff89fdfd5138272404b7e60126ac
---

## 问题现象

应用弹窗无论在横屏下点击打开，旋转至竖屏显示，还是在竖屏下打开，旋转至横屏显示，弹窗都会消失不显示。

## 修改建议

目前子窗Popup在宿主窗口方式变化（平移、旋转）时，Popup会主动关闭。若期望在横竖屏旋转下依旧保留弹窗显示的场景，建议使用自定义弹窗实现，可参考[自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)官方文档。
