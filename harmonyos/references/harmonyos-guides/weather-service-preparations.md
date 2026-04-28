---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/weather-service-preparations
title: 开发准备
breadcrumb: 指南 > 应用服务 > Weather Service Kit（天气服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38ba3b3eb9150162589b022a93ab2cfa309364fdf68c6e6b8d004fde8d1e321b
---

在阅读本章节前，请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

## 开通天气服务

说明

Weather Service Kit当前仅面向系统应用开放，暂不对外开放。

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)。
2. 选择“开发与服务”，找到您的项目，选择您创建的HarmonyOS应用。
3. 选择“开放能力管理”标签，勾选“天气服务”能力开关，点击保存按钮。

## 申请权限

应用在使用Weather Service Kit能力前，需在应用的module.json5配置文件中声明所需权限。涉及的权限包括：

* ohos.permission.INTERNET：用于请求对应天气相关数据。

```
1. {
2. "module": {
3. // ...
4. "requestPermissions": [
5. {
6. "name": "ohos.permission.INTERNET",
7. // ...
8. }
9. // ...
10. ]
11. }
12. }
```

## 配置Profile文件

在接口调用过程中，天气服务会对您的Profile文件进行鉴权。因此，您需要在开通天气服务后，按照[配置签名信息](application-dev-overview.md#配置签名信息)的流程，申请并配置签名信息。

## （可选）申请位置权限

获取用户当前位置的天气数据，需要调用Location Kit（位置服务）获取当前位置经纬度信息，使用前参考[申请权限](../harmonyos-references/js-apis-geolocationmanager.md#申请权限)。
