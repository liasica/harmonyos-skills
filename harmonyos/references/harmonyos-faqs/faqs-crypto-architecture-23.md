---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-23
title: 如何用已有证书做RSA的公钥加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何用已有证书做RSA的公钥加密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a2f3fa7a6ea06b4e8271daaa56a89c609a6e11b8576874aaf18d6ba0a884f593
---

**问题场景**

使用PEM格式证书中的公钥调用示例中的 `rsaPubKeyEncrypt()` 方法时，初始化失败。使用指南中示例的公钥可以成功加密，但加密后的数据转换为字符串后显示为乱码。

**解决措施**

将内容转换为字符串时，可以将其转换为Base64或十六进制。具体转换方法请参考以下代码：

```typescript
function uint8ArrayToHexStr(data: Uint8Array): string {
  let hexString = '';
  let i: number;
  for (i = 0; i < data.length; i++) {
    let char = ('00' + data[i].toString(16)).slice(-2);
    hexString += char;
  }
  return hexString;
}
```

参考如下代码内容，使用正确的证书数据进行处理。

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function rsaPubKeyEncrypt(pubKey: cryptoFramework.PubKey, plainText: cryptoFramework.DataBlob) {
  try {
    let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
    let keyGenPromise: cryptoFramework.KeyPair =
      await asyKeyGenerator.convertKey({ data: pubKey.getEncoded().data }, null);
    let cipher = cryptoFramework.createCipher('RSA1024|PKCS1');
    await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, keyGenPromise.pubKey, null);
    let encryptData = await cipher.doFinal(plainText);
    return uint8ArrayToHexStr(encryptData.data);
  } catch (err) {
    console.info(err);
    return uint8ArrayToHexStr(new Uint8Array());
  }
}
```
