---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-11
title: 如何对大文件进行SM4加密
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何对大文件进行SM4加密
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3e27fb5acbe4361c034879c5914083f6ebae0427a6fd5ce2e8f28e5d422d3eb
---

使用分段加解密时，对于ECB和CBC模式，不论update传入的数据是否为分组长度的整数倍，都会以分组为单位进行加/解密，并输出本次update产生的新分组结果。当update积累的数据达到分组长度时产生输出，否则返回null。未加/解密的数据将保留，等待下一次update/doFinal时拼接继续处理。最后，doFinal会将剩余未加/解密的数据，根据创建cipher时设置的padding模式进行填充，补齐到分组的整数倍长度，再输出剩余加解密结果。

参考代码如下：

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function genIvParamsSpec() {
  let arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  let dataIv = new Uint8Array(arr);
  // The production environment should use randomly generated IVs. All zeros here are only for display purposes.
  let ivBlob: cryptoFramework.DataBlob = { data: dataIv };
  let ivParamsSpec: cryptoFramework.IvParamsSpec = {
    algName: 'IvParamsSpec',
    iv: ivBlob
  };
  return ivParamsSpec;
}

function stringToUint8Array(str: string): Uint8Array {
  let arr: Array<number> = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  }
  return new Uint8Array(arr);
}

async function testAesMultiUpdate(plainText: string) {
  let symAlgName = 'SM4_128';
  let length = 1024;
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
  let cipherAlgName = 'SM4_128|CBC|PKCS7';
  let globalCipher = cryptoFramework.createCipher(cipherAlgName);
  let result = new Uint8Array();
  let data: cryptoFramework.DataBlob;
  let startEncrypt = 0;
  let endEncrypt = 0;
  let promiseSymKey = await symKeyGenerator.generateSymKey();
  await globalCipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, promiseSymKey, genIvParamsSpec());
  let updateOutput: cryptoFramework.DataBlob;
  while (plainText.length > 0) {
    const contentCurr = plainText.substring(0, length);
    plainText = plainText.substring(length, plainText.length);
    let messageBlob: cryptoFramework.DataBlob = { data: stringToUint8Array(contentCurr) };
    updateOutput = await globalCipher.update(messageBlob);
    if (updateOutput !== null) {
      let mergeText = new Uint8Array(result.length + updateOutput.data.length);
      mergeText.set(result);
      mergeText.set(updateOutput.data, result.length);
      result = mergeText;
    }
  }
  startEncrypt = new Date().getTime();
  data = await globalCipher.doFinal(null);
  endEncrypt = new Date().getTime();
  console.info('TEST加密' + (endEncrypt - startEncrypt));
  let mergeText = new Uint8Array(result.length + data.data.length);
  mergeText.set(result);
  mergeText.set(data.data, result.length);
  result = mergeText;
  let contentTemp = result;
  console.info('TEST加密成功', contentTemp);
  await globalCipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, promiseSymKey, genIvParamsSpec());
  console.info('TEST == 长度' + contentTemp.length);
}

@Entry
@Component
struct SM4Encryption {
  @State message: string = 'Hello World';

  aboutToAppear(): void {
    testAesMultiUpdate('123456789102345566478416518498454151689546549849');
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('SM4EncryptionHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

**参考链接**

[@ohos.security.cryptoFramework (加解密算法库框架)](../harmonyos-references/js-apis-cryptoframework.md)
