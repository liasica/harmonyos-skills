---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-taas-api
title: TrustedAppService（可信应用服务）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > TrustedAppService（可信应用服务）
category: harmonyos-references
scraped_at: 2026-04-29T13:57:40+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:74e826a505e849c0c01795e3d6384eb427844d824565022822ef32ca52ea3ff3
---

本模块提供应用数据的安全证明服务，支持创建证明密钥、销毁证明密钥、初始化证明会话、结束证明会话和获取安全地理位置，能够为安全摄像头和安全地理位置功能提供安全证明能力，确保图像或位置数据未被篡改。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
```

## createAttestKey

PhonePC/2in1Tablet

createAttestKey(options: AttestOptions): Promise<void>

创建证明密钥，在证明密钥不存在或者不可用的条件下调用，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AttestOptions](devicesecurity-taas-api.md#attestoptions) | 是 | 生成证明密钥的参数，需要指定密钥类型和密钥大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-taas.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | argument is invalid. |
| 1011500001 | algorithm param is invalid. |
| 1011500002 | algorithm param is missing. |
| 1011500003 | create attestation key failed. |
| 1011500004 | create anonymous certificate failed. |
| 1011500005 | operating file failed. |
| 1011500006 | IPC communication failed. |

**示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let properties: Array<trustedAppService.AttestParam> = [
6. {
7. tag: trustedAppService.AttestTag.ATTEST_TAG_ALGORITHM,
8. value: trustedAppService.AttestKeyAlg.ATTEST_ALG_ECC
9. },
10. {
11. tag: trustedAppService.AttestTag.ATTEST_TAG_KEY_SIZE,
12. value: trustedAppService.AttestKeySize.ATTEST_ECC_KEY_SIZE_256
13. }
14. ];
15. let options: trustedAppService.AttestOptions = {
16. properties: properties,
17. };
18. await trustedAppService.createAttestKey(options)
19. .then(
20. (): void => {
21. hilog.info(0x0000, 'testTag', 'Succeeded in creating attest key');
22. }
23. ).catch(
24. (error: BusinessError): void => {
25. let err = error as BusinessError;
26. hilog.error(0x0000, 'testTag', `Failed to create attest key, code:${err.code}, message:${err.message}`);
27. });
```

## AttestOptions

PhonePC/2in1Tablet

