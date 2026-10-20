---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/crypto-architecture-kit-faq-0001
title: 公钥数据格式转换常见问题
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > 常见问题 > 公钥数据格式转换常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:53+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:01a824f1d1faf6221528c61fb277ab6605d1a9c882fe3c16187087bd67c7a4c3
---

**Q：如何将公钥转为十六进制或者base64进制数据？**

**A**：公钥转为十六进制或Base64编码数据，参考代码如下：

```ts
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
