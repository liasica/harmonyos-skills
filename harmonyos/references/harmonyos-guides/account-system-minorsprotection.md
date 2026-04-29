---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-system-minorsprotection
title: 应用与系统联动切换未成年人模式
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > 未成年人模式 > 应用与系统实现未成年人模式联动 > 应用与系统联动切换未成年人模式
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:55+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:22d42223ae464cb6b6179405cf9c6c90b4cbd37defd5613c4c82348f340b3bb7
---

## 场景介绍

在未成年人模式下，应用可通过以下两种方式获取系统未成年人模式状态，与系统未成年人模式进行联动：

说明

以下两种方式都需要应用实现，如开发者不实现订阅系统未成年人模式公共事件，则应用无法实时感知系统未成年人模式的变化。

示例：当应用处于前台时，若开发者未实现订阅系统未成年人模式公共事件，用户从控制中心开启未成年人模式后，当前应用将无法实时感知系统未成年人模式的变化。

1. 查询系统的未成年人模式是否开启：应用启动时，可调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)接口，主动查询系统的未成年人模式状态；如系统未成年人模式为开启状态，则应自动开启应用的未成年人模式；如系统未成年人模式为关闭状态，则应自动关闭应用的未成年人模式。
2. 订阅[系统未成年人模式公共事件](account-system-minorsprotection.md#事件说明)感知系统的未成年人模式状态：应用进程存在时，可订阅系统的未成年人模式公共事件，当订阅到系统未成年人模式开启或关闭时，应用可自动进行未成年人模式状态切换。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/c321NA2UTBqwlq1A5zbm4g/zh-cn_image_0000002589325129.png?HW-CC-KV=V1&HW-CC-Date=20260429T053654Z&HW-CC-Expire=86400&HW-CC-Sign=4B780A2E7BFABB5B768815D31EBB47812137E9B88AA80F76501A25D5472DDF8F)

流程说明：

1. 用户打开应用时，应用通过订阅[系统未成年人模式公共事件](account-system-minorsprotection.md#事件说明)感知系统未成年人模式的状态变化。如果订阅到系统未成年人模式开启事件，则开启应用的未成年人模式，如果订阅到系统未成年人模式关闭事件，则展示内容不做限制，并关闭应用的未成年人模式。
2. 调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)或[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式的开启状态和年龄段信息，如果系统未成年人模式未开启，则展示内容不做限制。如果系统未成年人模式已开启，则需要根据返回的年龄段做内容分级，而且需开启应用的未成年人模式。

## 接口说明

以下是应用与系统联动切换未成年人模式的相关接口说明，更多接口及使用方法请参见[API参考](../harmonyos-references/account-api-minorsprotection.md)。

| 接口名 | 描述 |
| --- | --- |
| [getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)(): [MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo) | 同步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |
| [getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)(): Promise<[MinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#minorsprotectioninfo)> | 异步接口，获取系统未成年人模式的开启状态，以及年龄段信息。 |

注意

1. 当未成年人模式开启时，当前设备的开发者调试模式会被禁用，开发者可以进入设置-系统-开发者选项，点击USB调试开关，会校验健康使用设备密码，校验成功后可解除开发者调试模式限制。
2. 如开发者重新开启USB调试开关后，发现DevEco Studio工具上hilog日志未恢复到断连之前，请执行“hdc shell hilog -G 16M”来扩大hilog日志缓存区，若hilog日志仍无法完全展示，可取出hilog日志本地查看。更多命令请参见[hilog](hilog.md)。
3. 如开发者需要频繁使用未成年人模式开启状态或者年龄段信息，建议在获取结果后进行缓存，并通过订阅[系统未成年人模式公共事件](account-system-minorsprotection.md#事件说明)来刷新未成年人模式开启状态或者年龄段信息，避免重复调用接口带来的性能损耗。
4. 当设备处于开机未解锁状态下，开发者调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)接口时，其返回的minorsProtectionMode字段为false。

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
   3. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   ```
2. 创建订阅者，订阅系统未成年人模式开启或关闭事件。推荐在应用Ability的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中调用。

   ```
   1. // 订阅者信息
   2. const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
   3. events: [commonEventManager.Support.COMMON_EVENT_MINORSMODE_ON,
   4. commonEventManager.Support.COMMON_EVENT_MINORSMODE_OFF]
   5. };

   7. // 如开发者使用await改写createSubscriber方法，需要把此变量定义到全局(struct外层)
   8. let subscriber: commonEventManager.CommonEventSubscriber;
   9. // 创建订阅者
   10. commonEventManager.createSubscriber(subscribeInfo)
   11. .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
   12. // 这里获取到commonEventSubscriber对象需要暂存，用于后续事件回调。不可直接使用，否则会出现事件回调不生效的情况
   13. subscriber = commonEventSubscriber;
   14. // 订阅公共事件
   15. commonEventManager.subscribe(subscriber,
   16. (error: BusinessError, data: commonEventManager.CommonEventData) => {
   17. if (error) {
   18. dealCommonEventAllError(error);
   19. return;
   20. }
   21. if (data.event === commonEventManager.Support.COMMON_EVENT_MINORSMODE_ON) {
   22. // 订阅到开启事件，可以调用获取年龄段的接口，根据年龄段刷新内容展示，同时如开发者有缓存年龄段或未成年人模式开启状态，则需要刷新缓存
   23. return;
   24. }
   25. if (data.event === commonEventManager.Support.COMMON_EVENT_MINORSMODE_OFF) {
   26. // 订阅到关闭事件，关闭当前应用的未成年人模式，刷新应用内容展示，取消年龄限制，如开发者有缓存未成年人模式开启状态，则需要刷新缓存
   27. }
   28. });
   29. })
   30. .catch((error: BusinessError) => {
   31. dealCommonEventAllError(error);
   32. });
   ```

   ```
   1. function dealCommonEventAllError(error: BusinessError): void {
   2. hilog.error(0x0000, 'testTag', `Failed to subscribe. Code: ${error.code}, message: ${error.message}`);
   3. }
   ```
3. 选择以下一种方式获取未成年人模式的开启状态，以及年龄段信息。当应用期望立即获取结果，推荐使用同步方式，当应用期望使用非阻塞的方式调用接口，推荐使用Promise异步回调方式。推荐在自定义组件的[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)生命周期或者应用Ability的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期中调用，如开发者有频繁使用到未成年人模式开启状态或年龄段信息，开发者则需把获取到的系统未成年人模式开启状态或年龄段缓存下来，通过订阅[系统未成年人模式公共事件](account-system-minorsprotection.md#事件说明)来刷新未成年人模式开启状态或年龄段。

   * 通过同步方式，调用[getMinorsProtectionInfoSync](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfosync)获取系统未成年人模式的开启状态，以及年龄段信息。

     ```
     1. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
     2. try {
     3. // 查询是否支持系统未成年人模式
     4. if (minorsProtection.supportMinorsMode()) {
     5. const minorsProtectionInfo: minorsProtection.MinorsProtectionInfo =
     6. minorsProtection.getMinorsProtectionInfoSync();
     7. // 获取未成年人模式开启状态
     8. const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
     9. // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
     10. hilog.info(0x0000, 'testTag',
     11. `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
     12. // 未成年人模式已开启，获取年龄段信息
     13. if (minorsProtectionMode) {
     14. const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
     15. if (ageGroup) {
     16. hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
     17. hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
     18. // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
     19. }
     20. } else {
     21. // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
     22. }
     23. } else {
     24. hilog.info(0x0000, 'testTag',
     25. 'The current device environment does not support the youth mode, please check the current device environment.');
     26. }
     27. } catch (error) {
     28. hilog.error(0x0000, 'testTag',
     29. `Failed to invoke supportMinorsMode or getMinorsProtectionInfoSync. errCode: ${error.code},
     30. errMessage: ${error.message}`);
     31. }
     32. } else {
     33. hilog.info(0x0000, 'testTag',
     34. 'The current device does not support the invoking of the getMinorsProtectionInfoSync interface.');
     35. }
     ```
   * 通过Promise异步回调方式，调用[getMinorsProtectionInfo](../harmonyos-references/account-api-minorsprotection.md#getminorsprotectioninfo)获取系统未成年人模式的开启状态，以及年龄段信息。

     ```
     1. if (canIUse('SystemCapability.AuthenticationServices.HuaweiID.MinorsProtection')) {
     2. try {
     3. // 查询是否支持系统未成年人模式
     4. if (minorsProtection.supportMinorsMode()) {
     5. minorsProtection.getMinorsProtectionInfo()
     6. .then((minorsProtectionInfo: minorsProtection.MinorsProtectionInfo) => {
     7. // 获取未成年人模式开启状态
     8. const minorsProtectionMode: boolean = minorsProtectionInfo.minorsProtectionMode;
     9. // 如开发者有频繁使用到未成年人模式开启状态，这里则需缓存未成年人模式开启状态
     10. hilog.info(0x0000, 'testTag',
     11. `Succeeded in getting minorsProtectionMode is: ${minorsProtectionMode.valueOf()}`);
     12. // 未成年人模式已开启，获取年龄段信息
     13. if (minorsProtectionMode) {
     14. const ageGroup: minorsProtection.AgeGroup | undefined = minorsProtectionInfo.ageGroup;
     15. if (ageGroup) {
     16. hilog.info(0x0000, 'testTag', `Succeeded in getting lowerAge is: ${ageGroup.lowerAge}`);
     17. hilog.info(0x0000, 'testTag', `Succeeded in getting upperAge is: ${ageGroup.upperAge}`);
     18. // 根据年龄段刷新内容展示。如开发者有频繁使用到年龄段信息，这里则需缓存年龄段信息
     19. }
     20. } else {
     21. // 未成年人模式未开启，应用需跟随系统未成年人模式，展示内容不做限制
     22. }
     23. })
     24. .catch((error: BusinessError<Object>) => {
     25. dealGetMinorsInfoAllError(error);
     26. });
     27. } else {
     28. hilog.info(0x0000, 'testTag',
     29. 'The current device environment does not support the youth mode, please check the current device environment.');
     30. }
     31. } catch (error) {
     32. hilog.error(0x0000, 'testTag',
     33. `Failed to invoke supportMinorsMode. errCode: ${error.code}, errMessage: ${error.message}`);
     34. }
     35. } else {
     36. hilog.info(0x0000, 'testTag',
     37. 'The current device does not support the invoking of the getMinorsProtectionInfo interface.');
     38. }
     ```

     ```
     1. function dealGetMinorsInfoAllError(error: BusinessError<Object>): void {
     2. hilog.error(0x0000, 'testTag', `Failed to getMinorsProtectionInfo. Code: ${error.code}, message: ${error.message}`);
     3. }
     ```
