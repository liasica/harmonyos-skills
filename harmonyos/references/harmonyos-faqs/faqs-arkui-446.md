---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-446
title: pc上，bindPopup设置了showInSubWindow:true时，气泡无法再弹出菜单
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > pc上，bindPopup设置了showInSubWindow:true时，气泡无法再弹出菜单
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:56+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:445d11a5c5c5850220f3e542b8a7e537013521cf0f0c1f287e153a2a570cfc0a
---

**问题背景**

在PC端使用bindPopup组件时，当设置了showInSubWindow: true属性后，如果气泡内的组件再次绑定子窗口弹窗，会导致内层弹窗无法正常弹出，如何修改？

**解决措施**

在PC设备上，使用[bindMenu方法](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu)弹出的菜单默认会以子窗口形式显示。由于系统限制，子窗口类型的弹窗无法嵌套绑定同类型弹窗，因此当尝试在子窗口弹窗内再弹出子窗口菜单时，操作将不被支持。若需要弹出bindMenu，可设置bindMenu的参数[showInSubWindow](../harmonyos-references/ts-universal-attributes-menu.md#menuoptions10)为false。

**参考链接**

[bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)
