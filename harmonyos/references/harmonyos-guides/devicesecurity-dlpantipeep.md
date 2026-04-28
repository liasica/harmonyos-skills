---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-dlpantipeep
title: 防窥保护
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 防窥保护
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d733f0080b90b774c971766ebb98ed437c4236075744046af2244809aa66d74b
---

## 场景介绍

支持应用根据屏幕窥视状态保护机主隐私，如拉起系统级蒙层遮盖窗口，非机主状态下不进行个性化推荐，隐藏浏览记录、支付记录、收藏记录等敏感信息。其中系统使用智能判断将长期通过人脸解锁手机的人作为防窥保护的机主。若防窥保护开关未打开，可以拉起设置弹窗或提醒用户进入设置页开启。

## 开发前置条件

* 需要在设备开启人脸识别。
* 在设备上选择“设置 > 隐私与安全 > 防窥保护”，开启防窥保护开关。通过人脸验证后，打开需要加入保护的应用开关。

## 约束与限制

满足以下所有条件：

1. 本特性需要设备上存在防窥保护选项。开发者可通过在设备上选择“设置 > 隐私与安全 > 防窥保护”查看防窥保护选项。
2. HarmonyOS系统：HarmonyOS 6.0.0 Beta1及以上。
3. DevEco Studio版本：DevEco Studio 6.0.0 Beta1及以上。
4. HarmonyOS SDK版本: HarmonyOS 6.0.0 Beta1 SDK及以上。
5. 防窥保护功能使用智能判断，通过传感器判断您周边环境给您风险提醒。判断因素包括人脸距离设备是否在一定的范围内、人脸是否有遮挡、周围环境是否有充足的光线。当距离较近或较远、人脸被遮挡、周围环境较暗时，可能会引起识别误差，从而导致系统未提醒或者误提醒。如果您认为智能判断可能有误，您可以尝试调整位置和光线，重新使用人脸解锁手机等操作，并再次使用该功能帮助您防窥。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/T36oHTiDTpy0BAMM2gbmdQ/zh-cn_image_0000002583438449.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234301Z&HW-CC-Expire=86400&HW-CC-Sign=AD317E4A1168605708B2A87044E088E883E653B35C2105F738B38F7FC67F5C1A)

**流程说明：**

1. 用户在“设置 > 隐私与安全 > 防窥保护”中开启当前应用的功能开关，或应用提供设置入口，用户点击后通过调用requestAntiPeepOptions(context: Context)接口拉起设置弹窗进行设置。
2. 调用isDlpAntiPeepSwitchOn()接口查询当前应用开关的状态。
3. 调用on()接口注册防窥保护通知：3.1 机主自身注视屏幕时反馈非窥视状态；3.2 机主与非机主同时注视屏幕时反馈被窥视状态。3.3 没有机主使用手机或机主分享场景，返回非窥视状态。
4. 手动调用getDlpAntiPeepInfo()接口返回当前应用的窥视状态。
5. 调用setAntiPeepMaskLayer(windowId: number)接口，拉起系统级蒙层。
6. 调用passDlpAntiPeepInfo()接口修改窥视状态，直到手机锁屏或应用退出前一直会返回非窥视状态。
7. 调用off()接口解除注册防窥保护通知。

## 接口说明

以下是获取防窥状态信息相关接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-dlpantipeep-api.md)。

| 接口名 | 描述 |
| --- | --- |
| isDlpAntiPeepSwitchOn(): Promise<boolean> | 检查是否打开防窥保护。 |
| on(type: 'dlpAntiPeep', callback: Callback<DlpAntiPeepStatus>): void | 订阅防窥保护状态通知。 |
| off(type: 'dlpAntiPeep', callback?: Callback<DlpAntiPeepStatus>): void | 解除订阅防窥保护状态通知。 |
| getDlpAntiPeepInfo(): DlpAntiPeepStatus | 获取当前应用的窥视状态。 |
| passDlpAntiPeepInfo(): void | 直到手机锁屏或应用退出前一直会返回非窥视状态。 |
| setAntiPeepMaskLayer(windowId: number): Promise<void> | 拉起系统级窗口蒙层遮盖。 |
| requestAntiPeepOptions(context: Context): Promise<AntiPeepOptionsResult> | 拉起设置弹框请求用户打开防窥保护开关。 |
| publishAntiPeepInformation(): Promise<void> | 发布防窥保护提示信息。 |

