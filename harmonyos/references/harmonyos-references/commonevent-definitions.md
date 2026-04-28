---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commonevent-definitions
title: 系统公共事件定义(待停用)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > 系统公共事件定义(待停用)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:42+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b1ade9dc005ebcba170ee266b62e5d69ebd97711da00bf639f55fd66c1db2722
---

本文档提供系统所定义的公共事件类型的索引。

公共事件类型定义在[ohos.commonEvent模块的Support枚举](js-apis-commonevent.md#support)中。

**系统能力：** SystemCapability.Notification.CommonEvent

* COMMON\_EVENT\_BOOT\_COMPLETED(deprecated) 提示用户已完成引导并加载系统。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用COMMON\_EVENT\_BOOT\_COMPLETED替代。

  + 值：usual.event.BOOT\_COMPLETED
  + 订阅者所需权限：ohos.permission.RECEIVER\_STARTUP\_COMPLETED（该权限仅系统应用可申请）
* COMMON\_EVENT\_LOCKED\_BOOT\_COMPLETED(deprecated) （预留事件，暂未支持）提示用户已完成引导，系统已加载，但屏幕仍锁定。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_LOCKED\_BOOT\_COMPLETED](commoneventmanager-definitions.md#common_event_locked_boot_completed)替代。

  + 值：usual.event.LOCKED\_BOOT\_COMPLETED
  + 订阅者所需权限：无
* COMMON\_EVENT\_SHUTDOWN(deprecated) 提示设备正在关闭并将继续直至最终关闭。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_SHUTDOWN](commoneventmanager-definitions.md#common_event_shutdown)替代。

  + 值：usual.event.SHUTDOWN
  + 订阅者所需权限：无
* COMMON\_EVENT\_BATTERY\_CHANGED(deprecated) 提示电池充电状态、电量和其他信息发生变化。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BATTERY\_CHANGED](commoneventmanager-definitions.md#common_event_battery_changed)替代。

  + 值：usual.event.BATTERY\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_BATTERY\_LOW(deprecated) 提示电池电量低。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BATTERY\_LOW](commoneventmanager-definitions.md#common_event_battery_low)替代。

  + 值：usual.event.BATTERY\_LOW
  + 订阅者所需权限：无
* COMMON\_EVENT\_BATTERY\_OKAY(deprecated) 提示电池退出低电量状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BATTERY\_OKAY](commoneventmanager-definitions.md#common_event_battery_okay)替代。

  + 值：usual.event.BATTERY\_OKAY
  + 订阅者所需权限：无
* COMMON\_EVENT\_POWER\_CONNECTED(deprecated) 提示设备连接到外部电源。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_POWER\_CONNECTED](commoneventmanager-definitions.md#common_event_power_connected)替代。

  + 值：usual.event.POWER\_CONNECTED
  + 订阅者所需权限：无
* COMMON\_EVENT\_POWER\_DISCONNECTED(deprecated) 提示设备与外部电源断开。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_POWER\_DISCONNECTED](commoneventmanager-definitions.md#common_event_power_disconnected)替代。

  + 值：usual.event.POWER\_DISCONNECTED
  + 订阅者所需权限：无
* COMMON\_EVENT\_SCREEN\_OFF(deprecated) 提示设备屏幕关闭且设备处于睡眠状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_SCREEN\_OFF](commoneventmanager-definitions.md#common_event_screen_off)替代。

  + 值：usual.event.SCREEN\_OFF
  + 订阅者所需权限：无
* COMMON\_EVENT\_SCREEN\_ON(deprecated) 提示设备屏幕打开且设备处于交互状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_SCREEN\_ON](commoneventmanager-definitions.md#common_event_screen_on)替代。

  + 值：usual.event.SCREEN\_ON
  + 订阅者所需权限：无
* COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED(deprecated) 提示设备热状态（温度等级）发生变化。

  说明

  从API version 8 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_THERMAL\_LEVEL\_CHANGED](commoneventmanager-definitions.md#common_event_thermal_level_changed)替代。

  + 值：usual.event.THERMAL\_LEVEL\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_USER\_PRESENT(deprecated) （预留事件，暂未支持）提示用户解锁了设备。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_PRESENT](commoneventmanager-definitions.md#common_event_user_presentdeprecated)替代。

  + 值：usual.event.USER\_PRESENT
  + 订阅者所需权限：无
* COMMON\_EVENT\_TIME\_TICK(deprecated) 提示系统时间发生更改（指时间正常流逝）。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_TIME\_TICK](commoneventmanager-definitions.md#common_event_time_tick)替代。

  + 值：usual.event.TIME\_TICK
  + 订阅者所需权限：无
* COMMON\_EVENT\_TIME\_CHANGED(deprecated) 提示系统时间被重新设置。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_TIME\_CHANGED](commoneventmanager-definitions.md#common_event_time_changed)替代。

  + 值：usual.event.TIME\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_DATE\_CHANGED(deprecated) （预留事件，暂未支持）提示系统日期已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DATE\_CHANGED](commoneventmanager-definitions.md#common_event_date_changed)替代。

  + 值：usual.event.DATE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_TIMEZONE\_CHANGED(deprecated) 提示系统时区发生变更。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_TIMEZONE\_CHANGED](commoneventmanager-definitions.md#common_event_timezone_changed)替代。

  + 值：usual.event.TIMEZONE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_CLOSE\_SYSTEM\_DIALOGS(deprecated) （预留事件，暂未支持）提示用户关闭临时系统对话框。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_CLOSE\_SYSTEM\_DIALOGS](commoneventmanager-definitions.md#common_event_close_system_dialogs)替代。

  + 值：usual.event.CLOSE\_SYSTEM\_DIALOGS
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_ADDED(deprecated) 提示设备上已安装新应用程序包。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_ADDED](commoneventmanager-definitions.md#common_event_package_added)替代。

  + 值：usual.event.PACKAGE\_ADDED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_REPLACED(deprecated) （预留事件，暂未支持）提示设备上已安装的旧版本应用程序已被新版本所替换。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_REPLACED](commoneventmanager-definitions.md#common_event_package_replaced)替代。

  + 值：usual.event.PACKAGE\_REPLACED
  + 订阅者所需权限：无
* COMMON\_EVENT\_MY\_PACKAGE\_REPLACED(deprecated) （预留事件，暂未支持）提示应用程序包的新版本已取代前一个版本。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_MY\_PACKAGE\_REPLACED](commoneventmanager-definitions.md#common_event_my_package_replaced)替代。

  + 值：usual.event.MY\_PACKAGE\_REPLACED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_REMOVED(deprecated) 提示已安装的应用程序已从设备卸载，但应用程序数据得到保留的。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_REMOVED](commoneventmanager-definitions.md#common_event_package_removed)替代。

  + 值：usual.event.PACKAGE\_REMOVED
  + 订阅者所需权限：无
* COMMON\_EVENT\_BUNDLE\_REMOVED(deprecated) （预留事件，暂未支持）提示已从设备中卸载已安装应用程序的附加包，但应用程序数据得到保留。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BUNDLE\_REMOVED](commoneventmanager-definitions.md#common_event_bundle_removed)替代。

  + 值：usual.event.BUNDLE\_REMOVED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED(deprecated) （预留事件，暂未支持）提示已从设备中完全卸载已安装的应用程序（包括应用程序数据和代码）。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_FULLY\_REMOVED](commoneventmanager-definitions.md#common_event_package_fully_removed)替代。

  + 值：usual.event.PACKAGE\_FULLY\_REMOVED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_CHANGED(deprecated) 提示应用程序包已发生更改（例如，包中的组件已启用或禁用）。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_CHANGED](commoneventmanager-definitions.md#common_event_package_changed)替代。

  + 值：usual.event.PACKAGE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_RESTARTED(deprecated) 提示用户终止了应用程序的所有进程并重启应用程序。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_RESTARTED](commoneventmanager-definitions.md#common_event_package_restarted)替代。

  + 值：usual.event.PACKAGE\_RESTARTED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED(deprecated) 提示用户清除了应用包数据。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED](commoneventmanager-definitions.md#common_event_package_data_cleared)替代。

  + 值：usual.event.PACKAGE\_DATA\_CLEARED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGES\_SUSPENDED(deprecated) （预留事件，暂未支持）提示应用程序已挂起。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGES\_SUSPENDED](commoneventmanager-definitions.md#common_event_packages_suspended)替代。

  + 值：usual.event.PACKAGES\_SUSPENDED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGES\_UNSUSPENDED(deprecated) （预留事件，暂未支持）提示应用HAP包未挂起（从挂起状态恢复）。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGES\_UNSUSPENDED](commoneventmanager-definitions.md#common_event_packages_unsuspended)替代。

  + 值：usual.event.PACKAGES\_UNSUSPENDED
  + 订阅者所需权限：无
* COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED(deprecated) 提示应用HAP包被挂起的。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_MY\_PACKAGE\_SUSPENDED](commoneventmanager-definitions.md#common_event_my_package_suspended)替代。

  + 值：usual.event.MY\_PACKAGE\_SUSPENDED
  + 订阅者所需权限：无
* COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED(deprecated) 提示应用包未挂起。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_MY\_PACKAGE\_UNSUSPENDED](commoneventmanager-definitions.md#common_event_my_package_unsuspended)替代。

  + 值：usual.event.MY\_PACKAGE\_UNSUSPENDED
  + 订阅者所需权限：无
* COMMON\_EVENT\_UID\_REMOVED(deprecated) （预留事件，暂未支持）提示用户ID已从系统中删除。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_UID\_REMOVED](commoneventmanager-definitions.md#common_event_uid_removed)替代。

  + 值：usual.event.UID\_REMOVED
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_FIRST\_LAUNCH(deprecated) （预留事件，暂未支持）提示首次启动已安装的应用程序。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_FIRST\_LAUNCH](commoneventmanager-definitions.md#common_event_package_first_launch)替代。

  + 值：usual.event.PACKAGE\_FIRST\_LAUNCH
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_NEEDS\_VERIFICATION(deprecated) （预留事件，暂未支持）提示应用需要系统校验。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_NEEDS\_VERIFICATION](commoneventmanager-definitions.md#common_event_package_needs_verification)替代。

  + 值：usual.event.PACKAGE\_NEEDS\_VERIFICATION
  + 订阅者所需权限：无
* COMMON\_EVENT\_PACKAGE\_VERIFIED(deprecated) （预留事件，暂未支持）提示应用已被系统校验。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_PACKAGE\_VERIFIED](commoneventmanager-definitions.md#common_event_package_verified)替代。

  + 值：usual.event.PACKAGE\_VERIFIED
  + 订阅者所需权限：无
* COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_AVAILABLE(deprecated) （预留事件，暂未支持）提示安装在外部存储上的应用程序对系统可用。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_AVAILABLE](commoneventmanager-definitions.md#common_event_external_applications_available)替代。

  + 值：usual.event.EXTERNAL\_APPLICATIONS\_AVAILABLE
  + 订阅者所需权限：无
* COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_UNAVAILABLE(deprecated) （预留事件，暂未支持）提示安装在外部存储上的应用程序对系统不可用。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_EXTERNAL\_APPLICATIONS\_UNAVAILABLE](commoneventmanager-definitions.md#common_event_external_applications_unavailable)替代。

  + 值：usual.event.EXTERNAL\_APPLICATIONS\_UNAVAILABLE
  + 订阅者所需权限：无
* COMMON\_EVENT\_CONFIGURATION\_CHANGED(deprecated) （预留事件，暂未支持）提示设备状态（例如，方向、区域设置等）已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_CONFIGURATION\_CHANGED](commoneventmanager-definitions.md#common_event_configuration_changed)替代。

  + 值：usual.event.CONFIGURATION\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_LOCALE\_CHANGED(deprecated) （预留事件，暂未支持）提示设备区域设置已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_LOCALE\_CHANGED](commoneventmanager-definitions.md#common_event_locale_changed)替代。

  + 值：usual.event.LOCALE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE(deprecated) （预留事件，暂未支持）提示设备存储空间不足。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_MANAGE\_PACKAGE\_STORAGE](commoneventmanager-definitions.md#common_event_manage_package_storage)替代。

  + 值：usual.event.MANAGE\_PACKAGE\_STORAGE
  + 订阅者所需权限：无
* COMMON\_EVENT\_DRIVE\_MODE(deprecated) （预留事件，暂未支持）提示系统处于驾驶模式。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DRIVE\_MODE](commoneventmanager-definitions.md#common_event_drive_mode)替代。

  + 值：common.event.DRIVE\_MODE
  + 订阅者所需权限：无
* COMMON\_EVENT\_HOME\_MODE(deprecated) （预留事件，暂未支持）提示系统处于HOME模式。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_HOME\_MODE](commoneventmanager-definitions.md#common_event_home_mode)替代。

  + 值：common.event.HOME\_MODE
  + 订阅者所需权限：无
* COMMON\_EVENT\_OFFICE\_MODE(deprecated) （预留事件，暂未支持）提示系统处于办公模式。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_OFFICE\_MODE](commoneventmanager-definitions.md#common_event_office_mode)替代。

  + 值：common.event.OFFICE\_MODE
  + 订阅者所需权限：无
* COMMON\_EVENT\_USER\_STARTED(deprecated) （预留事件，暂未支持）提示用户已启动。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_STARTED](commoneventmanager-definitions.md#common_event_user_started)替代。

  + 值：usual.event.USER\_STARTED
  + 订阅者所需权限：无
* COMMON\_EVENT\_USER\_BACKGROUND(deprecated) （预留事件，暂未支持）提示用户已被带到后台。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_BACKGROUND](commoneventmanager-definitions.md#common_event_user_background)替代。

  + 值：usual.event.USER\_BACKGROUND
  + 订阅者所需权限：无
* COMMON\_EVENT\_USER\_FOREGROUND(deprecated) （预留事件，暂未支持）提示用户已被带到前台。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_FOREGROUND](commoneventmanager-definitions.md#common_event_user_foreground)替代。

  + 值：usual.event.USER\_FOREGROUND
  + 订阅者所需权限：无
* COMMON\_EVENT\_USER\_SWITCHED(deprecated) 提示用户正在切换。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用COMMON\_EVENT\_USER\_SWITCHED替代。

  + 值：usual.event.USER\_SWITCHED
  + 订阅者所需权限：ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。
* COMMON\_EVENT\_USER\_STARTING(deprecated) （预留事件，暂未支持）提示用户正在启动。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_STARTING](commoneventmanager-definitions.md#common_event_user_starting)替代。

  + 值：usual.event.USER\_STARTING
  + 订阅者所需权限：ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。
* COMMON\_EVENT\_USER\_UNLOCKED(deprecated) （预留事件，暂未支持）在重启后解锁时，提示当前用户的凭据加密存储已解锁。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_UNLOCKED](commoneventmanager-definitions.md#common_event_user_unlocked)替代。

  + 值：usual.event.USER\_UNLOCKED
  + 订阅者所需权限：无
* COMMON\_EVENT\_USER\_STOPPING(deprecated) （预留事件，暂未支持）提示要停止用户。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_STOPPING](commoneventmanager-definitions.md#common_event_user_stopping)替代。

  + 值：usual.event.USER\_STOPPING
  + 订阅者所需权限：ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。
* COMMON\_EVENT\_USER\_STOPPED(deprecated) （预留事件，暂未支持）提示用户已停止。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USER\_STOPPED](commoneventmanager-definitions.md#common_event_user_stopped)替代。

  + 值：usual.event.USER\_STOPPED
  + 订阅者所需权限：无
* COMMON\_EVENT\_WIFI\_POWER\_STATE(deprecated) 提示Wi-Fi功能状态的变更，如启用或禁用。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_POWER\_STATE](commoneventmanager-definitions.md#common_event_wifi_power_state)替代。

  + 值：usual.event.wifi.POWER\_STATE
  + 订阅者所需权限：无
* COMMON\_EVENT\_WIFI\_SCAN\_FINISHED(deprecated) 提示Wi-Fi接入点已被扫描并证明可用。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_SCAN\_FINISHED](commoneventmanager-definitions.md#common_event_wifi_scan_finished)替代。

  + 值：usual.event.wifi.SCAN\_FINISHED
  + 订阅者所需权限：ohos.permission.LOCATION
* COMMON\_EVENT\_WIFI\_RSSI\_VALUE(deprecated) 提示Wi-Fi信号强度（RSSI）改变。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_RSSI\_VALUE](commoneventmanager-definitions.md#common_event_wifi_rssi_value)替代。

  + 值：usual.event.wifi.RSSI\_VALUE
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_WIFI\_CONN\_STATE(deprecated) 提示Wi-Fi连接状态发生改变。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_CONN\_STATE](commoneventmanager-definitions.md#common_event_wifi_conn_state)替代。

  + 值：usual.event.wifi.CONN\_STATE
  + 订阅者所需权限：无
* COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE(deprecated) 提示Wi-Fi热点功能状态的变更，如启用或禁用。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_HOTSPOT\_STATE](commoneventmanager-definitions.md#common_event_wifi_hotspot_state)替代。

  + 值：usual.event.wifi.HOTSPOT\_STATE
  + 订阅者所需权限：无
* COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN(deprecated) 提示有客户端加入当前设备Wi-Fi热点。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_AP\_STA\_JOIN](commoneventmanager-definitions.md#common_event_wifi_ap_sta_join)替代。

  + 值：usual.event.wifi.WIFI\_HS\_STA\_JOIN
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE(deprecated) 提示客户端已断开与当前设备Wi-Fi热点的连接。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_AP\_STA\_LEAVE](commoneventmanager-definitions.md#common_event_wifi_ap_sta_leave)替代。

  + 值：usual.event.wifi.WIFI\_HS\_STA\_LEAVE
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE(deprecated) 提示MPLink（增强Wi-Fi功能）状态已更改（暂不支持）。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_MPLINK\_STATE\_CHANGE](commoneventmanager-definitions.md#common_event_wifi_mplink_state_change)替代。

  + 值：usual.event.wifi.mplink.STATE\_CHANGE
  + 订阅者所需权限：无
* COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE(deprecated) 提示Wi-Fi P2P连接状态改变。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_P2P\_CONN\_STATE](commoneventmanager-definitions.md#common_event_wifi_p2p_conn_state)替代。

  + 值：usual.event.wifi.p2p.CONN\_STATE\_CHANGE
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO and ohos.permission.LOCATION
* COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED(deprecated) 提示Wi-Fi P2P状态发生变更，如启用和禁用。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_P2P\_STATE\_CHANGED](commoneventmanager-definitions.md#common_event_wifi_p2p_state_changed)替代。

  + 值：usual.event.wifi.p2p.STATE\_CHANGE
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED(deprecated) 提示Wi-Fi P2P对等体状态变化。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_P2P\_PEERS\_STATE\_CHANGED](commoneventmanager-definitions.md#common_event_wifi_p2p_peers_state_changed)替代。

  + 值：usual.event.wifi.p2p.DEVICES\_CHANGE
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED(deprecated) 提示Wi-Fi P2P发现状态变化。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_P2P\_PEERS\_DISCOVERY\_STATE\_CHANGED](commoneventmanager-definitions.md#common_event_wifi_p2p_peers_discovery_state_changed)替代。

  + 值：usual.event.wifi.p2p.PEER\_DISCOVERY\_STATE\_CHANGE
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED(deprecated) 提示Wi-Fi P2P当前设备状态变化。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_P2P\_CURRENT\_DEVICE\_STATE\_CHANGED](commoneventmanager-definitions.md#common_event_wifi_p2p_current_device_state_changed)替代。

  + 值：usual.event.wifi.p2p.CURRENT\_DEVICE\_CHANGE
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED(deprecated) 提示Wi-Fi P2P群组信息已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_WIFI\_P2P\_GROUP\_STATE\_CHANGED](commoneventmanager-definitions.md#common_event_wifi_p2p_group_state_changed)替代。

  + 值：usual.event.wifi.p2p.GROUP\_STATE\_CHANGED
  + 订阅者所需权限：ohos.permission.GET\_WIFI\_INFO
* COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙免提通信连接状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CONNECT\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_handsfree_ag_connect_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.handsfree.ag.CONNECT\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CURRENT\_DEVICE\_UPDATE(deprecated) （预留事件，暂未支持）提示连接到具有蓝牙免提功能的设备处于活动状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_CURRENT\_DEVICE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_handsfree_ag_current_device_updatedeprecated)替代。

  + 值：usual.event.bluetooth.handsfree.ag.CURRENT\_DEVICE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_AUDIO\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP连接状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREE\_AG\_AUDIO\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_handsfree_ag_audio_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.handsfree.ag.AUDIO\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP连接状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CONNECT\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_connect_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsource.CONNECT\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CURRENT\_DEVICE\_UPDATE(deprecated) （预留事件，暂未支持）提示使用蓝牙A2DP连接的设备处于活动状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CURRENT\_DEVICE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_current_device_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsource.CURRENT\_DEVICE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAYING\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP播放状态发生改变。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_PLAYING\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_playing_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsource.PLAYING\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP的AVRCP连接状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_AVRCP\_CONNECT\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_avrcp_connect_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsource.AVRCP\_CONNECT\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP音频编解码状态更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSOURCE\_CODEC\_VALUE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsource_codec_value_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsource.CODEC\_VALUE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_DISCOVERED(deprecated) （预留事件，暂未支持）提示发现远程蓝牙设备。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_DISCOVERED](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_discovereddeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.DISCOVERED
  + 订阅者所需权限：ohos.permission.LOCATION and ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CLASS\_VALUE\_UPDATE(deprecated) （预留事件，暂未支持）提示远程蓝牙设备的蓝牙类别已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CLASS\_VALUE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_class_value_updatedeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.CLASS\_VALUE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_CONNECTED(deprecated) （预留事件，暂未支持）提示已与远程蓝牙设备建立低级别（ACL）连接。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_CONNECTED](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_acl_connecteddeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.ACL\_CONNECTED
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_DISCONNECTED(deprecated) （预留事件，暂未支持）提示低级别（ACL）连接已从远程蓝牙设备断开。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_ACL\_DISCONNECTED](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_acl_disconnecteddeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.ACL\_DISCONNECTED
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_NAME\_UPDATE(deprecated) （预留事件，暂未支持）提示远程蓝牙设备的友好名称首次被检索或自上次检索以来被更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_NAME\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_name_updatedeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.NAME\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE(deprecated) （预留事件，暂未支持）提示远程蓝牙设备连接状态更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIR\_STATE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_pair_statedeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.PAIR\_STATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_BATTERY\_VALUE\_UPDATE(deprecated) （预留事件，暂未支持）提示远程蓝牙设备的电池电量首次被检索或自上次检索以来被更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_BATTERY\_VALUE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_battery_value_updatedeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.BATTERY\_VALUE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_SDP\_RESULT(deprecated) （预留事件，暂未支持）提示远程蓝牙设备SDP状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_SDP\_RESULT](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_sdp_resultdeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.SDP\_RESULT
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_UUID\_VALUE(deprecated) （预留事件，暂未支持）提示远程蓝牙设备UUID连接状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_UUID\_VALUE](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_uuid_valuedeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.UUID\_VALUE
  + 订阅者所需权限：ohos.permission.DISCOVER\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_REQ(deprecated) （预留事件，暂未支持）提示远程蓝牙设备配对请求。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_REQ](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_pairing_reqdeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.PAIRING\_REQ
  + 订阅者所需权限：ohos.permission.DISCOVER\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_CANCEL(deprecated) （预留事件，暂未支持）提示取消蓝牙配对。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_PAIRING\_CANCEL](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_pairing_canceldeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.PAIRING\_CANCEL
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REQ(deprecated) （预留事件，暂未支持）提示远程蓝牙设备连接请求。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REQ](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_connect_reqdeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.CONNECT\_REQ
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REPLY(deprecated) （预留事件，暂未支持）提示远程蓝牙设备连接请求响应。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_REPLY](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_connect_replydeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.CONNECT\_REPLY
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_CANCEL(deprecated) （预留事件，暂未支持）提示取消与远程蓝牙设备的连接。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_REMOTEDEVICE\_CONNECT\_CANCEL](commoneventmanager-definitions.md#common_event_bluetooth_remotedevice_connect_canceldeprecated)替代。

  + 值：usual.event.bluetooth.remotedevice.CONNECT\_CANCEL
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_CONNECT\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙免提连接状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_CONNECT\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_handsfreeunit_connect_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.handsfreeunit.CONNECT\_STATE\_UPDATE
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AUDIO\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙免提音频状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AUDIO\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_handsfreeunit_audio_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.handsfreeunit.AUDIO\_STATE\_UPDATE
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_COMMON\_EVENT(deprecated) （预留事件，暂未支持）提示蓝牙免提音频网关状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_COMMON\_EVENT](commoneventmanager-definitions.md#common_event_bluetooth_handsfreeunit_ag_common_eventdeprecated)替代。

  + 值：usual.event.bluetooth.handsfreeunit.AG\_COMMON\_EVENT
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_CALL\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙免提呼叫状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HANDSFREEUNIT\_AG\_CALL\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_handsfreeunit_ag_call_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.handsfreeunit.AG\_CALL\_STATE\_UPDATE
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_HOST\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙适配器状态已更改，例如蓝牙已打开或关闭。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_host_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.host.STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISCOVERABLE(deprecated) （预留事件，暂未支持）提示用户允许扫描蓝牙请求。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISCOVERABLE](commoneventmanager-definitions.md#common_event_bluetooth_host_req_discoverabledeprecated)替代。

  + 值：usual.event.bluetooth.host.REQ\_DISCOVERABLE
  + 订阅者所需权限：无
* COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_ENABLE(deprecated) （预留事件，暂未支持）提示用户打开蓝牙请求。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_ENABLE](commoneventmanager-definitions.md#common_event_bluetooth_host_req_enabledeprecated)替代。

  + 值：usual.event.bluetooth.host.REQ\_ENABLE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISABLE(deprecated) （预留事件，暂未支持）提示用户关闭蓝牙请求。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_REQ\_DISABLE](commoneventmanager-definitions.md#common_event_bluetooth_host_req_disabledeprecated)替代。

  + 值：usual.event.bluetooth.host.REQ\_DISABLE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_UPDATE(deprecated) （预留事件，暂未支持）提示设备蓝牙扫描模式更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_SCAN\_MODE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_host_scan_mode_updatedeprecated)替代。

  + 值：usual.event.bluetooth.host.SCAN\_MODE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_STARTED(deprecated) （预留事件，暂未支持）提示设备上已启动蓝牙扫描。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_STARTED](commoneventmanager-definitions.md#common_event_bluetooth_host_discovery_starteddeprecated)替代。

  + 值：usual.event.bluetooth.host.DISCOVERY\_STARTED
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_FINISHED(deprecated) （预留事件，暂未支持）提示设备上蓝牙扫描完成。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_DISCOVERY\_FINISHED](commoneventmanager-definitions.md#common_event_bluetooth_host_discovery_finisheddeprecated)替代。

  + 值：usual.event.bluetooth.host.DISCOVERY\_FINISHED
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_HOST\_NAME\_UPDATE(deprecated) （预留事件，暂未支持）提示设备蓝牙适配器名称已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_HOST\_NAME\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_host_name_updatedeprecated)替代。

  + 值：usual.event.bluetooth.host.NAME\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_CONNECT\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP宿的连接状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_CONNECT\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsink_connect_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsink.CONNECT\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_PLAYING\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP宿的播放状态发生改变。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_PLAYING\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsink_playing_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsink.PLAYING\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_AUDIO\_STATE\_UPDATE(deprecated) （预留事件，暂未支持）提示蓝牙A2DP宿的音频状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_BLUETOOTH\_A2DPSINK\_AUDIO\_STATE\_UPDATE](commoneventmanager-definitions.md#common_event_bluetooth_a2dpsink_audio_state_updatedeprecated)替代。

  + 值：usual.event.bluetooth.a2dpsink.AUDIO\_STATE\_UPDATE
  + 订阅者所需权限：ohos.permission.USE\_BLUETOOTH
* COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED(deprecated) （预留事件，暂未支持）提示设备NFC适配器状态已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_NFC\_ACTION\_ADAPTER\_STATE\_CHANGED](commoneventmanager-definitions.md#common_event_nfc_action_adapter_state_changed)替代。

  + 值：usual.event.nfc.action.ADAPTER\_STATE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED(deprecated) （预留事件，暂未支持）提示检测到NFC设备RF字段处于使能状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_ON\_DETECTED](commoneventmanager-definitions.md#common_event_nfc_action_rf_field_on_detected)替代。

  + 值：usual.event.nfc.action.RF\_FIELD\_ON\_DETECTED
  + 订阅者所需权限：ohos.permission.MANAGE\_SECURE\_SETTINGS（该权限仅系统应用可申请）
* COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED(deprecated) （预留事件，暂未支持）提示检测到NFC设备RF字段处于关闭状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_NFC\_ACTION\_RF\_FIELD\_OFF\_DETECTED](commoneventmanager-definitions.md#common_event_nfc_action_rf_field_off_detected)替代。

  + 值：usual.event.nfc.action.RF\_FIELD\_OFF\_DETECTED
  + 订阅者所需权限：ohos.permission.MANAGE\_SECURE\_SETTINGS（该权限仅系统应用可申请）
* COMMON\_EVENT\_DISCHARGING(deprecated) 提示系统停止为电池充电。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DISCHARGING](commoneventmanager-definitions.md#common_event_discharging)替代。

  + 值：usual.event.DISCHARGING
  + 订阅者所需权限：无
* COMMON\_EVENT\_CHARGING(deprecated) 提示系统开始为电池充电。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_CHARGING](commoneventmanager-definitions.md#common_event_charging)替代。

  + 值：usual.event.CHARGING
  + 订阅者所需权限：无
* COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED(deprecated) （预留事件，暂未支持）提示系统空闲模式已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DEVICE\_IDLE\_MODE\_CHANGED](commoneventmanager-definitions.md#common_event_device_idle_mode_changed)替代。

  + 值：usual.event.DEVICE\_IDLE\_MODE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED(deprecated) 提示系统节能模式更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_POWER\_SAVE\_MODE\_CHANGED](commoneventmanager-definitions.md#common_event_power_save_mode_changed)替代。

  + 值：usual.event.POWER\_SAVE\_MODE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_USER\_ADDED(deprecated) 提示用户已添加到系统中。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用COMMON\_EVENT\_USER\_ADDED替代。

  + 值：usual.event.USER\_ADDED
  + 订阅者所需权限：ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。
* COMMON\_EVENT\_USER\_REMOVED(deprecated) 提示用户已从系统中删除。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用COMMON\_EVENT\_USER\_REMOVED替代。

  + 值：usual.event.USER\_REMOVED
  + 订阅者所需权限：ohos.permission.MANAGE\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。
* COMMON\_EVENT\_ABILITY\_ADDED(deprecated) （预留事件，暂未支持）提示有某个能力已被添加。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_ABILITY\_ADDED](commoneventmanager-definitions.md#common_event_ability_added)替代。

  + 值：usual.event.ABILITY\_ADDED
  + 订阅者所需权限：ohos.permission.LISTEN\_BUNDLE\_CHANGE
* COMMON\_EVENT\_ABILITY\_REMOVED(deprecated) （预留事件，暂未支持）提示已删除某个能力。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_ABILITY\_REMOVED](commoneventmanager-definitions.md#common_event_ability_removed)替代。

  + 值：usual.event.ABILITY\_REMOVED
  + 订阅者所需权限：ohos.permission.LISTEN\_BUNDLE\_CHANGE
* COMMON\_EVENT\_ABILITY\_UPDATED(deprecated) （预留事件，暂未支持）提示能力已更新。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_ABILITY\_UPDATED](commoneventmanager-definitions.md#common_event_ability_updated)替代。

  + 值：usual.event.ABILITY\_UPDATED
  + 订阅者所需权限：ohos.permission.LISTEN\_BUNDLE\_CHANGE
* COMMON\_EVENT\_LOCATION\_MODE\_STATE\_CHANGED(deprecated) （预留事件，暂未支持）提示系统定位模式已更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_LOCATION\_MODE\_STATE\_CHANGED](commoneventmanager-definitions.md#common_event_location_mode_state_changed)替代。

  + 值：usual.event.location.MODE\_STATE\_CHANGED
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_SLEEP(deprecated) （预留事件，暂未支持）提示车辆的车载信息娱乐（IVI）系统正在休眠。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_SLEEP](commoneventmanager-definitions.md#common_event_ivi_sleep)替代。

  + 值：common.event.IVI\_SLEEP
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_PAUSE(deprecated) （预留事件，暂未支持）提示车辆的车载信息娱乐（IVI）系统已休眠，并通知应用程序停止播放。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_PAUSE](commoneventmanager-definitions.md#common_event_ivi_pause)替代。

  + 值：common.event.IVI\_PAUSE
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_STANDBY(deprecated) （预留事件，暂未支持）提示车辆的车载信息娱乐（IVI）系统中的第三方应用暂停当前工作。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_STANDBY](commoneventmanager-definitions.md#common_event_ivi_standby)替代。

  + 值：common.event.IVI\_STANDBY
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_LASTMODE\_SAVE(deprecated) （预留事件，暂未支持）提示车辆的车载信息娱乐（IVI）系统中的第三方应用保存其最后一个模式。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_LASTMODE\_SAVE](commoneventmanager-definitions.md#common_event_ivi_lastmode_save)替代。

  + 值：common.event.IVI\_LASTMODE\_SAVE
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_VOLTAGE\_ABNORMAL(deprecated) （预留事件，暂未支持）提示车辆电源系统电压异常。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_VOLTAGE\_ABNORMAL](commoneventmanager-definitions.md#common_event_ivi_voltage_abnormal)替代。

  + 值：common.event.IVI\_VOLTAGE\_ABNORMAL
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_HIGH\_TEMPERATURE(deprecated) （预留事件，暂未支持）提示车辆的车载信息娱乐（IVI）系统温度过高。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_HIGH\_TEMPERATURE](commoneventmanager-definitions.md#common_event_ivi_high_temperature)替代。

  + 值：common.event.IVI\_HIGH\_TEMPERATURE
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_EXTREME\_TEMPERATURE(deprecated) （预留事件，暂未支持）提示车辆的车载信息娱乐（IVI）系统温度极高。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_EXTREME\_TEMPERATURE](commoneventmanager-definitions.md#common_event_ivi_extreme_temperature)替代。

  + 值：common.event.IVI\_EXTREME\_TEMPERATURE
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_TEMPERATURE\_ABNORMAL(deprecated) （预留事件，暂未支持）提示车辆的车载信息娱乐（IVI）系统具有极端温度。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_TEMPERATURE\_ABNORMAL](commoneventmanager-definitions.md#common_event_ivi_temperature_abnormal)替代。

  + 值：common.event.IVI\_TEMPERATURE\_ABNORMAL
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_VOLTAGE\_RECOVERY(deprecated) （预留事件，暂未支持）提示车辆电源系统电压恢复正常。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_VOLTAGE\_RECOVERY](commoneventmanager-definitions.md#common_event_ivi_voltage_recovery)替代。

  + 值：common.event.IVI\_VOLTAGE\_RECOVERY
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_TEMPERATURE\_RECOVERY(deprecated) （预留事件，暂未支持）提示车载系统温度恢复正常。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_TEMPERATURE\_RECOVERY](commoneventmanager-definitions.md#common_event_ivi_temperature_recovery)替代。

  + 值：common.event.IVI\_TEMPERATURE\_RECOVERY
  + 订阅者所需权限：无
* COMMON\_EVENT\_IVI\_ACTIVE(deprecated) （预留事件，暂未支持）提示车载系统电池服务处于活动状态。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_IVI\_ACTIVE](commoneventmanager-definitions.md#common_event_ivi_active)替代。

  + 值：common.event.IVI\_ACTIVE
  + 订阅者所需权限：无
* COMMON\_EVENT\_USB\_DEVICE\_ATTACHED(deprecated) 当用户设备作为USB主机时，提示USB设备已挂载。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USB\_DEVICE\_ATTACHED](commoneventmanager-definitions.md#common_event_usb_device_attached)替代。

  + 值：usual.event.hardware.usb.action.USB\_DEVICE\_ATTACHED
  + 订阅者所需权限：无
* COMMON\_EVENT\_USB\_DEVICE\_DETACHED(deprecated) 当用户设备作为USB主机时，提示USB设备被卸载。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USB\_DEVICE\_DETACHED](commoneventmanager-definitions.md#common_event_usb_device_detached)替代。

  + 值：usual.event.hardware.usb.action.USB\_DEVICE\_DETACHED
  + 订阅者所需权限：无
* COMMON\_EVENT\_USB\_ACCESSORY\_ATTACHED(deprecated) （预留事件，暂未支持）提示已连接USB附件。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USB\_ACCESSORY\_ATTACHED](commoneventmanager-definitions.md#common_event_usb_accessory_attached)替代。

  + 值：usual.event.hardware.usb.action.USB\_ACCESSORY\_ATTACHED
  + 订阅者所需权限：无
* COMMON\_EVENT\_USB\_ACCESSORY\_DETACHED(deprecated) （预留事件，暂未支持）提示USB附件被卸载。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_USB\_ACCESSORY\_DETACHED](commoneventmanager-definitions.md#common_event_usb_accessory_detached)替代。

  + 值：usual.event.hardware.usb.action.USB\_ACCESSORY\_DETACHED
  + 订阅者所需权限：无
* COMMON\_EVENT\_DISK\_REMOVED(deprecated) （预留事件，暂未支持）提示外部存储设备状态变更为移除。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DISK\_REMOVED](commoneventmanager-definitions.md#common_event_disk_removed)替代。

  + 值：usual.event.data.DISK\_REMOVED
  + 订阅者所需权限：ohos.permission.STORAGE\_MANAGER，该权限仅系统应用可申请。
* COMMON\_EVENT\_DISK\_UNMOUNTED(deprecated) （预留事件，暂未支持）提示外部存储设备状态变更为卸载。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DISK\_UNMOUNTED](commoneventmanager-definitions.md#common_event_disk_unmounted)替代。

  + 值：usual.event.data.DISK\_UNMOUNTED
  + 订阅者所需权限：ohos.permission.STORAGE\_MANAGER，该权限仅系统应用可申请。
* COMMON\_EVENT\_DISK\_MOUNTED(deprecated) （预留事件，暂未支持）提示外部存储设备状态变更为挂载。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DISK\_MOUNTED](commoneventmanager-definitions.md#common_event_disk_mounted)替代。

  + 值：usual.event.data.DISK\_MOUNTED
  + 订阅者所需权限：ohos.permission.STORAGE\_MANAGER，该权限仅系统应用可申请。
* COMMON\_EVENT\_DISK\_BAD\_REMOVAL(deprecated) （预留事件，暂未支持）提示外部存储设备在挂载状态下被移除。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DISK\_BAD\_REMOVAL](commoneventmanager-definitions.md#common_event_disk_bad_removal)替代。

  + 值：usual.event.data.DISK\_BAD\_REMOVAL
  + 订阅者所需权限：ohos.permission.STORAGE\_MANAGER，该权限仅系统应用可申请。
* COMMON\_EVENT\_DISK\_UNMOUNTABLE(deprecated) （预留事件，暂未支持）提示外部存储设备在插卡情况下无法挂载。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DISK\_UNMOUNTABLE](commoneventmanager-definitions.md#common_event_disk_unmountable)替代。

  + 值：usual.event.data.DISK\_UNMOUNTABLE
  + 订阅者所需权限：ohos.permission.STORAGE\_MANAGER，该权限仅系统应用可申请。
* COMMON\_EVENT\_DISK\_EJECT(deprecated) （预留事件，暂未支持）提示用户已作出弹出外部存储介质的操作（系统软件层面的交互操作，非直接物理弹出）。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_DISK\_EJECT](commoneventmanager-definitions.md#common_event_disk_eject)替代。

  + 值：usual.event.data.DISK\_EJECT
  + 订阅者所需权限：ohos.permission.STORAGE\_MANAGER，该权限仅系统应用可申请。
* COMMON\_EVENT\_VISIBLE\_ACCOUNTS\_UPDATED(deprecated) （预留事件，暂未支持）提示账户发生可见性的更改。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_VISIBLE\_ACCOUNTS\_UPDATED](commoneventmanager-definitions.md#common_event_visible_accounts_updated)替代。

  + 值：usual.event.data.VISIBLE\_ACCOUNTS\_UPDATED
  + 订阅者所需权限：ohos.permission.GET\_APP\_ACCOUNTS，该权限仅系统应用可申请。
* COMMON\_EVENT\_ACCOUNT\_DELETED(deprecated) （预留事件，暂未支持）提示有账户被删除。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_ACCOUNT\_DELETED](commoneventmanager-definitions.md#common_event_account_deleted)替代。

  + 值：usual.event.data.ACCOUNT\_DELETED
  + 订阅者所需权限：ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS，该权限仅系统应用可申请。
* COMMON\_EVENT\_FOUNDATION\_READY(deprecated) （预留事件，暂未支持）提示foundation已准备好。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_FOUNDATION\_READY](commoneventmanager-definitions.md#common_event_foundation_ready)替代。

  + 值：usual.event.data.FOUNDATION\_READY
  + 订阅者所需权限：ohos.permission.RECEIVER\_STARTUP\_COMPLETED（该权限仅系统应用可申请）
* COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED(deprecated) 提示设备飞行模式发生了切换。

  说明

  从API version 7 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_AIRPLANE\_MODE\_CHANGED](commoneventmanager-definitions.md#common_event_airplane_mode_changed10)替代。

  + 值：usual.event.AIRPLANE\_MODE
  + 订阅者所需权限：无
* COMMON\_EVENT\_SPLIT\_SCREEN(deprecated) 提示分屏。

  说明

  从API version 8 开始支持，从API version 9 开始废弃，建议使用[COMMON\_EVENT\_SPLIT\_SCREEN](commoneventmanager-definitions.md#common_event_split_screen)替代。
