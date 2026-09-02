---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-sensor-use
title: 传感器资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 传感器资源合理使用
category: best-practices
scraped_at: 2026-09-02T14:53:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:30eadabb1d432404423920cc5aa5239a5b145eec2ab13ad01c14ed5ba20a6219
---

应用退至后台时，禁止使用传感器资源。若有正常业务需求，申请后台长时任务后，可在锁屏状态下获取传感器信息。

## 约束

应用退至后台时，禁止使用传感器资源。若有正常业务需求，申请后台长时任务后，可在锁屏状态下获取传感器信息。

## 示例

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  // ...
  onForeground(): void {
    try {
      //In the foreground, listen to the required type of sensor based on the service requirements
      sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
        console.info("Succeeded in obtaining data.x:" + data.x + "y:" + data.y + "z:" + data.z);
      }, {
        interval: 100000000
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.warn(0x000, 'testTag', `sensor on failed, code=${err.code}, message=${err.message}`);
    }
  }

  onBackground(): void {
    try {
      //The backstage cancels the listening
      sensor.off(sensor.SensorId.ACCELEROMETER);
    } catch (error) {
      let err = error as BusinessError;
      hilog.warn(0x000, 'testTag', `sensor off failed, code=${err.code}, message=${err.message}`);
    }
  }
}
```

有关传感器开发相关接口的使用，详情可以参考[传感器开发指导](../harmonyos-guides/sensor-guidelines.md)。
