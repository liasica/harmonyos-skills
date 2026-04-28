---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-faq-2
title: 使用DocumentViewPicker拿到的uri通过openPreview打开显示预览失败
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > Preview Kit常见问题 > 使用DocumentViewPicker拿到的uri通过openPreview打开显示预览失败
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e5a2c5e061742cd3f8dd560f7101e6beb3b1f3f5c892dd9b686a2fb1f633770
---

DocumentViewPicker拿到的文件uri应用仅有临时权限，该权限无法分享给预览，导致预览失败。可先对uri[持久化权限](file-persistpermission.md)，然后再采用openPreview打开文件；或者可以先将文件拷贝至应用沙箱内，再预览沙箱内文件。
