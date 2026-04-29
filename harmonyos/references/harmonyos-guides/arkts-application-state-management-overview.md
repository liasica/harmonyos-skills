---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-application-state-management-overview
title: 管理应用拥有的状态概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理应用拥有的状态 > 管理应用拥有的状态概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4279d1d6380eb48c1d7d380779501ab5ac4a26c78087aa480783b83e86832185
---

在管理组件拥有的状态章节中介绍的装饰器仅能在页面内，即一个组件树上共享状态变量。如果开发者要实现应用级的，或者多个页面的状态数据共享，就需要用到应用级别的状态管理的概念。ArkTS根据不同特性，提供了多种应用状态管理的能力：

* [LocalStorage](arkts-localstorage.md)：页面级UI状态存储，通常用于[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)内、页面间的状态共享。
* [AppStorage](arkts-appstorage.md)：特殊的单例LocalStorage对象，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。
* [PersistentStorage](arkts-persiststorage.md)：持久化存储UI状态，通常和AppStorage配合使用，选择AppStorage存储的数据写入磁盘，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。
* [Environment](arkts-environment.md)：应用程序运行的设备的环境参数，环境参数会同步到AppStorage中，可以和AppStorage搭配使用。
