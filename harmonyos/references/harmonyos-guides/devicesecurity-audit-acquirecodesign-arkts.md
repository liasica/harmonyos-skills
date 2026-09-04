---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-audit-acquirecodesign-arkts
title: 代码签名信息查询场景
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全审计 > 代码签名信息查询场景
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7bd95fdab8270788fa9221137834816421beba63f0e3bd7483e4b56fe9839457
---

从6.1.1(24)开始，新增提供文件代码签名信息查询接口，可以获取设备上已签名的文件签名信息。

## 场景介绍

签名信息包括：应用ID、签发组织证书链、签名摘要、签名时间戳、签名使用的Hash算法。通过[acquireCodeSign](../harmonyos-references/devicesecurity-securityaudit-api.md#acquirecodesign)接口，开发者应用可以获取代码签名信息，辅助开发者应用判断运行代码的完整性和安全性，从而有效防止恶意软件的运行，提升设备安全防护能力。

## 约束和限制

1. 当前能力仅支持PC/2in1设备。
2. 调用[acquireCodeSign](../harmonyos-references/devicesecurity-securityaudit-api.md#acquirecodesign)接口的开发者应用需要具备读取目标代码签名文件的权限。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/C4r9SNaMS5WMLwiqNlMahg/zh-cn_image_0000002712404506.png)

**流程说明：**

1. 开发者应用调用文件代码签名信息查询接口[acquireCodeSign](../harmonyos-references/devicesecurity-securityaudit-api.md#acquirecodesign)。
2. [acquireCodeSign](../harmonyos-references/devicesecurity-securityaudit-api.md#acquirecodesign)接口同步返回开发者应用所传入的文件对应的代码签名信息。

## 接口说明

接口如下表，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-securityaudit-api.md#acquirecodesign)。

| 接口名 | 描述 |
| --- | --- |
| [acquireCodeSign](../harmonyos-references/devicesecurity-securityaudit-api.md#acquirecodesign)(path: string): string | 获取输入的文件路径的代码签名信息。 |

## 开发步骤

**说明** 

在开发准备过程中，需要申请权限：ohos.permission.QUERY\_AUDIT\_EVENT，只允许清单内的企业类应用申请该权限，申请方式请参考：[企业类应用可用权限](permissions-for-enterprise-apps.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { securityAudit } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 开发者应用调用[acquireCodeSign](../harmonyos-references/devicesecurity-securityaudit-api.md#acquirecodesign)接口，获取所传入的文件对应的代码签名信息。

   ```typescript
   const TAG = 'SecurityAuditJsTest';
   let path = 'test';
   try {
     hilog.info(0x0000, TAG, 'acquireCodeSign begin.');
     const result = securityAudit.acquireCodeSign(path);
     hilog.info(0x0000, TAG, 'Succeeded in queryCodeSign.');
     // ...
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'acquireCodeSign failed: %{public}d %{public}s', e.code, e.message);
     // ...
   }
   ```
