---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-65
title: 如何实现文件加解密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何实现文件加解密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eee431c1fcc29c9756b7cb2745480671293f4346614bb6a20c04a64d0c674c56
---

## 问题现象

文件以明文形式存储或传输，存在敏感数据泄露风险。本案例从沙箱读取文件后，通过对称加密算法DES对文件进行加密、解密等操作，验证密文解密后得出的明文与源文件一致。

## 背景知识

* [DES](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#des)：DES是分组加密算法（64位/8字节分组），加密模式支持ECB/CBC/OFB/CFB。
* CBC模式：密钥长度64位,加密的明文长度非64位整数倍时必须填充PKCS5/PKCS7。

## 解决方案

1. 通过[createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)指定算法名称获取相应的对称密钥生成器实例。

   ```ts
   /**
    * 初始化密钥
    *
    * @returns 密钥
    */
   export function initCipherKey(): cryptoFramework.SymKey | undefined {
     let symKeyData: Uint8Array = new Uint8Array([238, 249, 61, 55, 128, 220, 183, 224]);
     let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
     let symKey: cryptoFramework.SymKey | undefined = undefined;
     try {
       let symGenerator: cryptoFramework.SymKeyGenerator = cryptoFramework.createSymKeyGenerator('DES64');
       symKey = symGenerator.convertKeySync(symKeyBlob);
       return symKey;
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, TAG, `Init key failed. code=${err.code}, message=${err.message}`);
     }
     return symKey;
   }
   ```
2. 通过[createCipher](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatecipher)创建Cipher对象，通过[initSync](../harmonyos-references/js-apis-cryptoframework.md#initsync12)初始化模式（加密/解密）。

   ```ts
   /**
    * 初始化cipher
    *
    * @param mode cipher类型
    * @param symKey 密钥
    * @returns cipher对象
    */
   export function initCipher(mode: cryptoFramework.CryptoMode,
     symKey: cryptoFramework.SymKey): cryptoFramework.Cipher | undefined {
     let cipher: cryptoFramework.Cipher | undefined;
     try {
       // 1.创建cipher
       cipher = cryptoFramework.createCipher('DES64|CBC|PKCS5');
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, TAG, `Init Cipher failed. code=${err.code}, message=${err.message}`);
       return cipher;
     }
     // 2.创建iv向量
     let cbcParamsSpec: cryptoFramework.IvParamsSpec = {
       iv: { data: new Uint8Array(new util.TextEncoder().encodeInto('DSEPUB86').buffer) },
       algName: 'IvParamsSpec'
     };
     // 3.初始化cipher对象
     cipher?.initSync(mode, symKey, cbcParamsSpec);
     return cipher;
   }
   ```
3. 从沙箱读取文件，将读取的文件内容存入缓冲区。

   ```ts
   /**
    * 读文件，将读取的文件数据缓存在Array数组中
    *
    * @param filesDir 文件路径
    * @returns 文件内容数组
    */
   export function readFile(filesDir: string): ArrayBuffer {
     let arrayBuffer: ArrayBuffer = new ArrayBuffer(DEFAULT_SIZE);
     try {
       const sourceFile = fileIo.openSync(filesDir, fileIo.OpenMode.READ_WRITE);
       let fileSize = fileIo.statSync(filesDir).size;
       arrayBuffer = new ArrayBuffer(fileSize);
       fileIo.readSync(sourceFile.fd, arrayBuffer);
       return arrayBuffer;
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, TAG, `ReadFile failed. code=${err.code}, message=${err.message}`);
     }
     return arrayBuffer;
   }
   ```
4. 使用[updateSync](../harmonyos-references/js-apis-cryptoframework.md#updatesync12)对文件分段加/解密，使用[doFinalSync](../harmonyos-references/js-apis-cryptoframework.md#dofinalsync12)处理剩余数据并结束加解密操作，将加密或解密完的文件保存到沙箱中。

   ```ts
   /**
    * 对文件进行加/解密，将加/解密后的内容写入新的文件中
    *
    * @param srcPath 要加/解密的源文件
    * @param desPath 加/解密后的内容写入新的文件路径
    * @param mode 加/解密 0：加密 1：解密
    * @param symKey 密钥
    */
   export function cipherDoFinal(srcPath: string, desPath: string, mode: cryptoFramework.CryptoMode,
     symKey: cryptoFramework.SymKey) {
     try {
       let plainText: cryptoFramework.DataBlob = {
         data: new Uint8Array(readFile(srcPath))
       };
       let cipher = initCipher(mode, symKey);
       let plainSplitLen = DEFAULT_SIZE;
       let result = new Uint8Array();
       for (let i = 0; i < plainText.data.length; i += plainSplitLen) {
         let updateMessage = plainText.data.subarray(i, i + plainSplitLen);
         let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
         let updateOutput = cipher!.updateSync(updateMessageBlob);
         let merged = new Uint8Array(result.length + updateOutput.data.length);
         merged.set(result);
         merged.set(updateOutput.data, result.length);
         result = merged;
       }
       const finalOutput = cipher?.doFinalSync(null);
       let mergeText = result;
       if (finalOutput !== null) {
         mergeText = new Uint8Array(result.length + finalOutput!.data.length);
         mergeText.set(result);
         mergeText.set(finalOutput!.data, result.length);
       }
       let encryptData: cryptoFramework.DataBlob = { data: mergeText };
       const encryptFile =
         fileIo.openSync(desPath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.APPEND);
       fileIo.write(encryptFile.fd, encryptData.data.buffer).catch((err: BusinessError) => {
         hilog.error(0x0000, TAG, `write file failed. code=${err.code}, message=${err.message}`);
       });
       fileIo.close(encryptFile.fd).catch((err: BusinessError) => {
         hilog.error(0x0000, TAG, `colse io failed. code=${err.code}, message=${err.message}`);
       });
     } catch (error) {
       let err = error as BusinessError;
       hilog.error(0x0000, TAG, `Cipher do final failed. code=${err.code}, message=${err.message}`);
     }
   }
   ```

完整示例如下，其中引入的Crypto文件为抽取出的加解密方法：

```ts
import { common } from '@kit.AbilityKit';
import { fileIo } from '@kit.CoreFileKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cipherDoFinal, initCipherKey } from './Crypto';

let symKey: cryptoFramework.SymKey;
const TAG = 'Crypto';
const FILE_NAME = 'test.txt';

@Entry
@Component
struct Index {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    this.rawfileToSandbox();
    symKey = initCipherKey()!;
  }

  build() {
    Column() {
      Row() {
        Button('encrypt')
          .onClick(() => {
            this.encrypt();
          });
        Button('decrypt')
          .margin({ left: 20 })
          .onClick(() => {
            this.decrypt();
          });
      }
      .margin({ top: 50 });
    }
    .height('100%')
    .width('100%');
  }

  rawfileToSandbox() {
    const fileContent = this.context.resourceManager.getRawFileContentSync(FILE_NAME);
    const sandboxDir = this.context.filesDir;
    const filePath = sandboxDir + '/' + FILE_NAME;
    try {
      const file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      fileIo.writeSync(file.fd, fileContent.buffer);
      fileIo.closeSync(file.fd);
    } catch (error) {
      hilog.error(0x0000, TAG, 'RawFile to Sandbox failed');
    }
  }

  encrypt() {
    cipherDoFinal(this.context.filesDir + '/' + FILE_NAME, this.context.filesDir + '/encrypt.txt',
      cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey);
  }

  decrypt() {
    cipherDoFinal(this.context.filesDir + '/encrypt.txt', this.context.filesDir + '/decrypt.txt',
      cryptoFramework.CryptoMode.DECRYPT_MODE, symKey);
  }
}
```

Crypto.ets文件如下：

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { util } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

const TAG = 'Crypto';
const DEFAULT_SIZE = 1024;

/**
 * 初始化密钥
 *
 * @returns 密钥
 */
export function initCipherKey(): cryptoFramework.SymKey | undefined {
  let symKeyData: Uint8Array = new Uint8Array([238, 249, 61, 55, 128, 220, 183, 224]);
  let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
  let symKey: cryptoFramework.SymKey | undefined = undefined;
  try {
    let symGenerator: cryptoFramework.SymKeyGenerator = cryptoFramework.createSymKeyGenerator('DES64');
    symKey = symGenerator.convertKeySync(symKeyBlob);
    return symKey;
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `Init key failed. code=${err.code}, message=${err.message}`);
  }
  return symKey;
}

/**
 * 初始化cipher
 *
 * @param mode cipher类型
 * @param symKey 密钥
 * @returns cipher对象
 */
export function initCipher(mode: cryptoFramework.CryptoMode,
  symKey: cryptoFramework.SymKey): cryptoFramework.Cipher | undefined {
  let cipher: cryptoFramework.Cipher | undefined;
  try {
    // 1.创建cipher
    cipher = cryptoFramework.createCipher('DES64|CBC|PKCS5');
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `Init Cipher failed. code=${err.code}, message=${err.message}`);
    return cipher;
  }
  // 2.创建iv向量
  let cbcParamsSpec: cryptoFramework.IvParamsSpec = {
    iv: { data: new Uint8Array(new util.TextEncoder().encodeInto('DSEPUB86').buffer) },
    algName: 'IvParamsSpec'
  };
  // 3.初始化cipher对象
  cipher?.initSync(mode, symKey, cbcParamsSpec);
  return cipher;
}

/**
 * 读文件，将读取的文件数据缓存在Array数组中
 *
 * @param filesDir 文件路径
 * @returns 文件内容数组
 */
export function readFile(filesDir: string): ArrayBuffer {
  let arrayBuffer: ArrayBuffer = new ArrayBuffer(DEFAULT_SIZE);
  try {
    const sourceFile = fileIo.openSync(filesDir, fileIo.OpenMode.READ_WRITE);
    let fileSize = fileIo.statSync(filesDir).size;
    arrayBuffer = new ArrayBuffer(fileSize);
    fileIo.readSync(sourceFile.fd, arrayBuffer);
    return arrayBuffer;
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `ReadFile failed. code=${err.code}, message=${err.message}`);
  }
  return arrayBuffer;
}

