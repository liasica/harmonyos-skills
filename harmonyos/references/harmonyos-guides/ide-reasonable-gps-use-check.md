---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-gps-use-check
title: "@performance/reasonable-gps-use-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/reasonable-gps-use-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8fbf1c0816cc2f444390e352fb2cbdd3e93848027484eb0427d9e08d43fcff3c
---

未申请长时任务的应用退到后台时，禁止使用定位服务。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/reasonable-gps-use-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { UIAbility } from '@kit.AbilityKit';
import { geoLocationManager } from '@kit.LocationKit';

export default class EntryAbility extends UIAbility {
  onForeground(): void {
    //在前台时按业务所需创建定位请求
    let requestInfo: geoLocationManager.LocationRequest = {
      'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
      'timeInterval': 0,
      'distanceInterval': 0,
      'maxAccuracy': 0
    };
    let locationChange = (location: geoLocationManager.Location): void => {
      console.log('locationChanger:data:' + JSON.stringify(location));
    };
    //监听位置的变化
    geoLocationManager.on('locationChange', requestInfo, locationChange);
  }

  onBackground(): void {
    //退后台取消监听
    geoLocationManager.off('locationChange');
  }
}
```

## 反例

```screen
import { UIAbility } from '@kit.AbilityKit';
import { geoLocationManager } from '@kit.LocationKit';

export default class EntryAbility extends UIAbility {
  onForeground(): void {
    //在前台时按业务所需创建定位请求
    let requestInfo: geoLocationManager.LocationRequest = {
      'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
      'timeInterval': 0,
      'distanceInterval': 0,
      'maxAccuracy': 0
    };
    let locationChange = (location: geoLocationManager.Location): void => {
      console.log('locationChanger:data:' + JSON.stringify(location));
    };
    //监听位置的变化
    geoLocationManager.on('locationChange', requestInfo, locationChange);
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
