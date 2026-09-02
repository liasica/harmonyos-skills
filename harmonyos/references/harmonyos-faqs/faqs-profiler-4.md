---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-4
title: 开启多线程开关后应用性能劣化
breadcrumb: FAQ > DevEco Studio > 性能分析 > 开启多线程开关后应用性能劣化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4c5febe417b94765c45a6792047a0179a0577f7c82de22f1446ff22029719955
---

**问题现象**

在进行DevEco Testing稳定性压测后，性能测试显示性能下降。

**可能原因**

DevEco Testing稳定性压测会默认开启多线程开关。压测结束后，该开关可能会关闭失败。多线程开关用于方便定位多线程安全问题，开启后会对性能产生影响。

**解决措施**

手动关闭多线程开关，使用如下命令。

```powershell
hdc shell param set persist.ark.properties 0x105c
hdc shell reboot
```
