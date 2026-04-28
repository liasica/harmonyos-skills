---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-6001
title: UX样式或效果的变更
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > OS平台行为变更说明 > 6.0.0(20) Beta1引入的行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1e32981aa9a56e2bef51257c10f05641791064d01f0429a3a6666e826b8abe84
---

## bindSheet在2in1设备中默认避让窗口安全区

**变更原因**

UX规格变更。

半模态内容需默认避让窗口安全区，否则会有重叠区域。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

**变更影响**

此变更涉及应用适配。

当自由窗口标题栏类型为悬浮标题栏时，需要半模态面板默认避让标题安全区。

场景1：半模态居中弹窗样式

* 变更前：半模态居中弹窗样式的面板最大高度为窗口高度的90%。
* 变更后：该样式的最大高度为窗口高度 - (窗口安全区高度 + 安全间距8vp) \* 2。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

场景2：半模态底部弹窗样式

* 变更前：半模态底部弹窗样式的面板最大高度为窗口高度 - 8vp。
* 变更后：该样式的最大高度为窗口高度 - (窗口安全区高度 + 安全间距8vp)。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

11

**变更的接口/组件**

bindSheet的preferType属性

**适配指导**

若开发者自定义的builder面板内容是固定高度，建议使用100%布局，变更后自定义的内容也可以自动撑满半模态面板。

若按变更前的最大高度规格限制的builder内容，需要变更为新规格计算。

## FullScreenLaunchComponent嵌入式运行元服务内容区避让系统安全区行为变更

**变更原因**

通过FullScreenLaunchComponent拉起嵌入式运行元服务时，元服务的windowMode为undefined，元服务的页面内容在任何场景下都不会避让系统安全区，嵌入式运行元服务和跳出式运行元服务页面默认避让行为不一致，需要元服务的开发者针对嵌入式场景主动做避让适配。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

说明：宿主是拉起方，即FullScreenLaunchComponent组件使用方，提供方是被嵌入式运行的元服务。

* 变更前：提供方的windowMode不跟随宿主，默认值为undefined，所有场景下，元服务的页面内容都不会默认避让系统安全区，需要开发者在提供方的代码逻辑中设置主动避让。
* 变更后：提供方的windowMode与宿主保持一致，当宿主的windowMode处于全屏显示时，若提供方未主动设置沉浸式页面布局，提供方页面将默认适配系统安全区域，开发者无需进行手动适配。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

12

**变更的接口/组件**

FullScreenLaunchComponent组件及嵌入式拉起的元服务。

**适配指导**

* 宿主的targetSdkVersion >= 20。

  + 建议宿主应用在6.0及以上版本使用嵌入式运行元服务，5.x版本建议使用跳出式运行元服务，提供方元服务无需在嵌入式场景主动避让适配。
  + 如果宿主应用需要在5.x使用嵌入式运行元服务，需要提供方元服务针对嵌入式场景做适配，需要判断提供方元服务的ohos.extra.atomicservice.param.key.isFollowHostWindowMode，如果ohos.extra.atomicservice.param.key.isFollowHostWindowMode为true，无需主动避让适配；否则需要主动避让适配。
* 宿主的targetSdkVersion < 20。

  + 不建议宿主应用使用嵌入式运行元服务，建议使用跳出式运行元服务。
  + 如果宿主应用需要使用嵌入式运行元服务，提供方元服务需要判断ohos.extra.atomicservice.param.key.isFollowHostWindowMode，若ohos.extra.atomicservice.param.key.isFollowHostWindowMode为true，无需主动避让适配；否则需要主动避让适配。

```
1. export default class AtomicServiceAbility extends EmbeddableUIAbility {
2. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
3. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
4. if (want.parameters) {
5. hilog.info(0x0000, 'testTag', '%{public}s', 'followed host window mode' + want.parameters['ohos.extra.atomicservice.param.key.isFollowHostWindowMode']);
6. }
7. }
8. }
```

## 半模态跟手样式弹窗显示位置避让规则变更

**变更原因**

基础能力增强，半模态跟手样式弹窗支持开发者自定义弹出方向，并根据位置避让流程决定弹窗最终显示位置。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前行为：半模态跟手样式弹窗默认弹出位置为绑定组件底部，会根据剩余空间情况同绑定组件左边和右边作对齐布局，不做任何半模态面板高度的压缩。

变更后行为：开发者可使用bindOptions中的placement（设置弹窗默认弹出位置，默认值Bottom）和 placementOnTarget（所有位置均放不下时，是否允许弹窗覆盖在绑定节点上）两个字段，自定义半模态跟手样式弹窗相关的弹出位置信息。半模态跟手样式弹窗在确保指定位置能容纳弹窗尺寸的前提下，优先依据设定的placement展示弹窗。若不可行，则遵循先垂直翻转，后尝试90°水平旋转的规则调整显示位置，以预设方向为下方为例，调整顺序依次为：下、上、右、左。如果设置的对齐方式导致组件布局超出窗口范围，将根据该对齐方式在水平或垂直方向上进行位移，直至组件完全显示在窗口内。如果在四个方向上均无法容纳跟手样式弹窗，处理方式遵循开发者设置的placementOnTarget属性。若属性值为True，将依据设定的placement，向其镜像方向平移，直至弹窗能够完全显示，且允许覆盖在绑定的弹出节点上；若属性值为false，则在四个方向中，选择能够完全展示弹窗宽度且剩余高度最大的方向，通过调整半模态高度以适应当前方向，确保弹窗能够放下，同时保持预设placement对应的对齐方式不变。

| 变更前 | 变更后placementOnTarget为true | 变更后placementOnTarget为false |
| --- | --- | --- |
|  |  |  |

**起始API Level**

11

**变更的接口/组件**

bindSheet

SheetType.POPUP

**适配指导**

默认行为变更，开发者无需适配，需注意若api16前实现的效果为底部左对齐或者底部右对齐，可以通过设置placement值为BottomLeft或BottomRight来实现对应显示效果。
