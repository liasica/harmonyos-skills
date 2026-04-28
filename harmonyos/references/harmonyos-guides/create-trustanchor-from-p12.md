---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-trustanchor-from-p12
title: 证书链校验时从p12文件构造TrustAnchor对象数组
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 证书链校验时从p12文件构造TrustAnchor对象数组
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:606eaafc3440567afbb2613f407802dd13da91be1fac76378eb8b52228430633
---

证书链校验时从p12文件构造TrustAnchor对象数组。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。
2. 基于现有的p12文件数据，调用[cert.createTrustAnchorsWithKeyStore](../harmonyos-references/js-apis-cert.md#certcreatetrustanchorswithkeystore12)创建[X509TrustAnchor](../harmonyos-references/js-apis-cert.md#x509trustanchor11)数组对象，并返回结果。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function test() {
5. // ...
6. try {
7. cert.createTrustAnchorsWithKeyStore(p12Data, '123456').then((data) => {
8. console.info('createTrustAnchorsWithKeyStore result: success, the num of result is :' + data.length);
9. }).catch((err: BusinessError) => {
10. console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${err.code}, message: ${err.message}`);
11. })
12. } catch (error) {
13. console.error(`createTrustAnchorsWithKeyStore failed, errCode: ${error.code}, message: ${error.message}`);
14. }
15. }
```

[CreateTrustanchorFromP12.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/CreateTrustanchorFromP12.ets#L17-L137)
