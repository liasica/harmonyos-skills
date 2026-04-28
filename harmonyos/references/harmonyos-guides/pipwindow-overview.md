---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-overview
title: 画中画开发概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 在应用程序中使用画中画功能 > 画中画开发概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b507ae602302fa100612bfc4ff64c81688ae52bf77dd46b9dcb12d725d8ac0e
---

## 场景介绍

应用在视频播放、视频会议、视频通话等场景下，可以使用画中画能力将视频内容以小窗（画中画）模式呈现。切换为小窗（画中画）模式后，用户可以进行其他界面操作，提升使用体验。

画中画的常见使用场景有以下几种：

* 视频播放。
* 视频通话。
* 视频会议。
* 直播。

系统提供以下三种画中画功能的开发方式：

* [使用XComponent实现画中画功能开发](pipwindow-xcomponent.md)：适用于应用通过[Navigation](../harmonyos-references/ts-basic-components-navigation.md)管理页面或Ability单页面情况下使用画中画的场景，这种实现方式无需应用管理页面。
* [使用typeNode实现画中画功能开发](pipwindow-typenode.md)：适用于所有场景，这种实现方式灵活性高，需要应用自行管理页面，推荐通过该方式使用画中画功能。
* [使用NDK接口实现画中画功能开发](pipwindow-native.md)：适用于依赖NDK接口开发的应用，需要应用自行管理页面。

## 约束与限制

* 基于安全考虑，应用处于后台时不允许通过startPiP启动画中画。针对应用返回后台时需要启动画中画的场景，建议使用setAutoStartEnabled(true)实现自动启动。

## 接口说明

以下是画中画功能的常用ArkTS接口，更多接口及使用参考[@ohos.PiPWindow (画中画窗口)](../harmonyos-references/js-apis-pipwindow.md)。

| 接口名 | 描述 |
| --- | --- |
| isPiPEnabled(): boolean | 判断当前系统是否开启画中画功能。 |
| create(config: PiPConfiguration): Promise<PiPController> | 创建画中画控制器。 |
| create(config: PiPConfiguration, contentNode: typeNode.XComponent): Promise<PiPController> | 使用typeNode创建画中画控制器。 |
| startPiP(): Promise<void> | 启动画中画。 |
| stopPiP(): Promise<void> | 停止画中画。 |
| setAutoStartEnabled(enable: boolean): void | 设置是否需要在应用退后台时自动启动画中画，true表示需要自动启动，false表示不需要自动启动。 |
| updateContentSize(width: number, height: number): void | 当媒体源切换时，向画中画控制器更新媒体源尺寸信息。 |
| on(type: 'stateChange', callback: (state: PiPState, reason: string) => void): void | 开启画中画生命周期状态的监听。 |
| off(type: 'stateChange'): void | 关闭画中画生命周期状态的监听。 |
| on(type: 'controlPanelActionEvent', callback: ControlPanelActionEventCallback): void | 开启画中画控制面板控件动作事件的监听。推荐使用on('controlEvent')来开启画中画控制面板控件动作事件的监听。 |
| off(type: 'controlPanelActionEvent'): void | 关闭画中画控制面板控件动作事件的监听。推荐使用off('controlEvent')来关闭画中画控制面板控件动作事件的监听。 |
| updatePiPControlStatus(controlType: PiPControlType, status: PiPControlStatus): void | 更新画中画控制面板控件状态。 |
| setPiPControlEnabled(controlType: PiPControlType, enabled: boolean): void | 设置控制面板控件使能状态。 |
| on(type: 'controlEvent', callback: CallBack<ControlEventParam>): void | 开启画中画控制面板控件动作事件的监听。 |
| off(type: 'controlEvent', callback?: CallBack<ControlEventParam>): void | 关闭画中画控制面板控件动作事件的监听。 |

以下是画中画功能的常用NDK接口，更多接口及使用参考[oh\_window\_pip.h](../harmonyos-references/capi-oh-window-pip-h.md)。

