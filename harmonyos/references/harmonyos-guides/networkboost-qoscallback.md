---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-qoscallback
title: 网络质量评估
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 网络质量 > 网络质量评估
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa16fa80f9beca6c2b3d50b0ce4610d1a984c9723807523a7ea8b66ca2abb316
---

## 场景介绍

应用在订阅网络质量Qos（Quality of Service）评估后，系统按照一定的周期或Qos变化后回调给应用。回调的Qos信息包括数据传输的链路类型、上下行空口实时带宽、上下行空口实时速率、RTT时延等。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/networkboost-netquality.md#netqualityon-netqoschange)。

| 接口名 | 描述 |
| --- | --- |
| on(type: 'netQosChange', callback: Callback<Array<NetworkQos>>): void | 订阅Qos信息状态变化。 |
| off(type: 'netQosChange', callback?: Callback<Array<NetworkQos>>): void | 取消订阅Qos信息状态变化。 |

## 开发步骤

1. 导入Network Boost Kit模块。

   ```
   1. import { netQuality } from '@kit.NetworkBoostKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过订阅的方式监听网络质量评估信息。

   ```
   1. try {
   2. netQuality.on('netQosChange', (list: Array<netQuality.NetworkQos>) => {
   3. if (list.length > 0) {
   4. list.forEach((qos) => {
   5. // 回调信息处理
   6. console.info(`数据链路类型: ${JSON.stringify(qos.pathType )}.` );
   7. console.info(`该数据链路类型的上行带宽: ${JSON.stringify(qos.linkUpBandwidth)}.` );
   8. console.info(`该数据链路类型的下行带宽: ${JSON.stringify(qos.linkDownBandwidth)}.` );
   9. // 单位为bps，若需转化为B/s，数值需要除以8
   10. console.info(`该数据链路类型的上行速率: ${JSON.stringify(qos.linkUpRate)}.` );
   11. // 单位为bps，若需转化为B/s，数值需要除以8
   12. console.info(`该数据链路类型的下行速率: ${JSON.stringify(qos.linkDownRate)}.` );
   13. // 实时速率为上行速率和下行速率之和
   14. console.info(`该数据链路类型的实时速率(B/s): ${JSON.stringify((qos.linkUpRate+ qos.linkDownRate) / 8)}.`);
   15. console.info(`该数据链路类型的RTT时延: ${JSON.stringify(qos.rttMs)}.` );
   16. console.info(`该数据链路类型的上行发送空口缓冲时延: ${JSON.stringify(qos.linkUpBufferDelayMs )}.`);
   17. });
   18. }
   19. });
   20. } catch (err) {
   21. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   22. }
   ```
3. 当应用业务流程结束，去订阅的方式取消监听网络质量评估信息。

   ```
   1. try {
   2. netQuality.off('netQosChange');
   3. } catch (err) {
   4. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
   5. }
   ```
