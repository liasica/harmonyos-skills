---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/sensor-service-kit-faq-0001
title: 设备竖立状态判断
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 常见问题 > 设备竖立状态判断
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:32+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:f93dac3718f44fbebf62ad05311958a7df76b8f7501462a70b77d0bbe247e0e1
---

**Q：在立体空间里如何判断设备是否是竖立的？**

**A**：[Sensor Service Kit](../harmonyos-guides/sensorservice-kit-intro.md)提供了订阅重力传感器[GRAVITY](../harmonyos-references/js-apis-sensor.md#gravity9)的能力，当传感器数据y轴的值越接近当地的重力加速度值(单位:m/s²)则越竖直。
