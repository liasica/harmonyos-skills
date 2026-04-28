---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-form-overview
title: ArkTS卡片概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:25+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:3eabfaeb5ac938a3574ac6e224973393c668c1bfb40c9c0f4f4ab35a2829fbcb
---

以下内容介绍基于ArkTS声明式开发范式语言开发卡片。

## 亮点/特征

1. 统一开发范式

   * ArkTS卡片统一了卡片和应用页面的开发范式，应用页面的布局可以直接复用到卡片布局中，提升开发体验和开发效率。具体请参考图1 卡片工程结构对比。

   **图1** 卡片工程结构对比

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/oxZidcAgTjmlHBfv6mpw_Q/zh-cn_image_0000002583438329.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=5DE62D4B8812B64C9B0A38548E07D7AB072D6CE4E684D0AD0F97DCBC8B1049CF)
2. 卡片能力增强

   * 新增了动效的能力：ArkTS卡片开放了[属性动画](../harmonyos-references/ts-animatorproperty.md)和[显式动画](../harmonyos-references/ts-explicit-animation.md)的能力，使卡片的交互更加友好。
   * 新增了自定义绘制的能力：ArkTS卡片开放了[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)画布组件的能力，卡片可以使用自定义绘制的能力构建更多样的显示和交互效果。
   * 允许卡片中运行逻辑代码：开放逻辑代码运行能力后，部分业务逻辑可以在卡片内部实现，拓宽了业务适用场景。

## 实现原理

* 卡片使用方：显示卡片内容的宿主应用，控制卡片在宿主中展示的位置，当前仅系统应用可以作为卡片使用方。
* 卡片提供方：提供卡片显示内容的应用，控制卡片的显示内容、控件布局以及控件点击事件。
* 卡片管理服务：用于管理系统中所添加卡片的常驻代理服务，提供[formProvider](../harmonyos-references/js-apis-app-form-formprovider.md)的接口能力，同时提供卡片对象的管理与使用以及卡片周期性刷新等能力。
* 卡片渲染服务：用于管理卡片渲染实例，渲染实例与卡片使用方的卡片组件一一绑定。卡片渲染服务根据form\_config.json配置的卡片信息运行widget.abc文件的卡片页面代码进行渲染，并将渲染后的数据发送至卡片使用方对应的卡片组件。

**图2** ArkTS卡片实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/VCzclhSQTpWJP3L-JFQ9Mg/zh-cn_image_0000002552958284.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=4C8CCDF9BB5328387ECFCD9212EC6E742C0F3E759A63B1F342F47515AB42B2C1)

**图3** ArkTS卡片渲染服务运行原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/dPmFs9a1SQq7RrYoUlePUg/zh-cn_image_0000002583478285.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=55AFD91976C1953BC1F39A598576BD05BE26CFCB5631912ABA342E9B92E2D15E)

与JS卡片相比，ArkTS卡片支持在卡片中运行逻辑代码，为确保ArkTS卡片发生问题后不影响卡片使用方应用的使用，ArkTS卡片新增了卡片渲染服务用于运行卡片页面代码widget.abc，卡片渲染服务由卡片管理服务管理。卡片使用方的每个卡片组件都对应了卡片渲染服务里的一个渲染实例，同一卡片提供方的渲染实例运行在同一个ArkTS虚拟机运行环境中，不同卡片提供方的渲染实例运行在不同的ArkTS虚拟机运行环境中，通过ArkTS虚拟机运行环境隔离不同卡片提供方卡片之间的资源与状态。开发过程中需要注意的是globalThis对象的使用，相同卡片提供方的卡片globalThis对象是同一个，不同卡片提供方的卡片globalThis对象是不同的。

## ArkTS卡片类型

ArkTS卡片分为动态卡片、静态卡片和互动卡片三种类型。

静态卡片整体的运行框架、渲染流程与动态卡片是一致的。主要区别在于，卡片渲染服务将卡片内容渲染完毕后，卡片使用方会使用最后一帧渲染的数据作为静态图片显示，其次卡片渲染服务中的卡片实例会释放该卡片的所有运行资源以节省内存。因此频繁的刷新会导致静态卡片运行时资源不断的创建和销毁，增加卡片功耗。

