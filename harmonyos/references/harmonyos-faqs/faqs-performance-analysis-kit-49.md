---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-49
title: 如何通过HDC命令截屏/获取相册
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过HDC命令截屏/获取相册
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:854a4b3d120d8ef795c690c20341b56e410bce20459aba047ebb3ef8092c6b78
---

1. 截屏功能：

   ```powershell
   hdc shell snapshot_display -f /data/local/tmp/test111.jpeg # -f表示指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径
   hdc file recv /data/local/tmp/test111.jpeg /data/local/tmp
   ```
2. 拉取系统相册：

   ```powershell
   hdc file recv /storage/media/100/local/files/Photo # 拉取相册到命令执行时的目录
   ```
