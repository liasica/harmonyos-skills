---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-certmanager
title: @ohos.security.certManager (证书管理模块)
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > ArkTS API > @ohos.security.certManager (证书管理模块)
category: harmonyos-references
scraped_at: 2026-04-29T13:58:03+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:3b1dd9acef6c28189f585a2569700c8118c0c636a9a4c79106077b3cf5322017
---

证书管理主要提供系统级的证书管理能力，实现证书全生命周期（安装，存储，使用，销毁）的管理和安全使用。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
```

## CmKeyPurpose

PhonePC/2in1TabletTVWearable

表示密钥使用目的的枚举，用于签名、验签。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CM\_KEY\_PURPOSE\_SIGN | 4 | 签名。 |
| CM\_KEY\_PURPOSE\_VERIFY | 8 | 验签。 |

## CmKeyDigest

PhonePC/2in1TabletTVWearable

表示签名、验签使用的摘要算法的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CM\_DIGEST\_NONE | 0 | 不需要摘要算法，选用此项时，需要业务传入已经计算过摘要的数据进行签名、验签。 |
| CM\_DIGEST\_MD5 | 1 | MD5摘要算法。 |
| CM\_DIGEST\_SHA1 | 2 | SHA1摘要算法。 |
| CM\_DIGEST\_SHA224 | 3 | SHA224摘要算法。 |
| CM\_DIGEST\_SHA256 | 4 | SHA256摘要算法。 |
| CM\_DIGEST\_SHA384 | 5 | SHA384摘要算法。 |
| CM\_DIGEST\_SHA512 | 6 | SHA512摘要算法。 |
| CM\_DIGEST\_SM318+ | 7 | SM3摘要算法。 |

## CmKeyPadding

PhonePC/2in1TabletTVWearable

表示签名、验签使用的填充方式的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CM\_PADDING\_NONE | 0 | 无填充。 |
| CM\_PADDING\_PSS | 1 | PSS方式填充。 |
| CM\_PADDING\_PKCS1\_V1\_5 | 2 | PKCS1\_V1\_5方式填充。 |

## CMSignatureSpec

PhonePC/2in1TabletTVWearable

表示签名、验签操作使用的参数集合，包括密钥使用目的、填充方式和摘要算法。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| purpose | [CmKeyPurpose](js-apis-certmanager.md#cmkeypurpose) | 否 | 否 | 表示密钥使用目的的枚举。 |
| padding | [CmKeyPadding](js-apis-certmanager.md#cmkeypadding) | 否 | 是 | 表示填充方式的枚举。 |
| digest | [CmKeyDigest](js-apis-certmanager.md#cmkeydigest) | 否 | 是 | 表示摘要算法的枚举。 |

## CertInfo

PhonePC/2in1TabletTVWearable

表示证书详细信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 表示证书的唯一标识符，最大长度为256字节。 |
| certAlias | string | 否 | 否 | 表示证书的别名，最大长度为128字节。 |
| state | boolean | 否 | 否 | 表示证书的状态，true为启用状态、false为禁用状态。 |
| issuerName | string | 否 | 否 | 表示证书的颁发者名称，最大长度为256字节。 |
| subjectName | string | 否 | 否 | 表示证书的使用者名称，最大长度为1024字节。 |
| serial | string | 否 | 否 | 表示证书的序列号，最大长度为64字节。格式为16进制字符串，例如：62C2CB4DE8405E96。 |
| notBefore | string | 否 | 否 | 表示证书有效期起始日期，最大长度为32字节。 |
| notAfter | string | 否 | 否 | 表示证书有效期截止日期，最大长度为32字节。 |
| fingerprintSha256 | string | 否 | 否 | 表示证书的指纹值，最大长度为128字节。 |
| cert | Uint8Array | 否 | 否 | 表示证书二进制数据，最大长度为8196字节。 |

## CertAbstract

PhonePC/2in1TabletTVWearable

表示证书简要信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 表示证书的唯一标识符，最大长度为256字节。 |
| certAlias | string | 否 | 否 | 表示证书的别名，最大长度为128字节。 |
| state | boolean | 否 | 否 | 表示证书的状态，true为启用状态、false为禁用状态。 |
| subjectName | string | 否 | 否 | 表示证书的使用者名称，最大长度为1024字节。 |

## Credential

PhonePC/2in1TabletTVWearable

表示凭据详细信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 表示凭据的类型，最大长度为8字节。 |
| alias | string | 否 | 否 | 表示凭据的别名，最大长度为128字节。 |
| keyUri | string | 否 | 否 | 表示凭据的唯一标识符，最大长度为256字节。 |
| certNum | number | 否 | 否 | 表示凭据中包含的证书个数。 |
| keyNum | number | 否 | 否 | 表示凭据中包含的密钥个数。 |
| credentialData | Uint8Array | 否 | 否 | 表示凭据二进制数据，最大长度为20480字节。 |
| certPurpose22+ | [CertificatePurpose](js-apis-certmanager.md#certificatepurpose22) | 否 | 是 | 表示凭据的用途。默认值为CertificatePurpose.PURPOSE\_DEFAULT。 |

## CredentialAbstract

PhonePC/2in1TabletTVWearable

表示凭据的简要信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 表示凭据的类型，最大长度为8字节。 |
| alias | string | 否 | 否 | 表示凭据的别名，最大长度为128字节。 |
| keyUri | string | 否 | 否 | 表示凭据的唯一标识符，最大长度为256字节。 |

## CMResult

PhonePC/2in1TabletTVWearable

表示接口的返回结果。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certList | Array<[CertAbstract](js-apis-certmanager.md#certabstract)> | 否 | 是 | 表示证书简要信息的列表。 |
| certInfo | [CertInfo](js-apis-certmanager.md#certinfo) | 否 | 是 | 表示证书详情。 |
| credentialList | Array<[CredentialAbstract](js-apis-certmanager.md#credentialabstract)> | 否 | 是 | 表示凭据简要信息的列表。 |
| credential | [Credential](js-apis-certmanager.md#credential) | 否 | 是 | 表示凭据详情。 |
| appUidList | Array<string> | 否 | 是 | 表示授权应用列表。 |
| uri | string | 否 | 是 | 表示证书或凭据的唯一标识符，最大长度为256字节。 |
| outData | Uint8Array | 否 | 是 | 表示签名结果。 |
| credentialDetailList22+ | Array<[Credential](js-apis-certmanager.md#credential)> | 否 | 是 | 表示凭据详细信息。 |

## CMHandle

PhonePC/2in1TabletTVWearable

表示签名、验签的初始化操作句柄。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handle | Uint8Array | 否 | 否 | 签名、验签的初始化操作句柄，最大长度为8字节。 |

## CMErrorCode

PhonePC/2in1TabletTVWearable

表示调用证书管理相关API的错误码。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CM\_ERROR\_NO\_PERMISSION | 201 | 表示应用程序无权限调用接口。 |
| CM\_ERROR\_INVALID\_PARAMS | 401 | 表示输入参数无效。 |
| CM\_ERROR\_GENERIC | 17500001 | 表示调用接口时发生内部错误。 |
| CM\_ERROR\_NO\_FOUND | 17500002 | 表示证书或凭据不存在。 |
| CM\_ERROR\_INCORRECT\_FORMAT | 17500003 | 表示输入证书或凭据的数据格式无效。 |
| CM\_ERROR\_MAX\_CERT\_COUNT\_REACHED12+ | 17500004 | 表示证书或凭据数量达到上限。 |
| CM\_ERROR\_NO\_AUTHORIZATION12+ | 17500005 | 表示应用未经用户授权。 |
| CM\_ERROR\_DEVICE\_ENTER\_ADVSECMODE18+ | 17500007 | 表示设备进入坚盾守护模式。 |
| CM\_ERROR\_STORE\_PATH\_NOT\_SUPPORTED20+ | 17500009 | 表示不支持指定的证书存储路径。 |
| CM\_ERROR\_ACCESS\_UKEY\_SERVICE\_FAILED22+ | 17500010 | 表示访问USB凭据服务失败。 |
| CM\_ERROR\_PARAMETER\_VALIDATION\_FAILED22+ | 17500011 | 表示输入参数校验失败。  例如：参数格式不正确、参数范围无效。 |

## CertType18+

PhonePC/2in1TabletTVWearable

表示证书类型。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CA\_CERT\_SYSTEM | 0 | 表示系统CA证书。 |
| CA\_CERT\_USER | 1 | 表示用户CA证书。 |

## CertScope18+

PhonePC/2in1TabletTVWearable

表示证书的位置。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CURRENT\_USER | 1 | 表示当前用户。 |
| GLOBAL\_USER | 2 | 表示设备公共，即所有用户都可以访问的位置。 |

## CertAlgorithm20+

PhonePC/2in1TabletTVWearable

表示证书的算法类型。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNATIONAL | 1 | 表示国际密码算法，如RSA、NIST ECC等。 |
| SM | 2 | 表示商用密码算法，如SM2、SM4等。 |

## CertStoreProperty18+

PhonePC/2in1TabletTVWearable

表示获取证书存储位置的参数集合，包括证书的类型及证书的位置。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certType | [CertType](js-apis-certmanager.md#certtype18) | 否 | 否 | 表示证书的类型。 |
| certScope | [CertScope](js-apis-certmanager.md#certscope18) | 否 | 是 | 表示证书的存储位置。当证书类型为CA\_CERT\_USER时，此项为必选项。 |
| certAlg20+ | [CertAlgorithm](js-apis-certmanager.md#certalgorithm20) | 否 | 是 | 表示证书算法类型。仅当certType为CA\_CERT\_SYSTEM时有效，默认值为INTERNATIONAL。 |

## AuthStorageLevel18+

PhonePC/2in1TabletTVWearable

表示凭据的存储级别。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EL1 | 1 | EL1级别，表示设备启动后可以访问。 |
| EL2 | 2 | EL2级别，表示设备首次解锁后可以访问。 |
| EL4 | 4 | EL4级别，表示设备解锁时可以访问。 |

## CertificatePurpose22+

PhonePC/2in1TabletTVWearable

表示凭据用途的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PURPOSE\_DEFAULT | 0 | 默认用途，用于凭据签名。 |
| PURPOSE\_ALL | 1 | 用于查询所有凭据。 |
| PURPOSE\_SIGN | 2 | 用于凭据签名。 |
| PURPOSE\_ENCRYPT | 3 | 用于凭据加密。 |

## UkeyInfo22+

PhonePC/2in1TabletTVWearable

提供USB凭据属性信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certPurpose | [CertificatePurpose](js-apis-certmanager.md#certificatepurpose22) | 否 | 是 | 表示凭据用途。 |

## certificateManager.installPrivateCertificate

PhonePC/2in1TabletTVWearable

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, callback: AsyncCallback<CMResult>): void

表示安装私有凭据，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | 表示带有密钥对和证书的密钥库文件，最大长度为20480字节。 |
| keystorePwd | string | 是 | 表示密钥库文件的密码，长度限制32字节以内。 |
| certAlias | string | 是 | 表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，长度建议32字节以内。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当安装私有凭据成功时，err为null，data为[CMResult](js-apis-certmanager.md#cmresult)对象中的uri属性；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | The keystore is in an invalid format or the keystore password is incorrect. |
| 17500004 | The number of certificates or credentials reaches the maximum allowed. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. /* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
4. let keystore: Uint8Array = new Uint8Array([
5. 0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
6. ]);
7. let keystorePwd: string = "123456";
8. try {
9. certificateManager.installPrivateCertificate(keystore, keystorePwd, "test", (err, cmResult) => {
10. if (err != null) {
11. console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
12. } else {
13. let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
14. console.info('Succeeded in installing private certificate.');
15. }
16. });
17. } catch (error) {
18. console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
19. }
```

