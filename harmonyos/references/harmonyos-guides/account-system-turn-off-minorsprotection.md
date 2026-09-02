---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-system-turn-off-minorsprotection
title: 关闭系统的未成年人模式
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 未成年人模式 > 应用与系统实现未成年人模式联动 > 应用内关闭未成年人模式 > 关闭系统的未成年人模式
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c13fcf87406d2ddd0d3106cfbab842c9ae8abac152c2532a1d40d341fa230f66
---

## 场景介绍

系统的未成年人模式已开启。用户打开应用，在应用内关闭系统未成年人模式。

应用可调用系统的未成年人模式关闭接口[leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnoffminorsmode)，验证家长密码后关闭系统的未成年人模式。

**说明** 

用户在应用内操作时，预期可能是关闭应用的未成年人模式，而非关闭整个系统的未成年人模式（其他应用/元服务的未成年人模式也会随之关闭）。如果开发者选择这种接入方式，建议在界面上告知用户即将关闭系统的未成年人模式。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/GP_8GYl1TR6y4IwSfdE8gg/zh-cn_image_0000002706674838.png)

流程说明：

1. 用户打开应用时，应用通过订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)感知系统未成年人模式的状态变化。可以调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)或[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式信息。
2. 当系统未成年人模式已开启，且用户需要在应用内关闭未成年人模式时，应用可调用[leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnoffminorsmode)引导关闭系统未成年人模式流程，关闭整个系统的未成年人模式。

## 接口说明

以下是关闭系统的未成年人模式相关接口说明，更多接口及使用方法请参见[API参考](../harmonyos-references/account-api-minorsprotection.md)。

| 接口名 | 描述 |
| --- | --- |
| [getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)(): [MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo) | 同步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)(): Promise<[MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo)> | 异步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnoffminorsmode)(context: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)): Promise<void> | 调用该方法进行关闭系统未成年人模式流程。 |

**注意** 

1. [leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnoffminorsmode)接口需在页面或自定义组件生命周期内调用。
2. 在开启系统未成年人模式时如果选择关闭USB调试，导致开发者调试模式被禁用，开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。
3. 如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见[hilog](hilog.md)。
4. 在应用内调用开启或关闭系统未成年人模式接口，如应用需弹出toast或弹框告知用户“未成年人模式已开启或关闭”，须在接口执行完成之后，在接口的then方法里面弹出toast或弹框，否则可能出现因系统页面未完全关闭，导致toast无法正常展示的情况。
5. 如开发者需要频繁使用系统未成年人模式开启状态或者年龄段信息，建议在获取结果后进行缓存，并通过订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)来刷新系统未成年人模式开启状态或者年龄段信息，避免重复调用接口带来的性能损耗。
6. 当设备处于开机未解锁状态下，开发者调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)接口时，其返回的minorsProtectionMode字段为false。

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
3. 当系统未成年人模式已开启，且用户主动关闭应用内未成年人模式时，应用需要调用[leadToTurnOffMinorsMode](../harmonyos-references/account-api-minorsprotection.md#leadtoturnoffminorsmode)引导用户关闭系统的未成年人模式。

   ```typescript
   // 查询当前设备是否支持此系统能力
   if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
     try {
       // 查询是否支持系统未成年人模式
       if (minorsProtection.supportMinorsMode()) {
         // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
         minorsProtection.leadToTurnOffMinorsMode(this.getUIContext().getHostContext())
           .then(() => {
             // 接口调用完成，如需显示弹窗，请在此处处理
           })
           .catch((error: BusinessError<Object>) => {
             dealTurnOffAllError(error);
           });
       } else {
         hilog.info(0x0000, 'testTag',
           'The current device environment does not support the youth mode, please check the current device environment.');
       }
     } catch (error) {
       hilog.error(0x0000, 'testTag',
         `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
     }
   } else {
     hilog.info(0x0000, 'testTag',
       'The current device does not support the invoking of the leadToTurnOffMinorsMode interface.');
   }
   ```

   ```typescript
   function dealTurnOffAllError(error: BusinessError<Object>): void {
     hilog.error(0x0000, 'testTag', `Failed to leadToTurnOffMinorsMode. Code: ${error.code}, message: ${error.message}`);
   }
   ```
