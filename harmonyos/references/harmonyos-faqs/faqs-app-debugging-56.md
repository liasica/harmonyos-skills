---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-56
title: Native调试堆栈可视化功能并行栈视图显示空白
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试堆栈可视化功能并行栈视图显示空白
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2c13b3f8a38057ee0d1d446fca3152b059986638ce8c0baeedfd86eea900ddc6
---

**问题现象**

使用Native调试堆栈可视化功能时，如果在任意两个页签之间来回切换，可能会遇到并行栈视图界面显示为空白的情况。

**解决措施**

导致该问题的原因可能是电脑GPU不兼容，或在云桌面的场景下使用DevEco Studio。

在DevEco Studio中**双击Shift**，在弹出的窗口中搜索**Registry**，**在Registry**页面中勾选**ide.browser.jcef.gpu.disable**项，关闭窗口并重启DevEco Studio即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/0aYQkKI3T2-aPouRJdcipw/zh-cn_image_0000002521308425.png?HW-CC-KV=V1&HW-CC-Date=20260428T003010Z&HW-CC-Expire=86400&HW-CC-Sign=955EA0EBF9675F7A333BB2D55A22E7E019A3C0D327C3C5C8C9B0C57144E36490)
