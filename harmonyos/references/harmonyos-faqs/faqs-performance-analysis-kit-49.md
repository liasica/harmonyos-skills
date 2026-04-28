---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-49
title: 如何通过HDC命令截屏/获取相册
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过HDC命令截屏/获取相册
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:19+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:30c6cd1ba7cb6d866373f186f2fcdcba532e9f7eaec996a54434ba2e35e7d2d1
---

1. 截屏功能：

   ```
   1. hdc shell snapshot_display -f /data/local/tmp/test111.jpeg # -f表示指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径
   2. hdc file recv /data/local/tmp/test111.jpeg /data/local/tmp
   ```
2. 拉取系统相册：

   ```
   1. hdc file recv /storage/media/100/local/files/Photo # 拉取相册到命令执行时的目录
   ```
