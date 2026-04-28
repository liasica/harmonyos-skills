---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-networksecurity
title: @ohos.net.networkSecurity (网络安全校验)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.networkSecurity (网络安全校验)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:618d72fb9da2f61eee98d68451e9dcee8e39a59f129df7ae7602e3718b2d1416
---

本模块提供网络安全校验能力。应用可以通过证书校验API完成证书校验功能。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { networkSecurity } from '@kit.NetworkKit';
```

## 完整示例

PhonePC/2in1TabletTVWearable

```
1. import { networkSecurity } from '@kit.NetworkKit';

3. // Define certificate blobs
4. const cert: networkSecurity.CertBlob = {
5. type: networkSecurity.CertType.CERT_TYPE_PEM,
6. data: '-----BEGIN CERTIFICATE-----\n... (certificate data) ...\n-----END CERTIFICATE-----',
7. };

9. const caCert: networkSecurity.CertBlob = {
10. type: networkSecurity.CertType.CERT_TYPE_PEM,
11. data: '-----BEGIN CERTIFICATE-----\n... (CA certificate data) ...\n-----END CERTIFICATE-----',
12. };

14. // Perform asynchronous certificate verification
15. networkSecurity.certVerification(cert, caCert)
16. .then((result) => {
17. console.info('Certificate verification result:', result);
18. })
19. .catch((error: BusinessError) => {
20. console.error('Certificate verification failed:', error);
21. });
```

注意

请务必将示例中的证书数据替换为实际的证书内容。

## CertType

PhonePC/2in1TabletTVWearable

证书编码类型。

**系统能力**: SystemCapability.Communication.NetStack

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CERT\_TYPE\_PEM | 0 | PEM格式证书。 |
| CERT\_TYPE\_DER | 1 | DER格式证书。 |

## CertBlob

PhonePC/2in1TabletTVWearable

证书数据。

**系统能力**: SystemCapability.Communication.NetStack

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | CertType | 否 | 否 | 证书编码类型。 |
| data | string | ArrayBuffer | 否 | 否 | 证书内容。 |

## networkSecurity.certVerification

PhonePC/2in1TabletTVWearable

certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>

系统将使用证书管理中的预置CA证书和用户安装的CA证书来校验应用传入的证书。使用Promise异步回调。

**系统能力**: SystemCapability.Communication.NetStack

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | CertBlob | 是 | 被校验的证书。 |
| caCert | CertBlob | 否 | 传入自定义的CA证书。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以promise形式返回一个数字，表示证书验证的结果。如果证书验证成功，则返回0； 否则验证失败。 |

**错误码：**

以下错误码的详细介绍请参见[网络安全校验错误码](errorcode-net-networksecurity.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2305001 | Unspecified error. |
| 2305002 | Unable to get issuer certificate. |
| 2305003 | Unable to get certificate revocation list (CRL). |
| 2305004 | Unable to decrypt certificate signature. |
| 2305005 | Unable to decrypt CRL signature. |
| 2305006 | Unable to decode issuer public key. |
| 2305007 | Certificate signature failure. |
| 2305008 | CRL signature failure. |
| 2305009 | Certificate is not yet valid. |
| 2305010 | Certificate has expired. |
| 2305011 | CRL is not yet valid. |
| 2305012 | CRL has expired. |
| 2305018 | Self-signed certificate. |
| 2305023 | Certificate has been revoked. |
| 2305024 | Invalid certificate authority (CA). |
| 2305027 | Certificate is untrusted. |
| 2305069 | Invalid certificate verification context. |

说明

这些错误代码对应于证书验证过程中的各种失败。

**示例：**

```
1. import { networkSecurity } from '@kit.NetworkKit';

3. // Define certificate blobs
4. const cert:networkSecurity.CertBlob = {
5. type: networkSecurity.CertType.CERT_TYPE_PEM,
6. data: '-----BEGIN CERTIFICATE-----\n... (certificate data) ...\n-----END CERTIFICATE-----',
7. };

9. const caCert:networkSecurity.CertBlob = {
10. type: networkSecurity.CertType.CERT_TYPE_PEM,
11. data: '-----BEGIN CERTIFICATE-----\n... (CA certificate data) ...\n-----END CERTIFICATE-----',
12. };

