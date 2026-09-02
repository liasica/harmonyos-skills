---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-verify-cerchainvalidator-revocation-object
title: 证书链在线校验证书吊销状态
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书链在线校验证书吊销状态
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6151e20f2845a337a283012edaa480d11c83c0a219556519bc7c6ca8ce7766b9
---

## 本地证书链吊销状态校验时仅校验终端实体证书

API 22开始支持本地证书链吊销状态校验时仅校验终端实体证书。

### 开发步骤

1. 导入[证书模块](../harmonyos-references/js-apis-cert.md)。

   ```ts
   import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11)创建证书链对象。
3. 调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建X.509证书对象。
4. 调用[cert.createX509CRL](../harmonyos-references/js-apis-cert.md#certcreatex509crl11)创建X.509证书吊销列表对象。
5. 构造[cert.CertChainValidationParameters](../harmonyos-references/js-apis-cert.md#certchainvalidationparameters11)证书链校验参数对象。
6. 调用[cert.validate](../harmonyos-references/js-apis-cert.md#validate11)，传入证书链校验参数，进行证书链校验。

本地仅校验终端实体证书的吊销状态示例：

```typescript
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createCertChain(certData: string): Promise<cert.X509CertChain> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = await cert.createX509CertChain(encodingBlob);
  } catch (err) {
    console.error(`createCertChain failed: errCode: ${err.code}, message: ${err.message}`);
  }
  return x509CertChain;
}

async function createCert(certData: string): Promise<cert.X509Cert> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    console.error(`createCert failed: errCode: ${err.code}, message: ${err.message}`);
  }
  return x509Cert;
}

export async function createCRL(crlPem: string): Promise<cert.CertCRLCollection> {
  try {
    let crlEncodingBlob: cert.EncodingBlob = {
      data: stringToUint8Array(crlPem),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
    }
    let crl: cert.X509CRL = await cert.createX509CRL(crlEncodingBlob);
    let collection: cert.CertCRLCollection = cert.createCertCRLCollection([], [crl]);
    return collection;
  } catch (error) {
    throw error as Error;
  }
}
// ...
async function doTestLeafCertCrlCheck() {
  try {
    let x509CertChain: cert.X509CertChain = await createCertChain(certChainData);
    let x509Cert: cert.X509Cert = await createCert(trustRootCertPem);
    let caCollection: cert.CertCRLCollection = await createCRL(crl);
    const param: cert.CertChainValidationParameters = {
      date: '20250926080000Z',
      trustAnchors: [{
        CACert: x509Cert
      }],
      certCRLs: [caCollection],
      revocationCheckParam: {
        options: [
          cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT
        ],
      }
    };
    await x509CertChain.validate(param);
    console.info(`validate result: success.`);
  } catch (error) {
    console.error(`x509CertChain validate failed: errCode: ${error.code}, message: ${error.message}`);
  }
}
```

## 在线校验证书链中的中间CA证书的吊销状态

从API version 22开始，支持在线校验证书链中的中间CA证书的吊销状态。

### 开发步骤

1. 导入[证书模块](../harmonyos-references/js-apis-cert.md)。

   ```ts
   import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11)创建证书链对象。
3. 调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建X.509证书对象。
4. 构造[cert.CertChainValidationParameters](../harmonyos-references/js-apis-cert.md#certchainvalidationparameters11)证书链校验参数。
5. 调用[cert.validate](../harmonyos-references/js-apis-cert.md#validate11)，传入证书链校验参数，进行证书链校验。

**说明** 

本开发指导中提供的示例代码需要在配置网络的前提下执行。

在线校验中间证书的吊销状态示例：

```typescript
import { cert } from '@kit.DeviceCertificateKit';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function createCertChain(certData: string): Promise<cert.X509CertChain> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = await cert.createX509CertChain(encodingBlob);
  } catch (err) {
    console.error(`createCertChain failed: errCode: ${err.code}, message: ${err.message}`);
  }
  return x509CertChain;
}

async function createCert(certData: string): Promise<cert.X509Cert> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    console.error(`createCert failed: errCode: ${err.code}, message: ${err.message}`);
  }
  return x509Cert;
}

// ...
async function doTestCaCheck() {
  try {
    let x509CertChain: cert.X509CertChain = await createCertChain(caChain);
    let x509Cert: cert.X509Cert = await createCert(caTrustCert);
    const param: cert.CertChainValidationParameters = {
      trustAnchors: [{
        CACert: x509Cert
      }],
      revocationCheckParam: {
        options: [
          cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_ACCESS_NETWORK,
          cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE
        ],
      }
    };
    await x509CertChain.validate(param);
    console.info(`validate result: success.`);
  } catch (error) {
    console.error(`x509CertChain validate failed: errCode: ${error.code}, message: ${error.message}`);
  }
}
```

## 证书链校验时忽略在线证书吊销检查的网络不可达异常

从API version 23开始，支持证书链校验时忽略网络不可达的在线证书吊销检查异常。

### 开发步骤

1. 导入[证书模块](../harmonyos-references/js-apis-cert.md)。

   ```ts
   import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11-2)创建证书链对象。
3. 调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建X.509证书对象。构造 cert.CertChainValidationParameters 证书链校验参数，配置 revocationCheckParam 为 RevocationCheckOptions.REVOCATION\_CHECK\_OPTION\_IGNORE\_NETWORK\_ERROR，以忽略网络不可达的情况。
4. 调用[cert.validate](../harmonyos-references/js-apis-cert.md#validate11)，传入证书链校验参数，进行证书链校验。

在线CRL检查忽略网络不可达异常示例：

```typescript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  const encoder = new util.TextEncoder();
  return encoder.encodeInto(str);
}
// ...
async function createX509Cert(certData: string): Promise<cert.X509Cert> {
  // 证书二进制数据，需业务自行赋值。
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509Cert failed: errCode: ${e.code}, message: ${e.message}`);
  }
  return x509Cert;
}

async function createX509CertChain(): Promise<cert.X509CertChain> {
  const root = await createX509Cert(rootCert);
  const intermediate = await createX509Cert(intermediateCert);
  const leaf = await createX509Cert(leafCert);
  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = cert.createX509CertChain([leaf, intermediate, root]);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CertChain failed: errCode: ${e.code}, message: ${e.message}`);
  }
  return x509CertChain;
}

async function validateCRL() {
  const certChain = await createX509CertChain();
  console.info('createX509CertChain result: success.');
  const root = await createX509Cert(rootCert);
  // 证书链校验数据，需业务自行赋值。
  const param: cert.CertChainValidationParameters = {
    trustAnchors: [{ CACert: root }],
    revocationCheckParam: {
      options: [
        cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_IGNORE_NETWORK_ERROR,
        cert.RevocationCheckOptions.REVOCATION_CHECK_OPTION_ACCESS_NETWORK
      ],
    }
  }
  try {
    await certChain.validate(param);
    console.info('validateCRL result: success.');
  } catch (err) {
    console.error(`X509CertChain validate failed: errCode: ${err.code}, message: ${err.message}`);
  }
}
```
