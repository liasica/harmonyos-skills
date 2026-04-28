---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology
title: Ability Kit术语
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Ability Kit术语
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ab93ef0189506a8aab1bc4c9f3f925ee62995e7eadf6a2aea12d2301ec28aa0d
---

## A

### AbilityStage

[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)是一个[Module](application-package-overview.md#应用的多module设计机制)级别的组件管理器。

### ArkTS子进程

ArkTS子进程是指启动后系统默认创建ArkTS运行时环境的应用子进程。

### App Linking

App Linking是一种实现应用间跳转的技术，通过系统传入的uri信息（HTTPS链接）将用户引导至目标应用中的特定内容。无论目标应用是否已安装，用户都能够访问链接对应的内容。这种跳转方式相比Deep Linking增加了域名校验机制，可以避免应用被仿冒，更加安全。

## C

### CandidateMasterProcess（备选主控进程）

当应用存在多个进程时，系统会在应用启动时自动指定主控进程。如果开发者希望当前进程被选为主控进程，可以将其放入备选主控进程列表中，该列表中的进程即为备选主控进程。当现在的主控进程销毁后，系统会将位于链表首节点的备选主控进程设置为主控进程。

### Context

Context是Stage模型中的上下文基类，它封装了应用程序运行所需的基本环境和能力。作为框架与应用组件之间的核心桥梁，Context提供了访问所属应用的资源、获取应用信息、管理应用生命周期等通用接口。

在Stage模型中，Context作为基类，定义了所有上下文共有的基本能力。其具体子类（如ApplicationContext、AbilityStageContext、UIAbilityContext、ExtensionContext等）则在此基础之上，扩展了特定组件层级或运行场景的专属功能。例如，ApplicationContext作为应用上下文，提供了应用生命周期监听、进程管理、应用环境设置等应用级别的管控能力；而AbilityStageContext则是AbilityStage的上下文环境，提供获取AbilityStage对应的ModuleInfo对象、环境变化对象。

## D

### Deep Linking

Deep Linking是一种通过链接拉起指定应用的技术，其特点是支持开发者定义任意形式的scheme。然而，由于缺乏对域名的所有权验证机制，存在被其他应用仿冒的风险。这与采用标准HTTPS链接并强制进行域名验证以保障唯一性和安全的App Linking形成显著区别。

### 多实例模式

多实例模式是一种允许同一个应用组件（比如UIAbility）同时存在多个独立运行实例的启动模式。

## F

### FA模型

FA模型是早期的应用模型，为应用程序提供必备的组件与运行机制。在该模型中每个应用组件独享一个ArkTS引擎实例，适用于简单应用的开发。

## I

### InsightIntentProvider (意图提供方管理能力)

[意图提供方管理能力](../harmonyos-references/js-apis-app-ability-insightintentprovider.md)指通过声明标准意图或自定义意图，将业务功能接入意图框架的应用主体。

## K

### 跨端迁移

跨端迁移指在A端运行的UIAbility迁移到B端上，完成迁移后，B端UIAbility继续任务，而A端UIAbility可按需决定是否退出。

## M

### MasterProcess（主控进程）

当应用存在多个进程时，如果开发者需要将不同的Ability实例动态分配给指定进程，系统会在应用启动时自动指定一个进程来负责总体的协调分配工作，该进程即为主控进程。默认情况下，系统指定应用启动的第一个进程为主控进程。

开发者可以设置[onNewProcessRequest](../harmonyos-references/js-apis-app-ability-abilitystage.md#onnewprocessrequest11)的返回值，让主控进程通过接收该接口的回调信息，决定新的Ability实例运行在哪个进程中。

## N

### Native子进程

Native子进程是指启动后只有C/C++代码运行环境的应用子进程，针对这种类型的子进程系统默认不会创建ArkTS运行时环境。

## P

### PageAbility组件

PageAbility是FA模型下的包含UI、提供展示UI能力的应用组件，主要用于与用户交互。

## S

### Stage模型

Stage模型是当前系统主推的应用模型，为应用程序提供必备的组件与运行机制。该模型提供了AbilityStage组件管理器和WindowStage窗口管理器，分别作为应用组件与窗口的“舞台”，故得名"Stage模型"。

Stage模型支持多个应用组件共享同一个ArkTS引擎实例，以及应用组件间的状态共享与对象调用，可以降低内存开销、提升开发效率，适用于复杂应用的开发。

## U

### UIAbility

UIAbility是包含UI界面的应用组件，是系统调度的基本单元，为应用提供绘制界面的窗口。

### UIAbility生命周期

UIAbility生命周期是指一个UIAbility组件从创建到销毁的完整过程，在这个过程中系统会在特定时间点调用相应的回调函数。例如，应用首次创建UIAbility实例时，系统会调用onCreate()回调。

### UIAbility冷启动

当UIAbility实例处于完全关闭状态并被启动时，将发生冷启动。冷启动意味着系统需要完整地加载并初始化该UIAbility的所有代码和资源。随后，其生命周期回调将按顺序触发：依次是onCreate、onWindowStageCreate和onForeground。

### UIAbility热启动

UIAbility热启动发生在实例已启动并切换至后台后再次被启动时。由于实例无需完全重建，系统可快速恢复其原有状态，其生命周期会跳过初始创建阶段，直接触发onNewWant回调，随后UIAbility进入前台状态并触发onForeground回调。

## X

### 显式Want启动

显式Want启动是指在启动目标应用组件时，调用方传入的[want](../harmonyos-references/js-apis-app-ability-want.md)参数中指定了abilityName和bundleName，称为显式Want启动。

当有明确处理请求的对象时，显式Want启动是一种简单有效的启动目标应用组件的方式。

### 系统级so

系统提供的so，属于操作系统的一部分，随系统镜像发布。

## Y

### 隐式Want启动

隐式Want启动是指在启动目标应用组件时，调用方传入的[want](../harmonyos-references/js-apis-app-ability-want.md)参数中未指定abilityName，称为隐式Want启动。

当目标处理对象不明确时，可以使用隐式Want启动。它允许当前应用直接调用其他应用提供的某项能力，而无需关心该能力由哪个具体应用提供。

### 应用级so

应用开发者通过[Node-API](use-napi-process.md)方式自行开发的so，属于应用的一部分，随应用发布。
