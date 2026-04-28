---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-36
title: 对于HAP包中引用的HSP包是否有数量限制
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 对于HAP包中引用的HSP包是否有数量限制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8c3c5376aaf1cf707e535105843d3a2d30a577e6840874270938e331b72904ce
---

目前没有明确的数量限制。

但是由于每个加载的[HSP](../harmonyos-guides/in-app-hsp.md)都需要占用一定的系统资源，过多的HSP包会对应用的性能造成影响。

如果应用中HSP包数量过多，建议使用单[HAP](../harmonyos-guides/hap-package.md)与多[HAR](../harmonyos-guides/har-package.md)方案，在动态加载场景中使用HSP。