14. // Perform asynchronous certificate verification
15. networkSecurity.certVerification(cert, caCert)
16. .then((result) => {
17. console.info('Certificate verification result:', result);
18. })
19. .catch((error: BusinessError) => {
20. console.error('Certificate verification failed:', error);
21. });
```

注意

请务必将示例中的证书数据替换为实际的证书内容。

## networkSecurity.certVerificationSync

PhonePC/2in1TabletTVWearable

certVerificationSync(cert: CertBlob, caCert?: CertBlob): number

系统将使用证书管理中的预置CA证书和用户安装的CA证书来校验应用传入的证书，使用同步方式返回。

**系统能力**：SystemCapability.Communication.NetStack

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cert | CertBlob | 是 | 被校验的证书。 |
| caCert | CertBlob | 否 | 传入自定义的CA证书。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 表示证书验证的结果。如果证书验证成功，则返回0； 否则验证失败。 |

**错误码：**

以下错误码的详细介绍请参见[网络安全校验错误码](errorcode-net-networksecurity.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2305001 | Unspecified error. |
| 2305002 | Unable to get issuer certificate. |
| 2305003 | Unable to get certificate revocation list (CRL). |
| 2305004 | Unable to decrypt certificate signature. |
| 2305005 | Unable to decrypt CRL signature. |
| 2305006 | Unable to decode issuer public key. |
| 2305007 | Certificate signature failure. |
| 2305008 | CRL signature failure. |
| 2305009 | Certificate is not yet valid. |
| 2305010 | Certificate has expired. |
| 2305011 | CRL is not yet valid. |
| 2305012 | CRL has expired. |
| 2305018 | Self-signed certificate. |
| 2305023 | Certificate has been revoked. |
| 2305024 | Invalid certificate authority (CA). |
| 2305027 | Certificate is untrusted. |
| 2305069 | Invalid certificate verification context. |

说明

这些错误代码对应于证书验证过程中的各种失败。

**示例：**

```
1. import { networkSecurity } from '@kit.NetworkKit';

3. // Create certificate blobs
4. const cert: networkSecurity.CertBlob = {
5. type: networkSecurity.CertType.CERT_TYPE_PEM,
6. data: '-----BEGIN CERTIFICATE-----\n...'
7. };

9. const caCert: networkSecurity.CertBlob = {
10. type: networkSecurity.CertType.CERT_TYPE_PEM,
11. data: '-----BEGIN CERTIFICATE-----\n...'
12. };

14. // Asynchronous verification
15. networkSecurity.certVerification(cert, caCert)
16. .then((result) => {
17. console.info('Verification Result:', result);
18. })
19. .catch((error: BusinessError) => {
20. console.error('Verification Error:', error);
21. });

23. // Synchronous verification
24. let resultSync: number = networkSecurity.certVerificationSync(cert, caCert);
25. console.info('Synchronous Verification Result:', resultSync);
```

注意

请务必将示例中的证书数据替换为实际的证书内容。

## networkSecurity.isCleartextPermitted18+

PhonePC/2in1TabletTVWearable

isCleartextPermitted(): boolean

从应用预置network\_config.json文件中获取整体明文HTTP是否允许信息，默认允许明文HTTP访问。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 整体明文HTTP是否允许。返回true表示允许访问明文HTTP，false表示不允许。默认返回true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { networkSecurity } from '@kit.NetworkKit';

3. try {
4. let result: boolean = networkSecurity.isCleartextPermitted();
5. console.info(`isCleartextPermitted Result: ${JSON.stringify(result)}`);
6. } catch (error) {
7. console.error(`isCleartextPermitted Error: ${JSON.stringify(error)}`);
8. }
```

## networkSecurity.isCleartextPermittedByHostName18+

PhonePC/2in1TabletTVWearable

isCleartextPermittedByHostName(hostName: string): boolean

从应用预置network\_config.json文件中获取按域名明文HTTP是否允许信息，默认允许明文HTTP访问。

**需要权限**：ohos.permission.INTERNET

**系统能力**：SystemCapability.Communication.NetStack

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| hostName | string | 是 | 需要查询的主机名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 按域名明文HTTP是否允许。返回true表示允许明文HTTP访问该主机，false表示不允许。默认返回true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { networkSecurity } from '@kit.NetworkKit';

3. try {
4. let result: boolean = networkSecurity.isCleartextPermittedByHostName("xxx");
5. console.info(`isCleartextPermitted Result: ${JSON.stringify(result)}`);
6. } catch (error) {
7. console.error(`isCleartextPermitted Error: ${JSON.stringify(error)}`);
8. }
```
