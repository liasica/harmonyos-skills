---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-huksexternalcrypto
title: @ohos.security.huksExternalCrypto (外部密钥管理)
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > ArkTS API > @ohos.security.huksExternalCrypto (外部密钥管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:45+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:3e09dd66d2115388c89550c66bcff380abe62ec5c061267a49739b4954f81903
---

模块提供外部密钥管理扩展功能的注册与注销，PIN码认证与认证状态获取等。

说明

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
```

## HuksExternalCryptoTagType

PC/2in1

表示外部加密数据类型的枚举。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HUKS\_EXT\_CRYPTO\_TAG\_TYPE\_INT | 1 << 28 | 表示TAG的值为整数类型。 |
| HUKS\_EXT\_CRYPTO\_TAG\_TYPE\_BYTES | 5 << 28 | 表示TAG的值为字节数组。 |

## HuksExternalCryptoTag

PC/2in1

表示调用参数的Tag。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HUKS\_EXT\_CRYPTO\_TAG\_UKEY\_PIN | HuksExternalCryptoTagType.HUKS\_EXT\_CRYPTO\_TAG\_TYPE\_BYTES | 200001 | 表示PIN码的TAG。 |
| HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME | HuksExternalCryptoTagType.HUKS\_EXT\_CRYPTO\_TAG\_TYPE\_BYTES | 200002 | 表示[CryptoExtensionAbility](js-apis-cryptoextensionability.md)的名称。 |
| HUKS\_EXT\_CRYPTO\_TAG\_EXTRA\_DATA | HuksExternalCryptoTagType.HUKS\_EXT\_CRYPTO\_TAG\_TYPE\_BYTES | 200003 | 外部数据，在通用查询场景，表示返回的数据。 |
| HUKS\_EXT\_CRYPTO\_TAG\_UID | HuksExternalCryptoTagType.HUKS\_EXT\_CRYPTO\_TAG\_TYPE\_INT | 200004 | 表示调用方的uid。 |
| HUKS\_EXT\_CRYPTO\_TAG\_PURPOSE | HuksExternalCryptoTagType.HUKS\_EXT\_CRYPTO\_TAG\_TYPE\_INT | 200005 | 表示证书链对应密钥的使用类型，具体类型详见[CertificatePurpose定义](js-apis-certmanager.md#certificatepurpose22)。 |

## HuksExternalCryptoParam

PC/2in1

表示调用接口使用的param数组的类型。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tag | [HuksExternalCryptoTag](js-apis-huksexternalcrypto.md#huksexternalcryptotag) | 否 | 否 | 参数标签，用于区分参数。 |
| value | boolean|number|bigint|Uint8Array | 否 | 否 | 标签对应值。 |

## HuksExternalPinAuthState

PC/2in1

表示Ukey PIN码管理的状态值的枚举。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HUKS\_EXT\_CRYPTO\_PIN\_NO\_AUTH | 0 | Ukey PIN未认证。 |
| HUKS\_EXT\_CRYPTO\_PIN\_AUTH\_SUCCEEDED | 1 | Ukey PIN认证成功。 |
| HUKS\_EXT\_CRYPTO\_PIN\_LOCKED | 2 | Ukey PIN已锁定。 |

## huksExternalCrypto.registerProvider

PC/2in1

registerProvider(providerName: string, params: Array<HuksExternalCryptoParam>): Promise<void>

注册指定的外部provider。使用Promise异步回调。

**需要权限：** ohos.permission.CRYPTO\_EXTENSION\_REGISTER

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| providerName | string | 是 | provider名称，最大长度为128。建议包含厂商信息，全局唯一，不要包含个人联系方式等敏感数据。  最多支持注册10个provider。 |
| params | Array<[HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 是 | 操作时需传入的参数，必选TAG：[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](js-apis-huksexternalcrypto.md#huksexternalcryptotag)，表示ability的名字，根据业务自己内部定义按照实际填写。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[HUKS错误码](errorcode-huks.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission failed. |
| 801 | api is not supported. |
| 12000002 | the ability name param is missing. |
| 12000005 | IPC communication failed. |
| 12000014 | memory is insufficient. |
| 12000018 | the input parameter is invalid. |
| 12000019 | the provider is already registered. |
| 12000020 | an error occurred in the dependent module. |
| 12000025 | the number of providers exceeds the limit. |

**示例：**

```
1. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

3. function StringToUint8Array(str: string) {
4. let arr: number[] = [];
5. for (let i = 0, j = str.length; i < j; ++i) {
6. arr.push(str.charCodeAt(i));
7. }
8. return new Uint8Array(arr);
9. }

11. const providerName = "testProviderName";
12. const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
13. {
14. tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
15. value: StringToUint8Array("CryptoExtension")
16. }
17. ];
18. huksExternalCrypto.registerProvider(providerName, extProperties)
19. .then((data) => {
20. console.info(`promise: registerProvider success`);
21. });
```

## huksExternalCrypto.unregisterProvider

PC/2in1

unregisterProvider(providerName: string, params?: Array<HuksExternalCryptoParam>): Promise<void>

注销指定的外部provider。使用Promise异步回调。

**需要权限：** ohos.permission.CRYPTO\_EXTENSION\_REGISTER

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| providerName | string | 是 | provider名称，最大长度为128。建议包含厂商信息，全局唯一，不要包含个人联系方式等敏感数据。如果provider注册了多个扩展能力，则该provider下的扩展能力都会被注销。 |
| params | Array<[HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 否 | 操作时需传入的参数。  可以在param参数中指定[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](js-apis-huksexternalcrypto.md#huksexternalcryptotag)，将根据“包名 + providerName + abilityName”注销对应的cryptoExtensionAbility。  如果未在params参数中指定[HUKS\_EXT\_CRYPTO\_TAG\_ABILITY\_NAME](js-apis-huksexternalcrypto.md#huksexternalcryptotag)，或者未传入params参数，则注销对应的providerName下的所有Provider。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[HUKS错误码](errorcode-huks.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | check permission failed. |
| 801 | api is not supported. |
| 12000005 | IPC communication failed. |
| 12000011 | the provider is not found. |
| 12000012 | Device environment or input parameter is abnormal. This may happen for several reasons, such as the model already being unloaded. |
| 12000014 | memory is insufficient. |
| 12000018 | the input parameter is invalid. |

**示例：**

```
1. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

