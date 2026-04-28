---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-liveformextensionability
title: @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:902cc8dc2df3b96307dece1a4161421e3a1adf38928147833ace0eca9f289a8b
---

LiveFormExtensionAbility模块提供互动卡片功能，包括创建、销毁互动卡片等，继承自[ExtensionAbility](js-apis-app-ability-extensionability.md)。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块设置了不允许调用的API名单，调用名单中的API将导致功能异常，详情请参见[附录](js-apis-app-form-liveformextensionability.md#附录)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { LiveFormExtensionAbility } from '@kit.FormKit';
```

## LiveFormExtensionAbility

PhonePC/2in1TabletTVWearable

互动卡片扩展类。包含互动卡片提供方接收创建和销毁互动卡片的通知接口。

### 属性

PhonePC/2in1TabletTVWearable

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [LiveFormExtensionContext](js-apis-application-liveformextensioncontext.md) | 否 | 否 | LiveFormExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onLiveFormCreate

PhonePC/2in1TabletTVWearable

onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void

LiveFormExtensionAbility界面内容对象创建后调用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](js-apis-app-form-liveformextensionability.md#liveforminfo) | 是 | 互动卡片信息，包括卡片id等信息。 |
| session | [UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md) | 是 | LiveFormExtensionAbility界面内容相关信息。 |

**示例：**

```
1. import { UIExtensionContentSession } from '@kit.AbilityKit';
2. import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

4. const TAG: string = '[testTag] LiveFormExtAbility';

6. export default class LiveFormExtAbility extends LiveFormExtensionAbility {
7. onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
8. console.info(TAG, `onLiveFormCreate, formId: ${liveFormInfo.formId}`);
9. }
10. }
```

### onLiveFormDestroy

PhonePC/2in1TabletTVWearable

onLiveFormDestroy(liveFormInfo: LiveFormInfo): void

LiveFormExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](js-apis-app-form-liveformextensionability.md#liveforminfo) | 是 | 互动卡片信息，包括卡片id等信息。 |

**示例：**

```
1. import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

3. const TAG: string = '[testTag] LiveFormExtAbility';

5. export default class LiveFormExtAbility extends LiveFormExtensionAbility {
6. onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
7. console.info(TAG, `onLiveFormDestroy, liveFormInfo: ${liveFormInfo.formId}`);
8. }
9. }
```

### LiveFormInfo

PhonePC/2in1TabletTVWearable

互动卡片信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | string | 否 | 否 | 卡片id。 |
| rect | [formInfo.Rect](js-apis-app-form-forminfo.md#rect20) | 否 | 否 | 卡片位置和大小信息。 |
| borderRadius | number | 否 | 否 | 卡片圆角半径信息。取值大于0，单位vp。 |

## 附录

PhonePC/2in1TabletTVWearable

本模块不允许调用的API名单如下。

| Kit名称 | 模块名称 |
| --- | --- |
| AbilityKit | [@ohos.ability.featureAbility (FeatureAbility模块)](js-apis-ability-featureability.md)  [@ohos.ability.particleAbility (ParticleAbility模块)](js-apis-ability-particleability.md)  [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](js-apis-launcherbundlemanager.md)  [@ohos.continuation.continuationManager (流转/协同管理)](js-apis-continuation-continuationmanager.md) |
| BasicServicesKit | [@ohos.account.appAccount (应用账号管理)](js-apis-appaccount.md)  [@ohos.account.distributedAccount (分布式账号管理)](js-apis-distributed-account.md)  [@ohos.account.osAccount (系统账号管理)](js-apis-osaccount.md)  [@ohos.pasteboard (剪贴板)](js-apis-pasteboard.md)  [@ohos.request (上传下载)](js-apis-request.md)  [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| BackgroundTasksKit | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md)  [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)  [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md)  [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| CalendarKit | [@ohos.calendarManager (日程管理能力)](js-apis-calendarmanager.md) |
| ConnectivityKit | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md)  [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md)  [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md)  [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md)  [nfctech (标准NFC-Tag Nfc 技术)](js-apis-nfctech.md)  [tagSession (标准NFC-Tag TagSession)](js-apis-tagsession.md) |
| ContactsKit | [@ohos.contact (联系人)](js-apis-contact.md) |
| ArkData | [@ohos.data.distributedData (分布式数据管理)](js-apis-distributed-data.md)  [@ohos.data.distributedDataObject (分布式数据对象)](js-apis-data-distributedobject.md)  [@ohos.data.distributedKVStore (分布式键值数据库)](js-apis-distributedkvstore.md) |
| MDMKit | [@ohos.enterprise.adminManager (admin权限管理)](js-apis-enterprise-adminmanager.md)  [@ohos.enterprise.deviceInfo（设备信息管理）](js-apis-enterprise-deviceinfo.md) |
| CoreFileKit | [@ohos.file.picker (选择器)](js-apis-file-picker.md) |
| MediaLibraryKit | [@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](js-apis-sendablephotoaccesshelper.md)  [@ohos.file.AlbumPickerComponent (Album Picker组件)](ohos-file-albumpickercomponent.md)  [@ohos.file.PhotoPickerComponent (PhotoPicker组件)](ohos-file-photopickercomponent.md)  [@ohos.file.RecentPhotoComponent (最近图片组件)](ohos-file-recentphotocomponent.md)  [@ohos.multimedia.movingphotoview (动态照片)](ohos-multimedia-movingphotoview.md) |
| PerformanceAnalysisKit | [@ohos.hidebug (Debug调试)](js-apis-hidebug.md) |
| AudioKit | [@ohos.multimedia.audio (音频管理)](arkts-apis-audio.md) |
| CameraKit | [@ohos.multimedia.cameraPicker (相机选择器)](js-apis-camerapicker.md)  [@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md) |
| AVSessionKit | [@ohos.multimedia.avCastPicker (投播组件)](ohos-multimedia-avcastpicker.md)  [@ohos.multimedia.avsession (媒体会话管理)](arkts-apis-avsession.md) |
| MediaKit | [@ohos.multimedia.media (媒体服务)](arkts-apis-media.md) |
| NotificationKit | [@ohos.notification (Notification模块)](js-apis-notification.md)  [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| TelephonyKit | [@ohos.telephony.call (拨打电话)](js-apis-call.md)  [@ohos.telephony.data (蜂窝数据)](js-apis-telephony-data.md)  [@ohos.telephony.observer (observer)](js-apis-observer.md)  [@ohos.telephony.radio (网络搜索)](js-apis-radio.md)  [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md)  [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
| UserAuthenticationKit | [@ohos.userIAM.userAuth (用户认证)](js-apis-useriam-userauth.md) |
| ArkUI | [@ohos.window (窗口)](arkts-apis-window.md) |
| MapKit | [sceneMap（场景化控件）](map-scenemap.md) |
| PaymentKit | [paymentService (鸿蒙支付服务)](payment-paymentservice.md) |
| ServiceCollaborationKit | [devicePicker (设备选择控制器)](servicecollaboration-devicepicker.md)  [CollaborationDevicePicker (流转控件)](servicecollaboration-collaborationdevicepicker.md) |
| ShareKit | [systemShare（分享）](share-system-share.md)  [harmonyShare（华为分享）](share-harmony-share.md) |
| VisionKit | [CardRecognition（卡证识别控件）](vision-card-recognition.md#section143611912403)  [DocumentScanner（文档扫描控件）](vision-document-scanner.md#section143611912403) |
| ScanKit | [Scan Kit（统一扫码服务）](scan-api.md) |
