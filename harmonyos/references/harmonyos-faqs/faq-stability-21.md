---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-21
title: 点击保存按钮应用无响应
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 点击保存按钮应用无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c076c3b41e38dd91cff5dec015e68f50a34604227cf2a9bc00b1b25b2950f570
---

## 问题现象

点击页面上的按钮，应用没有响应，随后应用闪退。

## 背景知识

* Kill Reason:ClearSession任务栏杀掉应用。
* [安全控件](../harmonyos-guides/security-component-overview.md)是系统提供的一组ArkUI基础组件，包括保存控件和粘贴控件。它们可以作为一种“特殊的按钮”融入应用页面，实现用户“点击即许可”的设计思路。
* 由于安全控件具有点击即授权的特性，为了保障用户的隐私不被恶意应用获取，系统针对安全控件做了很多的限制。应用开发者需保证安全控件在应用界面上清晰可见、用户能明确识别，防止因覆盖、混淆等因素导致授权失败，具体可以参考[安全控件约束和限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

## 问题定位

1. 查看faultlogger目录，没有和应用相关的故障日志。
2. 在hilog日志中搜索关键字kill Reason，可以看到应用退出原因是ClearSession，任务栏杀掉应用退出的。

   ```txt
   07-06 22:49:21.426 52117 52131 I C05A05/security_component_service/SecCompManager: [NotifyProcessBackground]App pid 51834 to background
   07-06 22:49:21.426  1073 59745 I C01702/resource_schedule_service/CgroupAdjuster: AdjustProcessGroup for 51834, source : 20
   07-06 22:49:21.427 51834 51834 I C02C11/应用包名/APPSPAWN: [appspawn_server.c:46]App exit code: 0
   07-06 22:49:21.427  1928 59832 W C01311/foundation/AppMS: [app_mgr_service_inner.cpp:1572]hisysevent write result=0, send [FRAMEWORK,PROCESS_KILL], pid=51834, processName=应用包名, msg=Kill Reason:ClearSession, FOREGROUND = 0
   07-06 22:49:21.428  1928 59778 W C01335/foundation/Connection: [connection_state_manager.cpp:404]callerPid:51834
   ```
3. 搜索关键字click accepted，可以看到应用在退出之前点击了关闭按钮，应用是点击关闭按钮退出的，并没有发生闪退。

   ```txt
   07-06 22:49:21.394 51834 51834 I C0391E/应用包名/AceGesture: [(100000:100000:scope)] Click try accept
   07-06 22:49:21.394 51834 51834 I C03951/应用包名/InputKeyFlow: [(100000:100000:scope)] Click accepted, tag: Button
   07-06 22:49:21.394  1073 59746 I C01718/resource_schedule_service/StandbyService: [HandleCommonEvent:1244] HandleCommonEvent resType = 9, value = 3, sceneInfo = {"callingUid":"20020208","clientPid":"51834","name":"touch","up_speed":"0.000000"}
   07-06 22:49:21.394 51834 51834 I C03952/应用包名/AceAppBar: [(100000:100000:scope)] callNative
   07-06 22:49:21.394 51834 51834 I C03952/应用包名/AceAppBar: [(100000:100000:scope)] OnCloseBtnClick
   07-06 22:49:21.394 51834 51834 I C03952/应用包名/AceAppBar: [(100000:100000:scope)] close button clicked
   ```
4. 继续查看点击事件，可以看到在点击关闭按钮之前，用户点击了保存按钮。

   ```txt
   07-06 22:49:21.145 51834 51834 I C0391E/应用包名/AceGesture: [(100000:100000:scope)] Click try accept
   07-06 22:49:21.145 51834 51834 I C03951/应用包名/InputKeyFlow: [(100000:100000:scope)] Click accepted, tag: SaveButton
   07-06 22:49:21.146  1073 59304 I C01718/resource_schedule_service/StandbyService: [HandleCommonEvent:1244] HandleCommonEvent resType = 9, value = 3, sceneInfo = {"callingUid":"20020208","clientPid":"51834","name":"touch","up_speed":"0.000000"}
   07-06 22:49:21.146  1073 59304 I C01718/resource_schedule_service/StandbyService: [HandleCommonEvent:1244] HandleCommonEvent resType = 9, value = 2, sceneInfo = {"callingUid":"20020208","clientPid":"51834","name":"click"}
   07-06 22:49:21.147 51834 51834 I C0421A/应用包名/WMSLayoutPc: [] GetCrossAxisState(3427): window id is 112, state is 0
   ```
5. 查看点击保存按钮之后的日志，可以发现保存按钮不符合安全控件约束，错误信息是security component is out of screen。安全控件超出了屏幕范围，导致授权失败，点击安全控件没有响应。

   ```txt
   07-06 22:49:21.148 52117 52117 I C05A05/security_component_service/WindowInfoHelper: [GetWindowScale]Get scale 1.000000
   07-06 22:49:21.149 52117 52117 E C05A05/security_component_service/SecCompInfoHelper: [CheckRectValid]SecurityComponentCheckFail: security component is out of screen
   07-06 22:49:21.149 52117 52117 E C05A05/security_component_service/SecCompManager: [CheckClickSecurityComponentInfo]compare component info failed.
   07-06 22:49:21.150 51834 51834 I C05A05/应用包名/SecCompClientEnhanceImpl: [EnhanceClientDeserialize]Client sessionInfo updated: pid=51834, sessionId=3616639695, seqNum=******033.
   07-06 22:49:21.150 51834 51834 E C05A05/应用包名/SecCompKit: [ReportSecurityComponentClickEvent]report click event fail, error: -56
   07-06 22:49:21.150 51834 51834 W C03956/应用包名/AceSecurityComponent: [(100000:100000:scope)] ReportSecurityComponentClickEvent failed, errno -56
   07-06 22:49:21.150 51834 51834 I C03951/应用包名/InputKeyFlow: [(100000:100000:scope)] id: 0, log: {types: Click, node: SaveButton, prcd: Down, state: READY, prcd: Up, state: SUCCEED}
   07-06 22:49:21.150 51834 51834 I C03919/应用包名/AceInputTracking: [(100000:100000:scope)] Consumed new event id=102139 in ace_container, lastEventInfo: id:102138
   07-06 22:49:21.150 51834 51834 I C03956/应用包名/AceSecurityComponent: [(100000:100000:scope)] Security component frameNode cached size: 1, index: 19
   ```

## 分析结论

安全控件超出屏幕范围导致点击无响应。

## 修改建议

参考SaveButton[示例1](../harmonyos-references/ts-security-components-savebutton.md#示例1)，调整安全控件位置和大小，使其符合[安全控件约束和限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

```typescript
@Entry
@Component
struct SaveButtonPage {
  build() {
    Row() {
      Column({ space: 10 }) {
        SaveButton({ text: SaveDescription.SAVE })
          .size({ width: 60, height: 30 });
      }.width('100%');
    }.height('100%');
  }
}
```
