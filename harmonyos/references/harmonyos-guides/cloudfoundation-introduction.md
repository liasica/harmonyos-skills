---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-introduction
title: Cloud Foundation Kit简介
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1ff5f82ad7dff186cd39f6bf986729b701fb886617563d7db430d28c574d13fb
---

Cloud Foundation Kit（云开发服务）可以按需为应用提供云函数、云数据库、云存储、预加载等云端服务。应用运行所需的服务器和环境均可由云端平台提供，开发者只需关注应用的业务逻辑，而无需关心基础设施（例如：服务器、操作系统、容器等）。

DevEco Studio中还提供了[端云一体化开发](agc-harmonyos-clouddev-overview.md)的开发体验，开发者可以基于统一的技术栈，高效、协同地完成端、云代码的编写、调试、编译和部署，极大提高构建HarmonyOS应用和元服务的效率。

## 优势

* 低运维成本

  开发者无需构建和管理云端资源，Cloud Foundation Kit提供了包括函数计算、数据库、存储、预加载等一系列能力。
* 弹性伸缩、按量计费

  面对波峰波谷的业务场景，Cloud Foundation Kit可根据实际请求量弹性伸缩、按量计费，开发者无需为空闲资源买单，有效提升资源利用率，降低资源成本。
* 安全可靠

  支持数据全密态加密，支持APP、用户和服务三重认证，提供基于角色的权限管理机制，全方位保障开发者和用户的数据安全。
* 端云一体化开发

  在DevEco Studio中提供了端云一体化开发体验，支持开发者基于统一的技术栈进行端、云代码协同开发，前端开发人员轻松转换为全栈工程师，极大提高构建HarmonyOS应用和元服务的效率、降低开发成本。

## 典型场景

### 应用/元服务后端构建

便捷操作云函数、云数据库、云存储、预加载服务，简化应用/元服务开发与运维相关的事务，快速构建应用/元服务的后端服务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/XaQkfs88Tz6V-ab5ZDUnzA/zh-cn_image_0000002552799188.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234835Z&HW-CC-Expire=86400&HW-CC-Sign=EDCB01A96142428B1DA5D58720508C50EB9C6485F781AFB94CA6796347FC937E)

### 计算密集型任务

当应用中出现计算密集型任务时，可在任务启动时自动分配足够的算力来支撑任务的执行，并在任务结束时自动释放资源，避免浪费。

开发者可以为云函数配置定时触发器，定时执行任务，也可以通过其他服务主动调用云函数来执行任务。

例如，通过Cloud Foundation Kit实现对数据的渲染、叠加等处理：

* 对原始数据进行封装，例如对报表数据的处理。
* 对数据的同步，例如数据的抽取、转化或者加载。
* 对视频或者图像的处理，例如生成不同分辨率的视频或者图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/aBmhmG4eRjKTXDoUHBHIFw/zh-cn_image_0000002583438883.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234835Z&HW-CC-Expire=86400&HW-CC-Sign=95C8D8544A1748CFAF221F972FDDD738FA9E3DEE98EB03E33AD529E235E0F582)

### 协议适配和转换场景

可用于协议适配和转换，以及第三方平台场景的对接，轻量灵活、快速部署，让开发者的业务快人一步。

例如：可以将数据存储、身份验证、消息队列、推送通知、定时任务等功能切片通过云服务实现胶水层的链接、转换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/rzgxvZPlQMKQ27dkrpuXbg/zh-cn_image_0000002552958838.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234835Z&HW-CC-Expire=86400&HW-CC-Sign=C6EA93819BCBF42422EA6117E832D201AD92152C2D719C79F48385230AD6D8DB)

### 浪涌式访问场景

传统架构服务在某些特殊场景下，可能出现大量的访问。为保证业务高峰时，系统能稳定运行，一般需要购买高性能、昂贵的服务器，组建集群负载均衡。但是，当业务回落时，就导致了大量服务器的资源浪费。

Cloud Foundation Kit能根据业务访问量快速自动扩容，规避业务高峰时系统异常的风险，度过业务流量高峰期，使应用从容应对诸如秒杀、节日活动等业务场景；并发量骤降时，弹性伸缩的特性亦支持自动缩容，释放闲置资源，避免浪费。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/feXoPXVnRAOiK8PunOijRQ/zh-cn_image_0000002583478839.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234835Z&HW-CC-Expire=86400&HW-CC-Sign=2E7D16FABFB26B207480DC2364CAC3007A71E81911F8A5D782C01BD8C1D812A7)

## 约束与限制

### 支持的设备

| 能力 | 设备 |
| --- | --- |
| 云函数 | Phone、Tablet、PC/2in1、Wearable、TV |
| 云数据库 | Phone、Tablet、PC/2in1、Wearable、TV |
| 云存储 | Phone、Tablet、PC/2in1、Wearable、TV |
| 预加载 | Phone、Tablet、PC/2in1 |

### 支持的国家/地区

请参见[支持的国家/地区](cloudfoundation-supported-regions.md)。

### 支持的签名方式

支持[关联注册应用进行自动签名](ide-signing.md#section20943184413328)（DevEco Studio 6.0.0 Beta5及以上版本）和[手动签名](ide-signing.md#section297715173233)两种方式。

## 模拟器支持情况

从6.0.0(20) Beta5版本开始，本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下：

* 通用差异：请参见[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)。
* 仅云函数、云数据库、云存储服务支持模拟器。关于如何使用模拟器调试，请参见[使用模拟器调试](cloudfoundation-emulator.md)。

## 计费说明

Cloud Foundation Kit包含云函数、云数据库、云存储、预加载服务，预加载服务支持通过云函数来实现资源加载，云函数、云数据库、云存储服务提供了免费额度以供试用，具体的配额明细请参考各服务的配额说明：

* [云函数计费说明](../AppGallery-connect-Guides/agc-cloud-function-price-0000001211271102.md)
* [云数据库计费说明](../AppGallery-connect-Guides/agc-clouddb-price-0000001256815629.md)
* [云存储计费说明](../AppGallery-connect-Guides/agc-cloudstorage-price-0000001253665999.md)
