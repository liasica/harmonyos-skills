---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability
title: "@ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)"
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2e96305e949dd0a17e9983e284d0f4565ef3e47273d628fbb6e58a31fb15e5d4
---

本模块实现故障的延迟通知功能。

[HiAppEvent](js-apis-hiviewdfx-hiappevent.md)订阅崩溃、应用冻屏事件时，只有当应用下次启动后才能接收上一次的事件。如果应用无法启动或长时间未打开，则存在故障无法及时上报的局限性。

本模块作为该场景的补充。在应用实现FaultLogExtensionAbility后，当应用发生崩溃或冻屏时，系统服务预计会在30分钟后拉起FaultLogExtensionAbility。

开发者可在[onFaultReportReady](js-apis-hiviewdfx-faultlogextensionability.md#onfaultreportready)中订阅并处理故障事件。

**说明** 

* 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 约束限制

为保障系统安全性和稳定性，防止FaultLogExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](js-apis-hiviewdfx-faultlogextensionability.md#附录)。

## 导入模块

```ts
import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';
```

## FaultLogExtensionAbility

应用接入故障延迟通知需要通过FaultLogExtensionAbility实现，开发者可以在[onFaultReportReady](js-apis-hiviewdfx-faultlogextensionability.md#onfaultreportready)中订阅并处理故障事件。

**注意** 

* FaultLogExtensionAbility被拉起后只有很短的时间完成故障处理，建议处理时间不要超过10秒。超时没有处理完成可以在[onDisconnect](js-apis-hiviewdfx-faultlogextensionability.md#ondisconnect)中保存状态。
* 从开机或上次拉起FaultLogExtensionAbility后，应用首次触发崩溃或冻屏开始计时。在拉起FaultLogExtensionAbility前反复触发崩溃或冻屏事件均不会重新计时。
* FaultLogExtensionAbility自身崩溃时，不会再次被系统服务拉起。

### 属性

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FaultLogExtensionContext](js-apis-hiviewdfx-faultlogextensioncontext.md) | 否 | 否 | FaultLogExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onConnect

onConnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成连接时调用此接口，用于执行初始化操作，该方法可选择性重写。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```ts
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onConnect() {
      console.info('onConnect');
    }
}
```

### onDisconnect

onDisconnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成断开连接时调用此接口，用于释放资源清理运行状态，该方法可选择性重写。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```ts
export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onDisconnect() {
      console.info('onDisconnect');
    }
}
```

### onFaultReportReady

onFaultReportReady(): void

FaultLogExtensionAbility回调。系统服务通知FaultLogExtensionAbility可以进行故障处理时，回调此接口，可以在该方法中订阅故障事件进行处理。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```ts
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';

export default class MyFaultLogExtension extends FaultLogExtensionAbility {
    onFaultReportReady() {
        hiAppEvent.addWatcher({
            name: "watcher",
            appEventFilters: [
                {
                    domain: hiAppEvent.domain.OS,
                    names: [hiAppEvent.event.APP_CRASH, hiAppEvent.event.APP_FREEZE]
                }
            ],
            onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
                // 进行故障事件处理
            }
        });
    }
}
```

## 附录

FaultLogExtensionAbility不支持以下模块的引用。

| Kit名称 | 模块名称 |
| --- | --- |
| AVSession Kit | [@ohos.multimedia.avsession (媒体会话管理)](arkts-apis-avsession.md) |
| Ability Kit | [@ohos.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) |
| ArkUI | [@ohos.window (窗口)](arkts-apis-window.md) |
| Audio Kit | [@ohos.multimedia.audio (音频管理)](arkts-apis-audio.md) |
| Background Tasks Kit | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md) |
| Background Tasks Kit | [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md) |
| Background Tasks Kit | [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| Background Tasks Kit | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md) |
| Basic Services Kit | [@ohos.power (系统电源管理)](js-apis-power.md) |
| Basic Services Kit | [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| Camera Kit | [@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md) |
| Camera Kit | [@ohos.multimedia.cameraPicker (相机选择器)](js-apis-camerapicker.md) |
| Connectivity Kit | [@ohos.wifiManager (WLAN)](js-apis-wifimanager.md) |
| Connectivity Kit | [@ohos.wifiManagerExt (WLAN扩展接口)](js-apis-wifimanagerext.md) |
| Connectivity Kit | [@ohos.wifiext (WLAN扩展接口)](js-apis-wifiext.md) |
| IME Kit | [@ohos.inputMethod (输入法框架)](js-apis-inputmethod.md) |
| Media Library Kit | [@ohos.multimedia.movingphotoview (动态照片)](ohos-multimedia-movingphotoview.md) |
| Notification Kit | [@ohos.notification (Notification模块)](js-apis-notification.md) |
| Notification Kit | [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| Sensor Service Kit | [@ohos.vibrator (振动)](js-apis-vibrator.md) |
| Telephony Kit | [@ohos.telephony.call (拨打电话)](js-apis-call.md) |
| Telephony Kit | [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md) |
| Telephony Kit | [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
| User Authentication Kit | [@ohos.userIAM.userAuth (用户认证)](js-apis-useriam-userauth.md) |
