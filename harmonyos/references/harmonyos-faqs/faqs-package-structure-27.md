---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-27
title: 如何实现在不使用UIAbility的情况下，能够模块化管理代码，并且各个模块之间可以相互路由跳转
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何实现在不使用UIAbility的情况下，能够模块化管理代码，并且各个模块之间可以相互路由跳转
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:36a60b03c0a7e32e786e43484068844ca42d4c4faeffdefc914f4f6178287ca2
---

采用HSP进行模块管理，可以实现页面间的跳转。无需导入包即可完成跳转，具体方式如下：

方式一：所有跳转到HSP内的页面需要使用特定格式：@bundle:包名（bundleName）/模块名（moduleName）/路径/页面所在的文件名（不加.ets后缀）。

方式二：正常entry内模块路由跳转：pages/页面所在的文件名（不加 .ets后缀）。

* 跳转到HSP页面使用方式一。
* HSP跳转到entry页面使用方式二。
* HSP跳转至HSP页面使用方式一。

**参考链接**

[HSP](../harmonyos-guides/in-app-hsp.md)
