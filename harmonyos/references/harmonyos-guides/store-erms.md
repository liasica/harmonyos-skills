---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-erms
title: 生态查询服务
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 生态查询服务
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e451719b7798340ba132a55464828a7e92679a2586d45b43379876b462a0d2dc
---

## 场景介绍

生态查询服务可以为您提供应用/元服务运行信息的查询，当前提供场景值查询和广告验签信息查询。场景值是用来描述用户进入应用和元服务的路径。您可以通过本服务，来查询您的元服务/应用是通过何种场景被打开的（[场景值列表](appgallery-scene-list.md#场景值列表)）。当前我们支持元服务的场景值查询，后续我们会继续公布应用场景值的查询。广告验签版本查询只在您的应用涉及广告场景下才会被使用到。您可以通过本查询服务，查询广告验签参数处理逻辑。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/CF0O_9E6SmCU7kV6cKd86g/zh-cn_image_0000002589245085.png?HW-CC-KV=V1&HW-CC-Date=20260429T053710Z&HW-CC-Expire=86400&HW-CC-Sign=1F3690A596D463DAB1405673DD13D3A623BD67133C097922D4ED0E6B76D2935E)

1. 用户需要查询应用/元服务自身场景值或者查询广告验签版本。
2. 应用调用[getSelfSceneCode](../harmonyos-references/store-scenemanager.md#scenemanagergetselfscenecode)接口和[getAdsVerificationVersion](../harmonyos-references/store-scenemanager.md#scenemanagergetadsverificationversion)接口分别获取自身场景值和广告验签版本。
3. 返回自身场景值和广告验签版本给应用/元服务。
4. 返回结果给用户。

## 约束与限制

* 生态查询服务支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。
* 如果应用或者元服务没有产生场景值，调用[getSelfSceneCode](../harmonyos-references/store-scenemanager.md#scenemanagergetselfscenecode)接口返回的场景值为空。
* 生态查询服务不支持模拟器，请使用真机调试。

## 接口说明

生态查询服务场景提供以下接口，具体API说明详见[接口文档](../harmonyos-references/store-scenemanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSelfSceneCode](../harmonyos-references/store-scenemanager.md#scenemanagergetselfscenecode)():string | 获取自身场景值。 |
| [getAdsVerificationVersion](../harmonyos-references/store-scenemanager.md#scenemanagergetadsverificationversion)(): number | 查询广告验签版本。 |

## 开发步骤

### 查询自身场景值

1. 导入模块。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { sceneManager } from '@kit.AppGalleryKit';
   ```
2. 调用[getSelfSceneCode](../harmonyos-references/store-scenemanager.md#scenemanagergetselfscenecode)方法。

   ```
   1. try {
   2. const sceneCode: string = sceneManager.getSelfSceneCode();
   3. hilog.info(0, 'TAG', "Succeeded in getting SelfSceneCode res = " + sceneCode);
   4. } catch (error) {
   5. hilog.error(0, 'TAG', `getSelfSceneCode failed. code is ${error.code}, message is ${error.message}`);
   6. }
   ```

### 查询广告验签版本

1. 导入模块。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { sceneManager } from '@kit.AppGalleryKit';
   ```
2. 调用[getAdsVerificationVersion](../harmonyos-references/store-scenemanager.md#scenemanagergetadsverificationversion)方法。

   ```
   1. try {
   2. const version: number = sceneManager.getAdsVerificationVersion();
   3. hilog.info(0, 'TAG', "Succeeded in getting AdsVerificationVersion res = " + version);
   4. } catch (error) {
   5. hilog.error(0, 'TAG', `getAdsVerificationVersion failed. code is ${error.code}, message is ${error.message}`);
   6. }
   ```
