---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-urlthreat-check
title: URL检测
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全检测 > URL检测
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:607a5b789bb387638cd09a0da770a19bf3da09a713e924c9992f07a43eea1da3
---

## 场景介绍

应用通过调用Device Security Kit的[checkUrlThreat](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectcheckurlthreat)接口检测URL是否为恶意的，并且根据检测结果来提示或拦截该URL。

典型场景：用户访问网址时，判断用户访问的URL是否为恶意网址，对于恶意网址，提示或拦截用户的访问风险。

## 约束与限制

* URL检测能力支持Phone、Tablet、PC/2in1设备。并且从5.1.0(18)版本开始，新增支持Wearable设备。
* 每个应用在每个设备上每天最多可以调用1万次接口；每个设备上最多支持5个并发调用。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/l7SCWXLxT4iaagJMrDMeYg/zh-cn_image_0000002742123439.png)

**流程说明：**

1. 开发者应用调用URL检测（[checkUrlThreat](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectcheckurlthreat)）接口，传入待检测的URL，并获得URL检测结果。

   Device Security Kit将请求发送到华为服务器检测URL风险，并将检测结果返回给开发者应用（NORMAL、PHISHING、MALWARE、OTHERS）。
2. 开发者应用可以根据检测结果来决定业务处理策略。

## 接口说明

以下是URL检测相关接口，包括ArkTS API，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectcheckurlthreat)。

| 接口名 | 描述 |
| --- | --- |
| [checkUrlThreat](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectcheckurlthreat)(req: [UrlCheckRequest](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#urlcheckrequest)): Promise<[UrlCheckResponse](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#urlcheckresponse)> | 检测URL风险 |

## 开发步骤

**说明** 

请确保已打开“[安全检测服务](devicesecurity-deviceverify-activateservice.md)”开关并[申请Profile](../app/agc-help-profile-0000002270709473.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { safetyDetect } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[checkUrlThreat](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectcheckurlthreat)接口获取URL检测结果。

   **注意** 

   该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

   ```typescript
   const TAG = 'SafetyDetectJsTest';

   // 请求URL检测，并处理结果
   let req : safetyDetect.UrlCheckRequest = {
     urls : ['https://test1.com']
   };
   try {
     hilog.info(0x0000, TAG, 'CheckUrlThreat begin.');
     const data: safetyDetect.UrlCheckResponse = await safetyDetect.checkUrlThreat(req);
     hilog.info(0x0000, TAG, 'Succeeded in checkUrlThreat: %{public}s %{public}d', data.results[0].url, data.results[0].threat);
     // ...
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'CheckUrlThreat failed: %{public}d %{public}s', e.code, e.message);
     // ...
   }
   ```
