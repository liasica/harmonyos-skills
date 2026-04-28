---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-40
title: 如何获取文件的扩展名
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何获取文件的扩展名
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:30+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:f4e7b4c9077b792da34d50c9f751c976aaaa6c0b60b3c17bfd8cacd99c7ac4f4
---

可以使用[fileIo.listFile](../harmonyos-references/js-apis-file-fs.md#fileiolistfile)接口获取文件夹目录下的文件列表，该接口的返回值为文件名称数组，通过获取到的文件名进行字符串的处理来获取文件的扩展名。例如，可通过字符串的lastIndexOf()方法定位最后一个点号位置，再用substring()截取扩展名部分。
