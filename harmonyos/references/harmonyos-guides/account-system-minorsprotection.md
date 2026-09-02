---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-system-minorsprotection
title: 应用与系统联动切换未成年人模式
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 未成年人模式 > 应用与系统实现未成年人模式联动 > 应用与系统联动切换未成年人模式
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:51+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9045bc0e5c32dd0917d5ffb8f9670a8ef11b408c376c3d393ce1ec4c341c235f
---

## 场景介绍

在未成年人模式下，应用可通过以下两种方式获取系统未成年人模式状态，与系统未成年人模式进行联动：

1. 查询系统的未成年人模式是否开启：应用启动时，可调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)接口，主动查询系统的未成年人模式状态；如系统未成年人模式为开启状态，则应自动开启应用的未成年人模式；如系统未成年人模式为关闭状态，则应自动关闭应用的未成年人模式。
2. 订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)感知系统的未成年人模式状态：应用进程存在时，可订阅系统的未成年人模式公共事件，当订阅到系统未成年人模式开启或关闭时，应用可自动进行未成年人模式状态切换。

**说明** 

以上两种方式都需要应用实现，若开发者不实现订阅系统未成年人模式公共事件，则应用无法实时感知系统未成年人模式的变化。

示例：当应用处于前台时，若开发者未实现订阅系统未成年人模式公共事件，用户从控制中心开启系统未成年人模式后，当前应用将无法实时感知系统未成年人模式的变化。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/e51cMR1KQu2fp_jM05rZjQ/zh-cn_image_0000002736433923.png)

流程说明：

1. 用户打开应用时，应用通过订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)感知系统未成年人模式的状态变化。如果订阅到系统未成年人模式开启事件，则开启应用的未成年人模式，如果订阅到系统未成年人模式关闭事件，则展示内容不做限制，并关闭应用的未成年人模式。
2. 调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)或[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式的开启状态和年龄段信息，如果系统未成年人模式未开启，则展示内容不做限制。如果系统未成年人模式已开启，则需要根据返回的年龄段做内容分级，而且需开启应用的未成年人模式。

## 接口说明

以下是应用与系统联动切换未成年人模式的相关接口说明，更多接口及使用方法请参见[API参考](../harmonyos-references/account-api-minorsprotection.md)。

| 接口名 | 描述 |
| --- | --- |
| [getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)(): [MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo) | 同步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)(): Promise<[MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo)> | 异步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |

**注意** 

1. 在开启系统未成年人模式时如果选择关闭USB调试，导致开发者调试模式被禁用，开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。
2. 如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见[hilog](hilog.md)。
3. 如开发者需要频繁使用系统未成年人模式开启状态或者年龄段信息，建议在获取结果后进行缓存，并通过订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)来刷新系统未成年人模式开启状态或者年龄段信息，避免重复调用接口带来的性能损耗。
4. 当设备处于开机未解锁状态下，开发者调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)接口时，其返回的minorsProtectionMode字段为false。

## 开发前提

请先参考“开发准备”的[配置签名和指纹](account-sign-fingerprints.md)章节，通过自动签名方式完成签名信息的配置。请注意，该接口无需配置公钥指纹、Client ID，也无需申请账号权限。

## 开发步骤

1. 导入[minorsProtection](../harmonyos-references/account-api-minorsprotection.md)模块及相关公共模块。

   ```typescript
   import { minorsProtection } from '@kit.AccountKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 创建订阅者，订阅系统未成年人模式开启或关闭事件。推荐在应用Ability的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中调用。示例代码请参考[开发步骤](account-notification-events.md#开发步骤-1)。
3. 选择以下一种方式获取系统未成年人模式的开启状态，以及年龄段信息。当应用期望立即获取结果，推荐使用同步方式，当应用期望使用非阻塞的方式调用接口，推荐使用Promise异步回调方式。推荐在自定义组件的[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)生命周期或者应用Ability的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中调用，如开发者有频繁使用到系统未成年人模式开启状态或年龄段信息，开发者则需把获取到的系统未成年人模式开启状态或年龄段缓存下来，通过订阅[系统未成年人模式开启/关闭事件](account-notification-events.md#事件说明-1)来刷新系统未成年人模式开启状态或年龄段。

   * 通过同步方式，调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)获取系统未成年人模式的开启状态，以及年龄段信息。

     ```typescript
     // 查询当前设备是否支持此系统能力
     if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
       try {
         // 查询是否支持系统未成年人模式
         if (minorsProtection.supportMinorsMode()) {
           const minorsProtectionInfo: minorsProtection.MinorsProtectionInfo =
             minorsProtection.getMinorsProtectionInfoSync();
           // 获取系统未成年人模式开启状态
           const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
           // 如开发者有频繁使用到系统未成年人模式开启状态，这里则需缓存系统未成年人模式开启状态
           hilog.info(0x0000, 'testTag',
             `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
           // 系统未成年人模式已开启，获取年龄段信息
           // ...
           if (minorsProtectionMode) {
             const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
             if (ageGroup) {
               hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
               hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
               // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
               // ...
             }
           } else {
             // 系统未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
             // ...
           }
         } else {
           hilog.info(0x0000, 'testTag',
             'The current device environment does not support the youth mode, please check the current device environment.');
         }
       } catch (error) {
         hilog.error(0x0000, 'testTag',
           `Failed to invoke supportMinorsMode or getMinorsProtectionInfoSync. errCode: ${error.code},
           errMessage: ${error.message}`);
       }
     } else {
       hilog.info(0x0000, 'testTag',
         'The current device does not support the invoking of the getMinorsProtectionInfoSync interface.');
     }
     ```
   * 通过Promise异步回调方式，调用[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式的开启状态，以及年龄段信息。

     ```typescript
     // 查询当前设备是否支持此系统能力
     if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
       try {
         // 查询是否支持系统未成年人模式
         if (minorsProtection.supportMinorsMode()) {
           minorsProtection.getMinorsProtectionInfo()
             .then((minorsProtectionInfo: minorsProtection.MinorsProtectionInfo) => {
               // 获取系统未成年人模式开启状态
               const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
               // 如开发者有频繁使用到系统未成年人模式开启状态，这里则需缓存系统未成年人模式开启状态
               hilog.info(0x0000, 'testTag',
                 `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
               // 系统未成年人模式已开启，获取年龄段信息
               if (minorsProtectionMode) {
                 const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
                 if (ageGroup) {
                   hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
                   hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
                   // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
                 }
               } else {
                 // 系统未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
               }
             })
             .catch((error: BusinessError<Object>) => {
               dealGetMinorsInfoAllError(error);
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
         'The current device does not support the invoking of the getMinorsProtectionInfo interface.');
     }
     ```

     ```typescript
     function dealGetMinorsInfoAllError(error: BusinessError<Object>): void {
       hilog.error(0x0000, 'testTag', `Failed to getMinorsProtectionInfo. Code: ${error.code}, message: ${error.message}`);
     }
     ```
