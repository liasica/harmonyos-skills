---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-66
title: 如何将16进制字符串转换回cryptoFramework.SymKey类型
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何将16进制字符串转换回cryptoFramework.SymKey类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd5e33053013da5bc1073de15cc0fe96a34e52a5776d9d6c3343c2267c4bba87
---

## 问题现象

通过随机生成对称密钥获得了Uint8Array类型的二进制数据symKeyGenerator.generateSymKeySync().getEncoded().data后，将该Uint8Array转成了16进制字符串，如何将16进制字符串转换回cryptoFramework.SymKey类型？

## 背景知识

* [随机生成对称密钥](../harmonyos-guides/crypto-generate-sym-key-randomly.md)，对称密钥对象可用于加解密操作，二进制数据可用于存储或运输。
* 使用[buffer.from](../harmonyos-references/js-apis-buffer.md#bufferfrom-4)方法可将十六进制字符串解码为Uint8Array类型的二进制数据。
* [convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)方法可将二进制数据包装为[DataBlob](../harmonyos-references/js-apis-cryptoframework.md#datablob)对象，并通过同步方法生成密钥[SymKey](../harmonyos-references/js-apis-cryptoframework.md#symkey)。

## 解决方案

1. 以创建密钥算法为SM4、密钥长度为128位的对称密钥生成器为例，将获取的对称密钥的二进制数据转为16进制字符串的代码如下：

   ```ts
   function getHexStringOfSymKey() {
     // 创建SymKeyGenerator实例。
     let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
     // 使用密钥生成器随机生成对称密钥。
     let promiseSymKey: cryptoFramework.SymKey = symKeyGenerator.generateSymKeySync();
     // 获取对称密钥的二进制数据，输出256位密钥。长度为32字节。
     let encodedKey = promiseSymKey.getEncoded();
     console.info(`demo日志1-生成的对称密钥编码为Uint8Array: ${encodedKey.data}`);
     // 将encodedKey转为16进制字符串。
     let hexString: string = '';
     for (let elem of encodedKey.data) {
       hexString += elem.toString(16).padStart(2, '0');
     }
     return hexString;
   }
   ```
2. 我们可以通过逆向操作将生成密钥对象的16进制字符串转变为SymKey类型，使用buffer.from方法将十六进制字符串解码为Uint8Array类型的二进制数据，然后根据原始密钥的算法类型（如AES、HMAC、3DES等）创建对应的密钥生成器，将二进制数据包装为DataBlob对象，并通过同步方法生成密钥。完整恢复代码如下：

   ```ts
   function getSymKeyFromHexString(hexString: string) {
     let keyData = new Uint8Array(buffer.from(hexString, 'hex').buffer);
     // 创建SymKeyGenerator实例。
     let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
     // 将二进制数据包装为 DataBlob对象，并通过同步方法生成密钥.
     let keyBlob: cryptoFramework.DataBlob = { data: keyData };
     let symKey = symKeyGenerator.convertKeySync(keyBlob);
     console.info(`demo日志3-对称密钥恢复后编码为Uint8Array: ${symKey.getEncoded().data}`);
     return symKey;
   }
   ```
3. 点击按钮测试后查看日志打印结果，从打印结果可见密钥对象被恢复成功。

   ```ts
   @Entry
   @Component
   struct Index {
     build() {
       Row() {
         Column() {
           Button('开始测试')
             .onClick(() => {
               let hexStringOfSymKey: string = getHexStringOfSymKey();
               console.info(`demo日志2-生成的对称密钥转16进制字符串：${hexStringOfSymKey}`);
               getSymKeyFromHexString(hexStringOfSymKey);
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

**完整代码如下：**

```ts
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function getHexStringOfSymKey() {
  // 创建SymKeyGenerator实例。
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
  // 使用密钥生成器随机生成对称密钥。
  let promiseSymKey: cryptoFramework.SymKey = symKeyGenerator.generateSymKeySync();
  // 获取对称密钥的二进制数据，输出256位密钥。长度为32字节。
  let encodedKey = promiseSymKey.getEncoded();
  console.info(`demo日志1-生成的对称密钥编码为Uint8Array: ${encodedKey.data}`);
  // 将encodedKey转为16进制字符串。
  let hexString: string = '';
  for (let elem of encodedKey.data) {
    hexString += elem.toString(16).padStart(2, '0');
  }
  return hexString;
}

function getSymKeyFromHexString(hexString: string) {
  let keyData = new Uint8Array(buffer.from(hexString, 'hex').buffer);
  // 创建SymKeyGenerator实例。
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
  // 将二进制数据包装为 DataBlob对象，并通过同步方法生成密钥.
  let keyBlob: cryptoFramework.DataBlob = { data: keyData };
  let symKey = symKeyGenerator.convertKeySync(keyBlob);
  console.info(`demo日志3-对称密钥恢复后编码为Uint8Array: ${symKey.getEncoded().data}`);
  return symKey;
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('开始测试')
          .onClick(() => {
            let hexStringOfSymKey: string = getHexStringOfSymKey();
            console.info(`demo日志2-生成的对称密钥转16进制字符串：${hexStringOfSymKey}`);
            getSymKeyFromHexString(hexStringOfSymKey);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 总结

将16进制字符串恢复为密钥对象需要注意：

1. 密钥长度匹配：

   需确保十六进制字符串的字节长度与目标算法匹配。如AES128需16字节（32位十六进制字符）、AES256需32字节（64位十六进制字符）。
2. 算法一致性：

   createSymKeyGenerator的参数必须与原密钥生成时的算法一致（如'AES128'、'HMAC'）。
3. 异步方法替代方案：

   若需异步处理，可使用symKeyGenerator.convertKey方法。
