---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-sensor-use
title: 传感器资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 传感器资源合理使用
category: best-practices
scraped_at: 2026-04-28T08:22:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:2568229a384b935f03d3f1251c3bc3829fde2fc338f2556760f301ffcf78d981
---

应用退至后台时，禁止使用传感器资源。若有正常业务需求，申请后台长时任务后，可在锁屏状态下获取传感器信息。

## 约束

应用退至后台时，禁止使用传感器资源。若有正常业务需求，申请后台长时任务后，可在锁屏状态下获取传感器信息。

## 示例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { sensor } from '@kit.SensorServiceKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. export default class EntryAbility extends UIAbility {
7. // ...
8. onForeground(): void {
9. try {
10. //In the foreground, listen to the required type of sensor based on the service requirements
11. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
12. console.info("Succeeded in obtaining data.x:" + data.x + "y:" + data.y + "z:" + data.z);
13. }, {
14. interval: 100000000
15. });
16. } catch (error) {
17. let err = error as BusinessError;
18. hilog.warn(0x000, 'testTag', `sensor on failed, code=${err.code}, message=${err.message}`);
19. }
20. }

22. onBackground(): void {
23. try {
24. //The backstage cancels the listening
25. sensor.off(sensor.SensorId.ACCELEROMETER);
26. } catch (error) {
27. let err = error as BusinessError;
28. hilog.warn(0x000, 'testTag', `sensor off failed, code=${err.code}, message=${err.message}`);
29. }
30. }
31. }
```

[Sensor.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/Sensor.ets#L6-L37)

有关传感器开发相关接口的使用，详情可以参考[传感器开发指导](../harmonyos-guides/sensor-guidelines.md)。
