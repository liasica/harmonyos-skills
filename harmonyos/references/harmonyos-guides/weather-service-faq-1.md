---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/weather-service-faq-1
title: 如何获取指定城市的天气数据？
breadcrumb: 指南 > 应用服务 > Weather Service Kit（天气服务） > Weather Service Kit 常见问题 > 如何获取指定城市的天气数据？
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a8b3de0ee851313d7ed925643e311a96a5e8ac6dffbf915f1fc666e7f595c4f
---

先调用[getAddressesFromLocationName](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocationname-1)方法获取指定城市的经纬度信息，然后根据返回的经纬度数据调用[getWeather](../harmonyos-references/weather-service-weatherservice.md#weatherservicegetweather)方法获取天气数据。
