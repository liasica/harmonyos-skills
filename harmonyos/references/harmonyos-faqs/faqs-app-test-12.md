---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-12
title: 录制结束时提示录制失败，无录制文件生成
breadcrumb: FAQ > DevEco Studio > 应用测试 > 录制结束时提示录制失败，无录制文件生成
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c470b837cf81b1eb0acd0b2fec9ea583801ec50ae3d462ecb7dce5b30f7595a7
---

**可能原因**

录制能力依赖的uitest检测能力被其他程序占用。

**解决措施**

重启手机或使用命令以杀死该服务，命令如下：

```
1. hdc shell killall -9 uitest
```
