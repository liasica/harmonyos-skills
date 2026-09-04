---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-appself-turn-off-minorsprotection
title: 关闭应用的未成年人模式（推荐）
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 未成年人模式 > 应用与系统实现未成年人模式联动 > 应用内关闭未成年人模式 > 关闭应用的未成年人模式（推荐）
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e9226e12c16dc8fcd68298a73ee8fa9439bdd7dfe14e7a2850e784b9d46c051d
---

## 场景介绍

系统的未成年人模式已开启，用户打开应用，希望单独关闭应用的未成年人模式，系统的未成年人模式仍保持开启。

当用户需要关闭应用的未成年人模式时，应用可调用系统家长身份验证接口[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)，验证通过后可关闭应用的未成年人模式。

**说明** 

当前场景为关闭未成年人模式的推荐方案，相较于关闭系统的未成年人模式，单独关闭应用的未成年人模式更为灵活，且较符合用户体验预期。当前场景需要开发者在应用侧记录单独关闭状态（示例：userTurnOffFlag，记录用户是否主动关闭了应用的未成年人模式），便于后续与系统重新联动。如应用重新启动时：

1. 当应用查询到userTurnOffFlag为True，应用需保持应用的未成年人模式为关闭状态。
2. 当应用查询到userTurnOffFlag为False，应用需与系统进行联动。

建议开发者在选择这种接入方式的时候，在界面上告知用户，当前仅关闭应用的未成年人模式，但系统的未成年人模式仍保持开启，避免用户误解。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/A5kfNpGZTcWCWR54lyxtww/zh-cn_image_0000002742003967.png)

流程说明：

1. 用户打开应用时，应用通过订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)感知系统未成年人模式的状态变化。可以调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)或[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式信息。当查询到系统未成年人模式未开启，需要记录单独关闭的标记为false。
2. 当系统未成年人模式已开启，且用户需要在应用内关闭未成年人模式时，应用可调用[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)验证系统未成年人模式密码，当校验通过后，才可关闭当前应用的未成年人模式，同时记录单独关闭的标记为true。

## 接口说明

以下是关闭应用的未成年人模式相关接口说明，更多接口及使用方法请参见[API参考](../harmonyos-references/account-api-minorsprotection.md)。

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
2. 订阅系统未成年人模式开启或关闭事件、获取系统未成年人模式的开启状态，以及年龄段信息请参考应用与系统联动切换未成年人模式章节的[开发步骤](account-system-minorsprotection.md#开发步骤)。当查询到系统未成年人模式已关闭或订阅系统未成年人模式关闭事件，需要记录单独关闭的标记为false。
3. 当系统未成年人模式已开启，用户需要关闭应用的未成年人模式时调用[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)方法拉起验证系统未成年人模式密码页面。验证成功后才可关闭，同时记录单独关闭的标记为true。

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
             // 使用结果判断验密是否通过，执行后续流程，验证成功后，关闭应用的未成年人模式，同时记录单独关闭的标记为true，需要缓存该标记
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
