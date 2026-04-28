---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-cast-1
title: 设备投屏时，投屏画面持续加载中如何处理
breadcrumb: FAQ > DevEco Testing > 实用工具 > 设备投屏 > 设备投屏时，投屏画面持续加载中如何处理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:946176edac1c5e0619006ab2446295eab15d058c35629f7d04d76a7ad4c10880
---

打开cmd窗口，在设备上执行hdc指令删除该文件：

```
1. hdc shell rm -r /data/local/tmp/latestScreen.jpeg
```

重试设备投屏，如果获取页面仍失败，请重启设备后再次尝试。
