---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-recommendcallback
title: 多网建议监听
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 多网建议监听
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0da055f06111bf0fee5848bd5e990bc2a28e59fba6940d6ae802f7686cdc529b
---

## 场景介绍

系统感知到应用可能需要使用多网络加速的场景时，如弱网、网络切换等特定场景，会给出建议。应用通过监听多网络加速的建议，决策发起多网络加速的请求。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-nethandover.md#nethandoveronmultipathrecommendation)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'multiPathRecommendation', callback: Callback<MultiPathRecommendationInfo>): void | 订阅多网建议信息变化。 |
| off(type: 'multiPathRecommendation', callback?: Callback<MultiPathRecommendationInfo>): void | 取消订阅多网建议信息变化。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. import { netHandover } from '@kit.NetworkBoostKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过订阅的方式监听系统多网建议变化信息。

   ```
   1. try {
   2. netHandover.on('multiPathRecommendation', (data: netHandover.MultiPathRecommendationInfo) => {
   3. // 回调信息处理
   4. console.info("on multiPathRecommendation: " + JSON.stringify(data));
   5. });
   6. } catch (err) {
   7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   8. }
   ```
3. 当应用业务流程结束，取消订阅系统多网建议变化信息。

   ```
   1. try {
   2. netHandover.off('multiPathRecommendation');
   3. } catch (err) {
   4. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   5. }
   ```
