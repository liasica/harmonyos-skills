---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-string-data-to-asym-key-pair
title: 指定PEM格式字符串数据转换非对称密钥对(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成和转换开发指导 > 指定PEM格式字符串数据转换非对称密钥对(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f6d7cc25bff295a25e55e40b62b798b6a73af042e916901d383810a63ec06348
---

以RSA为例，根据指定的非对称密钥字符串数据，生成非对称密钥对（KeyPair）。

说明

针对非对称密钥的convertPemKey操作：

* 公钥需满足X.509规范、PKCS#1规范、PEM编码格式。
* 私钥需满足PKCS#8规范、PKCS#1规范、PEM编码格式。

## 指定PEM格式字符串数据转换密钥对

对应的算法规格请查看[非对称密钥生成和转换规格](crypto-asym-key-generation-conversion-spec.md)。

1. 调用[cryptoFramework.createAsyKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreateasykeygenerator)，指定字符串参数'RSA1024'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（AsyKeyGenerator）。

   生成RSA非对称密钥时，默认素数为2，此处省略了参数PRIMES\_2。
2. 调用[AsyKeyGenerator.convertPemKey](../harmonyos-references/js-apis-cryptoframework.md#convertpemkey12)，传入二进制密钥数据，生成非对称密钥对象（KeyPair）。
3. 调用[AsyKeyGenerator.getEncodedPem](../harmonyos-references/js-apis-cryptoframework.md#getencodedpem12)，将非对称密钥对象中的公钥转换成pkcs1或x509格式，私钥转换成pkcs1或pkcs8格式。

* 以Promise方式生成RSA密钥对为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. let priKeyPkcs1Str1024: string =
  4. '-----BEGIN RSA PRIVATE KEY-----\n' +
  5. 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n' +
  6. 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n' +
  7. 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n' +
  8. 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n' +
  9. 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n' +
  10. '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n' +
  11. 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n' +
  12. 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n' +
  13. 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n' +
  14. 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n' +
  15. 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n' +
  16. 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n' +
  17. 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n' +
  18. '-----END RSA PRIVATE KEY-----\n';
  19. let publicPkcs1Str1024: string =
  20. '-----BEGIN RSA PUBLIC KEY-----\n' +
  21. 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n' +
  22. 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n' +
  23. 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n' +
  24. '-----END RSA PUBLIC KEY-----\n';

  26. async function testPkcs1ToPkcs8ByPromise() {
  27. let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  28. let keyPair = await asyKeyGenerator.convertPemKey(publicPkcs1Str1024, priKeyPkcs1Str1024);
  29. let priPemKey = keyPair.priKey;
  30. let pubPemKey = keyPair.pubKey;
  31. let priString = priPemKey.getEncodedPem('PKCS8');
  32. let pubString = pubPemKey.getEncodedPem('X509');
  33. console.info('[promise]TestPkcs1ToPkcs8ByPromise priString output: ' + priString);
  34. console.info('[promise]TestPkcs1ToPkcs8ByPromise pubString output: ' + pubString);
  35. }
  ```

  [Promise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSpecifiedPEMAsymmetricKeyPair/entry/src/main/ets/pages/Promise.ets#L16-L52)
* 同步返回结果（调用方法[convertPemKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertpemkeysync12)）：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. let priKeyPkcs1Str1024: string =
  4. '-----BEGIN RSA PRIVATE KEY-----\n' +
  5. 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n' +
  6. 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n' +
  7. 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n' +
  8. 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n' +
  9. 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n' +
  10. '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n' +
  11. 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n' +
  12. 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n' +
  13. 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n' +
  14. 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n' +
  15. 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n' +
  16. 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n' +
  17. 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n' +
  18. '-----END RSA PRIVATE KEY-----\n';
  19. let publicPkcs1Str1024: string =
  20. '-----BEGIN RSA PUBLIC KEY-----\n' +
  21. 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n' +
  22. 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n' +
  23. 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n' +
  24. '-----END RSA PUBLIC KEY-----\n';

  26. function testPkcs1ToPkcs8BySync() {
  27. let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  28. try {
  29. let keyPairData = asyKeyGenerator.convertPemKeySync(publicPkcs1Str1024, priKeyPkcs1Str1024);
  30. if (keyPairData != null) {
  31. console.info('[Sync]: convert pem key pair result: success.');
  32. } else {
  33. console.error('[Sync]: convert pem key pair result: fail.');
  34. }
  35. let priPemKey = keyPairData.priKey;
  36. let pubPemKey = keyPairData.pubKey;
  37. let priString = priPemKey.getEncodedPem('PKCS8');
  38. let pubString = pubPemKey.getEncodedPem('X509');
  39. console.info('[Sync]TestPkcs1ToPkcs8BySync priString output: ' + priString);
  40. console.info('[Sync]TestPkcs1ToPkcs8BySync pubString output: ' + pubString);
  41. } catch (e) {
  42. console.error(`Sync failed: errCode: ${e.code}, message: ${e.message}`);
  43. }
  44. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/KeyGenerationConversion/ConvertSpecifiedPEMAsymmetricKeyPair/entry/src/main/ets/pages/Sync.ets#L16-L61)
