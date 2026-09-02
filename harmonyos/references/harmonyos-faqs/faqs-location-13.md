---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-13
title: 地理围栏功能的使用方式及常见问题解答
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 地理围栏功能的使用方式及常见问题解答
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:fa432e511d9f0354247cc5445e1300ca229d1b8e35e012cca0208d4dd2a0134a
---

## 问题现象

关于HarmonyOS系统地理围栏功能相关问题：

1. 什么是地理围栏，端侧围栏和云侧围栏的区别是什么？
2. 如何使用地理围栏功能，实现用户位置到达某个范围时触发相关操作？
3. 使用地理围栏功能时，是否要求应用必须处于在线状态或后台运行？
4. 该功能的使用是否涉及收费项目？
5. 地理围栏功能支持海外吗？
6. 地理围栏的ID如何维护管理？
7. 使用geoLocationManager.on('gnssFenceStatusChange')地理围栏监听，如何识别是进入围栏还是退出围栏？
8. 按照开发文档要求，给locationkit@huawei.com发送邮件申请开通云端地理围栏服务，但一直未得到反馈，如何处理？

## 解决方案

1. [地理围栏说明可参考官网简介](../harmonyos-guides/geofence-intro.md)。

   ***端侧围栏：***

   仅支持构建圆形围栏，并且依赖GNSS芯片的地理围栏功能，仅在室外开阔区域才能准确识别用户进出围栏事件。

   应用场景举例：开发者可以使用地理围栏技术，在企业周围创建一个区域围栏，当用户进入这个区域，在移动设备上进行有针对性的提醒。端侧围栏比较适合于开发者要使用自己的个性化围栏场景。

   ***云侧围栏：***

   云端围栏是指开发者直接使用云侧公共围栏，当用户进入这个区域，在移动设备上进行有针对性的提醒。

   应用场景举例：云侧围栏当前无法直接在AGC平台开通，需要通过邮件申请开通。云端围栏在云侧注册围栏，围栏数据是公共围栏，比如商圈、景点等，云侧围栏比较适合于开发者要使用公共围栏的场景。
2. 具体开发指南如下：
   * 端侧围栏：[端侧GNSS围栏开发指导](../harmonyos-guides/geofence-guidelines.md)。GNSS地理围栏功能依赖GNSS定位芯片（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。APP可以在入参[GnssGeofenceRequest](../harmonyos-references/js-apis-geolocationmanager.md#gnssgeofencerequest12)中传入回调函数用于接收地理围栏事件；也可以传入通知对象[NotificationRequest](../harmonyos-references/js-apis-notification.md#notificationrequest)，在系统识别到地理围栏事件发生时会弹出APP创建的通知，用户可通过点击通知的方式拉起应用。示例代码参考官网API[添加一个GNSS地理围栏](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageraddgnssgeofence12)。
   * 云侧围栏：[云端围栏开发指导](../harmonyos-guides/fenceextensionability.md)。
   * 地理围栏所使用的接口详细说明参见：[Location Kit](../harmonyos-references/js-apis-geolocationmanager.md)。

3. 应用运行状态要求：

   在HarmonyOS系统中使用地理围栏功能，并不强制要求应用处于前台运行。当应用完成地理围栏区域划定及监听事件配置后，即便应用切换至后台运行（甚至应用不在线状态），地理围栏功能仍可持续生效。系统将基于定位服务持续监测设备位置，依据预设规则触发对应事件。
4. 费用相关说明：

   HarmonyOS系统的地理围栏功能属于系统标准位置服务功能，集成于系统开放的API中。正常使用该功能不会产生额外费用，开发者可基于系统提供的开发能力，在合规范围内进行功能开发与应用部署。
5. 支持范围说明：

   地理围栏所使用的接口[Location Kit](../harmonyos-references/js-apis-geolocationmanager.md)中有说明该模块能力仅支持WGS-84坐标系，WGS-84是一个全球通用的国际标准大地坐标系，用于GPS全球定位系统，也是国际上最为广泛使用的真实原始坐标系，因此它也用于表示全球各地的地理位置，包括海外地区。
6. 地理围栏的ID如何维护管理？
   * 地理围栏的ID由系统服务统一进行管理，创建围栏的应用不对围栏ID进行管理。当系统首次创建围栏的时候ID会从1开始计数，ID具有全局唯一性。
   * 当发生手机重启、位置服务重启的情形下，围栏会被清除，ID发生重置。

7. [geoLocationManager.on('gnssFenceStatusChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerongnssfencestatuschange)创建的地理围栏，触发围栏进出事件时会调用对应的getWantAgent()拉起Ability，可以在Ability页面的onCreate()中，通过want.parameters?.["transition"]返回的值来判断[围栏事件类型](../harmonyos-references/js-apis-geolocationmanager.md#geofencetransitionevent12)。
8. 可以直接使用端侧地理围栏，无需额外申请权限。对于历史文化景点等位置固定且介绍内容可预先内置的场景，不需要云端动态下发。用户到达景点时，系统直接弹出包含历史文化介绍的通知即可完成信息展示，整个流程不需要网络请求和云端参与。端侧GNSS围栏开发指导请参考[端侧GNSS围栏开发指导](../harmonyos-guides/geofence-guidelines.md)。
