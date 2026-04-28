---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-background-process-manager-h
title: background_process_manager.h
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > C API > 头文件 > background_process_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:05:38+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:5de4045006f90df76b7b5a2a6b158513da854b8ad6e457c278400f388891bf62
---

## 概述

PhonePC/2in1TabletTVWearable

本模块提供了后台子进程管控接口。开发者可以通过本模块接口对子进程进行压制、解压制，避免子进程过多占用系统资源，导致系统使用卡顿。本模块接口仅对通过[OH\_Ability\_StartNativeChildProcess](capi-native-child-process-h.md#oh_ability_startnativechildprocess)接口创建的子进程生效。

**引用文件：** <background\_process\_manager/background\_process\_manager.h>

**库：** libbackground\_process\_manager.z.so

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**起始版本：** 17

**相关模块：** [BackgroundProcessManager](capi-backgroundprocessmanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [BackgroundProcessManager\_ProcessPriority](capi-background-process-manager-h.md#backgroundprocessmanager_processpriority) | BackgroundProcessManager\_ProcessPriority | 子进程压制档位。 |
| [BackgroundProcessManager\_ErrorCode](capi-background-process-manager-h.md#backgroundprocessmanager_errorcode) | BackgroundProcessManager\_ErrorCode | 定义后台子进程管控错误码。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int OH\_BackgroundProcessManager\_SetProcessPriority(int pid, BackgroundProcessManager\_ProcessPriority priority)](capi-background-process-manager-h.md#oh_backgroundprocessmanager_setprocesspriority) | 设置子进程的压制档位，子进程被压制后可获得的CPU资源将会受到限制。如果主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，子进程如需继续压制，需要重新调用本接口。 |
| [int OH\_BackgroundProcessManager\_ResetProcessPriority(int pid)](capi-background-process-manager-h.md#oh_backgroundprocessmanager_resetprocesspriority) | 为子进程解压制，即子进程策略恢复为主进程调度策略。若主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，等效于执行一次resetProcessPriority动作。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### BackgroundProcessManager\_ProcessPriority

PhonePC/2in1TabletTVWearable

```
1. enum BackgroundProcessManager_ProcessPriority
```

**描述**

子进程压制档位。

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| PROCESS\_BACKGROUND = 1 | 该档位相较PROCESS\_INACTIVE压制效果更显著，获取到的CPU资源更少。推荐执行处于后台的图文页面等用户无感知业务的后台子进程时设置该档位。 |
| PROCESS\_INACTIVE = 2 | 推荐正在执行播放音频、导航等用户可感知业务的后台子进程时设置该档位。 |

### BackgroundProcessManager\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum BackgroundProcessManager_ErrorCode
```

**描述**

定义后台子进程管控错误码。

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| ERR\_BACKGROUND\_PROCESS\_MANAGER\_SUCCESS = 0 | 压制参数发送成功。 |
| ERR\_BACKGROUND\_PROCESS\_MANAGER\_INVALID\_PARAM = 401 | 参数检查失败。 |
| ERR\_BACKGROUND\_PROCESS\_MANAGER\_REMOTE\_ERROR = 31800001 | 客户端进程请求系统服务进程，获取系统服务操作失败。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_BackgroundProcessManager\_SetProcessPriority()

PhonePC/2in1TabletTVWearable

```
1. int OH_BackgroundProcessManager_SetProcessPriority(int pid, BackgroundProcessManager_ProcessPriority priority)
```

**描述**

设置子进程的压制档位，子进程被压制后可获得的CPU资源将会受到限制。如果主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，子进程如需继续压制，需要重新调用本接口。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int pid | 需要被压制子进程的进程号，[OH\_Ability\_StartNativeChildProcess](capi-native-child-process-h.md#oh_ability_startnativechildprocess)接口创建子进程后的pid参数，即为子进程进程号。 |
| [BackgroundProcessManager\_ProcessPriority](capi-background-process-manager-h.md#backgroundprocessmanager_processpriority) priority | 压制档位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回 [ERR\_BACKGROUND\_PROCESS\_MANAGER\_SUCCESS](capi-background-process-manager-h.md#backgroundprocessmanager_errorcode)，表示压制参数发送成功。  返回 [ERR\_BACKGROUND\_PROCESS\_MANAGER\_INVALID\_PARAM](capi-background-process-manager-h.md#backgroundprocessmanager_errorcode)，表示参数检查失败。 |

### OH\_BackgroundProcessManager\_ResetProcessPriority()

PhonePC/2in1TabletTVWearable

```
1. int OH_BackgroundProcessManager_ResetProcessPriority(int pid)
```

**描述**

为子进程解压制，即子进程策略恢复为主进程调度策略。若主进程调度策略发生变化，如从后台切至前台等，子进程会跟随主进程一同变化，等效于执行一次resetProcessPriority动作。

**起始版本：** 17

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int pid | 子进程的进程号，[OH\_Ability\_StartNativeChildProcess](capi-native-child-process-h.md#oh_ability_startnativechildprocess)接口创建子进程后的pid参数，即为子进程进程号。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回 [ERR\_BACKGROUND\_PROCESS\_MANAGER\_SUCCESS](capi-background-process-manager-h.md#backgroundprocessmanager_errorcode)，表示压制参数发送成功。 |
