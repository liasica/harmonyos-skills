---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-listener-connect-status
title: 监听HiCar的连接状态
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 获取HiCar连接状态 > 监听HiCar的连接状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb11a8601804d5deef19bca409669f7b277a5e589fffbd803fc32b99e7ae721c
---

## 场景介绍

生态应用可以通过监听智慧出行连接状态接口获取连接信息，适配HiCar业务（如：应用流转）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/LgUOePiTSbSFskWCtsllgw/zh-cn_image_0000002583478471.png?HW-CC-KV=V1&HW-CC-Date=20260427T234436Z&HW-CC-Expire=86400&HW-CC-Sign=AA1A553CEC2F0BD2C8A01079D22D515F471FC0600204402CCC8D4BEBCC88D035)

## 接口说明

监听HiCar的连接状态使用接口如下：

| 接口名 | 描述 |
| --- | --- |
| [on('smartMobilityStatus')](../harmonyos-references/car-smartmobilitycommon.md#onsmartmobilitystatus) | 注册智慧出行连接状态的监听。 |
| [off('smartMobilityStatus')](../harmonyos-references/car-smartmobilitycommon.md#offsmartmobilitystatus) | 取消注册智慧出行连接状态的监听。 |

## 开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/wEDM3KdUQVCcq_WsRPdN1Q/zh-cn_image_0000002552798822.png?HW-CC-KV=V1&HW-CC-Date=20260427T234436Z&HW-CC-Expire=86400&HW-CC-Sign=AB2F7EA555756CC38724CA227E0E004888AC9EBBB3F2500A3FDCE390AEC5B316)

## 开发步骤

1. 导入相关模块。

   ```
   1. import { smartMobilityCommon } from '@kit.CarKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 监听HiCar连接状态。

   应用在适配HiCar时，需要注册智慧出行连接状态的监听，用于对应的业务逻辑处理。

   ```
   1. try {
   2. // 获取SmartMobilityAwareness实例
   3. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();

   5. // 业务类型
   6. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];

   8. // 智慧出行连接状态回调函数
   9. const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
   10. hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
   11. if (info.status === smartMobilityCommon.SmartMobilityStatus.RUNNING) {
   12. // 连接成功通知
   13. } else if (info.status === smartMobilityCommon.SmartMobilityStatus.IDLE) {
   14. // 断开连接通知
   15. }
   16. };

   18. // 注册智慧出行连接状态的监听
   19. awareness.on('smartMobilityStatus', types, callBack);
   20. } catch (e) {
   21. // 捕获接口调用异常时的错误码并做相应处理
   22. hilog.error(0x0000, 'testTag', `on smart mobility status listener error, error code: ${e?.code}`);
   23. }
   ```
3. 取消监听。

   在应用退出时，需要取消之前注册的监听，减少系统不必要的资源消耗。

   ```
   1. try {
   2. // 获取SmartMobilityAwareness实例
   3. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
   4. // 业务类型
   5. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];
   6. // 取消注册智慧出行连接状态的监听
   7. awareness.off('smartMobilityStatus', types);
   8. } catch (e) {
   9. // 捕获接口调用异常时的错误码并做相应处理
   10. hilog.error(0x0000, 'testTag', `off smart mobility status listener error, error code: ${e?.code}`);
   11. }
   ```
