---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hyperstartup-application
title: 应用快启
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用生命周期 > 应用启动 > 应用快启
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:10+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:72bbabe2aef6210b93ae9235ddce038fb1e76ca1a133b7201abbdbffb37c1a81
---

## 概述

随着应用功能不断丰富，启动阶段往往需要完成进程创建、运行时初始化、模块加载、资源解析、首屏构建等一系列操作。当冷启动链路较长或启动阶段资源、模块加载占比较高时，将导致用户在首屏等待时间变长，进而影响应用体验和留存表现。

从API version 24开始，系统提供应用快启机制。该机制通过提前完成启动阶段中可复用流程的初始化工作，在用户再次启动应用时，复用相关启动初始化结果，减少重复初始化和加载开销，缩短启动链路耗时，有助于提升应用启动速度和稳定性。

应用快启机制的特点：

* **系统级启动加速**：通过复用启动初始化结果，减少冷启动阶段的重复执行流程，显著提升启动性能。
* **用户无感体验提升**：用户无须额外操作即可获得应用启动体验提升。
* **面向启动瓶颈优化**：特别适用于冷启动耗时较高、资源加载或模块加载占比较大的应用场景。

开发者可以从以下维度判断应用是否适合接入快启能力：

* 应用冷启动性能较差，启动时延高于1.6s。
* 资源加载、模块加载在启动过程中的耗时占比超过25%。

## 基本概念

* 应用快启：系统提供的启动加速能力。应用接入后，系统会在适当时机提前完成部分启动初始化工作，并在后续启动时复用相关初始化结果，减少重复执行的启动流程。
* 快启初始化：系统为应用快启提前完成初始化工作的过程。该过程只适合执行可复用、无外部状态依赖、不会影响数据一致性的启动逻辑。设备已解锁时，用户执行灭屏或锁屏操作后，系统开始快启初始化，并在后续完成该初始化流程。
* 快启初始化结果：快启初始化完成后形成的可复用启动结果。应用、系统或运行环境发生变化时，系统可能清理已有初始化结果，并在满足条件后重新进行快启初始化。
* 快启初始化结果清理：应用卸载、应用安装、应用更新、系统重启以及部分系统环境变量发生变化时，系统会清理已有快启初始化结果。清理后，应用后续需在满足条件时重新进行快启初始化。
* 快启点：启动流程中的一个时序分界点。快启点前的启动流程会被纳入快启优化范围，应用快启时会跳过这些流程；快启点后的启动流程不受影响，普通启动和快启都会继续执行。
* 快启启动：应用通过快启机制复用部分启动初始化结果，从而加速下一次启动。快启只影响快启点前的流程，快启点后的业务仍按正常启动时序执行。
* 快启风险操作：不适合在快启初始化过程中执行的操作，例如依赖磁盘数据实时读取、注册需要持续响应的事件监听、建立长时网络连接、执行有状态的进程间通信等。此类操作需要后置到快启点之外，或在快启后的回调中重新同步。

## 约束限制

* 当前仅支持手机设备。
* 在开发者模式下，使用debug签名的应用不受系统侧管控限制，开发者可自主进行快启特性的接入、调试与本地测试。
* 系统对”快启启动”功能进行了权限管控。线上使能特性需要开发者先提交”快启启动”申请。该权限仅面向企业开发者开放。
  1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
  2. 在项目列表选择项目，并在应用列表下选择需要申请“应用快启”功能的应用。
  3. 进入“项目设置 > 开放能力管理”页面，点击“应用快启”对应的“申请”。
* 应用配置快启后，实际是否进行快启以及具体的快启时机，均由系统根据用户习惯等信息来综合决定。开发者无法对此进行干预。

## 实现原理

快启技术会提前完成启动流程中可复用部分的初始化工作。应用启动时，可复用相关初始化结果，从而跳过这部分启动流程，达到启动加速的目标。如下图所示，快启相较于普通启动可跳过启动过程中的部分阶段，从而减少启动时延：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/BpsM1lfFTbyrIkhar3tdHA/zh-cn_image_0000002706673092.png)

