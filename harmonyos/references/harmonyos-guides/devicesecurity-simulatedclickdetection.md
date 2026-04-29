---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-simulatedclickdetection
title: 模拟点击检测
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 业务风险检测 > 模拟点击检测
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a7d66a356b143f382c72ea595a4982750c1b309a9071bf21d97969266f738622
---

## 场景介绍

从6.0.0(20) 版本开始，新增支持模拟点击检测。

应用通过调用Device Security Kit的detectSimulatedClickRisk接口，获取模拟点击检测结果，用于自动化点击、设备墙等作弊行为检测。

应用可以根据检测结果评估如何进行业务操作。

## 约束与限制

每30秒最多可以调用10次，每个应用在每个设备上每天最多可以调用20次。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/8BMpAeW4QI2-IZncJJ1CKg/zh-cn_image_0000002558764900.png?HW-CC-KV=V1&HW-CC-Date=20260429T053139Z&HW-CC-Expire=86400&HW-CC-Sign=43BC18F16FA4E048F962A4EFCDB8C66702C04BEED15CB93D7635FE5AB0B30698)

**流程说明：**

1. 开发者应用调用detectSimulatedClickRisk接口，发起模拟点击检测请求。

   Device Security Kit收到请求后，首先采集当前设备模拟点击线索数据，然后将线索数据发送到Device Security服务器做检测，最后通过detectSimulatedClickRisk接口的返回值将检测结果传递给开发者应用。
2. 获取检测结果，并根据结果做出相应处理。

## 接口说明

以下是模拟点击检测相关接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-brid-api.md)。

| 接口名 | 描述 |
| --- | --- |
| detectSimulatedClickRisk(params: SimulatedClickDetectionRequest): Promise<string> | 模拟点击检测。 |

## 开发步骤

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用detectSimulatedClickRisk接口获取模拟点击检测结果。

   ```
   1. const TAG = "BusinessRiskIntelligentDetectionJsTest";

   3. let params = {
   4. version: 1
   5. } as businessRiskIntelligentDetection.SimulatedClickDetectionRequest;
   6. try {
   7. hilog.info(0x0000, TAG, 'Detect simulated click risk begin.');
   8. businessRiskIntelligentDetection.detectSimulatedClickRisk(params).then((result: string) => {
   9. hilog.info(0x0000, TAG, 'Detect simulated click risk success: %{public}s', result);
   10. }).catch((error: Error) => {
   11. let e: BusinessError = error as BusinessError;
   12. hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
   13. });
   14. } catch (error) {
   15. let e: BusinessError = error as BusinessError;
   16. hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
   17. }
   ```
3. 开发者应用可以根据模拟点击检测结果进行业务处理。

   模拟点击检测结果是一个格式为JSON格式的字符串，内容示例如下

   ```
   1. {
   2. "timestampMs": 9860437986543,
   3. "version": 1,
   4. "riskDecision": "fake",
   5. "tags": ["AbnormalTap"]
   6. }
   ```

   说明

   * timestampMs：发起请求时生成的时间戳。
   * riskDecision：风险检测结果。
   * version：检测结果消息格式的版本。默认值为1，当前只支持1。
   * tags：模拟点击关键特征。如果tags列表为空，表示未发现关键特征。如果tags列表不为空，表示发现关键特征。

   | tags值 | 含义 |
   | --- | --- |
   | AbnormalDeviceIntegrity | 设备完整性遭到破坏。 |
   | AbnormalDeviceBehavior | 设备行为异常，例如，设备连接状态、传感器状态等行为异常。 |
   | AbnormalTap | 存在异常点击行为，例如，点击事件注入，自动化点击等。 |

   | riskDecision值 | 含义 |
   | --- | --- |
   | fake | 当前设备存在作弊风险行为。存在自动化操控行为或设备墙作弊行为，详情见tags。 |
   | likelyReal | 当前操作设备的是真人用户的可能性较高。 |
   | unknown | 未知。未检测到明显特征，无法识别。 |
