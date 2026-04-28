---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/onlineauthentication-soter-api
title: SOTER
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > ArkTS API > SOTER
category: harmonyos-references
scraped_at: 2026-04-28T08:07:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a97b6f86d1e5fd7611c4b0d63bdb07d20eeb8487e730de27e7292677ac936640
---

SOTER提供移动端免密身份认证能力，支持使用SOTER协议的应用实现免密登录，免密支付等业务场景。

支持的设备类型为：Phone, PC/2in1, Tablet

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { soter } from '@kit.OnlineAuthenticationKit'
```

## KeyType

PhonePC/2in1Tablet

密钥选型，为枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ECC\_P256 | 0 | 密钥选型ECC P256。 |

## SignedResult

PhonePC/2in1Tablet

表示签名结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | Uint8Array | 是 | 原始报文。 |
| signature | Uint8Array | 是 | 原始报文的签名。 |
| saltLength | number | 是 | 盐值长度，小于U32类型最大值。 |

## getVersionSync

PhonePC/2in1Tablet

getVersionSync(): string

该接口用于获取SOTER免密认证API接口的版本号，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回SOTER免密认证的API接口版本号。最大长度64个字符。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let res: string = soter.getVersionSync();// 开发者处理结果
```

## getVersion

PhonePC/2in1Tablet

getVersion(): Promise<string>

该接口用于获取SOTER免密认证API接口的版本号，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回SOTER免密认证的API接口版本号。最大长度64个字符。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let resPromise: Promise<string> = soter.getVersion();
4. resPromise.then(result => {
5. console.info('Succeeded in doing getVersion.');
6. // 开发者处理结果
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to call getVersion. Code: ${error.code}, message: ${error.message}`);
9. });
```

## hasAppSecureKeySync

PhonePC/2in1Tablet

hasAppSecureKeySync(keyType: KeyType): boolean

该接口用于查询应用密钥的生成状态，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，当前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 同步返回应用密钥的生成状态。true代表已生成，false代表未生成。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

3. // 查询应用密钥生成状态 同步
4. let hasAppSecureKey: boolean = soter.hasAppSecureKeySync(keyType);
```

## hasAppSecureKey

PhonePC/2in1Tablet

hasAppSecureKey(keyType: KeyType): Promise<boolean>

该接口用于查询应用密钥的生成状态，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回应用密钥的生成状态。true代表已生成，false代表未生成。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

5. // 异步查询应用密钥的生成状态
6. let hasAppSecureKeyPromise: Promise<boolean> = soter.hasAppSecureKey(keyType);
7. hasAppSecureKeyPromise.then(result => {
8. console.info('Succeeded in doing hasAppSecureKey.');
9. // 开发者处理结果
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to call hasAppSecureKey. Code: ${error.code}, message: ${error.message}`);
12. });
```

## generateAppSecureKeySync

PhonePC/2in1Tablet

generateAppSecureKeySync(keyType: KeyType): Uint8Array

该接口用于生成App应用密钥，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回App应用密钥。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

3. // 生成应用密钥
4. let appSecureKey: Uint8Array = soter.generateAppSecureKeySync(keyType);
```

## generateAppSecureKey

PhonePC/2in1Tablet

generateAppSecureKey(keyType: KeyType): Promise<Uint8Array>

该接口用于生成App应用密钥，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256，其余枚举值均报错。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回App应用密钥。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

5. // 生成应用密钥
6. let appSecureKeyPromise: Promise<Uint8Array> = soter.generateAppSecureKey(keyType);
7. appSecureKeyPromise.then(result => {
8. console.info('Succeeded in doing generateAppSecureKey.');
9. // 开发者处理结果
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to call generateAppSecureKey. Code: ${error.code}, message: ${error.message}`);
12. });
```

## getAppSecureKeySync

PhonePC/2in1Tablet

getAppSecureKeySync(keyType: KeyType): Uint8Array

该接口用于获取App应用密钥，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回App应用密钥。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

3. // 获取应用密钥 同步
4. let appSecureKey: Uint8Array = soter.getAppSecureKeySync(keyType);
```

## getAppSecureKey

PhonePC/2in1Tablet

getAppSecureKey(keyType: KeyType): Promise<Uint8Array>

该接口用于获取App应用密钥，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回App应用密钥。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256

5. // 获取应用密钥 Promise
6. let appSecureKeyPromise: Promise<Uint8Array> = soter.getAppSecureKey(keyType);
7. appSecureKeyPromise.then(result => {
8. console.info('Succeeded in doing getAppSecureKey.');
9. // 开发者处理结果
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to call getAppSecureKey. Code: ${error.code}, message: ${error.message}`);
12. });
```

## hasAuthKeySync

PhonePC/2in1Tablet

hasAuthKeySync(keyAlias: string, keyType: KeyType): boolean

该接口用于查询AuthKey生成状态，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 同步返回AuthKey生成状态，true代表已生成，false代表未生成。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
2. let keyAlias: string = 'keyAlias'; // 开发者自定义索引

4. // 查询AuthKey开通状态 同步
5. let hasAuthKey: boolean = soter.hasAuthKeySync(keyAlias, keyType);
```

