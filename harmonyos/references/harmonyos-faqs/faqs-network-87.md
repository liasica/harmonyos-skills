---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-87
title: 实现手机端搭建HTTP服务端供电脑浏览器访问
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 实现手机端搭建HTTP服务端供电脑浏览器访问
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:04c6df0e00d300b5bde8aafd5b798459fb98f61e711dffa4e670011b802ecf5f
---

## 问题现象

如何实现一个基于HarmonyOS API的HTTP服务器？

## 背景知识

HarmonyOS没有提供HTTP服务端的实现接口，但是因为HTTP协议是基于TCP的，可以通过TCPSocketServer类用API接口，加上HTTP协议的格式，打造一个简单的HTTP服务端。

## 解决方案

用TCPSocket在服务端开启TCP监听，启动服务器来监听指定端口，接收客户端连接。当客户端发送消息时，服务器接收并返回响应。停止服务器时关闭连接监听，释放资源。

```ts
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

// 全局变量
let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

@Entry
@Component
struct Index {
  @State port: number = 8080;
  @State running: boolean = false;
  @State msgHistory: string = '';
  // 监听的ip地址，此处地址实际使用过程中替换为真实地址
  @State webUrl: string = 'xx.xx.xx';
  scroller: Scroller = new Scroller();

  build() {
    Column() {
      Text('HTTP服务器')
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .margin(10);

      Row() {
        Text('端口:')
          .fontSize(16)
          .margin(5);

        TextInput({ text: this.port.toString() })
          .onChange((value) => {
            this.port = parseInt(value) || 8080;
            this.webUrl = `${this.webUrl}:${this.port}`;
          })
          .type(InputType.Number)
          .width(80)
          .height(40)
          .margin(5);
      };

      Button(this.running ? '停止服务器' : '启动服务器')
        .onClick(() => {
          this.running = !this.running;
          if (this.running) {
            this.startServer();
          } else {
            this.stopServer();
          }
        })
        .width(200)
        .margin(10);

      Text('访问地址:')
        .fontSize(16)
        .margin(5);

      Text(this.webUrl)
        .fontSize(14)
        .textAlign(TextAlign.Start)
        .margin(5);

      Scroll(this.scroller) {
        Text(this.msgHistory)
          .textAlign(TextAlign.Start)
          .fontSize(12);
      }
      .height(300)
      .width('100%')
      .padding(10)
      .border({ width: 1, color: Color.Gray })
      .margin(10);
    }
    .width('100%')
    .height('100%')
    .padding(10);
  }

  // 开启服务
  startServer() {
    let listenAddr: socket.NetAddress = {
      address: '0.0.0.0',
      port: this.port,
      family: 1
    };

    tcpServer.listen(listenAddr, (err: BusinessError) => {
      if (err) {
        this.msgHistory += 'listen fail \r\n';
        return;
      }
      this.msgHistory += 'listen success \r\n';
    });

    // 连接后得到了clientSocket对象，然后继续订阅clientSocket对象的收到客户端消息事件
    tcpServer.on('connect', (clientSocket: socket.TCPSocketConnection) => {
      clientSocket.on('message', (msgInfo: socket.SocketMessageInfo) => {
        let requestMsg = buf2String(msgInfo.message);
        this.msgHistory += requestMsg + '\r\n';
        let resp = buildRespString(requestMsg);
        clientSocket.send({ data: resp });
      });
    });
  }

  stopServer() {
    tcpServer.off('connect');
  }
}

// 构造给客户端的应答内容
function buildRespString(content: string) {
  let result: string = '';
  let bodyContent = '<html>';
  bodyContent += '<head>';
  bodyContent += '<title>';
  bodyContent += 'HTTP服务器模拟';
  bodyContent += '</title>';
  bodyContent += '</head>';
  bodyContent += '<body>';
  bodyContent += '<h1>';
  bodyContent += '浏览器发送的请求信息';
  bodyContent += '</h1>';
  bodyContent += '<pre><h2>';
  bodyContent += content;
  bodyContent += '</h2></pre>';
  bodyContent += '</body>';
  bodyContent += '</html>';

  let textEncoder = new util.TextEncoder();
  let contentBuf = textEncoder.encodeInto(bodyContent);

  result += 'HTTP/1.1 200 OK \r\n';
  result += 'Content-Type: text/html; charset=utf-8 \r\n';
  result += `Content-Length: ${contentBuf.length} \r\n`;
  result += '\r\n';
  result += bodyContent;

  return result;
}

// ArrayBuffer转字符串
function buf2String(buf: ArrayBuffer): string {
  const msgArray = new Uint8Array(buf);
  const textDecoder = util.TextDecoder.create('utf-8');
  return textDecoder.decodeToString(msgArray);
}
```

## 总结

HarmonyOS API10提供了TCPSocketServer类，包含了如下几个关键接口：

* 监听方法，绑定IP地址和端口，端口可以指定或由系统随机分配。成功调用该方法后，[TCPSocketServer](../harmonyos-references/js-apis-socket.md#tcpsocketserver10)对象监听并接收与此套接字建立的TCPSocket连接。

  ```ts
  listen(address: NetAddress): Promise<void>
  ```
* 订阅TCPSocketServer的连接事件，在新的客户端套接字连接上以后，会触发callback回调，在回调中包含TCPSocketConnection对象，该对象就表示TCPSocket客户端与服务端的连接。

  ```ts
  on(type: 'connect', callback: Callback<TCPSocketConnection>): void
  ```

TCPSocketConnection是服务端和客户端通讯的基础。

* 提供了发送数据到客户端的方法：

  ```ts
  send(options: TCPSendOptions): Promise<void>
  ```
* 订阅客户端消息接收的事件：

  ```ts
  on(type: 'message', callback: Callback<SocketMessageInfo>): void
  ```

  在这个事件的callback回调里，包含了SocketMessageInfo参数，该参数的属性message就是客户端发送过来的消息。