## 开发步骤

说明

* 在开发准备过程中，需要申请权限：ohos.permission.DLP\_GET\_HIDE\_STATUS；用于获取当前应用使用过程中被非机主本人窥视屏幕相关状态信息。
* 面向合作企业开放，仅在允许名单内的固定应用可申请该权限，申请方式请参考：[申请使用受限权限](declare-permissions-in-acl.md)
* 开发者需向用户说明数据使用的目的、方式和范围。

1. 导入防窥保护模块及相关公共模块。

   ```
   1. import { dlpAntiPeep } from '@kit.DeviceSecurityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { common } from '@kit.AbilityKit';
   ```
2. 调用检查接口确认当前应用是否开启防窥保护，开启防窥保护时调用防窥保护订阅接口获取窥视状态信息。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State message: string = 'DlpAntiPeep';
   5. private hasShownMask: boolean = false;

   7. // 防窥状态变化回调
   8. private onStatusChange = async (status: dlpAntiPeep.DlpAntiPeepStatus): Promise<void> => {
   9. if (status === dlpAntiPeep.DlpAntiPeepStatus.PASS) { // 表示当前状态为无人窥视
   10. console.info('DlpAntiPeepStatus is PASS.');
   11. } else if (status === dlpAntiPeep.DlpAntiPeepStatus.HIDE) { // 表示有人在窥屏，应用可以进行隐私保护操作。
   12. console.info('DlpAntiPeepStatus is HIDE.');
   13. if (!this.hasShownMask) {
   14. await this.setMaskLayer(); // 拉起系统蒙层
   15. }
   16. }
   17. }

   19. // 检查防窥保护开关并订阅通知
   20. async aboutToAppear() {
   21. try {
   22. const isOpen = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
   23. if (isOpen) {
   24. dlpAntiPeep.on('dlpAntiPeep', this.onStatusChange);
   25. } else {
   26. // 开关未开启，引导用户设置
   27. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   28. const result = await dlpAntiPeep.requestAntiPeepOptions(context);
   29. if (result === dlpAntiPeep.AntiPeepOptionsResult.SUCCESS ||
   30. result === dlpAntiPeep.AntiPeepOptionsResult.ALREADY_ON) { // 表示防窥保护开关开启成功或已开启
   31. dlpAntiPeep.on('dlpAntiPeep', this.onStatusChange);
   32. }
   33. }
   34. } catch (error) {
   35. console.error(`Failed to init DlpAntiPeep. Code: ${error.code}, message: ${error.message}`);
   36. }
   37. }

   39. // 取消订阅防窥保护通知
   40. aboutToDisappear() {
   41. try {
   42. dlpAntiPeep.off('dlpAntiPeep', this.onStatusChange);
   43. } catch (error) {
   44. console.error(`Failed to off DlpAntiPeep. Code: ${error.code}, message: ${error.message}`);
   45. }
   46. }

   48. onPageShow() {
   49. console.info('Page shown, reset mask flag');
   50. this.hasShownMask = false;
   51. }

   53. // 拉起系统蒙层
   54. private async setMaskLayer(): Promise<void> {
   55. try {
   56. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   57. const windowClass = await window.getLastWindow(context);
   58. const windowId = windowClass.getWindowProperties().id;
   59. await dlpAntiPeep.setAntiPeepMaskLayer(windowId);
   60. this.hasShownMask = true; // 避免窥视状态时频繁拉起蒙层
   61. } catch (error) {
   62. console.error(`Failed to set AntiPeep MaskLayer. Code: ${error.code}, message: ${error.message}`);
   63. }
   64. }

   66. build() {
   67. Column() {
   68. Text(this.message)
   69. .fontSize(20)
   70. .margin(20)
   71. }
   72. .width('100%')
   73. .height('100%')
   74. .justifyContent(FlexAlign.Center)
   75. }
   76. }
   ```
