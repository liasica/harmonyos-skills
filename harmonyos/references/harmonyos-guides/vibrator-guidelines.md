---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vibrator-guidelines
title: 振动开发指导(ArkTS)
breadcrumb: 指南 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > 振动 > 振动开发指导(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:33:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:435992a119422f32fea02993a5d61c887c7d2924c98ed1fae3f9d09478bc6734
---

## 场景介绍

当设备需要设置不同的振动效果时，可以调用Vibrator模块，例如：设备的按键可以设置不同强度和不同时长的振动，闹钟和来电可以设置不同强度和时长的单次或周期振动。

详细的接口介绍请参考[@ohos.vibrator (振动)](../harmonyos-references/js-apis-vibrator.md)。

## 接口说明

| 名称 | 描述 |
| --- | --- |
| startVibration(effect: VibrateEffect, attribute: VibrateAttribute): Promise<void> | 根据指定振动效果和振动属性触发马达振动，使用Promise异步回调。 |
| startVibration(effect: VibrateEffect, attribute: VibrateAttribute, callback: AsyncCallback<void>): void | 根据指定振动效果和振动属性触发马达振动，使用Callback异步回调。 |
| stopVibration(stopMode: VibratorStopMode): Promise<void> | 按照指定模式停止马达的振动，使用Promise异步回调。 |
| stopVibration(stopMode: VibratorStopMode, callback: AsyncCallback<void>): void | 按照指定模式停止马达的振动，使用Callback异步回调。 |
| stopVibration(): Promise<void> | 停止所有模式的马达振动，使用Promise异步回调。 |
| stopVibration(param?: VibratorInfoParam): Promise<void> | 不传参则停止本地设备所有马达的振动，也可传参停止指定马达振动，使用Promise异步回调。 |
| stopVibration(callback: AsyncCallback<void>): void | 停止所有模式的马达振动，使用Callback异步回调。 |
| isSupportEffect(effectId: string): Promise<boolean> | 查询是否支持传入的参数effectId。返回true则表示支持，否则不支持，使用Promise异步回调。 |
| isSupportEffect(effectId: string, callback: AsyncCallback<boolean>): void | 查询是否支持传入的参数effectId。返回true则表示支持，否则不支持，使用Callback异步回调。 |
| getEffectInfoSync(effectId: string, param?: VibratorInfoParam): EffectInfo | 同步查询是否支持传入的参数effectId，param可指定具体马达。返回EffectInfo中isEffectSupported字段可判断是否支持。 |
| getVibratorInfoSync(param?: VibratorInfoParam): Array<VibratorInfo> | 同步查询一个或所有设备的马达信息列表。返回VibratorInfo包含设备ID、马达ID、设备名称、是否支持高清振动、是否本地设备等信息。 |
| on(type: 'vibratorStateChange', callback: Callback<VibratorStatusEvent>): void | 注册马达设备上线下状态变化的监听。callback参数VibratorStatusEvent可返回事件时间戳、设备ID、马达数量、上线或下线等信息。 |
| off(type: 'vibratorStateChange', callback?: Callback<VibratorStatusEvent>): void | 注销马达设备上线下状态变化的监听。 |
| isHdHapticSupported(): boolean | 查询是否支持高清振动。 |

## 振动效果说明

目前支持三类振动效果，如下所示：

| 名称 | 说明 |
| --- | --- |
| 固定时长振动 | 传入一个固定时长，马达按照默认强度和频率触发振动，振动效果描述请参考[VibrateTime](../harmonyos-references/js-apis-vibrator.md#vibratetime9)。 |
| 预置振动 | 系统中的[EffectId](../harmonyos-references/js-apis-vibrator.md#effectid)，这些效果适用于某些固定场景，比如效果"haptic.clock.timer"通常用于用户调整计时器时的振感反馈，振动效果描述请参考[VibratePreset](../harmonyos-references/js-apis-vibrator.md#vibratepreset9)。 |
| 自定义振动 | 自定义振动提供给用户设计自己所需振动效果的能力，用户可通过自定义振动配置文件，并遵循相应规则编排所需振动形式，使能更加开放的振感交互体验，效果描述请参考[VibrateFromFile](../harmonyos-references/js-apis-vibrator.md#vibratefromfile10)。 |

自定义振动配置文件为Json格式，在形式上如下所示：

```
1. {
2. "MetaData": {
3. "Create": "2023-01-09",
4. "Description": "a haptic case",
5. "Version": 1.0,
6. "ChannelNumber": 1
7. },
8. "Channels": [
9. {
10. "Parameters": {
11. "Index": 0
12. },
13. "Pattern": [
14. {
15. "Event": {
16. "Type": "transient",
17. "StartTime": 0,
18. "Parameters": {
19. "Frequency": 31,
20. "Intensity": 100
21. }
22. }
23. },
24. {
25. "Event": {
26. "Type": "continuous",
27. "StartTime": 40,
28. "Duration": 54,
29. "Parameters": {
30. "Frequency": 30,
31. "Intensity": 38,
32. "Curve": [
33. {
34. "Time": 0,
35. "Frequency": 0,
36. "Intensity": 0
37. },
38. {
39. "Time": 1,
40. "Frequency": 15,
41. "Intensity": 0.5
42. },
43. {
44. "Time": 40,
45. "Frequency": -8,
46. "Intensity": 1.0
47. },
48. {
49. "Time": 54,
50. "Frequency": 0,
51. "Intensity": 0
52. }
53. ]
54. }
55. }
56. }
57. ]
58. }
59. ]
60. }
```

JSON文件共包含3个属性。

1. "MetaData"属性中为文件头信息，可在如下属性中添加描述：

   | 名称 | 必填项 | 说明 |
   | --- | --- | --- |
   | Version | 是 | 文件格式的版本号，向前兼容，目前支持版本1.0。 |
   | ChannelNumber | 是 | 表示马达振动的通道数，最大支持双马达通道。 |
   | Create | 否 | 可记录文件创作时间。 |
   | Description | 否 | 可指明振动效果、创建信息等附加说明。 |
2. "Channels"属性中为马达振动通道的相关信息。

   "Channels"是Json数组，表示各个通道的信息，包含2个属性。

   | 名称 | 必填项 | 说明 |
   | --- | --- | --- |
   | Parameters | 是 | 为通道参数。其中"Index"表示通道编号，0表示全通道发送，1、2分别对应左右马达。0不能与其他通道编号同时作为配置参数。 |
   | Pattern | 否 | 马达振动序列。 |

   "Pattern"是Json数组，包含振动事件序列，每个"Event"属性代表1个振动事件，支持添加2种振动类型。

   | 振动类型 | 说明 |
   | --- | --- |
   | transient | 瞬态短振动，干脆有力。 |
   | continuous | 稳态长振动，具备长时间输出强劲有力振动的能力。 |

   "Event"表示一个振动事件，包含如下属性：

   | 名称 | 必填项 | 说明 |
   | --- | --- | --- |
   | Type | 是 | 振动事件类型，为"transient" 或"continuous"。 |
   | StartTime | 是 | 振动的起始时间，单位ms，有效范围为[0, 1800,000]。 |
   | Duration | 是 | 振动持续时间，仅当类型为"continuous"时有效，单位ms，有效范围为[0, 5000]。 |
3. "Parameters"表示振动事件参数设置，必填项，可设置以下属性参数：

   | 名称 | 必填项 | 说明 |
   | --- | --- | --- |
   | Intensity | 是 | 振动事件强度，有效范围为[0, 100]，数字大小代表最大振动量的xx%。 |
   | Frequency | 是 | 振动事件频率，有效范围为[0, 100]，一般支持频率调节的马达设置为55时为器件的谐振频率，此时振动量最大，越靠近谐振频率的振动，同强度设置的振动量越大。 |
   | Curve | 否 | 振动曲线，当振动事件类型为"continuous"时有效，为Json数组，支持设置一组调节点，调节点数量最大支持16个，最小为4个，每个调节点需包含如下属性：  "Time"：相对事件起始时间的偏移，最小为0，最大不能超过事件振动时长；  "Intensity"：相对事件振动强度的增益，范围为[0, 1]，此值乘上振动事件强度为对应时间点调节后的强度；  "Frequency"：相对事件振动频率的变化，范围为[-100, 100]，此值加上振动事件频率为对应时间点调节后的频率。 |

其他要求：

| 参数 | 要求 |
| --- | --- |
| 振动事件(event)的数量 | 不得超过128个。 |
| 振动配置文件长度 | 不得超过64KB。 |

## 开发步骤

1. 新建一个工程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/rvV9tGW8TfyB2nswxiDw9g/zh-cn_image_0000002558764982.png?HW-CC-KV=V1&HW-CC-Date=20260429T053340Z&HW-CC-Expire=86400&HW-CC-Sign=7164C96AE162BF950670F402AEE1FBEF9DDF184E4E10A9F6B68C1DCD9099CB19)
2. 配置权限，具体配置方式请参考[声明权限](declare-permissions.md)。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.VIBRATE"
   4. }
   5. ],
   ```
3. 导入模块。

   ```
   1. import { vibrator } from '@kit.SensorServiceKit';
   2. import { resourceManager } from '@kit.LocalizationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
4. 定义常量。

   ```
   1. const fileName: string = 'vibrator.json';
   2. let TAG = 'vibrator:';
   ```
5. 振动器查询。

   **情形一** 查询所有马达信息：

   ```
   1. try {
   2. const vibratorInfoList: vibrator.VibratorInfo[] = vibrator.getVibratorInfoSync();
   3. console.info(`vibratorInfoList: ${JSON.stringify(vibratorInfoList)}`);
   4. // ...
   5. } catch (error) {
   6. let e: BusinessError = error as BusinessError;
   7. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   8. }
   ```

   **情形二** 查询指定设备的一个或多个马达信息：

   ```
   1. try {
   2. const vibratorParam: vibrator.VibratorInfoParam = {
   3. deviceId: -1    // deviceId 需要是查询出来真实存在的设备
   4. }
   5. const vibratorInfoList: vibrator.VibratorInfo[] = vibrator.getVibratorInfoSync(vibratorParam);
   6. console.info(`vibratorInfoList: ${JSON.stringify(vibratorInfoList)}`);
   7. // ...
   8. } catch (error) {
   9. let e: BusinessError = error as BusinessError;
   10. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   11. }
   ```
6. 根据指定振动效果和振动属性触发马达振动。

   **情形一** 按照指定持续时间触发马达振动：

   ```
   1. try {
   2. // 触发马达振动
   3. vibrator.startVibration({
   4. type: 'time',
   5. duration: 1000,
   6. }, {
   7. id: 0,
   8. usage: 'alarm'
   9. }, (error: BusinessError) => {
   10. if (error) {
   11. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   12. return;
   13. }
   14. console.info('Succeed in starting vibration');
   15. });
   16. } catch (err) {
   17. let e: BusinessError = err as BusinessError;
   18. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   19. }
   ```

   **情形二** 按照预置振动效果触发马达振动，可先查询振动效果是否被支持，再调用振动接口：

   ```
   1. try {
   2. vibrator.isSupportEffect(this.realEffectId, (err: BusinessError, state: boolean) => {
   3. if (err) {
   4. console.error(`Failed to query effect. Code: ${err.code}, message: ${err.message}`);
   5. return;
   6. }
   7. console.info('Succeed in querying effect');
   8. if (state) {
   9. try {
   10. // 触发马达振动
   11. vibrator.startVibration({
   12. type: 'preset',
   13. effectId: this.realEffectId,
   14. count: 1,
   15. intensity: 50,
   16. }, {
   17. usage: 'unknown'
   18. }, (error: BusinessError) => {
   19. if (error) {
   20. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   21. } else {
   22. console.info('Succeed in starting vibration');
   23. }
   24. });
   25. } catch (error) {
   26. let e: BusinessError = error as BusinessError;
   27. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   28. }
   29. }
   30. })
   31. } catch (error) {
   32. let e: BusinessError = error as BusinessError;
   33. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   34. }
   ```

   **情形三** 按照自定义振动配置文件触发马达振动：

   ```
   1. // 获取文件资源描述符
   2. let rawFd: resourceManager.RawFileDescriptor | undefined = this.uiContext.getHostContext()?.resourceManager.getRawFdSync(fileName);
   3. if (rawFd != undefined) {
   4. // 触发马达振动
   5. try {
   6. vibrator.startVibration({
   7. type: "file",
   8. hapticFd: { fd: rawFd.fd, offset: rawFd.offset, length: rawFd.length }
   9. }, {
   10. id: 0,
   11. usage: 'alarm' // 根据实际选择类型归属不同的开关管控
   12. }, (error: BusinessError) => {
   13. if (error) {
   14. console.error(`Failed to start vibration. Code: ${error.code}, message: ${error.message}`);
   15. return;
   16. }
   17. console.info('Succeed in starting vibration');
   18. });
   19. } catch (err) {
   20. let e: BusinessError = err as BusinessError;
   21. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   22. } finally {
   23. vibrator.stopVibration();
   24. this.uiContext.getHostContext()?.resourceManager.closeRawFdSync(fileName);
   25. }
   26. }
   ```

   **情形四** Pattern类型的马达振动：

   添加短振事件的方式获取Pattern，并触发振动：

   ```
   1. let builder: vibrator.VibratorPatternBuilder = new vibrator.VibratorPatternBuilder();
   2. try {
   3. let param: vibrator.TransientParam = {
   4. intensity: 80,
   5. frequency: 70,
   6. index: 0
   7. }
   8. builder.addTransientEvent(0, param);
   9. console.info(`addTransientEvent builder is ${builder.build()}`);
   10. } catch (error) {
   11. let e: BusinessError = error as BusinessError;
   12. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   13. }
   14. try {
   15. vibrator.startVibration({
   16. type: "pattern",
   17. pattern: builder.build()
   18. }, {
   19. id: 1,
   20. deviceId: -1,
   21. // 根据实际选择类型归属不同的开关管控
   22. usage: "alarm"
   23. }, (error: BusinessError) => {
   24. if (error) {
   25. let e: BusinessError = error as BusinessError;
   26. console.error(`Vibrate fail. Code: ${e.code}, message: ${e.message}`);
   27. } else {
   28. console.info(`vibrate success`);
   29. }
   30. });
   31. } catch (error) {
   32. let e: BusinessError = error as BusinessError;
   33. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   34. }
   ```

   添加长振事件的方式获取Pattern，并触发振动：

   ```
   1. let builder: vibrator.VibratorPatternBuilder = new vibrator.VibratorPatternBuilder();
   2. try {
   3. // VibratorCurvePoint参数最少设置4个，最大设置16个
   4. let pointsMe: vibrator.VibratorCurvePoint[] = [
   5. { time: 0, intensity: 0, frequency: -7 },
   6. { time: 42, intensity: 1, frequency: -6 },
   7. { time: 128, intensity: 0.94, frequency: -4 },
   8. { time: 217, intensity: 0.63, frequency: -14 },
   9. { time: 763, intensity: 0.48, frequency: -14 },
   10. { time: 1125, intensity: 0.53, frequency: -10 },
   11. { time: 1503, intensity: 0.42, frequency: -14 },
   12. { time: 1858, intensity: 0.39, frequency: -14 },
   13. { time: 2295, intensity: 0.34, frequency: -17 },
   14. { time: 2448, intensity: 0.21, frequency: -14 },
   15. { time: 2468, intensity: 0, frequency: -21 }
   16. ]
   17. let param: vibrator.ContinuousParam = {
   18. intensity: 97,
   19. frequency: 34,
   20. points: pointsMe,
   21. index: 0
   22. }
   23. builder.addContinuousEvent(0, 2468, param);
   24. console.info(`addContinuousEvent builder is ${builder.build()}`);
   25. } catch (error) {
   26. let e: BusinessError = error as BusinessError;
   27. console.error(`Exception. Code ${e.code}`);
   28. }
   29. try {
   30. vibrator.startVibration({
   31. type: 'pattern',
   32. pattern: builder.build()
   33. }, {
   34. id: 1,
   35. deviceId: -1,
   36. usage:"alarm",
   37. }, (error: BusinessError) => {
   38. if (error) {
   39. let e: BusinessError = error as BusinessError;
   40. console.error(`Vibrate fail. Code: ${e.code}, message: ${e.message}`);
   41. } else {
   42. console.info(`vibrate success`);
   43. }
   44. });
   45. } catch (error) {
   46. let e: BusinessError = error as BusinessError;
   47. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   48. }
   ```
7. 停止马达的振动。

   **方式一** 按照指定模式停止对应的马达振动，自定义振动不支持此类停止方式：

   ​停止固定时长振动：

   ```
   1. try {
   2. // 按照VIBRATOR_STOP_MODE_TIME模式停止振动
   3. vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_TIME, (error: BusinessError) => {
   4. if (error) {
   5. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   6. return;
   7. }
   8. console.info('Succeed in stopping vibration');
   9. })
   10. } catch (err) {
   11. let e: BusinessError = err as BusinessError;
   12. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   13. }
   ```

   ​停止预置振动：

   ```
   1. try {
   2. // 按照VIBRATOR_STOP_MODE_PRESET模式停止振动
   3. vibrator.stopVibration(vibrator.VibratorStopMode.VIBRATOR_STOP_MODE_PRESET, (error: BusinessError) => {
   4. if (error) {
   5. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   6. return;
   7. }
   8. console.info('Succeed in stopping vibration');
   9. })
   10. } catch (err) {
   11. let e: BusinessError = err as BusinessError;
   12. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   13. }
   ```

   **方式二** 停止所有模式的马达振动，包括自定义振动：

   ```
   1. try {
   2. // 停止所有模式的马达振动
   3. vibrator.stopVibration((error: BusinessError) => {
   4. if (error) {
   5. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   6. return;
   7. }
   8. console.info('Succeed in stopping vibration');
   9. })
   10. } catch (error) {
   11. let e: BusinessError = error as BusinessError;
   12. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   13. }
   ```

   **方式三** 停止指定设备的振动：

   ```
   1. const vibratorInfoParam: vibrator.VibratorInfoParam = {
   2. deviceId: -1   // deviceId 需要是查询出来真实存在的设备
   3. }
   4. try {
   5. vibrator.stopVibration(vibratorInfoParam).then(() => {
   6. console.info('Succeed in stopping vibration');
   7. }, (error: BusinessError) => {
   8. console.error(`Failed to stop vibration. Code: ${error.code}, message: ${error.message}`);
   9. });
   10. } catch (error) {
   11. let e: BusinessError = error as BusinessError;
   12. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   13. }
   ```
8. 动态马达状态变化监听。

   注册监听。

   ```
   1. // 回调函数
   2. vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
   3. console.info('vibrator state callback info:', JSON.stringify(data));
   4. // ...
   5. }
   6. // ...
   7. try {
   8. // 订阅 vibratorStateChange事件
   9. vibrator.on('vibratorStateChange', this.vibratorStateChangeCallback);
   10. } catch (error) {
   11. let e: BusinessError = error as BusinessError;
   12. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   13. }
   ```

   取消监听,取消传入的callback需与注册的一致。

   ```
   1. // 回调函数
   2. vibratorStateChangeCallback = (data: vibrator.VibratorStatusEvent) => {
   3. console.info('vibrator state callback info:', JSON.stringify(data));
   4. // ...
   5. }
   6. // ...
   7. try {
   8. // 取消订阅 vibratorStateChange事件
   9. vibrator.off('vibratorStateChange', this.vibratorStateChangeCallback);
   10. // 取消订阅所有 vibratorStateChange事件
   11. // vibrator.off('vibratorStateChange');
   12. } catch (error) {
   13. let e: BusinessError = error as BusinessError;
   14. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   15. }
   ```
9. 通过设备ID和马达ID获取预置振动效果信息。

   ```
   1. try {
   2. const effectInfo: vibrator.EffectInfo = vibrator.getEffectInfoSync('haptic.clock.timer', { deviceId: -1, vibratorId: 1});
   3. console.info(`isEffectSupported: ${effectInfo.isEffectSupported}`);
   4. // ...
   5. } catch (error) {
   6. let e: BusinessError = error as BusinessError;
   7. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
   8. }
   ```
10. 查询是否支持高清振动。

    ```
    1. try {
    2. // 查询是否支持高清振动
    3. let ret = vibrator.isHdHapticSupported();
    4. console.info(`The query result is ${ret}`);
    5. // ...
    6. } catch (error) {
    7. let e: BusinessError = error as BusinessError;
    8. console.error(`An unexpected error occurred. Code: ${e.code}, message: ${e.message}`);
    9. }
    ```
