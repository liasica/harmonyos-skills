---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-password-minorsprotection
title: 应用内调整未成年人模式设置
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 未成年人模式 > 应用与系统实现未成年人模式联动 > 应用内调整未成年人模式设置
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:a775e82df948aa4eb602c6df989d4b615e4c8d3b5a7201538fd9822cbfa23890
---

## 场景介绍

系统的未成年人模式已开启，应用已随系统切换至未成年人模式。用户打开应用，希望在应用内调整内容偏好、使用时长等设置，需要验证家长身份。

应用可调用家长身份验证接口[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)，拉起验证系统未成年人模式密码页面。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/IN7vNm1sTR6quFOA45psEg/zh-cn_image_0000002742123927.png)

流程说明：

1. 用户打开应用时，应用通过[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)感知系统未成年人模式的状态变化。可以调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)或[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式信息。
2. 当系统未成年人模式已开启，且用户修改应用内设置时，应用可调用[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)验证系统未成年人模式密码，当校验通过后，才可修改当前应用的未成年人模式设置。

## 接口说明

以下是应用内验证家长密码相关接口说明，更多接口及使用方法请参见[API参考](../harmonyos-references/account-api-minorsprotection.md)。

| 接口名 | 描述 |
| --- | --- |
| [getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)(): [MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo) | 同步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)(): Promise<[MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo)> | 异步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)(context: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)): Promise<boolean> | 调用该方法拉起验证系统未成年人模式密码页面。 |

**注意** 

1. [verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)接口需在页面或自定义组件生命周期内调用，否则会返回错误码[401](../harmonyos-references/errorcode-universal.md#section401-参数检查失败)。接口调用前提是系统未成年人模式已开启，如果在未开启系统未成年人模式下调用此接口会返回错误码[1009900002](../harmonyos-references/errorcode-account-kit.md#section1009900002-未成年人模式未开启)。
2. 在开启系统未成年人模式时如果选择关闭USB调试，导致开发者调试模式被禁用，开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。
3. 如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见[hilog](hilog.md)。
4. 如开发者需要频繁使用系统未成年人模式开启状态或者年龄段信息，建议在获取结果后进行缓存，并通过订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)来刷新系统未成年人模式开启状态或者年龄段信息，避免重复调用接口带来的性能损耗。
5. 当设备处于开机未解锁状态下，开发者调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)接口时，其返回的minorsProtectionMode字段为false。

## 开发前提

请先参考“开发准备”的[配置签名和指纹](account-sign-fingerprints.md)章节，通过自动签名方式完成签名信息的配置。请注意，该接口无需配置公钥指纹、Client ID，也无需申请账号权限。

## 开发步骤

1. 导入[minorsProtection](../harmonyos-references/account-api-minorsprotection.md)模块及相关公共模块。

   ```typescript
   import { minorsProtection } from '@kit.AccountKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 订阅系统未成年人模式开启或关闭事件、获取系统未成年人模式的开启状态，以及年龄段信息请参考应用与系统联动切换未成年人模式章节的[开发步骤](account-system-minorsprotection.md#开发步骤)。
3. 当系统未成年人模式已开启，用户需要调整应用内未成年人模式设置时调用[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)方法拉起验证系统未成年人模式密码页面。验证成功后才允许修改。

   ```typescript
   // 查询当前设备是否支持此系统能力
   if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
     try {
       // 查询是否支持系统未成年人模式
       if (minorsProtection.supportMinorsMode()) {
         // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
         await minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
           .then((result: boolean) => {
             hilog.info(0x0000, 'testTag', `Succeeded in getting verify result is: ${result.valueOf()}`);
             // ...
             // 使用结果判断验密是否通过，执行后续流程
             // ...
           })
           .catch((error: BusinessError<Object>) => {
             dealVerifyAllError(error);
             // ...
           });
         // ...
       } else {
         hilog.info(0x0000, 'testTag',
           'The current device environment does not support the youth mode, please check the current device environment.');
         // ...
       }
     } catch (error) {
       hilog.error(0x0000, 'testTag',
         `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
       // ...
     }
   } else {
     hilog.info(0x0000, 'testTag',
       'The current device does not support the invoking of the verifyMinorsProtectionCredential interface.');
     // ...
   }
   ```

   ```typescript
   function dealVerifyAllError(error: BusinessError<Object>): void {
     hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
   }
   ```