| 接口名 | 描述 |
| --- | --- |
| int32\_t OH\_PictureInPicture\_CreatePipConfig(PictureInPicture\_PipConfig\* pipConfig) | 创建画中画参数配置器。 |
| int32\_t OH\_PictureInPicture\_DestroyPipConfig(PictureInPicture\_PipConfig\* pipConfig) | 销毁画中画参数配置器。 |
| int32\_t OH\_PictureInPicture\_CreatePip(PictureInPicture\_PipConfig pipConfig, uint32\_t\* controllerId) | 创建画中画控制器。 |
| int32\_t OH\_PictureInPicture\_DeletePip(uint32\_t controllerId) | 删除画中画控制器。 |
| int32\_t OH\_PictureInPicture\_StartPip(uint32\_t controllerId) | 启动画中画。 |
| int32\_t OH\_PictureInPicture\_StopPip(uint32\_t controllerId) | 停止画中画。 |
| int32\_t OH\_PictureInPicture\_UpdatePipContentSize(uint32\_t controllerId, uint32\_t width, uint32\_t height) | 当媒体源切换时，向画中画控制器更新媒体源尺寸信息。 |
| int32\_t OH\_PictureInPicture\_UpdatePipControlStatus(uint32\_t controllerId, PictureInPicture\_PipControlType controlType, PictureInPicture\_PipControlStatus status) | 更新画中画控制面板控件状态。 |
| int32\_t OH\_PictureInPicture\_SetPipControlEnabled(uint32\_t controllerId, PictureInPicture\_PipControlType controlType, bool enabled) | 设置画中画控制面板控件使能状态。 |
| int32\_t OH\_PictureInPicture\_RegisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback) | 开启画中画surface创建完成的监听。 |
| int32\_t OH\_PictureInPicture\_UnregisterStartPipCallback(uint32\_t controllerId, WebPipStartPipCallback callback) | 关闭画中画surface创建完成的监听。 |
| int32\_t OH\_PictureInPicture\_RegisterLifecycleListener(uint32\_t controllerId, WebPipLifeCycleCallback callback) | 开启画中画生命周期状态的监听。 |
| int32\_t OH\_PictureInPicture\_UnregisterLifecycleListener(uint32\_t controllerId, WebPipLifeCycleCallback callback) | 关闭画中画生命周期状态的监听。 |
| int32\_t OH\_PictureInPicture\_RegisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback) | 开启画中画控制面板控件动作事件的监听。 |
| int32\_t OH\_PictureInPicture\_UnregisterControlEventListener(uint32\_t controllerId, WebPipControlEventCallback callback) | 关闭画中画控制面板控件动作事件的监听。 |
| int32\_t OH\_PictureInPicture\_RegisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback) | 开启画中画窗口尺寸变化事件的监听。 |
| int32\_t OH\_PictureInPicture\_UnregisterResizeListener(uint32\_t controllerId, WebPipResizeCallback callback) | 关闭画中画窗口尺寸变化事件的监听。 |

## 交互方式

画中画窗口提供以下交互方式：

* 单击画中画窗口：如果画中画控制层未显示，则显示画中画控制层，3秒后自动隐藏控制层；如果当前控制层已显示，则隐藏画中画控制层。
* 双击画中画窗口：放大或缩小画中画窗口。
* 拖动画中画窗口：可以将画中画窗口拖动到屏幕任意位置。如果将画中画窗口拖动到屏幕左右边缘，画中画窗口会自动隐藏；隐藏后在屏幕边缘显示画中画隐藏图标，点击该图标后画中画窗口恢复显示。
* 拖拽缩放画中画窗口：可以拖拽画中画窗口四边以及四个对角缩放画中画窗口大小，窗口尺寸不能超过默认最大档与最小档，当拖拽过程中画中画窗口超过窗口尺寸限制以及超出屏幕尺寸，会触发回弹效果。
* 拖动删除画中画窗口：可以将画中画窗口拖动到底部垃圾桶热区，删除画中画窗口。对于申请长时任务的应用，需要主动监听画中画生命周期STOPPED事件，关闭任务或进程。

画中画控制层提供以下功能：

* 窗口控制：包括“关闭”和“恢复全屏窗口”功能。点按“关闭”按钮后，画中画窗口关闭；点按“恢复全屏窗口”按钮后，将从画中画窗口恢复到应用原始界面。
* 内容控制：内容控制区根据不同场景呈现不同，应用可根据实际场景需要进行设置，各场景控制层示意图如下所示。

**图1** 不同场景下画中画控制层的不同呈现

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/SrEfEwCGSgO19C-u2m4lqQ/zh-cn_image_0000002552798526.png?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=9A345F42189A62F6CE6C24357DE18F75E4D5088A53DCBFA41C6A5B51D19C3BAC)

## 配置画中画控制层可选控件

