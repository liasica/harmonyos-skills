---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device-attestation-apps
title: 应用端开发
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 应用真实性证明 > 创建密钥确立可信凭证 > 应用端开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7b9c45eec4e4a80ef45fc01bd7b514059d66c125fb98e144a96fc2b9407710df
---

## 接口说明

接口能力由[Universal Keystore Kit](huks-overview.md)提供，涉及的功能指导请参考：

* [Universal Keystore Kit简介](huks-overview.md)
* [查询密钥是否存在(ArkTS)](huks-check-key-arkts.md)
* [查询密钥是否存在(C/C++)](huks-check-key-ndk.md)
* [生成密钥(ArkTS)](huks-key-generation-arkts.md)
* [生成密钥(C/C++)](huks-key-generation-ndk.md)
* [匿名密钥证明(ArkTS)](huks-key-anon-attestation-arkts.md)
* [匿名密钥证明(C/C++)](huks-key-anon-attestation-ndk.md)
* [签名/验签(ArkTS)](huks-signing-signature-verification-arkts.md)
* [签名/验签(C/C++)](huks-signing-signature-verification-ndk.md)

## 查询应用公私钥对是否存在

查询应用公私钥对是否存在，如果已存在，则不需要重复创建。

**示例：**

```
1. import { huks } from '@kit.UniversalKeystoreKit';

3. let keyAlias = 'serviceKey_user01';  // 业务密钥别名
4. let isKeyExist: Boolean;

6. let huksOptions: huks.HuksOptions = {
7. properties: []
8. }
9. try {
10. huks.hasKeyItem(keyAlias, huksOptions, (error, data) => {
11. if (error) {
12. console.error(`callback: hasKeyItem failed, ` + JSON.stringify(error));
13. } else {
14. if (data !== null && data.valueOf() !== null) {
15. isKeyExist = data.valueOf();
16. console.info(`callback: hasKeyItem success, isKeyExist = ${isKeyExist}`);
17. }
18. }
19. });
20. } catch (error) {
21. console.error(`callback: hasKeyItem input arg invalid, ` + JSON.stringify(error));
22. }
```

## 创建应用公私钥对

创建一个用于验证应用请求真实性的非对称算法密钥对，称为应用公私钥对（包含应用公钥和应用私钥），比如RSA、ECC算法的密钥对。通过Universal Keystore Kit创建的密钥对基于硬件的安全环境进行生成和安全存储。

说明

安全建议：为了提高安全性，建议为终端设备中登录的每个用户生成唯一的密钥对。

**示例：**

```
1. import { huks } from '@kit.UniversalKeystoreKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let keyAlias = 'serviceKey_user01'; // 业务密钥别名

6. function GetGenerateProperties() {
7. let properties: Array<huks.HuksParam> = new Array();
8. let index = 0;
9. properties[index++] = {
10. tag: huks.HuksTag.HUKS_TAG_ALGORITHM,
11. value: huks.HuksKeyAlg.HUKS_ALG_ECC
12. };
13. properties[index++] = {
14. tag: huks.HuksTag.HUKS_TAG_KEY_SIZE,
15. value: huks.HuksKeySize.HUKS_AES_KEY_SIZE_256
16. };
17. properties[index++] = {
18. tag: huks.HuksTag.HUKS_TAG_PURPOSE,
19. value: huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_SIGN |
20. huks.HuksKeyPurpose.HUKS_KEY_PURPOSE_VERIFY
21. };
22. properties[index++] = {
23. tag: huks.HuksTag.HUKS_TAG_DIGEST,
24. value: huks.HuksKeyDigest.HUKS_DIGEST_SHA256
25. }
26. return properties;
27. }

29. async function GenerateKey(keyAlias: string) {
30. let genProperties = GetGenerateProperties();
31. let options: huks.HuksOptions = {
32. properties: genProperties
33. }
34. await huks.generateKeyItem(keyAlias, options)
35. .then(() => {
36. console.info(`promise: generate Key success.`);
37. }).catch((err: BusinessError) => {
38. console.error(`promise: generate Key failed, error: ` + err.message);
39. })
40. }
```

## 对应用公钥和应用ID进行证明

应用调用Universal Keystore Kit的密钥证明接口对生成的应用公钥和调用的应用身份进行证明，Universal Keystore Kit返回密钥证明证书链给应用，证书链采用X509标准格式。

说明

安全建议：为了在发送密钥证明证书链给应用服务器时能够防重放攻击，建议应用先从应用服务器获取一次性的挑战值Challenge，并在调用密钥证明接口时输入挑战值Challenge。应用服务器采用安全随机数生成挑战值Challenge，并缓存到服务器中。

**示例：**

```
1. import { huks } from '@kit.UniversalKeystoreKit';

3. class HuksProperties {
4. tag: huks.HuksTag = huks.HuksTag.HUKS_TAG_ALGORITHM;
5. value: huks.HuksKeyAlg | huks.HuksKeySize | huks.HuksKeyPurpose | huks.HuksKeyDigest |
6. huks.HuksKeyStorageType | huks.HuksKeyPadding | huks.HuksKeyGenerateType |
7. huks.HuksCipherMode | Uint8Array = huks.HuksKeyAlg.HUKS_ALG_ECC;
8. }

10. let challenge = stringToUint8Array('challenge_data'); // 从服务器获取的挑战值Challenge
11. let keyAlias = 'serviceKey_user01'; // 业务密钥别名

13. function stringToUint8Array(str: string): Uint8Array {
14. let arr: number[] = [];
15. for (let i = 0, j = str.length; i < j; ++i) {
16. arr.push(str.charCodeAt(i));
17. }
18. let tmpUint8Array = new Uint8Array(arr);
19. return tmpUint8Array;
20. }

22. async function anonAttestKey(): Promise<void> {
23. let aliasString = keyAlias;

25. let properties: HuksProperties[] = [
26. {
27. tag: huks.HuksTag.HUKS_TAG_ATTESTATION_CHALLENGE,
28. value: challenge
29. }
30. ];

32. let options: huks.HuksOptions = {
33. properties: properties
34. };

36. try {
37. let data = await huks.anonAttestKeyItem(aliasString, options);
38. // todo：把证书链信息（data变量）发送到云侧的服务器。如下示例代码把证书链打印到日志中，供调测使用，商用代码不需要打印。
39. console.info(`anonAttestKeyItem success`);
40. data.certChains?.forEach(cert => {
41. console.info(cert);
42. });
43. } catch (error) {
44. console.error(`promise: anonAttestKeyItem fail`);
45. }
46. }
```
