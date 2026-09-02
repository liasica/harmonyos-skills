---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-37
title: HAR如何转换为HSP
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAR如何转换为HSP
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:29+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:be5b06743d58e31d9456e2ee2ae026199613a281dc7812a15c28b46c7f47773c
---

[HAR](../harmonyos-guides/har-package.md)转为[HSP](../harmonyos-guides/in-app-hsp.md)主要是通过修改配置文件实现。具体步骤如下：

1. 在HAR的module.json5中，将type字段的值改为“shared”，并配置deliveryWithInstall字段为“true”。
2. 若HSP需要对外声明可跳转的页面，在module.json5文件中添加pages字段，并在“resources/base”目录下创建“profile/main\_pages.json”文件，配置“src”。
3. 将HAR的hvigorfile.ts文件中的“harTasks”更改为“hspTasks”。
4. HAR的build-profile.json5文件中默认生成consumerFiles字段，该项字段HAR可配置，为默认导出的[混淆加固](../harmonyos-guides/ide-build-obfuscation.md)规则，需要删除。

**配置更改后重新编译。**

**说明** 

部分组件和模块在HAP、HSP、HAR中集成使用时存在差异，例如[加载HAR中Worker线程文件相比HSP存在单独的使用约束](../harmonyos-guides/worker-introduction.md#文件路径注意事项)，因此按照以上步骤完成HSP转HAR后，请关注对应组件和模块介绍并进行适配。
