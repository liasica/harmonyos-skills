---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability
title: @ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f09426eef6240f7e1eef42dd330ef82396d6a116dfdcfeeaf92ebf135d79c187
---

本模块实现故障的延迟通知功能。

[HiAppEvent](js-apis-hiviewdfx-hiappevent.md)订阅崩溃、应用冻屏事件时，只有当应用下次启动后才能接收上一次的事件。如果应用无法启动或长时间未打开，则存在故障无法及时上报的局限性。

本模块作为该场景的补充。在应用实现FaultLogExtensionAbility后，当应用发生崩溃或冻屏时，系统服务预计会在30分钟后拉起FaultLogExtensionAbility。

开发者可在[onFaultReportReady](js-apis-hiviewdfx-faultlogextensionability.md#onfaultreportready)中订阅并处理故障事件。

说明

* 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块设置了不允许调用的API名单，调用名单中的API将导致功能异常，详情请参见[附录](js-apis-hiviewdfx-faultlogextensionability.md#附录)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FaultLogExtensionAbility } from '@kit.PerformanceAnalysisKit';
```

## FaultLogExtensionAbility

PhonePC/2in1TabletTVWearable

应用接入故障延迟通知需要通过FaultLogExtensionAbility实现，开发者可以在[onFaultReportReady](js-apis-hiviewdfx-faultlogextensionability.md#onfaultreportready)中订阅并处理故障事件。

注意

* FaultLogExtensionAbility被拉起后只有很短的时间完成故障处理，建议处理时间不要超过10秒。超时没有处理完成可以在[onDisconnect](js-apis-hiviewdfx-faultlogextensionability.md#ondisconnect)中保存状态。
* 从开机或上次拉起FaultLogExtensionAbility后，应用首次触发崩溃或冻屏开始计时。在拉起FaultLogExtensionAbility前反复触发崩溃或冻屏事件均不会重新计时。
* FaultLogExtensionAbility自身崩溃时，不会再次被系统服务拉起。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FaultLogExtensionContext](js-apis-hiviewdfx-faultlogextensioncontext.md) | 否 | 否 | FaultLogExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onConnect

PhonePC/2in1TabletTVWearable

onConnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成连接时调用此接口，用于执行初始化操作，该方法可选择性重写。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```
1. export default class MyFaultLogExtension extends FaultLogExtensionAbility {
2. onConnect() {
3. console.info('onConnect');
4. }
5. }
```

### onDisconnect

PhonePC/2in1TabletTVWearable

onDisconnect(): void

FaultLogExtensionAbility生命周期回调。当系统服务完成断开连接时调用此接口，用于释放资源清理运行状态，该方法可选择性重写。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```
1. export default class MyFaultLogExtension extends FaultLogExtensionAbility {
2. onDisconnect() {
3. console.info('onDisconnect');
4. }
5. }
```

### onFaultReportReady

PhonePC/2in1TabletTVWearable

onFaultReportReady(): void

FaultLogExtensionAbility回调。系统服务通知FaultLogExtensionAbility可以进行故障处理时，回调此接口，可以在该方法中订阅故障事件进行处理。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**示例：**

```
1. import { hiAppEvent } from '@kit.PerformanceAnalysisKit';

3. export default class MyFaultLogExtension extends FaultLogExtensionAbility {
4. onFaultReportReady() {
5. hiAppEvent.addWatcher({
6. name: "watcher",
7. appEventFilters: [
8. {
9. domain: hiAppEvent.domain.OS,
10. names: [hiAppEvent.event.APP_CRASH, hiAppEvent.event.APP_FREEZE]
11. }
12. ],
13. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
14. // 进行故障事件处理
15. }
16. });
17. }
18. }
```

## 附录

PhonePC/2in1TabletTVWearable

本模块不允许调用的API名单如下。

| Kit名称 | 模块名称 |
| --- | --- |
| AVSessionKit | [@ohos.multimedia.avsession (媒体会话管理)](arkts-apis-avsession.md) |
| AbilityKit | [@ohos.UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) |
| ArkUI | [@ohos.window (窗口)](arkts-apis-window.md) |
| AudioKit | [@ohos.multimedia.audio (音频管理)](arkts-apis-audio.md) |
| BackgroundTasksKit | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md) |
| BackgroundTasksKit | [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md) |
| BackgroundTasksKit | [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| BackgroundTasksKit | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md) |
| BasicServicesKit | [@ohos.power (系统电源管理)](js-apis-power.md) |
| BasicServicesKit | [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| CameraKit | [@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md) |
| CameraKit | [@ohos.multimedia.cameraPicker (相机选择器)](js-apis-camerapicker.md) |
| ConnectivityKit | [@ohos.wifiManager (WLAN)](js-apis-wifimanager.md) |
| ConnectivityKit | [@ohos.wifiManagerExt (WLAN扩展接口)](js-apis-wifimanagerext.md) |
| ConnectivityKit | [@ohos.wifiext (WLAN扩展接口)](js-apis-wifiext.md) |
| IMEKit | [@ohos.inputMethod (输入法框架)](js-apis-inputmethod.md) |
| MediaLibraryKit | [@ohos.multimedia.movingphotoview (动态照片)](ohos-multimedia-movingphotoview.md) |
| NotificationKit | [@ohos.notification (Notification模块)](js-apis-notification.md) |
| NotificationKit | [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| SensorServiceKit | [@ohos.vibrator (振动)](js-apis-vibrator.md) |
| TelephonyKit | [@ohos.telephony.call (拨打电话)](js-apis-call.md) |
| TelephonyKit | [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md) |
| TelephonyKit | [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
| UserAuthenticationKit | [@ohos.userIAM.userAuth (用户认证)](js-apis-useriam-userauth.md) |
