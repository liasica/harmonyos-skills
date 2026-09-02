---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/verify-certchain-by-systemca
title: 使用系统预置CA证书校验证书链
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 使用系统预置CA证书校验证书链
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9a40df7575a5276cc19f3d225443fa8ff171b66ea11c3a28c502fd06eb1f7565
---

从API version 20开始，支持使用系统预置CA证书校验证书链。

以校验证书链为例，完成证书链对象的创建，使用系统预置CA证书对证书链进行校验。

## 开发步骤

1. 导入[证书模块](../harmonyos-references/js-apis-cert.md)。

   ```ts
   import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 基于已有的证书数据，调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11)创建X.509证书链对象，并返回结果。
3. 调用[x509CertChain.validate](../harmonyos-references/js-apis-cert.md#validate11)设置校验参数trustSystemCa为true，使用系统预置CA证书校验证书链并返回结果。

```typescript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';
// ...
async function sample() {
  let textEncoder = new util.TextEncoder();
  // 证书链二进制数据，需业务自行赋值。
  const encodingBlob: cert.EncodingBlob = {
    data: textEncoder.encodeInto(certChainData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
  try {
    x509CertChain = await cert.createX509CertChain(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }

  // 证书链校验数据，需业务自行赋值。
  const param: cert.CertChainValidationParameters = {
    date: '20250623163000Z',
    trustAnchors: [{}],
    trustSystemCa: true,
  };
  try {
    const validationRes = await x509CertChain.validate(param);
    console.info('X509CertChain validate result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`X509CertChain validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
}
```