## hasAuthKey

PhonePC/2in1Tablet

hasAuthKey(keyAlias: string, keyType: KeyType): Promise<boolean>

该接口用于查询AuthKey生成状态，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回查询AuthKey生成状态。true代表已生成，false代表未生成。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
4. let keyAlias: string = 'keyAlias';

6. // 查询AuthKey生成状态 Promise
7. let hasAuthKeyPromise: Promise<boolean> = soter.hasAuthKey(keyAlias, keyType);
8. hasAuthKeyPromise.then(result => {
9. console.info('Succeeded in doing hasAuthKey.');
10. // 开发者处理结果
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to call hasAuthKey. Code: ${error.code}, message: ${error.message}`);
13. });
```

## generateAuthKeySync

PhonePC/2in1Tablet

generateAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult

该接口用于生成AuthKey，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SignedResult](onlineauthentication-soter-api.md#signedresult) | 返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
2. let keyAlias: string = 'keyAlias';

4. // 生成AuthKey
5. let signedResult: soter.SignedResult = soter.generateAuthKeySync(keyAlias, keyType);
6. let authKey: Uint8Array = signedResult?.signature; // 开发者使用结果AuthKey
```

## generateAuthKey

PhonePC/2in1Tablet

generateAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>

该接口用于生成AuthKey，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SignedResult](onlineauthentication-soter-api.md#signedresult)> | Promise对象，返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
4. let keyAlias: string = 'keyAlias';

6. // 生成AuthKey
7. let authKeyPromise: Promise<soter.SignedResult> = soter.generateAuthKey(keyAlias, keyType);
8. authKeyPromise.then(result => {
9. console.info('Succeeded in doing generateAuthKey.');
10. // 开发者处理结果
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to call generateAuthKey. Code: ${error.code}, message: ${error.message}`);
13. });
```

## getAuthKeySync

PhonePC/2in1Tablet

getAuthKeySync(keyAlias: string, keyType: KeyType): SignedResult

该接口用于获取AuthKey，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SignedResult](onlineauthentication-soter-api.md#signedresult) | 返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
2. let keyAlias: string = 'keyAlias';

4. // 使用同步接口获取AuthKey
5. let signedResult: soter.SignedResult = soter.getAuthKeySync(keyAlias, keyType);
6. let authKey: Uint8Array = signedResult.message; // 开发者使用结果AuthKey
```

## getAuthKey

PhonePC/2in1Tablet

getAuthKey(keyAlias: string, keyType: KeyType): Promise<SignedResult>

