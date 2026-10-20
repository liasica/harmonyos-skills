---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0004
title: hdc命令发送本地文件至远端设备常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > hdc命令发送本地文件至远端设备常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:15+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:e621fae3c99fb8f2f3255905cba3cbe215c98b2d6cd5f635ef5b2d5a8e69f61c
---

**Q：如何用hdc命令将本地文件发送至远端设备？**

**A**：从本地向远端设备发送文件，命令格式如下：

```shell
hdc file send local remote
```

local 表示本地待发送的文件路径，remote 表示远程待接收的文件路径。

使用方法：

```shell
hdc file send E:\example.txt /data/local/tmp/example.txt
```

参考链接：[hdc-文件相关命令](../harmonyos-guides/hdc.md#文件传输)。
