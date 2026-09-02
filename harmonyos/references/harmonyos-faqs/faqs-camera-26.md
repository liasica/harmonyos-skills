---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-26
title: 调用preconfig接口发生报错7400201
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 调用preconfig接口发生报错7400201
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cb95cce3a7d1aeaa80c3b8cc10afe4b346ccf5ee60277854d162dc6cddf33e48
---

## 问题现象

用户在使用应用内的相机进行业务操作时，打开相机界面后发现没有显示画面，并且收到了错误码7400201报错。

## 背景知识

* [7400201 相机服务异常](../harmonyos-references/errorcode-camera.md#section7400201-相机服务异常)：属于系统内部通用错误，可能原因有相机服务异常，比如相机服务重启、跨进程调用异常等。
* [使用相机预配置(ArkTS)](../harmonyos-guides/camera-preconfig.md)：相机预配置（[preconfig](../harmonyos-references/arkts-apis-camera-videosession.md#preconfig12)），对常用的场景和分辨率进行了预配置集成，可简化开发相机应用流程，提高应用的开发效率。

## 问题定位

1. 搜索日志中错误码7400201，查看是否有如下日志。

   ```txt
   07-01 22:31:45.915   11445-11445   C02B01/com....hm/CAMERA   com....hm       E     {IsPreconfigProfilesLegal():237} VideoSession::IsPreconfigProfilesLegal check video profile fail, no matched video profiles:1003 3840x2160
   07-01 22:31:45.915   11445-11445   C02B01/com....hm/CAMERA   com....hm       E     {Preconfig():295} VideoSession::Preconfig preconfigProfile is illegal.
   07-01 22:31:45.915   11445-11445   A03D00/com....hm/JSAPP    com....hm       E     initCamera fail: {"code":"7400201"}
   ```
2. 从上述日志可知preconfig接口抛出7400201错误码是因为指定的参数非法导致，于是检查相关代码逻辑，发现在调用preconfig接口前未曾调用[canPreconfig](../harmonyos-references/arkts-apis-camera-videosession.md#canpreconfig12)接口校验参数是否支持。

## 分析结论

本次7400201错误码是preconfig的相机预配置参数组合在当前设备当前模式下不支持导致的。

## 修改建议

调用canPreconfig检查对应的PreconfigType和PreconfigRatio的组合在当前设备上是否支持。确认支持后，再调用preconfig接口启用Preconfig配置。如果确认不支持该预配置参数组合，则需要给出相应的业务处理逻辑，防止报错。详情请参考[完整示例](../harmonyos-guides/camera-preconfig.md#完整示例)。
