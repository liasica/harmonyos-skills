---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-superprivacymode-api
title: SuperPrivacyMode（超级隐私模式）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > SuperPrivacyMode（超级隐私模式）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:14+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ca780cfae42d5925c951435bc42193935e5c48ca6981ad0c852816d9b0a87a2d
---

本模块提供超级隐私模式相关接口，应用可根据当前的超级隐私模式的状态进行相应业务处理。

**起始版本：** 6.0.2(22)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { superPrivacyMode } from '@kit.DeviceSecurityKit';
```

## SuperPrivacyMode

PhonePC/2in1TabletTVWearable

表示超级隐私模式状态的枚举。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 6.0.2(22)

**设备行为差异：** 该枚举在Wearable、TV中无效果，使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)部分的相关说明。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 表示当前超级隐私模式状态为关。 |
| ON\_WHEN\_FOLDED | 1 | 表示当前超级隐私模式状态为仅折叠保护（展开时超级隐私不生效，折叠时生效）。 |
| ALWAYS\_ON | 2 | 表示当前超级隐私模式状态为始终保护。 |

## getSuperPrivacyMode

PhonePC/2in1TabletTVWearable

getSuperPrivacyMode(): Promise<SuperPrivacyMode>

获取当前超级隐私模式状态。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 6.0.2(22)

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回1006200005错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)部分的相关说明。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SuperPrivacyMode](devicesecurity-superprivacymode-api.md#superprivacymode)> | Promise对象，返回当前的超级隐私模式状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200002 | Internal error. |
| 1006200005 | This device is not support SuperPrivacy. |

**示例：**

```
1. import { superPrivacyMode } from '@kit.DeviceSecurityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = "SuperPrivacyModeTest";

7. let mode: superPrivacyMode.SuperPrivacyMode = superPrivacyMode.SuperPrivacyMode.OFF;
8. try {
9. mode = await superPrivacyMode.getSuperPrivacyMode();
10. hilog.info(DOMAIN, TAG, `Super privacy mode = ${mode}`);
11. } catch (err) {
12. hilog.error(DOMAIN, TAG, `call getSuperPrivacyMode interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
13. }
```

## on('superPrivacyModeChange')

PhonePC/2in1TabletTVWearable

on(type: 'superPrivacyModeChange', callback: Callback<SuperPrivacyMode>): void

订阅超级隐私模式状态变化事件。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 6.0.2(22)

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回1006200005错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)部分的相关说明。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 输入固定字符串'superPrivacyModeChange'，表示需要订阅'superPrivacyModeChange'。 |
| callback | Callback<[SuperPrivacyMode](devicesecurity-superprivacymode-api.md#superprivacymode)> | 是 | 回调函数，返回调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200001 | General error. |
| 1006200002 | Internal error. |
| 1006200005 | This device is not support SuperPrivacy. |

**示例：**

```
1. import { superPrivacyMode } from '@kit.DeviceSecurityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = "SuperPrivacyModeTest";

7. const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
8. hilog.info(DOMAIN, TAG, `super privacy mode changed, mode = ${superPrivacyMode}`);
9. }

11. hilog.info(DOMAIN, TAG, 'start register super privacy mode changed listener');
12. try {
13. superPrivacyMode.on('superPrivacyModeChange', superPrivacyChangedCallback);
14. hilog.info(DOMAIN, TAG, 'register super privacy mode change listener success');
15. } catch (err) {
16. hilog.error(DOMAIN, TAG, `register super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
17. }
```

## off('superPrivacyModeChange')

PhonePC/2in1TabletTVWearable

off(type: 'superPrivacyModeChange', callback?: Callback<SuperPrivacyMode>): void

取消订阅超级隐私模式状态变化事件。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 6.0.2(22)

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回1006200005错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)部分的相关说明。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 输入固定字符串'superPrivacyModeChange'，表示需要订阅的事件为'superPrivacyModeChange'。 |
| callback | Callback<[SuperPrivacyMode](devicesecurity-superprivacymode-api.md#superprivacymode)> | 否 | 回调函数，返回调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200001 | General error. |
| 1006200002 | Internal error. |
| 1006200005 | This device is not support SuperPrivacy. |

**示例：**

```
1. import { superPrivacyMode } from '@kit.DeviceSecurityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG = "SuperPrivacyModeTest";

7. const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
8. hilog.info(DOMAIN, TAG, `super privacy mode changed, mode = ${superPrivacyMode}`);
9. }

11. hilog.info(DOMAIN, TAG, 'start unregister super privacy mode changed listener');
12. try {
13. superPrivacyMode.off('superPrivacyModeChange', superPrivacyChangedCallback);
14. } catch (err) {
15. hilog.error(DOMAIN, TAG, `unregister super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
16. }
```
