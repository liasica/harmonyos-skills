---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-56
title: Native调试堆栈可视化功能并行栈视图显示空白
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试堆栈可视化功能并行栈视图显示空白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:cbcb71acce605f94b9241e7f7d9ab37f810785b01f9bf9c665e54cec12c53959
---

**问题现象**

使用Native调试堆栈可视化功能时，如果在任意两个页签之间来回切换，可能会遇到并行栈视图界面显示为空白的情况。

**解决措施**

导致该问题的原因可能是电脑GPU不兼容，或在云桌面的场景下使用DevEco Studio。

在DevEco Studio中**双击Shift**，在弹出的窗口中搜索**Registry**，**在Registry**页面中勾选**ide.browser.jcef.gpu.disable**项，关闭窗口并重启DevEco Studio即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/HBUvfqggTbeWKIT69hE-7Q/zh-cn_image_0000002624638710.png)