/**
 * 对文件进行加/解密，将加/解密后的内容写入新的文件中
 *
 * @param srcPath 要加/解密的源文件
 * @param desPath 加/解密后的内容写入新的文件路径
 * @param mode 加/解密 0：加密 1：解密
 * @param symKey 密钥
 */
export function cipherDoFinal(srcPath: string, desPath: string, mode: cryptoFramework.CryptoMode,
  symKey: cryptoFramework.SymKey) {
  try {
    let plainText: cryptoFramework.DataBlob = {
      data: new Uint8Array(readFile(srcPath))
    };
    let cipher = initCipher(mode, symKey);
    let plainSplitLen = DEFAULT_SIZE;
    let result = new Uint8Array();
    for (let i = 0; i < plainText.data.length; i += plainSplitLen) {
      let updateMessage = plainText.data.subarray(i, i + plainSplitLen);
      let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
      let updateOutput = cipher!.updateSync(updateMessageBlob);
      let merged = new Uint8Array(result.length + updateOutput.data.length);
      merged.set(result);
      merged.set(updateOutput.data, result.length);
      result = merged;
    }
    const finalOutput = cipher?.doFinalSync(null);
    let mergeText = result;
    if (finalOutput !== null) {
      mergeText = new Uint8Array(result.length + finalOutput!.data.length);
      mergeText.set(result);
      mergeText.set(finalOutput!.data, result.length);
    }
    let encryptData: cryptoFramework.DataBlob = { data: mergeText };
    const encryptFile =
      fileIo.openSync(desPath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.APPEND);
    fileIo.write(encryptFile.fd, encryptData.data.buffer).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, `write file failed. code=${err.code}, message=${err.message}`);
    });
    fileIo.close(encryptFile.fd).catch((err: BusinessError) => {
      hilog.error(0x0000, TAG, `colse io failed. code=${err.code}, message=${err.message}`);
    });
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, TAG, `Cipher do final failed. code=${err.code}, message=${err.message}`);
  }
}
```

## 常见FAQ

Q：如果文件太大怎么处理？

A：对文件分段读取加/解密，也可以对文件压缩后再做加/解密。
