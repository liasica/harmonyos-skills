---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h
title: context_constant.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > context_constant.h
category: harmonyos-references
scraped_at: 2026-04-28T07:58:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:70dd2ac50a6a3ed26d7c41faeaac7cc04058791e76ff04f8aeba870f9c714784
---

## 概述

PhonePC/2in1TabletTVWearable

提供AbilityRuntime模块上下文常量的定义。

**引用文件：** <AbilityKit/ability\_runtime/context\_constant.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 13

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityRuntime\_AreaMode](capi-context-constant-h.md#abilityruntime_areamode) | AbilityRuntime\_AreaMode | 文件数据加密等级。 |
| [AbilityRuntime\_StartVisibility](capi-context-constant-h.md#abilityruntime_startvisibility) | AbilityRuntime\_StartVisibility | 启动Ability时的窗口和dock栏图标的显示模式。 |
| [AbilityRuntime\_WindowMode](capi-context-constant-h.md#abilityruntime_windowmode) | AbilityRuntime\_WindowMode | 窗口模式。 |
| [AbilityRuntime\_SupportedWindowMode](capi-context-constant-h.md#abilityruntime_supportedwindowmode) | AbilityRuntime\_SupportedWindowMode | 组件所支持的窗口模式。在应用内启动UIAbility时，指定窗口是否显示最大化/窗口化/分屏按键。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### AbilityRuntime\_AreaMode

PhonePC/2in1TabletTVWearable

```
1. enum AbilityRuntime_AreaMode
```

**描述**

文件数据加密等级。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL1 = 0 | 设备级加密区，设备开机后可访问的数据区。  对于私有文件，如闹铃、壁纸等，应用可以将这些文件放到设备级加密分区（EL1）中，以保证在用户输入密码前就可以被访问。 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL2 = 1 | 用户级加密区，设备开机，首次输入密码后才能够访问的数据区。  对于私有文件，如闹铃、壁纸等，应用可以将这些文件放到设备级加密分区（EL1）中，以保证在用户输入密码前就可以被访问。 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL3 = 2 | 用户级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，可读写；解锁后，可读写。  未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，可创建、可打开、可写不可读；解锁后，可创建、可打开、可读写。  对于应用中的记录步数、文件下载、音乐播放，需要在锁屏时读写和创建新文件，放在（EL3）的加密分区比较合适。 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL4 = 3 | 用户级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，FEB2.0可读写、FEB3.0不可读写；解锁后，可读写。  未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，不可创建；解锁后，可创建、可打开、可读写。  对于用户安全信息相关的文件，锁屏时不需要读写文件、也不能创建文件，放在（EL4）的加密分区更合适。 |
| ABILITY\_RUNTIME\_AREA\_MODE\_EL5 = 4 | 应用级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，可读写；解锁后，可读写。  未打开文件：锁屏时，获取DataAccessLock（JS API）下可打开、可读写，否则不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，可创建、可打开、可读写；解锁后，可创建、可打开、可读写。  对于用户隐私敏感数据文件，锁屏后默认不可读写，如果锁屏后需要读写文件，则锁屏前可以调用[Access](js-apis-screenlockfilemanager.md#screenlockfilemanageracquireaccess)接口申请继续读写文件，或者锁屏后也需要创建新文件且可读写，放在（EL5）的应用级加密分区更合适。 |

### AbilityRuntime\_StartVisibility

PhonePC/2in1TabletTVWearable

```
1. enum AbilityRuntime_StartVisibility
```

**描述**

启动Ability时的窗口和dock栏图标的显示模式。

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| ABILITY\_RUNTIME\_HIDE\_UPON\_START = 0 | 隐藏窗口及dock栏图标。仅在2in1设备上生效。 |
| ABILITY\_RUNTIME\_SHOW\_UPON\_START = 1 | 显示窗口及dock栏图标。仅在2in1设备上生效。 |

### AbilityRuntime\_WindowMode

PhonePC/2in1TabletTVWearable

```
1. enum AbilityRuntime_WindowMode
```

**描述**

窗口模式。

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| ABILITY\_RUNTIME\_WINDOW\_MODE\_UNDEFINED = 0 | 窗口模式未定义。 |
| ABILITY\_RUNTIME\_WINDOW\_MODE\_FULL\_SCREEN = 1 | 全屏模式。仅在2in1设备上生效。 |

### AbilityRuntime\_SupportedWindowMode

PhonePC/2in1TabletTVWearable

```
1. enum AbilityRuntime_SupportedWindowMode
```

**描述**

在应用内启动UIAbility时，指定窗口是否显示最大化/窗口化/分屏按键。如果未配置该字段，则默认采用该UIAbility对应的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的supportWindowMode字段取值。

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FULL\_SCREEN = 0 | 窗口支持全屏显示。 |
| ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_SPLIT = 1 | 窗口支持分屏显示。通常需要配合ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FULL\_SCREEN或ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FLOATING一起使用，不建议只配置ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_SPLIT。当仅配置ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_SPLIT时，2in1设备上的窗口默认为悬浮窗模式，支持进入分屏模式。 |
| ABILITY\_RUNTIME\_SUPPORTED\_WINDOW\_MODE\_FLOATING = 2 | 支持窗口化显示。 |
