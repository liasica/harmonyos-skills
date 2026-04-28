---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-6
title: 组件被错误下线后，重新推送包时提示需等待24小时，如何解除该限制
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 组件被错误下线后，重新推送包时提示需等待24小时，如何解除该限制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7e6ca8bf64f44c74d8e26f15ea517b82edee323601d1fbf9522ee7c634466059
---

**问题描述**

版本上传时发现版本号错误，已下架并修正版本号。重新上传时提示在规定时间内禁止发布。请问能否恢复或告知规定时间是多久？

**解决方案**

修改ohpm-repo里面的配置文件。将重新上架等待小时数修改为如0.00x，然后执行ohpm install并重启ohpm-repo。但使用此方式时，重新上架的版本号需加1，具体可以参考[配置文件](../harmonyos-guides/ide-ohpm-repo-configuration.md)。
