---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-59
title: 使用TaskPool在子线程使用AES加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 使用TaskPool在子线程使用AES加密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:49c2a1ae9f46368a1f0d2120180f871d3cd1ec502aa67182f62822873627fcb9
---

## 问题现象

开发者希望在子线程（TaskPool）中执行AES加密操作，但遇到以下问题：

* cryptoFramework加密对象（如密钥、加密器）无法直接跨线程传递。
* 自定义函数在并发任务中被识别为闭包，导致序列化失败。
* 加密操作阻塞主线程，影响UI流畅性。

## 背景知识

* [使用AES对称密钥加解密](../harmonyos-guides/crypto-aes-sym-encrypt-decrypt-ccm.md)：cryptoFramework支持在子线程（TaskPool）中操作，但需满足特定条件；加密操作涉及的对象（如密钥、加密器）必须是Sendable类型（可序列化对象）。
* [TaskPool](../harmonyos-guides/taskpool-introduction.md)：TaskPool为应用程序提供多线程环境，降低资源消耗并提高系统性能。

## 解决方案

1. 在[并发函数](../harmonyos-guides/taskpool-introduction.md#并发函数中使用自定义类或函数)中使用自定义类或函数时，需将其定义在单独的文件中，否则可能被视为闭包。加解密逻辑拆分为独立文件，确保所有对象可序列化。

   ```ts
   // utils/Func.ets
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { buffer } from '@kit.ArkTS';

   export function genIvParamsSpec() {
     let ivBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('0123456789101112', 'utf-8').buffer) };
     let ivParamsSpec: cryptoFramework.IvParamsSpec = {
       algName: 'IvParamsSpec',
       iv: ivBlob
     };
     return ivParamsSpec;
   }

   function genkey() {
     // 子线程内生成密钥（避免传递非Sendable对象）
     let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
     return symKeyGenerator.generateSymKeySync();
   }

   export const key: cryptoFramework.SymKey = genkey();

   export const CIPHER_TRANSFORMATION = 'AES256|CBC|PKCS7';
   ```
2. 通过TaskPool分发任务，主函数调用并发函数并获取结果。

   ```ts
   // Index.ets
   import { taskpool } from '@kit.ArkTS';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { genIvParamsSpec, key, CIPHER_TRANSFORMATION } from '../utils/Func';

   // 步骤1：定义并发函数（内部创建加密对象）
   @Concurrent
   function aesEncrypt(src: Uint8Array): Uint8Array {
     let cipher = cryptoFramework.createCipher(CIPHER_TRANSFORMATION);
     const iv = genIvParamsSpec();
     cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, key, iv);
     const plaintext: cryptoFramework.DataBlob = { data: src };
     return cipher.doFinalSync(plaintext).data;
   }

   // 步骤2：主线程调用taskpool
   async function startEncryption() {
     let task = new taskpool.Task(aesEncrypt, new Uint8Array([0x01, 0x02])); // 传递原始数据
     let encryptedData = await taskpool.execute(task) as Uint8Array;
     console.info('Encryption succeeded:', encryptedData.toString());
   }

   @Entry
   @Component
   struct Index {
     build() {
       RelativeContainer() {
         Button('AES加密')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .onClick(() => {
             startEncryption();
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
