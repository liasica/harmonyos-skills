---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-17
title: 如何用hdc命令将本地文件发送至远端设备
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何用hdc命令将本地文件发送至远端设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:2ef7a23dc8862cfdffa135598dd24f0f161f1239b377de9dd87b7a7af5166ab3
---

从本地向远端设备发送文件，命令格式如下：

```powershell
hdc file send local remote
```

local 表示本地待发送的文件路径，remote 表示远程待接收的文件路径。

使用方法：

```powershell
hdc file send E:\example.txt /data/local/tmp/example.txt
```

**参考链接**

[hdc-文件相关命令](../harmonyos-guides/hdc.md#文件传输)
