---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-2
title: 如何读取运动传感器比如加速度传感器
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 如何读取运动传感器比如加速度传感器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:55f963df1d1ceb5b7ea4c7b0aff946b769768c0e694001296020ad4401ea67a2
---

1. 导入sensor（传感器）模块：

```typescript
import { sensor } from '@kit.SensorServiceKit';
```

2. 设置加速度传感器的数据回调监听：

```typescript
try {
  sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
    console.info('X-coordinate component: ' + data.x);
    console.info('Y-coordinate component: ' + data.y);
    console.info('Z-coordinate component: ' + data.z);
  }, { interval: 10000000 });
} catch (err) {
  console.error('On fail, errCode: ' + err.code + ' ,msg: ' + err.message);
}
```

**参考链接**

[传感器](../harmonyos-references/js-apis-sensor.md)