| 卡片类型 | 支持的能力 | 适用场景 | 优缺点 |
| --- | --- | --- | --- |
| 静态卡片 | 仅支持UI组件和布局能力。 | 主要用于展示静态信息（UI相对固定），仅可以通过FormLink组件跳转到指定的UIAbility。 | 功能简单但可以有效控制内存开销。 |
| 动态卡片 | 除了支持UI组件和布局能力，还支持通用事件能力和自定义动效能力。 | 用于有复杂业务逻辑和交互的场景。例如：卡片页面图片的刷新、卡片内容的刷新等。 | 功能丰富但内存开销较大。 |
| 互动卡片 | 在动态卡片基础上，额外支持破框动效能力。 | 用于有复杂业务逻辑和交互，需要执行破框动效呈现更好视觉体验的场景。例如：桌面卡片游戏等。 | 功能丰富但内存开销较大。 |

### 动态卡片

ArkTS卡片中提供了[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口用于卡片Card.ets和FormExtensionAbility之间的交互，当前支持router、message和call三种类型的事件，仅在卡片控件的点击事件中可以调用。

**图4** ArkTS事件交互实现原理

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/MoE-SgzUSFmmnlYiCCbJ_A/zh-cn_image_0000002552798636.png?HW-CC-KV=V1&HW-CC-Date=20260427T234123Z&HW-CC-Expire=86400&HW-CC-Sign=1EBE3EC35D9278ADB26885AE1DABA73F3CEDC8E4FCCA0F3C76CB8AF02D296C6A)

动态卡片事件的主要使用场景如下：

* router事件：可以使用router事件跳转到应用自身的UIAbility，以完成点击卡片跳转应用内页面的交互功能。
* call事件：可以使用call事件拉起应用自身的UIAbility到后台，再通过UIAbility申请对应后台[长时任务](long-time-task-overview.md)完成音乐播放等功能。
* message事件：可以使用message拉起FormExtensionAbility，通过onFormEvent接口回调通知，以完成卡片内控件点击消息传递，从而更新卡片内容。

### 静态卡片

ArkTS卡片提供FormLink静态卡片交互组件，用于静态卡片内部和提供方应用间的交互，当前支持router、message和call三种类型的事件。请参见[FormLink](../harmonyos-references/ts-container-formlink.md)。

### 互动卡片

从API version 20开始支持互动卡片，互动卡片提供破框动效能力，并实现人机交互，提升信息提醒、浅层交互和可玩性。具体请参考[互动卡片概述](arkts-ui-liveform-overview.md)。

## 模拟器支持情况

本Kit支持模拟器开发，但与真机存在部分能力差异，具体如下：

* 通用差异：详情请参见[模拟器与真机的差异](ide-emulator-specification.md)。
* 模拟器中不支持 1 \* 1卡片预览。
* 模拟器中不支持背板透明卡片预览。
* 模拟器中不支持互动卡片预览。

## 约束与限制

ArkTS卡片支持在UI内运行逻辑代码，相较于JS卡片具备了更加丰富的能力，但也增加了使用卡片进行恶意行为的风险。因为承载ArkTS卡片UI部分的widget.abc代码运行在系统公共的FRS进程内，并最终显示在卡片使用方应用中（一般为桌面应用），为确保系统渲染进程的稳定性、各卡片之间的隔离安全性，以及内存功耗等资源考虑，对ArkTS卡片UI可使用的能力做了以下约束：

* 当前仅支持基于ArkUI框架开发卡片，暂不支持跨平台开发。
* 当导入模块时，仅支持导入标识“支持在ArkTS卡片中使用”的模块。若使用了不支持使用的API，卡片加载显示异常。
* 支持导入[HAR](har-package.md)静态共享包，不支持导入[HSP](in-app-hsp.md)动态共享包。
* 不支持使用native语言开发，不支持加载native so。
* 针对卡片UI页面开发，ArkTS卡片仅支持[声明式开发范式](arkts-ui-development-overview.md)的部分组件、事件、动效、数据管理、状态管理和API能力。对于支持在ArkTS卡片UI页面中使用的接口，会添加“卡片能力”的标记，如：从API version 12开始，该接口支持在ArkTS卡片中使用。
* 卡片组件内容的事件处理和卡片使用方的事件处理是独立的，为防止手势冲突，卡片内不支持左右滑动的控件。

除此之外，当前ArkTS卡片还存在如下约束：

* 不支持极速预览。
* 不支持断点调试能力。
* 不支持Hot Reload热重载。
* 不支持[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)。
* DevEco Studio的相关约束请参考[使用约束](ide-service-widget.md#section1181172254318)。
