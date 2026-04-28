---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-gps-use-check
title: @performance/reasonable-gps-use-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/reasonable-gps-use-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:17+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:5567a5392817f6969f866744bb631f3d9992a133e3e9539aa5322fab72d43503
---

无长时任务的应用退到后台时，禁止使用定位服务。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/reasonable-gps-use-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { geoLocationManager } from '@kit.LocationKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground(): void {
6. //在前台时按业务所需创建定位请求
7. let requestInfo: geoLocationManager.LocationRequest = {
8. 'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
9. 'timeInterval': 0,
10. 'distanceInterval': 0,
11. 'maxAccuracy': 0
12. };
13. let locationChange = (location: geoLocationManager.Location): void => {
14. console.log('locationChanger:data:' + JSON.stringify(location));
15. };
16. //监听位置的变化
17. geoLocationManager.on('locationChange', requestInfo, locationChange);
18. }

20. onBackground(): void {
21. //退后台取消监听
22. geoLocationManager.off('locationChange');
23. }
24. }
```

## 反例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { geoLocationManager } from '@kit.LocationKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground(): void {
6. //在前台时按业务所需创建定位请求
7. let requestInfo: geoLocationManager.LocationRequest = {
8. 'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
9. 'timeInterval': 0,
10. 'distanceInterval': 0,
11. 'maxAccuracy': 0
12. };
13. let locationChange = (location: geoLocationManager.Location): void => {
14. console.log('locationChanger:data:' + JSON.stringify(location));
15. };
16. //监听位置的变化
17. geoLocationManager.on('locationChange', requestInfo, locationChange);
18. }

20. onBackground(): void {
21. }
22. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
