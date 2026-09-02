---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sensorservicekit-7001
title: Sensor Service Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Sensor Service Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:b9ac40632b0c13aad70801b6c38ffee56cbdb4457624b4535c427f8eec98bbd2
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 权限变更 | 类名：sensor；  API声明：function once(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION, callback: Callback<LinearAccelerometerResponse>): void;  差异内容：ohos.permission.ACCELERATION | 类名：sensor；  API声明：function once(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION, callback: Callback<LinearAccelerometerResponse>): void;  差异内容：ohos.permission.ACCELEROMETER | api/@ohos.sensor.d.ts |
