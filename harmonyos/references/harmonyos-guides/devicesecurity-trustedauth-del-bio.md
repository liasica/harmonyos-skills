---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-del-bio
title: 关闭指定生物类型认证能力
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 生物特征绑定、认证与解绑 > 关闭指定生物类型认证能力
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:02+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:f113a00a095b7e14bf7d6bc2dd68d57ed73a877e786e6e56d307fdf40f383622
---

## 场景介绍

当用户期望关闭指定生物特征认证能力时，可以通过指定已开通的生物特征信息，关闭指定的生物类型认证能力。

## 约束与限制

1. 本功能在6.1.1(24)之前版本仅支持Phone；6.1.1(24)及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。
2. 本功能需企业开发者应用服务器端完成接口接入，以配合端云协同认证流程。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/7q4msuBNSsi1c8RMbfvV2w/zh-cn_image_0000002736433453.jpg)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/errorcode-devicesecurity-trusted-auth.md)。

| 接口名 | 描述 |
| --- | --- |
| [disableTrustedBioAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationdisabletrustedbioauthentication)(authID: bigint, authType: [AuthType](../harmonyos-references/devicesecurity-trusted-auth-api.md#authtype)): Promise<void> | 解绑指定生物类型认证能力。 |

## 开发步骤

1. 导入trustedAuthentication 和相关依赖模块。

   ```typescript
   import { resourceManager } from '@kit.LocalizationKit'
   import { huks } from '@kit.UniversalKeystoreKit';
   import { userAuth } from '@kit.UserAuthenticationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 首先开发者需要在服务器查询对应账户是否已开通对应生物特征认证能力，在确认开通后方可发起解绑指定生物类型认证能力请求。
3. 发起关闭指定生物类型认证能力请求前，需从服务器获取当前账号在[设置数字盾密码](devicesecurity-trustedauth-setpwd.md)时获取的authID。
4. 调用数字盾解绑指定生物类型认证能力接口发起关闭对应生物类型认证能力申请。

   ```typescript
   async disableTrustedBioAuthentication(assetName: string, authType: number): Promise<void> {
     try {
       let resArray: Uint8Array = await AssetUtils.QueryDataFromAssetStore(assetName);
       let credentialID: bigint = CryptoUtils.uint8ArrayToBigInt(resArray); // 实际填充为从服务器获取到的账号对应的credentialID值
       await trustedAuthentication.disableTrustedBioAuthentication(credentialID, authType);
       hilog.info(0x0000, 'testTag', 'unBound success');
     } catch (error) {
       hilog.error(0x0000, 'testTag', 'unBound fail', JSON.stringify(error));
       throw new Error('unBound fail' + (error as BusinessError).message);
     }
   }
   ```
5. 在接收到端侧解绑成功结果后，开发者需要同步将服务器绑定的生物特征信息解绑。