**包含在快启点内的流程有**：AbilityStage模块加载、[AbilityStage.onCreate](../harmonyos-references/js-apis-app-ability-abilitystage.md#oncreate)和UIAbility模块加载。其中，在[模块加载](arkts-module-side-effects.md)过程中将执行部分代码，包括顶层代码（top level）、so的constructor和类静态变量初始化等。

## 快启适配

### 快启风险操作

快启会跳过部分启动流程。为了保证数据一致性和状态正确，开发者需要消除快启初始化流程中的风险操作，才能保障快启后应用数据的正确性。

风险操作的实例如下：

* 磁盘数据访问

  快启初始化过程中发生的磁盘数据读取操作，不会在快启中执行，因此会导致数据不一致问题。

  示例：快启初始化过程中，应用业务读取存储在数据库中的字体属性（宋体）。应用快启后，用户将字体调整为楷体，该属性被持久化到数据库文件，随后应用退出；下次应用快启时，由于没有再次读取数据库（该流程已被跳过），导致字体仍为宋体，而不是更新后的楷体。
* 事件监听回调注册

  快启初始化过程中建立的回调事件监听，不会在快启前持续响应，可能导致事件丢失。

  示例：快启初始化过程中，应用业务注册了颜色模式监听，初始为深色模式；在应用未被用户启动的情况下，系统颜色模式发生变化，切换为浅色模式。由于该监听不会在快启前持续响应，因此无法接收到切换颜色模式的广播消息。下次用户通过快启方式启动应用时，应用仍会显示为深色模式。
* 网络访问

  快启初始化中建立的网络连接不可控，可能出现连接中断等问题。

  示例：快启初始化中，建立了长时TCP连接以接收云端信息；快启初始化完成后，该连接不会持续响应，超时导致连接失败。
* 进程间通信（IPC）

  快启初始化中，禁止有状态的进程间通信，例如保存应用状态和数据持久化（允许参数获取等无状态的进程间通信），否则会触发保护机制导致快启初始化失败。

### 将快启风险操作后置到快启点之外

系统为开发者提供了新的回调接口[onAboutToCreateAbility()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onabouttocreateability24)。该接口在AbilityStage.onCreate()执行完毕后触发，但不参与快启初始化过程。无论是否开启应用快启功能，该回调均会被调用。

**示例1：** AbilityStage.onCreate中存在快启风险操作。

```typescript
export class AppAbilityStage extends AbilityStage {
    onCreate() {
        this.readFile();
    }
    readFile() {
        // 从磁盘读取文件
    }
}
```

建议：

1. 将快启风险操作后置到AbilityStage.onAboutToCreateAbility。

   ```typescript
   export class AppAbilityStage extends AbilityStage {
       onAboutToCreateAbility() {
           this.readFile();
       }
   }
   ```
2. 调整业务逻辑时，需要考虑时序依赖，保障业务逻辑正确性。
3. AbilityStage.onCreate()是首个包含较多业务逻辑的生命周期回调。若该回调中的业务不易拆分，建议开发者在首次适配时，将AbilityStage.onCreate()的内容整体移至[onAboutToCreateAbility()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onabouttocreateability24)。后续可通过业务前移扩大收益。

**示例2：** 顶层代码中存在快启风险操作。

以下示例在顶层代码中实例化类，并最终导致文件访问：

```typescript
class ClassA {
    constructor() {
        this.readFile();
    }

    readFile() {
        // 从磁盘读取文件
    }
}

let tmp = new ClassA();
```

建议：

1. 顶层代码会随import该模块而执行，所以在时序上顶层代码与首个调用者绑定，属于隐式且不可控的调用，修改时容易造成调用时序混乱，所以建议在非顶层代码中实现业务逻辑。
2. 具体到快启特性，系统要求应用模块不可以在顶层代码执行快启风险操作，而是要根据业务逻辑调整到生命周期回调中执行。

**示例3：** C++的构造函数中存在快启风险操作。

```typescript
static napi_module OpenPlatformModule = {
    .nm_version = 1,
    .nm_flags = 100,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "openplatform",
    .nm_priv = ((void *)0),
    .reserved = {0}
};

void read_file() {
    // 从磁盘读取文件
}

extern "C" __attribute__((constructor)) void RegisterOpenPlatformModule(void) {
    napi_module_register(&OpenPlatformModule);
    read_file();
}
```

建议：

1. 逐一检查启动过程中加载的so。constructor中不存在快启风险操作的so在AbilityStage.onCreate中进行dlopen，以扩大快启收益。
2. 存在风险操作constructor的so，需要放到UIAbility等快启点之外的生命周期中调用。

**示例4：** 类静态变量初始化中存在快启风险操作。

以下示例中存在两类静态初始化：一是静态变量初始化，会读取文件；二是静态代码块执行，会进行网络访问。

```typescript
export class AppAbilityStage extends AbilityStage {
    private a = 1;
    static data = AppAbilityStage.readFile();
    static {
        AppAbilityStage.netAccess();
    }
    static readFile() {
        // 从磁盘读取文件
    }
    static netAccess() {
        // 网络访问
    }
}
```

建议：根据业务逻辑进行调整，将快启风险操作移出快启点。

### 在更新回调接口中更新数据

考虑到实际调整业务逻辑的困难，部分对外数据交互难以剥离。快启机制为开发者提供新的回调接口[onLaunchFromHyperSnap()](../harmonyos-references/js-apis-app-ability-abilitystage.md#onlaunchfromhypersnap24)，该回调接口仅在快启流程（而不是快启初始化流程）中执行，正常冷启动不执行该回调。开发者可以在该回调接口中重新请求外部数据进行同步，保证数据一致性。

```typescript
export class AppAbilityStage extends AbilityStage {
    onCreate() {
        this.initLanguage(language);
    }
    initLanguage(language) {
        readFile(); // AbilityStage.onCreate中存在快启风险操作
    }
    readFile() {
        // 从磁盘读取文件
    }
}
```

```typescript
export class AppAbilityStage extends AbilityStage {
    onLaunchFromHyperSnap() {
        this.updateLanguage(); // 在onLaunchFromHyperSnap中进行更新
    }
    updateLanguage() {
        readFile();
    }
}
```

## 通过应用侧云推开关开启或关闭快启功能

云推开关是一种通过云端在线配置、动态开启或关闭应用特定功能的机制。

借助[setHyperSnapEnabled()](../harmonyos-references/js-apis-app-ability-hypersnapmanager.md#hypersnapmanagersethypersnapenabled)，应用可以根据需要关闭快启功能，直至云推开关重新开启。

云推开关的基本规格：

* setHyperSnapEnabled配置值默认为关闭（false）。
* setHyperSnapEnabled设置的配置值会被持久化，设备重启仍有效。
* 应用更新和应用安装会重置为默认值。

云推开关使用示例：

* 应用安装完成后，首次启动时主动拉取云端配置，并调用setHyperSnapEnabled(true)进行设置。
* 应用监控云端配置变化，云端主动推送新配置（注：与云端交互的逻辑需要在快启点之后执行，避免在快启点内进行网络交互，同时防止快启跳过该业务逻辑的执行）。
* 云端推送获取设置的同时，需在应用本地保存一份配置（例如存储到数据库）。
* 快启点内，AbilityStage.onCreate中读取本地配置，并重新调用接口。

通过上述实现，可保障应用更新后继续使用快启特性。

```typescript
export class LauncherAbility extends UIAbility {
    onCreate() {
        // ...
    }

    onConfigChange(key: string, value: string) {
        if (key == "enable_hyper_snap") {
            if (value == "true") {
                setHyperSnapEnabled(true);
            } else {
                setHyperSnapEnabled(false);
            }
        }
    }
}

export class AppAbilityStage extends AbilityStage {
    onCreate() {
        const hyperSnapConfig = this.readConfigFromDB();
        if (hyperSnapConfig === "true") {
            setHyperSnapEnabled(true);
        } else {
            setHyperSnapEnabled(false);
        }
    }

    readConfigFromDB() {
        // 从数据库读取setHyperSnapEnabled参数
    }
}
```

## 通过应用主动重置快启初始化结果

系统对外提供了[requestRebuildHyperSnap()](../harmonyos-references/js-apis-app-ability-hypersnapmanager.md#hypersnapmanagerrequestrebuildhypersnap)接口，该接口支持应用在自己的业务逻辑中主动调用，清理当前快启初始化结果，在满足条件时重新进行快启初始化。

```typescript
export class LauncherAbility extends UIAbility {
    onCreate() {
        // ...
        try {
            // ...
        } catch (error) {
            // ...
            requestRebuildHyperSnap(); // 开发者可根据业务在报错时重新生成快启初始化结果
            // ...
        }
    }
}
```

## 通过调整业务逻辑提升快启加速收益

纳入快启点的启动逻辑越多，快启收益通常越明显。开发者可以对整个启动流程进行梳理和分析，将适合纳入快启点的启动逻辑（即不含[快启风险操作](hyperstartup-application.md#快启风险操作)），在保障业务逻辑正确性的条件下前置到快启点内，扩大应用快启技术提升启动性能的收益。

* **将启动过程中的时序无关且无快启风险操作的逻辑前置到快启点内**

  如果存在可前置且无时序依赖的任务，建议评估是否将其放到快启点内以扩大收益。同时，需要确保该任务不会引入快启风险操作。
* **将启动过程中的加载依赖库逻辑前置到快启点内**

  import动作前置存在适用范围，系统建议将冷启动过程中的import动作尽可能放到快启初始化流程内，以扩大收益。通过[DevEco Profiler调优工具](ide-profiler.md)扫描关键词“Evaluate”，获取启动过程中的import动作。

  不建议将启动后的import动作前置到启动流程甚至快启初始化流程中，否则可能导致以下问题。

  （1）劣化普通冷启动性能。

  （2）导致启动流程的资源占用不必要地增加。

  建议采用动态import的方式在AbilityStage.onCreate中执行import动作。

  ```typescript
  export class AppAbilityStage extends AbilityStage {
    onCreate() {
      // ...
      this.preLoadKit();
      // ...
    }

    async preLoadKit() {
      await import('@ohos/common/src/..../1');
      await import('@ohos/common/src/..../2');
      // ...
      await import('@ohos/common/src/..../N');
    }
  }
  ```

## 快启接入的辅助工具

为帮助开发者定位需要适配和修改的内容，系统提供了[配套插件工具](https://gitcode.com/HarmonyOS_Samples/HyperStartup/blob/master/tools/hyperstartupcheck-user-manual.md)。该工具基于代码扫描，识别具有快启风险的代码，并报告给开发者进行修正，节省人工排查工作量，提升应用适配快启的效率。

## 示例代码

针对应用快启启动开发，可参考以下相关实例：

* [应用快启技术实现的应用加速启动](https://gitcode.com/HarmonyOS_Samples/HyperStartup)
