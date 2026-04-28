---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-18
title: 如何将公钥转为十六进制或者base64进制数据
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何将公钥转为十六进制或者base64进制数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5690608bb7535e22b32e325a15dc3b3af5261c3e901b0ce4864e096b0ff53183
---

公钥转为十六进制或Base64编码数据，参考代码如下：

```
1. import { buffer, util } from '@kit.ArkTS';

3. @Entry
4. @Component
5. struct PubKeysConvert {
6. build() {
7. Column(){
8. Button('公钥转十六进制').onClick(() => {
9. let pubKeyData = '公钥'
10. let res = buffer.from(pubKeyData).toString('hex')
11. console.info('公钥转十六进制',res)
12. })
13. Button('公钥转base64').onClick(() => {
14. let pubKeyUint8Array = new Uint8Array(buffer.from('公钥','utf-8').buffer)
15. let res = new util.Base64Helper().encodeToStringSync(pubKeyUint8Array)
16. console.info('公钥转base64',res)
17. })
18. }
19. }
20. }
```

[PubKeysConvert.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/PubKeysConvert.ets#L21-L40)
