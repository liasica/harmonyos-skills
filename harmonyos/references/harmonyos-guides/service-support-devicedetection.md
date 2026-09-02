---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/service-support-devicedetection
title: 检测设备硬件一致性
breadcrumb: 指南 > 系统 > 基础功能 > Service Support Kit（服务与支持） > 检测设备硬件一致性
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:09+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:b562a20a320c86b15b7bcd933563734ce40fa4c95b2e07880a7bd51b10a293ee
---

## 场景介绍

企业应用通过集成设备硬件一致性检测能力，赋能回收场景的自动化检测。例如：在“以旧换新”活动中，门店人员利用检测类应用调用该能力，对旧机的屏幕、电池及主板等核心硬件进行检测。检测结果直接作为旧机估价与回收决策的关键依据。需注意的是，检测过程要求设备保持联网，以保障数据实时获取与结果准确性。

## 约束与限制

* 接入限制：该功能仅对涉及二手电子设备回收业务企业开放，该企业需持有二手电子设备回收资质及签署DSA（Data Sharing Agreement，数据共享协议）协议。
* 使用限制：检测过程中，设备需要保持联网状态。
* 权限申请说明：需申请权限ohos.permission.DETECT\_DEVICE，该能力受限开放，仅支持部分合作企业应用接入。权限申请方式请参考[申请使用受限权限](declare-permissions-in-acl.md)。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/servicesupport-api-devicedetection.md)。

| 接口名 | 描述 |
| --- | --- |
| getDeviceComponentVerificationDetails(): Promise<DeviceComponentVerificationResult> | 获取设备硬件一致性校验结果。使用Promise异步回调。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { BusinessError } from "@kit.BasicServicesKit";
   import { deviceDetection } from "@kit.ServiceSupportKit";
   ```
2. 调用[DeviceComponentVerificationResult](../harmonyos-references/servicesupport-api-devicedetection.md#componentverificationdetail)定义设备硬件信息。

   ```typescript
   // 创建初始化结果对象
   let result: deviceDetection.DeviceComponentVerificationResult = {
       componentDetails: []
   }
   ```
3. 调用[getDeviceComponentVerificationDetails](../harmonyos-references/servicesupport-api-devicedetection.md#devicedetectiongetdevicecomponentverificationdetails)获取设备一致性校验结果。

   ```typescript
   try {
       // 接收一致性检测结果
       result = await deviceDetection.getDeviceComponentVerificationDetails();
   } catch (error) {
       // 捕获异常
       const err: BusinessError = error as BusinessError;
       console.error('enter into getDeviceComponentVerificationDetails catch, code is: ' + err.code + ' message is: ' + err.message);
   }
   ```
