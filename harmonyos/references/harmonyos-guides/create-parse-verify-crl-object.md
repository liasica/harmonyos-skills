---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-parse-verify-crl-object
title: 证书吊销列表对象的创建、解析和校验
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书吊销列表对象的创建、解析和校验
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:58d4cf03942c5ffeab5112230ae8585fbe74e04d129a4d63e8445cc88b05f069
---

以校验证书是否已吊销为例，完成证书吊销列表对象的创建、解析和校验。若证书已被吊销，将打印被吊销日期。

## 开发步骤

1. 导入[证书模块](../harmonyos-references/js-apis-cert.md)和[加解密算法库框架](../harmonyos-references/js-apis-cryptoframework.md)。

   ```ts
   import { cert } from '@kit.DeviceCertificateKit';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   ```
2. 基于已有的CRL数据，调用[cert.createX509CRL](../harmonyos-references/js-apis-cert.md#certcreatex509crl11)创建X.509证书吊销列表的对象。
3. 解析证书吊销列表信息。

   此处以获取证书吊销列表版本、证书吊销列表类型、证书吊销列表颁发者名称、证书吊销列表对象的字符串类型数据为例，更多字段信息获取接口请查看API参考文档[X509CRL11+](../harmonyos-references/js-apis-cert.md#x509crl11)。
4. 基于已有公钥信息，创建PublicKey公钥对象。

   具体可参考加解密算法库框架-指定二进制数据生成非对称密钥对[convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey-3)。
5. 调用[X509CRL.verify](../harmonyos-references/js-apis-cert.md#verify11)校验签名合法性。
6. 基于已有的X.509证书数据，调用[cert.createX509Cert](../harmonyos-references/js-apis-cert.md#certcreatex509cert)创建证书对象。
7. 调用[X509CRL.isRevoked](../harmonyos-references/js-apis-cert.md#isrevoked11)判断X.509证书是否已被吊销。
8. 调用[X509CRL.getRevokedCert](../harmonyos-references/js-apis-cert.md#getrevokedcert11)获取被吊销证书对象。
9. 调用[X509CRLEntry.getRevocationDate](../harmonyos-references/js-apis-cert.md#getrevocationdate11)获取被吊销日期。

```typescript
import { cert } from '@kit.DeviceCertificateKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

// ...
// CRL示例
function crlSample(): void {
  let textEncoder = new util.TextEncoder();
  let encodingBlob: cert.EncodingBlob = {
    // 将CRL数据从string转为Uint8Array。
    data: textEncoder.encodeInto(crlData),
    // CRL格式，仅支持PEM和DER格式。在这个例子中，CRL用的是PEM格式。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };

  // 创建X509CRL实例。
  cert.createX509CRL(encodingBlob, (err, x509Crl) => {
    if (err != null) {
      // 创建X509CRL实例失败。
      console.error(`createX509Crl failed, errCode: ${err.code}, errMsg:${err.message} `);
      return;
    }
    // 创建X509CRL实例成功。
    console.info('createX509CRL result: success.');

    // 获取CRL的版本。
    let version = x509Crl.getVersion();
    // 获取证书吊销列表类型。
    let revokedType = x509Crl.getType();
    console.info(`X509 CRL version: ${version}, type :${revokedType}`);

    // 获取证书吊销列表颁发者名称。
    let issuerName = x509Crl.getIssuerName(cert.EncodingType.ENCODING_UTF8);
    console.info(`X509 CRL issuerName: ${issuerName}`);

    // 获取证书吊销列表对象的字符串类型数据。
    let crlString = x509Crl.toString(cert.EncodingType.ENCODING_UTF8);
    console.info(`X509 CRL crlString: ${crlString}`);

    // 公钥的二进制数据需要传入@ohos.security.cryptoFramework的convertKey()方法去获取公钥对象。
    try {
      let keyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024|PRIMES_3');
      console.info('createAsyKeyGenerator result: success.');
      let pubEncodingBlob: cryptoFramework.DataBlob = {
        data: pubKeyData,
      };
      keyGenerator.convertKey(pubEncodingBlob, null, (e, keyPair) => {
        if (e == null) {
          console.info('convertKey result: success.');
          x509Crl.verify(keyPair.pubKey, (err, data) => {
            if (err == null) {
              // 签名验证成功。
              console.info('verify result: success.');
            } else {
              // 签名验证失败。
              console.error(`verify failed, errCode: ${err.code}, errMsg: ${err.message}`);
            }
          });
        } else {
          console.error(`convert key failed, errCode: ${e.code}, errMsg: ${e.message}`);
        }
      })
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`get pubKey failed, errCode: ${e.code}, errMsg: ${e.message}`);
    }

    // 使用certFramework的createX509Cert()方法创建一个X509Cert实例。
    let certBlob: cert.EncodingBlob = {
      data: textEncoder.encodeInto(certData),
      encodingFormat: cert.EncodingFormat.FORMAT_PEM
    };
    let revokedFlag = true;
    let serial: bigint = BigInt('0');
    cert.createX509Cert(certBlob, (err, x509Cert) => {
      if (err == null) {
        try {
          serial = x509Cert.getCertSerialNumber();
          // 检查证书是否被吊销。
          revokedFlag = x509Crl.isRevoked(x509Cert);
          console.info(`revokedFlag is: ${revokedFlag}`);
          if (!revokedFlag) {
            console.info('the given x509Cert is not revoked.');
            return;
          }
          // 根据序列号来获取被吊销的证书。
          try {
            let crlEntry = x509Crl.getRevokedCert(serial);
            console.info('getRevokedCert result: success.');
            let serialNumber = crlEntry.getSerialNumber();
            console.info(`crlEntry serialNumber is: ${serialNumber}`);

            // 获取被吊销证书的吊销日期。
            let date = crlEntry.getRevocationDate();
            console.info(`revocation date is: ${date}`);
          } catch (error) {
            let e: BusinessError = error as BusinessError;
            console.error(`getRevokedCert failed, errCode: ${e.code}, errMsg: ${e.message}`);
          }
        } catch (error) {
          let e: BusinessError = error as BusinessError;
          console.error(`isRevoked failed, errCode: ${e.code}, errMsg:${e.message}`);
        }
      } else {
        console.error(`create x509 cert failed, errCode: ${err.code}, errMsg: ${err.message}`);
      }
    })

  });
}
```
