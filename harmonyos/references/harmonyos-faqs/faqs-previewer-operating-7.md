---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-7
title: DevEco无法执行Previewer，报错“This module is referencing one or more HSPs and cannot be previewed.”怎么处理
breadcrumb: FAQ > DevEco Studio > 界面预览 > DevEco无法执行Previewer，报错“This module is referencing one or more HSPs and cannot be previewed.”怎么处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4d7ed53d0379642ac5cd037d8bb91c6d748f8844e6fc7eeac28461629dca5b34
---

原因如下：

* 引入了HSP，DevEco Studio NEXT Developer Beta1版本不支持模块预览，请在HSP内直接预览。
* 项目中使用的方法API可能不在Previewer支持的列表里：[支持使用预览器的API清单](../harmonyos-guides/ide-previewer-api-list.md)，注意：支持列表会随版本更新变化，建议定期查看官方文档。

**解决措施**

可以在设备管理器中选择本地模拟器， 或者通过USB连接真机来运行。

**参考链接**

[使用模拟器运行应用](../harmonyos-guides/ide-run-emulator.md)
