---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-108
title: socket.TCPSocketServer订阅'connect'事件，off掉之后，重新订阅不生效
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > socket.TCPSocketServer订阅'connect'事件，off掉之后，重新订阅不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:75a36fdc00e3587958a1dee9e8f8c7415c4d1f92f932e8843cbc5db2fa61aa0a
---

## 问题现象

socket.TCPSocketServer订阅'connect'事件，off掉之后，重新订阅，回调方法不生效。问题代码如下：

```ts
// 开启serverSocket监听
const tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
let bindAddr: socket.NetAddress = {
  address: '::',
  port: 1111,
  family: 25
};
// 设置TCPSocketServer连接的其他属性
const options: socket.TCPExtraOptions = {
  keepAlive: true,
};
tcpServer.setExtraOptions(options);
tcpServer.listen(bindAddr).then(() => {
  console.info(TAG, 'bind address success');
}).catch((err: BusinessError) => {
  console.error(TAG, `server listen error : ${err.message}`);
});

// 订阅TCPSocketServer的事件
const connectCallBack = () => {
  console.info('test');
};
tcpServer.on('connect', connectCallBack);

tcpServer.off('connect', connectCallBack);
// 回调不生效了
tcpServer.on('connect', connectCallBack);
```

## 背景知识

* [TCPSocketServer.listen](../harmonyos-references/js-apis-socket.md#listen10)：绑定IP地址和端口，端口可以指定或由系统随机分配。监听并接受与此套接字建立的TCPSocket连接。
* [TCPSocketServer.on('connect')](../harmonyos-references/js-apis-socket.md#onconnect10)：订阅TCPSocketServer的连接事件。

## 解决方案

根据官网文档[on('connect')](../harmonyos-references/js-apis-socket.md#onconnect10)说明，listen方法调用成功后，才可调用此方法。因此on('connect')重新开启监听之前，重新调用listen并成功即可：

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';
import { webview } from '@kit.ArkWeb';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

@Entry
@Component
struct tcpServerTest {
  @State port: number = 8080;
  @State running: boolean = false;
  @State msgHistory: string = '';
  @State webUrl: string = 'xx.com';
  scroller: Scroller = new Scroller();
  webScroller: Scroller = new Scroller();
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row(){
        Text('端口')
          .fontSize(15)
          .height(40)
          .alignRules({
            left: { anchor: '__container__', align: HorizontalAlign.Start },
            top: { anchor: 'txtTitle', align: VerticalAlign.Bottom }
          })
          .padding(10)

        TextInput({ text: this.port.toString() })
          .onChange((value) => {
            this.port = parseInt(value);
          })
          .type(InputType.Number)
          .width(80)
          .height(40)
          .fontSize(15)
          .alignRules({
            left: { anchor: 'txtPort', align: HorizontalAlign.End },
            top: { anchor: 'txtPort', align: VerticalAlign.Top }
          })
          .padding(10)

        Button(this.running ? '停止' : '启动')
          .onClick(() => {
            this.running = !this.running;
            if (this.running) {
              this.start();
            } else {
              this.stop();
            }
          })
          .height(40)
          .width(80)
          .fontSize(15)
          .alignRules({
            right: { anchor: '__container__', align: HorizontalAlign.End },
            top: { anchor: 'txtPort', align: VerticalAlign.Top }
          })
          .padding(10)

        Button('重新订阅')
          .onClick(() => {
            this.start();
          })
          .alignRules({
            left: { anchor: '__container__', align: HorizontalAlign.End },
            top: { anchor: 'txtTitle', align: VerticalAlign.Top }
          })
          .padding(10)
          .height(40)
      }
      Scroll(this.scroller) {
        Text(this.msgHistory)
          .textAlign(TextAlign.Start)
          .padding(10)
          .width('100%')
          .fontSize(12)
          .backgroundColor(0xeeeeee)
      }
      .alignRules({
        left: { anchor: '__container__', align: HorizontalAlign.Start },
        top: { anchor: 'butRun', align: VerticalAlign.Bottom }
      })
      .align(Alignment.Top)
      .backgroundColor(0xeeeeee)
      .height(200)
      .scrollable(ScrollDirection.Vertical)
      .scrollBar(BarState.On)
      .scrollBarWidth(20)
      .padding(10)

      Row(){
        Text('请求地址')
          .id('txtUrl')
          .fontSize(15)
          .height(40)
          .alignRules({
            left: { anchor: '__container__', align: HorizontalAlign.Start },
            top: { anchor: 'scrollHis', align: VerticalAlign.Bottom }
          })
          .padding(10)
        TextInput({ text: this.webUrl.toString() })
          .onChange((value) => {
            this.webUrl = value;
          })
          .height(40)
          .fontSize(15)
          .padding(10)
          .width(200)
        Button('请求')
          .onClick(() => {
            this.controller.loadUrl(this.webUrl);
          })
          .height(40)
          .width(80)
          .fontSize(15)
          .alignRules({
            right: { anchor: '__container__', align: HorizontalAlign.End },
            top: { anchor: 'txtUrl', align: VerticalAlign.Top }
          })
          .padding(10)
      }
      Scroll(this.webScroller) {
        Web({ src: this.webUrl, controller: this.controller })
          .padding(10)
          .width('100%')
          .backgroundColor(0xeeeeee)
          .textZoomRatio(200)
          .fileAccess(false)
          .geolocationAccess(false)
      }
      .alignRules({
        left: { anchor: '__container__', align: HorizontalAlign.Start },
        top: { anchor: 'txtUrl', align: VerticalAlign.Bottom },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
      })
      .backgroundColor(0xeeeeee)
      .scrollable(ScrollDirection.Vertical)
      .scrollBar(BarState.On)
      .scrollBarWidth(20)
      .align(Alignment.Top)
    }
    .height('100%')
    .width('100%')
  }

  start() {
 // 将url替换成有效的链接资源，例如使用本地环回地址
    this.webUrl = 'xxx' + this.port.toString();
    let listenAddr: socket.NetAddress = {
      address: '0.0.0.0',
      port: this.port,
      family: 1
    };
    // listen方法调用成功后，调用on('connect')开启监听
    tcpServer.listen(listenAddr, (err: BusinessError) => {
      if (err) {
        this.msgHistory += 'listen fail \r\n';
        return;
      }
      this.msgHistory += 'listen success \r\n';
      console.info('listen success');
      tcpServer.on('connect', (clientSocket: socket.TCPSocketConnection) => {
        console.info(`connect success: ${JSON.stringify(clientSocket)}`);
        clientSocket.on('message', (msgInfo: socket.SocketMessageInfo) => {
          let textDecoder = util.TextDecoder.create('utf-8');
          let requestMsg = textDecoder.decodeToString(new Uint8Array(msgInfo.message));
          let resp = buildRespString(requestMsg);
          clientSocket.send({ data: resp });
        });
      });
    });
  }
  // 关闭监听
  stop() {
    tcpServer.off('connect');
    console.info('close listen connect');
  }
}

//构造给客户端的应答内容
function buildRespString(content: string) {
  let result: string = '';
  let bodyContent = `<html><head><title>HTTP服务器模拟</title></head><body><h1>浏览器发送的请求信息</h1><pre><h2>${content}</h2></pre></body></html>`;
  let textEncoder = new util.TextEncoder();
  let contentBuf = textEncoder.encodeInto(bodyContent);
  result += `HTTP/1.1 200 OK \r\nContent-Type: text/html; charset=utf-8 \r\nContent-Length: ${contentBuf.length} \r\n\r\n${bodyContent}`;
  return result;
}
```