该接口用于获取AuthKey，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| keyType | [KeyType](onlineauthentication-soter-api.md#keytype) | 是 | 密钥选型，目前只支持 soter.KeyType.ECC\_P256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SignedResult](onlineauthentication-soter-api.md#signedresult)> | Promise对象，返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 密钥选型，当前只支持ECC_P256
4. let keyAlias: string = 'keyAlias';

6. // 获取AuthKey Promise
7. let authKeyPromise: Promise<soter.SignedResult> = soter.getAuthKey(keyAlias, keyType);
8. authKeyPromise.then(result => {
9. console.info('Succeeded in doing getAuthKey.');
10. // 开发者处理结果
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to call getAuthKey. Code: ${error.code}, message: ${error.message}`);
13. });
```

## generateChallengeSync

PhonePC/2in1Tablet

generateChallengeSync(keyAlias: string): Uint8Array

该接口用于生成Challenge，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回生成的Challenge。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyAlias: string = 'keyAlias';

3. // 生成Challenge
4. let challenge: Uint8Array = soter.generateChallengeSync(keyAlias);
```

## generateChallenge

PhonePC/2in1Tablet

generateChallenge(keyAlias: string): Promise<Uint8Array>

该接口用于生成Challenge，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回生成的Challenge。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyAlias: string = 'keyAlias';

5. // 生成Challenge
6. let challengePromise: Promise<Uint8Array> = soter.generateChallenge(keyAlias);
7. challengePromise.then(result => {
8. console.info('Succeeded in doing generateChallenge.');
9. // 开发者处理结果
10. }).catch((error: BusinessError) => {
11. console.error(`Failed to call generateChallenge. Code: ${error.code}, message: ${error.message}`);
12. });
```

## signWithAuthKeySync

PhonePC/2in1Tablet

signWithAuthKeySync(keyAlias: string, authToken: Uint8Array, info: string): SignedResult

该接口用于SOTER免密认证，同步返回签名的报文。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| authToken | Uint8Array | 是 | 用户身份认证通过的凭证（通过用户认证模块可获取，调用@ohos.userIAM.userAuth的getUserAuthInstance）。 |
| info | string | 是 | 开发者自定义信息，info最大长度为511字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SignedResult](onlineauthentication-soter-api.md#signedresult) | 返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. let keyAlias: string = 'keyAlias';
2. // 开发者调用@ohos.userIAM.userAuth的getUserAuthInstance获取authToken；authToken需要开发者替换为真实入参。
3. let authToken = new Uint8Array([0]);
4. let info = '';
5. let authResult: soter.SignedResult = soter.signWithAuthKeySync(keyAlias, authToken, info)
```

## signWithAuthKey

PhonePC/2in1Tablet

signWithAuthKey(keyAlias: string, authToken: Uint8Array, info: string): Promise<SignedResult>

该接口用于SOTER免密认证，使用Promise异步回调返回签名的报文。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |
| authToken | Uint8Array | 是 | 用户身份认证通过的凭证（通过用户认证模块可获取，调用@ohos.userIAM.userAuth的getUserAuthInstance）。 |
| info | string | 是 | 开发者自定义信息，info最大长度为511字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SignedResult](onlineauthentication-soter-api.md#signedresult)> | Promise对象，返回SignedResult对象。其中signature为返回报文的签名，message为返回报文的原文，saltLength为加密盐值长度。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyAlias: string = 'keyAlias';
4. // 开发者调用@ohos.userIAM.userAuth的getUserAuthInstance获取authToken；authToken需要开发者替换为真实入参。
5. let authToken = new Uint8Array([0]);
6. let info = '';
7. let authResultPromise: Promise<soter.SignedResult> = soter.signWithAuthKey(keyAlias, authToken, info);
8. authResultPromise.then(result => {
9. console.info('Succeeded in doing signWithAuthKey.');
10. // 开发者处理结果
11. }).catch((error: BusinessError) => {
12. console.error(`Failed to call signWithAuthKey. Code: ${error.code}, message: ${error.message}`);
13. });
```

## deleteAuthKeySync

PhonePC/2in1Tablet

deleteAuthKeySync(keyAlias: string): void

该接口用于删除AuthKey。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. // 删除认证密钥
2. let keyAlias: string = 'keyAlias';
3. soter.deleteAuthKeySync(keyAlias);
```

## deleteAuthKey

PhonePC/2in1Tablet

deleteAuthKey(keyAlias: string): Promise<void>

该接口用于删除AuthKey，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyAlias | string | 是 | 开发者自定义的密钥别名，keyAlias长度取值范围为[1, 31]。合法字符为：a-z, A-Z, 0-9, -(非首字符), \_(非首字符)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Parameter verification failed. |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let keyAlias: string = 'keyAlias';
4. // 删除AuthKey
5. let delPromise: Promise<void> = soter.deleteAuthKey(keyAlias);
6. delPromise.then(() => {
7. console.info('Succeeded in doing deleteAuthKey.');
8. }).catch((error: BusinessError) => {
9. console.error(`Failed to call deleteAuthKey. Code: ${error.code}, message: ${error.message}`);
10. });
```

## deleteAppSecureKeySync

PhonePC/2in1Tablet

deleteAppSecureKeySync(): void

该接口用于删除应用密钥，同步返回结果。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. // 删除应用密钥
2. soter.deleteAppSecureKeySync();
```

## deleteAppSecureKey

PhonePC/2in1Tablet

deleteAppSecureKey(): Promise<void>

该接口用于删除应用密钥，使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SOTER

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[SOTER免密认证错误码](onlineauthentication-error-code-soter.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Device type error. |
| 1014500001 | The service is abnormal. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 删除应用密钥
4. let delAppSecureKeyPromise: Promise<void> = soter.deleteAppSecureKey();
5. delAppSecureKeyPromise.then(() => {
6. console.info('Succeeded in doing deleteAppSecureKey.');
7. }).catch((error: BusinessError) => {
8. console.error(`Failed to call deleteAppSecureKey. Code: ${error.code}, message: ${error.message}`);
9. });
```
