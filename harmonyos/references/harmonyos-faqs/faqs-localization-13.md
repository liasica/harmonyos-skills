---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-13
title: 如何将文件转换成字符串
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何将文件转换成字符串
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:25a464da7716b5c6bddcde36ea3bc6642cbe42c90dd283b8a4f820148f1a0562
---

1. 获取resources/rawfile目录下对应的rawfile文件内容。
2. 调用util模块的TextDecoder将字节数组解码为字符串。
3. 对Uint8Array进行解码。

参考示例如下：

```typescript
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct FileToString {
  build() {
    Row() {
      Column() {
        Button('file to string')
          .onClick(() => {
            getContext().resourceManager.getRawFileContent('test.txt').then((value: Uint8Array) => {
              let textDecoder: util.TextDecoder = util.TextDecoder.create(); // Call the TextDecoder class of the til module
              let decodedString: string = textDecoder.decodeToString(value); // 对Uint8Array解码
              let strBase64 = new util.Base64Helper().encodeToStringSync(value); // Convert a Uint8Array to a Base64 string
              console.info('retStr:', decodedString);
              console.info('strBase64:', strBase64);
            }).catch((error: BusinessError) => {
              console.error(`callback getRawFileContent failed, error code: ${error.code}, message: ${error.message}.`);
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接**

[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)

[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)
