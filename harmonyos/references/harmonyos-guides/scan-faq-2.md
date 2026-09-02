---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-2
title: 扫码直达跳转失败
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 扫码直达跳转失败
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1a5e60bfd91fbb400642687fe6b37314947735519a88ca14ae69eb7c30c1fbb4
---

**问题现象**

扫码直达跳转失败。

**解决措施**

请检查App Linking配置是否正确：

1. 检查开发者网站服务器配置是否正确。
2. 检查App Linking中网址域名关联是否正确。
3. 检查应用的module.json5文件中域名关联是否正确。
4. 检查应用的签名是否正确，参考[手动签名](ide-signing-manual.md)。

详情参考：App Linking的[FAQ](app-linking-startupapp.md#faq)。
