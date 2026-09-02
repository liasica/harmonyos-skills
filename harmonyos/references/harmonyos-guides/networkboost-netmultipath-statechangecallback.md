---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-statechangecallback
title: 多网状态监听
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 多网状态监听
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7061704fc9fe445c28b8d5a2daf818b1b5910e1e042651be78940c7e6940e7b1
---

## 场景介绍

应用通过监听多网络状态的变化，感知可用网络的变化，从而选择在多网络上传输数据的策略。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-nethandover.md#nethandoveronmultipathstatechange)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'multiPathStateChange', callback: Callback<MultiPathStateInfo>): void | 订阅多网状态信息变化。 |
| off(type: 'multiPathStateChange', callback?: Callback<MultiPathStateInfo>): void | 取消订阅多网状态信息变化。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```typescript
   import { netHandover } from '@kit.NetworkBoostKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过订阅的方式监听多网状态变化信息。

   ```typescript
   try {
     netHandover.on('multiPathStateChange', (data: netHandover.MultiPathStateInfo) => {
       // 回调信息处理
       console.info('on multiPathStateChange multiPathState:', data.multiPathState);
       console.info('on multiPathStateChange cause:', data.cause);
       console.info('on multiPathStateChange netHandle:', data.netHandle.netId);
       console.info('on multiPathStateChange pathState:', data.pathState);
       console.info('on multiPathStateChange pathType:', data.pathType);
     });
   } catch (err) {
     console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   }
   ```
3. 当应用业务流程结束和应用退出时，取消订阅多网状态变化信息。

   ```typescript
   try {
     netHandover.off('multiPathStateChange');
   } catch (err) {
     console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   }
   ```
