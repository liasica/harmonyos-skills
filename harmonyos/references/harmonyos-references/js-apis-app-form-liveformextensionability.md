---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-liveformextensionability
title: "@ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)"
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > @ohos.app.form.LiveFormExtensionAbility (LiveFormExtensionAbility)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4282b281221c8f9385442c2d11dc6905bcc2bcd6351bf7d858ba3b6e526a5de6
---

LiveFormExtensionAbility（互动卡片扩展能力）模块提供互动卡片功能，包括接收创建和销毁互动卡片的通知等，继承自[ExtensionAbility](js-apis-app-ability-extensionability.md)。

**说明** 

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 约束限制

为保障系统安全性和稳定性，防止LiveFormExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](js-apis-app-form-liveformextensionability.md#附录)。

## 导入模块

```ts
import { LiveFormExtensionAbility } from '@kit.FormKit';
```

## LiveFormExtensionAbility

互动卡片扩展类，用于实现互动卡片的提供方功能。包含互动卡片提供方接收创建和销毁互动卡片的通知接口，开发者可在这些回调中实现卡片的初始化、数据绑定、资源清理等逻辑。[onLiveFormCreate](js-apis-app-form-liveformextensionability.md#onliveformcreate)在用户切换互动卡片状态为激活态时触发，用于初始化和数据绑定；[onLiveFormDestroy](js-apis-app-form-liveformextensionability.md#onliveformdestroy)在用户切换互动卡片状态为非激活态时触发，用于资源清理。两者形成完整的生命周期管理，应确保在create中分配的资源在destroy中正确释放。

### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [LiveFormExtensionContext](js-apis-application-liveformextensioncontext.md) | 否 | 否 | LiveFormExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onLiveFormCreate

onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void

LiveFormExtensionAbility实例创建完成的回调。当用户切换到互动卡片激活态时，系统会自动调用此回调，开发者可在此回调中进行卡片初始化、数据绑定等操作。

**配对调用：**

* 与onLiveFormDestroy()方法成对使用，构成完整的互动卡片生命周期。
* 当互动卡片切换为非激活态时，系统会自动调用onLiveFormDestroy()进行资源清理。
* 开发者应确保在onLiveFormCreate中申请的资源在onLiveFormDestroy中正确释放，避免内存泄漏。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](js-apis-app-form-liveformextensionability.md#liveforminfo) | 是 | 互动卡片信息，用于标识处于激活态的互动卡片，包括卡片id等信息。 |
| session | [UIExtensionContentSession](js-apis-app-ability-uiextensioncontentsession.md) | 是 | LiveFormExtensionAbility的界面会话对象，用于管理与卡片的交互会话。 |

**示例：**

```ts
import { UIExtensionContentSession } from '@kit.AbilityKit';
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
    console.info(TAG, `onLiveFormCreate, formId: ${liveFormInfo.formId}`);
  }
}
```

### onLiveFormDestroy

onLiveFormDestroy(liveFormInfo: LiveFormInfo): void

LiveFormExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| liveFormInfo | [LiveFormInfo](js-apis-app-form-liveformextensionability.md#liveforminfo) | 是 | 互动卡片信息，用于标识处于非激活态的互动卡片，包括卡片id等信息。 |

**示例：**

```ts
import { LiveFormExtensionAbility, LiveFormInfo } from '@kit.FormKit';

const TAG: string = '[testTag] LiveFormExtAbility';

export default class LiveFormExtAbility extends LiveFormExtensionAbility {
  onLiveFormDestroy(liveFormInfo: LiveFormInfo) {
    console.info(TAG, `onLiveFormDestroy, liveFormInfo: ${liveFormInfo.formId}`);
  }
}
```

## LiveFormInfo

互动卡片信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formId | string | 否 | 否 | 卡片id。 |
| rect | [formInfo.Rect](js-apis-app-form-forminfo.md#rect20) | 否 | 否 | 卡片位置和大小信息。 |
| borderRadius | number | 否 | 否 | 卡片圆角半径信息。取值大于等于0，单位vp。 |

## 附录

LiveFormExtensionAbility不支持以下模块的引用。

| Kit名称 | 模块名称 |
| --- | --- |
| AbilityKit | [Context (Stage模型的上下文基类)](js-apis-inner-application-context.md)  [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)  [@ohos.ability.featureAbility (FeatureAbility模块)](js-apis-ability-featureability.md)  [@ohos.ability.particleAbility (ParticleAbility模块)](js-apis-ability-particleability.md)  [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](js-apis-launcherbundlemanager.md)  [@ohos.continuation.continuationManager (流转/协同管理)](js-apis-continuation-continuationmanager.md) |
| BasicServicesKit | [@ohos.account.appAccount (应用账号管理)](js-apis-appaccount.md)  [@ohos.account.distributedAccount (分布式账号管理)](js-apis-distributed-account.md)  [@ohos.account.osAccount (系统账号管理)](js-apis-osaccount.md)  [@ohos.pasteboard (剪贴板)](js-apis-pasteboard.md)  [@ohos.request (上传下载)](js-apis-request.md)  [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| BackgroundTasksKit | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md)  [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)  [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md)  [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| CalendarKit | [@ohos.calendarManager (日程管理能力)](js-apis-calendarmanager.md) |
| ConnectivityKit | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md)  [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md)  [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md)  [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md)  [nfctech (标准NFC-Tag Nfc 技术)](js-apis-nfctech.md)  [tagSession (标准NFC-Tag TagSession)](js-apis-tagsession.md) |
| ContactsKit | [@ohos.contact (联系人)](js-apis-contact.md) |
| ArkData | [@ohos.data.distributedData (分布式数据管理)](js-apis-distributed-data.md)  [@ohos.data.distributedDataObject (分布式数据对象)](js-apis-data-distributedobject.md)  [@ohos.data.distributedKVStore (分布式键值数据库)](js-apis-distributedkvstore.md) |
| MDMKit | [@ohos.enterprise.adminManager（admin权限管理）](js-apis-enterprise-adminmanager.md)  [@ohos.enterprise.deviceInfo（设备信息管理）](js-apis-enterprise-deviceinfo.md) |
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
| VisionKit | [CardRecognition（卡证识别控件）](vision-card-recognition.md)  [DocumentScanner（文档扫描控件）](vision-document-scanner.md) |
| ScanKit | [Scan Kit（统一扫码服务）](scan-api.md) |