3. function StringToUint8Array(str: string) {
4. let arr: number[] = [];
5. for (let i = 0, j = str.length; i < j; ++i) {
6. arr.push(str.charCodeAt(i));
7. }
8. return new Uint8Array(arr);
9. }

11. const providerName = "testProviderName";
12. const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [
13. {
14. tag: huksExternalCrypto.HuksExternalCryptoTag.HUKS_EXT_CRYPTO_TAG_ABILITY_NAME,
15. value: StringToUint8Array("CryptoExtension")
16. }
17. ];
18. huksExternalCrypto.unregisterProvider(providerName, extProperties)
19. .then((data) => {
20. console.info(`promise: unregisterProvider success`);
21. });
```

## huksExternalCrypto.getUkeyPinAuthState

PC/2in1

getUkeyPinAuthState(resourceId: string, params?: Array<HuksExternalCryptoParam>): Promise<HuksExternalPinAuthState>

获取PIN码认证状态。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID，可通过[导出证书的接口](js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取，其结果中附带资源ID。 |
| params | Array<[HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 否 | 操作的属性。非系统应用传入[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)是非法参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[HuksExternalPinAuthState](js-apis-huksexternalcrypto.md#huksexternalpinauthstate)> | Promise对象，返回认证结果。  HUKS\_EXT\_CRYPTO\_PIN\_NO\_AUTH 表示未认证；HUKS\_EXT\_CRYPTO\_PIN\_AUTH\_SUCCEEDED 表示认证成功；HUKS\_EXT\_CRYPTO\_PIN\_LOCKED 表示PIN被锁定。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[HUKS错误码](errorcode-huks.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | api is not supported. |
| 12000005 | IPC communication failed. |
| 12000006 | the Ukey driver operation failed. |
| 12000011 | queried entity does not exist. This may happen because the resource ID has not been opened. |
| 12000012 | Device environment or input parameter is abnormal. This error may occur if the process function is not found, or due to other issues. |
| 12000014 | memory is insufficient. |
| 12000018 | the input parameter is invalid. |
| 12000020 | the provider operation failed. |
| 12000024 | the provider or Ukey is busy. |

**示例：**

```
1. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

