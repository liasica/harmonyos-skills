---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-16
title: 地图服务使用报错
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 地图服务使用报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:ac91578ade70b9d6f07d635b770d626e57ffac455145c7bca8030baad08444db
---

## 问题现象

1. 调用地图组件时，使用报错，地图无法显示。
2. 在使用site地点搜索API时，没有返回结果且日志中也没有错误信息。

## 背景知识

Map Kit（地图服务）为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化显示地图、位置搜索和路径规划等功能，轻松完成地图构建工作。您可以轻松地在HarmonyOS应用中集成地图相关的功能，全方位提升用户体验。

开发准备可参考[地图开发准备](../harmonyos-guides/map-config-agc.md)。

## 问题定位

1. 检查设备网络状态。
2. 检查是否在AppGallery Connect上提前开通了地图服务，并确保在申请Profile文件之前已开启地图服务。开通地图服务后最多需要等待24小时才能生效，可通过临时调整系统时间进行验证。
3. 确认应用是否在真实设备上运行。
4. 是否未更新手动签名中的证书。
5. 是否开启了"useNormalizedOHMUrl": true配置。
6. 是否开启获取定位权限：ohos.permission.LOCATION，ohos.permission.APPROXIMATELY\_LOCATION。
7. 参考[1002600003](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)完成应用身份校验。

## 分析结论

1. 地图白屏不显示，是因为缺少权限。使用地图服务需要在AGC后台配置地图服务，且需要手动签名。

   参考链接：a. [开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。b. [手动配置签名信息](../harmonyos-guides/ide-signing.md#section297715173233)。
2. 使用site地点搜索服务，此服务使用时也需要开通地图服务，并进行手动签名。步骤可参考分析结论1。

## 修改建议

1. 在AGC后台[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
2. [手动配置签名信息](../harmonyos-guides/ide-signing.md#section297715173233)。
3. [配置clientID](../harmonyos-guides/health-configuration-client-id.md)。

## 常见FAQ

Q：debug版本及正式上架版本运行正常，但打包release版本在云真机测试时静态地图报错：1002600003应用身份校验失败。

A：直接打包release版本安装到云真机无法通过验证，需要正式上架、邀请测试或公开测试才可以。

Q：Map Kit是否支持设置地图语言？

A：Map Kit当前不支持手动设置地图语言，Map Kit地图的语言是跟随系统语言设置的。

Q：已开通地图服务并手动签名，为什么地图加载仍显示白屏？

A：白屏是因为初始化地图失败，原因是自定义函数在MapController实例化前调用了MapController，导致访问了空实例。需要确保在MapController访问时，已完成MapController实例化。

Q：放大缩小和我的位置组件是否支持自定义位置？

A：当前放大缩小和我的位置组件不支持自定义位置。

Q：Map Kit是否支持OpenHarmony？

A：Map Kit当前不支持OpenHarmony。
