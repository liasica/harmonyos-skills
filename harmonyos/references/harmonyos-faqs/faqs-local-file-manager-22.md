---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-22
title: 如何校验文件一致性
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何校验文件一致性
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d16a04846abbc1ed0224d3f241d2e6f0b88ec4dde476129ba42d32233e5a41e0
---

通过比较Hash值的方法来校验文件的一致性。Hash算法使用MD5算法，[消息摘要计算MD5(ArkTS)](../harmonyos-guides/crypto-generate-message-digest-md5.md)，参考代码如下：

```
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { fileIo } from '@kit.CoreFileKit'
3. import { buffer } from '@kit.ArkTS';

5. async function calFileMd5(fileUrl: string) {
6. let md = cryptoFramework.createMd('MD5');
7. let file = fileIo.openSync(fileUrl, fileIo.OpenMode.READ_ONLY);
8. let arrayBuffer = new ArrayBuffer(2048);
9. let len: number = 0;
10. let position: number = 0;
11. do {
12. len = fileIo.readSync(file.fd, arrayBuffer, { offset: position });
13. if (len > 0) {
14. let uint8Array = new Uint8Array(arrayBuffer.slice(0, len));
15. let updateMessageBlob: cryptoFramework.DataBlob = { data: uint8Array };
16. await md.update(updateMessageBlob);
17. position += len;
18. }
19. } while (len > 0);
20. fileIo.closeSync(file);
21. let mdOutput = await md.digest();
22. console.info('...calFileMd5: ' + buffer.from(mdOutput.data).toString('hex'));
23. }
```

[CalFileMd5.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocationKit/entry/src/main/ets/pages/CalFileMd5.ets#L21-L44)

**参考链接：**

[@ohos.file.hash (文件哈希处理)](../harmonyos-references/js-apis-file-hash.md)
