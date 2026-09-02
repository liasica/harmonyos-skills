---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-13
title: 调用sensor.once接口获取走路时的步频数据不准确
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 调用sensor.once接口获取走路时的步频数据不准确
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a15ab93a5d92d7423ab9823bf4b07b556224d99060f49ec2276d394e277bd201
---

## 问题现象

通过调用sensor.once接口获取计步器传感器数据，并计算走路时的步频，得到的数据差距较大，是什么原因？

## 总结

[sensor.once](../harmonyos-references/js-apis-sensor.md#sensoroncesensoridpedometer9)：获取一次计步器传感器数据。计步传感器数据上报有一定延迟，延迟时间由具体的实现产品决定。

[sensor.on](../harmonyos-references/js-apis-sensor.md#sensoronsensoridpedometer9)：订阅计步器传感器数据。计步传感器数据上报有一定延迟，延迟时间由具体的实现产品决定。

## 解决方案

对于计步器类型的传感器PEDOMETER，[sensor.once](../harmonyos-references/js-apis-sensor.md#sensoroncesensoridpedometer9)接口用于获取一次计步器传感器数据，而[sensor.on](../harmonyos-references/js-apis-sensor.md#sensoronsensoridpedometer9)接口用于订阅且每隔一段时间都会获取一次计步器传感器数据。若一直处于走路状态，建议使用sensor.on接口获取稳定的步频数据。

## 总结

[sensor.once](../harmonyos-references/js-apis-sensor.md#sensoroncesensoridpedometer9)：适用于单次计步。

[sensor.on](../harmonyos-references/js-apis-sensor.md#sensoronsensoridpedometer9)：适用于持续计步。
