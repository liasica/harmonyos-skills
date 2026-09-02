---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-and-verify-cert-chain
title: 构建并校验证书链
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 构建并校验证书链
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2cddec9f1280005db9e7c2dabecead5a853623dd465c163a3f36d5a5210bde06
---

从API版本26.0.0开始，证书链校验器提供证书链构建和校验能力，支持通过[CertValidationParams](../harmonyos-references/js-apis-cert.md#certvalidationparams)参数配置构建和校验行为，包括信任锚设置、证书吊销检查、日期校验等。

## 开发步骤

1. 导入[@ohos.security.cert](../harmonyos-references/js-apis-cert.md)。

   ```ts
   import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 基于已有的证书数据，创建待校验[X509Cert](../harmonyos-references/js-apis-cert.md#x509cert)证书对象。
3. 调用[cert.createCertChainValidator](../harmonyos-references/js-apis-cert.md#certcreatecertchainvalidator)接口创建证书链校验器对象。
4. 创建[CertValidationParams](../harmonyos-references/js-apis-cert.md#certvalidationparams)校验参数对象。
5. 调用[validateCert(cert: X509Cert, params: CertValidationParams): Promise<CertValidationResult>](../harmonyos-references/js-apis-cert.md#validatecert)接口构建并校验证书链，返回校验成功的证书链[CertValidationResult](../harmonyos-references/js-apis-cert.md#certvalidationresult)。

## 场景一：指定信任证书

当应用有自定义的信任锚证书时，可以通过[trustedCerts](../harmonyos-references/js-apis-cert.md#certvalidationparams)参数指定信任的CA证书。

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
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
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

async function validateCertChainWithCustomTrustAnchor(): Promise<void> {
  try {
    // 创建证书对象
    let endEntityCert = await createX509Cert(endEntityCertData);
    let intermediateCaCert = await createX509Cert(intermediateCaCertData);
    let rootCaCert = await createX509Cert(rootCaCertData);

    // 构建校验参数
    let params: cert.CertValidationParams = {
      // 不信任的中间证书，用于构建证书链
      untrustedCerts: [intermediateCaCert],
      // 信任锚证书，用于验证证书链
      trustedCerts: [rootCaCert],
      // 不信任系统预置CA证书
      trustSystemCa: false,
      date: '20260422121212Z'
    };
    // 创建证书链校验器实例
    let validator = cert.createCertChainValidator('PKIX');

    // 验证endEntityCert
    let result: cert.CertValidationResult = await validator.validateCert(endEntityCert, params);
    console.info('validate success, certChain length: ' + result.certChain.length);
    for (let i = 0; i < result.certChain.length; i++) {
      let subject = result.certChain[i].getSubjectX500DistinguishedName().getName(cert.EncodingType.ENCODING_UTF8);
      console.info(`Cert ${i} subject: ${subject}`);
    }
  } catch (err) {
    // 校验失败
    let error = err as BusinessError;
    console.error('validate failed, errCode: ' + error.code + ', errMsg: ' + error.message);
    throw new Error(error.message)
  }
}
```

## 场景二：信任系统预置CA证书

当应用需要验证互联网公开证书（如HTTPS网站证书）时，可以使用系统预置的CA证书作为信任锚。通过设置[trustSystemCa](../harmonyos-references/js-apis-cert.md#certvalidationparams)为true，校验器会使用系统预置CA证书库构建并验证证书链。

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
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
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

async function validateCertChainWithSystemCa(): Promise<void> {
  try {
    // 创建证书对象
    let endEntityCert = await createX509Cert(endEntityCertData);
    let intermediateCaCert = await createX509Cert(intermediateCaCertData);

    // 构建校验参数
    let params: cert.CertValidationParams = {
      // 不信任的中间证书，用于构建证书链
      untrustedCerts: [intermediateCaCert],
      // 信任系统预置CA证书
      trustSystemCa: true,
      // 忽略证书过期或未生效
      ignoreErrs: [cert.CertResult.ERR_CERT_HAS_EXPIRED, cert.CertResult.ERR_CERT_NOT_YET_VALID],
    };

    // 创建证书链校验器实例
    let validator = cert.createCertChainValidator('PKIX');

    // 验证endEntityCert
    let result: cert.CertValidationResult = await validator.validateCert(endEntityCert, params);
    console.info('validate success, certChain length: ' + result.certChain.length);
    for (let i = 0; i < result.certChain.length; i++) {
      let subject = result.certChain[i].getSubjectX500DistinguishedName().getName(cert.EncodingType.ENCODING_UTF8);
      console.info(`Cert ${i} subject: ${subject}`);
    }
  } catch (err) {
    let error = err as BusinessError;
    console.error('validate failed, errCode: ' + error.code + ', errMsg: ' + error.message);
    throw new Error(error.message)
  }
}
```

## 场景三：证书吊销校验（CRL）

可以通过[crls](../harmonyos-references/js-apis-cert.md#x509certrevokedparams)参数指定CRL，用来检查证书是否被吊销。

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
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
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

async function createX509CRL(crlDataStr: string): Promise<cert.X509CRL> {
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(crlDataStr),
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  let x509CRL: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509CRL = await cert.createX509CRL(encodingBlob);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`createX509CRL failed: errCode: ${e.code}, message: ${e.message}`);
  }
  return x509CRL;
}

async function validateCertChainWithCrl(): Promise<void> {
  try {
    // 创建证书对象
    let endEntityCert = await createX509Cert(endEntityCertData);
    let intermediateCaCert = await createX509Cert(intermediateCaCertData);
    let rootCaCert = await createX509Cert(rootCaCertData);

    // 创建CRL对象
    let crl = await createX509CRL(crlData);

    // 构建吊销校验参数
    let revokedParams: cert.X509CertRevokedParams = {
      // 启用CRL检查
      revocationFlags: [cert.CertRevocationFlag.CERT_REVOCATION_CRL_CHECK],
      // 提供CRL列表
      crls: [crl]
    };

    // 构建校验参数
    let params: cert.CertValidationParams = {
      untrustedCerts: [intermediateCaCert],
      trustedCerts: [rootCaCert],
      trustSystemCa: false,
      // 不校验证书有效期（仅用于示例，实际场景建议开启）
      validateDate: false,
      // 设置吊销校验参数
      revokedParams: revokedParams,
    };

    // 创建证书链校验器实例
    let validator = cert.createCertChainValidator('PKIX');

    // 验证endEntityCert
    let result: cert.CertValidationResult = await validator.validateCert(endEntityCert, params);
    console.info('validate success, certChain length: ' + result.certChain.length);
    for (let i = 0; i < result.certChain.length; i++) {
      let subject = result.certChain[i].getSubjectX500DistinguishedName().getName(cert.EncodingType.ENCODING_UTF8);
      console.info(`Cert ${i} subject: ${subject}`);
    }
  } catch (err) {
    let error = err as BusinessError;
    if (error.code === cert.CertResult.ERR_CERT_HAS_REVOKED) {
      console.error('certificate has been revoked');
    } else {
      console.error('validate failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      throw new Error(error.message)
    }
  }
}
```

## 场景四：国密证书链校验

国密SM2证书链校验，通常需要设置[userId](../harmonyos-references/js-apis-cert.md#certvalidationparams)参数。

```typescript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

function stringToUint8Array(str: string): Uint8Array {
  const encoder = new util.TextEncoder();
  return encoder.encodeInto(str);
}

// ...

async function createX509Cert(certData: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(certData),
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

async function validateSm2CertChain(): Promise<void> {
  try {
    let sm2EndEntityCert = await createX509Cert(sm2EndEntityCertData);
    let sm2IntermediateCaCert = await createX509Cert(sm2IntermediateCaCertData);
    let sm2RootCaCert = await createX509Cert(sm2RootCaCertData);

    let userId = new Uint8Array([
      0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38,
      0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38
    ]);

    let params: cert.CertValidationParams = {
      // 不信任的中间证书，用于构建证书链
      untrustedCerts: [sm2IntermediateCaCert],
      // 信任锚证书，用于验证证书链
      trustedCerts: [sm2RootCaCert],
      // 不校验证书有效期（仅用于示例，实际场景建议开启）
      validateDate: false,
      // sm2验签使用的用户ID
      userId: userId
    };
    // 创建证书链校验器实例
    let validator = cert.createCertChainValidator('PKIX');

    // 验证sm2EndEntityCert证书
    let result: cert.CertValidationResult = await validator.validateCert(sm2EndEntityCert, params);
    console.info('validate success, certChain length: ' + result.certChain.length);
    for (let i = 0; i < result.certChain.length; i++) {
      let subject = result.certChain[i].getSubjectX500DistinguishedName().getName(cert.EncodingType.ENCODING_UTF8);
      console.info(`Cert ${i} subject: ${subject}`);
      let alg = result.certChain[i].getSignatureAlgName()
      console.info(`Cert ${i} Signature Algorithm: ${alg}`);
    }
  } catch (err) {
    let error = err as BusinessError;
    console.error('validate failed, errCode: ' + error.code + ', errMsg: ' + error.message);
    throw new Error(error.message)
  }
}
```
