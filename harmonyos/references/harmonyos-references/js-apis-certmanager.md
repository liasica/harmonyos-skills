---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-certmanager
title: "@ohos.security.certManager (证书管理模块)"
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > ArkTS API > @ohos.security.certManager (证书管理模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ebbf7126cde34d12dfff6e2f9902829f7034c240ea6d396883739b092306b853
---

证书管理主要提供系统级的证书管理能力，实现证书全生命周期（安装，存储，使用，销毁）的管理和安全使用。

可用于校验应用服务器的HTTPS证书链、通过双向HTTPS登录网站或应用服务器。

**说明** 

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
```

## CmKeyPurpose

表示密钥使用目的的枚举，用于签名、验签。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CM\_KEY\_PURPOSE\_SIGN | 4 | 签名。 |
| CM\_KEY\_PURPOSE\_VERIFY | 8 | 验签。 |

## CmKeyDigest

表示签名、验签使用的摘要算法的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CM\_DIGEST\_NONE | 0 | 选用此项时，需要应用程序传入已经计算过摘要的数据进行签名、验签。 |
| CM\_DIGEST\_MD5 | 1 | MD5摘要算法。 |
| CM\_DIGEST\_SHA1 | 2 | SHA1摘要算法。 |
| CM\_DIGEST\_SHA224 | 3 | SHA224摘要算法。 |
| CM\_DIGEST\_SHA256 | 4 | SHA256摘要算法。 |
| CM\_DIGEST\_SHA384 | 5 | SHA384摘要算法。 |
| CM\_DIGEST\_SHA512 | 6 | SHA512摘要算法。 |
| CM\_DIGEST\_SM318+ | 7 | SM3摘要算法。 |

## CmKeyPadding

表示签名、验签使用的填充方式的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CM\_PADDING\_NONE | 0 | 无填充。 |
| CM\_PADDING\_PSS | 1 | PSS方式填充。 |
| CM\_PADDING\_PKCS1\_V1\_5 | 2 | PKCS1\_V1\_5方式填充。 |

## CMSignatureSpec

表示签名、验签操作使用的参数集合，包括密钥使用目的、填充方式和摘要算法。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| purpose | [CmKeyPurpose](js-apis-certmanager.md#cmkeypurpose) | 否 | 否 | 表示密钥使用目的的枚举。 |
| padding | [CmKeyPadding](js-apis-certmanager.md#cmkeypadding) | 否 | 是 | 表示填充方式的枚举。默认值：CM\_PADDING\_PSS，表示使用PSS填充方式。 |
| digest | [CmKeyDigest](js-apis-certmanager.md#cmkeydigest) | 否 | 是 | 表示摘要算法的枚举。默认值：CM\_DIGEST\_SHA256，表示使用SHA256摘要算法。 |

## CertInfo

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

表示证书简要信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 表示证书的唯一标识符，最大长度为256字节。 |
| certAlias | string | 否 | 否 | 表示证书的别名，最大长度为128字节。 |
| state | boolean | 否 | 否 | 表示证书的状态，true为启用状态、false为禁用状态。 |
| subjectName | string | 否 | 否 | 表示证书的使用者名称，最大长度为1024字节。 |

## Credential

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

表示凭据的简要信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 否 | 表示凭据的类型，最大长度为8字节。 |
| alias | string | 否 | 否 | 表示凭据的别名，最大长度为128字节。 |
| keyUri | string | 否 | 否 | 表示凭据的唯一标识符，最大长度为256字节。 |

## CMResult

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
| uriList | Array<string> | 否 | 是 | 表示证书URI列表。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |

## CMHandle

表示签名、验签的初始化操作句柄。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| handle | Uint8Array | 否 | 否 | 签名、验签的初始化操作句柄，最大长度为8字节。 |

## CertBlob

表示证书文件数据。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.CertificateManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certData | Uint8Array | 否 | 否 | 表示证书文件数据。当certFormat传入PEM\_DER，最大长度为8KB。当certFormat传入P7B，最大长度为300KB。 |
| certFormat | [CertFileFormat](js-apis-certmanager.md#certfileformat) | 否 | 是 | 表示证书文件格式。默认值：PEM\_DER。 |
| certScope | [CertScope](js-apis-certmanager.md#certscope18) | 否 | 是 | 表示用户CA证书的存储位置。默认值：CURRENT\_USER。 |

## CMErrorCode

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
| CM\_ERROR\_DEVICE\_ENTER\_ADVSECMODE18+ | 17500007 | 表示设备进入坚盾守护模式。该模式下CA证书安装操作受限。 |
| CM\_ERROR\_STORE\_PATH\_NOT\_SUPPORTED20+ | 17500009 | 表示不支持指定的证书存储路径。 |
| CM\_ERROR\_ACCESS\_UKEY\_SERVICE\_FAILED22+ | 17500010 | 表示访问USB Key服务失败。 |
| CM\_ERROR\_PARAMETER\_VALIDATION\_FAILED22+ | 17500011 | 表示输入参数校验失败。  例如：参数格式不正确、参数范围无效。 |

## CertType18+

表示证书类型。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CA\_CERT\_SYSTEM | 0 | 表示系统CA证书。 |
| CA\_CERT\_USER | 1 | 表示用户CA证书。 |

## CertScope18+

表示证书的位置。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CURRENT\_USER | 1 | 表示当前用户。 |
| GLOBAL\_USER | 2 | 表示设备公共，即所有用户都可以访问的位置。 |

## CertAlgorithm20+

表示证书的算法类型。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNATIONAL | 1 | 表示国际密码算法，如RSA、NIST ECC等。 |
| SM | 2 | 表示商用密码算法，如SM2、SM4等。海外设备不支持使用该算法的证书。 |

## CertStoreProperty18+

表示获取证书存储位置的参数集合，包括证书的类型及证书的位置。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certType | [CertType](js-apis-certmanager.md#certtype18) | 否 | 否 | 表示证书的类型。 |
| certScope | [CertScope](js-apis-certmanager.md#certscope18) | 否 | 是 | 表示证书的存储位置。当证书类型为CA\_CERT\_USER时，此项为必选项。 |
| certAlg20+ | [CertAlgorithm](js-apis-certmanager.md#certalgorithm20) | 否 | 是 | 表示证书算法类型。仅当certType为CA\_CERT\_SYSTEM时有效，默认值为INTERNATIONAL。海外设备不支持SM算法。 |

## AuthStorageLevel18+

表示凭据的存储级别。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EL1 | 1 | EL1级别，表示设备启动后可以访问。 |
| EL2 | 2 | EL2级别，表示设备首次解锁后可以访问。 |
| EL4 | 4 | EL4级别，表示设备解锁时可以访问。 |

## CertificatePurpose22+

表示凭据用途的枚举。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PURPOSE\_DEFAULT | 0 | 默认用途，用于凭据签名。 |
| PURPOSE\_ALL | 1 | 用于查询所有凭据。 |
| PURPOSE\_SIGN | 2 | 用于凭据签名。 |
| PURPOSE\_ENCRYPT | 3 | 用于凭据加密。 |

## UkeyInfo22+

提供USB Key证书凭据属性信息。

**系统能力：** SystemCapability.Security.CertificateManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| certPurpose | [CertificatePurpose](js-apis-certmanager.md#certificatepurpose22) | 否 | 是 | 表示凭据用途。默认值：PURPOSE\_DEFAULT。 |

## CertFileFormat

表示证书文件格式。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.Security.CertificateManager

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PEM\_DER | 0 | 表示证书文件格式为PEM或DER。 |
| P7B | 1 | 表示证书文件格式为P7B。 |

## certificateManager.installPrivateCertificate

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, callback: AsyncCallback<CMResult>): void

安装私有凭据。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | 表示带有密钥对和证书的密钥库文件，最大长度为20480字节。 |
| keystorePwd | string | 是 | 表示密钥库文件的密码，长度限制32字节以内。 |
| certAlias | string | 是 | 表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，最大长度32字节。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当安装私有凭据成功时，err为null，data为[CMResult](js-apis-certmanager.md#cmresult)对象中的uri属性；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | The keystore is in an invalid format or the keystore password is incorrect. |
| 17500004 | The number of certificates or credentials reaches the maximum allowed.  适用版本：12+ |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
let keystorePwd: string = '123456';
try {
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test', (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
    } else {
      let uri: string = cmResult?.uri ?? '';
      console.info('Succeeded in installing private certificate.');
    }
  });
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.installPrivateCertificate

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>

安装私有凭据。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | 表示带有密钥对和证书的密钥库文件，最大长度为20480字节。 |
| keystorePwd | string | 是 | 表示密钥库文件的密码，长度限制32字节以内。 |
| certAlias | string | 是 | 表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，最大长度32字节。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回安装私有凭据的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的uri属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | The keystore is in an invalid format or the keystore password is incorrect. |
| 17500004 | The number of certificates or credentials reaches the maximum allowed.  适用版本：12+ |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
let keystorePwd: string = '123456';
try {
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test').then((cmResult) => {
    let uri: string = cmResult?.uri ?? '';
    console.info('Succeeded in installing private certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.installPrivateCertificate18+

installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>

安装私有凭据并指定凭据的存储级别。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keystore | Uint8Array | 是 | 表示带有密钥对和证书的密钥库文件，最大长度为20480字节。 |
| keystorePwd | string | 是 | 表示密钥库文件的密码。  长度限制：32字节以内。 |
| certAlias | string | 是 | 表示用户输入的凭据别名，当前仅支持传入数字、字母或下划线，最大长度32字节。 |
| level | [AuthStorageLevel](js-apis-certmanager.md#authstoragelevel18) | 是 | 表示凭据的存储级别。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回安装私有凭据的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的uri属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | The keystore is in an invalid format or the keystore password is incorrect. |
| 17500004 | The number of certificates or credentials reaches the maximum allowed. |

**示例：**

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的凭据数据需要业务赋值，本例数据非凭据数据。 */
let keystore: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
let keystorePwd: string = '123456';
try {
  /* 安装凭据在首次解锁设备后可以使用。 */
  let level = certificateManager.AuthStorageLevel.EL2;
  certificateManager.installPrivateCertificate(keystore, keystorePwd, 'test', level).then((cmResult) => {
    let uri: string = cmResult.uri ?? '';
    console.info('Succeeded in installing private certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install private certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to install private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getPrivateCertificate

getPrivateCertificate(keyUri: string, callback: AsyncCallback<CMResult>): void

获取私有凭据的详细信息，使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待获取凭据的唯一标识符，长度限制256字节以内。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当获取私有凭据的详细信息成功时，err为null，data为[CMResult](js-apis-certmanager.md#cmresult)对象中的credential属性；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. Possible causes: 1. The certificate URI is incorrect; 2. The certificate has been uninstalled. Please check the certificate URI. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

let uri: string = 'test'; /* 业务获取私有凭据详情，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.getPrivateCertificate(uri, (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to get private certificate. Code: ${err.code}, message: ${err.message}`);
    } else {
      if (cmResult?.credential == undefined) {
        console.info('The result of getting private certificate is undefined.');
      } else {
        let list = cmResult?.credential;
        console.info('Succeeded in getting private certificate.');
      }
    }
  });
} catch (error) {
  console.error(`Failed to get private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getPrivateCertificate

getPrivateCertificate(keyUri: string): Promise<CMResult>

获取私有凭据详情。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待获取凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取私有凭据详细信息的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的credential属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 业务获取私有凭据详情，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.getPrivateCertificate(uri).then((cmResult) => {
    if (cmResult?.credential == undefined) {
      console.info('The result of getting private certificate is undefined.');
    } else {
      let list = cmResult.credential;
      console.info('Succeeded in getting private certificate.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get private certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.uninstallPrivateCertificate

uninstallPrivateCertificate(keyUri: string, callback: AsyncCallback<void>): void

卸载指定的私有凭据，使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待卸载凭据的唯一标识符，长度限制256字节以内。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当卸载私有凭据成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

let uri: string = 'test'; /* 业务删除私有凭据，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.uninstallPrivateCertificate(uri, (err) => {
    if (err != null) {
      console.error(`Failed to uninstall private certificate. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in uninstalling private certificate.');
    }
  });
} catch (error) {
  console.error(`Failed to uninstall private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.uninstallPrivateCertificate

uninstallPrivateCertificate(keyUri: string): Promise<void>

卸载指定的私有凭据。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示待卸载凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 业务删除私有凭据，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.uninstallPrivateCertificate(uri).then(() => {
    console.info('Succeeded in uninstalling private certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to uninstall private certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to uninstall private certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.installUserTrustedCertificate

installUserTrustedCertificate(certificate: CertBlob): Promise<CMResult>

安装用户CA证书。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT

**系统能力：** SystemCapability.Security.CertificateManager

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certificate | [CertBlob](js-apis-certmanager.md#certblob) | 是 | 表示证书信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回安装用户CA证书的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的uri属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter verification failed. Possible causes: the certData parameter is empty or exceeds the maximum length. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | Indicates that the certificate is in an invalid format. |
| 17500004 | Indicates that the number of certificates reaches the maximum allowed. |
| 17500007 | Indicates that the device enters advanced security mode. In this mode, the user CA certificate cannot be installed. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* 安装的CA证书数据需要业务赋值，本例数据非CA证书数据 */
let certData: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
try {
  let certBlob: certificateManager.CertBlob = {
    certData: certData,
    certFormat: certificateManager.CertFileFormat.PEM_DER,
    certScope: certificateManager.CertScope.CURRENT_USER
  };
  certificateManager.installUserTrustedCertificate(certBlob).then((cmResult) => {
    let uri: string = cmResult.uri ?? '';
    console.info('Succeeded in installing user trusted certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to install user trusted certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to install user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.installUserTrustedCertificateSync18+

installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult

安装用户CA证书。

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
| [CMResult](js-apis-certmanager.md#cmresult) | 表示CA证书的安装结果，返回值为CMResult对象中的uri属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500003 | Indicates that the certificate is in an invalid format. |
| 17500004 | Indicates that the number of certificates reaches the maximum allowed. |
| 17500007 | Indicates that the device enters advanced security mode. In this mode, the user CA certificate cannot be installed. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

/* 安装的CA证书数据需要业务赋值，本例数据非CA证书数据 */
let certData: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
try {
  let result: certificateManager.CMResult = certificateManager.installUserTrustedCertificateSync(certData,
    certificateManager.CertScope.CURRENT_USER);
  let certUri = result.uri;
  if (certUri === undefined) {
    console.error('The result of install user trusted certificate is undefined.');
  } else {
    console.info('Succeeded in installing user trusted certificate.');
  }
} catch (error) {
  console.error(`Failed to install user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.uninstallUserTrustedCertificateSync18+

uninstallUserTrustedCertificateSync(certUri: string) : void

卸载用户CA证书。

**需要权限：** ohos.permission.ACCESS\_ENTERPRISE\_USER\_TRUSTED\_CERT

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certUri | string | 是 | 表示待卸载证书的唯一标识符，长度限制256字节以内。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | Indicates that the certificate does not exist. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

let certUri: string = 'test'; /* 业务删除证书，需要使用证书的标识符，此处省略 */
try {
  certificateManager.uninstallUserTrustedCertificateSync(certUri);
} catch (error) {
  console.error(`Failed to uninstall user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.init

init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void

使用凭据进行签名、验签的初始化操作，是签名验签流程的第一步，后续需依次调用update和finish接口完成操作。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| authUri | string | 是 | 表示使用凭据的唯一标识符，长度限制256字节以内。 |
| spec | [CMSignatureSpec](js-apis-certmanager.md#cmsignaturespec) | 是 | 表示签名、验签的属性。 |
| callback | AsyncCallback<[CMHandle](js-apis-certmanager.md#cmhandle)> | 是 | 回调函数。当签名、验签的初始化操作成功时，err为null，data为获取到的CMHandle；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |
| 17500005 | The application is not authorized by the user. Please call [openAuthorizeDialog](js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog20) method to request user authorization for the certificate or credential.  适用版本：12+ |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

let uri: string = 'test'; /* 业务使用凭据进行签名、验签的初始化操作，需要使用凭据的唯一标识符，此处省略 */
const req: certificateManager.CMSignatureSpec = {
  purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_SIGN,
  padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
  digest: certificateManager.CmKeyDigest.CM_DIGEST_SHA256
};
try {
  certificateManager.init(uri, req, (err, cmHandle) => {
    if (err != null) {
      console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in initiating.');
    }
  });
} catch (error) {
  console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.init

init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>

使用凭据进行签名、验签的初始化操作。使用Promise异步回调。

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
| Promise<[CMHandle](js-apis-certmanager.md#cmhandle)> | Promise对象，返回签名、验签的初始化操作结果，返回值为CMHandle对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |
| 17500005 | The application is not authorized by the user.  适用版本：12+ |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 业务使用凭据进行签名、验签的初始化操作，需要使用凭据的唯一标识符，此处省略 */
const req: certificateManager.CMSignatureSpec = {
  purpose: certificateManager.CmKeyPurpose.CM_KEY_PURPOSE_VERIFY,
  padding: certificateManager.CmKeyPadding.CM_PADDING_PSS,
  digest: certificateManager.CmKeyDigest.CM_DIGEST_MD5
};
try {
  certificateManager.init(uri, req).then((handle) => {
    console.info('Succeeded in initiating.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to init. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.update

update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void

签名、验签的数据更新操作，需要在init操作之后调用，用于传入待签名、验签的数据。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示操作句柄，需先调用[init](js-apis-certmanager.md#certificatemanagerinit)方法获得。 |
| data | Uint8Array | 是 | 表示待签名、验签的数据。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当签名、验签的数据更新操作成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let srcData: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.update(cmHandle, srcData, (err) => {
    if (err != null) {
      console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in updating.');
    }
  });
} catch (error) {
  console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.update

update(handle: Uint8Array, data: Uint8Array): Promise<void>

签名、验签的数据更新操作。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示操作句柄，需先调用[init](js-apis-certmanager.md#certificatemanagerinit)方法获得。 |
| data | Uint8Array | 是 | 表示待签名、验签的数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let srcData: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.update(cmHandle, srcData).then(() => {
    console.info('Succeeded in updating.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to update. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to update. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.finish

finish(handle: Uint8Array, callback: AsyncCallback<CMResult>): void

完成签名的操作，是签名流程的最后一步，需要先调用init和update接口。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示操作句柄，需先调用[init](js-apis-certmanager.md#certificatemanagerinit)方法获得。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当签名成功时，err为null，data为[CMResult](js-apis-certmanager.md#cmresult)对象中的outData属性，表示签名数据；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.finish(cmHandle, (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to finish. Code: ${err.code}, message: ${err.message}`);
    } else {
      if (cmResult?.outData != undefined) {
        let signRes = cmResult?.outData;
        console.info('Succeeded in finishing.');
      } else {
        console.info('The result of finishing is undefined.');
      }
    }
  });
} catch (error) {
  console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.finish

finish(handle: Uint8Array, signature: Uint8Array, callback: AsyncCallback<CMResult>): void

完成验签的操作，是验签流程的最后一步，需要先调用init和update接口。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示操作句柄，需先调用[init](js-apis-certmanager.md#certificatemanagerinit)方法获得。 |
| signature | Uint8Array | 是 | 表示签名数据。 |
| callback | AsyncCallback<[CMResult](js-apis-certmanager.md#cmresult)> | 是 | 回调函数。当验签成功时，err为null，data为[CMResult](js-apis-certmanager.md#cmresult)对象中的outData属性，验签时outData属性为null；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
let signRes: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.finish(cmHandle, signRes, (err, cmResult) => {
    if (err != null) {
      console.error(`Failed to finish. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in finishing.');
    }
  });
} catch (error) {
  console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.finish

finish(handle: Uint8Array, signature?: Uint8Array): Promise<CMResult>

完成签名、验签的操作。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示操作句柄，需先调用[init](js-apis-certmanager.md#certificatemanagerinit)方法获得。 |
| signature | Uint8Array | 否 | 表示用于验签操作的签名数据。签名操作时无需传入此参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象。执行签名操作时，返回签名的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的outData属性；执行验签操作时，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  /* 签名的finish操作 */
  certificateManager.finish(cmHandle).then((cmResult) => {
    if (cmResult?.outData != undefined) {
      let signRes1 = cmResult?.outData;
      console.info('Succeeded in finishing signature.');
    } else {
      console.info('The result of signature is undefined.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to finish signature. Code: ${err.code}, message: ${err.message}`);
  });

  /* 签名的结果 */
  let signRes: Uint8Array = new Uint8Array([
    0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
  ]);
  /* 验签的finish操作 */
  certificateManager.finish(cmHandle, signRes).then((cmResult) => {
    console.info('Succeeded in finishing verification.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to finish verification. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to finish. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.abort

abort(handle: Uint8Array, callback: AsyncCallback<void>): void

中止签名、验签的操作。与finish方法互斥，一个签名验签流程只能选择调用其中一个方法。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当中止签名、验签成功时，err为null，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.abort(cmHandle, (err) => {
    if (err != null) {
      console.error(`Failed to abort. Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('Succeeded in aborting.');
    }
  });
} catch (error) {
  console.error(`Failed to abort. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.abort

abort(handle: Uint8Array): Promise<void>

中止签名、验签的操作。与finish方法互斥，一个签名验签流程只能选择调用其中一个方法。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handle | Uint8Array | 是 | 表示初始化操作返回的句柄，最大长度为8字节。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* cmHandle为业务调用init接口的返回值，此处仅为示例 */
let cmHandle: Uint8Array = new Uint8Array([
  0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08
]);
try {
  certificateManager.abort(cmHandle).then(() => {
    console.info('Succeeded in aborting.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to abort. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to abort. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getPublicCertificate12+

getPublicCertificate(keyUri: string): Promise<CMResult>

获取用户公共凭据的详细信息。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示用户公共凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取用户公共凭据详细信息的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的credential属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |
| 17500005 | The application is not authorized by the user. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 用户获取公共凭据详情，需要使用凭据的唯一标识符，此处省略 */
try {
  certificateManager.getPublicCertificate(uri).then((cmResult) => {
    if (cmResult?.credential == undefined) {
      console.info('The result of getting public certificate is undefined.');
    } else {
      let cred = cmResult.credential;
      console.info('Succeeded in getting Public certificate.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get Public certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get Public certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.isAuthorizedApp12+

isAuthorizedApp(keyUri: string): Promise<boolean>

当前应用是否由指定的用户凭据授权。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示用户授权给应用使用的凭据的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回查询应用是否被授权的结果，true为已授权，false为未授权。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string = 'test'; /* 用户授权给应用使用的凭据的唯一标识符，此处省略 */
try {
  certificateManager.isAuthorizedApp(uri).then((res) => {
    if (res) {
      console.info('The application is authorized by the user.');
    } else {
      console.info('The application is not authorized by the user.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to check if the application is authorized. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to check if the application is authorized. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getAllUserTrustedCertificates12+

getAllUserTrustedCertificates(): Promise<CMResult>

获取当前用户和设备公共位置的所有用户根CA证书列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取用户根CA证书列表的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的certList属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getAllUserTrustedCertificates().then((cmResult) => {
    if (cmResult === undefined) { // 用户根CA证书个数为0时，返回cmResult为undefined。
      console.info('The count of the user trusted certificates is 0.');
    } else if (cmResult.certList == undefined) {
      console.info('The result of getting all user trusted certificates is undefined.');
    } else {
      let list = cmResult.certList;
      console.info('Succeeded in getting all user trusted certificates.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get all user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get all user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getAllUserTrustedCertificates18+

getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>

根据证书的位置获取用户根CA证书列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scope | [CertScope](js-apis-certmanager.md#certscope18) | 是 | 表示证书的位置。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取用户根CA证书列表的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的certList属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  /* 获取当前用户下的用户根CA证书列表，如果需要获取设备公共位置的用户根CA列表，则传入GLOBAL_USER */
  let scope: certificateManager.CertScope = certificateManager.CertScope.CURRENT_USER;
  certificateManager.getAllUserTrustedCertificates(scope).then((cmResult) => {
    if (cmResult === undefined) { // 用户根CA证书个数为0时，返回cmResult为undefined。
      console.info('The count of the user trusted certificates is 0.');
    } else if (cmResult.certList == undefined) {
      console.info('The result of getting current user trusted certificates is undefined.');
    } else {
      let list = cmResult.certList;
      console.info('Succeeded in getting current user trusted certificates.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get current user trusted certificates. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get current user trusted certificates. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getUserTrustedCertificate12+

getUserTrustedCertificate(certUri: string): Promise<CMResult>

获取用户根CA证书的详细信息。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| certUri | string | 是 | 表示用户根CA证书的唯一标识符，长度限制256字节以内。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取用户根CA证书详细信息的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的certInfo属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate does not exist. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let certUri: string = 'testUserCert'; /* 用户获取用户根CA证书详情，需要使用CA证书的唯一标识符，此处省略 */
try {
  certificateManager.getUserTrustedCertificate(certUri).then((cmResult) => {
    if (cmResult?.certInfo == undefined) {
      console.info('The result of getting user trusted certificate is undefined.');
    } else {
      let cert = cmResult.certInfo;
      console.info('Succeeded in getting user trusted certificate.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get user trusted certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get user trusted certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getPrivateCertificates13+

getPrivateCertificates(): Promise<CMResult>

获取应用安装的凭据列表。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取应用安装的凭据列表的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的credentialList属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  certificateManager.getPrivateCertificates().then((cmResult) => {
    if (cmResult === undefined) { // 应用安装的凭据个数为0时，返回cmResult为undefined。
      console.info('The count of the private certificates is 0.');
    } else if (cmResult.credentialList == undefined) {
      console.info('The result of getting all private certificates installed by the application is undefined.');
    } else {
      let list = cmResult.credentialList;
      console.info('Succeeded in getting all private certificates installed by the application.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get all private certificates installed by the application. ` +
      `Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get all private certificates installed by the application. ` +
    `Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getCertificateStorePath18+

getCertificateStorePath(property: CertStoreProperty): string

获取证书的存储路径。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. For example, CertStoreProperty.certType is set to CA\_CERT\_USER, but CertStoreProperty.certScope is not specified. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500009 | The device does not support the specified certificate storage path, For example, the device outside China does not support the certificate that uses SM algorithm.  适用版本：20+ |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';

try {
  /* 获取系统CA的存储位置 */
  let property1: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_SYSTEM
  };
  let systemCAPath = certificateManager.getCertificateStorePath(property1);
  console.info(`Succeeded in getting system CA path: ${systemCAPath}`);

  /* 获取当前用户的用户CA存储位置 */
  let property2: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_USER,
    certScope: certificateManager.CertScope.CURRENT_USER
  };
  let userCACurrentPath = certificateManager.getCertificateStorePath(property2);
  console.info(`Succeeded in getting current user's user CA path: ${userCACurrentPath}`);

  /* 获取设备公共的用户CA存储位置 */
  let property3: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_USER,
    certScope: certificateManager.CertScope.GLOBAL_USER
  };
  let globalCACurrentPath = certificateManager.getCertificateStorePath(property3);
  console.info(`Succeeded in getting global user's user CA path: ${globalCACurrentPath}`);

  /* 获取SM算法系统CA的存储位置 */
  let property4: certificateManager.CertStoreProperty = {
    certType: certificateManager.CertType.CA_CERT_SYSTEM,
    certAlg: certificateManager.CertAlgorithm.SM
  };
  let smSystemCAPath = certificateManager.getCertificateStorePath(property4);
  console.info(`Succeeded in getting SM system CA path: ${smSystemCAPath}`);
} catch (error) {
  console.error(`Failed to get store path. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getUkeyCertificate22+

getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>

获取USB Key证书凭据详细信息。使用Promise异步回调。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**设备行为差异：**

* 从API版本26.0.0开始，该接口在Phone、PC/2in1、Tablet设备可正常调用，在其他设备中返回801错误码。
* 在API版本22-24，该接口在PC/2in1设备可正常调用，在其他设备中返回801错误码。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示USB Key证书凭据的唯一标识符，长度限制256字节以内。 |
| ukeyInfo | [UkeyInfo](js-apis-certmanager.md#ukeyinfo22) | 是 | 表示USB Key证书凭据的属性信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取到的USB Key证书凭据详情的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的credentialDetailList属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 801 | Capability not supported. The application does not have the permission required to call the API. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | Indicates that the certificate does not exist. |
| 17500010 | Indicates that access USB Key service failed. |
| 17500011 | Indicates that the input parameters validation failed. For example, the parameter format is incorrect or the value range is invalid. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyUri: string = 'test'; /* USB凭据的唯一标识符，此处省略 */
let ukeyInfo: certificateManager.UkeyInfo = { /* USB凭据的属性信息，此处省略 */
  certPurpose: certificateManager.CertificatePurpose.PURPOSE_DEFAULT
};
try {
  certificateManager.getUkeyCertificate(keyUri, ukeyInfo).then((cmResult) => {
    if (cmResult?.credentialDetailList === undefined) {
      console.info('The result of getting detail of USB Key certificate is undefined.');
    } else {
      let list = cmResult.credentialDetailList;
      console.info('Succeeded in getting detail of USB Key certificate.');
    }
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get detail of USB Key certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get detail of USB Key certificate. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.getUkeyCertificateList

getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise<CMResult>

获取USB Key证书凭据列表。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**设备行为差异：** 该接口在Phone、PC/2in1、Tablet设备可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ukeyProvider | string | 是 | 表示USB Key的设备提供商。 |
| ukeyInfo | [UkeyInfo](js-apis-certmanager.md#ukeyinfo22) | 是 | 表示USB Key证书凭据的属性信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CMResult](js-apis-certmanager.md#cmresult)> | Promise对象，返回获取USB Key证书凭据列表的结果，返回值为[CMResult](js-apis-certmanager.md#cmresult)对象中的credentialDetailList属性。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. |
| 17500010 | Indicates that access USB Key service failed. |
| 17500011 | Parameter verification failed. Possible causes: the ukeyInfo parameter is invalid. For example, the parameter format is incorrect or the value range is invalid. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

let ukeyProvider: string = 'testProvider'; /* USB凭据提供商，此处省略 */
let ukeyInfo: certificateManager.UkeyInfo = { /* USB凭据的属性信息，此处省略 */
  certPurpose: certificateManager.CertificatePurpose.PURPOSE_DEFAULT
};
try {
  certificateManager.getUkeyCertificateList(ukeyProvider, ukeyInfo).then((cmResult) => {
    let list: Array<certificateManager.Credential> = cmResult.credentialDetailList ?? [];
    console.info('Succeeded in getting USB Key certificate list.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to get USB Key certificate list. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to get USB Key certificate list. Code: ${error.code}, message: ${error.message}`);
}
```

## certificateManager.importUkeyCertificate

importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>

导入证书到USB Key。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**系统能力：** SystemCapability.Security.CertificateManager

**设备行为差异：** 该接口在Phone、PC/2in1、Tablet设备可正常调用，在其他设备中返回801错误码。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyUri | string | 是 | 表示USB Key证书凭据的uri。  keyUri参数用于标识证书实体，可以通过调用[getUkeyCertificateList](js-apis-certmanager.md#certificatemanagergetukeycertificatelist)接口得到，最大长度为256字节。 |
| cert | Uint8Array | 是 | 表示待导入的证书数据。最大长度为10KB。  证书数据格式遵循SKF（Smart Key Framework）规范的定义。 |
| ukeyInfo | [UkeyInfo](js-apis-certmanager.md#ukeyinfo22) | 是 | 表示USB Key证书凭据属性信息。  UkeyInfo.CertificatePurpose只能取值为PURPOSE\_SIGN、PURPOSE\_ENCRYPT或PURPOSE\_DEFAULT。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[证书管理错误码](errorcode-certmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. |
| 17500001 | Internal error. Possible causes: 1. IPC communication failed; 2. Memory operation error; 3. File operation error. Please try again. |
| 17500002 | The certificate identified by keyUri does not exist. |
| 17500010 | Indicates that access USB Key service failed. |
| 17500011 | Indicates that the input parameters validation failed. For example, the parameter format is incorrect or the value range is invalid. |

**示例**：

```ts
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

/* keyUri和cert数据需要业务赋值，本例数据仅为示例 */
let keyUri: string = 'test'; /* USB Key证书的uri，可通过getUkeyCertificateList获取 */
let certData: Uint8Array = new Uint8Array([
  0x30, 0x82, 0x0b, 0xc1, 0x02, 0x01
]);
let ukeyInfo: certificateManager.UkeyInfo = {
  certPurpose: certificateManager.CertificatePurpose.PURPOSE_SIGN
};
try {
  certificateManager.importUkeyCertificate(keyUri, certData, ukeyInfo).then(() => {
    console.info('Succeeded in importing USB Key certificate.');
  }).catch((error: Error) => {
    let err = error as BusinessError;
    console.error(`Failed to import USB Key certificate. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  console.error(`Failed to import USB Key certificate. Code: ${error.code}, message: ${error.message}`);
}
```
