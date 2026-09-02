---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-29
title: 如何使用SM3算法生成散列值
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何使用SM3算法生成散列值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5c9a92c93ea4e6364d451308c2c710c114e160a97d3725acff1d5945c6c70676
---

调用[cryptoFramework.createMd](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatemd)方法，传入SM3，可参考如下代码：

```typescript
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util, buffer } from '@kit.ArkTS';

let base64 = new util.Base64Helper();

@Entry
@Component
struct SM3Encrypted {
  stringToUint8Array(str: string) {
    return new Uint8Array(buffer.from(str, 'utf-8').buffer);
  }

  // Complete the summary in Promise format
  doMdByPromise() {
    // Summary algorithm name.
    let mdAlgName = 'SM3';
    // The data to be summarized.
    let message = 'Hello,world';
    let md = cryptoFramework.createMd(mdAlgName);
    console.info('[Promise]: Md algName is: ' + md.algName);
    let promiseMdUpdate = md.update({ data: this.stringToUint8Array(message) });
    promiseMdUpdate.then(() => {
      // Call digest() to return the result.
      let PromiseMdDigest = md.digest();
      return PromiseMdDigest;
    }).then(digestOutput => {
      let mdOutput = digestOutput.data;
      // Uint8Array to base64
      let str2 = base64.encodeToStringSync(mdOutput);
      // Convert to hexadecimal
      let str = this.uint8ArrayToHexStr(mdOutput);
      console.info('[Promise]: MD result: ' + mdOutput);
      let mdLen = md.getMdLength();
      console.info('[Promise]: MD len: ' + mdLen);
    }).catch((error: BusinessError) => {
      console.error('[Promise]: error: ' + error.message);
    });
  }

  // The summary result is Uint8Array type, converted to hexadecimal string data
  uint8ArrayToHexStr(data: Uint8Array): string {
    let hexString = '';
    let i: number;
    for (i = 0; i < data.length; i++) {
      let char = ('00' + data[i].toString(16)).slice(-2);
      hexString += char;
    }
    return hexString;
  }

  build() {
    Column({ space: 10 }) {
      Button('使用SM3加密')
        .onClick(() => {
          this.doMdByPromise();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```
