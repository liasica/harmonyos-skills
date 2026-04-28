---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-position-navigation-use
title: 后台定位导航服务合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台软件资源合理使用 > 后台定位导航服务合理使用
category: best-practices
scraped_at: 2026-04-28T08:22:46+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:462bfc0fe6ce86ba40f48d23475755f512be6ce7514dba0a0bd2c6144580589f
---

使用定位导航服务时，申请长时任务的应用需设置正确应用场景。

## 约束

NA

## 示例

应用可以使用被动定位：

方式1：

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let requestInfo: geoLocationManager.LocationRequest = {
4. 'scenario': geoLocationManager.LocationRequestScenario.NO_POWER,
5. 'timeInterval': 0,
6. 'distanceInterval': 0,
7. 'maxAccuracy': 0
8. };
```

[GpsOne.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/GpsOne.ets#L21-L28)

方式2：

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let requestInfo: geoLocationManager.LocationRequest = {
4. 'priority': geoLocationManager.LocationRequestPriority.LOW_POWER,
5. 'timeInterval': 0,
6. 'distanceInterval': 0,
7. 'maxAccuracy': 0
8. };
```

[GpsTwo.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseSoftware/entry/src/main/ets/pages/GpsTwo.ets#L21-L28)

有关定位服务开发相关接口的使用，详情可以参考[Location Kit（位置服务）](../harmonyos-guides/location-kit.md)。
