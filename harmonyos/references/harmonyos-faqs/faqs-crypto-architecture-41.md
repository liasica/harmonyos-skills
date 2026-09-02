---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-41
title: decodeURI解码部分字符失败
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > decodeURI解码部分字符失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d1c445c43155fc65c86016012ec7016bdb1e65f176463123063da9d9eb50c45a
---

## 问题现象

decodeURI解码部分字符失败。

示例代码如下：

```ts
@Entry
@Component
struct FileDemo {
  @State message: string =
    "resource%3A%2F%2Frawfile%2Fsdym%2Findex.html%23%2Fpages%2Fcommon%2FwebviewH5"
  @State decodeURI: string = ''
  @State decodeURIComponent: string = ''

  build() {
    Row() {
      Column() {
        Button("decodeURI").fontSize(50).fontWeight(FontWeight.Bold).onClick(() => {
          this.decodeURI = decodeURI(this.message)
          console.info(`decodeURI: ${this.decodeURI}`) // decodeURI()函数可对encodeURI()函数编码过的URI进行解码。实际上应该是：resource://rawfile/sdym/index.html#/pages/common/webviewH5
        })
      }.width('100%')
    }.height('100%')
  }
}
```

日志信息参考如下：

```shell
05-30 13:47:10.873   21059-21059   A03D00/com.cnk...ication/JSAPP  com.cnki....lication  I     decodeURI: resource%3A%2F%2Frawfile%2Fsdym%2Findex.html%23%2Fpages%2Fcommon%2FwebviewH5
```

## 背景知识

* decodeURI(encodedURI)：其中encodedURI参数：完整的编码统一资源标识符，返回值：一个新字符串，表示给定编码的统一资源标识符（URI）的未编码版本。
* decodeURIComponent(encodedURI)使用与decodeURI()中描述的相同的解码算法。它解码所有转义序列，包括那些不是由encodeURIComponent创建的转义序列，例如：.-.!~\*'()。

## 解决方案

decodeURI()假定输入是完整的URI，因此它不会解码属于URI语法的字符，建议使用decodeURIComponent()方法。

示例代码如下：

```ts
@Entry
@Component
struct FileDemo {
  message: string =
    'resource%3A%2F%2Frawfile%2Fsdym%2Findex.html%23%2Fpages%2Fcommon%2FwebviewH5';
  @State decodeURI: string = '';
  @State decodeURIComponent: string = '';

  build() {
    Row() {
      Column() {
        Button('decodeURI').fontSize(30).fontWeight(FontWeight.Bold).onClick(() => {
          this.decodeURI = decodeURI(this.message);
          console.info(`decodeURI: ${this.decodeURI}`);
        });
        Text(`decodeURI:${this.decodeURI}`);
        Button('decodeURIComponent').fontSize(30).fontWeight(FontWeight.Bold).onClick(() => {
          this.decodeURIComponent = decodeURIComponent(this.message);
          console.info(`decodeURIComponent: ${this.decodeURIComponent}`);
        });
        Text(`decodeURI:${this.decodeURIComponent}`);
      }.width('100%');
    }.height('100%');
  }
}
```
