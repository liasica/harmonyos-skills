---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-81
title: http请求requestInStream接口如何使用
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求requestInStream接口如何使用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:f04f0bf51d45f2916f7a1445287f11f41b33162dd364a8fbf6f51a31e75b9ffa
---

## 问题现象

* 场景一：http请求requestInStream接口如何获取响应数据？
* 场景二：使用requestInStream流式请求时，on('headersReceive')偶尔出现无回调的情况。

## 背景知识

[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10)可以根据URL地址，发起http网络请求并返回流式响应。

## 解决方案

* 场景一：

  使用[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10)接口需要注意，callback回调返回的是number类型的数据，也就是响应码，不会返回具体的数据，可通过[on("dataReceive")](../harmonyos-references/js-apis-http.md#ondatareceive10)接收响应数据，当订阅成功时，error为undefined，data为接收到的http流式数据，类型为ArrayBuffer；否则为错误对象。

  ```ts
  import { http } from '@kit.NetworkKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  class Header {
    public contentType: string;

    constructor(contentType: string) {
      this.contentType = contentType;
    }
  }

  function createAndRequest() {
    let httpRequest = http.createHttp();
    let options: http.HttpRequestOptions = {
      method: http.RequestMethod.POST, // 可选，默认为http.RequestMethod.GET。
      // 当使用POST请求时此字段用于传递请求体内容，具体格式与服务端协商确定。
      extraData: 'data to send',
      expectDataType: http.HttpDataType.STRING, // 可选，指定返回数据的类型。
      usingCache: true, // 可选，默认为true。
      priority: 1, // 可选，默认为1。
      // 开发者根据自身业务需要添加header字段。
      header: new Header('application/json'),
      readTimeout: 60000, // 可选，默认为60000ms。
      connectTimeout: 60000, // 可选，默认为60000ms。
      usingProtocol: http.HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定。
      usingProxy: false, // 可选，默认不使用网络代理，自API 10开始支持该属性。
    };
    httpRequest.requestInStream('EXAMPLE_URL', options, (err: BusinessError<void>, data: number) => {
      if (!err) {
        console.info('requestInStream OK! ResponseCode is ' + JSON.stringify(data));
      } else {
        console.error('requestInStream ERROR : err = ' + JSON.stringify(err));
      }
    });
    httpRequest.on('dataReceive', (data: ArrayBuffer) => {
      console.info('dataReceive length: ' + JSON.stringify(data.byteLength));
    });
    httpRequest.on('dataEnd', () => {
      console.info('Receive dataEnd !');
      httpRequest.destroy();
    });
  }

  @Entry
  @Component
  struct Index {
    build() {
      RelativeContainer() {
        Button('click')
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            createAndRequest();
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  当所有数据接收完毕后，on('dataEnd', () => {})方法会被调用，标志着数据接收完成。在使用完http请求对象后，调用destroy()方法来主动销毁这个对象，避免资源泄露。
* 场景二：

  确保[on('headersReceive')](../harmonyos-references/js-apis-http.md#onheadersreceive8)在requestInStream之前同步执行，且无异步间隙：

  ```ts
  let httpRequest = http.createHttp();
  httpRequest.on('headersReceive', (header: Object) => {
    console.info(`header: ${JSON.stringify(header)}`);
  });
  // 之后再调用requestInStream
  httpRequest.requestInStream("EXAMPLE_URL", options).then(...);
  ```

  另外，可采取以下措施避免回调丢失：

  方式一：避免复用HttpRequest对象。每次请求都新建一个[http.createHttp()](../harmonyos-references/js-apis-http.md#httpcreatehttp)实例，并在请求结束后调用destroy()释放资源。

  方式二：使用[once('headersReceive')](../harmonyos-references/js-apis-http.md#onceheadersreceive8)替代on('headersReceive')。如果只需要一次回调，可改用once避免重复订阅带来的潜在问题。

  方式三：增加错误处理与日志。在requestInStream的catch中打印错误码和错误信息，判断是否因超时或网络异常导致：

  ```ts
  httpRequest.requestInStream("EXAMPLE_URL", options)
    .then(...)
    .catch((err: BusinessError) => {
      console.error(`requestInStream ERROR : err = ${JSON.stringify(err)}`);
    });
  ```

## 总结

requestInStream接口是用于处理http请求返回的流式数据的方法。在HarmonyOS中，当http请求的响应数据量较大时，比如超过5M、100M，使用requestInStream可以有效地处理这些数据，避免内存溢出等问题。

## 常见FAQ

Q：http发起的requestInStream流式请求，dataReceiveProgress无回调。

A：服务端需返回Content-Length字段，不然没有数据长度，dataReceiveProgress也就不会被触发。
