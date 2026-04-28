---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commoneventmanager-definitions
title: 系统定义的公共事件
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 进程线程通信 > 系统定义的公共事件
category: harmonyos-references
scraped_at: 2026-04-28T08:09:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:441135950422c0292a8fb72b42bce46d3e3131c018bbedc9d001a6347464a635
---

本文档提供了系统定义的公共事件清单。

公共事件类型定义在[ohos.commonEventManager模块的Support枚举](js-apis-commoneventmanager.md#support)中。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## Ability Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_PACKAGE\_RESTARTED

PhonePC/2in1TabletTVWearable

表示用户重启应用包并终止其所有进程。

在设备上指定用户重启应用包并终止其所有进程，将会触发事件通知服务发布该系统公共事件。

说明

三方应用只能监听自身应用的重启事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_RESTARTED"

### COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED

PhonePC/2in1TabletTVWearable

表示用户清除应用包数据。

在设备上指定用户清除应用包数据，将会触发事件通知服务发布该系统公共事件。

说明

三方应用只能监听自身应用的数据清理事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_DATA\_CLEARED"

### COMMON\_EVENT\_QUICK\_FIX\_APPLY\_RESULT

PhonePC/2in1TabletTVWearable

表示快速修复应用。

在设备上指定用户快速修复应用，将会触发事件通知服务发布该系统公共事件。

说明

三方应用只能监听自身应用的快速修复事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.QUICK\_FIX\_APPLY\_RESULT"

### COMMON\_EVENT\_QUICK\_FIX\_REVOKE\_RESULT10+

PhonePC/2in1TabletTVWearable

表示撤销快速修复。

在设备上撤销快速修复时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.QUICK\_FIX\_REVOKE\_RESULT"

### COMMON\_EVENT\_PACKAGE\_ADDED

PhonePC/2in1TabletTVWearable

表示设备上已安装新应用包的公共事件的动作。

在设备上指定用户下安装了新的应用程序，将会触发事件通知服务发布该系统公共事件。

说明

三方应用只能监听自身应用的安装事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_ADDED"

### COMMON\_EVENT\_PACKAGE\_REMOVED

PhonePC/2in1TabletTVWearable

表示已从设备卸载已安装的应用程序，但应用程序数据保留的公共事件的操作。

在设备指定用户下卸载指定的应用程序包，将会触发事件通知服务发布该系统公共事件。

说明

三方应用只能监听自身应用的卸载事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_REMOVED"

### COMMON\_EVENT\_BUNDLE\_REMOVED

PhonePC/2in1TabletTVWearable

表示现有的应用程序包从设备中移除的事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.BUNDLE\_REMOVED"

### COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED

PhonePC/2in1TabletTVWearable

表示现有的应用程序包从设备上完全删除的事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_FULLY\_REMOVED"

### COMMON\_EVENT\_PACKAGE\_CHANGED

PhonePC/2in1TabletTVWearable

表示应用包已更改的公共事件的动作（例如，包中的组件已启用或禁用）。

在设备上安装的应用程序包更新或者包的组件被禁用使能，将会触发事件通知服务发布该系统公共事件。

说明

三方应用只能监听自身应用的更改事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_CHANGED"

### COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED

PhonePC/2in1TabletTVWearable

表示用户清除应用包缓存数据的公共事件的动作。

对设备上安装的应用程序包清除缓存时，将会触发事件通知服务发布该系统公共事件。

说明

三方应用只能监听自身应用的缓存清理事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_CACHE\_CLEARED"

### COMMON\_EVENT\_PACKAGES\_SUSPENDED

PhonePC/2in1TabletTVWearable

表示包已经被挂起。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGES\_SUSPENDED"

### COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED

PhonePC/2in1TabletTVWearable

发送到已被系统挂起的包。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.MY\_PACKAGE\_SUSPENDED"

### COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED

PhonePC/2in1TabletTVWearable

发送到已被系统解除挂起的包。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.MY\_PACKAGE\_UNSUSPENDED"

### COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE

PhonePC/2in1TabletTVWearable

通知用户低内存状态并且应该启动包管理。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.MANAGE\_PACKAGE\_STORAGE"

## Account Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_MINORSMODE\_ON12+

PhonePC/2in1TabletTVWearable

表示用户开启未成年人模式。

在设备上开启未成年人模式，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**取值：** "usual.event.MINORSMODE\_ON"

### COMMON\_EVENT\_MINORSMODE\_OFF12+

PhonePC/2in1TabletTVWearable

表示用户关闭未成年人模式。

在设备上关闭未成年人模式，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**取值：** "usual.event.MINORSMODE\_OFF"

## ArkData

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_DATA\_SHARE\_READY12+

PhonePC/2in1TabletTVWearable

表示datashare服务可用。

datashare服务启动完成后，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.DATA\_SHARE\_READY"

## ArkUI

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_SPLIT\_SCREEN

PhonePC/2in1TabletTVWearable

表示分屏行为的公共事件。

启动最近任务窗口、创建或销毁分屏条，都会触发通知服务发布这个系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**取值：** "common.event.SPLIT\_SCREEN"

## Notification Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_SLOT\_CHANGE

PhonePC/2in1TabletTVWearable

表示通知渠道或通知开关发生变化。

通知设置里修改应用的渠道参数、渠道开关，或者开启、关闭通知使能开关时，都会触发通知服务发布这个系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.NOTIFICATION\_CONTROLLER

**取值：** "usual.event.SLOT\_CHANGE"

## Background Tasks Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED

PhonePC/2in1TabletTVWearable

表示设备上待机状态变化，触发公共事件发布动作。

如果用户一段时间没有使用设备且屏幕已经关闭情况下，系统延迟后台应用程序CPU和网络访问，将会触发公共事件服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.DEVICE\_IDLE\_MODE\_CHANGED"

## Basic Services Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_USB\_STATE

PhonePC/2in1TabletTVWearable

表示USB设备状态发生变化。

当USB断开或者连接时状态发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.hardware.usb.action.USB\_STATE"

### COMMON\_EVENT\_USB\_PORT\_CHANGED

PhonePC/2in1TabletTVWearable

提示用户设备的USB端口状态发生改变。

当USB的端口状态发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.hardware.usb.action.USB\_PORT\_CHANGED"

### COMMON\_EVENT\_USB\_DEVICE\_ATTACHED

PhonePC/2in1TabletTVWearable

当用户设备作为USB主机时，提示USB设备已挂载。

当USB连接时状态发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED"

### COMMON\_EVENT\_USB\_DEVICE\_DETACHED

PhonePC/2in1TabletTVWearable

当用户设备作为USB主机时，提示USB设备被卸载。

当USB断开时状态发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED"

### COMMON\_EVENT\_TIME\_CHANGED

PhonePC/2in1TabletTVWearable

设置系统时间的公共事件的动作。

当设置系统时间时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.TIME\_CHANGED"

### COMMON\_EVENT\_TIME\_TICK

PhonePC/2in1TabletTVWearable

表示系统时间更改的公共事件的动作。

当以整分钟为单位的系统时间更改时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.TIME\_TICK"

### COMMON\_EVENT\_TIMEZONE\_CHANGED

PhonePC/2in1TabletTVWearable

表示系统时区更改的公共事件的动作。

当系统时区更改时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.TIMEZONE\_CHANGED"

### COMMON\_EVENT\_USER\_INFO\_UPDATED

PhonePC/2in1TabletTVWearable

表示用户信息已更新。

分布式账号信息变更、系统账号头像信息变更、系统账号名称变更将会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

与这个公共事件相关的接口：setOsAccountName、setOsAccountProfilePhoto, 这些为系统API，setOsAccountDistributedInfo为公共API，具体参看[系统账号接口文档](js-apis-osaccount.md)、[分布式账号接口文档](js-apis-distributed-account.md)。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.USER\_INFO\_UPDATED"

### COMMON\_EVENT\_USER\_UNLOCKED

PhonePC/2in1TabletTVWearable

表示设备重启后解锁时，当前用户的凭据加密存储已解锁的公共事件的动作。

切换到带有锁屏密码的用户，并且首次解锁会发出触发事件通知服务发布该系统公共事件，事件携带标识该用户的系统账号ID。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.USER\_UNLOCKED"

### COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGIN

PhonePC/2in1TabletTVWearable

表示分布式账号登录成功的动作。

分布式账号登录成功时会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

与这个公共事件相关的接口：setOsAccountDistributedInfo、updateOsAccountDistributedInfo(已废弃)，这些为公共API，setOsAccountDistributedInfoByLocalId为系统API，具体参看[分布式账号接口文档](js-apis-distributed-account.md)。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**取值：** "common.event.DISTRIBUTED\_ACCOUNT\_LOGIN"

### COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT

PhonePC/2in1TabletTVWearable

表示分布式账号登出成功的动作。

分布式账号登出时会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

与这个公共事件相关的接口：setOsAccountDistributedInfo、updateOsAccountDistributedInfo(已废弃)，这些为公共API，setOsAccountDistributedInfoByLocalId为系统API，具体参看[分布式账号接口文档](js-apis-distributed-account.md)。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**取值：** "common.event.DISTRIBUTED\_ACCOUNT\_LOGOUT"

### COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID

PhonePC/2in1TabletTVWearable

表示分布式账号token令牌无效的动作。

分布式账号的token令牌无效时会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

与这个公共事件相关的接口：setOsAccountDistributedInfo、updateOsAccountDistributedInfo(已废弃)，这些为公共API，setOsAccountDistributedInfoByLocalId为系统API，具体参看[分布式账号接口文档](js-apis-distributed-account.md)。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**取值：** "common.event.DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID"

### COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOFF

PhonePC/2in1TabletTVWearable

表示分布式账号注销的动作。

分布式账号注销成功会时触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

与这个公共事件相关的接口：setOsAccountDistributedInfo、updateOsAccountDistributedInfo(已废弃)，这些为公共API，setOsAccountDistributedInfoByLocalId为系统API，具体参看[分布式账号接口文档](js-apis-distributed-account.md)。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**取值：** "common.event.DISTRIBUTED\_ACCOUNT\_LOGOFF"

### COMMON\_EVENT\_SCREEN\_LOCKED

PhonePC/2in1TabletTVWearable

表示屏幕锁定的公共事件。

当锁屏锁定时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**取值：** "usual.event.SCREEN\_LOCKED"

### COMMON\_EVENT\_SCREEN\_UNLOCKED

PhonePC/2in1TabletTVWearable

表示屏幕解锁的公共事件。

当锁屏解锁时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**取值：** "usual.event.SCREEN\_UNLOCKED"

### COMMON\_EVENT\_USER\_PRESENT(deprecated)

PhonePC/2in1TabletTVWearable

用户解锁设备的公共事件的动作。

说明：

从API Version 10开始废弃，替代接口为[COMMON\_EVENT\_SCREEN\_UNLOCKED](commoneventmanager-definitions.md#common_event_screen_unlocked)。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.USER\_PRESENT"

### COMMON\_EVENT\_BATTERY\_CHANGED

PhonePC/2in1TabletTVWearable

表示电池充电状态、电平和其他信息发生变化的公共事件的动作。

当电池电量、电池温度、电池健康状态、设备连接的充电器类型、充电器最大电流、充电器最大电压、电池充电状态、充电次数、电池的总容量、电池剩余容量、电池的技术型号、电池的充电类型变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.BATTERY\_CHANGED"

### COMMON\_EVENT\_BATTERY\_LOW

PhonePC/2in1TabletTVWearable

表示电池电量低的普通事件的动作。

当电池电量低于设备设置的低电量百分比值时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.BATTERY\_LOW"

### COMMON\_EVENT\_BATTERY\_OKAY

PhonePC/2in1TabletTVWearable

表示电池退出低电量状态的公共事件的动作。

当电池电量从低电量等级变化到电池电量高于低电量等级时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.BATTERY\_OKAY"

### COMMON\_EVENT\_POWER\_CONNECTED

PhonePC/2in1TabletTVWearable

设备连接到外部电源的公共事件的动作。

当设备连接到外部可识别的充电器类型充电时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.POWER\_CONNECTED"

### COMMON\_EVENT\_POWER\_DISCONNECTED

PhonePC/2in1TabletTVWearable

设备与外部电源断开的公共事件的动作。

当设备与外部电源断开时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.POWER\_DISCONNECTED"

### COMMON\_EVENT\_DISCHARGING

PhonePC/2in1TabletTVWearable

表示系统停止为电池充电的公共事件的动作。

当系统停止为电池充电时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.DISCHARGING"

### COMMON\_EVENT\_CHARGING

PhonePC/2in1TabletTVWearable

表示系统开始为电池充电的公共事件的动作。

当系统开始为电池充电时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.CHARGING"

### COMMON\_EVENT\_CHARGE\_IDLE\_MODE\_CHANGED10+

PhonePC/2in1TabletTVWearable

表示设备进入充电空闲模式的公共事件的动作。

当设备处于空闲、正在充电并且温升可接受的一种状态时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.CHARGE\_IDLE\_MODE\_CHANGED"

### COMMON\_EVENT\_SHUTDOWN

PhonePC/2in1TabletTVWearable

表示设备正在关闭并将继续最终关闭的公共事件的操作。

当设备正在关闭并将继续最终关闭时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.SHUTDOWN"

### COMMON\_EVENT\_SCREEN\_OFF

PhonePC/2in1TabletTVWearable

表示由电源服务发起的设备灭屏完成的普通事件的动作。

当由电源服务发起的设备灭屏完成时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.SCREEN\_OFF"

### COMMON\_EVENT\_SCREEN\_ON

PhonePC/2in1TabletTVWearable

表示由电源服务发起的设备亮屏完成的普通事件的动作。

当由电源服务发起的设备亮屏完成时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.SCREEN\_ON"

### COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED

PhonePC/2in1TabletTVWearable

表示系统节能模式更改的公共事件的动作。

当系统节能模式更改时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.POWER\_SAVE\_MODE\_CHANGED"

### COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED

PhonePC/2in1TabletTVWearable

表示设备热状态的公共事件的动作。

当设备热等级变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.THERMAL\_LEVEL\_CHANGED"

### COMMON\_EVENT\_ENTER\_FORCE\_SLEEP12+

PhonePC/2in1TabletTVWearable

表示设备即将进入强制睡眠模式的公共事件的动作。

当设备即将进入强制睡眠模式时，将会触发事件通知服务发布该系统公共事件。所有订阅者必须在1秒钟内处理该事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.ENTER\_FORCE\_SLEEP"

### COMMON\_EVENT\_EXIT\_FORCE\_SLEEP12+

PhonePC/2in1TabletTVWearable

表示设备退出强制睡眠模式的公共事件的动作。

当设备退出强制睡眠模式时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.EXIT\_FORCE\_SLEEP"

### COMMON\_EVENT\_ENTER\_HIBERNATE15+

PhonePC/2in1TabletTVWearable

表示设备即将进入休眠模式的公共事件的动作。

当设备即将进入休眠模式时，将会触发事件通知服务发布该系统公共事件。所有订阅者必须在1秒钟内处理该事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.ENTER\_HIBERNATE"

### COMMON\_EVENT\_EXIT\_HIBERNATE15+

PhonePC/2in1TabletTVWearable

表示设备退出休眠模式的公共事件的动作。

当设备退出休眠模式时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.EXIT\_HIBERNATE"

## Connectivity Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_CHANGE20+

PhonePC/2in1TabletTVWearable

表示蓝牙HFP AG连接状态变化的公共事件的操作。

当蓝牙HFP AG连接状态变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.handsfree.ag.CONNECT\_STATE\_CHANGE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_CHANGE20+

PhonePC/2in1TabletTVWearable

表示蓝牙A2DP Source连接状态变化的公共事件的操作。

当蓝牙A2DP Source连接状态变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.CONNECT\_STATE\_CHANGE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_CHANGE20+

PhonePC/2in1TabletTVWearable

表示蓝牙AVRCP连接状态变化的公共事件的操作。

当蓝牙AVRCP连接状态变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.AVRCP\_CONNECT\_STATE\_CHANGE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_CHANGE20+

PhonePC/2in1TabletTVWearable

表示蓝牙媒体编解码器变化的公共事件的操作。

当蓝牙媒体编解码器变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.CODEC\_VALUE\_CHANGE"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_STATE\_CHANGE20+

PhonePC/2in1TabletTVWearable

表示蓝牙远程设备ACL连接状态变化的公共事件的操作。

当蓝牙远程设备ACL连接状态变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.ACL\_STATE\_CHANGE"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE\_CHANGE20+

PhonePC/2in1TabletTVWearable

表示蓝牙配对状态变化的公共事件的操作。

当蓝牙配对状态变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.PAIR\_STATE\_CHANGE"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_CHANGE23+

PhonePC/2in1TabletTVWearable

表示蓝牙扫描模式变化的公共事件的操作。

当蓝牙扫描模式变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.host.SCAN\_MODE\_CHANGE"

### COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED

PhonePC/2in1TabletTVWearable

指示设备NFC状态已更改的公共事件的操作。

指示设备NFC状态更改时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.nfc.action.ADAPTER\_STATE\_CHANGED"

### COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED

PhonePC/2in1TabletTVWearable

检测到NFC场强进入的公共事件。

当检测到NFC场强进入时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.nfc.action.RF\_FIELD\_ON\_DETECTED"

### COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED

PhonePC/2in1TabletTVWearable

检测到NFC场强离开的公共事件。

当检测到NFC场强离开时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.nfc.action.RF\_FIELD\_OFF\_DETECTED"

### COMMON\_EVENT\_WIFI\_POWER\_STATE

PhonePC/2in1TabletTVWearable

Wi-Fi状态变化。

当Wi-Fi状态发生变化时（如启用、禁用Wi-Fi），将会触发事件通知服务发布该系统公共事件。

状态值：0：WLAN正在关闭，1：WLAN已关闭，2：WLAN正在打开，3：WLAN已启动。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.wifi.POWER\_STATE"

### COMMON\_EVENT\_WIFI\_SCAN\_FINISHED

PhonePC/2in1TabletTVWearable

表示Wi-Fi接入点已被扫描并证明可用的动作。

当Wi-Fi接入点已被扫描并证明可用，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.LOCATION

**取值：** "usual.event.wifi.SCAN\_FINISHED"

### COMMON\_EVENT\_WIFI\_SCAN\_STATE

PhonePC/2in1TabletTVWearable

表示Wi-Fi扫描接入点状态改变。

当Wi-Fi扫描接入点状态发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.LOCATION

**取值：** "usual.event.wifi.SCAN\_STATE"

### COMMON\_EVENT\_WIFI\_RSSI\_VALUE

PhonePC/2in1TabletTVWearable

表示Wi-Fi信号强度（RSSI）改变。

当Wi-Fi信号强度（RSSI）发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.RSSI\_VALUE"

### COMMON\_EVENT\_WIFI\_CONN\_STATE

PhonePC/2in1TabletTVWearable

Wi-Fi连接状态发生改变。

当Wi-Fi连接状态发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.wifi.CONN\_STATE"

### COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE

PhonePC/2in1TabletTVWearable

表示Wi-Fi热点状态变化。

当Wi-Fi热点状态发生变化，将会触发事件通知服务发布该系统公共事件。

状态值：2：AP正在打开，3：AP已启动，4：AP正在关闭，5：AP已关闭。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.wifi.HOTSPOT\_STATE"

### COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN

PhonePC/2in1TabletTVWearable

表示客户端加入当前设备Wi-Fi热点。

当客户端加入当前设备Wi-Fi热点，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.WIFI\_HS\_STA\_JOIN"

### COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE

PhonePC/2in1TabletTVWearable

表示客户端已断开与当前设备Wi-Fi热点的连接。

当客户端已断开与当前设备Wi-Fi热点的连接，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.WIFI\_HS\_STA\_LEAVE"

### COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE

PhonePC/2in1TabletTVWearable

表示MPLink（增强Wi-Fi功能）状态已更改。

当MPLink（增强Wi-Fi功能）状态发生变化，将会触发事件通知服务发布该系统公共事件（暂不支持）。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者需要的权限：** 无

**取值：** "usual.event.wifi.mplink.STATE\_CHANGE"

### COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE

PhonePC/2in1TabletTVWearable

表示Wi-Fi P2P连接状态改变。

当Wi-Fi P2P连接状态发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO和ohos.permission.LOCATION

**取值：** "usual.event.wifi.p2p.CONN\_STATE\_CHANGE"

### COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED

PhonePC/2in1TabletTVWearable

表示Wi-Fi P2P状态变化。

当Wi-Fi P2P状态发生变化，将会触发事件通知服务发布该系统公共事件。

状态值：2：P2P正在打开，3：P2P已启动，4：P2P正在关闭，5：P2P已关闭。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.p2p.STATE\_CHANGE"

### COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED

PhonePC/2in1TabletTVWearable

表示Wi-Fi P2P对等体状态变化。

当Wi-Fi P2P对等体状态变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.p2p.DEVICES\_CHANGE"

### COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED

PhonePC/2in1TabletTVWearable

表示Wi-Fi P2P发现状态变化。

当Wi-Fi P2P发现状态变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.p2p.PEER\_DISCOVERY\_STATE\_CHANGE"

### COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED

PhonePC/2in1TabletTVWearable

表示Wi-Fi P2P当前设备状态变化。

当Wi-Fi P2P当前设备状态变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.p2p.CURRENT\_DEVICE\_CHANGE"

### COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED

PhonePC/2in1TabletTVWearable

表示Wi-Fi P2P群组信息已更改。

当Wi-Fi P2P群组信息发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_WIFI\_INFO

**取值：** "usual.event.wifi.p2p.GROUP\_STATE\_CHANGED"

## MDM Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED

PhonePC/2in1TabletTVWearable

表示浏览器托管策略已更改。

当浏览器托管策略发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.MANAGED\_BROWSER\_POLICY\_CHANGED"

## Localization Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_LOCALE\_CHANGED

PhonePC/2in1TabletTVWearable

设置系统语言的公共事件的动作。

当设置系统语言时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.LOCALE\_CHANGED"

## Network Kit

PhonePC/2in1TabletTVWearable

### COMMON\_EVENT\_CONNECTIVITY\_CHANGE10+

PhonePC/2in1TabletTVWearable

指示网络连接状态变化。

各类网络（以太网、Wi-Fi、蜂窝等）在发生连接状态状态变化时（断开、断开中、连接中、已连接等），将会触发事件通知服务发布该系统公共事件。

具体枚举值及其对应的连接状态如下表所示：

| 枚举值 | 连接状态 |
| --- | --- |
| 2 | 连接中 |
| 3 | 已连接 |
| 4 | 正在断开 |
| 5 | 已断开 |

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**取值：** "usual.event.CONNECTIVITY\_CHANGE"

### COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED10+

PhonePC/2in1TabletTVWearable

指示飞行模式状态变化。

在开启或者关闭系统飞行模式状态后，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.AIRPLANE\_MODE"

### COMMON\_EVENT\_HTTP\_PROXY\_CHANGE10+

PhonePC/2in1TabletTVWearable

指示网络Http代理配置信息更新。

在系统全局代理或者各类网络（以太网、Wi-Fi、蜂窝等）Http代理配置信息发生变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.HTTP\_PROXY\_CHANGE"

## Telephony Kit

PhonePC/2in1TabletTVWearable

电话服务子系统面向应用发布如下系统公共事件。

### COMMON\_EVENT\_SIM\_STATE\_CHANGED10+

PhonePC/2in1TabletTVWearable

提示SIM卡状态更新。

在设备上面的SIM卡状态发生变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.SIM\_STATE\_CHANGED"

### COMMON\_EVENT\_CALL\_STATE\_CHANGED10+

PhonePC/2in1TabletTVWearable

提示呼叫状态更新。

在设备呼叫状态更新时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_TELEPHONY\_STATE（该权限仅系统应用可申请）

**取值：** "usual.event.CALL\_STATE\_CHANGED"

### COMMON\_EVENT\_NETWORK\_STATE\_CHANGED10+

PhonePC/2in1TabletTVWearable

提示网络状态更新。

在设备网络状态更新时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.NETWORK\_STATE\_CHANGED"

### COMMON\_EVENT\_SIGNAL\_INFO\_CHANGED10+

PhonePC/2in1TabletTVWearable

提示信号信息更新。

在设备信号信息更新时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.SIGNAL\_INFO\_CHANGED"

## AppGallery Kit

PhonePC/2in1TabletTVWearable

AppGallery Kit面向应用发布如下系统公共事件。

### COMMON\_EVENT\_PRIVACY\_STATE\_CHANGED11+

PhonePC/2in1TabletTVWearable

表示隐私签署结果的公共事件。

隐私弹框场景下，用户点击同意，会发送此事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PRIVACY\_STATE\_CHANGED"

## Multimodalinput Kit

PhonePC/2in1TabletTVWearable

Multimodalinput Kit面向应用发布如下系统公共事件。

### COMMON\_EVENT\_TABLET\_MODE\_CHANGED23+

PhonePC/2in1TabletTVWearable

表示可感知支架开合的设备，例如具有支架的平板电脑，

其支架开合状态变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**取值：** "usual.event.TABLET\_MODE\_CHANGED "

### COMMON\_EVENT\_LID\_STATE\_CHANGED23+

PhonePC/2in1TabletTVWearable

表示可感知开合盖子的设备，例如具有开合盖子的笔记本电脑，

其开合盖状态变化时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**取值：** "usual.event.LID\_STATE\_CHANGED"

## 预留公共事件

PhonePC/2in1TabletTVWearable

以下事件为预留公共事件，暂未支持。

### COMMON\_EVENT\_LOCKED\_BOOT\_COMPLETED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）提示用户已完成引导，系统已加载，但屏幕仍锁定。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.LOCKED\_BOOT\_COMPLETED"

### COMMON\_EVENT\_PACKAGE\_FIRST\_LAUNCH

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）应用程序在安装后首次启动。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_FIRST\_LAUNCH"

### COMMON\_EVENT\_PACKAGE\_NEEDS\_VERIFICATION

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）当一个包需要被验证时，由系统包验证者发送。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_NEEDS\_VERIFICATION"

### COMMON\_EVENT\_PACKAGE\_VERIFIED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）当一个包被验证时，由系统包验证者发送。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_VERIFIED"

### COMMON\_EVENT\_PACKAGE\_REPLACED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示设备上安装了新版本的应用程序包并替换了旧版本的动作。数据包含包的名称。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGE\_REPLACED"

### COMMON\_EVENT\_MY\_PACKAGE\_REPLACED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示设备上安装了新版本的应用程序包并替换了旧版本的应用程序包的动作，不包含额外的数据，只发送给被替换的应用程序。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.MY\_PACKAGE\_REPLACED"

### COMMON\_EVENT\_PACKAGES\_UNSUSPENDED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示包已经被解除挂起。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.PACKAGES\_UNSUSPENDED"

### COMMON\_EVENT\_CLOSE\_SYSTEM\_DIALOGS

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户关闭临时系统对话框的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.CLOSE\_SYSTEM\_DIALOGS"

### COMMON\_EVENT\_UID\_REMOVED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户ID已从系统中删除的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.UID\_REMOVED"

### COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_AVAILABLE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示安装在外部存储上的应用程序对系统可用的公共事件的操作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.EXTERNAL\_APPLICATIONS\_AVAILABLE"

### COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_UNAVAILABLE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示安装在外部存储上的应用程序对系统不可用的公共事件的操作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.EXTERNAL\_APPLICATIONS\_UNAVAILABLE"

### COMMON\_EVENT\_CONFIGURATION\_CHANGED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示设备状态（例如，方向和区域设置）已更改的公共事件的操作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.CONFIGURATION\_CHANGED"

### COMMON\_EVENT\_DRIVE\_MODE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示系统处于驾驶模式的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.DRIVE\_MODE"

### COMMON\_EVENT\_HOME\_MODE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示系统处于HOME模式的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.HOME\_MODE"

### COMMON\_EVENT\_OFFICE\_MODE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示系统处于办公模式的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.OFFICE\_MODE"

### COMMON\_EVENT\_USER\_STARTED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户已启动的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.USER\_STARTED"

### COMMON\_EVENT\_USER\_BACKGROUND

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户已被带到后台的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.USER\_BACKGROUND"

### COMMON\_EVENT\_USER\_STARTING

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示要启动用户的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS（该权限仅系统应用可申请）

**取值：** "usual.event.USER\_STARTING"

### COMMON\_EVENT\_USER\_STOPPING

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示要停止用户的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS（该权限仅系统应用可申请）

**取值：** "usual.event.USER\_STOPPING"

### COMMON\_EVENT\_USER\_STOPPED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户已停止的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.USER\_STOPPED"

### COMMON\_EVENT\_DISK\_REMOVED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）外部存储设备状态变更为移除时发送此公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.STORAGE\_MANAGER（该权限仅系统应用可申请）

**取值：** "usual.event.data.DISK\_REMOVED"

### COMMON\_EVENT\_DISK\_UNMOUNTED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）外部存储设备状态变更为卸载时发送此公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.STORAGE\_MANAGER（该权限仅系统应用可申请）

**取值：** "usual.event.data.DISK\_UNMOUNTED"

### COMMON\_EVENT\_DISK\_MOUNTED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）外部存储设备状态变更为挂载时发送此公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.STORAGE\_MANAGER（该权限仅系统应用可申请）

**取值：** "usual.event.data.DISK\_MOUNTED"

### COMMON\_EVENT\_DISK\_BAD\_REMOVAL

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）外部存储设备状态变更为挂载状态下移除时发送此公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.STORAGE\_MANAGER（该权限仅系统应用可申请）

**取值：** "usual.event.data.DISK\_BAD\_REMOVAL"

### COMMON\_EVENT\_DISK\_UNMOUNTABLE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）外部存储设备状态变更为插卡情况下无法挂载时发送此公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.STORAGE\_MANAGER（该权限仅系统应用可申请）

**取值：** "usual.event.data.DISK\_UNMOUNTABLE"

### COMMON\_EVENT\_DISK\_EJECT

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）用户已表示希望删除外部存储介质时发送此公共事件。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.STORAGE\_MANAGER（该权限仅系统应用可申请）

**取值：** "usual.event.data.DISK\_EJECT"

### COMMON\_EVENT\_DATE\_CHANGED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示系统日期已更改的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.DATE\_CHANGED"

### COMMON\_EVENT\_USB\_ACCESSORY\_ATTACHED

PhonePC/2in1TabletTVWearable

表示已连接USB配件的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.hardware.usb.action.USB\_ACCESSORY\_ATTACHED"

### COMMON\_EVENT\_USB\_ACCESSORY\_DETACHED

PhonePC/2in1TabletTVWearable

表示USB配件被卸载的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.hardware.usb.action.USB\_ACCESSORY\_DETACHED"

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）蓝牙免提通信连接状态公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_CHANGE](commoneventmanager-definitions.md#common_event_bluetooth_handsfree_ag_connect_state_change20)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.handsfree.ag.CONNECT\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CURRENT\_DEVICE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示连接到蓝牙免提的设备处于活动状态的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.handsfree.ag.CURRENT\_DEVICE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_AUDIO\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙A2DP连接状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.handsfree.ag.AUDIO\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）蓝牙A2DP连接状态公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_CHANGE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_connect_state_change20)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.CONNECT\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CURRENT\_DEVICE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示使用蓝牙A2DP连接的设备处于活动状态的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.CURRENT\_DEVICE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙A2DP的AVRCP连接状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_CHANGE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_avrcp_connect_state_change20)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.AVRCP\_CONNECT\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAYING\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）蓝牙A2DP播放状态改变的普通事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.PLAYING\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙A2DP音频编解码状态更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_CHANGE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_codec_value_change20)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsource.CODEC\_VALUE\_UPDATE"

### COMMON\_EVENT\_USER\_FOREGROUND

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户已被带到前台的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.USER\_FOREGROUND“

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_DISCOVERED(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示发现远程蓝牙设备的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.LOCATION和ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.DISCOVERED"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CLASS\_VALUE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示远程蓝牙设备的蓝牙类别已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.CLASS\_VALUE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_CONNECTED(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示已与远程蓝牙设备建立低级别（ACL）连接的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_STATE\_CHANGE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_acl_state_change20)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.remotedevice.ACL\_CONNECTED"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_DISCONNECTED(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示低电平（ACL）连接已从远程蓝牙设备断开的普通事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_STATE\_CHANGE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_acl_state_change20)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.ACL\_DISCONNECTED"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_NAME\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示远程蓝牙设备的友好名称首次被检索或自上次检索以来被更改的公共事件的操作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.NAME\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）远程蓝牙设备连接状态更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE\_CHANGE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_pair_state_change20)替代。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.PAIR\_STATE"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_BATTERY\_VALUE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示远程蓝牙设备的电池电量首次被检索或自上次检索以来被更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.BATTERY\_VALUE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_SDP\_RESULT(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）远程蓝牙设备SDP状态公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.remotedevice.SDP\_RESULT"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_UUID\_VALUE(deprecated)

PhonePC/2in1TabletTVWearable

远程蓝牙设备UUID连接状态公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.UUID\_VALUE"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_REQ(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示远程蓝牙设备配对请求的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.DISCOVER\_BLUETOOTH

**取值：** "usual.event.bluetooth.remotedevice.PAIRING\_REQ"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_CANCEL(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）取消蓝牙配对的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.remotedevice.PAIRING\_CANCEL"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REQ(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示远程蓝牙设备连接请求的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.remotedevice.CONNECT\_REQ"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REPLY(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示远程蓝牙设备连接请求响应的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.remotedevice.CONNECT\_REPLY"

### COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_CANCEL(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示取消与远程蓝牙设备的连接的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.remotedevice.CONNECT\_CANCEL"

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_CONNECT\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙免提连接状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.handsfreeunit.CONNECT\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AUDIO\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙免提音频状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.handsfreeunit.AUDIO\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_COMMON\_EVENT(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙免提音频网关状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.handsfreeunit.AG\_COMMON\_EVENT"

### COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_CALL\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙免提呼叫状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.handsfreeunit.AG\_CALL\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

表示蓝牙适配器状态已更改的公共事件的操作，例如蓝牙已打开或关闭。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.host.STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISCOVERABLE(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 9 开始支持，从API version 20 开始废弃。

（预留事件，暂未支持）表示用户允许扫描蓝牙请求的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.bluetooth.host.REQ\_DISCOVERABLE"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_ENABLE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户打开蓝牙请求的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.host.REQ\_ENABLE"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISABLE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示用户关闭蓝牙请求的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.host.REQ\_DISABLE"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）设备蓝牙扫描模式更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.host.SCAN\_MODE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_STARTED(deprecated)

PhonePC/2in1TabletTVWearable

设备上已启动蓝牙扫描的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.host.DISCOVERY\_STARTED"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_FINISHED(deprecated)

PhonePC/2in1TabletTVWearable

设备上蓝牙扫描完成的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.host.DISCOVERY\_FINISHED"

### COMMON\_EVENT\_BLUETOOTH\_HOST\_NAME\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

指示设备蓝牙适配器名称已更改的公共事件的操作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.ACCESS\_BLUETOOTH

**取值：** "usual.event.bluetooth.host.NAME\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_CONNECT\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙A2DP连接状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsink.CONNECT\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_PLAYING\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）蓝牙A2DP播放状态改变的普通事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsink.PLAYING\_STATE\_UPDATE"

### COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_AUDIO\_STATE\_UPDATE(deprecated)

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示蓝牙A2DP宿的音频状态已更改的公共事件的动作。

说明

从API version 9 开始支持，从API version 20 开始废弃。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.USE\_BLUETOOTH

**取值：** "usual.event.bluetooth.a2dpsink.AUDIO\_STATE\_UPDATE"

### COMMON\_EVENT\_ABILITY\_ADDED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示已添加能力的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.LISTEN\_BUNDLE\_CHANGE

**取值：** "usual.event.ABILITY\_ADDED"

### COMMON\_EVENT\_ABILITY\_REMOVED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示已删除能力的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.LISTEN\_BUNDLE\_CHANGE

**取值：** "usual.event.ABILITY\_REMOVED"

### COMMON\_EVENT\_ABILITY\_UPDATED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示能力已更新的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.LISTEN\_BUNDLE\_CHANGE

**取值：** "usual.event.ABILITY\_UPDATED"

### COMMON\_EVENT\_LOCATION\_MODE\_STATE\_CHANGED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示系统定位模式已更改的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.location.MODE\_STATE\_CHANGED"

### COMMON\_EVENT\_IVI\_SLEEP

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示表示车辆的车载信息娱乐（IVI）系统正在休眠的常见事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_SLEEP"

### COMMON\_EVENT\_IVI\_PAUSE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示IVI已休眠，并通知应用程序停止播放。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_PAUSE"

### COMMON\_EVENT\_IVI\_STANDBY

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示第三方应用暂停当前工作的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_STANDBY"

### COMMON\_EVENT\_IVI\_LASTMODE\_SAVE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示第三方应用保存其最后一个模式的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_LASTMODE\_SAVE"

### COMMON\_EVENT\_IVI\_VOLTAGE\_ABNORMAL

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示车辆电源系统电压异常的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_VOLTAGE\_ABNORMAL"

### COMMON\_EVENT\_IVI\_HIGH\_TEMPERATURE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示IVI温度过高。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_HIGH\_TEMPERATURE"

### COMMON\_EVENT\_IVI\_EXTREME\_TEMPERATURE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示IVI温度极高。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_EXTREME\_TEMPERATURE"

### COMMON\_EVENT\_IVI\_TEMPERATURE\_ABNORMAL

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示车载系统具有极端温度的常见事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_TEMPERATURE\_ABNORMAL"

### COMMON\_EVENT\_IVI\_VOLTAGE\_RECOVERY

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示车辆电源系统电压恢复正常的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_VOLTAGE\_RECOVERY"

### COMMON\_EVENT\_IVI\_TEMPERATURE\_RECOVERY

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示车载系统温度恢复正常的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_TEMPERATURE\_RECOVERY"

### COMMON\_EVENT\_IVI\_ACTIVE

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示电池服务处于活动状态的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "common.event.IVI\_ACTIVE"

### COMMON\_EVENT\_VISIBLE\_ACCOUNTS\_UPDATED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示账户可见更改的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.GET\_APP\_ACCOUNTS（该权限仅系统应用可申请）

**取值：** "usual.event.data.VISIBLE\_ACCOUNTS\_UPDATED"

### COMMON\_EVENT\_ACCOUNT\_DELETED

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）删除账户的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS（该权限仅系统应用可申请）

**取值：** "usual.event.data.ACCOUNT\_DELETED"

### COMMON\_EVENT\_FOUNDATION\_READY

PhonePC/2in1TabletTVWearable

（预留事件，暂未支持）表示foundation已准备好的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** ohos.permission.RECEIVER\_STARTUP\_COMPLETED（该权限仅系统应用可申请）

**取值：** "usual.event.data.FOUNDATION\_READY"

### COMMON\_EVENT\_SPN\_INFO\_CHANGED

PhonePC/2in1TabletTVWearable

表示spn显示信息已更新的公共事件的动作。

**系统能力：** SystemCapability.Notification.CommonEvent

**订阅者所需权限：** 无

**取值：** "usual.event.SPN\_INFO\_CHANGED"
