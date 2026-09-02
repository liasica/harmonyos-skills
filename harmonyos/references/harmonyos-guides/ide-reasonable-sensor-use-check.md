---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-sensor-use-check
title: "@performance/reasonable-sensor-use-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/reasonable-sensor-use-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1248e53a94f5990561d9fadc1f7c34f1bf31c6bfe33f7ca053afc81b15b00d43
---

应用退到后台时，禁止使用传感器资源。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/reasonable-sensor-use-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { UIAbility } from '@kit.AbilityKit';
import { sensor } from '@kit.SensorServiceKit';
export default class EntryAbility extends UIAbility {
  onForeground(): void {
    // In the foreground, listen to the required type of sensor based on the service requirements
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    });
  }
  onBackground(): void {
    // The background cancels the listening
    sensor.off(sensor.SensorId.ACCELEROMETER);
  }
}
```

## 反例

```screen
import { UIAbility } from '@kit.AbilityKit';
import { sensor } from '@kit.SensorServiceKit';
export default class EntryAbility extends UIAbility {
  onForeground(): void {
    // In the foreground, listen to the required type of sensor based on the service requirements
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    });
  }
  onBackground(): void {
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
