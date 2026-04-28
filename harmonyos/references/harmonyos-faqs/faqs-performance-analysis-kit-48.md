---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-48
title: 如何在多设备情况下使用hdc
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何在多设备情况下使用hdc
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:99fc45a8e2368d1fe141fea28ad2b38dbadc654066e6354267a3afc02eb3d06b
---

**问题场景**

启动模拟器并连接真机，然后调用hdc命令获取udid。此时仅打印一条模拟器的udid。

**解决措施**

多设备环境下执行hdc shell会失败，需要指定设备执行hdc -t xx shell。否则，会报错。
