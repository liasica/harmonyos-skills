---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-88
title: HTTP请求过程中如何解决encodeURI无效问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HTTP请求过程中如何解决encodeURI无效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8270d7e88cd1e45c4f73fb84d09011a9a19200973584c7b413f19885aea81ce8
---

## 问题现象

HTTP请求中，使用encodeURI()转码并发送HTTP请求，后台收到字符串中的+号变成空格，导致异常。

## 背景知识

在构建HTTP GET或POST请求时，不应使用encodeURI()对完整的URI进行编码，因为它不会对&+和=这类在URL中具有特殊语义的字符进行编码，可以使用encodeURIComponent()进行编码。

## 解决方案

对于HTTP请求的键值对"key1=value1&key2=value2&key3=value3"的信息主体数据，需要使用encodeURIComponent()进行编码，可以将+和=等字符进行编码。

示例代码如下：

```ts
@Entry
@Component
struct EncodeURIDemo {
  message: string = 'GXH8yctxJJJNiWT+sBG3dA==';
  @State URIComponent: string = '';
  @State URICode: string = '';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
        Column() {
          Button() {
            Text('encodeURIComponent')
              .fontSize(15)
          }
          .type(ButtonType.Capsule)
          .onClick(() => {
            // 使用encodeURIComponent进行编码
            this.URIComponent = encodeURIComponent(this.message);
            console.info('encodeURIComponent：', this.message);
          })

          // 展示encodeURIComponent编码后的信息
          Text(this.URIComponent).fontSize(20)
            .fontWeight(FontWeight.Bold)
        }

        Column() {
          Button() {
            Text('encodeURI')
              .fontSize(15)
          }
          .type(ButtonType.Capsule)
          .onClick(() => {
            // 使用encodeURI进行编码
            this.URICode = encodeURI(this.message);
            console.info('encodeURI：', this.message);
          })

          // 展示encodeURI编码后的信息
          Text(this.URICode).fontSize(20)
            .fontWeight(FontWeight.Bold)
        }
      }
      .width('100%')
    }.height('100%')
  }
}
```

## 常见FAQ

Q：HarmonyOS NEXT系统上应用层开发是不是只支持HTTPS，不支持HTTP？

A：网络支持HTTP和HTTPS协议，具体可以参考[@ohos.net.http (数据请求)](../harmonyos-references/js-apis-http.md)。

Q：请求URL拼接参数包含中文，如：https://xxx.com?q=小会报错Bad Request。

A：将请求中的中文用encodeURIComponent编码处理即可，例如：encodeURIComponent('小')。
