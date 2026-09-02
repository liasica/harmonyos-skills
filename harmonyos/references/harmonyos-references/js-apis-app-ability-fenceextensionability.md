---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-fenceextensionability
title: "@ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)"
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > ArkTS API > @ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:15f9d5e39c2e2aa49ba337004c701c610fcdc20f3d27c5be60bf6b1c8d680736
---

FenceExtensionAbility为开发者提供的地理围栏相关的能力，继承自ExtensionAbility。

**说明** 

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { FenceExtensionAbility } from '@kit.LocationKit';
```

## 约束限制

为保障系统安全性和稳定性，防止FenceExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](js-apis-app-ability-fenceextensionability.md#附录)。

## FenceExtensionAbility

为开发者提供地理围栏相关的能力，继承自ExtensionAbility。

### 属性

**系统能力**：SystemCapability.Location.Location.Geofence

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FenceExtensionContext](js-apis-app-ability-fenceextensioncontext.md) | 否 | 否 | 围栏服务上下文。 |

### onFenceStatusChange

onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void

接收系统通知的地理围栏事件，根据围栏事件类型和数据进行相应处理。

**系统能力**：SystemCapability.Location.Location.Geofence

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | [geoLocationManager.GeofenceTransition](js-apis-geolocationmanager.md#geofencetransition12) | 是 | 地理围栏事件信息；包含地理围栏ID和具体的地理围栏事件。 |
| additions | Record<string, string> | 是 | 附加信息 |

**示例：**

```ts
import { FenceExtensionAbility, geoLocationManager } from '@kit.LocationKit';
import { notificationManager } from '@kit.NotificationKit';
import { Want, wantAgent } from '@kit.AbilityKit';

export class MyFenceExtensionAbility extends FenceExtensionAbility {
  onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void {
    // 接受围栏状态变化事件，处理业务逻辑
    console.info(`on geofence transition,id:${transition.geofenceId},event:${transition.transitionEvent},additions:${JSON.stringify(additions)}`);

    // 可以发送围栏业务通知
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      wants: [
        {
          bundleName: 'com.example.myapplication',
          abilityName: 'EntryAbility',
          parameters:
          {
            'geofenceId': transition?.geofenceId,
            'transitionEvent': transition?.transitionEvent,
          }
        } as Want
      ],
      actionType: wantAgent.OperationType.START_ABILITY,
      requestCode: 100
    };
    wantAgent.getWantAgent(wantAgentInfo).then((wantAgentMy) => {
      let notificationRequest: notificationManager.NotificationRequest = {
        id: 1,
        content: {
          notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
          normal: {
            title: `围栏通知`,
            text: `on geofence transition,id:${transition.geofenceId},event:${transition.transitionEvent},additions:${JSON.stringify(additions)}`,
          }
        },
        notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
        wantAgent: wantAgentMy
      };
      notificationManager.publish(notificationRequest);
    });
  }
}
```

### onDestroy

onDestroy(): void

接收FenceExtensionAbility的销毁事件并处理，会在FenceExtensionAbility销毁前回调。

**系统能力**：SystemCapability.Location.Location.Geofence

**模型约束**：此接口仅可在Stage模型下使用。

**示例：**

```ts
import { FenceExtensionAbility } from '@kit.LocationKit';

class MyFenceExtensionAbility extends FenceExtensionAbility {
  onDestroy(): void {
    // 处理ability销毁事件
    console.info(`on ability destroy`);
  }
}
```

## 附录

FenceExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit | [@ohos.ability.featureAbility (FeatureAbility模块)](js-apis-ability-featureability.md) |
| Ability Kit | [@ohos.ability.particleAbility (ParticleAbility模块)](js-apis-ability-particleability.md) |
| Ability Kit | [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](js-apis-launcherbundlemanager.md) |
| Ability Kit | [@ohos.continuation.continuationManager (流转/协同管理)](js-apis-continuation-continuationmanager.md) |
| Ability Kit | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) |
| AppGallery Kit | [privacyManager（隐私管理服务）](store-privacymanager.md) |
| ArkUI | [@ohos.window (窗口)](js-apis-window.md) |
| Audio Kit | [@ohos.multimedia.audio (音频管理)](js-apis-audio.md) |
| AVSession Kit | [@ohos.multimedia.avsession (媒体会话管理)](js-apis-avsession.md) |
| Background Tasks Kit | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md) |
| Background Tasks Kit | [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md) |
| Background Tasks Kit | [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| Background Tasks Kit | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md) |
| Basic Services Kit | [@ohos.account.appAccount (应用账号管理)](js-apis-appaccount.md) |
| Basic Services Kit | [@ohos.account.distributedAccount (分布式账号管理)](js-apis-distributed-account.md) |
| Basic Services Kit | [@ohos.account.osAccount (系统账号管理)](js-apis-osaccount.md) |
| Basic Services Kit | [@ohos.deviceInfo (设备信息)](js-apis-device-info.md) |
| Basic Services Kit | [@ohos.request (上传下载)](js-apis-request.md) |
| Basic Services Kit | [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| Camera Kit | [@ohos.multimedia.camera (相机管理)](js-apis-camera.md) |
| Contacts Kit | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md) |
| Contacts Kit | [@ohos.contact (联系人)](js-apis-contact.md) |
| Connectivity Kit | [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md) |
| Connectivity Kit | [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md) |
| Connectivity Kit | [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md) |
| Connectivity Kit | [nfctech (标准NFC-Tag Nfc 技术)](js-apis-nfctech.md) |
| Connectivity Kit | [tagSession (标准NFC-Tag TagSession)](js-apis-tagsession.md) |
| Form Kit | [@ohos.application.formError (formError)](js-apis-application-formerror.md) |
| MDM Kit | [@ohos.enterprise.adminManager（admin权限管理）](js-apis-enterprise-adminmanager.md) |
| Media Kit | [@ohos.multimedia.media (媒体服务)](js-apis-media.md) |
| Performance Analysis Kit | [@ohos.hidebug (Debug调试)](js-apis-hidebug.md) |
| Sensor Service Kit | [@ohos.vibrator (振动)](js-apis-vibrator.md) |
| Telephony Kit | [@ohos.telephony.call (拨打电话)](js-apis-call.md) |
| Telephony Kit | [@ohos.telephony.data (蜂窝数据)](js-apis-telephony-data.md) |
| Telephony Kit | [@ohos.telephony.observer (observer)](js-apis-observer.md) |
| Telephony Kit | [@ohos.telephony.radio (网络搜索)](js-apis-radio.md) |
| Telephony Kit | [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md) |
| Telephony Kit | [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
| User Authentication Kit | [@ohos.userIAM.userAuth (用户认证)](js-apis-useriam-userauth.md) |