## certificateManager.installPrivateCertificate

PhonePC/2in1TabletTVWearable

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>

表示安装私有凭据。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | 表示带有密钥对和证书的密钥库文件，最大长度为20480字节。 |
| keystorePwd | string | 是 | 表示密钥库文件的密码，长度限制32字节以内。 |
| certAlias | string | 是 | 表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，长度建议32字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示安装私有凭据的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的uri属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | The keystore is in an invalid format or the keystore password is incorrect. |
| 17500004 | The number of certificates or credentials reaches the maximum allowed. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
5. let keystore: Uint8Array = new Uint8Array([
6. 0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
7. ]);
8. let keystorePwd: string = "123456";
9. try {
10. certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test').then((cmResult) => {
11. let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
12. console.info('Succeeded in installing private certificate.');
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
15. })
16. } catch (error) {
17. console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
18. }
```

## certificateManager.installPrivateCertificate18+

PhonePC/2in1TabletTVWearable

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>

表示安装私有凭据并指定凭据的存储级别。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | 表示带有密钥对和证书的密钥库文件，最大长度为20480字节。 |
| keystorePwd | string | 是 | 表示密钥库文件的密码。  长度限制：32字节以内。 |
| certAlias | string | 是 | 表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线。  长度建议：32字节以内。 |
| level | [AuthStorageLevel](js-apis-certmanager.md#authstoragelevel18) | 是 | 表示凭据的存储级别。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示安装私有凭据的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的uri属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | The keystore is in an invalid format or the keystore password is incorrect. |
| 17500004 | The number of certificates or credentials reaches the maximum allowed. |

**示例：**

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /* 安装的凭据数据需要业务赋值，本例数据非凭据数据。 */
5. let keystore: Uint8Array = new Uint8Array([
6. 0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
7. ]);
8. let keystorePwd: string = "123456";
9. try {
10. /* 安装凭据在首次解锁设备后可以使用。 */
11. let level = certificateManager.AuthStorageLevel.EL2;
12. certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test', level).then((cmResult) => {
13. let uri: string = (cmResult?.uri == undefined) ? '' : cmResult.uri;
14. console.info('Succeeded in installing private certificate.');
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
17. })
18. } catch (error) {
19. console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
20. }
```

