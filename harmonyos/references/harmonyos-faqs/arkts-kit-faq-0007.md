---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0007
title: Base64编码与转换常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见问题 > Base64编码与转换常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:19+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:9e4e354a4ab55506ed82dc4dab084b157ba344ab02d6d3884e1bbd8a5876da38
---

**Q：如何进行base64编码？**

**A**：可使用util中的Base64Helper()方法进行base64编码，参考代码如下：

```ts
import { util } from '@kit.ArkTS';

@Entry
@Component
struct Base64Encode {
  @State message: string = 'Base64 encoding';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let base64 = new util.Base64Helper();
            let arr = new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56]);
            let base64Str = base64.encodeToStringSync(arr); // Uint8Array to base64
            console.log('encodeToStringSync',base64Str);
            // base64.decodeSync(''); // base64 to Uint8Array
            // console.log('decodeSync',base64.decodeSync(''));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
