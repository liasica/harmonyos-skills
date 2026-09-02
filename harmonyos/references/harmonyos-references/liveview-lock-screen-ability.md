---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-lock-screen-ability
title: LiveViewLockScreenExtensionAbility
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > LiveViewLockScreenExtensionAbility
category: harmonyos-references
scraped_at: 2026-09-02T14:53:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:057189e4f6a5899fe5bc802ea5b73631a5f9b378be7c96938db79b214be36b60
---

LiveViewLockScreenExtensionAbility为[锁屏沉浸实况窗](../design-guides/system-features-live-view-0000001955186861.md#section553375320)可视化区的[ExtensionAbility](../harmonyos-guides/extensionability-overview.md)组件，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)，适用于需要在锁屏状态下展示丰富内容的实时活动场景。开发者通过继承该类并实现应用的扩展组件，可以在用户未解锁屏幕的情况下，在锁屏界面以可视化形式呈现更多的数据情况以及提供更多快速操作。

**起始版本：** 5.0.0(12)

## 约束限制

* LiveViewLockScreenExtensionAbility为独立子进程，不能跨进程拉起其他Ability。
* 为保障系统安全性和稳定性，防止LiveViewLockScreenExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](liveview-lock-screen-ability.md#附录)。

## 导入模块

```typescript
import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
```

**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

## LiveViewLockScreenExtensionAbility

锁屏沉浸实况窗扩展Ability，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [LiveViewLockScreenExtensionContext](liveview-lock-screen-context.md) | 否 | 否 | LiveViewLockScreenExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

## 示例

```typescript
import { LiveViewLockScreenExtensionAbility } from '@kit.LiveViewKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class LiveViewLockScreenExtAbility extends LiveViewLockScreenExtensionAbility {
  onCreate(): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onCreate begin.');
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession): void {
    hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onSessionCreate begin.');
    let param: Record<string, UIExtensionContentSession> = {
      'session': session
    };
    let storage: LocalStorage = new LocalStorage(param);

    // 解析从liveViewLocalScreenAbilityParameters中传入的参数
    const parameters = want?.parameters;
    let words: string = parameters?.['words'] ? parameters?.['words'] as string : 'Hello World!';
    storage.setOrCreate('words', words);

    // 加载锁屏沉浸实况窗页面
    session.loadContent('pages/LiveViewLockScreenPage', storage);
  }
}
```

## 附录

LiveViewLockScreenExtensionAbility不允许调用的API名单如下。

| Kit名称 | 模块名称 |
| --- | --- |
| Ability Kit | [@ohos.ability.featureAbility (FeatureAbility模块)](js-apis-ability-featureability.md)  [@ohos.ability.particleAbility (ParticleAbility模块)](js-apis-ability-particleability.md)  [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](js-apis-launcherbundlemanager.md)  [@ohos.continuation.continuationManager (流转/协同管理)](js-apis-continuation-continuationmanager.md) |
| AppGallery Kit | [privacyManager（隐私管理服务）](store-privacymanager.md) |
| ArkData | [@ohos.data.distributedData (分布式数据管理)](js-apis-distributed-data.md)  [@ohos.data.distributedDataObject (分布式数据对象)](js-apis-data-distributedobject.md)  [@ohos.data.distributedKVStore (分布式键值数据库)](js-apis-distributedkvstore.md) |
| ArkUI | [@ohos.window (窗口)](arkts-apis-window.md) |
| Audio Kit | [@ohos.multimedia.audio (音频管理)](arkts-apis-audio.md) |
| AVSession Kit | [@ohos.multimedia.avsession (媒体会话管理)](arkts-apis-avsession.md)  [@ohos.multimedia.avCastPicker (投播组件)](ohos-multimedia-avcastpicker.md) |
| Background Tasks Kit | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md)  [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)  [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md)  [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| Basic Services Kit | [@ohos.account.appAccount (应用账号管理)](js-apis-appaccount.md)  [@ohos.account.distributedAccount (分布式账号管理)](js-apis-distributed-account.md)  [@ohos.account.osAccount (系统账号管理)](js-apis-osaccount.md)  [@ohos.request (上传下载)](js-apis-request.md)  [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md)  [@ohos.pasteboard (剪贴板)](js-apis-pasteboard.md) |
| Calendar Kit | [@ohos.calendarManager (日程管理能力)](js-apis-calendarmanager.md) |
| Camera Kit | [@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md)  [@ohos.multimedia.cameraPicker (相机选择器)](js-apis-camerapicker.md) |
| Connectivity Kit | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md)  [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md)  [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md)  [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md)  [nfctech (标准NFC-Tag Nfc 技术)](js-apis-nfctech.md)  [tagSession (标准NFC-Tag TagSession)](js-apis-tagsession.md) |
| Contacts Kit | [@ohos.contact (联系人)](js-apis-contact.md) |
| Core File Kit | [@ohos.file.picker (选择器)](js-apis-file-picker.md) |
| Form Kit | [@ohos.app.form.formInfo (formInfo)](js-apis-app-form-forminfo.md#forminfo)  [@ohos.application.formError (formError)](js-apis-application-formerror.md) |
| Map Kit | [sceneMap（场景化控件）](map-scenemap.md) |
| MDM Kit | [@ohos.enterprise.adminManager (admin权限管理)](js-apis-enterprise-adminmanager.md)  [@ohos.enterprise.deviceInfo（设备信息管理）](js-apis-enterprise-deviceinfo.md) |
| Media Kit | [@ohos.multimedia.media (媒体服务)](arkts-apis-media.md) |
| Media Library Kit | [@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](js-apis-sendablephotoaccesshelper.md)  [@ohos.file.AlbumPickerComponent (Album Picker组件)](ohos-file-albumpickercomponent.md)  [@ohos.file.PhotoPickerComponent (PhotoPicker组件)](ohos-file-photopickercomponent.md)  [@ohos.file.RecentPhotoComponent (最近图片组件)](ohos-file-recentphotocomponent.md)  [@ohos.multimedia.movingphotoview (动态照片)](ohos-multimedia-movingphotoview.md)  [@ohos.file.photoAccessHelper (相册管理模块)](js-apis-photoaccesshelper.md) |
| Notification Kit | [@ohos.notification (Notification模块)](js-apis-notification.md)  [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| Payment Kit | [paymentService (鸿蒙支付服务)](payment-paymentservice.md) |
| Performance Analysis Kit | [@ohos.hidebug (Debug调试)](js-apis-hidebug.md) |
| Scan Kit | [customScan (自定义界面扫码)](scan-customscan-api.md)  [detectBarcode (图像识码)](scan-imagedecode.md)  [generateBarcode (码图生成)](scan-generatebarcode.md)  [scanBarcode (默认界面扫码)](scan-scanbarcode-api.md)  [scanCore (扫码公共信息)](scan-scancore.md) |
| Sensor Service Kit | [@ohos.vibrator (振动)](js-apis-vibrator.md) |
| Service Collaboration Kit | [devicePicker (设备选择控制器)](servicecollaboration-devicepicker.md)  [CollaborationDevicePicker (流转控件)](servicecollaboration-collaborationdevicepicker.md) |
| Share Kit | [systemShare（分享）](share-system-share.md)  [harmonyShare（华为分享）](share-harmony-share.md) |
| Telephony Kit | [@ohos.telephony.call (拨打电话)](js-apis-call.md)  [@ohos.telephony.data (蜂窝数据)](js-apis-telephony-data.md)  [@ohos.telephony.observer (observer)](js-apis-observer.md)  [@ohos.telephony.radio (网络搜索)](js-apis-radio.md)  [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md)  [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
| User Authentication Kit | [@ohos.userIAM.userAuth (用户认证)](js-apis-useriam-userauth.md) |
| Vision Kit | [CardRecognition（卡证识别控件）](vision-card-recognition.md)  [DocumentScanner（文档扫描控件）](vision-document-scanner.md) |
