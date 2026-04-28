---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-6021
title: Notification Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Notification Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c0490cd700a3bc2c0c7e1a46e490b009bc54fa7b0445110177a469f0071c3d71
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：export interface ActionResult  差异内容：NA | 类名：global；  API声明：export interface ActionResult  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：ActionResult；  API声明：bundleName: string;  差异内容：NA | 类名：ActionResult；  API声明：bundleName: string;  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：ActionResult；  API声明：abilityName: string;  差异内容：NA | 类名：ActionResult；  API声明：abilityName: string;  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：ActionResult；  API声明：uri: string;  差异内容：NA | 类名：ActionResult；  API声明：uri: string;  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export interface ShowNotificationOptions  差异内容：NA | 类名：global；  API声明：export interface ShowNotificationOptions  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：ShowNotificationOptions；  API声明：contentTitle?: string;  差异内容：NA | 类名：ShowNotificationOptions；  API声明：contentTitle?: string;  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：ShowNotificationOptions；  API声明：contentText?: string;  差异内容：NA | 类名：ShowNotificationOptions；  API声明：contentText?: string;  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export default class Notification  差异内容：NA | 类名：global；  API声明：declare class Notification  差异内容：7 | api/@system.notification.d.ts |
| API废弃版本变更 | 类名：Notification；  API声明：static show(options?: ShowNotificationOptions): void;  差异内容：NA | 类名：Notification；  API声明：static show(options?: ShowNotificationOptions): void;  差异内容：7 | api/@system.notification.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class NotificationSubscriberExtensionAbility  差异内容：declare class NotificationSubscriberExtensionAbility | api/@ohos.application.NotificationSubscriberExtensionAbility.d.ts |
| 新增API | NA | 类名：NotificationSubscriberExtensionAbility；  API声明：context: NotificationSubscriberExtensionContext;  差异内容：context: NotificationSubscriberExtensionContext; | api/@ohos.application.NotificationSubscriberExtensionAbility.d.ts |
| 新增API | NA | 类名：NotificationSubscriberExtensionAbility；  API声明：onDestroy(): void;  差异内容：onDestroy(): void; | api/@ohos.application.NotificationSubscriberExtensionAbility.d.ts |
| 新增API | NA | 类名：NotificationSubscriberExtensionAbility；  API声明：onReceiveMessage(notificationInfo: NotificationInfo): void;  差异内容：onReceiveMessage(notificationInfo: NotificationInfo): void; | api/@ohos.application.NotificationSubscriberExtensionAbility.d.ts |
| 新增API | NA | 类名：NotificationSubscriberExtensionAbility；  API声明：onCancelMessages(hashCodes: Array<string>): void;  差异内容：onCancelMessages(hashCodes: Array<string>): void; | api/@ohos.application.NotificationSubscriberExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class NotificationSubscriberExtensionContext  差异内容：export default class NotificationSubscriberExtensionContext | api/@ohos.application.NotificationSubscriberExtensionContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace notificationExtensionSubscription  差异内容：declare namespace notificationExtensionSubscription | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：function openSubscriptionSettings(context: UIAbilityContext): Promise<void>;  差异内容：function openSubscriptionSettings(context: UIAbilityContext): Promise<void>; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>;  差异内容：function subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：function unsubscribe(): Promise<void>;  差异内容：function unsubscribe(): Promise<void>; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：function getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>;  差异内容：function getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：function isUserGranted(): Promise<boolean>;  差异内容：function isUserGranted(): Promise<boolean>; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：function getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>;  差异内容：function getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：export enum SubscribeType  差异内容：export enum SubscribeType | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：SubscribeType；  API声明：BLUETOOTH = 0  差异内容：BLUETOOTH = 0 | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：export type BundleOption = \_BundleOption;  差异内容：export type BundleOption = \_BundleOption; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：export type GrantedBundleInfo = \_GrantedBundleInfo;  差异内容：export type GrantedBundleInfo = \_GrantedBundleInfo; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：export type NotificationExtensionSubscriptionInfo = \_NotificationExtensionSubscriptionInfo;  差异内容：export type NotificationExtensionSubscriptionInfo = \_NotificationExtensionSubscriptionInfo; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：export type NotificationInfo = \_NotificationInfo;  差异内容：export type NotificationInfo = \_NotificationInfo; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface NotificationExtensionContent  差异内容：export interface NotificationExtensionContent | api/notification/NotificationExtensionContent.d.ts |
| 新增API | NA | 类名：NotificationExtensionContent；  API声明：title: string;  差异内容：title: string; | api/notification/NotificationExtensionContent.d.ts |
| 新增API | NA | 类名：NotificationExtensionContent；  API声明：text: string;  差异内容：text: string; | api/notification/NotificationExtensionContent.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface NotificationExtensionSubscriptionInfo  差异内容：export interface NotificationExtensionSubscriptionInfo | api/notification/NotificationExtensionSubscriptionInfo.d.ts |
| 新增API | NA | 类名：NotificationExtensionSubscriptionInfo；  API声明：addr: string;  差异内容：addr: string; | api/notification/NotificationExtensionSubscriptionInfo.d.ts |
| 新增API | NA | 类名：NotificationExtensionSubscriptionInfo；  API声明：type: notificationExtensionSubscription.SubscribeType;  差异内容：type: notificationExtensionSubscription.SubscribeType; | api/notification/NotificationExtensionSubscriptionInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface NotificationInfo  差异内容：export interface NotificationInfo | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly hashCode: string;  差异内容：readonly hashCode: string; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly notificationSlotType: notificationManager.SlotType;  差异内容：readonly notificationSlotType: notificationManager.SlotType; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly content: NotificationExtensionContent;  差异内容：readonly content: NotificationExtensionContent; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly bundleName: string;  差异内容：readonly bundleName: string; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly appName?: string;  差异内容：readonly appName?: string; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly deliveryTime?: number;  差异内容：readonly deliveryTime?: number; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly groupName?: string;  差异内容：readonly groupName?: string; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：NotificationInfo；  API声明：readonly appIndex: number;  差异内容：readonly appIndex: number; | api/notification/NotificationInfo.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface GrantedBundleInfo  差异内容：export interface GrantedBundleInfo | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：GrantedBundleInfo；  API声明：bundleName: string;  差异内容：bundleName: string; | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：GrantedBundleInfo；  API声明：readonly appIndex: number;  差异内容：readonly appIndex: number; | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：GrantedBundleInfo；  API声明：readonly appName?: string;  差异内容：readonly appName?: string; | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function getBadgeNumber(): Promise<number>;  差异内容：function getBadgeNumber(): Promise<number>; | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：global；  API声明：export interface NotificationIconButton  差异内容：export interface NotificationIconButton | NA | api/notification/notificationContent.d.ts |
| 删除API | 类名：notificationManager；  API声明：export interface RingtoneInfo  差异内容：export interface RingtoneInfo | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneInfo；  API声明：ringtoneType: RingtoneType;  差异内容：ringtoneType: RingtoneType; | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneInfo；  API声明：ringtoneTitle?: string;  差异内容：ringtoneTitle?: string; | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneInfo；  API声明：ringtoneFileName?: string;  差异内容：ringtoneFileName?: string; | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneInfo；  API声明：ringtoneUri?: string;  差异内容：ringtoneUri?: string; | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：notificationManager；  API声明：export enum RingtoneType  差异内容：export enum RingtoneType | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneType；  API声明：RINGTONE\_TYPE\_SYSTEM = 0  差异内容：RINGTONE\_TYPE\_SYSTEM = 0 | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneType；  API声明：RINGTONE\_TYPE\_LOCAL = 1  差异内容：RINGTONE\_TYPE\_LOCAL = 1 | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneType；  API声明：RINGTONE\_TYPE\_ONLINE = 2  差异内容：RINGTONE\_TYPE\_ONLINE = 2 | NA | api/@ohos.notificationManager.d.ts |
| 删除API | 类名：RingtoneType；  API声明：RINGTONE\_TYPE\_NONE = 3  差异内容：RINGTONE\_TYPE\_NONE = 3 | NA | api/@ohos.notificationManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.application.NotificationSubscriberExtensionAbility.d.ts  差异内容：NotificationKit | api/@ohos.application.NotificationSubscriberExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.application.NotificationSubscriberExtensionContext.d.ts  差异内容：NotificationKit | api/@ohos.application.NotificationSubscriberExtensionContext.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.notificationExtensionSubscription.d.ts  差异内容：NotificationKit | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\notification\NotificationExtensionContent.d.ts  差异内容：NotificationKit | api/notification/NotificationExtensionContent.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\notification\NotificationExtensionSubscriptionInfo.d.ts  差异内容：NotificationKit | api/notification/NotificationExtensionSubscriptionInfo.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\notification\NotificationInfo.d.ts  差异内容：NotificationKit | api/notification/NotificationInfo.d.ts |
| 删除导出符号 | 类名：global；  API声明：export interface NotificationIconButton  差异内容：export interface NotificationIconButton | 类名：global；  API声明：  差异内容：NA | api/notification/notificationContent.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface GrantedBundleInfo  差异内容：NA | 类名：global；  API声明：  差异内容：export interface GrantedBundleInfo | api/notification/NotificationCommonDef.d.ts |
| arkts演进版本整改兼容变化 | 类名：global；  API声明：export default class Notification  差异内容：NA | 类名：global；  API声明：declare class Notification  差异内容：NA | api/@system.notification.d.ts |
