---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-trustanchor-from-p12
title: "证书链校验时从PKCS #12文件构造TrustAnchor对象数组"
breadcrumb: "指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书链校验时从PKCS #12文件构造TrustAnchor对象数组"
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:01+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:390701992b937bec8c8317b9dcf1e7d85a85670758d793f6e067cbb68241721b
---

证书链校验时从PKCS #12文件构造TrustAnchor对象数组。

## 开发步骤

1. 导入[证书模块](../harmonyos-references/js-apis-cert.md)。
2. 基于现有的PKCS #12文件数据，调用[cert.createTrustAnchorsWithKeyStore](../harmonyos-references/js-apis-cert.md#certcreatetrustanchorswithkeystore12)创建[X509TrustAnchor](../harmonyos-references/js-apis-cert.md#x509trustanchor11)数组对象，并返回结果。

```typescript
import { cert } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

function test() {
  // ...
  try {
    cert.createTrustAnchorsWithKeyStore(p12Data, '123456').then((data) => {
      console.info('createTrustAnchorsWithKeyStore result: success, the num of result is :' + data.length);
    }).catch((err: BusinessError) => {
      console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${err.code}, message: ${err.message}`);
    })
  } catch (error) {
    console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${error.code}, message: ${error.message}`);
  }
}
```
