---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-23
title: 如何用已有证书做RSA的公钥加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何用已有证书做RSA的公钥加密
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:46544852405022cbd81af1ad7172f6292d6b78820652bd7f2f9a560cc8f70ca4
---

**问题场景**

使用PEM格式证书中的公钥调用示例中的 `rsaPubKeyEncrypt()` 方法时，初始化失败。使用指南中示例的公钥可以成功加密，但加密后的数据转换为字符串后显示为乱码。

**解决措施**

将内容转换为字符串时，可以将其转换为Base64或十六进制。具体转换方法请参考以下代码：

```
1. function uint8ArrayToHexStr(data: Uint8Array): string {
2. let hexString = '';
3. let i: number;
4. for (i = 0; i < data.length; i++) {
5. let char = ('00' + data[i].toString(16)).slice(-2);
6. hexString += char;
7. }
8. return hexString;
9. }
```

[RsaPubKeyEncrypt.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/e56d79f92d56df249533f4b232cf5ad4ac1655f0/CryptoArchitectureKit/entry/src/main/ets/pages/RsaPubKeyEncrypt.ets#L53-L61)

参考如下代码内容，使用正确的证书数据进行处理。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

3. async function rsaPubKeyEncrypt(pubKey: cryptoFramework.PubKey, plainText: cryptoFramework.DataBlob) {
4. try {
5. let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
6. let keyGenPromise: cryptoFramework.KeyPair =
7. await asyKeyGenerator.convertKey({ data: pubKey.getEncoded().data }, null);
8. let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
9. await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyGenPromise.pubKey, null);
10. let encryptData = await cipher.doFinal(plainText);
11. return uint8ArrayToHexStr(encryptData.data);
12. } catch (err) {
13. console.info(err);
14. return uint8ArrayToHexStr(new Uint8Array());
15. }
16. }
```

[RsaPubKeyEncrypt.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/e56d79f92d56df249533f4b232cf5ad4ac1655f0/CryptoArchitectureKit/entry/src/main/ets/pages/RsaPubKeyEncrypt.ets#L34-L49)
