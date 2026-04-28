---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-sensor-use-check
title: @performance/reasonable-sensor-use-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/reasonable-sensor-use-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:17+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d121fd3e9a0723624911c3f2de89c8a511120ddcefb407175daf4a56a9384e1e
---

应用退到后台时，禁止使用传感器资源。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/reasonable-sensor-use-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { sensor } from '@kit.SensorServiceKit';
3. export default class EntryAbility extends UIAbility {
4. onForeground(): void {
5. // In the foreground, listen to the required type of sensor based on the service requirements
6. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
7. });
8. }
9. onBackground(): void {
10. // The background cancels the listening
11. sensor.off(sensor.SensorId.ACCELEROMETER);
12. }
13. }
```

## 反例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { sensor } from '@kit.SensorServiceKit';
3. export default class EntryAbility extends UIAbility {
4. onForeground(): void {
5. // In the foreground, listen to the required type of sensor based on the service requirements
6. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
7. });
8. }
9. onBackground(): void {
10. }
11. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
