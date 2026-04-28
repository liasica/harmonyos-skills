---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intelligentscene
title: @ohos.intelligentScene (情景模式)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 其他 > @ohos.intelligentScene (情景模式)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:881316794fe26a44390ed3bea59e9c74d3bc69d9f97461b61d23720313de32c2
---

本模块提供查询免打扰的相关功能，包括查询系统的免打扰功能是否开启、查询应用自身是否允许打扰等。情景模式（免打扰、睡眠模式、学习模式、工作模式和自定义模式）开启时，免打扰功能会开启。

说明

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhoneTablet

```
1. import { intelligentScene } from '@kit.BasicServicesKit';
```

## intelligentScene.isDoNotDisturbEnabled

PhoneTablet

isDoNotDisturbEnabled(): Promise<boolean>

系统免打扰功能是否已开启，使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.IntelligentScene

**需要权限：** ohos.permission.GET\_DONOTDISTURB\_STATE

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回免打扰功能是否已开启。true表示免打扰功能已开启，false表示免打扰功能未开启。 |

**错误码**：

以下错误码详细介绍请参考[情景模式错误码](errorcode-intelligentscene.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 35200001 | Internal error. |

**示例**：

```
1. import { BusinessError, intelligentScene } from '@kit.BasicServicesKit';

3. let isDoNotDisturbEnabled: boolean = false;
4. try {
5. isDoNotDisturbEnabled = await intelligentScene.isDoNotDisturbEnabled();
6. } catch (err) {
7. console.error(`Failed to get doNotDisturb state, code: ${err.code}, message: ${err.message}`);
8. }
9. if (isDoNotDisturbEnabled) {
10. console.info('DoNotDisturb state is open');
11. } else {
12. console.info('DoNotDisturb state is closed');
13. }
```

## intelligentScene.isNotifyAllowedInDoNotDisturb

PhoneTablet

isNotifyAllowedInDoNotDisturb(): Promise<boolean>

如果用户已经把当前应用添加到了情景模式允许打扰列表内，那么开启此情景模式后，当前应用推送的通知将正常提醒、并且响铃振动，使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Applications.IntelligentScene

**需要权限：** ohos.permission.GET\_DONOTDISTURB\_STATE

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。免打扰功能未开启时，返回false；免打扰功能开启时，返回是否允许当前应用打扰：true表示允许打扰，false表示不允许打扰。 |

**错误码**：

以下错误码详细介绍请参考[情景模式错误码](errorcode-intelligentscene.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 35200001 | Internal error. |

**示例**：

```
1. import { BusinessError, intelligentScene } from '@kit.BasicServicesKit';

3. let isNotifyAllowedInDoNotDisturb: boolean = false;
4. try {
5. isNotifyAllowedInDoNotDisturb = await intelligentScene.isNotifyAllowedInDoNotDisturb();
6. } catch (err) {
7. console.error(`Failed to get doNotDisturb state, code: ${err.code}, message: ${err.message}`);
8. }
9. if (isNotifyAllowedInDoNotDisturb) {
10. console.info('Allowed to notify in doNotDisturb state');
11. } else {
12. console.info('Not allowed to notify in doNotDisturb state or doNotDisturb is closed');
13. }
```
