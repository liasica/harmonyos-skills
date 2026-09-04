---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/metadatabinding-guidelines
title: 记忆链接开发指导
breadcrumb: 指南 > 系统 > 硬件 > Multimodal Awareness Kit（多模态融合感知服务） > 记忆链接开发指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:35+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:39f79135f9c2eb1b4a45cde9acf0edfab865188cf043a9934fcefc027945dee9
---

## 概述

MetadataBinding（记忆链接）指由第三方应用提供[鸿蒙App Linking链接](applinking-introduction.md)，系统将当前用户浏览的内容与鸿蒙App Linking链接进行关联并保存的功能。

详细的接口介绍请参考[@ohos.multimodalAwareness.metadataBinding (记忆链接)](../harmonyos-references/js-apis-awareness-metadatabinding.md)。

## 场景介绍

第三方应用可使用记忆链接功能，将鸿蒙App Linking链接映射到调用接口的系统应用或服务。例如，用户在【电商应用】中浏览某个商品时，截图保存了该商品的图片，系统将记录图片与【电商应用】提供的鸿蒙App Linking链接的映射关系。当用户再次浏览该图片时，用户主动触发小艺识屏能力，系统会提醒用户是否需要返回【电商应用】查看商品详情，提醒样式由小艺配置。

## 演示示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/f_2AL6S1SqmAFTPlcSYRtw/zh-cn_image_0000002742123557.gif)

## 接口说明

* 本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块支持记忆链接的功能。

| 接口名 | 描述 |
| --- | --- |
| [submitMetadata](../harmonyos-references/js-apis-awareness-metadatabinding.md#metadatabindingsubmitmetadata)(metadata: string): void; | 第三方应用将待编码的鸿蒙App Linking链接传递给多模态融合感知服务，该服务决定适当时机将内容传递给调用编码接口的系统应用。 |
| [on](../harmonyos-references/js-apis-awareness-metadatabinding.md#metadatabindingonoperationsubmitmetadata)(type: 'operationSubmitMetadata', bundleName: string, callback: Callback<number>): void; | 订阅系统事件以获取编码内容，应用注册回调，事件发生时回传编码内容。 |
| [off](../harmonyos-references/js-apis-awareness-metadatabinding.md#metadatabindingoffoperationsubmitmetadata)(type: 'operationSubmitMetadata', bundleName: string, callback?: Callback<number>): void; | 取消订阅系统获取编码内容的事件。取消注册回调接口。 |

## 约束与限制

* 鸿蒙App Linking链接超过128字节时会编码失败，截图保存原始图像

## 开发步骤

1. 导入模块。

   ```typescript
   import { metadataBinding } from '@kit.MultimodalAwarenessKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { Callback } from '@kit.BasicServicesKit';
   ```
2. 定义记忆服务回调及包名，函数接收回传编码的内容。

   ```typescript
   let callback : Callback<number> = (event: number) => {};
   let bundleName: string = 'com.example.app';
   ```
3. 订阅记忆服务。

   ```typescript
   try {
     metadataBinding.on('operationSubmitMetadata', bundleName, callback);
     console.info('on succeeded');
     // ...
   } catch (err) {
     let error = err as BusinessError;
     console.error('Register event error and err code is ' + error.code);
     // ...
   }
   ```
4. 提供鸿蒙App Linking链接。

   ```typescript
   let metadata: string = 'sample metadata';
   try {
     metadataBinding.submitMetadata(metadata);
     // ...
   } catch (err) {
     let error = err as BusinessError;
     console.error('Submit metadata error and err code is ' + error.code);
     // ...
   }
   ```
5. 取消订阅记忆服务。

   ```typescript
   try {
     metadataBinding.off('operationSubmitMetadata', bundleName, callback);
     console.info('off succeeded');
     // ...
   } catch (err) {
     let error = err as BusinessError;
     console.error('Unregister event error and err code is ' + error.code);
     // ...
   }
   ```
