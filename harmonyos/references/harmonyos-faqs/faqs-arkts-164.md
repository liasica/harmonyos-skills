---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-164
title: 如何解决网络传输中字节流解码为UTF-8时出现的乱码问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何解决网络传输中字节流解码为UTF-8时出现的乱码问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6bed4f382775d4538768483b586f5e788fa6d4d8951ef0b114edde6393dda4b0
---

## 问题现象

解析流式请求返回数据时，需要将其通过utf-8格式编码转换为字符串才能正常显示，但是过程出现了乱码“�”，怎么解决呢？

```ts
let httpRequest = http.createHttp()
httpRequest.on("dataReceive", (data: ArrayBuffer) => {
  let textDecoderOptions: util.TextDecoderOptions = {
    fatal: false,
    ignoreBOM : true
  }
  let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
  let uin8 = new Uint8Array(data)
  this.message += textDecoder.decodeToString(uin8, {stream: false})
});
httpRequest.on("dataEnd", () => {
  console.info("Receive dataEnd !");
  httpRequest.destroy();
});
```

## 背景知识

* UTF-8编码规则与字节长度：
  + UTF-8采用1-4个字节表示一个字符，具体长度由首字节的高位标志决定：

    首字节特征：0xxxxxxx（0-127）：单字节字符（如ASCII字符）。110xxxxx（194-223）：双字节字符的首字节。1110xxxx（224-239）：三字节字符的首字节。11110xxx（240-247）：四字节字符的首字节。
  + 后续字节特征：所有后续字节均以10开头（二进制前缀）。
* [util.TextDecoder：](../harmonyos-references/js-apis-util.md#textdecoder)用于将字节数组解码为字符串，支持utf-8、utf-16le/be、iso-8859和windows-1251等不同的编码格式。
* [DecodeToStringOptions：](../harmonyos-references/js-apis-util.md#decodetostringoptions12)用于配置decodeToString方法在解码字节流时的行为参数。
* [TextDecoderOptions：](../harmonyos-references/js-apis-util.md#textdecoderoptions11)解码相关选项参数，包含两个属性fatal和ignoreBOM。
* [http.on("dataReceive")：](../harmonyos-references/js-apis-http.md#ondatareceive10)订阅HTTP流式响应数据接收事件，HTTP流式响应（HTTP Streaming）是一种服务器将响应数据分块逐步传输给客户端的技术。

## 问题定位

1. 依据UTF-8编码规则，一个字符可能有多个字节，例如，汉字“请”的完整UTF-8编码为E8 AF 95（232, 175, 149），若仅有首字节232，解码时就会出现乱码或占位符。
2. 当util.TextDecoder.decodeToString的DecodeToStringOptions.stream参数设为false时，在流式响应事件中接收字节流数据，如果最后一个字符对应的字节序列被分割到两次传输中，解码后末尾部分就可能出现乱码“�”。
3. 当util.TextDecoder.decodeToString的DecodeToStringOptions.stream参数设置为true时，解码器会保留输入末尾不完整的字节序列，并将其与下一次调用decodeToString时传入的新数据拼接处理。但需注意，必须使用同一个util.TextDecoder实例进行连续解码；如果每次解析都创建新的解码器实例，将导致之前保留的缓冲区数据丢失。

## 分析结论

由以上问题定位分析可知，以下结论：

1. 流式响应数据分段传输，会存在将一个完整字符对应的字节序列可能会被分割。
2. 调用util.TextDecoder.decodeToString解码字节流时，其参数DecodeToStringOptions.stream设置为了false，如果对应的字节序列不完整时，便会出现乱码。
3. 创建util.TextDecoder的TextDecoderOptions配置这一步骤放在了流式响应回调里面，导致缓冲区每次接收响应时都会被重置，丢弃了缓冲字节，会产生了乱码。

## 修改建议

综合上面分析结论，需要进行以下两步修改：

1、util.TextDecoder的TextDecoderOptions配置应该放在全局作用域，而不是放在流式响应事件方法当中。这样避免每次解析字节流时都会重新创建TextDecoderOptions，缓冲区不会被重置。

2、util.TextDecoder.decodeToString解析数据的时候需要配置解析相关参数DecodeToStringOptions.stream设置为true，当解码字节流时，如果遇到不完整序列，会将该序列保存至缓冲区。

代码修改如下：

```ts
import { util } from '@kit.ArkTS';
import { http } from '@kit.NetworkKit';

@Entry
@Component
struct StreamDataDecodeDemo {
  message: string = '';

  build() {
    RelativeContainer() {
      Text('流式解码测试')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let httpRequest = http.createHttp();
          let options: http.HttpRequestOptions = {
            method: http.RequestMethod.POST,
            extraData: 'data to send',
          };
          httpRequest.requestInStream('EXAMPLE_URL', options, (err: BusinessError<void>, data: number) => {
            if (!err) {
              console.info('requestInStream OK! ResponseCode is ' + JSON.stringify(data));
            } else {
              console.error('requestInStream ERROR : err = ' + JSON.stringify(err));
            }
          });
          // 放在流式请求外部，防止在流式请求中每次接收到字节序列均创建，造成缓冲字节序列丢失。
          let textDecoderOptions: util.TextDecoderOptions = {
            fatal: false,
            ignoreBOM : true
          };
          let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
          httpRequest.on('dataReceive', (data: ArrayBuffer) => {
            let uin8 = new Uint8Array(data);
            this.message += textDecoder.decodeToString(uin8, {stream: true});
          });
          httpRequest.on('dataEnd', () => {
            console.info('Receive dataEnd !');
            httpRequest.destroy();
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 总结

流式HTTP请求数据往往不会一次性全部接收，而是每次接收一部分字节序列数据。由于中文一般对应2-4个字节，如果流式响应恰好将一个中文的多个字节分成两部分接收，解码后就会出现乱码的现象。所以需要将DecodeToStringOptions.stream设置为true，不完整字节序列就会存储在TextDecoder字节缓冲区当中，会追加在下次调用decodeToString的参数之前；另外，需要将TextDecoderOptions放在全局作用域创建，防止在每次响应当中重新创建TextDecoder对象，造成TextDecoder字节缓冲区丢失。
