---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-2
title: 如何读取运动传感器比如加速度传感器
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 如何读取运动传感器比如加速度传感器
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b0646a3b33cee8dfc948f6b06eb47c64bc88a378f48af92dae2ab3f99baec34e
---

1. 导入sensor（传感器）模块：

```
1. import { sensor } from '@kit.SensorServiceKit';
```

[Accelerometer.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/SensorService/entry/src/main/ets/pages/Accelerometer.ets#L21-L21)

2. 设置加速度传感器的数据回调监听：

```
1. try {
2. sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
3. console.info('X-coordinate component: ' + data.x);
4. console.info('Y-coordinate component: ' + data.y);
5. console.info('Z-coordinate component: ' + data.z);
6. }, { interval: 10000000 });
7. } catch (err) {
8. console.error('On fail, errCode: ' + err.code + ' ,msg: ' + err.message);
9. }
```

[Accelerometer.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/SensorService/entry/src/main/ets/pages/Accelerometer.ets#L26-L34)

**参考链接**

[传感器](../harmonyos-references/js-apis-sensor.md)
