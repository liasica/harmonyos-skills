---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-8
title: 如何判断设备在立体空间里是竖立着的
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 如何判断设备在立体空间里是竖立着的
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:1006601e04586ea34cddafbccab06258a3294f5ffa3d8366bda9907e2a0b2f4d
---

## 问题现象

在立体空间里如何判断设备是否是竖立的。

## 解决方案

[Sensor Service Kit](../harmonyos-guides/sensorservice-kit-intro.md)提供了订阅重力传感器[GRAVITY](../harmonyos-references/js-apis-sensor.md#sensoronsensoridgravity9)的能力，当传感器数据y轴的值越接近当地的重力加速度值(单位:m/s²)则越竖直。
