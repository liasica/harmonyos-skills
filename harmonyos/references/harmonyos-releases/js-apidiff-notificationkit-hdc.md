---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-hdc
title: Notification Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Notification Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1b628de8c2e9218a837c62c3ad48e8a7c63a061715bbc881ccfcb6ef4bdfb46a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：NotificationContent；  API声明：contentType: notification.ContentType;  差异内容：NA | 类名：NotificationContent；  API声明：contentType?: notification.ContentType;  差异内容：11 | api/notification/notificationContent.d.ts |
| API废弃版本变更 | 类名：NotificationRequest；  API声明：slotType?: notification.SlotType;  差异内容：NA | 类名：NotificationRequest；  API声明：slotType?: notification.SlotType;  差异内容：11 | api/notification/notificationRequest.d.ts |
| API废弃版本变更 | 类名：NotificationSlot；  API声明：type: notification.SlotType;  差异内容：NA | 类名：NotificationSlot；  API声明：type?: notification.SlotType;  差异内容：11 | api/notification/notificationSlot.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function publish(request: NotificationRequest): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function publish(request: NotificationRequest): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function cancel(id: number, label?: string): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function cancel(id: number, label?: string): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function cancelAll(): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function cancelAll(): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function addSlot(type: SlotType): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function addSlot(type: SlotType): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function getSlot(slotType: SlotType): Promise<NotificationSlot>;  差异内容：NA | 类名：notification；  API声明：function getSlot(slotType: SlotType): Promise<NotificationSlot>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function getSlots(): Promise<Array<NotificationSlot>>;  差异内容：NA | 类名：notification；  API声明：function getSlots(): Promise<Array<NotificationSlot>>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function removeSlot(slotType: SlotType): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function removeSlot(slotType: SlotType): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function removeAllSlots(): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function removeAllSlots(): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotType；  API声明：UNKNOWN\_TYPE = 0  差异内容：NA | 类名：SlotType；  API声明：UNKNOWN\_TYPE = 0  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotType；  API声明：SOCIAL\_COMMUNICATION = 1  差异内容：NA | 类名：SlotType；  API声明：SOCIAL\_COMMUNICATION = 1  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotType；  API声明：SERVICE\_INFORMATION = 2  差异内容：NA | 类名：SlotType；  API声明：SERVICE\_INFORMATION = 2  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotType；  API声明：CONTENT\_INFORMATION = 3  差异内容：NA | 类名：SlotType；  API声明：CONTENT\_INFORMATION = 3  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotType；  API声明：OTHER\_TYPES = 0xFFFF  差异内容：NA | 类名：SlotType；  API声明：OTHER\_TYPES = 0xFFFF  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_BASIC\_TEXT  差异内容：NA | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_BASIC\_TEXT  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_LONG\_TEXT  差异内容：NA | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_LONG\_TEXT  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_PICTURE  差异内容：NA | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_PICTURE  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_CONVERSATION  差异内容：NA | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_CONVERSATION  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_MULTILINE  差异内容：NA | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_MULTILINE  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotLevel；  API声明：LEVEL\_NONE = 0  差异内容：NA | 类名：SlotLevel；  API声明：LEVEL\_NONE = 0  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotLevel；  API声明：LEVEL\_MIN = 1  差异内容：NA | 类名：SlotLevel；  API声明：LEVEL\_MIN = 1  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotLevel；  API声明：LEVEL\_LOW = 2  差异内容：NA | 类名：SlotLevel；  API声明：LEVEL\_LOW = 2  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotLevel；  API声明：LEVEL\_DEFAULT = 3  差异内容：NA | 类名：SlotLevel；  API声明：LEVEL\_DEFAULT = 3  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：SlotLevel；  API声明：LEVEL\_HIGH = 4  差异内容：NA | 类名：SlotLevel；  API声明：LEVEL\_HIGH = 4  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function getActiveNotificationCount(): Promise<number>;  差异内容：NA | 类名：notification；  API声明：function getActiveNotificationCount(): Promise<number>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function getActiveNotifications(): Promise<Array<NotificationRequest>>;  差异内容：NA | 类名：notification；  API声明：function getActiveNotifications(): Promise<Array<NotificationRequest>>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function cancelGroup(groupName: string): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function cancelGroup(groupName: string): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function isSupportTemplate(templateName: string): Promise<boolean>;  差异内容：NA | 类名：notification；  API声明：function isSupportTemplate(templateName: string): Promise<boolean>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：NA | 类名：notification；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：notification；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：NA | 类名：notification；  API声明：function isDistributedEnabled(): Promise<boolean>;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：BundleOption；  API声明：bundle: string;  差异内容：NA | 类名：BundleOption；  API声明：bundle: string;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：BundleOption；  API声明：uid?: number;  差异内容：NA | 类名：BundleOption；  API声明：uid?: number;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：NotificationKey；  API声明：id: number;  差异内容：NA | 类名：NotificationKey；  API声明：id: number;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：NotificationKey；  API声明：label?: string;  差异内容：NA | 类名：NotificationKey；  API声明：label?: string;  差异内容：9 | api/@ohos.notification.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly id: string;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly id: string;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly bundleName: string;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly bundleName: string;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly hostAbility: string;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly hostAbility: string;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly icon: string;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly icon: string;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly iconId: number;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly iconId: number;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly label: string;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly label: string;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly labelId: number;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly labelId: number;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly disableMessage: string;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly disableMessage: string;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly wants: Array<ShortcutWant>;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly wants: Array<ShortcutWant>;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly isStatic?: boolean;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly isStatic?: boolean;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly isHomeShortcut?: boolean;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly isHomeShortcut?: boolean;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| API废弃版本变更 | 类名：ShortcutInfo；  API声明：readonly isEnabled?: boolean;  差异内容：NA | 类名：ShortcutInfo；  API声明：readonly isEnabled?: boolean;  差异内容：9 | api/bundle/shortcutInfo.d.ts |
| 权限变更 | 类名：global；  API声明： declare namespace commonEvent  差异内容：N/A | 类名：global；  API声明： declare namespace commonEvent  差异内容：NA | api/@ohos.commonEvent.d.ts |
| 权限变更 | 类名：commonEvent；  API声明： export enum Support  差异内容：N/A | 类名：commonEvent；  API声明： export enum Support  差异内容：NA | api/@ohos.commonEvent.d.ts |
| 权限变更 | 类名：global；  API声明： declare namespace notification  差异内容：N/A | 类名：global；  API声明： declare namespace notification  差异内容：NA | api/@ohos.notification.d.ts |
| 权限变更 | 类名：notification；  API声明： export enum ContentType  差异内容：N/A | 类名：notification；  API声明： export enum ContentType  差异内容：NA | api/@ohos.notification.d.ts |
| 错误码变更 | 类名：notificationManager；  API声明：function publish(request: NotificationRequest, callback: AsyncCallback<void>): void;  差异内容：1600001,1600002,1600003,1600004,1600005,1600009,401 | 类名：notificationManager；  API声明：function publish(request: NotificationRequest, callback: AsyncCallback<void>): void;  差异内容：1600001,1600002,1600003,1600004,1600005,1600007,1600009,1600012,1600014,1600015,1600016,2300007,401 | api/@ohos.notificationManager.d.ts |
| 错误码变更 | 类名：notificationManager；  API声明：function publish(request: NotificationRequest): Promise<void>;  差异内容：1600001,1600002,1600003,1600004,1600005,1600009,401 | 类名：notificationManager；  API声明：function publish(request: NotificationRequest): Promise<void>;  差异内容：1600001,1600002,1600003,1600004,1600005,1600007,1600009,1600012,1600014,1600015,1600016,2300007,401 | api/@ohos.notificationManager.d.ts |
| 错误码变更 | 类名：notificationManager；  API声明：function addSlot(type: SlotType, callback: AsyncCallback<void>): void;  差异内容：1600001,1600002,1600003,401 | 类名：notificationManager；  API声明：function addSlot(type: SlotType, callback: AsyncCallback<void>): void;  差异内容：1600001,1600002,1600003,1600012,401 | api/@ohos.notificationManager.d.ts |
| 错误码变更 | 类名：notificationManager；  API声明：function addSlot(type: SlotType): Promise<void>;  差异内容：1600001,1600002,1600003,401 | 类名：notificationManager；  API声明：function addSlot(type: SlotType): Promise<void>;  差异内容：1600001,1600002,1600003,1600012,401 | api/@ohos.notificationManager.d.ts |
| 错误码变更 | 类名：notificationManager；  API声明：function requestEnableNotification(callback: AsyncCallback<void>): void;  差异内容：1600001,1600002,1600003,401 | 类名：notificationManager；  API声明：function requestEnableNotification(callback: AsyncCallback<void>): void;  差异内容：1600001,1600002,1600003,1600004,1600013,401 | api/@ohos.notificationManager.d.ts |
| 错误码变更 | 类名：notificationManager；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：1600001,1600002,1600003,401 | 类名：notificationManager；  API声明：function requestEnableNotification(): Promise<void>;  差异内容：1600001,1600002,1600003,1600004,1600013,401 | api/@ohos.notificationManager.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationActionButton  差异内容：N/A | 类名：global；  API声明： export interface NotificationActionButton  差异内容：NA | api/notification/notificationActionButton.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationBasicContent  差异内容：N/A | 类名：global；  API声明： export interface NotificationBasicContent  差异内容：NA | api/notification/notificationContent.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationLongTextContent  差异内容：N/A | 类名：global；  API声明： export interface NotificationLongTextContent  差异内容：NA | api/notification/notificationContent.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationMultiLineContent  差异内容：N/A | 类名：global；  API声明： export interface NotificationMultiLineContent  差异内容：NA | api/notification/notificationContent.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationPictureContent  差异内容：N/A | 类名：global；  API声明： export interface NotificationPictureContent  差异内容：NA | api/notification/notificationContent.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationContent  差异内容：N/A | 类名：global；  API声明： export interface NotificationContent  差异内容：NA | api/notification/notificationContent.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationRequest  差异内容：N/A | 类名：global；  API声明： export interface NotificationRequest  差异内容：NA | api/notification/notificationRequest.d.ts |
| 权限变更 | 类名：global；  API声明： export interface DistributedOptions  差异内容：N/A | 类名：global；  API声明： export interface DistributedOptions  差异内容：NA | api/notification/notificationRequest.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationSlot  差异内容：N/A | 类名：global；  API声明： export interface NotificationSlot  差异内容：NA | api/notification/notificationSlot.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationTemplate  差异内容：N/A | 类名：global；  API声明： export interface NotificationTemplate  差异内容：NA | api/notification/notificationTemplate.d.ts |
| 权限变更 | 类名：global；  API声明： export interface NotificationUserInput  差异内容：N/A | 类名：global；  API声明： export interface NotificationUserInput  差异内容：NA | api/notification/notificationUserInput.d.ts |
| 属性变更 | 类名：NotificationContent；  API声明：contentType: notification.ContentType;  差异内容：contentType: notification.ContentType; | 类名：NotificationContent；  API声明：contentType?: notification.ContentType;  差异内容：contentType?: notification.ContentType; | api/notification/notificationContent.d.ts |
| 属性变更 | 类名：NotificationSlot；  API声明：type: notification.SlotType;  差异内容：type: notification.SlotType; | 类名：NotificationSlot；  API声明：type?: notification.SlotType;  差异内容：type?: notification.SlotType; | api/notification/notificationSlot.d.ts |
| 属性变更 | 类名：NotificationTemplate；  API声明：data: {  [key: string]: Object;  };  差异内容：{  [key: string]: Object;  } | 类名：NotificationTemplate；  API声明：data: Record<string, Object>;  差异内容：Record<string, Object> | api/notification/notificationTemplate.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void;  差异内容：function requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function requestEnableNotification(context: UIAbilityContext): Promise<void>;  差异内容：function requestEnableNotification(context: UIAbilityContext): Promise<void>; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function isNotificationEnabled(callback: AsyncCallback<boolean>): void;  差异内容：function isNotificationEnabled(callback: AsyncCallback<boolean>): void; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function isNotificationEnabled(): Promise<boolean>;  差异内容：function isNotificationEnabled(): Promise<boolean>; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void;  差异内容：function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function setBadgeNumber(badgeNumber: number): Promise<void>;  差异内容：function setBadgeNumber(badgeNumber: number): Promise<void>; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：SlotType；  API声明：LIVE\_VIEW = 4  差异内容：LIVE\_VIEW = 4 | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：SlotType；  API声明：CUSTOMER\_SERVICE = 5  差异内容：CUSTOMER\_SERVICE = 5 | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_SYSTEM\_LIVE\_VIEW  差异内容：NOTIFICATION\_CONTENT\_SYSTEM\_LIVE\_VIEW | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：ContentType；  API声明：NOTIFICATION\_CONTENT\_LIVE\_VIEW  差异内容：NOTIFICATION\_CONTENT\_LIVE\_VIEW | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：export type NotificationSystemLiveViewContent = \_NotificationSystemLiveViewContent;  差异内容：export type NotificationSystemLiveViewContent = \_NotificationSystemLiveViewContent; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：export type NotificationCapsule = \_NotificationCapsule;  差异内容：export type NotificationCapsule = \_NotificationCapsule; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：export type NotificationButton = \_NotificationButton;  差异内容：export type NotificationButton = \_NotificationButton; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：export type NotificationTime = \_NotificationTime;  差异内容：export type NotificationTime = \_NotificationTime; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：export type NotificationProgress = \_NotificationProgress;  差异内容：export type NotificationProgress = \_NotificationProgress; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationBasicContent；  API声明：lockscreenPicture?: image.PixelMap;  差异内容：lockscreenPicture?: image.PixelMap; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface NotificationSystemLiveViewContent  差异内容： export interface NotificationSystemLiveViewContent | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationSystemLiveViewContent；  API声明：typeCode: number;  差异内容：typeCode: number; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationSystemLiveViewContent；  API声明：capsule?: NotificationCapsule;  差异内容：capsule?: NotificationCapsule; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationSystemLiveViewContent；  API声明：button?: NotificationButton;  差异内容：button?: NotificationButton; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationSystemLiveViewContent；  API声明：time?: NotificationTime;  差异内容：time?: NotificationTime; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationSystemLiveViewContent；  API声明：progress?: NotificationProgress;  差异内容：progress?: NotificationProgress; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface NotificationCapsule  差异内容： export interface NotificationCapsule | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationCapsule；  API声明：title?: string;  差异内容：title?: string; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationCapsule；  API声明：icon?: image.PixelMap;  差异内容：icon?: image.PixelMap; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationCapsule；  API声明：backgroundColor?: string;  差异内容：backgroundColor?: string; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface NotificationButton  差异内容： export interface NotificationButton | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationButton；  API声明：names?: Array<string>;  差异内容：names?: Array<string>; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationButton；  API声明：icons?: Array<image.PixelMap>;  差异内容：icons?: Array<image.PixelMap>; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface NotificationTime  差异内容： export interface NotificationTime | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationTime；  API声明：initialTime?: number;  差异内容：initialTime?: number; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationTime；  API声明：isCountDown?: boolean;  差异内容：isCountDown?: boolean; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationTime；  API声明：isPaused?: boolean;  差异内容：isPaused?: boolean; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationTime；  API声明：isInTitle?: boolean;  差异内容：isInTitle?: boolean; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface NotificationProgress  差异内容： export interface NotificationProgress | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationProgress；  API声明：maxValue?: number;  差异内容：maxValue?: number; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationProgress；  API声明：currentValue?: number;  差异内容：currentValue?: number; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationProgress；  API声明：isPercentage?: boolean;  差异内容：isPercentage?: boolean; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationContent；  API声明：notificationContentType?: notificationManager.ContentType;  差异内容：notificationContentType?: notificationManager.ContentType; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationContent；  API声明：systemLiveView?: NotificationSystemLiveViewContent;  差异内容：systemLiveView?: NotificationSystemLiveViewContent; | api/notification/notificationContent.d.ts |
| 新增API | NA | 类名：NotificationRequest；  API声明：appMessageId?: string;  差异内容：appMessageId?: string; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationRequest；  API声明：notificationSlotType?: notificationManager.SlotType;  差异内容：notificationSlotType?: notificationManager.SlotType; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationRequest；  API声明：sound?: string;  差异内容：sound?: string; | api/notification/notificationRequest.d.ts |
| 新增API | NA | 类名：NotificationSlot；  API声明：notificationType?: notificationManager.SlotType;  差异内容：notificationType?: notificationManager.SlotType; | api/notification/notificationSlot.d.ts |
| 新增API | NA | 类名：global；  API声明： export enum NotificationFlagStatus  差异内容： export enum NotificationFlagStatus | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：NotificationFlagStatus；  API声明：TYPE\_NONE = 0  差异内容：TYPE\_NONE = 0 | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：NotificationFlagStatus；  API声明：TYPE\_OPEN = 1  差异内容：TYPE\_OPEN = 1 | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：NotificationFlagStatus；  API声明：TYPE\_CLOSE = 2  差异内容：TYPE\_CLOSE = 2 | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface NotificationFlags  差异内容： export interface NotificationFlags | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：NotificationFlags；  API声明：readonly soundEnabled?: NotificationFlagStatus;  差异内容：readonly soundEnabled?: NotificationFlagStatus; | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：NotificationFlags；  API声明：readonly vibrationEnabled?: NotificationFlagStatus;  差异内容：readonly vibrationEnabled?: NotificationFlagStatus; | api/notification/notificationFlags.d.ts |
| 新增API | NA | 类名：global；  API声明： export interface BadgeEnabledChangedCallback  差异内容： export interface BadgeEnabledChangedCallback | api/notification/notificationSubscriber.d.ts |
