---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-overview
title: 业务介绍
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 业务介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:58+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:148f890ff9c42be47facbf407d60aefb4634fbb9e81ba7b164b2ce1f6c366eed
---

## 什么是端云一体化开发

为丰富HarmonyOS对云端开发的支持、实现端云联动，DevEco Studio以[Cloud Foundation Kit（云开发服务）](cloudfoundation-introduction.md)为底座、在传统的“端开发”基础上新增“云开发”能力：开发者选择云开发工程模板，可创建一个同时包含端侧工程与云侧工程的端云一体化工程。之后，开发者在云侧工程对云函数或者云数据库等服务进行开发、调试和部署，而后在端侧工程通过Cloud Foundation Kit调用部署的云端服务。

DevEco Studio中提供的端云一体化开发体验，支持开发者基于统一的技术栈进行端、云代码协同开发，前端开发人员轻松转换为全栈工程师，极大提高了构建HarmonyOS应用和元服务的效率、降低开发成本。

## 什么是云开发工程模板

云开发工程模板是为端云一体化开发工程构建的场景化模板，提供了常见场景的代码实现。使用云开发工程模板，您可根据工程向导轻松创建端云一体化开发工程，工程将自动加载模板内预置的代码和资源文件。

DevEco Studio目前预置了通用云开发模板（[CloudDev]Empty Ability），该模板当前使用[Cloud Foundation Kit（云开发服务）](cloudfoundation-introduction.md)搭建了基础的演示项目，不含业务属性。您可参考模板学习如何进行基础的端云工程开发，后续开发时可删除预置的页面代码。

[点击此处](agc-harmonyos-clouddev-emptyability.md)了解通用云开发模板的更多信息。

## 端云一体化开发特性

端云一体化开发特性主要包含了如下功能。

| 主要功能 | 说明 |
| --- | --- |
| 端云一体化开发 | 您不仅可以在DevEco Studio中开发和调试应用端侧的业务代码，还可以开发和调试应用云侧的服务代码、并在开发完成后将云侧工程一键部署至AGC云端。 |
| Cloud Foundation Kit | 云侧工程接入Cloud Foundation Kit，按需为应用提供云函数、云数据库、云存储等云端服务，借助Cloud Foundation Kit开箱即用、一键部署、自动弹性伸缩、免运维等特点助力开发者降本增效。 |

## 端云一体化开发的优势

相比于传统开发模式，端云一体化开发模式具备成本低、效率高、门槛低等优势，具体区别见下表。

| 区别点 | 传统开发模式 | 端云一体化开发模式 |
| --- | --- | --- |
| 开发工具 | 端侧与云侧各需一套开发工具，云侧需自建服务器，工具成本高。 | DevEco Studio一套开发工具即可支撑端侧与云侧同时开发，无需搭建服务器，工具成本低。 |
| 开发人员 | * 端侧与云侧要求不同的开发语言，技能要求高。 * 需多人投入，且开发人员之间需持续、准确沟通，人力与沟通成本高、效率低。 | * 依托Cloud Foundation Kit开放的接口，端侧开发人员也能轻松开发云侧代码，大大降低开发门槛。 * 开发人员数量少，降低人力成本，提高沟通效率。 |
| 运维 | 需自行构建运营与运维能力，成本高、负担重。 | 直接接入Cloud Foundation Kit，具有开箱即用、一键部署、自动弹性伸缩、免运维等特点，开发者可聚焦业务逻辑本身，实现降本增效。 |

## 工作原理

DevEco Studio支持开发者在本地完成云侧服务资源的开发与部署，并可在端侧工程中调用您开发的云侧代码，真正实现端云一体化开发。

1. 选择云开发工程模板，根据工程向导[创建端云一体化开发工程](agc-harmonyos-clouddev-devproject.md)。
2. 分别为Cloud Foundation Kit提供的各个服务完成端云代码的开发、调试和部署。

   说明

   云侧与端侧工程的代码可并行开发，一般无先后顺序。但若需在端侧代码中调用云侧代码，云侧代码必须先部署到AGC云端，因此建议您先完成云侧代码的开发、调试与部署，再进行端侧代码开发与调试。

   1. 开发云侧工程：在云侧工程开发Cloud Foundation Kit提供的服务，目前包括云函数、云对象和云数据库。
      * [开发云函数](agc-harmonyos-clouddev-cloudfunctions.md)：在云侧工程下创建并配置函数、开发函数代码、调试函数、部署函数到AGC云端。
      * [开发云对象](agc-harmonyos-clouddev-cloudobj.md)：在云侧工程下创建云对象、开发云对象代码、调试云对象、部署云对象到AGC云端。
      * [开发云数据库](agc-harmonyos-clouddev-clouddb.md)：在云侧工程下创建对象类型、在对象类型中添加数据条目、部署云数据库到AGC云端。
   2. [部署云侧工程](agc-harmonyos-clouddev-deploy.md)：云侧工程代码开发调试完毕后，一键部署云侧工程到AGC云端。
   3. [开发端侧工程](agc-harmonyos-clouddev-appdevelop.md)：在端侧工程下通过Cloud Foundation Kit调用部署的云侧代码，包括调用云函数、调用云对象、访问云数据库、调用云存储。
3. 端云两侧工程代码全部开发完成后，将端云一体化工程打包成APP，提交至AGC申请上架。

## 约束与限制

### 支持的设备

仅支持手机。

### 支持的国家/地区

当前仅在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

### 支持的签名方式

支持[关联注册应用进行自动签名](ide-signing.md#section20943184413328)和[手动签名](ide-signing.md#section297715173233)两种方式。

### 模拟器支持情况

从6.0.0(20) Beta5版本开始支持模拟器开发，但与真机存在部分能力差异，详情请参见[模拟器与真机的差异](ide-emulator-specification.md)。

关于如何使用模拟器调试，请参见[使用模拟器调试](cloudfoundation-emulator.md)。

## 计费说明

使用端云一体化开发服务时，会开通并使用云函数、云数据库、云存储服务。华为为每个服务都提供了免费额度以供试用，具体的配额明细可以参考各服务的配额说明：

* [云函数](../AppGallery-connect-Guides/agc-cloud-function-price-0000001211271102.md)
* [云数据库](../AppGallery-connect-Guides/agc-clouddb-price-0000001256815629.md)
* [云存储](../AppGallery-connect-Guides/agc-cloudstorage-price-0000001253665999.md)
