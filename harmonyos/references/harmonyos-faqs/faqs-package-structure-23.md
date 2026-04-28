---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-23
title: 从HAP的拆包中，如何区分是HAR和HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 从HAP的拆包中，如何区分是HAR和HSP
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6156098fc1b412b692dd186382e1e18d09d49f71fc069ca63bca6313358c3a44
---

HAP包拆包只能在module.json文件的dependencies字段看到引用的HSP模块名，看不到引用的HAR。HAR在编译时已打包在HAP包里，而HSP是单独成包的。.app文件安装时，HSP与HAP处于同一级别。

**参考链接**

[HAP](../harmonyos-guides/hap-package.md)、[HAR](../harmonyos-guides/har-package.md)、[HSP](../harmonyos-guides/in-app-hsp.md)
