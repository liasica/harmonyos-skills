---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sensorservicekit-6101
title: Sensor Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Sensor Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f5a5cd771ce2ab06ac8fa1e2ddba6c19335a2841ba6d1c0446f4410c4d1bcbe2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：sensor；  API声明：function on(type: SensorId.FUSION\_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void;  差异内容：NA | 类名：sensor；  API声明：function on(type: SensorId.FUSION\_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void;  差异内容：401 | api/@ohos.sensor.d.ts |
| 新增错误码 | 类名：sensor；  API声明：function off(type: SensorId.FUSION\_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void;  差异内容：NA | 类名：sensor；  API声明：function off(type: SensorId.FUSION\_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void;  差异内容：401 | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：Sensor；  API声明：isMockSensor?: boolean;  差异内容：isMockSensor?: boolean; | api/@ohos.sensor.d.ts |
