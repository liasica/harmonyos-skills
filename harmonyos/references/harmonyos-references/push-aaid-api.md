---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/push-aaid-api
title: AAID（应用匿名标识符）
breadcrumb: API参考 > 应用服务 > Push Kit（推送服务） > ArkTS API > AAID（应用匿名标识符）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb78068d7622840fbc2edd6f7050cb8b47211b3180e2cc30c969e08d8aff4491
---

本模块提供了开发者获取和删除应用匿名标识符（AAID，Anonymous Application Identifier）的能力。AAID用于标识应用身份。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AAID } from '@kit.PushKit';
```

## AAID.getAAID

PhonePC/2in1TabletTVWearable

getAAID(callback: AsyncCallback<string>): void

获取AAID，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当获取AAID成功，err为undefined，data为获取到的AAID，字符长度为36；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```
1. import { AAID } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // data为获取的应用匿名标识符
7. AAID.getAAID((err: BusinessError, data: string) => {
8. if (err) {
9. hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
10. } else {
11. hilog.info(0x0000, 'testTag', 'Succeeded in getting AAID');
12. }
13. });
14. } catch (err) {
15. let e: BusinessError = err as BusinessError;
16. hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
17. }
```

## AAID.getAAID

PhonePC/2in1TabletTVWearable

getAAID(): Promise<string>

获取AAID，使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回AAID，字符长度为36。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```
1. import { AAID } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. // data为获取的应用匿名标识符
7. AAID.getAAID().then((data: string) => {
8. hilog.info(0x0000, 'testTag', 'Succeeded in getting AAID');
9. }).catch((err: BusinessError) => {
10. hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
11. });
12. } catch (err) {
13. let e: BusinessError = err as BusinessError;
14. hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
15. }
```

## AAID.deleteAAID

PhonePC/2in1TabletTVWearable

deleteAAID(callback: AsyncCallback<void>): void

删除AAID，使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除AAID成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```
1. import { AAID } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. AAID.deleteAAID((err: BusinessError) => {
7. if (err) {
8. hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
9. } else {
10. hilog.info(0x0000, 'testTag', 'Succeeded in deleting AAID.');
11. }
12. });
13. } catch (err) {
14. let e: BusinessError = err as BusinessError;
15. hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', e.code, e.message);
16. }
```

## AAID.deleteAAID

PhonePC/2in1TabletTVWearable

deleteAAID(): Promise<void>

删除AAID，使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Push.PushService

**设备行为差异：** 对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](push-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900006 | Failed to connect to the AAID service. |
| 1000900007 | Internal error of the AAID service. |

**示例：**

```
1. import { AAID } from '@kit.PushKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. try {
6. AAID.deleteAAID().then(() => {
7. hilog.info(0x0000, 'testTag', 'Succeeded in deleting AAID');
8. }).catch((err: BusinessError) => {
9. hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
10. });
11. } catch (err) {
12. let e: BusinessError = err as BusinessError;
13. hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', e.code, e.message);
14. }
```
