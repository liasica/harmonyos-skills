---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-sha3
title: 消息摘要计算SHA3(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 消息摘要计算 > 消息摘要计算开发指导 > 消息摘要计算SHA3(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dec438df6d275292d288f69bb6c6031ea19ec18b041fc59409c21f84eebcd140
---

从API version 22开始，算法库支持使用该算法进行摘要计算操作。

对应的算法规格请查看[消息摘要计算算法规格](crypto-generate-message-digest-overview.md#支持的算法与规格)。

## 开发步骤

在调用update接口传入数据时，可以[一次性传入所有数据](crypto-generate-message-digest-sha3.md#摘要算法一次性传入)，也可以把数据人工分段，然后[分段update](crypto-generate-message-digest-sha3.md#分段摘要算法)。对于同一段数据而言，计算结果没有差异。对于数据量较大的数据，开发者可以根据实际需求选择是否分段传入。

下面分别提供两种方式的示例代码。

### 摘要算法（一次性传入）

1. 调用[cryptoFramework.createMd](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemd)，指定摘要算法SHA3-256，生成摘要实例（Md）。
2. 调用[Md.update](../harmonyos-references/js-apis-cryptoframework.md#update-6)，传入自定义消息，进行摘要更新计算。单次update长度没有限制。
3. 调用[Md.digest](../harmonyos-references/js-apis-cryptoframework.md#digest)，获取摘要计算结果。
4. 调用[Md.getMdLength](../harmonyos-references/js-apis-cryptoframework.md#getmdlength)，获取摘要计算长度，单位为字节。

* 以使用await方式单次传入数据，获取摘要计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function doMd() {
  5. let mdAlgName = 'SHA3-256'; // 摘要算法名。
  6. let message = 'mdTestMessage'; // 待摘要的数据。
  7. let md = cryptoFramework.createMd(mdAlgName);
  8. // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制。
  9. await md.update({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
  10. let mdResult = await md.digest();
  11. console.info('Md result: ' + mdResult.data);
  12. let mdLen = md.getMdLength();
  13. console.info('md len: ' + mdLen);
  14. }
  ```

  [SingleTimeAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageDigestComputation/entry/src/main/ets/pages/sha3/singleTime/SingleTimeAsync.ets#L15-L31)
* 以使用同步方式单次传入数据，获取摘要计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function doMdBySync() {
  5. let mdAlgName = 'SHA3-256'; // 摘要算法名。
  6. let message = 'mdTestMessage'; // 待摘要的数据。
  7. let md = cryptoFramework.createMd(mdAlgName);
  8. // 数据量较少时，可以只做一次update，将数据全部传入，接口未对入参长度做限制。
  9. md.updateSync({ data: new Uint8Array(buffer.from(message, 'utf-8').buffer) });
  10. let mdResult = md.digestSync();
  11. console.info('[Sync]:Md result: ' + mdResult.data);
  12. let mdLen = md.getMdLength();
  13. console.info('md len: ' + mdLen);
  14. }
  ```

  [SingleTimeSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageDigestComputation/entry/src/main/ets/pages/sha3/singleTime/SingleTimeSync.ets#L15-L30)

### 分段摘要算法

1. 调用[cryptoFramework.createMd](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemd)，指定摘要算法MD5，生成摘要实例（Md）。
2. 传入自定义消息，将一次传入数据量设置为20字节，多次调用[Md.update](../harmonyos-references/js-apis-cryptoframework.md#update-7)，进行摘要更新计算。
3. 调用[Md.digest](../harmonyos-references/js-apis-cryptoframework.md#digest-1)，获取摘要计算结果。
4. 调用[Md.getMdLength](../harmonyos-references/js-apis-cryptoframework.md#getmdlength)，获取摘要计算长度，单位为字节。

* 以使用await方式分段传入数据，获取摘要计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. async function doLoopMd() {
  5. let mdAlgName = 'SHA3-256'; // 摘要算法名。
  6. let md = cryptoFramework.createMd(mdAlgName);
  7. // 假设信息总共43字节，根据utf-8解码后，也是43字节。
  8. let messageText = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee';
  9. let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
  10. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求。
  11. for (let i = 0; i < messageData.length; i += updateLength) {
  12. let updateMessage = messageData.subarray(i, i + updateLength);
  13. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  14. await md.update(updateMessageBlob);
  15. }
  16. let mdOutput = await md.digest();
  17. console.info('md result: ' + mdOutput.data);
  18. let mdLen = md.getMdLength();
  19. console.info('md len: ' + mdLen);
  20. }
  ```

  [SegmentationAsync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageDigestComputation/entry/src/main/ets/pages/sha3/segmentation/SegmentationAsync.ets#L15-L37)
* 以使用同步方式分段传入数据，获取摘要计算结果为例：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { buffer } from '@kit.ArkTS';

  4. function doLoopMdBySync() {
  5. let mdAlgName = 'SHA3-256'; // 摘要算法名。
  6. let md = cryptoFramework.createMd(mdAlgName);
  7. // 假设信息总共43字节，根据utf-8解码后，也是43字节。
  8. let messageText = 'aaaaa.....bbbbb.....ccccc.....ddddd.....eee';
  9. let messageData = new Uint8Array(buffer.from(messageText, 'utf-8').buffer);
  10. let updateLength = 20; // 假设以20字节为单位进行分段update，实际并无要求。
  11. for (let i = 0; i < messageData.length; i += updateLength) {
  12. let updateMessage = messageData.subarray(i, i + updateLength);
  13. let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
  14. md.updateSync(updateMessageBlob);
  15. }
  16. let mdOutput = md.digestSync();
  17. console.info('[Sync]:md result: ' + mdOutput.data);
  18. let mdLen = md.getMdLength();
  19. console.info('md len: ' + mdLen);
  20. }
  ```

  [SegmentationSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/MessageDigestComputation/entry/src/main/ets/pages/sha3/segmentation/SegmentationSync.ets#L16-L38)
