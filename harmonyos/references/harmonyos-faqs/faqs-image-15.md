---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-15
title: 如何实现PixelMap和base64的相互转换
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何实现PixelMap和base64的相互转换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e281a063d32dbe501bc758d39857ca33cec9322e89dba577b76f57bf88ce7d9f
---

PixelMap是无压缩的位图对象，包含像素数据以及基本的图片信息（如图片尺寸、像素密度、像素格式等）。

Base64编码是一种将二进制数据转换为ASCII字符串的编码方式，用于存储、传输。一般不会对PixelMap做Base64编码，而是将PixelMap编码成Uint8Array后，再对文件的二进制数据进行Base64编码。

* PixelMap文件转Base64
  1. 将PixelMap编码成ArrayBuffer数据

     需要通过ImagePacker的packToData方法从PixelMap对象中获取到ArrayBuffer类型数据。需要注意，使用ImagePacker对PixelMap进行编码，得到的图片文件和原始图片文件不能保证完全一致，这是因为编码算法、编码参数不同都会导致文件存在差异。如：原始图片文件在最初编码时设置的quality参数仅为80甚至更低，使用ImagePacker编码时将quality设为100，就会导致图片文件体积明显增大。
  2. 从ArrayBuffer数据获取到Uint8Array类型数据

     直接通过ArrayBuffer数据new出Uint8Array类型数据即可，例如：let uint8buffer = new Uint8Array(arrayBuffer)，其中arraybuffer为原始ArrayBuffer类型数据，uint8buffer为获取到的Uint8Array类型数据
  3. 将ArrayBuffer数据转换成Base64类型

     HarmonyOS的util工具函数提供了Base64Helper类，Base64Helper类中的encodeToStringSync方法可以将Uint8Array转换为Base64编码。如果要保证Base64编码后的结果仍能够解码成原始的图片文件，请直接使用Base64Helper类进行二进制数据转换操作，避免增加图片编解码相关操作。

* Base64转PixelMap文件
  1. 将Base64类型数据解析成ArrayBuffer类型

     同样的，可以通过Base64Helper类中的decodeSync方法可以将Base64数据解析成Uint8Array类型数据。
  2. 将Uint8Array类型数据转换成ArrayBuffer数据

     可以通过slice方法从Uint8Array数据获取到ArrayBuffer数据，例如：const arraybuffer: ArrayBuffer = uint8array.buffer.slice(0)，其中uint8buffer为原始Uint8Array类型数据，arraybuffer为获取到的ArrayBuffer类型数据
  3. 将ArrayBuffer数据转换成PixelMap类型

     可以通过ImageSource实现ArrayBuffer数据到PixelMap类型的转化。首先通过Image模块的createImageSource方法从ArrayBuffer中构造出ImageSource实例，然后通过ImageSource的createPixelMap方法解码出PixelMap类型数据。

**参考链接**

[图片编码](../harmonyos-guides/image-encoding-arts.md)

[图片解码](../harmonyos-guides/image-decoding-arts.md)

[Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)
