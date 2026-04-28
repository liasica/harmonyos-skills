---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-22
title: HMAC加密报错：Error message:convertSymKey key failed!
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > HMAC加密报错：Error message:convertSymKey key failed!
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9e7e634079f6612572c4028c4c89031ca1943a3983995226c0a5f46e73babf68
---

**问题场景**

HMAC加密报错：Error message:convertSymKey key failed!

**解决措施**

检查消息认证码算法（HMAC）对应的摘要算法（例如：SHA224）的密钥长度（bit）是否和代码中的密钥长度一致。长度不一致时，可能报错"convertSymKey key failed!"。

以消息认证码算法：HMAC、摘要算法：SHA224为例。当密钥长度为28字节时，代码运行成功。当密钥长度为26字节时，程序运行报错："convertSymKey key failed!"。

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { buffer } from '@kit.ArkTS';

4. @Entry
5. @Component
6. struct HMACFailed {
7. // ...
8. ConvertKeySync() {
9. // The symmetric key length is 28 bytes, 224 bits
10. let keyMessage = '87654321abcdefgh87654321abcd'; // Execution successful
11. // Execution successful. key encoded data：56,55,54,53,52,51,50,49,97,98,99,100,101,102,103,104,56,55,54,53,52,51,50,49,97,98,99,100
12. // The symmetric key length is 26 bytes, 208 bits
13. // let keyMessage = '87654321abcdefgh87654321ab'; // Execution failed
14. // Execution failed,error message: convertSymKey key failed!
15. let keyBlob: cryptoFramework.DataBlob = {
16. data: new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
17. }
18. // Message Authentication Code Algorithm: HMAC, Digest Algorithm: SHA224, Key Length (bits): 224, String Parameter: HMAC|SHA224
19. let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC|SHA224');
20. let key = symKeyGenerator.convertKeySync(keyBlob);
21. let encodedKey = key.getEncoded();
22. console.info('key encoded data：' + encodedKey.data);
23. }
24. // ...
25. }
```

[HMACFailed.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/HMACFailed.ets#L22-L68)

**参考链接**

[HMAC](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#hmac)
