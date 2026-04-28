---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number-hardware
title: 使用硬件熵源生成安全随机数(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 随机数 > 使用硬件熵源生成安全随机数(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fefe4a87f5af130fca7c50bfabf404625b780637f6de115dd92f529a24cead92
---

从API version 21开始，可以选择使用硬件熵源生成安全随机数。

随机数主要用于临时会话密钥生成和非对称加密算法密钥生成等场景。在加解密场景中，安全随机数生成器需要具备随机性、不可预测性和不可重现性。

使用更安全的熵源，对随机数而言，就意味着 “结果难以被猜测或复现”，是 “真随机性” 的量化体现。

当前硬件熵源通过调用[HUKS](huks-overview.md)接口实现。

开发者可以调用接口，完成以下具体功能：

* 生成指定长度的安全随机数，并将其用于生成对应的密钥。
* 开启硬件熵源。
* 指定随机种子，生成一系列的随机序列。

在开发前，开发者应该先对加解密基础知识有一定了解，并熟知以下随机数相关的基本概念：

* **内部状态**

  代表随机数生成器内存中的数值，当内部状态相同时，随机数生成器会生成固定的随机数序列。
* **随机种子**

  一个用来对伪随机数的内部状态进行初始化的数据，随机数生成器通过种子来生成一系列的随机序列。

  当前OpenSSL实现方式，随机数生成器内部状态是不断变化的，即使设置相同的种子，生成的随机数序列也不会相同。

## 支持的算法与规格

安全随机数生成，设置硬件熵源之后，使用OpenSSL的RAND\_priv\_bytes接口生成。

| 算法 | 长度（Byte） |
| --- | --- |
| CTR\_DRBG | [1, INT\_MAX] |

## 开发步骤

1. 调用[cryptoFramework.createRandom](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreaterandom)，生成随机数实例。
2. 调用[cryptoFramework.enableHardwareEntropy](../harmonyos-references/js-apis-cryptoframework.md#enablehardwareentropy21)，开启硬件熵源。
3. （可选）设置DataBlob数据，调用[Random.setSeed](../harmonyos-references/js-apis-cryptoframework.md#setseed)，为随机数生成器设置种子。
4. 设置指定字节长度，调用[Random.generateRandom](../harmonyos-references/js-apis-cryptoframework.md#generaterandom)或[Random.generateRandomSync](../harmonyos-references/js-apis-cryptoframework.md#generaterandomsync10)，生成安全随机数。

   指定字节长度范围为1~INT\_MAX。

* 通过await返回异步结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. async function doRand() {
  4. let rand = cryptoFramework.createRandom();
  5. rand.enableHardwareEntropy();
  6. let seed = new Uint8Array([1, 2, 3]);
  7. rand.setSeed({ data: seed });
  8. let len = 12;
  9. let randOutput = await rand.generateRandom(len);
  10. console.info('rand output: ' + randOutput.data);
  11. }
  ```

  [Await.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SecureHardWareRandomNumberGeneration/entry/src/main/ets/pages/Await.ets#L15-L28)
* 同步返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. function doRandBySync() {
  5. let rand = cryptoFramework.createRandom();
  6. rand.enableHardwareEntropy();
  7. let len = 24; // Generate a 24-byte random number.
  8. try {
  9. let randData = rand.generateRandomSync(len);
  10. if (randData.data.length !== 0) {
  11. console.info('[Sync]: rand result: ' + randData.data);
  12. } else {
  13. console.error('[Sync]: get rand result: fail!');
  14. }
  15. } catch (error) {
  16. let e: BusinessError = error as BusinessError;
  17. console.error(`do rand failed: errCode: ${e.code}, message: ${e.message}`);
  18. }
  19. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SecureHardWareRandomNumberGeneration/entry/src/main/ets/pages/Sync.ets#L15-L36)
