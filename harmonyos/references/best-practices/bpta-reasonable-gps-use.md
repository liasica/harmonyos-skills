---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-gps-use
title: GPS资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > GPS资源合理使用
category: best-practices
scraped_at: 2026-09-02T14:53:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:0fffac608562416f5624da49efc67222eb4128d817488d6b1b589153a599edc1
---

无长时间任务的应用退到后台时，禁止使用定位服务。

## 约束

未申请长时任务的应用退到后台后，系统会强制停止其定位请求。

## 示例

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { geoLocationManager } from '@kit.LocationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// ...

export default class EntryAbility extends UIAbility {
  // ...
  onForeground(): void {
    // Create a location request based on service requirements at the foreground
    let requestInfo: geoLocationManager.LocationRequest = {
      'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
      'timeInterval': 0,
      'distanceInterval': 0,
      'maxAccuracy': 0
    };
    let locationChange = (location: geoLocationManager.Location): void => {
      console.log('locationChanger:data:' + JSON.stringify(location));
    };
    try {
      //The change of the listening position
      geoLocationManager.on('locationChange', requestInfo, locationChange);
    } catch (error) {
      let err = error as BusinessError;
      hilog.warn(0x000, 'testTag', `geoLocationManager on failed, code=${err.code}, message=${err.message}`);
    }
  }

  onBackground(): void {
    try {
      //The backstage cancels the listening
      geoLocationManager.off('locationChange', locationChange);
    } catch (error) {
      let err = error as BusinessError;
      hilog.warn(0x000, 'testTag', `geoLocationManager off failed, code=${err.code}, message=${err.message}`);
    }
  }
}
```