在使用[create](../harmonyos-references/js-apis-pipwindow.md#pipwindowcreate)接口创建画中画时，可通过在[PiPConfiguration](../harmonyos-references/js-apis-pipwindow.md#pipconfiguration)中新增[PiPControlGroup](../harmonyos-references/js-apis-pipwindow.md#pipcontrolgroup12)类型的数组配置当前画中画控制层控件。

* 视频播放场景可通过配置[VideoPlayControlGroup](../harmonyos-references/js-apis-pipwindow.md#videoplaycontrolgroup12)来显示可选的控制层控件。

  **图2** 视频播放场景配置控制层可选控件

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/3WAVBWIPQ_O8VbeEAr92kg/zh-cn_image_0000002583438221.png?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=0BFF8075738EF5FE4646901DA5A1F5718D4E368957FBB515D11DBB2F2C34CFB9)
* 视频通话场景可通过配置[VideoCallControlGroup](../harmonyos-references/js-apis-pipwindow.md#videocallcontrolgroup12)来显示可选的控制层控件。示意图如下所示。

  **图3** 视频通话场景配置控制层可选控件

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/o-PZzqOMTUS7XTU3Go_LQQ/zh-cn_image_0000002552958176.png?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=4A8335F6411A723B594825C33B53D2EA863A7F286B3D613D180FC02BE3397154)

  若不配置，视频通话模版默认不存在任何按钮，点击画中画窗口即可启动还原（见下图左，未配置任何控件的操作示意图）。下图右为配置控件的操作示意图。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/6_ontSA-Q8S0F7ddaGtwBQ/zh-cn_image_0000002583478177.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=BAF5816408B7A51556CE607F5BE731630CBCF60A01A2D5E8322D2681F7635172) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/E5TdZJSRSce-0W11LZwqzA/zh-cn_image_0000002552798528.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=A214D3094402C3F9F799BDD1F3401548C6E1D0B00A578B4628F448166FDD4A85)
* 视频会议场景可通过配置[VideoMeetingControlGroup](../harmonyos-references/js-apis-pipwindow.md#videomeetingcontrolgroup12)来显示可选的控制层控件。示意图如下所示。若不配置，视频会议模版默认不存在任何按钮，点击画中画窗口即可启动还原（与视频通话模版操作示意图一致）。

  **图4** 视频会议场景配置控制层可选控件

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/bYnG7MDvSfGy_kjCY_mM5g/zh-cn_image_0000002583438223.png?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=1B4755C35C70F641EBBC2D7117B8C044206306DEBCE2DBE867BB60A7657213AC)
* 直播场景可通过配置[VideoLiveControlGroup](../harmonyos-references/js-apis-pipwindow.md#videolivecontrolgroup12)来显示可选的控制层控件。示意图如下所示。

  **图5** 直播场景配置控制层可选控件

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/1jWilYutRyGQKvDdlqH3TA/zh-cn_image_0000002552958178.png?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=CC316CBCD83591C9A9C9EA6ABB3FBD166B22F8F3EBC5A78652FD7423F8F07373)

## 在画中画内容上方展示自定义UI

在使用[create](../harmonyos-references/js-apis-pipwindow.md#pipwindowcreate)接口创建画中画时，可通过在[PiPConfiguration](../harmonyos-references/js-apis-pipwindow.md#pipconfiguration)中传入customUIController来显示自定义UI。

说明

自定义显示的UI无法响应交互事件。

**图6** 在画中画内容上方显示自定义UI

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Nl9OFef-R7GIyw_tNXbk8w/zh-cn_image_0000002583478179.png?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=0B156C88759644B4864FD084E7F36774D0903753B3B39BBA7E0BF061CB08BDA6)

## 更新画中画控制面板控件状态

应用可以使用updatePiPControlStatus接口更新控制面板控件的功能状态，如将视频播放模板下VIDEO\_PLAY\_PAUSE控件的播放状态更改为暂停状态，见下图。

应用也可以使用setPiPControlEnabled接口设置控制面板控件的使能状态，如将视频播放模板下VIDEO\_PREVIOUS控件从可点击状态变为不可点击状态，见下图。

**图7** 更新控件功能状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/iCLMNIydSSyWCmzyTWUvgg/zh-cn_image_0000002552798530.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=C671DBBFD86E9C75F45CEA4DB37EA1B1517C0240909731B30A05E6F09385A2A2)

**图8** 设置控件使能状态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/T19v603dT_WTXsfdiGrT8Q/zh-cn_image_0000002583438225.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=D572F9564DE0A6854390A00DB4F2299DF8AA54312239C2BDFB7035452D5BD2D5)
