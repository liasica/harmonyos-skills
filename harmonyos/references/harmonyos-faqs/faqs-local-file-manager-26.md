---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-26
title: 从FilePicker返回的图片地址uri是不是只是在一定的时间内有访问权限
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 从FilePicker返回的图片地址uri是不是只是在一定的时间内有访问权限
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0ec478b192a66ae6bf6484abeecc1c8eb7ece34ab30ac29c360c83df6b47457f
---

重启应用后，URI失效是正常现象。系统通过Picker生成的URI具有临时访问权限，应用被终止后（包括重启）该权限将失效。因此，需要重新通过Picker选择来生成新的URI。