## certificateManager.getPrivateCertificate

PhonePC/2in1TabletTVWearable

getPrivateCertificate(keyUri: string, callback: AsyncCallback<CMResult>): void

表示获取私有凭据的详细信息，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待获取凭据的唯一标识符，长度限制256字节以内。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当获取私有凭据的详细信息成功时，err为null，data为[CMResult](js-apis-certmanager.md#cmresult)对象中的credential属性；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. let uri: string = 'test'; /* 业务获取私有凭据详情，需要使用凭据的唯一标识符，此处省略 */
4. try {
5. certificateManager.getPrivateCertificate(uri, (err, cmResult) => {
6. if (err != null) {
7. console.error(`Failed to get private certificate. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. if (cmResult?.credential == undefined) {
10. console.info('The result of getting private certificate is undefined.');
11. } else {
12. let list = cmResult.credential;
13. console.info('Succeeded in getting private certificate.');
14. }
15. }
16. });
17. } catch (error) {
18. console.error(`Failed to get private certificate. Code: ${error.code}, message: ${error.message}`);
19. }
```

## certificateManager.getPrivateCertificate

PhonePC/2in1TabletTVWearable

getPrivateCertificate(keyUri: string): Promise<CMResult>

表示获取私有凭据详情。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待获取凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示获取私有凭据详细信息的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的credential属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let uri: string = 'test'; /* 业务获取私有凭据详情，需要使用凭据的唯一标识符，此处省略 */
5. try {
6. certificateManager.getPrivateCertificate(uri).then((cmResult) => {
7. if (cmResult?.credential == undefined) {
8. console.info('The result of getting private certificate is undefined.');
9. } else {
10. let list = cmResult.credential;
11. console.info('Succeeded in getting private certificate.');
12. }
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to get private certificate. Code: ${err.code}, message: ${err.message}`);
15. })
16. } catch (error) {
17. console.error(`Failed to get private certificate. Code: ${error.code}, message: ${error.message}`);
18. }
```

## certificateManager.uninstallPrivateCertificate

PhonePC/2in1TabletTVWearable

uninstallPrivateCertificate(keyUri: string, callback: AsyncCallback<void>): void

表示卸载指定的私有凭据，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待卸载凭据的唯一标识符，长度限制256字节以内。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当卸载私有凭据成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. let uri: string = 'test'; /* 业务删除私有凭据，需要使用凭据的唯一标识符，此处省略 */
4. try {
5. certificateManager.uninstallPrivateCertificate(uri, (err, result) => {
6. if (err != null) {
7. console.error(`Failed to uninstall private certificate. Code: ${err.code}, message: ${err.message}`);
8. } else {
9. console.info('Succeeded in uninstalling private certificate.');
10. }
11. });
12. } catch (error) {
13. console.error(`Failed to uninstall private certificate. Code: ${error.code}, message: ${error.message}`);
14. }
```

## certificateManager.uninstallPrivateCertificate

PhonePC/2in1TabletTVWearable

uninstallPrivateCertificate(keyUri: string): Promise<void>

表示卸载指定的私有凭据。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待卸载凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let uri: string = 'test'; /* 业务删除私有凭据，需要使用凭据的唯一标识符，此处省略 */
5. try {
6. certificateManager.uninstallPrivateCertificate(uri).then((cmResult) => {
7. console.info('Succeeded in uninstalling private certificate.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to uninstall private certificate. Code: ${err.code}, message: ${err.message}`);
10. })
11. } catch (error) {
12. console.error(`Failed to uninstall private certificate. Code: ${error.code}, message: ${error.message}`);
13. }
```

## certificateManager.installUserTrustedCertificateSync18+

PhonePC/2in1TabletTVWearable

installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope) : CMResult

表示安装用户CA证书。

**需要权限：** ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | Uint8Array | 是 | 表示CA证书数据，最大长度为8196字节。 |
| certScope | [CertScope](js-apis-certmanager.md#certscope18) | 是 | 表示CA证书安装的位置。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [CMResult](js-apis-certmanager.md#cmresult) | 表示CA证书的安装结果，返回值CMResult对象中的uri属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | Indicates that the certificate is in an invalid format. |
| 17500004 | Indicates that the number of certificates reaches the maximum allowed. |
| 17500007 | Indicates that the device enters advanced security mode. In this mode, the user CA certificate cannot be installed. |

**示例**：

```
1. import {certificateManager} from '@kit.DeviceCertificateKit';

3. /* 安装的CA证书数据需要业务赋值，本例数据非CA证书数据 */
4. let certData: Uint8Array = new Uint8Array([
5. 0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01,
6. ]);
7. try {
8. let result: certificateManager.CMResult = certificateManager.installUserTrustedCertificateSync(certData, certificateManager.CertScope.CURRENT_USER);
9. let certUri = result.uri;
10. if (certUri === undefined) {
11. console.error("The result of install user trusted certificate is undefined.");
12. } else {
13. console.info("Succeeded to install user trusted certificate.");
14. }
15. } catch (error) {
16. console.error(`Failed to install user trusted certificate. Code: ${error.code}, message: ${error.message}`);
17. }
```

## certificateManager.uninstallUserTrustedCertificateSync18+

PhonePC/2in1TabletTVWearable

uninstallUserTrustedCertificateSync(certUri: string) : void

表示删除用户CA证书。

**需要权限：** ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certUri | string | 是 | 表示待卸删除证书的唯一标识符，长度限制256字节以内。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | Indicates that the certificate does not exist. |

**示例**：

```
1. import {certificateManager} from '@kit.DeviceCertificateKit';

3. let certUri: string = "test"; /* 业务删除证书，需要使用证书的标识符，此处省略 */
4. try {
5. certificateManager.uninstallUserTrustedCertificateSync(certUri);
6. } catch (error) {
7. console.error(`Failed to uninstall user trusted certificate. Code: ${error.code}, message: ${error.message}`);
8. }
```

## certificateManager.init

PhonePC/2in1TabletTVWearable

init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void

表示使用凭据进行签名、验签的初始化操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authUri | string | 是 | 表示使用凭据的唯一标识符，长度限制256字节以内。 |
| spec | [CMSignatureSpec](js-apis-certmanager.md#cmsignaturespec) | 是 | 表示签名、验签的属性。 |
| callback | AsyncCallback<[CMHandle](js-apis-certmanager.md#cmhandle)> | 是 | 回调函数。当签名、验签的初始化操作成功时，err为null，data为获取到的CMHandle；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |
| 17500005 | The application is not authorized by the user. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. let uri: string = 'test'; /* 业务使用凭据进行签名、验签的初始化操作，需要使用凭据的唯一标识符，此处省略 */
4. const req: certificateManager.CMSignatureSpec = {
5. purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_SIGN,
6. padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
7. digest: certificateManager.CmKeyDigest.CM_DIGEST_SHA256
8. }
9. try {
10. certificateManager.init(uri, req, (err, cmHandle) => {
11. if (err != null) {
12. console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
13. } else {
14. console.info('Succeeded in initiating.');
15. }
16. })
17. } catch (error) {
18. console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
19. }
```

## certificateManager.init

PhonePC/2in1TabletTVWearable

init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>

表示使用凭据进行签名、验签的初始化操作。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authUri | string | 是 | 表示使用凭据的唯一标识符，长度限制256字节以内。 |
| spec | [CMSignatureSpec](js-apis-certmanager.md#cmsignaturespec) | 是 | 表示签名、验签的属性。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMHandle](js-apis-certmanager.md#cmhandle)> | Promise对象。表示签名、验签的初始化操作结果，返回CMHandle对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |
| 17500005 | The application is not authorized by the user. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let uri: string = 'test'; /* 业务使用凭据进行签名、验签的初始化操作，需要使用凭据的唯一标识符，此处省略 */
5. const req: certificateManager.CMSignatureSpec = {
6. purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_VERIFY,
7. padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
8. digest: certificateManager.CmKeyDigest.CM_DIGEST_MD5
9. }
10. try {
11. certificateManager.init(uri, req).then((handle) => {
12. console.info('Succeeded in initiating.');
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
15. })
16. } catch (error) {
17. console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
18. }
```

## certificateManager.update

PhonePC/2in1TabletTVWearable

update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void

表示签名、验签的数据更新操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |
| data | Uint8Array | 是 | 表示待签名、验签的数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当签名、验签的数据更新操作成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. /* cmHandle为业务调用init接口的返回值，此处仅为示例 */
4. let cmHandle: Uint8Array = new Uint8Array([
5. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
6. ]);
7. let srcData: Uint8Array = new Uint8Array([
8. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
9. ]);
10. try {
11. certificateManager.update(cmHandle, srcData, (err, result) => {
12. if (err != null) {
13. console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
14. } else {
15. console.info('Succeeded in updating.');
16. }
17. });
18. } catch (error) {
19. console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
20. }
```

## certificateManager.update

PhonePC/2in1TabletTVWearable

update(handle: Uint8Array, data: Uint8Array): Promise<void>

表示签名、验签的数据更新操作。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |
| data | Uint8Array | 是 | 表示待签名、验签的数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /* cmHandle为业务调用init接口的返回值，此处仅为示例 */
5. let cmHandle: Uint8Array = new Uint8Array([
6. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
7. ]);
8. let srcData: Uint8Array = new Uint8Array([
9. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
10. ]);
11. try {
12. certificateManager.update(cmHandle, srcData).then((result) => {
13. console.info('Succeeded in updating.');
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
16. })
17. } catch (error) {
18. console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
19. }
```

## certificateManager.finish

PhonePC/2in1TabletTVWearable

finish(handle: Uint8Array, callback: AsyncCallback<CMResult>): void

表示完成签名的操作，Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当签名成功时，err为null，data为[CMResult](js-apis-certmanager.md#cmresult)对象中的outData属性，表示签名数据；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. /* cmHandle为业务调用init接口的返回值，此处仅为示例 */
4. let cmHandle: Uint8Array = new Uint8Array([
5. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
6. ]);
7. try {
8. certificateManager.finish(cmHandle, (err, cmResult) => {
9. if (err != null) {
10. console.error(`Failed to finish. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. if (cmResult?.outData != undefined) {
13. let signRes: Uint8Array = cmResult.outData;
14. console.info('Succeeded in finishing.');
15. } else {
16. console.info('The result of finishing is undefined.');
17. }
18. }
19. });
20. } catch(error) {
21. console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
22. }
```

## certificateManager.finish

PhonePC/2in1TabletTVWearable

finish(handle: Uint8Array, signature: Uint8Array, callback: AsyncCallback<CMResult>): void

表示完成验签的操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |
| signature | Uint8Array | 是 | 表示签名数据。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当验签成功时，err为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. /* cmHandle为业务调用init接口的返回值，此处仅为示例 */
4. let cmHandle: Uint8Array = new Uint8Array([
5. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
6. ]);
7. let signRes: Uint8Array = new Uint8Array([
8. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
9. ]);
10. try {
11. certificateManager.finish(cmHandle, signRes, (err, cmResult) => {
12. if (err != null) {
13. console.error(`Failed to finish. Code: ${err.code}, message: ${err.message}`);
14. } else {
15. console.info('Succeeded in finishing.');
16. }
17. });
18. } catch(error) {
19. console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
20. }
```

## certificateManager.finish

PhonePC/2in1TabletTVWearable

finish(handle: Uint8Array, signature?: Uint8Array): Promise<CMResult>

表示完成签名、验签的操作。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |
| signature | Uint8Array | 否 | 表示用于验签操作的签名数据，仅验签操作需要指定。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。执行签名操作时，表示签名的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的outData属性；执行验签操作时，无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /* cmHandle为业务调用init接口的返回值，此处仅为示例 */
5. let cmHandle: Uint8Array = new Uint8Array([
6. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
7. ]);
8. try {
9. /* 签名的finish操作 */
10. certificateManager.finish(cmHandle).then((cmResult) => {
11. if (cmResult?.outData != undefined) {
12. let signRes1: Uint8Array = cmResult.outData;
13. console.info('Succeeded in finishing signature.');
14. } else {
15. console.info('The result of signature is undefined.');
16. }
17. }).catch((err: BusinessError) => {
18. console.error(`Failed to finish signature. Code: ${err.code}, message: ${err.message}`);
19. })

21. /* 签名的结果 */
22. let signRes: Uint8Array = new Uint8Array([
23. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
24. ]);
25. /* 验签的finish操作 */
26. certificateManager.finish(cmHandle, signRes).then((cmResult) => {
27. console.info('Succeeded in finishing verification.');
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to finish verification. Code: ${err.code}, message: ${err.message}`);
30. })
31. } catch(error) {
32. console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
33. }
```

## certificateManager.abort

PhonePC/2in1TabletTVWearable

abort(handle: Uint8Array, callback: AsyncCallback<void>): void

表示中止签名、验签的操作，使用Callback回调异步返回结果。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当中止签名、验签成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. /* cmHandle为业务调用init接口的返回值，此处仅为示例 */
4. let cmHandle: Uint8Array = new Uint8Array([
5. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
6. ]);
7. try {
8. certificateManager.abort(cmHandle, (err, cmResult) => {
9. if (err != null) {
10. console.error(`Failed to abort. Code: ${err.code}, message: ${err.message}`);
11. } else {
12. console.info('Succeeded in aborting.');
13. }
14. });
15. } catch(error) {
16. console.error(`Failed to abort. Code: ${error.code}, message: ${error.message}`);
17. }
```

## certificateManager.abort

PhonePC/2in1TabletTVWearable

abort(handle: Uint8Array): Promise<void>

表示中止签名、验签的操作。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. /* cmHandle为业务调用init接口的返回值，此处仅为示例 */
5. let cmHandle: Uint8Array = new Uint8Array([
6. 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
7. ]);
8. try {
9. certificateManager.abort(cmHandle).then((result) => {
10. console.info('Succeeded in aborting.');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to abort. Code: ${err.code}, message: ${err.message}`);
13. })
14. } catch (error) {
15. console.error(`Failed to abort. Code: ${error.code}, message: ${error.message}`);
16. }
```

## certificateManager.getPublicCertificate12+

PhonePC/2in1TabletTVWearable

getPublicCertificate(keyUri: string): Promise<CMResult>

表示获取用户公共凭据的详细信息。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示用户公共凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示获取用户公共凭据详细信息的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的credential属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |
| 17500005 | The application is not authorized by the user. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let uri: string = 'test'; /* 用户获取公共凭据详情，需要使用凭据的唯一标识符，此处省略 */
5. try {
6. certificateManager.getPublicCertificate(uri).then((cmResult) => {
7. if (cmResult?.credential == undefined) {
8. console.info('The result of getting public certificate is undefined.');
9. } else {
10. let cred = cmResult.credential;
11. console.info('Succeeded in getting Public certificate.');
12. }
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to get Public certificate. Code: ${err.code}, message: ${err.message}`);
15. })
16. } catch (error) {
17. console.error(`Failed to get Public certificate. Code: ${error.code}, message: ${error.message}`);
18. }
```

## certificateManager.isAuthorizedApp12+

PhonePC/2in1TabletTVWearable

isAuthorizedApp(keyUri: string): Promise<boolean>

表示当前应用是否由指定的用户凭据授权。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示用户授权给应用使用的凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。表示查询应用是否被授权的结果，true为已授权，false为未授权。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let uri: string = 'test'; /* 用户授权给应用使用的凭据的唯一标识符，此处省略 */
5. try {
6. certificateManager.isAuthorizedApp(uri).then((res) => {
7. if (res) {
8. console.info('The application is authorized by the user.');
9. } else {
10. console.info('The application is not authorized by the user.');
11. }
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to check if the application is authorized. Code: ${err.code}, message: ${err.message}`);
14. })
15. } catch (error) {
16. console.error(`Failed to check if the application is authorized. Code: ${error.code}, message: ${error.message}`);
17. }
```

## certificateManager.getAllUserTrustedCertificates12+

PhonePC/2in1TabletTVWearable

getAllUserTrustedCertificates(): Promise<CMResult>

表示获取当前用户和设备公共位置的所有用户根CA证书列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示获取用户根CA证书列表的结果，返回值[CMResult](js-apis-certmanager.md#cmresult)对象中的certList属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. certificateManager.getAllUserTrustedCertificates().then((cmResult) => {
6. if (cmResult === undefined) { // 用户根CA证书个数为0时，返回cmResult为undefined。
7. console.info('the count of the user trusted certificates is 0');
8. } else if (cmResult.certList == undefined) {
9. console.info('The result of getting all user trusted certificates is undefined.');
10. } else {
11. let list = cmResult.certList;
12. console.info('Succeeded in getting all user trusted certificates.');
13. }
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to get all user trusted certificates. Code: ${err.code}, message: ${err.message}`);
16. })
17. } catch (error) {
18. console.error(`Failed to get all user trusted certificates. Code: ${error.code}, message: ${error.message}`);
19. }
```

## certificateManager.getAllUserTrustedCertificates18+

PhonePC/2in1TabletTVWearable

getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>

表示根据证书的位置获取用户根CA证书列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [CertScope](js-apis-certmanager.md#certscope18) | 是 | 表示证书的位置。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示获取用户根CA证书列表的结果，返回值[CMResult](js-apis-certmanager.md#cmresult)对象中的certList属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. /* 获取当前用户下的用户根CA证书列表; 如果需要获取设备公共位置的用户根CA列表，则传入GLOBAL_USER */
6. let scope: certificateManager.CertScope = certificateManager.CertScope.CURRENT_USER;
7. certificateManager.getAllUserTrustedCertificates(scope).then((cmResult) => {
8. if (cmResult === undefined) { // 用户根CA证书个数为0时，返回cmResult为undefined。
9. console.info('the count of the user trusted certificates is 0');
10. } else if (cmResult.certList == undefined) {
11. console.info('The result of getting current user trusted certificates is undefined.');
12. } else {
13. let list = cmResult.certList;
14. console.info('Succeeded in getting current user trusted certificates.');
15. }
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to get current user trusted certificates. Code: ${err.code}, message: ${err.message}`);
18. })
19. } catch (error) {
20. console.error(`Failed to get current user trusted certificates. Code: ${error.code}, message: ${error.message}`);
21. }
```

## certificateManager.getUserTrustedCertificate12+

PhonePC/2in1TabletTVWearable

getUserTrustedCertificate(certUri: string): Promise<CMResult>

表示获取用户根CA证书的详细信息。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certUri | string | 是 | 表示用户根CA证书的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示获取用户根CA证书详细信息的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的certInfo属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let certUri: string = 'testUserCert'; /* 用户获取用户根CA证书详情，需要使用CA证书的唯一标识符，此处省略 */
5. try {
6. certificateManager.getUserTrustedCertificate(certUri).then((cmResult) => {
7. if (cmResult?.certInfo == undefined) {
8. console.info('The result of getting user trusted certificate is undefined.');
9. } else {
10. let cert = cmResult.certInfo;
11. console.info('Succeeded in getting user trusted certificate.');
12. }
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to get user trusted certificate. Code: ${err.code}, message: ${err.message}`);
15. })
16. } catch (error) {
17. console.error(`Failed to get user trusted certificate. Code: ${error.code}, message: ${error.message}`);
18. }
```

## certificateManager.getPrivateCertificates13+

PhonePC/2in1TabletTVWearable

getPrivateCertificates(): Promise<CMResult>

表示获取应用安装的凭据列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。表示获取应用安装的凭据列表的结果，返回值[CMResult](js-apis-certmanager.md#cmresult)对象中的credentialList属性。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. certificateManager.getPrivateCertificates().then((cmResult) => {
6. if (cmResult === undefined) { // 应用安装的凭据个数为0时，返回cmResult为undefined。
7. console.info('the count of the private certificates is 0');
8. } else if (cmResult.credentialList == undefined) {
9. console.info('The result of getting all private certificates installed by the application is undefined.');
10. } else {
11. let list = cmResult.credentialList;
12. console.info('Succeeded in getting all private certificates installed by the application.');
13. }
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to get all private certificates installed by the application. Code: ${err.code}, message: ${err.message}`);
16. })
17. } catch (error) {
18. console.error(`Failed to get all private certificates installed by the application. Code: ${error.code}, message: ${error.message}`);
19. }
```

## certificateManager.getCertificateStorePath18+

PhonePC/2in1TabletTVWearable

getCertificateStorePath(property: CertStoreProperty): string;

表示获取证书的存储路径。

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| property | [CertStoreProperty](js-apis-certmanager.md#certstoreproperty18) | 是 | 表示获取证书存储路径的参数集合。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | 表示证书的存储路径。 |

**错误码：**

以下错误码的详细介绍请参见[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. For example, CertStoreProperty.certType is set to CA\_CERT\_USER, but CertStoreProperty.certScope is not specified. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500009 | The device does not support the specified certificate storage path, For example, the device outside China does not support the certificate that uses SM algorithm. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';

3. try {
4. /* 获取系统CA的存储位置 */
5. let property1: certificateManager.CertStoreProperty = {
6. certType: certificateManager.CertType.CA_CERT_SYSTEM,
7. }
8. let systemCAPath = certificateManager.getCertificateStorePath(property1);
9. console.info(`Success to get system ca path: ${systemCAPath}`);

11. /* 获取当前用户的用户CA存储位置 */
12. let property2: certificateManager.CertStoreProperty = {
13. certType: certificateManager.CertType.CA_CERT_USER,
14. certScope: certificateManager.CertScope.CURRENT_USER,
15. }
16. let userCACurrentPath = certificateManager.getCertificateStorePath(property2);
17. console.info(`Success to get current user's user ca path: ${userCACurrentPath}`);

