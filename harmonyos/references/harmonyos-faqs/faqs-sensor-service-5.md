---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-5
title: 如何获取设备传感器列表
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 如何获取设备传感器列表
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac33b53e5b73ba5d3dc7afe4a4c49bc6b47dcb1c5d2b60d66c5f5c1f2aef0672
---

## 问题现象

设备中内置了大量传感器，在使用传感器功能时，需要先获取传感器列表，然后判断设备是否具有所需的传感器，有哪些方式可以获取到设备的传感器列表？

## 背景知识

* [传感器类型](../harmonyos-guides/sensor-overview.md#传感器类型)：系统传感器是应用访问底层硬件传感器的一种设备抽象概念。开发者根据传感器提供的[Sensor接口](../harmonyos-references/js-apis-sensor.md)，可以查询设备上的传感器，订阅传感器数据，并根据传感器数据定制相应的算法开发各类应用，比如指南针、运动健康、游戏等。
* [sensorId](../harmonyos-references/js-apis-sensor.md#sensorid9)：当前支持订阅或取消订阅的传感器类型Id。
* [sensor.getSensorList](../harmonyos-references/js-apis-sensor.md#sensorgetsensorlist9)：获取设备上的所有传感器信息。

## 解决方案

* **方案一：** 通过系统API接口[sensor.getSensorListSync](../harmonyos-references/js-apis-sensor.md#sensorgetsensorlistsync12)获取。
* **方案二：** 通过hdc命令获取。
  1. 通过cmd进入命令窗口，或通过IDE进入Terminal命令窗口。
  2. 执行hdc shell。
  3. 执行hidumper -s 3601 -a -l命令。

## 常见FAQ

Q：GT系列、Fit系列是否支持心率读取？

A：GT系列、Fit系列为Lite Wearable设备，两款手表支持心率读取，参考文档：[Sensor.subscribeHeartRate](../harmonyos-references/js-apis-system-sensor.md#sensorsubscribeheartrate)，需要申请权限：ohos.permission.READ\_HEALTH\_DATA。
