---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-navigation-router-h
title: navigation_router.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > navigation_router.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fd6f598ad08bf0c083090422c8e1e3e4c9e7c52dca47e97446baa80998790970
---

## 概述

定义Navigation和Router组件的相关枚举。

**引用文件：** <arkui/node\_attributes/navigation\_router.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NDKNavigation](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NDKNavigation)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_NavDestinationState](capi-navigation-router-h.md#arkui_navdestinationstate) | ArkUI\_NavDestinationState | 定义NavDestination组件的状态。 |
| [ArkUI\_RouterPageState](capi-navigation-router-h.md#arkui_routerpagestate) | ArkUI\_RouterPageState | 定义[Router](arkts-apis-uicontext-router.md)（路由页面）的状态。 |

## 枚举类型说明

### ArkUI\_NavDestinationState

```c
enum ArkUI_NavDestinationState
```

**描述**

定义NavDestination组件的状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_SHOW = 0 | NavDestination组件显示。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_HIDE = 1 | NavDestination组件隐藏。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_APPEAR = 2 | NavDestination从组件树上挂载。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_DISAPPEAR = 3 | NavDestination从组件树上卸载。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_SHOW = 4 | NavDestination组件显示之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_HIDE = 5 | NavDestination组件隐藏之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_APPEAR = 6 | NavDestination挂载到组件树之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_WILL\_DISAPPEAR = 7 | NavDestination从组件树上卸载之前。 |
| ARKUI\_NAV\_DESTINATION\_STATE\_ON\_BACK\_PRESS = 100 | NavDestination从组件返回。 |

### ArkUI\_RouterPageState

```c
enum ArkUI_RouterPageState
```

**描述**

定义[Router](arkts-apis-uicontext-router.md)（路由页面）的状态。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_ROUTER\_PAGE\_STATE\_ABOUT\_TO\_APPEAR = 0 | Router Page即将创建。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ABOUT\_TO\_DISAPPEAR = 1 | Router Page即将销毁。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_SHOW = 2 | Router Page显示。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_HIDE = 3 | Router Page隐藏。 |
| ARKUI\_ROUTER\_PAGE\_STATE\_ON\_BACK\_PRESS = 4 | Router Page返回时。 |
