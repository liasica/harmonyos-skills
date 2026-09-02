---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-52
title: Map Kit使用报错1002600003如何解决
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit使用报错1002600003如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:7848c16fc084f6372ab798cc8b9a0489f9f855b1e57dbf871c65693722b4208c
---

## 问题现象

使用地图显示、地点搜索、逆地理编码、路径规划、地图选点等功能时，报错1002600003："App authentication failed."，如何解决？

## 背景知识

Map Kit地图服务提供以下能力：

* map 地图显示：创建地图组件、设置地图属性、自定义地图等。
* site 位置搜索：POI搜索、正地理编码、逆地理编码。
* navi 路径规划：出行路径规划、批量算路、轨迹绑路。
* staticMap 静态图：获取指定位置地图图片。
* sceneMap 地图Picker（场景化控件）：地点详情展示、地点选取、区划选择。

使用以上相关地图服务能力，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。

## 解决方案

1002600003错误码表示应用身份校验失败。

常见原因：

1. 未开通地图服务。

   使用@kit.MapKit的[map（地图显示功能）](../harmonyos-references/map-map.md)、[navi（路径规划）](../harmonyos-references/map-navi-api.md)、[sceneMap（场景化控件）](../harmonyos-references/map-scenemap.md)、[site（地点搜索）](../harmonyos-references/map-site.md)、[staticMap（静态图）](../harmonyos-references/map-staticmap.md)能力，均需要应用开通地图服务，参见[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)章节，通过DevEco Studio或AppGallery Connect网站开通地图服务，并进行签名。
2. 在AppGallery Connect网站开通地图服务后，未重新生成Profile文件进行重新签名。

   在AppGallery Connect网站重新生成[调试Profile](../app/agc-help-debug-profile-0000002248181278.md)或[发布Profile](../app/agc-help-release-profile-0000002248341090.md)文件，重新[配置签名](../harmonyos-guides/ide-signing.md#section1240072619462)。
3. 如果使用HarmonyOS 5.0.2(14)及以前版本，请检查client\_id或公钥指纹配置不正确。

   参见[1002600003 应用身份校验失败](../harmonyos-references/errorcode-map.md#section1002600003-应用身份校验失败)指导中处理步骤1-4解决。
4. 工程级build-profile.json5文件中signingConfigs的name与products中signingConfig不匹配，导致签名无效。

   在DevEco Studio中打开工程级[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md#section45865492619)文件，将products中signingConfig的值修改为与signingConfigs中name保持一致。
