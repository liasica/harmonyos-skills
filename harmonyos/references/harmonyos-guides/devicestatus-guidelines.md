---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicestatus-guidelines
title: 设备状态感知开发指导
breadcrumb: 指南 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > 设备状态感知开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ba75840cdf9b766eec4049509b2f512497d3544fdb4df8322fab639cc8f1d115
---

DeviceStatus（设备状态感知）模块提供设备状态感知能力，可以获取到设备的信息，例如：获取设备静止姿态感知状态（支架态）。

详细的接口介绍请参考[@ohos.multimodalAwareness.deviceStatus (设备状态感知)](../harmonyos-references/js-apis-awareness-devicestatus.md)。

## 基本概念

在进行设备状态感知模块的使用前，开发者应了解以下基本概念：

* 支架态

  设备进入支架态指设备静止，且屏幕与水平面角度处于45度-135度。折叠屏手机需处于折叠状态或者完全展开状态。

## 获取设备静止姿态感知状态（支架态）开发指导

### 场景介绍

开发过程中，需要订阅设备静止姿态（支架态）感知，并且通过订阅时传入的回调函数来获取到当前的状态值。

从API version 18开始，支持获取设备静止姿态（支架态）。

### 约束与限制

设备需要支持加速度计。

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void; | 订阅设备静止姿态（支架态）感知，结果通过callback返回。 |
| off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void; | 取消订阅设备静止姿态（支架态）感知。 |

### 开发步骤

1. 导入模块。

   ```
   1. import { deviceStatus } from '@kit.MultimodalAwarenessKit';
   ```
2. 订阅设备静止姿态（支架态）感知事件。

   ```
   1. try {
   2. deviceStatus.on('steadyStandingDetect', (data:deviceStatus.SteadyStandingStatus) => {
   3. console.info('succeed to get status, now status = ' + data);
   4. });
   5. } catch (err) {
   6. console.error('on failed, err = ' + err);
   7. }
   ```
3. 取消本客户端订阅的所有设备静止姿态（支架态）感知事件。

   ```
   1. try {
   2. deviceStatus.off('steadyStandingDetect');
   3. } catch (err) {
   4. console.error('off failed, err = ' + err);
   5. }
   ```
4. 取消订阅设备静止姿态（支架态）感知事件的特定回调。

   ```
   1. // 定义callback变量
   2. let callback : Callback<deviceStatus.SteadyStandingStatus> = (data : deviceStatus.SteadyStandingStatus) => {
   3. console.info('succeed to get status, now status = ' + data);
   4. };
   5. // 以callback为回调函数，订阅设备静止姿态感知（支架态）事件
   6. try {
   7. deviceStatus.on('steadyStandingDetect', callback);
   8. } catch (err) {
   9. console.error('on failed, err = ' + err);
   10. }
   11. // 取消该客户端订阅设备静止姿态感知（支架态）事件的特定回调函数
   12. try {
   13. deviceStatus.off('steadyStandingDetect', callback);
   14. } catch (err) {
   15. console.error('off failed, err = ' + err);
   16. }
   ```
