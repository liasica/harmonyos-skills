---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-sensorlistenernotoff
title: SensorListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > SensorListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2c9cebb84fa106462dc67ca605e1c591be22e61c962d2d995c13cbd1ff2cb367
---

[@ohos.sensor](../doccenter-references/api/js-apis-sensor.md)传感器提供获取传感器数据的能力，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

**说明** 

调用.on()监听接口后，只要存在对应的.off()调用（即取消全部或部分监听），不产生告警；仅当代码中不存在任何.off()调用时，才产生告警。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "SensorListenerNotOff",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import { sensor } from '@kit.SensorServiceKit';
import Ability from '@ohos.app.ability.Ability';

/**
 * 正例：正确释放资源
 */
export class TestRelease extends Ability {
    private sensorCallBack1 = (data: object) => {
        console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
    }
    private sensorCallBack2 = (data: object) => {
        console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
    }
    onCreate(): void {
        sensor.on(sensor.SensorId.ACCELEROMETER, this.sensorCallBack1);
        sensor.on(sensor.SensorId.ACCELEROMETER, this.sensorCallBack2);
    }
    onDestroy(): void {
        sensor.off(sensor.SensorId.ACCELEROMETER, this.sensorCallBack1);
        sensor.off(sensor.SensorId.ACCELEROMETER, this.sensorCallBack2);
    }
}
```

## 反例

```ts
import { sensor } from '@kit.SensorServiceKit';
import Ability from '@ohos.app.ability.Ability';

/**
 * 反例：未释放资源
 */
export class TestNotRelease extends Ability {
    private sensorCallBack1 = (data: object) => {
        console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
    }
    private sensorCallBack2 = (data: object) => {
        console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
    }
    onCreate(): void {
        sensor.on(sensor.SensorId.ACCELEROMETER, this.sensorCallBack1);
        sensor.on(sensor.SensorId.ACCELEROMETER, this.sensorCallBack2); // leak
    }
    onDestroy(): void {
        sensor.off(sensor.SensorId.ACCELEROMETER, this.sensorCallBack1);
    }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
