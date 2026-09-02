---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-48
title: 如何在多设备情况下使用hdc
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何在多设备情况下使用hdc
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:696b2bafa6a6389b0821967e5699948e38bae99b06e83f7cd713150d3fd190fa
---

**问题场景**

启动模拟器并连接真机，然后调用hdc命令获取udid。此时仅打印一条模拟器的udid。

**解决措施**

在多设备环境下直接执行hdc shell会失败，需要使用hdc -t [connect-key] shell指定设备进行操作。其中，connect-key为每个设备的唯一标识符，可通过执行hdc list targets命令获取。

参考链接

[查询设备列表](../harmonyos-guides/hdc.md#查询设备列表)

[连接指定的目标设备](../harmonyos-guides/hdc.md#连接指定的目标设备)
