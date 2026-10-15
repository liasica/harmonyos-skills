---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-position-navigation-use
title: 后台定位导航服务合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台软件资源合理使用 > 后台定位导航服务合理使用
category: best-practices
scraped_at: 2026-10-16T07:06:48+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:ed54283ff5f1aa9360db0270f5ddf5b2e5c1826d1d8f676e35c4c5ba52388cc5
---

使用定位导航服务时，申请长时任务的应用需设置正确应用场景。

## 约束

不涉及

## 示例

应用可以使用被动定位：

方式1：

```typescript
import { geoLocationManager } from '@kit.LocationKit';

let requestInfo: geoLocationManager.LocationRequest = {
  'scenario': geoLocationManager.LocationRequestScenario.NO_POWER,
  'timeInterval': 0,
  'distanceInterval': 0,
  'maxAccuracy': 0
};
```

方式2：

```typescript
import { geoLocationManager } from '@kit.LocationKit';

let requestInfo: geoLocationManager.LocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.LOW_POWER,
  'timeInterval': 0,
  'distanceInterval': 0,
  'maxAccuracy': 0
};
```

有关定位服务开发相关接口的使用，详情可以参考[Location Kit（位置服务）](../harmonyos-guides/location-kit.md)。