19. /* 获取设备公共的用户CA存储位置 */
20. let property3: certificateManager.CertStoreProperty = {
21. certType: certificateManager.CertType.CA_CERT_USER,
22. certScope: certificateManager.CertScope.GLOBAL_USER,
23. }
24. let globalCACurrentPath = certificateManager.getCertificateStorePath(property3);
25. console.info(`Success to get global user's user ca path: ${globalCACurrentPath}`);

27. /* 获取SM算法系统CA的存储位置 */
28. let property4: certificateManager.CertStoreProperty = {
29. certType: certificateManager.CertType.CA_CERT_SYSTEM,
30. certAlg: certificateManager.CertAlgorithm.SM,
31. }
32. let smSystemCAPath = certificateManager.getCertificateStorePath(property4);
33. console.info(`Success to get SM system ca path: ${smSystemCAPath}`);
34. } catch (error) {
35. console.error(`Failed to get store path. Code: ${error.code}, message: ${error.message}`);
36. }
```

## certificateManager.getUkeyCertificate22+

PhonePC/2in1TabletTVWearable

getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>

表示获取USB凭据详细信息。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**设备行为差异：** 该接口在PC设备可正常调用，在其他设备中返回801错误码。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示USB凭据的唯一标识符，长度限制256字节以内。 |
| ukeyInfo | [UkeyInfo](js-apis-certmanager.md#ukeyinfo22) | 是 | 表示USB凭据的属性信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取到的USB凭据详情的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 801 | Capability not supported. The application does not have the permission required to call the API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | Indicates that the certificate does not exist. |
| 17500010 | Indicates that access USB key service failed. |
| 17500011 | Indicates that the input parameters validation failed. For example, the parameter format is incorrect or the value range is invalid. |

**示例**：

```
1. import { certificateManager } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let keyUri: string = 'test'; /* USB凭据的唯一标识符，此处省略 */
5. let ukeyInfo: certificateManager.UkeyInfo = { /* USB凭据的属性信息，此处省略 */
6. certPurpose: certificateManager.CertificatePurpose.PURPOSE_DEFAULT,
7. }
8. try {
9. certificateManager.getUkeyCertificate(keyUri, ukeyInfo).then((cmResult) => {
10. let list = cmResult.credentialDetailList;
11. console.info('Succeeded in getting detail of USB key certificate.');
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to get detail of USB key certificate. Code: ${err.code}, message: ${err.message}`);
14. })
15. } catch (error) {
16. console.error(`Failed to get detail of USB key certificate. Code: ${error.code}, message: ${error.message}`);
17. }
```
