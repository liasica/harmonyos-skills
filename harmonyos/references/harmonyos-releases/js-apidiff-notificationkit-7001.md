---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-notificationkit-7001
title: Notification Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Notification Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:804236a2b41811887400bf271f5c4728253dae7ffe9d88bb0c5204093616321a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export interface UserGrantSetting  差异内容：export interface UserGrantSetting | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：UserGrantSetting；  API声明：readonly userGrantEnabled: boolean;  差异内容：readonly userGrantEnabled: boolean; | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：UserGrantSetting；  API声明：readonly grantedBundleInfos?: Array<GrantedBundleInfo>;  差异内容：readonly grantedBundleInfos?: Array<GrantedBundleInfo>; | api/notification/NotificationCommonDef.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：function openSubscriptionSettingsWithResult(context: UIAbilityContext): Promise<UserGrantSetting>;  差异内容：function openSubscriptionSettingsWithResult(context: UIAbilityContext): Promise<UserGrantSetting>; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationExtensionSubscription；  API声明：export type UserGrantSetting = \_UserGrantSetting;  差异内容：export type UserGrantSetting = \_UserGrantSetting; | api/@ohos.notificationExtensionSubscription.d.ts |
| 新增API | NA | 类名：notificationManager；  API声明：function openNotificationSettingsWithResult(context: UIAbilityContext): Promise<NotificationSetting>;  差异内容：function openNotificationSettingsWithResult(context: UIAbilityContext): Promise<NotificationSetting>; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting；  API声明：lockScreenEnabled?: boolean;  差异内容：lockScreenEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting；  API声明：bannerEnabled?: boolean;  差异内容：bannerEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting；  API声明：badgeNumberEnabled?: boolean;  差异内容：badgeNumberEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
| 新增API | NA | 类名：NotificationSetting；  API声明：notificationEnabled?: boolean;  差异内容：notificationEnabled?: boolean; | api/@ohos.notificationManager.d.ts |
