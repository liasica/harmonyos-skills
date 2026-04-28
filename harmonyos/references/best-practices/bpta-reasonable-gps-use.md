---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-gps-use
title: GPS资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > GPS资源合理使用
category: best-practices
scraped_at: 2026-04-28T08:22:45+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:ee40e6f49f449b023460e5f8c3b4eef52385a1c03119c09c07f930e77a5dc73a
---

无长时间任务的应用退到后台时，禁止使用定位服务。

## 约束

未申请长时任务的应用退到后台后，系统会强制停止其定位请求。

## 示例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { geoLocationManager } from '@kit.LocationKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. // ...

8. export default class EntryAbility extends UIAbility {
9. // ...
10. onForeground(): void {
11. // Create a location request based on service requirements at the foreground
12. let requestInfo: geoLocationManager.LocationRequest = {
13. 'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
14. 'timeInterval': 0,
15. 'distanceInterval': 0,
16. 'maxAccuracy': 0
17. };
18. let locationChange = (location: geoLocationManager.Location): void => {
19. console.log('locationChanger:data:' + JSON.stringify(location));
20. };
21. try {
22. //The change of the listening position
23. geoLocationManager.on('locationChange', requestInfo, locationChange);
24. } catch (error) {
25. let err = error as BusinessError;
26. hilog.warn(0x000, 'testTag', `geoLocationManager on failed, code=${err.code}, message=${err.message}`);
27. }
28. }

30. onBackground(): void {
31. try {
32. //The backstage cancels the listening
33. geoLocationManager.off('locationChange', locationChange);
34. } catch (error) {
35. let err = error as BusinessError;
36. hilog.warn(0x000, 'testTag', `geoLocationManager off failed, code=${err.code}, message=${err.message}`);
37. }
38. }
39. }
```

[Gps.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/Gps.ets#L6-L50)
