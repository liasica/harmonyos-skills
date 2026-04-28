---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-510
title: Notification Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Notification Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:14+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9559a5271faa37d1e811cf8162a53ee8999c6240686a8894cc1b8e53aa99a4c7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：notificationManager；  API声明：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：notificationManager；  API声明：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void;  差异内容：801 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager；  API声明：function setBadgeNumber(badgeNumber: number): Promise<void>;  差异内容：NA | 类名：notificationManager；  API声明：function setBadgeNumber(badgeNumber: number): Promise<void>;  差异内容：801 | api/@ohos.notificationManager.d.ts |
| 新增错误码 | 类名：notificationManager；  API声明：function openNotificationSettings(context: UIAbilityContext): Promise<void>;  差异内容：NA | 类名：notificationManager；  API声明：function openNotificationSettings(context: UIAbilityContext): Promise<void>;  差异内容：801 | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function cancelAll(): Promise<void>;  差异内容：401 | 类名：notificationManager；  API声明：function cancelAll(): Promise<void>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function getSlots(): Promise<Array<NotificationSlot>>;  差异内容：401 | 类名：notificationManager；  API声明：function getSlots(): Promise<Array<NotificationSlot>>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function removeAllSlots(): Promise<void>;  差异内容：401 | 类名：notificationManager；  API声明：function removeAllSlots(): Promise<void>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function isNotificationEnabled(): Promise<boolean>;  差异内容：401 | 类名：notificationManager；  API声明：function isNotificationEnabled(): Promise<boolean>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function getActiveNotificationCount(): Promise<number>;  差异内容：401 | 类名：notificationManager；  API声明：function getActiveNotificationCount(): Promise<number>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function getActiveNotifications(): Promise<Array<NotificationRequest>>;  差异内容：401 | 类名：notificationManager；  API声明：function getActiveNotifications(): Promise<Array<NotificationRequest>>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：401 | 类名：notificationManager；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 删除错误码 | 类名：notificationManager；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：401 | 类名：notificationManager；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：NA | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface NotificationIconButton  差异内容：export interface NotificationIconButton | api/notification/notificationContent.d.ts |
| 起始版本有变化 | 类名：notificationManager；  API声明：function isNotificationEnabled(callback: AsyncCallback<boolean>): void;  差异内容：9 | 类名：notificationManager；  API声明：function isNotificationEnabled(callback: AsyncCallback<boolean>): void;  差异内容：11 | api/@ohos.notificationManager.d.ts |
| 起始版本有变化 | 类名：notificationManager；  API声明：function isNotificationEnabled(): Promise<boolean>;  差异内容：9 | 类名：notificationManager；  API声明：function isNotificationEnabled(): Promise<boolean>;  差异内容：11 | api/@ohos.notificationManager.d.ts |
| 起始版本有变化 | 类名：global；  API声明：export enum NotificationFlagStatus  差异内容：8 | 类名：global；  API声明：export enum NotificationFlagStatus  差异内容：11 | api/notification/notificationFlags.d.ts |
| 起始版本有变化 | 类名：NotificationFlagStatus；  API声明：TYPE\_NONE = 0  差异内容：8 | 类名：NotificationFlagStatus；  API声明：TYPE\_NONE = 0  差异内容：11 | api/notification/notificationFlags.d.ts |
| 起始版本有变化 | 类名：NotificationFlagStatus；  API声明：TYPE\_OPEN = 1  差异内容：8 | 类名：NotificationFlagStatus；  API声明：TYPE\_OPEN = 1  差异内容：11 | api/notification/notificationFlags.d.ts |
| 起始版本有变化 | 类名：NotificationFlagStatus；  API声明：TYPE\_CLOSE = 2  差异内容：8 | 类名：NotificationFlagStatus；  API声明：TYPE\_CLOSE = 2  差异内容：11 | api/notification/notificationFlags.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：NotificationRequest；  API声明：updateOnly?: boolean;  差异内容：updateOnly?: boolean; | api/notification/notificationRequest.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface NotificationIconButton  差异内容：NA | 类名：global；  API声明：  差异内容：export interface NotificationIconButton | api/notification/notificationContent.d.ts |
