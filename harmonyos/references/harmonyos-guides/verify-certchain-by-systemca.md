---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/verify-certchain-by-systemca
title: 使用系统预置CA证书校验证书链
breadcrumb: 指南 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > 证书算法库框架 > 使用系统预置CA证书校验证书链
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d070705d488ded199db41d9d402e3315b4bce82eb4ee897cd38e8568a079d143
---

从API 20开始，支持使用系统预置CA证书校验证书链。

以校验证书链为例，完成证书链对象的创建，使用系统预置CA证书对证书链进行校验。

## 开发步骤

1. 导入[证书算法库框架模块](../harmonyos-references/js-apis-cert.md)。

   ```
   1. import { cert } from '@kit.DeviceCertificateKit';
   ```
2. 基于已有的证书数据，调用[cert.createX509CertChain](../harmonyos-references/js-apis-cert.md#certcreatex509certchain11)创建X509证书链对象，并返回结果。
3. 调用[x509CertChain.validate](../harmonyos-references/js-apis-cert.md#validate11)设置校验参数trustSystemCa为true，使用系统预置CA证书校验证书链并返回结果。

```
1. import { cert } from '@kit.DeviceCertificateKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util } from '@kit.ArkTS';
4. // ...
5. async function sample() {
6. let textEncoder = new util.TextEncoder();
7. // 证书链二进制数据，需业务自行赋值。
8. const encodingBlob: cert.EncodingBlob = {
9. data: textEncoder.encodeInto(certChainData),
10. // 根据encodingData的格式进行赋值，支持FORMAT_PEM、FORMAT_DER和FORMAT_PKCS7。
11. encodingFormat: cert.EncodingFormat.FORMAT_PEM
12. };
13. let x509CertChain: cert.X509CertChain = {} as cert.X509CertChain;
14. try {
15. x509CertChain = await cert.createX509CertChain(encodingBlob);
16. } catch (err) {
17. let e: BusinessError = err as BusinessError;
18. console.error(`createX509CertChain failed, errCode: ${e.code}, errMsg: ${e.message}`);
19. }

21. // 证书链校验数据，需业务自行赋值。
22. const param: cert.CertChainValidationParameters = {
23. date: '20250623163000Z',
24. trustAnchors: [{}],
25. trustSystemCa: true,
26. };
27. try {
28. const validationRes = await x509CertChain.validate(param);
29. console.info('X509CertChain validate result: success.');
30. } catch (err) {
31. let e: BusinessError = err as BusinessError;
32. console.error(`X509CertChain validate failed, errCode: ${e.code}, errMsg: ${e.message}`);
33. }
34. }
```

[VerifyCertchainBySystemca.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/DeviceCertificateKit/CertificateAlgorithmLibrary/entry/src/main/ets/pages/VerifyCertchainBySystemca.ets#L16-L157)
