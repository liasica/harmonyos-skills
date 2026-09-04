---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-startup-process
title: 应用启动流程
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用生命周期 > 应用启动 > 应用启动流程
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4baf3edda4808be94316f6db0d01f66c1cb5c4652bb883edbc3b3bec967811b0
---

## 概述

应用启动是指用户通过入口（如桌面图标、快捷方式等）触发系统拉起应用的过程。在应用模型中，一次典型的应用启动会依次经历**进程启动**、**AbilityStage启动**、**UIAbility启动**三个阶段，并在此过程中触发对应的生命周期回调。理解三者的关系与时序，有助于开发者在正确的时机完成初始化、资源申请与界面加载。

* **进程启动**：进程是系统进行资源分配的基本单位，详见[进程模型概述](process-model-overview.md)。当应用的首个进程创建时，意味着应用的启动。默认情况下，应用中（同一Bundle名称）的所有[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件运行在同一个独立进程（主进程）中。如果目标进程尚未创建，系统会先创建应用进程，并在进程内创建主线程进入消息循环；若进程已存在（如热启动场景），则直接复用已有进程。
* **AbilityStage启动**：[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md)是一个[Module](application-package-overview.md#应用的多module设计机制)级别的组件管理器，应用的[HAP](hap-package.md)在首次加载时会创建一个AbilityStage实例，每个HAP对应一个AbilityStage实例。在开始加载对应Module的第一个应用组件实例之前，系统会先创建AbilityStage，并在创建完成后执行其[onCreate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)生命周期回调，用于通知开发者可以对该Module进行初始化。
* **UIAbility启动**：[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)组件是一种包含UI的应用组件。三方应用必须包含至少一个UIAbility组件，否则没有界面对用户展示。UIAbility实例创建后，系统会依次触发[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)、[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)、[onForeground()](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)生命周期回调，完成UI加载并展示在前台。

进程、AbilityStage与UIAbility生命周期的关系如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/UcpKBY4lTC-3txMxw22AAA/zh-cn_image_0000002742002219.png)

| 阶段 | 触发时机 | 主要职责 |
| --- | --- | --- |
| 进程启动 | 应用首个进程创建时 | 分配系统资源、创建主线程、加载应用运行环境 |
| AbilityStage启动 | HAP首次加载、创建第一个应用组件实例前 | Module级初始化，如资源预加载、线程创建、启动框架任务执行 |
| UIAbility启动 | 创建UIAbility实例并展示 | 实例级初始化、UI加载、前后台资源申请与释放 |

## 启动阶段回调的使用建议

### Module级别初始化（AbilityStage.onCreate）

如[概述](application-startup-process.md#概述)所述，系统会先创建AbilityStage并执行其[onCreate()](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)回调。该回调在每个HAP的生命周期中仅触发一次，适合放置Module级别的初始化逻辑。

**建议在此回调中：**

* 执行该Module的资源预加载，如全局配置读取、基础数据预热。
* 注册[EnvironmentCallback](../harmonyos-references/js-apis-app-ability-environmentcallback.md)监听系统环境变量（语言、深浅色等）变化。
* 若已开启[应用启动框架AppStartup](app-startup.md)，自动模式下的启动任务会在AbilityStage构造过程中开始执行，开发者无需在此手动调用。

**不建议在此回调中：**

* 执行与特定UIAbility实例强相关的业务逻辑（应在UIAbility的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)中完成）。
* 执行大量耗时同步操作阻塞主线程，建议将耗时任务异步化或交由子线程处理。

### 指定实例模式路由（AbilityStage.onAcceptWant）

当[UIAbility指定实例模式（specified）](uiability-launch-type.md#specified启动模式)启动时，系统会触发AbilityStage的[onAcceptWant()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onacceptwant)回调，由开发者返回实例标识来决定复用已有UIAbility实例还是创建新实例。

**建议在此回调中：**

* 根据Want中的bundleName、abilityName、parameters等字段判断本次启动应匹配的实例标识。
* 返回稳定的字符串标识用于实例路由，例如基于文档ID、会话ID等业务维度生成。

**不建议在此回调中：**

* 执行与实例匹配无关的耗时业务逻辑。
* 返回空值或null忽略匹配，这会导致系统按默认行为创建新实例，失去specified模式的意义。

### UIAbility实例初始化（UIAbility.onCreate）

该回调在UIAbility实例的整个生命周期中仅触发一次，开发者可以在该回调中执行仅发生一次的启动逻辑。

**建议在此回调中：**

* 读取并解析启动参数[Want](../harmonyos-references/js-apis-app-ability-want.md)与[LaunchParam](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)，根据启动原因（如入口图标、Deep Linking、应用间跳转）分流业务。
* 执行该UIAbility实例级别的一次性初始化，如全局状态初始化、权限预检查、监听注册。

**不建议在此回调中：**

* 加载并渲染UI界面，UI加载应在[onWindowStageCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)中通过[loadContent()](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)完成。
* 申请仅在UI可见时才需要的资源（如定位、相机），这类资源应在[onForeground()](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)中申请、在[onBackground()](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)中释放。
* 执行耗时同步任务阻塞主线程，影响启动速度。

## 启动入口

应用的启动入口是指用户进入应用的途径（如桌面图标、快捷方式等）。不同入口在触发UIAbility启动时，系统传入的[Want](../harmonyos-references/js-apis-app-ability-want.md)参数（如action、uri、parameters）可能不同，开发者可在UIAbility的onCreate()或onNewWant()中据此区分来源并执行相应逻辑。

应用也可被其他应用通过[Want](want-overview.md)或[应用链接](app-uri-config.md)拉起，或被系统通过[意图框架](insight-intent-overview.md)调度启动。这类跨应用启动场景的详细说明请参见[应用间跳转](link-between-apps-overview.md)。

### 应用图标（桌面图标）

应用图标是应用最常见的启动入口，通常显示在系统桌面上。用户点击桌面图标后，系统会根据[module.json5配置文件](module-configuration-file.md)中声明的入口UIAbility（通常为entry类型HAP中startWindowIcon与label所对应的UIAbility）发起启动。

### 快捷方式

快捷方式是指长按应用图标弹出的快捷菜单项，允许用户直接跳转到应用的特定功能页面。开发者可以在[module.json5配置文件](module-configuration-file.md#shortcuts标签)的shortcuts标签中声明静态快捷方式，或通过[shortcutManager](../harmonyos-references/js-apis-shortcutmanager.md)接口动态发布快捷方式。

* 用户点击快捷方式后，系统会以携带特定parameters或uri的Want启动对应UIAbility。
* 开发者可在UIAbility的onCreate()或onNewWant()中解析Want参数，直接加载目标功能页，减少用户操作层级。

### 快捷栏启动

在PC/2in1、Tablet等设备上，用户可将应用固定到快捷栏，点击图标即可快速启动。

* 快捷栏启动应用的底层流程与桌面图标一致，仅入口位置不同。
* 若应用已存在前台或后台实例，点击快捷栏图标通常会将已有实例切到前台；是否创建新实例取决于UIAbility的[启动模式](uiability-launch-type.md)。
