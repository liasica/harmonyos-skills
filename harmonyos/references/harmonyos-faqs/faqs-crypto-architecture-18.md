---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-18
title: 如何将公钥转为十六进制或者base64进制数据
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 如何将公钥转为十六进制或者base64进制数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ab99d8cf63f46edf77ecfb061629191e035990bbddd1765f482d6d4f35ce1d15
---

公钥转为十六进制或Base64编码数据，参考代码如下：

```typescript
import { buffer, util } from '@kit.ArkTS';

@Entry
@Component
struct PubKeysConvert {
  build() {
    Column(){
      Button('公钥转十六进制').onClick(() => {
        let pubKeyData = '公钥'
        let res = buffer.from(pubKeyData).toString('hex')
        console.info('公钥转十六进制',res)
      })
      Button('公钥转base64').onClick(() => {
        let pubKeyUint8Array = new Uint8Array(buffer.from('公钥','utf-8').buffer)
        let res = new util.Base64Helper().encodeToStringSync(pubKeyUint8Array)
        console.info('公钥转base64',res)
      })
    }
  }
}
```
