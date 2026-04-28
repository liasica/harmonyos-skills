---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-utilities-uiviewer-1
title: 如何处理UIViewer获取页面时，无论如何操作切换设备界面，UIViewer展示的都是同一个界面
breadcrumb: FAQ > DevEco Testing > 实用工具 > UIViewer > 如何处理UIViewer获取页面时，无论如何操作切换设备界面，UIViewer展示的都是同一个界面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f4c34c74bc5248c1f4a1c34560124197f07232b6a25998aece1f37dfa9174ed7
---

打开cmd窗口，在设备上执行hdc指令删除该文件：

```
1. hdc shell rm -r /data/local/tmp/latestScreen.jpeg
```

重试设备投屏。如果获取页面仍然显示同一界面，请重启设备后再次尝试。
