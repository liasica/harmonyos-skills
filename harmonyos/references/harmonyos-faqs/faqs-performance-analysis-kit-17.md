---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-17
title: 如何用hdc命令将本地文件发送至远端设备
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何用hdc命令将本地文件发送至远端设备
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:10c9491f75483f1743454ddf1689349fc5bf7eb1e002715507d77a58e904f0f0
---

从本地向远端设备发送文件，命令格式如下：

```
1. hdc file send local remote
```

local 表示本地待发送的文件路径，remote 表示远程待接收的文件路径。

使用方法：

```
1. hdc file send E:\example.txt /data/local/tmp/example.txt
```

**参考链接**

[hdc-文件相关命令](../harmonyos-guides/hdc.md#文件传输)
