---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-453
title: 全屏模态转场和半模态转场中是否可以实现避让软键盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 全屏模态转场和半模态转场中是否可以实现避让软键盘
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ea13097d22457d15a3e9ec8cd1045989ff6d25ccf452e47a02a167a72fbcbaa3
---

全屏模态转场不支持软键盘避让功能，半模态可以通过设置keyboardAvoidMode属性来实现软键盘的避让，由于全屏模态转场会占据整个屏幕空间，系统默认不处理软键盘避让；而半模态转场可通过keyboardAvoidMode属性动态调整布局位置，可参考：[SheetKeyboardAvoidMode枚举说明](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetkeyboardavoidmode13枚举说明)。
