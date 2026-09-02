---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-35
title: 如何使用ZeroPadding解决AES算法加密程序崩溃
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何使用ZeroPadding解决AES算法加密程序崩溃
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:777534c392e35a79e591ff63a2ef6a8d99c5ba12613ac7b4843120c0b8e8dacc
---

## 问题现象

使用AES算法的CBC模式加密，执行doFinalSync程序崩溃，问题代码如下：

```ts
function tcpEncrypt(value: string, iv: string, key: string): Uint8Array {
  let cipher = cryptoFramework.createCipher('AES128|CBC|NoPadding');
  let siv = genIvParamsSpec(iv);
  let symKey = genSymKeyByData(StrUtil.strToUint8Array(key));
  cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, siv);
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(value, 'utf-8').buffer) };
  let cipherData = cipher.doFinalSync(plainText);
  return cipherData.data;
}
```

日志如下:

```txt
Pid:41288
Uid:20020022
Reason:Error
Error name:Error
Error message:do final fail!
Error code:
Stacktrace:
 at tcpEncrypt (entry/src/main/ets/utils/Aes.ets:116:20)
 at tcpEncryptData (entry/src/main/ets/utils/Aes.ets:14:10)
 at toBuffer (entry/src/main/ets/utils/SQHeaderEx.ets:81:33)
 at send (entry/src/main/ets/utils/TcpSocket.ets:96:20)
 at getTcpPublicKey (entry/src/main/ets/utils/CommonUtil.ets:60:5)
 at anonymous (entry/src/main/ets/utils/TcpSocket.ets:42:7)
```

## 背景知识

