---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-overview
title: DataAbility组件概述
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > DataAbility组件开发指导 > DataAbility组件概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:49763de7bea8234198805e37cea5bf4bf0c698aff2e34c35b666c5a141bb121e
---

DataAbility，即"使用Data模板的Ability"，主要用于对外部提供统一的数据访问对象，不提供用户交互界面。DataAbility可由PageAbility、ServiceAbility或其他应用启动，即使用户切换到其他应用，DataAbility仍将在后台继续运行。

使用DataAbility有助于应用管理其自身和其他应用存储数据的访问，并提供与其他应用共享数据的方法。DataAbility既可用于同设备不同应用的数据共享，也支持跨设备不同应用的数据共享。

数据的存放形式多样，可以是数据库，也可以是磁盘上的文件。DataAbility对外提供对数据的增、删、改、查，以及打开文件等接口，这些接口的具体实现由开发者提供。
