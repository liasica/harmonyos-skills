---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-178
title: Buffer如何追加数据
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > Buffer如何追加数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c6cf99edc90fb3a7f92e1eb1c41fa5bf47c281cecbf020c6cd0aee88ee8e0d0
---

## 问题现象

[Buffer](../harmonyos-guides/buffer.md)没有看到writeBuffer(buffer: Buffer)方法，如何实现追加流？

## 背景知识

* [Buffer](../harmonyos-guides/buffer.md)将内存区域抽象为可读写、修改的逻辑对象，提供高效的二进制数据处理接口。每个Buffer实例是连续的字节序列，支持创建自定义大小的内存块，用于存储和操作序列化后的数据。
* [Buffer.concat](../harmonyos-references/js-apis-buffer.md#bufferconcat)将数组中的内容复制指定字节长度到新的Buffer对象中并返回。
* [Buffer.fill](../harmonyos-references/js-apis-buffer.md#fill)使用value填充当前对象指定位置的数据，默认为循环填充，并返回填充后的Buffer对象。

## 解决方案

Buffer对象需要指定大小初始化且内存容量固定。

1. Buffer已填充满数据，通过[concat](../harmonyos-references/js-apis-buffer.md#bufferconcat)合并Buffer对象并返回新的Buffer对象。

   ```ts
   let buf1 = buffer.from('1234');
   let buf2 = buffer.from('abcd');
   let buf = buffer.concat([buf1, buf2]);
   console.info('已填充数据',buf.toString()); // 1234abcd
   ```
2. Buffer未填充满数据，通过[Buffer.fill](../harmonyos-references/js-apis-buffer.md#fill)填充数据。

   ```ts
   let buf = buffer.allocUninitializedFromPool(8);
   buf.fill(buffer.from('1234'), 0, 4);
   buf.fill(buffer.from('abcd'), 4, 8);
   console.info(buf.toString()); // 1234abcd
   ```

完整示例代码如下：

```ts
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('已填充数据')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          let buf1 = buffer.from('1234');
          let buf2 = buffer.from('abcd');
          let buf = buffer.concat([buf1, buf2]);
          console.info('已填充数据',buf.toString()); // 1234abcd
        })

      Text('未填充满数据')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          let buf = buffer.allocUninitializedFromPool(8);
          buf.fill(buffer.from('1234'), 0, 4);
          buf.fill(buffer.from('abcd'), 4, 8);
          console.info(buf.toString()); // 1234abcd
        })
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

## 总结

ArkTS的Buffer对象的内容可以在创建后修改，但其长度是固定的，不能动态改变。
