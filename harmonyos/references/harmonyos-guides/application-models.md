---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-models
title: 应用模型
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用模型
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a8ffdc261a82325dc40d45c3dd5b76abe8dd4bb8ae844d1b2c39b4e02e729c97
---

## 应用模型的构成要素

应用模型是系统为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必备的组件和运行机制。有了应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。

应用模型的构成要素包括：

1. 应用组件

   应用组件是应用的基本组成单位和运行入口。

   在用户启动、使用和退出应用的过程中，应用组件会在不同的状态间切换，这些状态称为[应用组件的生命周期](uiability-lifecycle.md)。

   应用组件提供生命周期回调函数，开发者通过这些回调可以感知应用状态的变化。

   在开发应用时，开发者首先需要编写应用组件及其生命周期回调函数，并在应用配置文件中配置相关信息。操作系统在运行时通过配置文件创建应用组件实例，并调度其生命周期回调函数，从而执行开发者的代码。
2. 应用进程模型

   应用进程模型定义应用进程的创建和销毁方式，以及进程间的通信方式。
3. 应用线程模型

   应用线程模型定义应用进程内线程的创建和销毁方式、主线程和UI线程的创建方式、线程间的通信方式。
4. 应用任务管理模型（仅对系统应用开放）

   应用任务管理模型定义任务（Mission）的创建和销毁方式，以及任务与组件间的关系。

   任务是用户使用一个应用组件实例的记录。每次用户启动一个新的应用组件实例，都会生成一个新的任务。

   例如，用户启动一个视频应用，在"最近任务"界面可以看到视频应用这个任务。当用户点击这个任务时，系统会把该任务切换到前台。如果这个视频应用中的视频编辑功能也是通过应用组件编写的，在用户启动视频编辑功能时，会创建视频编辑的应用组件实例，在"最近任务"界面中将会展示视频应用、视频编辑两个任务。
5. 应用配置文件

   应用配置文件中包含应用配置信息、应用组件信息、权限信息、开发者自定义信息等，这些信息在编译构建、分发和运行阶段分别提供给编译工具、应用市场和操作系统使用。

## 应用模型概况

随着系统的演进发展，先后提供了两种应用模型：

* [FA（Feature Ability）模型](ability-terminology.md#fa模型)：从API 7开始支持的模型，已经不再主推。
* [Stage模型](ability-terminology.md#stage模型)：从API 9开始新增的模型，是目前主推且会长期演进的模型。在该模型中，由于提供了AbilityStage、WindowStage等类作为应用组件和Window窗口的“舞台”，因此称这种应用模型为Stage模型。

## 通过对比认识FA模型与Stage模型

**Stage模型与FA模型最大的区别在于**：Stage模型中，多个应用组件共享同一个ArkTS引擎实例；而FA模型中，每个应用组件独享一个ArkTS引擎实例。因此在Stage模型中，应用组件之间可以方便的共享对象和状态，同时减少复杂应用运行对内存的占用。Stage模型作为主推的应用模型，开发者通过它能够更加便利地开发出分布式场景下的复杂应用。

可通过如下对比表格了解两种模型的整体概况。

**表1** FA模型与Stage模型差异概览

| 项目 | FA模型 | Stage模型 |
| --- | --- | --- |
| **应用组件** | 1. 组件分类  - PageAbility组件：包含UI，提供展示UI的能力。详细介绍请参见[PageAbility组件概述](pageability-overview.md)。  - ServiceAbility组件：提供后台服务的能力，无UI。详细介绍请参见[ServiceAbility组件概述](serviceability-overview.md)。  - DataAbility组件：提供数据分享的能力，无UI。详细介绍请参见[DataAbility组件概述](dataability-overview.md)。  2. 开发方式  通过导出匿名对象、固定入口文件的方式指定应用组件。开发者无法进行派生，不利于扩展能力。 | 1. 组件分类  - UIAbility组件：包含UI，提供展示UI的能力，主要用于和用户交互。详细介绍请参见[UIAbility组件概述](uiability-overview.md)。  - ExtensionAbility组件：提供特定场景（如卡片、输入法）的扩展能力，满足更多的使用场景。详细介绍请参见[ExtensionAbility组件概述](extensionability-overview.md)。  2. 开发方式  采用面向对象的方式，将应用组件以类接口的形式开放给开发者，可以进行派生，利于扩展能力。 |
| **进程模型** | 有两类进程：  1. 主进程  2. 渲染进程  详细介绍请参见[进程模型](process-model-fa.md)。 | 包含主进程、ExtensionAbility进程、渲染进程等基本进程类型，以及其他进程类型。  详细介绍请参见[进程模型](process-model-stage.md)。 |
| **线程模型** | 1. ArkTS引擎实例的创建  一个进程可以运行多个应用组件实例，每个应用组件实例分别运行在单独的ArkTS引擎实例中。  2. 线程模型  每个ArkTS引擎实例都在一个单独线程（非主线程）上创建，主线程没有ArkTS引擎实例。  3. 进程内对象共享：不支持。  详细介绍请参见[线程模型](thread-model-fa.md)。 | 1. ArkTS引擎实例的创建  一个进程可以运行多个应用组件实例，所有应用组件实例共享一个ArkTS引擎实例。  2. 线程模型  ArkTS引擎实例在主线程上创建。  3. 进程内对象共享：支持。  详细介绍请参见[线程模型](thread-model-stage.md)。 |
| **应用配置文件** | 使用config.json描述应用信息、HAP信息和应用组件信息。  详细介绍请参见[应用配置文件概述（FA模型）](application-configuration-file-overview-fa.md)。 | 使用app.json5描述应用信息，module.json5描述HAP信息、应用组件信息。  详细介绍请参见[应用配置文件概述（Stage模型）](application-configuration-file-overview-stage.md)。 |
