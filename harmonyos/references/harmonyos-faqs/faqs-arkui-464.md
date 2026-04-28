---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-464
title: 半模态打开的页面被半模态覆盖了，怎么解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 半模态打开的页面被半模态覆盖了，怎么解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1fcec62ee215192a29208a231f43c1d2a7ce3b6d14b944b4e7b8abfebdc57274
---

**问题描述**

在路由框架使用NavPathStack+NavDestination的组合方案时。在页面A通过bindSheet打开了一个半模态窗口W，然后在窗口W里，点击按钮打开页面B，此时发现页面B在窗口W下面打开。希望新页面打开不要被半模态窗口覆盖住。

**解决措施**

半模态面板默认是在当前UIContext内顶层显示，在所有页面之上。可以通过设置半模态的[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)中[mode](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetmode12枚举说明)属性来实现打开的页面覆盖在半模态上方。
