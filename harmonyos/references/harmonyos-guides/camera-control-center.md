---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-control-center
title: 相机控制器(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 相机控制器(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2c06df1e01750d49237e284577f8522e6667918f1d25f6f09b25bb8464cd9cc9
---

从API version 20开始，相机框架通过相机控制器，为应用在直播场景提供美颜、虚化等能力。

相机控制器为直播和视频通话场景设计，目前仅支持在前置镜头的录像模式下使用，最高可支持1080P分辨率和30fps帧率。

## 开发步骤

详细的API说明请参考[Camera](../harmonyos-references/arkts-apis-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过[isControlCenterSupported](../harmonyos-references/arkts-apis-camera-controlcenterquery.md#iscontrolcentersupported20)接口，查询当前设备及当前场景是否支持相机控制器。

   ```
   1. function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
   2. let isSupported: boolean = videoSession.isControlCenterSupported();
   3. return isSupported;
   4. }
   ```
3. 通过[getSupportedEffectTypes](../harmonyos-references/arkts-apis-camera-controlcenterquery.md#getsupportedeffecttypes20)接口，查询当前设备及当前场景下，相机控制器支持的效果类型。

   ```
   1. function getSupportedEffectTypes(videoSession: camera.VideoSession): Array<camera.ControlCenterEffectType> {
   2. let effectTypes: Array<camera.ControlCenterEffectType> = [];
   3. effectTypes = videoSession.getSupportedEffectTypes();
   4. return effectTypes;
   5. }
   ```
4. 若设备及场景支持相机控制器，使用[enableControlCenter](../harmonyos-references/arkts-apis-camera-controlcenter.md#enablecontrolcenter20)接口可启用或关闭控制器。

   ```
   1. function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
   2. let isSupported: boolean = videoSession.isControlCenterSupported();
   3. if (isSupported) {
   4. videoSession.enableControlCenter(enable);
   5. }
   6. }
   ```
5. 使能相机控制器后，可以在状态栏看到新增的视频效果图标。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Lqz73YzqQhCklLMrL7Jo3g/zh-cn_image_0000002583478571.png?HW-CC-KV=V1&HW-CC-Date=20260427T234559Z&HW-CC-Expire=86400&HW-CC-Sign=DC0D25673E0FE8DD759DD27E74B90461683A0A98315193CAF5071299846BC2C5)
6. 点击视频效果图标，在弹出的二级页面中，用户可调节控制器支持的效果，如图所示为美颜和背景虚化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/DXzHB_kkTG-maiqg-9oLpg/zh-cn_image_0000002552798922.png?HW-CC-KV=V1&HW-CC-Date=20260427T234559Z&HW-CC-Expire=86400&HW-CC-Sign=F1C5D2E86110119C63740584CEEAE787C74A7D95BE25EB28E0B14F74350E5EB2)

## 状态监听

使用相机控制器的过程中，应用可以监听控制器效果的使能状态。

通过注册[controlCenterEffectStatusChange](../harmonyos-references/arkts-apis-camera-videosession.md#oncontrolcentereffectstatuschange20)的回调函数获取控制器中各效果的使能状态。

当控制器中某效果使能状态发生变化时，callback返回[ControlCenterStatusInfo](../harmonyos-references/arkts-apis-camera-i.md#controlcenterstatusinfo20)参数。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function callback(err: BusinessError, status: camera.ControlCenterStatusInfo): void {
5. if (err !== undefined && err.code !== 0) {
6. console.error(`Callback Error, errorCode: ${err.code}`);
7. return;
8. }
9. console.info(`controlCenterEffectStatusChange: ${status}`);
10. }

12. function registerControlCenterEffectStatusChangeCallback(videoSession: camera.VideoSession): void {
13. videoSession.on('controlCenterEffectStatusChange', callback);
14. }
```
