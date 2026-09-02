---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-scenecallback
title: 网络场景识别
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 网络质量 > 网络场景识别
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cbd9eb7094ab4128576e25868efc7d14e41ffa094fcf793c209620507e384420
---

## 场景介绍

应用在订阅网络场景识别后，系统在网络场景实时信息或预测信息发生变化后回调给应用，回调的网络场景信息包括数据传输的链路类型、网络场景类型、数传策略建议、弱信号信息等。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-netquality.md#netqualityonnetscenechange)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'netSceneChange', callback: Callback<Array<NetworkScene>>): void | 订阅网络场景信息状态变化。 |
| off(type: 'netSceneChange', callback?: Callback<Array<NetworkScene>>): void | 取消订阅网络场景信息状态变化。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```typescript
   import { netQuality } from '@kit.NetworkBoostKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过订阅的方式监听网络场景识别信息。

   ```typescript
   try {
     netQuality.on('netSceneChange', (list: Array<netQuality.NetworkScene>) => {
       if (list.length > 0) {
         list.forEach((sceneInfo) => {
           // 网络场景识别回调信息处理
           console.info('Scene type:', sceneInfo.scene);
           console.info('PathType:', sceneInfo.pathType);
           console.info('RecommendedAction:', sceneInfo.recommendedAction);
           if (sceneInfo.scene == 'congestion') {
             // 网络拥塞分支处理
           }
           if (sceneInfo.weakSignalPrediction) {
             // 存在弱信号预测信息，对弱信号预测信息进行处理
           }
         });
       }
     });
   } catch (err) {
     console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   }
   ```
3. 当应用业务流程结束，取消订阅监听网络场景识别信息。

   ```typescript
   try {
     netQuality.off('netSceneChange');
   } catch (err) {
     console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   }
   ```
