---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-61
title: DevEco Device File Browser无法查看系统媒体文件目录
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > DevEco Device File Browser无法查看系统媒体文件目录
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dd7bc162b5a6c114a65be44b1da21f7992e32143172102a287c7a7ae08d952ac
---

**问题现象**

DevEco Device File Browser无法查看/storage/media/local/files/Photo 下的媒体文件，DevEco Studio上看不到图库相册里的文件，无法导出想要的媒体文件。

**可能原因**

由于安全原因，收紧了对系统媒体路径的访问权限。

解决措施

* 后续计划提供更加安全和开发者友好的访问目录方式。当前可使用mediatool命令行工具来进行文件导出。mediatool工具可以根据媒体文件在图库中的名字，对媒体文件进行导出。
* 详细使用指导请看：[mediatool工具](../harmonyos-guides/mediatool.md#mediatool工具)

**参考链接**

[媒体库资源访问工具](../harmonyos-guides/mediatool.md)
