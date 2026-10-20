---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0007
title: HDC命令截屏与相册图片获取常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > HDC命令截屏与相册图片获取常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:15+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:936b7479282944682be4d00d1497d5a21bea58d9102dd7134e9577e9df1f5cb7
---

**Q：如何通过HDC命令截屏/获取相册？**

**A**：具体操作如下：

1. 截屏功能：

   ```shell
   hdc shell snapshot_display -f /data/local/tmp/test111.jpeg # -f表示指定图片在设备上的存储路径，如不指定，会在命令执行完成后显示图片默认存储路径
   hdc file recv /data/local/tmp/test111.jpeg /data/local/tmp
   ```
2. 拉取系统相册：

   ```shell
   hdc file recv /storage/media/100/local/files/Photo # 拉取相册到命令执行时的目录
   ```
