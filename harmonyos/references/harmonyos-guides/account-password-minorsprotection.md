---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-password-minorsprotection
title: 应用内调整未成年人模式设置
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 未成年人模式 > 应用与系统实现未成年人模式联动 > 应用内调整未成年人模式设置
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30d8e1e6730c9a18dcd111d8ebdfec802b5d2660c24a622f7d1c89dda6571ad2
---

## 场景介绍

系统的未成年人模式已开启，应用已随系统切换至未成年人模式。用户打开应用，希望在应用内调整内容偏好、使用时长等设置，需要验证家长身份。

应用可调用家长身份验证接口[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)，拉起验证未成年人模式密码页面。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/SEmFqUmBT-iAZMd0DWui0g/zh-cn_image_0000002552799112.png?HW-CC-KV=V1&HW-CC-Date=20260427T234804Z&HW-CC-Expire=86400&HW-CC-Sign=B43E26BBFDBC9AE2952257D6E1D6B8331835E404A79FC354DDB4F462B6DFF13C)

流程说明：

1. 用户打开应用时，应用通过[系统未成年人模式公共事件](account-password-minorsprotection.md#事件说明)感知未成年人模式的状态变化。可以调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)或[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式信息。
2. 当系统未成年人模式已开启，且用户修改应用内设置时，应用可调用[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)验证未成年人模式密码，当校验通过后，才可修改当前应用的未成年人模式设置。

## 接口说明

以下是应用内验证家长密码相关接口说明，更多接口及使用方法请参见[API参考](../harmonyos-references/account-api-minorsprotection.md)。

| 接口名 | 描述 |
| --- | --- |
| [getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)(): [MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo) | 同步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)(): Promise<[MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo)> | 异步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)(context: [common.Context](../harmonyos-references/js-apis-app-ability-common.md#context)): Promise<boolean> | 调用该方法拉起验证未成年人模式密码页面。 |

注意

1. [verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)接口需在页面或自定义组件生命周期内调用。接口调用前提是未成年人模式已开启，如果在未开启未成年人模式下调用此接口会返回错误码[1009900002](../harmonyos-references/account-api-error-code.md#section1009900002-未成年人模式未开启)。
2. 当未成年人模式开启时，当前设备的开发者调试模式会被禁用，开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。
3. 如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见[hilog](hilog.md)。
4. 如开发者需要频繁使用未成年人模式开启状态或者年龄段信息，建议在获取结果后进行缓存，并通过订阅[系统未成年人模式公共事件](account-password-minorsprotection.md#事件说明)来刷新未成年人模式开启状态或者年龄段信息，避免重复调用接口带来的性能损耗。
5. 当设备处于开机未解锁状态下，开发者调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)接口时，其返回的minorsProtectionMode字段为false。

## 事件说明

以下是系统未成年人模式开启或关闭发送的广播事件。

| 事件名称 | 值 | 描述 |
| --- | --- | --- |
| [COMMON\_EVENT\_MINORSMODE\_ON](../harmonyos-references/commoneventmanager-definitions.md#common_event_minorsmode_on12) | usual.event.MINORSMODE\_ON | 表示系统未成年人模式开启事件。 |
| [COMMON\_EVENT\_MINORSMODE\_OFF](../harmonyos-references/commoneventmanager-definitions.md#common_event_minorsmode_off12) | usual.event.MINORSMODE\_OFF | 表示系统未成年人模式关闭事件。 |

说明

未成年人模式开启事件触发时机：

主动开启系统未成年人模式（PC/2in1设备暂不支持从控制中心开启未成年人模式），当前设备会发送未成年人模式开启事件。

## 开发前提

请先参考“开发准备”的[配置签名和指纹](account-sign-fingerprints.md)章节，通过自动签名方式完成签名信息的配置。请注意，该接口无需配置公钥指纹、Client ID，也无需申请账号权限。

## 开发步骤

1. 导入[minorsProtection](../harmonyos-references/account-api-minorsprotection.md)模块及相关公共模块。

   ```
   1. import { minorsProtection } from '@kit.AccountKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 订阅系统未成年人模式开启或关闭事件、获取未成年人模式的开启状态，以及年龄段信息请参考应用与系统联动切换未成年人模式章节的[开发步骤](account-system-minorsprotection.md#开发步骤)。
3. 当未成年人模式已开启，用户需要调整应用内未成年人模式设置时调用[verifyMinorsProtectionCredential](../harmonyos-references/account-api-minorsprotection.md#verifyminorsprotectioncredential)方法拉起验证未成年人模式密码页面。验证成功后才允许修改。

   ```
   1. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
   2. try {
   3. if (minorsProtection.supportMinorsMode()) {
   4. // 此示例为代码片段，实际需在自定义组件实例中使用，并传入有效的Context上下文对象
   5. minorsProtection.verifyMinorsProtectionCredential(this.getUIContext().getHostContext())
   6. .then((result: boolean) => {
   7. hilog.info(0x0000, 'testTag', `Succeeded in getting verify result is: ${result.valueOf()}`);
   8. // 使用结果判断验密是否通过，执行后续流程
   9. })
   10. .catch((error: BusinessError<Object>) => {
   11. dealVerifyAllError(error);
   12. });
   13. } else {
   14. hilog.info(0x0000, 'testTag',
   15. 'The current device environment does not support the youth mode, please check the current device environment.');
   16. }
   17. } catch (error) {
   18. hilog.error(0x0000, 'testTag',
   19. `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
   20. }
   21. } else {
   22. hilog.info(0x0000, 'testTag',
   23. 'The current device does not support the invoking of the verifyMinorsProtectionCredential interface.');
   24. }
   ```

   ```
   1. function dealVerifyAllError(error: BusinessError<Object>): void {
   2. hilog.error(0x0000, 'testTag', `Failed to verify. Code: ${error.code}, message: ${error.message}`);
   3. }
   ```