3. function StringToUint8Array(str: string) {
4. let arr: number[] = [];
5. for (let i = 0, j = str.length; i < j; ++i) {
6. arr.push(str.charCodeAt(i));
7. }
8. return new Uint8Array(arr);
9. }

11. const testResourceId = "{\"providerName\":\"testProviderName\", \"bundleName\":\"com.example.cryptoapplication\", \"abilityName\":\"CryptoExtension\",\"index\":{\"key\":\"testKey\"}}";
12. const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];
13. huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
14. .then((data) => {
15. console.info(`promise: getUkeyPinAuthState success, data: ${data}`);
16. });
```

## huksExternalCrypto.getProperty

PC/2in1

getProperty(resourceId: string, propertyId: string, params?: Array<HuksExternalCryptoParam>): Promise<Array<HuksExternalCryptoParam>>

调用此接口获取属性值并返回结果。使用Promise异步回调。

propertyId表示查询属性的ID信息，当前仅支持GMT 0016-2023中定义的SKF接口名作为属性ID，支持的ID包括如下：

* SKF\_EnumDev
* SKF\_GetDevInfo
* SKF\_EnumApplication
* SKF\_EnumContainer

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceId | string | 是 | 资源ID，可通过[导出证书的接口](js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取，该接口的返回结果中附带resourceId。 |
| propertyId | string | 是 | 查找操作的属性名称，是GMT 0016-2023中定义的SKF接口名，应用开发者需要针对接口名进行适配。 |
| params | Array<[HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)> | 否 | 需要传递给[Extension Ability](js-apis-cryptoextensionability.md)的输入参数。非系统应用传入[HUKS\_EXT\_CRYPTO\_TAG\_UID](js-apis-huksexternalcrypto.md#huksexternalcryptotag)是非法参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[HuksExternalCryptoParam](js-apis-huksexternalcrypto.md#huksexternalcryptoparam)>> | Promise对象，返回调用接口的结果。当调用成功时，返回结果为HuksExternalCryptoParam类型的数组，包含要查询的属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[HUKS错误码](errorcode-huks.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 12000005 | IPC communication failed. |
| 12000006 | If the Ukey driver operation failed. Possible causes: 1. Error reported when the provider accesses the SKF interface of Ukey. |
| 12000011 | If the cached resource ID is not found. |
| 12000012 | Device environment or input parameter is abnormal. This error may occur if the process function is not found, or due to other issues. |
| 12000014 | If the memory is insufficient. |
| 12000018 | Input parameter is invalid. Possible causes: 1. The resourceId or propertyId length is invalid. 2. The params contains invalid tags or invalid value types. |
| 12000020 | If the provider operation failed. Possible causes: 1. The provider experienced an internal processing error. |
| 12000021 | The Ukey PIN is locked. |
| 12000023 | The Ukey PIN is not authenticated. |
| 12000024 | If the provider or Ukey is busy. |

**示例：**

```
1. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';

3. const testResourceId = JSON.stringify({
4. providerName: "testProviderName",
5. bundleName: "com.example.cryptoapplication",
6. abilityName: "CryptoExtension",
7. index: {
8. key: "testKey"
9. } as ESObject
10. });

12. let propertyId = "SKF_EnumDev";
13. const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

15. console.info(`promise: await huksExternalCrypto getProperty`);
16. async function testFunction() : Promise<void>
17. {
18. try {
19. await huksExternalCrypto.getProperty(testResourceId, propertyId, extProperties)
20. .then((data) => {
21. console.info(`promise: getProperty success, data: ` + JSON.stringify(data));
22. });
23. } catch (error) {
24. console.error(`promise: getProperty failed, errCode : ${error.code}, errMsg : ${error.message}`);
25. }
26. }
```
