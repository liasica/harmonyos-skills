---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-cipher
title: @system.cipher (加密算法)
breadcrumb: API参考 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > ArkTS API > 已停止维护的接口 > @system.cipher (加密算法)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3553d4e7dd3fba3577017a02ed1a41236d92c49ed8f9ec659d917e8d8d6dfa49
---

说明

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始废弃， 建议使用[@ohos.security.cryptoFramework的Cipher](js-apis-cryptoframework.md#cipher)替代。

## 导入模块

```
1. import cipher from '@system.cipher';
```

## CipherResponse

调用cipher接口后，返回的内容。

**系统能力**：SystemCapability.Security.Cipher

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | 否 | 否 | 返回的内容。 |

## CipherRsaOptions

调用cipher rsa方法时，传入的参数。

**系统能力**：SystemCapability.Security.Cipher

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | 加密类型，可选项有：  1. encrypt 加密；  2. decrypt 解密。 |
| text | string | 是 | 待加密或解密的文本内容。待加密的文本内容应该是一段普通文本，长度不能超过 keySize / 8 - 66，其中 keySize 是密钥的长度（例如密钥长度为 1024 时，text 不能超过 62 个字节）。待解密的文本内容应该是经过 base64 编码的一段二进制值。base64 编码使用默认风格。 |
| key | string | 是 | 加密的密钥，RSA的密钥。加密时key为公钥，解密时key为私钥。 |
| transformation | string | 否 | RSA算法的填充项，默认为RSA/None/OAEPWithSHA256AndMGF1Padding。 |
| success | (data: [CipherResponse](js-apis-system-cipher.md#cipherresponse)) => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## CipherAesOptions

调用cipher aes方法时，传入的参数。

**系统能力**：SystemCapability.Security.Cipher

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | string | 是 | 加密类型，可选项有：  1. encrypt 加密；  2. decrypt 解密。 |
| text | string | 是 | 待加密或解密的文本内容。待加密的文本内容应该是一段普通文本。待解密的文本内容应该是经过 base64 编码的一段二进制值。base64 编码使用默认风格。 |
| key | string | 是 | 加密或解密使用到的密钥，经过 base64 编码后生成的字符串。 |
| transformation | string | 否 | AES算法的加密模式和填充项，默认AES/CBC/PKCS5Padding。 |
| iv | string | 否 | AES加解密的初始向量，经过base64编码后的字符串，默认值为key值。 |
| ivOffset | string | 否 | AES加解密的初始向量偏移，默认值0，仅支持0。 |
| ivLen | string | 否 | AES加解密的初始向量字节长度，当前为预留字段，默认值16，仅支持16。 |
| success | (data: [CipherResponse](js-apis-system-cipher.md#cipherresponse)) => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## cipher.rsa

rsa(options: CipherRsaOptions): void

RSA 算法加解密。

**系统能力：** SystemCapability.Security.Cipher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CipherRsaOptions](js-apis-system-cipher.md#cipherrsaoptions) | 是 | rsa加解密需要设置的参数。 |

**示例：**

```
1. export default {
2. rsa() {
3. cipher.rsa({
4. // 加密。
5. action: 'encrypt',
6. // 待加密的文本内容。
7. text: 'hello',
8. // base64编码后的加密公钥。
9. key:
10. 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCx414QSP3RsYWYzf9mkBMiBAXo\n' +
11. '6S7Lpva1fKlcuVxjoFC1iMnzD4mC0uiL4k5MNi43J64c7dbqi3qAJjdAtuwQ6NZJ\n' +
12. '+Enz0RzmVFh/4yk6lmqRzuEFQqhQqSZzaLq6sq2N2G0Sv2Xl3sLvqAfe2HNm2oBw\n' +
13. 'jBpApTJ3TeneOo6Z5QIDAQAB',
14. success: function(data) {
15. console.info(`handling success:${data.text}`);
16. },
17. fail: function(data, code) {
18. console.error(`### cipher.rsa encrypt fail ### ${code}:${data}`);
19. },
20. complete: function() {
21. console.info(`operation complete!`);
22. }
23. });
24. cipher.rsa({
25. // 解密：
26. action: 'decrypt',
27. // 待解密的内容，是base64编码后的一段二进制值，解密后是文本内容“hello”。
28. text:
29. 'EPeCFPib6ayKbA0M6oSywARvFZ8dFYfjQv3nY8ikZGtS9UHq2sLPvAfpeIzggSiCxqbWeCftP1XQ\n' +
30. 'Sa+jEpzFlT1qoSTunBbrYzugPTajIJDTg6R1IRsF/J+mmakn0POVPvi4jCo9wqavB324Bx0Wipnc\n' +
31. 'EU5WO0oBHo5l4x6dTpU=',
32. // base64编码后的解密私钥。
33. key:
34. 'MIICXgIBAAKBgQCx414QSP3RsYWYzf9mkBMiBAXo6S7Lpva1fKlcuVxjoFC1iMnz\n' +
35. 'D4mC0uiL4k5MNi43J64c7dbqi3qAJjdAtuwQ6NZJ+Enz0RzmVFh/4yk6lmqRzuEF\n' +
36. 'QqhQqSZzaLq6sq2N2G0Sv2Xl3sLvqAfe2HNm2oBwjBpApTJ3TeneOo6Z5QIDAQAB\n' +
37. 'AoGBAKPNtoRQcklxqo+2wQP0j2m3Qqnib1DggjVEgb/8f/LNYQSI3U2QdROemryU\n' +
38. 'u3y6N3xacZ359PktTrRKfH5+8ohmHGhIuPAnefp6bLvAFUcl4t1xm74Cow62Kyw3\n' +
39. 'aSbmuTG98dxPA1sXD0jiprdtsq2wQ9CoKNyY7/d/pKoqxNuBAkEA4GytZ60NCTj9\n' +
40. 'w24jACFeko5YqCFY/TTLoc4SQvWtFMnimRPclLZhtUIK0P8dib71UFedx+AxklgL\n' +
41. 'A5gjcfo+2QJBAMrqiwyCh3OQ5DhyRPDwt87x1/jg5fy4hhete2ufSf2FoQCVqO+w\n' +
42. 'PKoljdXmJeS6rGgzGibstuHLrP3tcIho4+0CQD3ZFWzF/xq0jxKlrpWhnJuNCRfE\n' +
43. 'oO6e9yNvVA8J/5oEDSOcmqSNIp4+RhbUx8InUxnCG6Ryv5aSFu71pYcKrPkCQQCL\n' +
44. 'RUGcm3ZGTnslduB0knNF+V2ndwzDUQ7P74UXT+PjurTPhujFYiuxCEd6ORVnEOzG\n' +
45. 'M9TORIgdH8MjIbWsGnndAkEAw9yURDaorE8IYPLF2IEn09g1uzvWPs3phDb6smVx\n' +
46. '8GfqIdUNf+aCG5TZK/kXBF1sqcsi7jXMAf4jBlejVbSVZg==',
47. success: function(data) {
48. console.info(`handling success:${data.text}`);
49. },
50. fail: function(data, code) {
51. console.error(`### cipher.rsa decrypt fail ### ${code}:${data}`);
52. },
53. complete: function() {
54. console.info(`operation complete!`);
55. }
56. });
57. }
58. }
```

## cipher.aes

aes(options: CipherAesOptions): void

AES 算法加解密。

**系统能力：** SystemCapability.Security.Cipher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CipherAesOptions](js-apis-system-cipher.md#cipheraesoptions) | 是 | aes加解密需要设置的参数。 |

**示例：**

```
1. export default {
2. aes() {
3. cipher.aes({
4. // 加密。
5. action: 'encrypt',
6. // 待加密的文本内容。
7. text: 'hello',
8. // base64编码后的密钥。
9. key: 'NDM5Qjk2UjAzMEE0NzVCRjlFMkQwQkVGOFc1NkM1QkQ=',
10. transformation: 'AES/CBC/PKCS5Padding',
11. ivOffset: '0',
12. ivLen: '16',
13. success: function(data) {
14. console.info(`handling success:${data.text}`);
15. },
16. fail: function(data, code) {
17. console.error(`### cipher.aes encrypt fail ### ${code}:${data}`);
18. },
19. complete: function() {
20. console.info(`operation complete!`);
21. }
22. });
23. cipher.aes({
24. // 解密：
25. action: 'decrypt',
26. // 待解密的内容，是base64编码后的一段二进制值。
27. text: '1o0kf2HXwLxHkSh5W5NhzA==',
28. // base64编码后的密钥。
29. key: 'NDM5Qjk2UjAzMEE0NzVCRjlFMkQwQkVGOFc1NkM1QkQ=',
30. transformation: 'AES/CBC/PKCS5Padding',
31. ivOffset: '0',
32. ivLen: '16',
33. success: function(data) {
34. console.info(`handling success:${data.text}`);
35. },
36. fail: function(data, code) {
37. console.error(`### cipher.aes decrypt fail ### ${code}:${data}`);
38. },
39. complete: function() {
40. console.info(`operation complete!`);
41. }
42. });
43. }
44. }
```
