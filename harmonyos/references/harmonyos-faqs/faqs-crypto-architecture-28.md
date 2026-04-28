---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-28
title: 在进行aes加密的时候，如何把字符串转换成Key对象
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 在进行aes加密的时候，如何把字符串转换成Key对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:381a405927586585c5b824a0c203a2a939b882c3c8dddca8ceb6e8b9aab91f51
---

可参考如下代码：

```
1. import { buffer, util } from '@kit.ArkTS';
2. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

4. @Entry
5. @Component
6. struct GetKey {
7. // Convert string to byte stream
8. stringToUint8Array(str: string) {
9. return new Uint8Array(buffer.from(str, 'utf-8').buffer);
10. }

12. //Import key
13. async getKey() {
14. let symAlgName = 'AES128';
15. let symKeyGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
16. let dataUint8Array = this.stringToUint8Array('294A2561FEFDF08D');
17. let keyBlob: cryptoFramework.DataBlob = { data: dataUint8Array };
18. console.info('keyBlob', JSON.stringify(keyBlob))
19. let symKey = await symKeyGenerator.convertKey(keyBlob);
20. return symKey;
21. }

23. build() {
24. Column({ space: 10 }) {
25. Button('aes加密时,字符串转换成Key对象')
26. .onClick(() => {
27. this.getKey();
28. })
29. }
30. .alignItems(HorizontalAlign.Center)
31. .height('100%')
32. .width('100%')
33. }
34. }
```

[GetKey.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/GetKey.ets#L21-L54)
