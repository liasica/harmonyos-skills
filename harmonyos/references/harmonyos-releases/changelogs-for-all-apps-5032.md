---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-5032
title: OS平台API行为的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.3(15) Beta2引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:30+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dc3a9b79d56683c831cc5748fc9562c422e4a44395cb510c9bfd0f7db0835c35
---

## ArkUI

### Image、Text和ListItem组件onDragStart接口默认行为变更

**变更原因**

Image、Text和ListItem组件存在设置onDragStart接口DragItemInfo返回值中的builder属性后，返回值中pixelMap和extraInfo属性不生效的问题。

**变更影响**

此变更涉及应用适配，只涉及Image、Text和ListItem组件。

* 变更前：onDragStart接口设置返回值中的builder属性后，无法解析pixelMap和extraInfo属性。同时设置了builder和pixelMap时，拖拽显示的是builder的预览图。onDrop回调中无法获取extraParams参数的值（对应extraInfo）。
* 变更后：onDragStart接口设置返回值中的builder属性后，能够解析pixelMap和extraInfo属性。同时设置了builder和pixelMap时，拖拽显示的是pixelMap的预览图。onDrop回调中能够获取extraParams参数的值（对应extraInfo）。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

**起始API Level**

11

**变更的接口/组件**

涉及组件：Image、Text和ListItem。

涉及接口： onDragStart(event: (event: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo)

**适配指导**

onDragStart接口的返回值用于指定拖拽过程中显示的图片(pixelMap，builder)以及拖拽过程中组件携带的额外信息(extraInfo)。变更后，pixelMap属性能够正常解析。由于pixelMap的优先级高于builder，如果同时设置了pixelMap和builder，应移除返回值中的pixelMap属性。同样，若不打算传递extraInfo，也应删除该属性。具体实现代码如下：

```
1. @Entry
2. @Component
3. struct SlideExample {
4. build() {
5. Row() {
6. Image()
7. .onDragStart((event) => {
8. return {
9. builder: () => { this.pixelMapBuilder() },
10. // 若需要拖拽显示builder，需要移除掉pixelMap属性的赋值。
11. // pixelMap:this.pixelMap,
12. // 若设置了builder并且不需要传递extraInfo，需要移除掉extraInfo属性的赋值。
13. // extraInfo: "test"
14. }
15. })
16. }.height('100%')
17. }
18. }
```

### 轴事件支持BEGIN、END及CANCEL类型回调触发

**变更原因**

开发者无法监听到轴事件的BEGIN、END、CANCEL类型的事件回调。

**变更影响**

此变更不涉及应用适配。

变更前：开发者通过OH\_NativeXComponent\_RegisterUIInputEventCallback接口监听轴事件回调，无法收到BEGIN、END、CANCEL类型的事件回调。

变更后：开发者通过OH\_NativeXComponent\_RegisterUIInputEventCallback接口监听轴事件回调，可以收到BEGIN、END、CANCEL类型的事件回调。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

**起始API Level**

12

**变更的接口/组件**

OH\_NativeXComponent\_RegisterUIInputEventCallback接口。

**适配指导**

默认行为变更，无需适配。

### TextController的SetStyledString接口支持保存设置的属性字符串信息到调用的TextController中

**变更原因**

优化属性字符串与Text组件的绑定时机。

**变更影响**

此变更涉及应用适配。

* 变更前：开发者调用TextController的setStyledString接口设置属性字符串时，如果调用时TextController还未绑定对应的Text，则此次设置无效。
* 变更后：开发者调用TextController的setStyledString接口时，调用的TextController会保存设置的属性字符串。当TextController和Text绑定时，如果TextController中已经存储之前调用setStyledString接口保存的属性字符串，则Text会自动设置保存的属性字符串，显示出对应的属性字符串。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

**起始API Level**

12

**适配指导**

变更后对setStyledString的接口的调用可以更加灵活，Text能够正确地显示出属性字符串。

```
1. @Entry
2. @Component
3. struct StyledStringExample {
4. controller: TextController = new TextController()

6. aboutToAppear(): void {
7. this.controller.setStyledString(new StyledString("123456")) // 变更前，由于此时controller还未和Text绑定，此次设置不生效。变更后，属性字符串可以正确的显示
8. }

10. build() {
11. Row() {
12. Column() {
13. Text(undefined, {controller: this.controller})
14. }.width('100%')
15. }.height('100%')
16. }
17. }
```

### PC/2in1设备上，悬浮窗层级由低于dock栏调整为高于dock栏

**变更原因**

应用创建的TYPE\_FLOAT类型的悬浮窗，因为层级低于Dock，会被Dock栏遮挡，在视频会议等场景，体验不符合应用预期。

**变更影响**

此变更不涉及应用适配。

* 变更前：在PC/2in1设备上，TYPE\_FLOAT类型的悬浮窗层级在dock栏之下。
* 变更后：在PC/2in1设备上，TYPE\_FLOAT类型的悬浮窗层级在dock栏之上。

**起始API Level**

9

**变更的接口/组件**

@ohos.window.d.ts

接口：TYPE\_FLOAT

**适配指导**

默认行为变更，无需适配。

## Call Service Kit

### 通话应用在前台时不显示通话胶囊

**变更原因**

通话体验优化。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

变更前：通话中，即使应用在前台，也会显示通话胶囊，点击通话胶囊可以返回通话界面。

变更后：通话中，如果应用在前台，不会显示通话胶囊；如果应用在前台，但不在通话界面，则需要应用通过显示画中画界面自行实现返回通话界面的功能，如图所示。

| 变更前 | 变更后（应用前台但非通话界面） |
| --- | --- |
|  |  |

**起始API Level**

4.1.0(11)

**变更的接口/组件**

voipCall.reportIncomingCall（上报来电）

voipCall.reportOutgoingCall（上报去电）

**适配指导**

通话中，如果应用是非通话界面在前台，则需要显示画中画界面用于返回通话界面，详见在应用程序中使用[画中画功能](../harmonyos-guides/window-pipwindow.md)。

## Performance Analysis Kit

### HiAppEvent模块onReceive、OH\_HiAppEvent\_OnReceive、takeNext接口支持应用分身故障日志订阅隔离

**变更原因**

应用分身从设计原则上要求数据隔离，当前应用分身的故障日志和主应用未进行隔离，不易于对分身应用的日志维护。

**变更影响**

此变更不涉及应用适配

变更前：hiappevent在主应用、分身应用可以同时获取到主应用和分身应用的故障日志。

变更后：hiappevent在主应用仅可以获取到主应用的故障日志，分身应用仅可以获取到分身应用的故障日志。

**起始API Level**

* takeNext接：9
* onReceive：11
* OH\_HiAppEvent\_OnReceive：12

**变更的接口/组件**

@ohos.hiviewdfx.hiAppEvent.d.ts中的[onReceive](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#watcher)、[takeNext](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#takenext)接口。

hiappevent.h中的[OH\_HiAppEvent\_OnReceive](../harmonyos-references/capi-hiappevent-h.md#oh_hiappevent_onreceive)接口。

**适配指导**

默认行为变更，无需适配。
