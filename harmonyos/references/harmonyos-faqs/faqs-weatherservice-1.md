---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-weatherservice-1
title: 查询天气数据失败怎么解决
breadcrumb: FAQ > 应用服务开发 > 天气数据服务（Weather Service Kit） > 查询天气数据失败怎么解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a9d594c6a8a1e67c64181a5d93ec94317039f5a05bd2bc1afc9c7781501e4bc8
---

## 问题现象

常见的查询天气数据失败的场景如下，该如何解决？

1. 在使用weatherService获取天气信息时，报1011900001错误码。
2. 请求了分钟级降水预报/天气预警/潮汐，未返回任何数据。

## 背景知识

[Weather Service Kit](../harmonyos-guides/weather-service-introduction.md)可以返回以下天气数据，满足开发者的天气数据使用需求：天气预报、分钟级降水预报、天气预警、天气指数、天文数据、潮汐。

## 问题定位

1. 查询错误码含义，检查是否已在AGC平台开通天气服务和相关权限。
2. 请求没有返回数据，确认区域当时是否有短时降水、天气预警发布、潮汐站点。

## 分析结论

1. 1011900001表示未开通天气服务，或者应用签名配置不正确。
2. 如果查询区域当时无短时降水、无天气预警发布或预警已经解除、无潮汐站点时，没有数据返回属于正常现象。

## 修改建议

1. 开发前请先参考[应用开发准备](../harmonyos-guides/application-dev-overview.md)完成基本准备工作及指纹配置，并在AGC平台上开通天气服务相关功能。接口调用过程中，天气服务会对您的Profile文件进行鉴权，所以在开发应用之前，您需要按照调试HarmonyOS应用的流程，申请并[配置调试签名信息](../harmonyos-guides/ide-signing.md)；在发布应用之前，要按照[发布HarmonyOS应用](../app/agc-help-release-app-0000002271695230.md)的流程，申请并配置正式签名信息。
2. 获取用户当前位置的天气数据需要调用位置服务，需要申请[位置权限](../harmonyos-guides/weather-service-preparations.md#可选申请位置权限)。如果查询区域当时无短时降水、无天气预警发布或预警已经解除、无潮汐站点时，没有数据返回属于正常现象。

## 常见FAQ

Q：依据修改建议，在AppGallery Connect中，选不到开通“天气服务”能力开关，无法开通天气服务，是什么原因？

A：[天气服务](../harmonyos-guides/weather-service-preparations.md#开通天气服务)当前仅面向系统应用开放。

Q：Weather Service Kit小时数据HourlyWeather里面的空气质量aqi数据为空，文档里面有这个字段，但是实际发现没返回数据。

A：[HourlyWeather](../harmonyos-references/weather-service-weatherservice.md#hourlyweather)里面的空气质量aqi为可选项，是可能为空的，不是必有数据项。
