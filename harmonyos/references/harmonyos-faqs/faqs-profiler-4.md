---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-4
title: 开启多线程开关后应用性能劣化
breadcrumb: FAQ > DevEco Studio > 性能分析 > 开启多线程开关后应用性能劣化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8ffc0aeca99c113f2e8bb85209f122e7c7776ebb76eab0ad951c6543ad1fdcf3
---

**问题现象**

在进行DevEco Testing稳定性压测后，性能测试显示性能下降。

**可能原因**

DevEco Testing稳定性压测会默认开启多线程开关。压测结束后，该开关可能会关闭失败。多线程开关用于方便定位多线程安全问题，开启后会对性能产生影响。

**解决措施**

手动关闭多线程开关，使用如下命令。

```
1. hdc shell param set persist.ark.properties 0x105c
2. hdc shell reboot
```
