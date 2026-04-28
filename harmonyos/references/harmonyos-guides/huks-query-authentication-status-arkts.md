---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-query-authentication-status-arkts
title: 查询认证状态(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 外部密钥管理扩展 > UkeyPIN码认证管理 > 查询认证状态(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3b0e746463b8f254982ddf4db4e640cdbaf0f5055465c8cd1af289e51276a471
---

从API 22开始，huksExternalCrypto提供PIN码认证状态查询功能接口。应用可以通过该接口查询PIN码是否认证通过。具体的场景介绍及规格，请参考[Ukey PIN码认证介绍及规格](huks-ukey-pin-authentication-management-overview.md)。

## 开发步骤

1. 通过证书管理系统能力提供的[证书选择接口](../harmonyos-references/js-apis-certmanagerdialog.md#certificatemanagerdialogopenauthorizedialog22)获取[keyUri](../harmonyos-references/js-apis-certmanagerdialog.md#certreference22)，并将其作为resourceId。
2. 调用查询认证状态接口[getUkeyPinAuthState](../harmonyos-references/js-apis-huksexternalcrypto.md#huksexternalcryptogetukeypinauthstate)验证PIN码。

## 开发案例

```
1. import { huksExternalCrypto } from '@kit.UniversalKeystoreKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function getUkeyPinAuthState(): Promise<huksExternalCrypto.HuksExternalPinAuthState> {
5. let ret: huksExternalCrypto.HuksExternalPinAuthState = huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_NO_AUTH;
6. try {
7. /* 1.构造查询PIN码状态参数 */
8. const testResourceId = JSON.stringify({
9. providerName: "testProviderName",
10. bundleName: "com.example.cryptoapplication",
11. abilityName: "CryptoExtension",
12. index: {
13. key: "testKey"
14. } as ESObject
15. });
16. const extProperties: Array<huksExternalCrypto.HuksExternalCryptoParam> = [];

18. /* 2.调用getUkeyPinAuthState */
19. await huksExternalCrypto.getUkeyPinAuthState(testResourceId, extProperties)
20. .then((data) => {
21. console.info(`promise: getUkeyPinAuthState success , data : ${data}`);
22. }).catch((error: BusinessError) => {
23. console.error(`promise: getUkeyPinAuthState failed, errCode : ${error.code}, errMsg : ${error.message}`);
24. });
25. } catch (error) {
26. console.error(`promise: getUkeyPinAuthState input arg invalid`);
27. }
28. return ret;
29. }

31. async function testGetUkeyPinAuthState() {
32. let ret: huksExternalCrypto.HuksExternalPinAuthState = await getUkeyPinAuthState();
33. if (ret != huksExternalCrypto.HuksExternalPinAuthState.HUKS_EXT_CRYPTO_PIN_AUTH_SUCCEEDED) {
34. console.error(`getUkeyPinAuthState failed`);
35. return;
36. }

38. console.info(`getUkeyPinAuthState success`);
39. }
```
