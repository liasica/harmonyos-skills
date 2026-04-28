---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-137
title: gbk字符串TextEncoder编码结果属性buffer长度为何比编码结果长度略大
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > gbk字符串TextEncoder编码结果属性buffer长度为何比编码结果长度略大
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:17+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:9e517fb84079f919fd9458b3342abc069ed8e942755a9c59a21d7d7e5c3fe1c2
---

**问题现象**

TextEncoder编码字符串“你好abc”，格式是gbk，分别获取编码结果长度和编码结果属性buffer的长度。如下图显示：

TextEncoder编码结果属性buffer的长度比编码结果的长度略大。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/iQYEO_2VRdSiqDgW2_nXNw/zh-cn_image_0000002194318536.png?HW-CC-KV=V1&HW-CC-Date=20260428T002416Z&HW-CC-Expire=86400&HW-CC-Sign=5B9B64E4BD8EFD418B2C2F941C2F093C0239B949CC890C4BC1431F7643473FA8 "点击放大")

**原因解释**

在TextEncoder编码底层代码逻辑中，需要创建arraybuffer，通过分析创建的arraybuffer长度就是编码结果buffer属性的长度。

其创建的arraybuffer是用来存放编码结果的，在编码结果生成前时需要提前创建arraybuffer，而创建arraybuffer的长度是未知的，为了保证arraybuffer长度能够存放编码结果，其长度是取编码字符串中单个字符占用的最大字节数乘以字符串长度来设置的，因此导致了TextEncoder编码结果buffer属性的byteLength比编码结果的长度略大。

**解决措施**

如果需要使用TextEncoder编码结果属性buffer的byteLength准确长度，可以通过buffer自带函数slice，依据TextEncoder编码结果长度获取buffer的byteLength准确长度。示例如下：

```
1. let textEncoder = util.TextEncoder.create('gbk');
2. let rstEncodeData: Uint8Array = textEncoder.encodeInto('你好abc');
3. let length = rstEncodeData.length;
4. console.info("rstEncodeData.length = " + length);
5. let byteLength = rstEncodeData.buffer.byteLength;
6. console.info("rstEncodeData.buffer.byteLength = " + byteLength);
7. console.info("rstEncodeData.buffer.slice(0, length).byteLength = " + rstEncodeData.buffer.slice(0, length).byteLength);
8. // rstEncodeData.buffer.slice(0, length).byteLength = 7
```

[GBKStringBufferLength.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/GBKStringBufferLength.ets#L22-L29)
