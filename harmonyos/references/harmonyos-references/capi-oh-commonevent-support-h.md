---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-support-h
title: oh_commonevent_support.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > oh_commonevent_support.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1fbad9e5b048cd08d05b5d219178c2e604412c995e66b90cf3520929b7b9741a
---

## 概述

PhonePC/2in1TabletTVWearable

提供系统定义的公共事件常量。

**库：** libohcommonevent.so

**引用文件：** <BasicServicesKit/oh\_commonevent\_support.h>

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**相关模块：** [OH\_CommonEvent](capi-oh-commonevent.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 常量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| static const char \* const COMMON\_EVENT\_SHUTDOWN = "usual.event.SHUTDOWN" | 表示设备正在关闭并将继续直至最终关闭的公共事件。  **起始版本：** 12  **系统能力：** SystemCapability.Notification.CommonEvent |
| static const char \* const COMMON\_EVENT\_BATTERY\_CHANGED = "usual.event.BATTERY\_CHANGED" | 表示电池充电状态、电平和其他信息发生变化的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_BATTERY\_LOW = "usual.event.BATTERY\_LOW" | 表示电池电量低的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_BATTERY\_OKAY = "usual.event.BATTERY\_OKAY" | 表示电池退出低电平状态的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_POWER\_CONNECTED = "usual.event.POWER\_CONNECTED" | 表示设备连接到外部电源的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_POWER\_DISCONNECTED = "usual.event.POWER\_DISCONNECTED" | 表示设备与外部电源断开的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_SCREEN\_OFF = "usual.event.SCREEN\_OFF" | 表示设备屏幕关闭且设备处于睡眠状态的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_SCREEN\_ON = "usual.event.SCREEN\_ON" | 表示设备屏幕打开且设备处于交互状态的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_ENTER\_HIBERNATE = "usual.event.ENTER\_HIBERNATE" | 表示设备即将进入休眠模式的公共事件的动作。  **起始版本：** 15 |
| static const char \* const COMMON\_EVENT\_EXIT\_HIBERNATE = "usual.event.EXIT\_HIBERNATE" | 表示设备退出休眠模式的公共事件的动作。  **起始版本：** 15 |
| static const char \* const COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED = "usual.event.THERMAL\_LEVEL\_CHANGED" | 表示设备热状态的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_TIME\_TICK = "usual.event.TIME\_TICK" | 表示系统时间更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_TIME\_CHANGED = "usual.event.TIME\_CHANGED" | 表示设置系统时间的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_TIMEZONE\_CHANGED = "usual.event.TIMEZONE\_CHANGED" | 表示系统时区更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_ADDED = "usual.event.PACKAGE\_ADDED" | 表示设备上已安装新应用包的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_REMOVED = "usual.event.PACKAGE\_REMOVED" | 表示已从设备卸载已安装的应用程序，但应用程序数据保留的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_BUNDLE\_REMOVED = "usual.event.BUNDLE\_REMOVED" | 表示已从设备中卸载已安装的捆绑包，但应用程序数据仍保留的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED = "usual.event.PACKAGE\_FULLY\_REMOVED" | 表示已从设备中完全卸载已安装的应用程序（包括应用程序数据和代码）的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_CHANGED = "usual.event.PACKAGE\_CHANGED" | 表示应用包已更改的公共事件（例如，包中的组件已启用或禁用）。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_RESTARTED = "usual.event.PACKAGE\_RESTARTED" | 表示用户重启应用包并杀死其所有进程的普通事件的动作。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED = "usual.event.PACKAGE\_DATA\_CLEARED" | 表示用户清除应用包数据的公共事件的动作。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED = "usual.event.PACKAGE\_CACHE\_CLEARED" | 表示用户清除应用包缓存数据的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_PACKAGES\_SUSPENDED = "usual.event.PACKAGES\_SUSPENDED" | 表示应用包已挂起的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED = "usual.event.MY\_PACKAGE\_SUSPENDED" | 表示应用包被挂起的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED = "usual.event.MY\_PACKAGE\_UNSUSPENDED" | 表示应用包未挂起的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_LOCALE\_CHANGED = "usual.event.LOCALE\_CHANGED" | 表示设备区域设置已更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE = "usual.event.MANAGE\_PACKAGE\_STORAGE" | 表示设备存储空间不足的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_USER\_UNLOCKED = "usual.event.USER\_UNLOCKED" | 表示设备重启后解锁时，当前用户的凭据加密存储已解锁的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOUT = "common.event.DISTRIBUTED\_ACCOUNT\_LOGOUT" | 表示分布式账号登出成功的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID = "common.event.DISTRIBUTED\_ACCOUNT\_TOKEN\_INVALID" | 表示分布式账号token令牌无效的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_DISTRIBUTED\_ACCOUNT\_LOGOFF = "common.event.DISTRIBUTED\_ACCOUNT\_LOGOFF" | 表示分布式账号注销的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_POWER\_STATE = "usual.event.wifi.POWER\_STATE" | 表示Wi-Fi状态公共事件，如启用和禁用。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_SCAN\_FINISHED = "usual.event.wifi.SCAN\_FINISHED" | 表示Wi-Fi接入点已被扫描并证明可用的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_RSSI\_VALUE = "usual.event.wifi.RSSI\_VALUE" | 表示Wi-Fi信号强度（RSSI）改变的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_CONN\_STATE = "usual.event.wifi.CONN\_STATE" | 表示Wi-Fi连接状态发生改变的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE = "usual.event.wifi.HOTSPOT\_STATE" | 表示Wi-Fi热点状态的公共事件，如启用或禁用。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN = "usual.event.wifi.WIFI\_HS\_STA\_JOIN" | 表示客户端加入当前设备Wi-Fi热点的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE = "usual.event.wifi.WIFI\_HS\_STA\_LEAVE" | 表示客户端已断开与当前设备Wi-Fi热点的连接的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE = "usual.event.wifi.mplink.STATE\_CHANGE" | 表示MPLink（增强Wi-Fi功能）状态已更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE = "usual.event.wifi.p2p.CONN\_STATE\_CHANGE" | 表示Wi-Fi P2P连接状态改变的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED = "usual.event.wifi.p2p.STATE\_CHANGE" | 表示Wi-Fi P2P状态公共事件，如启用和禁用。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED = "usual.event.wifi.p2p.DEVICES\_CHANGE" | 表示Wi-Fi P2P对等体状态变化的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED = "usual.event.wifi.p2p.PEER\_DISCOVERY\_STATE\_CHANGE" | 表示Wi-Fi P2P发现状态变化的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED = "usual.event.wifi.p2p.CURRENT\_DEVICE\_CHANGE" | 表示Wi-Fi P2P当前设备状态变化的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED = "usual.event.wifi.p2p.GROUP\_STATE\_CHANGED" | 表示Wi-Fi P2P群组信息已更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED = "usual.event.nfc.action.ADAPTER\_STATE\_CHANGED" | 表示设备NFC状态已更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED = "usual.event.nfc.action.RF\_FIELD\_ON\_DETECTED" | 表示检测到NFC场强进入的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED = "usual.event.nfc.action.RF\_FIELD\_OFF\_DETECTED" | 表示检测到NFC场强离开的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_DISCHARGING = "usual.event.DISCHARGING" | 表示系统停止为电池充电的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_CHARGING = "usual.event.CHARGING" | 表示系统开始为电池充电的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED = "usual.event.DEVICE\_IDLE\_MODE\_CHANGED" | 表示系统待机空闲模式已更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_CHARGE\_IDLE\_MODE\_CHANGED = "usual.event.CHARGE\_IDLE\_MODE\_CHANGED" | 表示设备进入充电空闲模式的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED = "usual.event.POWER\_SAVE\_MODE\_CHANGED" | 表示系统节能模式更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_USB\_STATE = "usual.event.hardware.usb.action.USB\_STATE" | 表示USB设备状态发生变化的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_USB\_PORT\_CHANGED = "usual.event.hardware.usb.action.USB\_PORT\_CHANGED" | 表示用户设备的USB端口状态发生改变的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_USB\_DEVICE\_ATTACHED = "usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED" | 当用户设备作为USB主机时，USB设备已挂载的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_USB\_DEVICE\_DETACHED = "usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED" | 当用户设备作为USB主机时，USB设备被卸载的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED = "usual.event.AIRPLANE\_MODE" | 表示设备飞行模式已更改的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_SPLIT\_SCREEN = "common.event.SPLIT\_SCREEN" | 表示分屏的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_QUICK\_FIX\_APPLY\_RESULT = "usual.event.QUICK\_FIX\_APPLY\_RESULT" | 表示快速修复应用的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_QUICK\_FIX\_REVOKE\_RESULT = "usual.event.QUICK\_FIX\_REVOKE\_RESULT" | 表示撤销快速修复的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_USER\_INFO\_UPDATED = "usual.event.USER\_INFO\_UPDATED" | 表示用户信息已更新的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_SIM\_STATE\_CHANGED = "usual.event.SIM\_STATE\_CHANGED" | 表示SIM卡状态更新的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_CALL\_STATE\_CHANGED = "usual.event.CALL\_STATE\_CHANGED" | 表示呼叫状态更新的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_NETWORK\_STATE\_CHANGED = "usual.event.NETWORK\_STATE\_CHANGED" | 表示网络状态更新的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_SIGNAL\_INFO\_CHANGED = "usual.event.SIGNAL\_INFO\_CHANGED" | 表示信号信息更新的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_SCREEN\_UNLOCKED = "usual.event.SCREEN\_UNLOCKED" | 表示屏幕解锁的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_SCREEN\_LOCKED = "usual.event.SCREEN\_LOCKED" | 表示屏幕锁定的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_HTTP\_PROXY\_CHANGE = "usual.event.HTTP\_PROXY\_CHANGE" | 表示HTTP代理的配置信息发生变化的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_CONNECTIVITY\_CHANGE = "usual.event.CONNECTIVITY\_CHANGE" | 表示网络连接状态变化的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_MINORSMODE\_ON = "usual.event.MINORSMODE\_ON" | 表示未成年人模式开启的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_MINORSMODE\_OFF = "usual.event.MINORSMODE\_OFF" | 表示未成年人模式关闭的公共事件。  **起始版本：** 12 |
| static const char \* const COMMON\_EVENT\_MANAGED\_BROWSER\_POLICY\_CHANGED = "usual.event.MANAGED\_BROWSER\_POLICY\_CHANGED" | 表示浏览器托管策略已更改。  **起始版本：** 15 |
| static const char\* const COMMON\_EVENT\_TABLET\_MODE\_CHANGED = "usual.event.TABLET\_MODE\_CHANGED" | 表示可感知支架开合的设备，其支架开合状态变化的公共事件。  **起始版本：** 23 |
| static const char\* const COMMON\_EVENT\_LID\_STATE\_CHANGED = "usual.event.LID\_STATE\_CHANGED" | 表示可感知开合盖子的设备，其开合盖状态变化的公共事件。  **起始版本：** 23 |
