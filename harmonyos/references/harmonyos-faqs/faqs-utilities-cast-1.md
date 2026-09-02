---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-1
title: 设备投屏时，投屏画面持续加载中如何处理
breadcrumb: FAQ > DevEco Testing > 实用工具 > 设备投屏 > 设备投屏时，投屏画面持续加载中如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:59c9b74ac7005a6dd88399004350c32a18acf0c752847d88c0d60d5f1f76a411
---

打开cmd窗口，在设备上执行hdc指令删除该文件：

```powershell
hdc shell rm -r /data/local/tmp/latestScreen.jpeg
```

重试设备投屏，如果获取页面仍失败，请重启设备后再次尝试。
