---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-37
title: HAR如何转换为HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAR如何转换为HSP
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5d6998d742f00f44b14d3c43dc3d26881fa99358848ac96fe4582d7a35b85c09
---

[HAR](../harmonyos-guides/har-package.md)转为[HSP](../harmonyos-guides/in-app-hsp.md)主要是通过修改配置文件实现。具体步骤如下：

1. 在HAR的module.json5中，将type字段的值改为“shared”，并配置deliveryWithInstall字段为“true”。
2. 若HSP需要对外声明可跳转的页面，在module.json5文件中添加pages字段，并在“resources/base”目录下创建“profile/main\_pages.json”文件，配置“src”。
3. 将HAR的hvigorfile.ts文件中的“harTasks”更改为“hspTasks”。
4. HAR的build-profile.json5文件中默认生成consumerFiles字段，该项字段HAR可配置，为默认导出的[混淆加固](../harmonyos-guides/ide-build-obfuscation.md)规则，需要删除。

配置更改后重新编译。
