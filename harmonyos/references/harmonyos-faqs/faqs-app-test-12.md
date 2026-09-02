---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-12
title: 录制结束时提示录制失败，无录制文件生成
breadcrumb: FAQ > DevEco Studio > 应用测试 > 录制结束时提示录制失败，无录制文件生成
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:1f98d01acaef596da0aece5bd33f07446c116fdc37c79a908c60d8a1e6bb67be
---

**可能原因**

录制能力依赖的uitest检测能力被其他程序占用。

**解决措施**

重启手机或使用命令以杀死该服务，命令如下：

```screen
hdc shell killall -9 uitest
```