[AES](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#aes)（Advanced Encryption Standard），最常见的对称加密算法。

基本特点：分组密码算法，分组长度为128位；密钥长度为128位、192位或256位；与3DES相比，安全性更高，处理速度更快。

由于AES为分组加密算法，分组长度为128位。在实际应用中，最后一组明文可能不足128位（16字节），此时可以通过不同的[填充模式](../harmonyos-guides/crypto-sym-encrypt-decrypt-spec.md#填充模式)进行数据填充。

## 问题定位

1. 检查秘钥是否正确。
2. 检查明文是否符合要求，确保明文中不包含汉字。
3. 检查加密算法的填充模式以及明文的长度。

## 分析结论

使用AES算法的CBC模式加密，由于最后一组明文不足128位，没有对明文进行填充导致崩溃。

## 修改建议

* 问题代码中填充模式选择NoPadding，不会对明文进行填充，所以当最后一组不足128位，导致程序崩溃，可以选择PKCS5和PKCS7进行填充。
* 如果需要ZeroPadding，需要开发者手动对密文进行填充，密文填充的示例代码如下：

  ```ts
  import { cryptoFramework } from '@kit.CryptoArchitectureKit';
  import { buffer } from '@kit.ArkTS';
  import { PromptAction } from '@kit.ArkUI';

  function generateRandom(len: number) {
    let rand = cryptoFramework.createRandom();
    let generateRandSync = rand.generateRandomSync(len);
    return generateRandSync;
  }

  function genIvParamsSpec() {
    let ivBlob = generateRandom(16);
    let ivParamsSpec: cryptoFramework.IvParamsSpec = {
      algName: 'IvParamsSpec',
      iv: ivBlob
    };
    return ivParamsSpec;
  }

  let iv = genIvParamsSpec();

  // 加密消息。
  function encryptMessage(symKey: cryptoFramework.SymKey, plainText: cryptoFramework.DataBlob) {
    let cipher = cryptoFramework.createCipher('AES128|CBC|NoPadding');
    cipher.initSync(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, iv);
    let cipherData = cipher.doFinalSync(plainText);
    return cipherData;
  }

  // 解密消息。
  function decryptMessage(symKey: cryptoFramework.SymKey, cipherText: cryptoFramework.DataBlob) {
    let decoder = cryptoFramework.createCipher('AES128|CBC|NoPadding');
    decoder.initSync(cryptoFramework.CryptoMode.DECRYPT_MODE, symKey, iv);
    let decryptData = decoder.doFinalSync(cipherText);
    return decryptData;
  }

  function genSymKeyByData(symKeyData: Uint8Array) {
    let symKeyBlob: cryptoFramework.DataBlob = { data: symKeyData };
    let aesGenerator = cryptoFramework.createSymKeyGenerator('AES128');
    let symKey = aesGenerator.convertKeySync(symKeyBlob);
    console.info('convertKeySync success');
    return symKey;
  }

  function stringPadding(str: string) {
    // 获取字符串长度
    let len = str.length;
    // 填充字符串到128位的整数倍
    if (len % 16 !== 0) {
      str = str.padEnd(len + 16 - (len % 16), '0');
    }
    return str;
  }

  function main(inputMessage:string) : boolean {
    try {
      let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
      let symKey = genSymKeyByData(keyData);
      let message = inputMessage;
      message = stringPadding(message);
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      let encryptText = encryptMessage(symKey, plainText);
      let decryptText = decryptMessage(symKey, encryptText);
      if (plainText.data.toString() === decryptText.data.toString()) {
        console.info('decrypt ok');
        console.info('decrypt plainText: ' + buffer.from(decryptText.data).toString('utf-8'));
        return true;
      } else {
        console.error('decrypt failed');
        return false;
      }
    } catch (error) {
      console.error(`AES CBC ${error}, error code: ${error.code}`);
      return false;
    }
  }

  @Entry
  @Component
  struct Index {
    @State inputMessage: string = '';
    @State paddingMessage: string = '';
    textInputController: TextInputController = new TextInputController();
    promptAction: PromptAction = this.getUIContext().getPromptAction();

    showResultToast(text:string) {
      this.promptAction.showToast({
        message: text,
        duration: 1000
      });
    }

    build() {
      Column({space: 10}) {
        Column() {
          Row() {
            Text('字符串')
              .width('100%')
              .fontSize(14)
              .fontColor('#e6000000')
              .fontWeight(FontWeight.Bold)
              .fontFamily('HarmonyOS Sans 2024 Light')
          }
          .justifyContent(FlexAlign.Start)

          Row() {
            TextInput({placeholder: '请输入文本！'})
              .type(InputType.Normal)
              .borderRadius('8')
              .onChange((value: string) => {
                // ZeroPadding不支持输入中文文本，请输入英文格式文本
                this.inputMessage = value;
              })
              .onDidDelete((info: DeleteValue) => {
                if (info.deleteOffset === 0) {
                  this.inputMessage = '';
                  this.paddingMessage = '';
                }
              })
          }
          .justifyContent(FlexAlign.Start)
          .width('100%')
          .margin({top: 5})

          Row() {
            Text('扩充后字符串')
              .width('100%')
              .fontSize(14)
              .fontColor('#e6000000')
              .fontWeight(FontWeight.Bold)
              .fontFamily('HarmonyOS Sans 2024 Light')
          }
          .justifyContent(FlexAlign.Start)
          .margin({top: 5})

          Row() {
            TextInput({ placeholder: '扩充后字符串', text: this.paddingMessage, controller: this.textInputController })
              .width('100%')
              .height('100%')
              .fontSize(12)
              .borderRadius('8')
              .backgroundColor('#0d000000')
          }
          .justifyContent(FlexAlign.Start)
          .margin({ top: 5 })
          .height(40)
        }
        .borderRadius(16)
        .backgroundColor('#FFFFFF')
        .height(160)
        .padding({
          top: 16,
          left: 16,
          right: 16,
          bottom: 16
        })
        .margin({ top: 8, left: 16, right: 16 })

        Button('扩充字符串')
          .onClick(() => {
            if (this.inputMessage) {
              this.paddingMessage = stringPadding(this.inputMessage);
              if (main(this.inputMessage)) {
                this.showResultToast('加解密成功！');
              } else {
                this.showResultToast('加解密失败！');
              }
            }
          })
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#fff1f3f5')
    }
  }
  ```

## 总结

算法库当前提供了[AES](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)加解密常用的7种加密模式：ECB、CBC、OFB、CFB、CTR、GCM和CCM。由于AES为分组加密算法，分组长度为128位。如果最后一组明文可能不足128位（16字节），可以通过不同的填充模式进行数据填充。

* ECB、CBC加密模式，明文长度不是128位整数倍，必须使用填充方法补足。
* CCM加密模式，必须指定附加验证数据且其长度必须大于等于1字节且小于等于2048字节。
