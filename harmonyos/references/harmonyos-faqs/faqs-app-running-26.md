---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-26
title: 模拟器无法连接网络
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器无法连接网络
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6166806ce74031f08f955b17221ebd156216d00c6f748ae63c9c1f676850b995
---

**问题现象**

开发者在模拟器中开启WLAN选项并连接到VirtWifi后，仍无法访问网站。

**解决措施**

是否连接VirtWifi与模拟器能否访问互联网无关。VirtWifi仅用于在模拟器中判断WLAN的连接状态。模拟器访问网络实际上利用的是本地计算机的以太网或者WLAN，与本地计算机共享同一网络资源。如出现无法连接网络的情况，请开发者确认本地网络访问是否受到了限制（如使用公司内网）。如果对网络访问进行了限制，则需要在模拟器上配置网络代理。参见[网络代理](../harmonyos-guides/ide-emulator-more-features.md#section206461549731)。