[createAttestKey](devicesecurity-taas-api.md#createattestkey)接口的请求参数。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| properties | Array<[AttestParam](devicesecurity-taas-api.md#attestparam)> | 否 | 否 | 开发者应用传入的用于生成证明密钥的配置信息。 |

## AttestParam

PhonePC/2in1Tablet

[AttestOptions](devicesecurity-taas-api.md#attestoptions)配置信息的内容条目。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tag | [AttestTag](devicesecurity-taas-api.md#attesttag) | 否 | 否 | 开发者应用传入的标签，用于生成证明密钥的配置信息。 |
| value | boolean|number|bigint|Uint8Array | 否 | 否 | 开发者应用传入的标签对应的值，用于生成证明密钥的配置信息。  **boolean：**  预留参数，暂未使用。  **number：**  1）tag为ATTEST\_TAG\_ALGORITHM，其值为[AttestKeyAlg](devicesecurity-taas-api.md#attestkeyalg)类型。  2）tag为ATTEST\_TAG\_KEY\_SIZE，其值为[AttestKeySize](devicesecurity-taas-api.md#attestkeysize)类型。  3）tag为ATTEST\_TAG\_DEVICE\_TYPE，其值为[AttestType](devicesecurity-taas-api.md#attesttype)类型。  **bigint：**  tag为ATTEST\_TAG\_DEVICE\_ID，其值为设备ID，取值范围int64类型的随机值。  **Uint8Array：**  预留参数，暂未使用。 |

## AttestTag

PhonePC/2in1Tablet

配置信息标签类型，使用[AttestTagType](devicesecurity-taas-api.md#attesttagtype)扩展定义。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| ATTEST\_TAG\_INVALID | AttestTagType.ATTEST\_TAG\_TYPE\_INVALID|0 | 不合法标签。 |
| ATTEST\_TAG\_ALGORITHM | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|1 | 算法标签。 |
| ATTEST\_TAG\_KEY\_SIZE | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|2 | 密钥大小标签。 |
| ATTEST\_TAG\_DEVICE\_TYPE | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|3 | 设备类型标签。 |
| ATTEST\_TAG\_DEVICE\_ID | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|4 | 设备序列号标签。 |

## AttestTagType

PhonePC/2in1Tablet

标签类型定义，用于区分数据类型。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| ATTEST\_TAG\_TYPE\_INVALID | 0<<28 | 不合法标签类型。 |
| ATTEST\_TAG\_TYPE\_INT | 1<<28 | INT类型。 |
| ATTEST\_TAG\_TYPE\_UINT | 2<<28 | UINT类型。 |
| ATTEST\_TAG\_TYPE\_ULONG | 3<<28 | ULONG类型。 |
| ATTEST\_TAG\_TYPE\_BOOL | 4<<28 | BOOL类型。 |
| ATTEST\_TAG\_TYPE\_BYTES | 5<<28 | BYTES类型。 |

## AttestKeyAlg

PhonePC/2in1Tablet

证明密钥算法类型。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| ATTEST\_ALG\_ECC | 1 | ECC算法类型。 |

## AttestKeySize

PhonePC/2in1Tablet

证明密钥长度。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| ATTEST\_ECC\_KEY\_SIZE\_256 | 256 | 证明密钥长度，256位。 |
| ATTEST\_ECC\_KEY\_SIZE\_384 | 384 | 证明密钥长度，384位。 |

## destroyAttestKey

PhonePC/2in1Tablet

destroyAttestKey(): Promise<void>

销毁证明密钥，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-taas.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 1011500005 | operating file failed. |
| 1011500006 | IPC communication failed. |
| 1011500007 | item not found. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. await trustedAppService.destroyAttestKey().then(
6. (): void => {
7. hilog.info(0x0000, 'testTag', 'Succeeded in destroying attest key');
8. }
9. ).catch(
10. (error: BusinessError): void => {
11. let err = error as BusinessError;
12. hilog.error(0x0000, 'testTag', `Failed to destroy attest key, code:${err.code}, message:${err.message}`);
13. }
14. );
```

## initializeAttestContext

PhonePC/2in1Tablet

initializeAttestContext(userData: string, options: AttestOptions): Promise<AttestReturnResult>

初始化证明会话，在创建证明密钥成功后使用，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| userData | string | 是 | 打开证明会话的参数，传入的用户数据，长度在16到127字节之间。 |
| options | [AttestOptions](devicesecurity-taas-api.md#attestoptions) | 是 | 打开证明会话的参数，需要指定设备类型和设备ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AttestReturnResult](devicesecurity-taas-api.md#attestreturnresult)> | 生成的匿名证书链。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-taas.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | argument is invalid. |
| 1011500002 | param is missing. |
| 1011500005 | operating file failed. |
| 1011500006 | IPC communication failed. |
| 1011500007 | item not found. |
| 1011500008 | anonymous certificate verify failed. |
| 1011500009 | anonymous certificate has expired. |
| 1011500010 | get attestation key failed. |
| 1011500011 | initialize secure camera failed. |

## AttestType

PhonePC/2in1Tablet

证明会话类型。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| ATTEST\_TYPE\_LOCATION | 1 | 安全地理位置类型。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_TYPE\_CAMERA | 2 | 安全摄像头类型。 |
| ATTEST\_TYPE\_SECIMAGE\_PROCESS | 3 | 安全图像处理类型。起始版本：5.1.0(18)。 |

## AttestReturnResult

PhonePC/2in1Tablet

[initializeAttestContext](devicesecurity-taas-api.md#initializeattestcontext)接口的返回值。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| certChains | Array<string> | 否 | 否 | 打开证明会话成功之后返回的匿名证书链 |

**示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // device_id 需要指定为 Bigint类型
6. let device_id_tt = 12581;
7. // userdata的长度需要超过16个Bytes，最大长度为127 Bytes
8. let user_data = "test_user_data_0000"
9. let properties2: Array<trustedAppService.AttestParam> = [
10. {
11. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
12. value: trustedAppService.AttestType.ATTEST_TYPE_LOCATION
13. },
14. {
15. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_ID,
16. value: BigInt(device_id_tt)
17. },
18. ];
19. let options2: trustedAppService.AttestOptions = {
20. properties: properties2,
21. };
22. await trustedAppService.initializeAttestContext(user_data, options2).then(
23. (returnResult: trustedAppService.AttestReturnResult): void => {
24. let chains = returnResult.certChains as Array<string>;
25. for (const item of chains) {
26. hilog.info(0x0000, 'testTag', 'item: ' + item);
27. };
28. }
29. ).catch(
30. (error: BusinessError): void => {
31. let err = error as BusinessError;
32. hilog.error(0x0000, 'testTag', `Failed to initialize attest context, code:${err.code}, message:${err.message}`);
33. }
34. );
```

## AttestExceptionErrCode

PhonePC/2in1Tablet

可信应用服务中创建证明密钥、销毁证明密钥、初始化证明会话、结束证明会话、获取当前安全位置等接口的错误码。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| ATTEST\_ERROR\_NO\_PERMISSION | 201 | 权限校验失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_ILLEGAL\_ARGUMENT | 401 | 参数检查失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_INVALID\_ALG\_ARGUMENT | 1011500001 | 无效的算法参数。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_MISSING\_ARGUMENT | 1011500002 | 参数传入不足。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_KEY\_GENERATOR\_FAILED | 1011500003 | 密钥生成失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_CERTS\_CREATION\_FAILED | 1011500004 | 证书创建失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_FILE\_OPERATION\_FAILED | 1011500005 | 文件操作失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_COMMUNICATION\_FAILED | 1011500006 | IPC通信失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_ITEM\_NOT\_FOUND | 1011500007 | 密钥不存在。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_CERTS\_VERIFICATION\_FAILED | 1011500008 | 证书校验失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_CERTS\_EXPIRED | 1011500009 | 证书已过期。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_KEY\_NOT\_MATCHED | 1011500010 | 密钥不匹配。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_SECURE\_CAMERA\_INITIALIZATION\_FAILED | 1011500011 | 安全相机初始化失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_CONTEXT\_BAD\_STATE | 1011500012 | 证明会话上下文异常。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_KEY\_EXPIRED | 1011500013 | 密钥已过期。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_LOCATION\_SERVICE\_UNAVAILABLE | 1011500014 | 位置服务不可用。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_LOCATION\_SWITCH\_OFF | 1011500015 | 位置信息开关关闭。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_LOCATION\_FAILED | 1011500016 | 位置信息获取失败。  **元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。 |
| ATTEST\_ERROR\_SIGNATURE\_VERIFICATION\_FAILED | 1011500017 | 签名验签失败。  **起始版本：5.1.0(18)。** |
| ATTEST\_ERROR\_SECIMAGE\_PROCESS\_FAILED | 1011500018 | 安全图像处理失败。  **起始版本：5.1.0(18)。** |

## finalizeAttestContext

PhonePC/2in1Tablet

finalizeAttestContext(options: AttestOptions): Promise<void>

结束证明会话，在结束安全证明服务后调用，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| options | [AttestOptions](devicesecurity-taas-api.md#attestoptions) | 是 | 关闭证明会话的参数，需要指定设备类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-taas.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | argument is invalid. |
| 1011500002 | param is missing. |
| 1011500006 | IPC communication failed. |
| 1011500007 | item not found. |

**示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let properties: Array<trustedAppService.AttestParam> = [
6. {
7. tag: trustedAppService.AttestTag.ATTEST_TAG_DEVICE_TYPE,
8. value: trustedAppService.AttestType.ATTEST_TYPE_CAMERA
9. }
10. ];
11. let options: trustedAppService.AttestOptions = {
12. properties: properties,
13. };
14. await trustedAppService.finalizeAttestContext(options).then(
15. (): void => {
16. hilog.info(0x0000, 'testTag', 'Succeeded in finalizing attest context');
17. }
18. ).catch(
19. (error: BusinessError): void => {
20. let err = error as BusinessError;
21. hilog.error(0x0000, 'testTag', `Failed to finalize attest context, code:${err.code}, message:${err.message}`);
22. }
23. );
```

## getCurrentSecureLocation

PhoneTablet

getCurrentSecureLocation(timeout : number, priority: LocatingPriority): Promise<SecureLocation>

获取当前安全位置，使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Location

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| timeout | number | 是 | 单次位置请求的超时时间，单位是毫秒（milliseconds），最小为1000毫秒。取值范围为大于等于1000。 |
| priority | [LocatingPriority](devicesecurity-taas-api.md#locatingpriority) | 是 | 获取安全地理位置的优先级策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SecureLocation](devicesecurity-taas-api.md#securelocation)> | 获取的安全位置 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-taas.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | has no permission. |
| 401 | argument is invalid. |
| 1011500012 | attestation context not initialized. |
| 1011500013 | attestation key has expired. |
| 1011500014 | location service is unavailable. |
| 1011500015 | The location switch is off. |
| 1011500016 | Failed to obtain the secure geographical location. |

## LocatingPriority

PhoneTablet

获取安全地理位置的优先级策略。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Location

**起始版本：** 5.0.0(12)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| PRIORITY\_ACCURACY | 0 | 精度优先，保证获取最高精度。 |
| PRIORITY\_LOCATING\_SPEED | 1 | 速度优先，保证位置获取速度。 |

## SecureLocation

PhoneTablet

获取的安全地理位置。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Location

**起始版本：** 5.0.0(12)

| **名称** | 类型 | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| originalLocation | [Location](devicesecurity-taas-api.md#location) | 否 | 否 | 地理位置信息。 |
| userData | String | 否 | 否 | 用户数据，长度在16到127字节之间。 |
| signature | String | 否 | 否 | 签名结果。  当证明密钥长度为256位时，signature长度为96字节；  当证明密钥长度为384位时，signature长度为136或者140字节。 |

## Location

PhoneTablet

获取的安全地理位置信息。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.TrustedAppService.Location

**起始版本：** 5.0.0(12)

| **名称** | 类型 | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 纬度，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 |
| longitude | number | 否 | 否 | 经度，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 |
| altitude | number | 否 | 否 | 高度，单位米。 |
| accuracy | number | 否 | 否 | 精度，单位米，取值大于等于0。 |
| timestamp | number | 否 | 否 | 时间戳，单位毫秒，取值大于等于0。 |

**示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. try {
6. const secureLocation = await trustedAppService.getCurrentSecureLocation(3000, trustedAppService.LocatingPriority.PRIORITY_LOCATING_SPEED);
7. hilog.info(0x0000, 'testTag', 'Succeeded in getting secure location, result = ${JSON.stringify(secureLocation)}');
8. } catch (error) {
9. let err = error as BusinessError;
10. hilog.error(0x0000, 'testTag', `Failed to get secure location, code:${err.code}, message:${err.message}`);
11. }
```

## procSecImageTransform

PhonePC/2in1Tablet

procSecImageTransform(srcSecImage: ArrayBuffer, procParams: SecImageProcParamsArray): Promise<SecImageBuffer>

处理安全图像压缩、裁剪操作，使用Promise异步回调。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**设备行为差异：** 该接口在支持安全摄像头能力的Phone、Tablet、PC/2in1均可正常调用，在不支持安全摄像头能力的Phone、Tablet、PC/2in1设备及其他设备类型中统一返回业务错误码1011500011。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| srcSecImage | ArrayBuffer | 是 | 安全相机返回签名后的安全图像。 |
| procParams | [SecImageProcParamsArray](devicesecurity-taas-api.md#secimageprocparamsarray) | 是 | 安全图像压缩、裁剪处理的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SecImageBuffer](devicesecurity-taas-api.md#secimagebuffer)> | 返回压缩、裁剪处理后签名的安全图像 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-taas.md) **。**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The app profile does not have the required permission. Please refer to the "Enabling Device Security Service" section in the Device Security Kit development guide. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1011500011 | secure image processing is not supported. |
| 1011500012 | attestation context not initialized. |
| 1011500013 | attestation key has expired. |
| 1011500017 | signature verification failed. |
| 1011500018 | secure image process failed. |

## SecImageProcParamsArray

PhonePC/2in1Tablet

[procSecImageTransform](devicesecurity-taas-api.md#procsecimagetransform)接口的请求参数。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| properties | Array<[SecImageProcParams](devicesecurity-taas-api.md#secimageprocparams)> | 否 | 否 | 开发者应用传入的用于安全图像压缩、裁剪处理的配置信息。 |

## SecImageProcParams

PhonePC/2in1Tablet

[SecImageProcParamsArray](devicesecurity-taas-api.md#secimageprocparamsarray)配置信息的内容条目。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| tag | [SecImageProcTag](devicesecurity-taas-api.md#secimageproctag) | 否 | 否 | 开发者应用传入的标签，用于安全图像压缩、裁剪处理的配置信息。 |
| value | number | [CropRegion](devicesecurity-taas-api.md#cropregion) | 否 | 否 | 开发者应用传入的标签对应的值，用于安全图像压缩、裁剪处理的配置信息。  **number：**  1）tag为SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT或者  SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT  ，其值为[SecImageProcParamsArray](devicesecurity-taas-api.md#secimageprocparamsarray)类型；  2）tag为SECIMAGE\_TAG\_PROC\_OPERATION，其值为[SecImageProcOperation](devicesecurity-taas-api.md#secimageprocoperation)类型；  3）tag为SECIMAGE\_TAG\_COMPRESSION\_QUALITY，其值为1到100之间；  **CropRegion：**  tag为SECIMAGE\_TAG\_CROP\_REGION，其值为[CropRegion](devicesecurity-taas-api.md#cropregion)类型。 |

## SecImageProcTag

PhonePC/2in1Tablet

安全图像压缩、裁剪处理的配置信息标签类型，使用[AttestTagType](devicesecurity-taas-api.md#attesttagtype)扩展定义。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.1.0(18)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| SECIMAGE\_TAG\_INVALID | AttestTagType.ATTEST\_TAG\_TYPE\_INVALID|0 | 不合法标签。 |
| SECIMAGE\_TAG\_SRC\_IMAGE\_FORMAT | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|1 | 原始安全图像的格式。 |
| SECIMAGE\_TAG\_DEST\_IMAGE\_FORMAT | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|2 | 压缩、裁剪处理后的安全图像的格式。 |
| SECIMAGE\_TAG\_PROC\_OPERATION | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|3 | 安全图像的处理命令，支持：压缩命令、裁剪命令、压缩并裁剪命令。 |
| SECIMAGE\_TAG\_COMPRESSION\_QUALITY | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|4 | 安全图像压缩处理的压缩质量。 |
| SECIMAGE\_TAG\_CROP\_REGION | AttestTagType.ATTEST\_TAG\_TYPE\_UINT|5 | 安全图像裁剪处理的裁剪区域。 |

## SecImageProcOperation

PhonePC/2in1Tablet

安全图像的处理命令。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.1.0(18)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| SECIMAGE\_COMPRESSION | 0 | 安全图像压缩命令。 |
| SECIMAGE\_CROPPING | 1 | 安全图像裁剪命令。 |
| SECIMAGE\_COMPRESSION\_AND\_CROPPING | 2 | 安全图像压缩并裁剪命令。 |

## SecImageProcFormat

PhonePC/2in1Tablet

安全图像的格式。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.1.0(18)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| SECIMAGE\_FORMAT\_INVALID | 0 | 无效的安全图像格式。 |
| SECIMAGE\_FORMAT\_YUV\_NV21 | 1 | YUV420 NV21格式的安全图像。输入原始安全图像格式，以及裁剪命令返回的安全图像格式均为SECIMAGE\_FORMAT\_YUV\_NV21。 |
| SECIMAGE\_FORMAT\_JPEG | 2 | JPEG格式的安全图像。压缩命令、压缩并裁剪命令返回的安全图像格式均为SECIMAGE\_FORMAT\_JPEG。 |

## CropRegion

PhonePC/2in1Tablet

安全图像裁剪处理的裁剪区域。裁剪区域参数作用如下图所示。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 裁剪区域左上角点在水平方向（横向）上相对于整个图像左边界的偏移量，取值范围在 0 到 640 之间的偶数。单位是像素（pixel）。 |
| y | number | 否 | 否 | 裁剪区域左上角点在垂直方向（纵向）上相对于整个图像上边界的偏移量，取值范围在 0 到 480 之间的偶数。单位是像素（pixel）。 |
| width | number | 否 | 否 | 裁剪区域的宽度，即横向的长度，取值范围在 0 到 640 之间的偶数，且需满足 x 与 width 的和不大于 640。单位是像素（pixel）。 |
| height | number | 否 | 否 | 裁剪区域的高度，即纵向的长度，取值范围在 0 到 480 之间的偶数，且需满足 y 与 height 的和不大于 480。单位是像素（pixel）。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/pFZthqy2QISqUbE5ZY9Y_Q/zh-cn_image_0000002589326927.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055739Z&HW-CC-Expire=86400&HW-CC-Sign=49188E5CF0B68472C90B0842ED62E8CA1D01F89C458FED7B726E318B2B2094FA)

## SecImageBuffer

PhonePC/2in1Tablet

获得压缩、裁剪处理后签名的安全图像。

**系统能力：** SystemCapability.Security.TrustedAppService.Core

**起始版本：** 5.1.0(18)

| **名称** | 类型 | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| secImage | ArrayBuffer | 否 | 否 | 返回压缩、裁剪处理后签名的安全图像。 |

**安全图像压缩示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

7. let properties: Array<trustedAppService.SecImageProcParams> = [
8. {
9. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
10. value: trustedAppService.SecImageProcOperation.SECIMAGE_COMPRESSION,
11. },
12. {
13. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
14. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
15. },
16. {
17. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
18. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_JPEG, // 安全图像压缩命令返回的图像格式为：JPEG 格式
19. },
20. {
21. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_COMPRESSION_QUALITY,
22. value: 90, // 实际使用请替换为业务场景需要的压缩质量
23. },
24. ];
25. let procParams: trustedAppService.SecImageProcParamsArray = {
26. properties: properties,
27. };
28. await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
29. (returnResult: trustedAppService.SecImageBuffer): void => {
30. let returnSecImageBuffer = returnResult.secImage;
31. }
32. ).catch(
33. (error: BusinessError): void => {
34. let err = error as BusinessError;
35. hilog.error(0x0000, 'testTag', `Failed to process secureImage compression, code:${err.code}, message:${err.message}`);
36. }
37. );
```

**安全图像裁剪示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

7. let properties: Array<trustedAppService.SecImageProcParams> = [
8. {
9. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
10. value: trustedAppService.SecImageProcOperation.SECIMAGE_CROPPING,
11. },
12. {
13. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
14. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩、裁剪命令输入的原始图像格式都为：YUV420 NV21 格式
15. },
16. {
17. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
18. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21, // 安全图像压缩命令返回的图像格式为：JPEG 格式
19. },
20. {
21. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_CROP_REGION,
22. value: { x : 0, y ：0, width : 320, height : 240 }, // 实际使用请替换为业务场景需要的裁剪区域范围
23. },
24. ];
25. let procParams: trustedAppService.SecImageProcParamsArray = {
26. properties: properties,
27. };
28. await trustedAppService.procSecImageTransform(srcSecImageBuffer, procParams).then(
29. (returnResult: trustedAppService.SecImageBuffer): void => {
30. let returnSecImageBuffer = returnResult.secImage;
31. }
32. ).catch(
33. (error: BusinessError): void => {
34. let err = error as BusinessError;
35. hilog.error(0x0000, 'testTag', `Failed to process secureImage cropping, code:${err.code}, message:${err.message}`);
36. }
37. );
```

**安全图像压缩并裁剪示例：**

```
1. import { trustedAppService } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const srcSecImageBuffer = new  ArrayBuffer(461844);// 实际使用请替换为Camera Kit获取到的安全图像buffer

7. let properties: Array<trustedAppService.SecImageProcParams> = [
8. {
9. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_PROC_OPERATION,
10. value: trustedAppService.SecImageProcOperation.SECIMAGE_COMPRESSION_AND_CROPPING,
11. },
12. {
13. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_SRC_IMAGE_FORMAT,
14. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_YUV_NV21,
15. },
16. {
17. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_DEST_IMAGE_FORMAT,
18. value: trustedAppService.SecImageProcFormat.SECIMAGE_FORMAT_JPEG,
19. },
20. {
21. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_COMPRESSION_QUALITY,
22. value: 90, // 实际使用请替换为业务场景需要的压缩质量
23. },
24. {
25. tag: trustedAppService.SecImageProcTag.SECIMAGE_TAG_CROP_REGION,
26. value: { x : 0, y ：0, width : 320, height : 240 }, // 实际使用请替换为业务场景需要的裁剪区域范围
27. },
28. ];
29. let procParams: trustedAppService.SecImageProcParamsArray = {
30. properties: properties,
31. };
32. await trustedAppService.procSecImageTransform(srcSecImageBuffer, options).then(
33. (returnResult: trustedAppService.SecImageBuffer): void => {
34. let returnSecImageBuffer = returnResult.secImage;
35. }
36. ).catch(
37. (error: BusinessError): void => {
38. let err = error as BusinessError;
39. hilog.error(0x0000, 'testTag', `Failed to process secureImage cropping, code:${err.code}, message:${err.message}`);
40. }
41. );
```
