---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-22
title: HMAC加密报错：Error message:convertSymKey key failed!
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > HMAC加密报错：Error message:convertSymKey key failed!
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d2c83391f818c25dcd93546cc30161f926e47c896c70a0b8f22c91365c43f54b
---

**问题场景**

HMAC加密报错：Error message:convertSymKey key failed!

**解决措施**

检查消息认证码算法（HMAC）对应的摘要算法（例如：SHA224）的密钥长度（bit）是否和代码中的密钥长度一致。长度不一致时，可能报错"convertSymKey key failed!"。

以消息认证码算法：HMAC、摘要算法：SHA224为例。当密钥长度为28字节时，代码运行成功。当密钥长度为26字节时，程序运行报错："convertSymKey key failed!"。

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct HMACFailed {
  // ...
  ConvertKeySync() {
    // The symmetric key length is 28 bytes, 224 bits
    let keyMessage = '87654321abcdefgh87654321abcd'; // Execution successful
    // Execution successful. key encoded data：56,55,54,53,52,51,50,49,97,98,99,100,101,102,103,104,56,55,54,53,52,51,50,49,97,98,99,100
    // The symmetric key length is 26 bytes, 208 bits
    // let keyMessage = '87654321abcdefgh87654321ab'; // Execution failed
    // Execution failed,error message: convertSymKey key failed! 
    let keyBlob: cryptoFramework.DataBlob = {
      data: new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
    }
    // Message Authentication Code Algorithm: HMAC, Digest Algorithm: SHA224, Key Length (bits): 224, String Parameter: HMAC|SHA224 
    let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC|SHA224');
    let key = symKeyGenerator.convertKeySync(keyBlob);
    let encodedKey = key.getEncoded();
    console.info('key encoded data：' + encodedKey.data);
  }
  // ...
}
```

**参考链接**

[HMAC](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#hmac)
