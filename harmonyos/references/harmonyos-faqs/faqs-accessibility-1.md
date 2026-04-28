---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-accessibility-1
title: 聚焦输入框，拉起小艺键盘输入时会重复朗读，比如输入“1”，会读“1 1”
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 无障碍开发（Accessibility） > 聚焦输入框，拉起小艺键盘输入时会重复朗读，比如输入“1”，会读“1 1”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:33+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:bb073587835b562f4e1c89f66e1b51bd85fadf0caa8f9db2fdb41e47b91e743d
---

在开启屏幕朗读下，在触摸输入时，小艺键盘会发送主动播报事件给屏幕朗读应用，播报事件中对应内容，此时又收到编辑框（TextArea、TextInput、SearchField、RichEditor）文本变化事件，播报输入的上屏内容，从而出现了重复朗读键盘输入内容的现象。
