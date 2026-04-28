---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sensorservicekit-6021
title: Sensor Service Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Sensor Service Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:49+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:82efa9f2ac10df40b89da11e4923b7ce021e76edc76baa036ec659b10f171586
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：SensorId；  API声明：FUSION\_PRESSURE = 283  差异内容：FUSION\_PRESSURE = 283 | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：sensor；  API声明：function on(type: SensorId.FUSION\_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void;  差异内容：function on(type: SensorId.FUSION\_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void; | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：sensor；  API声明：function off(type: SensorId.FUSION\_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void;  差异内容：function off(type: SensorId.FUSION\_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void; | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：sensor；  API声明：interface FusionPressureResponse  差异内容：interface FusionPressureResponse | api/@ohos.sensor.d.ts |
| 新增API | NA | 类名：FusionPressureResponse；  API声明：fusionPressure: number;  差异内容：fusionPressure: number; | api/@ohos.sensor.d.ts |
