---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-19
title: HAP/HAR/HSP的关系是什么？是否都可以声明注册Ability和Page？三种类型分别推荐哪些的使用场景？选择原则是什么
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > HAP/HAR/HSP的关系是什么？是否都可以声明注册Ability和Page？三种类型分别推荐哪些的使用场景？选择原则是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7ed69f4c6c12d0712b8b87103abc91798bd60c34a983365300ec378c6afe3186
---

**HAP：应用安装和运行的基本单元**。支持在配置文件中声明abilities、extensionAbilities组件，支持在配置文件中声明pages页面。

主要使用场景：

* Entry：应用的主模块，用于实现应用的入口界面、入口图标、主特性功能等。
* Feature：应用的特性模块，用于实现应用的特性功能。

**HAR：静态共享包**。编译态复用，不支持在配置文件中声明abilities、extensionAbilities组件，不支持在配置文件中声明pages页面，支持Navigation组件导航。

主要使用场景：

* 作为二方库，发布到OHPM私仓，供公司内部其他应用依赖使用。
* 作为三方库，发布到OHPM中心仓，供其他应用依赖使用。

**HSP：动态共享包**。运行时复用，不支持在配置文件中声明abilities、extensionAbilities组件，支持在配置文件中声明pages页面。

主要使用场景：

* 多模块共用的代码、资源可以使用HSP，提高代码的可重用性和可维护性。
* 元服务分包预加载。

**参考链接**

[Stage模型应用程序包结构](../harmonyos-guides/application-package-structure-stage.md)
