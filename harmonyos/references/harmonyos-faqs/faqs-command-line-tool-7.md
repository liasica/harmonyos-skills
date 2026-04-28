---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-7
title: ohpm私仓修改upload_max_times不生效
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm私仓修改upload_max_times不生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1b1b955bc4035206985b1067bc928b0a16c1b49aaa0501ab4ac920b8d8e78f8b
---

**问题描述**

默认值为100，修改为9999后仍存在100的限制。

**解决方案**

[2024-03-05T19:17:41.123] [INFO] default - "deploy\_root" environment variables: "OHPM\_REPO\_DEPLOY\_ROOT = C:\Users\uhamc\AppData\Roaming\Huawei\ohpm-repo". PS C:\Users\uhamc> ohpm-repo start

[2024-03-05T19:18:10.555] [INFO] default - config file path: "C:\Users\uhamc\AppData\Roaming\Huawei\ohpm-repo\conf\config.yaml".

ohpm-repo启动时会打印config地址。修改该config文件后，重启服务以使更改生效。

**参考链接**

[配置文件](../harmonyos-guides/ide-ohpm-repo-configuration.md)
