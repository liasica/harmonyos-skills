---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sm2-sign-data-format-conversion
title: SM2签名数据格式转换(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 签名验签介绍及算法规格 > SM2签名数据格式转换(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50c10a39799385f0b62ecf649aaa10e91c9a9c06d5693274ffc4ba517b057933
---

当前支持DER格式与（r、s）格式互转的能力。

开发者可指定SM2签名数据，将其转换成DER格式密文。反之，也可以从DER格式密文中取出具体的SM2签名数据。

**指定密文参数，转换为DER格式**

1. 构造[EccSignatureSpec](../harmonyos-references/js-apis-cryptoframework.md#eccsignaturespec20)对象，用于指定SM2密文参数。
2. 调用[genEccSignature](../harmonyos-references/js-apis-cryptoframework.md#geneccsignature20)，将EccSignatureSpec对象传入，转换为DER格式的SM2密文。

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testSm2SignDataRsToDer() {
  try {
    let spec: cryptoFramework.EccSignatureSpec = {
      r: BigInt('97726608965854271693043443511967021777934035174185659091642456228829830775155'),
      s: BigInt('23084224202834231287427338597254751764391338275617140205467537273296855150376'),
    };

    let data = cryptoFramework.SignatureUtils.genEccSignature(spec);
    console.info('genEccSignature result: success.');
    console.info('data = ' + data);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`ecc failed: errCode: ${e.code}, message: ${e.message}`);
  }
}
```

**指定DER格式，转换为（r、s）格式**

1. 指定DER格式的SM2密文参数。
2. 调用[genEccSignatureSpec](../harmonyos-references/js-apis-cryptoframework.md#geneccsignaturespec20)，将DER格式数据传入，转换为（r、s）格式的SM2密文。

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testSm2SignDataDerToRs() {
  try {
    let data =
      new Uint8Array([48, 69, 2, 33, 0, 216, 15, 76, 238, 158, 165, 108, 76, 72, 63, 115, 52, 255, 51, 149, 54, 224,
        179, 49, 225, 70, 36, 117, 88, 154, 154, 27, 194, 161, 3, 1, 115, 2, 32, 51, 9, 53, 55, 248, 82, 7, 159, 179,
        144, 57, 151, 195, 17, 31, 106, 123, 32, 139, 219, 6, 253, 62, 240, 181, 134, 214, 107, 27, 230, 175, 40]);
    let spec: cryptoFramework.EccSignatureSpec = cryptoFramework.SignatureUtils.genEccSignatureSpec(data);
    console.info('genEccSignatureSpec result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`ecc failed: errCode: ${e.code}, message: ${e.message}`);
  }
}
```
