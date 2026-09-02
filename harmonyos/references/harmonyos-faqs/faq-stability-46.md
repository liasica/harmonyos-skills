---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-46
title: 应用启动中进行加解密处理时，出现闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用启动中进行加解密处理时，出现闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2fbd52b1359fd7cb8645c063300065cd942ec1686fa08342d921803092bd00bf
---

## 问题现象

应用在启动中使用加解密功能的情况下，发生闪退。

## 背景知识

* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* JsCrash日志规格说明可以参考[日志规格](../harmonyos-guides/jscrash-guidelines.md#日志规格)。
* [doFinal](../harmonyos-references/js-apis-cryptoframework.md#dofinal)和[doFinalSync](../harmonyos-references/js-apis-cryptoframework.md#dofinalsync12)用于加解密本次传入的数据，并获取加密或解密后的数据。
* 在数据存储或传输场景中，可以使用加解密操作用于保证数据的机密性，防止敏感数据泄露，详细可见[加解密开发指导](../harmonyos-guides/crypto-encrypt-decrypt-dev.md)。

## 问题定位

1. 从faultlogger目录下获取到应用的JsCrash故障日志，故障原因是Error，故障信息为do final fail!，数据加解密失败。

   ```screen
   Reason:Error
   Error name:Error
   Error message:do final fail!
   Error code:
   Stacktrace:
   Cannot get SourceMap info, dump raw stack:
       at decryptSync (entry|@pura/harmony-utils|1.3.4|src/main/ets/crypto/CryptoUtil.ts:26:1)
       at decryptSync (entry|@pura/harmony-utils|1.3.4|src/main/ets/crypto/SM4.ts:66:1)
       at decryptECBSync (entry|@pura/harmony-utils|1.3.4|src/main/ets/crypto/SM4.ts:54:1)
       at sm4Decode (entry|entry|1.0.0|src/main/ets/utils/j1.ts:93:1)
       at aboutToAppear (entry|entry|1.0.0|src/main/ets/pages/GWLogin.ts:316:1)
       at anonymous (entry|entry|1.0.0|src/main/ets/d/n1.ts:698:1)
   ```
2. 排查hilog日志，搜索关键字HCF，从JsCipherDoFinalSync[726]: failed to do final!日志中可以看出，应用在调用[doFinalSync](../harmonyos-references/js-apis-cryptoframework.md#dofinalsync12)接口失败。

   ```screen
   07-30 14:34:30.066 14335 14335 E C02F0A/com.hx.example/HCF: CommonDoFinal[592]: EVP_CipherFinal_ex failed!
   07-30 14:34:30.066 14335 14335 E C02F0A/com.hx.example/HCF: JsCipherDoFinalSync[726]: failed to do final!
   ```
3. 由于分组加密算法对分组长度存在限制，必须使用填充方法对每个分组补足到规定长度，如果不符合要求就会导致[doFinalSync](../harmonyos-references/js-apis-cryptoframework.md#dofinalsync12)接口失败，需要排查加密算法的填充模式以及明文的长度是否正常，以及加解密密钥是否一致。

## 分析结论

* 没有正确对明文进行填充，导致数据加解密失败。
* 加解密密钥不一致，导致无法正确解密。

## 修改建议

* 选择正确的填充模式，例如PKCS5和PKCS7，或自行填充。
* 确保加解密使用的密钥保持一致。

  ```screen
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';

  @Entry
  @Component
  struct EncryptComponent {
    @State data: string = '';
    @State encryptText: cryptoFramework.DataBlob | null = null;
    @State decryptTextString: string = '';
    @State result: string = '';

    // 加密消息
    encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
      let cipher = cryptoFramework.createCipher('SM4_128|ECB|PKCS7');
      cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, null);
      let encryptData = cipher.doFinalSync(plainText);
      return encryptData;
    }

    decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
      let decoder = cryptoFramework.createCipher('SM4_128|ECB|PKCS7');
      decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, null);
      let decryptData = decoder.doFinalSync(cipherText);
      return decryptData;
    }

    genSymKeyByData(symKeyData: Uint8Array) {
      let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
      let symGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
      let symKey = symGenerator.convertKeySync(symKeyBlob);
      return symKey;
    }

    encryptSuccess() {
      let keyData = new Uint8Array([7, 154, 52, 176, 4, 236, 150, 43, 237, 9, 145, 166, 141, 174, 224, 131]);
      let symKey = this.genSymKeyByData(keyData);
      let message = this.data;
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      this.encryptText = this.encryptMessage(symKey, plainText);
      this.result = `加密结果(DataBlob)：${this.encryptText.data.toString()}`;
    }

    decryptSuccess() {
      let keyData = new Uint8Array([7, 154, 52, 176, 4, 236, 150, 43, 237, 9, 145, 166, 141, 174, 224, 131]);
      let symKey = this.genSymKeyByData(keyData);
      if (this.encryptText != null) {
        let decryptText = this.decryptMessage(symKey, this.encryptText);
        this.decryptTextString = buffer.from(decryptText.data).toString('utf-8');
        this.result = `解密结果(DataBlob)：${decryptText.data.toString()}\n解密结果(string)：${this.decryptTextString}`;
      } else {
        this.result = '无加密内容，需先加密';
      }
    }

    build() {
      Column({ space: 15 }) {
        TextInput({ placeholder: '输入加密内容' })
          .onChange((value: string) => {
            this.data = value;
          })
          .margin({ left: 15, right: 15 })
        Button('加密')
          .onClick(() => {
            this.encryptSuccess();
          })
        Button('解密')
          .onClick(() => {
            this.decryptSuccess();
          })
        Text(this.result)
          .fontSize(20)
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center)
    }
  }
  ```
