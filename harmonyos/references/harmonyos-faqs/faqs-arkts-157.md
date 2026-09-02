---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-157
title: ArkTS中随机数生成
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS中随机数生成
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b63338ea810e572d05185bc0420463126925d36cb1491bf4fab22faabeec8641
---

## 问题现象

在ArkTS中如何生成随机数（如用作字段唯一标识的uuid等）？如何生成安全的随机数字字符串？

## 背景知识

* **安全的随机数定义**。

  安全的随机数是指那些难以预测且符合统计随机性的随机数，通常用于加密应用中对安全性要求极高的场景。这些随机数必须满足以下条件：

  **不可预测性**：即使攻击者知道生成随机数的算法及其之前的输出，也无法预测下一个随机数。

  **统计随机性**：随机数序列在统计上应该接近均匀分布，不应表现出任何可识别的模式或偏差。

  **计算效率**：生成随机数的速度应足够快，以满足实际应用的需求。

  **抗攻击性**：能够抵御各种已知的随机数预测攻击，如线性同余生成器（LCG）攻击等。

  常见的用于生成安全随机数的方法：

  + CTR\_DRBG（Counter-based Deterministic Random Bit Generator）是一种基于计数器的确定性随机位生成器，广泛应用于密码学和安全领域。CTR\_DRBG是NIST（美国国家标准与技术研究院）在SP800-90A和SP800-90B中定义的一种标准随机数生成算法。
  + 它基于一个初始化向量（IV）和一个密钥来生成伪随机数。CTR\_DRBG的设计使得它能够高效地生成大量伪随机数，并且具有良好的统计特性和安全性。

* **ArkTS中生成随机数**。
  + **安全要求不高的场景**：

    可通过工具类util中的接口【util.generateRandomUUID】生成随机的RFC 4122版本4的【string】类型UUID。

    也可以使用【util.generateRandomBinaryUUID】接口生成随机的RFC 4122版本4的【Uint8Array】类型UUID。
  + **安全要求高的场景**：

    加解密算法库框架【@ohos.security.cryptoFramework】包提供了安全生成随机数能力，目前支持随机数生成算法（只支持CTR\_DRBG算法规格）。

  **说明** 

  随机数生成算法目前支持生成长度为[1,INT\_MAX]的安全随机数，长度单位为byte。

  随机数生成算法使用openssl的RAND\_priv\_bytes接口生成安全随机数。

## 解决方案

* 针对安全要求不高的场景（如唯一标识的uuid字符串生成）可以借助工具包@ohos.util提供的随机数生成api。

  ```screen
  import { util } from '@kit.ArkTS'

  class ConstantUtils {
    // 调用此函数会生成两个UUID，其中一个UUID进行缓存，一个UUID用于输出
    // 首次调用时，参数是true或false无区别；下次调用时，如果参数是true，依旧缓存上次UUID，并生成新的UUID；如果参数是false，将生成两个UUID，其中一个UUID进行缓存，一个UUID进行输出
    // 默认true
    uuid1: string = util.generateRandomUUID(false);
    uuid2: string = util.generateRandomUUID(true);
    // 返回Uint8Array类型，参数同generateRandomUUID
    uuid3: Uint8Array = util.generateRandomBinaryUUID(true);
    uuid4: string = JSON.stringify(util.generateRandomBinaryUUID(true));
  }
  ```

* 对于安全要求比较高的场景，推荐使用加解密算法库框架@ohos.security.cryptoFramework包生成安全随机数，操作步骤如下：
  1. 通过接口createRandom生成随机数操作实例。
  2. 接受输入长度，通过接口generateRandom，生成指定长度的随机数。
  3. 接受DataBlob数据，通过接口setSeed，为随机数生成池设置种子。

     ```screen
     import cryptoFramework from '@ohos.security.cryptoFramework';
     import { BusinessError } from '@ohos.base';

     // Generate a random number in promise mode
     function doRandByPromise() {
       let rand = cryptoFramework.createRandom();
       let len = 4; // Generate a 4-byte random number
       let promiseGenerateRand = rand.generateRandom(len);
       promiseGenerateRand.then(randData => {
         console.info('[Promise]: rand result: ' + randData.data);
         try {
           rand.setSeed(randData);
         } catch (error) {
           let e: BusinessError = error as BusinessError;
           console.error(`setSeed failed, ${e.code}, ${e.message}`);
         }
       }).catch((error: BusinessError) => {
         console.error('[Promise]: error: ' + error.message);
       });
     }

     // Generate a random number in callback mode
     function doRandByCallback() {
       let rand = cryptoFramework.createRandom();
       let len = 4; // Generate a 4-byte random number
       rand.generateRandom(len, (err, randData) => {
         if (err) {
           console.error('[Callback]: err: ' + err.code);
         } else {
           console.info('[Callback]: generate random result: ' + randData.data);
           try {
             rand.setSeed(randData);
           } catch (error) {
             let e: BusinessError = error as BusinessError;
             console.error(`setSeed failed, ${e.code}, ${e.message}`);
           }
         }
       });
     }

     // Generate a random number synchronously
     function doRandBySync() {
       let rand = cryptoFramework.createRandom();
       let len = 24; // Generate a 24-byte random number
       try {
         let randData = rand.generateRandomSync(len);
         if (randData != null) {
           console.info('[Sync]: rand result: ' + randData.data);
         } else {
           console.error('[Sync]: get rand result fail!');
         }
       } catch (error) {
         let e: BusinessError = error as BusinessError;
         console.error(`do rand failed, ${e.code}, ${e.message}`);
       }
     }
     ```

上面的方法1【doRandBySync】中，【rand.generateRandomSync】用于“同步生成指定长度的随机数”；它的参数是指定生成随机数的长度，单位为字节，范围在1到INT\_MAX之间。

该方法会同步生成指定长度的随机数，并返回一个DataBlob对象；返回的DataBlob对象中存储了生成的随机数，而DataBlob对象是一个字节数组，可以包含多个字节。当前随机数只能指定长度，无法指定范围，可以将得到的随机数自定义范围。

```screen
let rand = cryptoFramework.createRandom();
// 设置生成随机数的字节长度为1
let randData = rand.generateRandomSync(1);
// 自定义范围(0-10之内)
let num: number = randData.data[0] * 10 / 255;
console.info('随机数:' + num);
```
