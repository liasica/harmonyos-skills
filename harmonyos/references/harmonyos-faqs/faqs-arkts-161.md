---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-161
title: emitter中接收ArrayBuffer使用console.log打印异常
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > emitter中接收ArrayBuffer使用console.log打印异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3dbf973cb3a4c002755f9380da45875a699e26a0c04c3604111fe4f23e981607
---

## 问题现象

emitter中接收传过来的ArrayBuffer，使用console.log方式打印ArrayBuffer，结果是{}。

## 背景知识

* [emitter](../harmonyos-references/js-apis-emitter.md)：提供了在同一进程不同线程间或同一线程内发送和处理事件的能力，支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。
* [Base64Helper](../harmonyos-references/js-apis-util.md#base64helper9)：Base64Helper类提供Base64编解码和Base64URL编解码功能。
* [TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)：TextDecoder用于将字节数组解码为字符串，支持utf-8、utf-16le/be、iso-8859和windows-1251等不同的编码格式。

## 问题定位

使用debug调试发现，ArrayBuffer数据正常发送，且正常接收到，使用console.log(${JSON.stringify(arrayBuffer)})二进制流时，显示异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ntUbGTUtTUKiDF4vd4IVyg/zh-cn_image_0000002628899070.png "点击放大")

## 分析结论

ArrayBuffer是原始字节流格式的数据，JSON.stringify会调用ArrayBuffer对象的toJSON()方法，默认没有实现这个方法，所以打印结果为空对象{}。

## 修改建议

由以上分析结论可知，要打印ArrayBuffer需要解码成对应格式才能打印：

可以使用[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)工具类将ArrayBuffer解码成字符串之后打印。

示例代码如下：

```ts
import { emitter } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct EmitterParam {
  private arrayBuffer = new ArrayBuffer(20);
  private str: string = 'Hello ArrayBuffer!';
  event: emitter.InnerEvent = {
    eventId: 1
  };
  // 自定义回调方法
  private callback = (eventData: emitter.EventData): void => {
    let arrayBuffer: ArrayBuffer = eventData.data!['buffer'];
    let textDecoder = new util.TextDecoder();
    let text = textDecoder.decodeToString(new Uint8Array(arrayBuffer));
    this.getUIContext().getPromptAction().showToast({
      message: `收到数据：${text}`
    });
    // 使用分段打印到控制台
    printInChunks(text);
  };

  aboutToAppear(): void {
    let bufView = new Uint8Array(this.arrayBuffer);
    for (let i = 0, strLen = this.str.length; i < strLen; i++) {
      bufView[i] = this.str.charCodeAt(i);
    }
    this.arrayBuffer = bufView.buffer as ArrayBuffer;
    emitter.on(this.event, this.callback); // 开启监听
  }

  build() {
    RelativeContainer() {
      Button(`发送数据: ${this.str}`).width('100%').height(100)
        .onClick(() => {
          let eventData: emitter.EventData = {
            data: {
              buffer: this.arrayBuffer
            }
          };
          emitter.emit(this.event, eventData);
        })
    }
    .height('100%')
    .width('100%')
  }
}

/*
 * 分段打印日志
 * */
function printInChunks(str: string, chunkSize = 1000) {
  for (let i = 0; i < str.length; i += chunkSize) {
    console.log(str.substring(i, i + chunkSize));
  }
}
```

## 常见FAQ

Q：为什么打印较长字符串hilog会截断？

A：console.log打印日志单次打印有长度限制，超出会被截断，可以使用分段打印。
