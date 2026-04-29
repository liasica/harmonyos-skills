---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-56
title: Native调试堆栈可视化功能并行栈视图显示空白
breadcrumb: FAQ > DevEco Studio > 应用调试 > Native调试堆栈可视化功能并行栈视图显示空白
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b76a51eb85c57cdfabc2879149a3c09fcfca93b7e7eff83dfe54990a28147fe7
---

**问题现象**

使用Native调试堆栈可视化功能时，如果在任意两个页签之间来回切换，可能会遇到并行栈视图界面显示为空白的情况。

**解决措施**

导致该问题的原因可能是电脑GPU不兼容，或在云桌面的场景下使用DevEco Studio。

在DevEco Studio中**双击Shift**，在弹出的窗口中搜索**Registry**，**在Registry**页面中勾选**ide.browser.jcef.gpu.disable**项，关闭窗口并重启DevEco Studio即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/0aYQkKI3T2-aPouRJdcipw/zh-cn_image_0000002521308425.png?HW-CC-KV=V1&HW-CC-Date=20260429T062126Z&HW-CC-Expire=86400&HW-CC-Sign=889E3BC1CCD7E2363C9AD577F1D6B770BD8B1E358CB4BC2BEFCB2181C620BF24)
