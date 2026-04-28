---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/motion-guidelines
title: 获取用户动作开发指导
breadcrumb: 指南 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > 获取用户动作开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c64999675c5da42a933e95ef5dce74e7ecc29e204731ca74440ada48de3e8d96
---

## 场景介绍

当应用需要获取用户动作时，可以调用motion模块，例如判断用户当前是用左手还是右手操作设备屏幕。

详细的接口介绍请参考[@ohos.multimodalAwareness.motion (动作感知能力)](../harmonyos-references/js-apis-awareness-motion.md)。

从API version 15开始，支持获取操作手状态。从API version 20开始，支持获取握持手状态。

## 获取操作手状态开发指导

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| on(type:'operatingHandChanged',callback:Callback<OperatingHandStatus>):void; | 订阅操作手感知，操作手结果通过callback返回。 |
| off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void; | 取消订阅操作手感知。 |
| getRecentOperatingHandStatus(): OperatingHandStatus; | 获取最新的操作手状态。 |

### 需要权限

使用motion模块获取用户操作手时，需要权限：ohos.permission.ACTIVITY\_MOTION 或 ohos.permission.DETECT\_GESTURE，具体申请方式请参考[声明权限](declare-permissions.md)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.ACTIVITY_MOTION"
4. },
5. {
6. "name" : "ohos.permission.DETECT_GESTURE"
7. }
8. ]
```

### 约束与限制

* 此功能如果设备不支持，将返回801错误码。
* 指关节操作不属于使用手操作场景。
* 窗口旋转场景，多指同时操作场景不支持。
* 能力有效范围：不包含距离屏幕边缘8mm内区域。
* 结果上报条件：首次订阅或切换操作手后，连续点数次触发。
* 触控响应说明：屏幕四周边缘8mm范围内不支持触控响应。

### 开发步骤

1. 导入模块。

   ```
   1. import { motion } from '@kit.MultimodalAwarenessKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义回调函数接收操作手结果

   ```
   1. let callback:Callback<motion.OperatingHandStatus> = (data:motion.OperatingHandStatus) => {
   2. console.info('callback succeeded' + data);
   3. };
   ```
3. 订阅操作手感知

   ```
   1. try {
   2. motion.on('operatingHandChanged', callback);
   3. console.info("on succeeded");
   4. } catch (err) {
   5. let error = err as BusinessError;
   6. console.error("Failed on and err code is " + error.code);
   7. }
   ```
4. 取消订阅操作手感知

   ```
   1. try {
   2. motion.off('operatingHandChanged');
   3. console.info("off succeeded");
   4. } catch (err) {
   5. let error = err as BusinessError;
   6. console.error("Failed off and err code is " + error.code);
   7. }
   ```
5. 获取最新操作手状态

   ```
   1. try {
   2. let data:motion.OperatingHandStatus = motion.getRecentOperatingHandStatus();
   3. console.info('get succeeded' + data);
   4. } catch (err) {
   5. let error = err as BusinessError;
   6. console.error("Failed get and err code is " + error.code);
   7. }
   ```

## 获取握持手状态开发指导

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| on(type:'holdingHandChanged',callback:Callback<HoldingHandStatus>): void; | 订阅握持手感知，感知结果通过callback返回。 |
| off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void; | 取消订阅握持手感知。 |

### 需要权限

使用motion模块获取用户握持手时，需要权限： ohos.permission.DETECT\_GESTURE，具体申请方式请参考[声明权限](declare-permissions.md)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.DETECT_GESTURE"
4. }
5. ]
```

### 约束与限制

* 此功能当前支持部分机型，若设置菜单中存在“智感握姿”开关（可在“设置-系统”中查看），则表明该设备支持此功能，若无此开关，将返回801错误码。
* 设备屏幕需处于亮屏且解锁状态。
* 设备保护壳（若有）厚度不得超过3毫米。
* 需以五指自然握持设备，同时掌心区域接触设备（或拇指外的四指及掌心区域接触）。
* 握持时确保每根接触手指的接触面积尽可能大（理想情况下不低于30mm²）。
* 佩戴手套会显著降低识别准确率。
* 竖屏握持时，摄像头需朝上。
* 支持横屏握持，但需要注意：应用横屏时竖屏握持即握持设备长边，应用竖屏时横屏握持即握持设备短边，均属异常姿态，无法保证识别成功。
* 握持时屏幕需朝向握持人。
* 握持时不得同时接触其他物体（如桌面、其他身体部位等）。
* 未握持的识别依赖设备状态，设备非静止时无法保证识别成功。

### 开发步骤

1. 导入模块。

   ```
   1. import { motion } from '@kit.MultimodalAwarenessKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义回调函数接收握持手结果

   ```
   1. let callback:Callback<motion.HoldingHandStatus> = (data:motion.HoldingHandStatus) => {
   2. console.info('callback succeeded' + data);
   3. };
   ```
3. 订阅握持手感知

   ```
   1. try {
   2. motion.on('holdingHandChanged', callback);
   3. console.info("on succeeded");
   4. } catch (err) {
   5. let error = err as BusinessError;
   6. console.error("Failed on and err code is " + error.code);
   7. }
   ```
4. 取消订阅握持手感知

   ```
   1. try {
   2. motion.off('holdingHandChanged');
   3. console.info("off succeeded");
   4. } catch (err) {
   5. let error = err as BusinessError;
   6. console.error("Failed off and err code is " + error.code);
   7. }
   ```
