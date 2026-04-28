---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-random-number
title: 安全随机数生成(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 随机数 > 安全随机数生成(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:02e33cc9543e3894e93b9a7a0893f2c7d0a1d43488b3177ef9c3ad86aadc4120
---

说明

从API version 12开始，轻量级智能穿戴设备支持获取随机数相关操作。

随机数主要用于临时会话密钥生成和非对称加密算法密钥生成等场景。在加解密场景中，安全随机数生成器需要具备随机性、不可预测性与不可重现性。当前系统生成的随机数满足密码学安全伪随机性要求。

开发者可以调用接口，完成以下功能：

* 生成指定长度的安全随机数，并将其用于生成对应的密钥。
* 指定随机种子，生成一系列的随机序列。

在开发前，开发者应该先对加解密基础知识有一定了解，并熟知以下随机数相关的基本概念：

* **内部状态**

  代表随机数生成器内存中的数值，当内部状态相同时，随机数生成器会生成固定的随机数序列。
* **随机种子**

  一个用来对伪随机数的内部状态进行初始化的数据，随机数生成器通过种子来生成一系列的随机序列。

  当前OpenSSL实现方式，随机数生成器内部状态是不断变化的，即使设置相同的种子，生成的随机数序列也不会相同。

## 支持的算法与规格

随机数生成算法使用OpenSSL的RAND\_priv\_bytes接口生成安全随机数。

| 算法 | 长度（Byte） |
| --- | --- |
| CTR\_DRBG | [1, INT\_MAX] |

## 开发步骤

1. 调用[cryptoFramework.createRandom](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreaterandom)，生成随机数实例。
2. （可选）设置DataBlob数据，调用[Random.setSeed](../harmonyos-references/js-apis-cryptoframework.md#setseed)，为随机数生成池设置种子。
3. 设置指定字节长度，调用[Random.generateRandom](../harmonyos-references/js-apis-cryptoframework.md#generaterandom)或[Random.generateRandomSync](../harmonyos-references/js-apis-cryptoframework.md#generaterandomsync10)，生成安全随机数。

   指定字节长度范围为1~INT\_MAX。

* 通过await返回异步结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

  3. async function doRand() {
  4. let rand = cryptoFramework.createRandom();
  5. let seed = new Uint8Array([1, 2, 3]);
  6. rand.setSeed({ data: seed });
  7. let len = 12;
  8. let randOutput = await rand.generateRandom(len);
  9. console.info('rand output: ' + randOutput.data);
  10. }
  ```

  [Await.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SecureRandomNumberGeneration/entry/src/main/ets/pages/Await.ets#L15-L27)
* 同步返回结果：

  ```
  1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. function doRandBySync() {
  5. let rand = cryptoFramework.createRandom();
  6. let len = 24; // Generate a 24-byte random number.
  7. try {
  8. let randData = rand.generateRandomSync(len);
  9. if (randData.data.length !== 0) {
  10. console.info('[Sync]: rand result: ' + randData.data);
  11. } else {
  12. console.error('[Sync]: get rand result: fail!');
  13. }
  14. } catch (error) {
  15. let e: BusinessError = error as BusinessError;
  16. console.error(`do rand failed: errCode: ${e.code}, message: ${e.message}`);
  17. }
  18. }
  ```

  [Sync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/CryptoArchitectureKit/SecureRandomNumberGeneration/entry/src/main/ets/pages/Sync.ets#L15-L35)
