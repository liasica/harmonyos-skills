---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-44
title: "使用SocketServer时，如何解决较高概率接收不到 client.on(\"message\", (value: SocketInfo) 中的回调问题"
breadcrumb: "FAQ > 系统开发 > 网络 > 网络（Network） > 使用SocketServer时，如何解决较高概率接收不到 client.on(\"message\", (value: SocketInfo) 中的回调问题"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3bfced16c1c25300abdc65e3a604ff3bce0d290144a2a6ef63979388cb5ba855
---

**原因**

客户端的socket被回收释放而导致较高概率接收不到client.on("message", (value: SocketInfo) 中的回调。

**解决措施**

定义一个数组，客户端连接时，将客户端的socket添加到数组中，防止被回收，确保能接收数据。代码如下：

```typescript
import { socket } from '@kit.NetworkKit';

let tcpServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();
// 定义存放客户端连接的数组
let tcpConnectArray: socket.TCPSocketConnection[] = [];

class SocketInfo {
  message: ArrayBuffer = new ArrayBuffer(1);
  remoteInfo: socket.SocketRemoteInfo = {} as socket.SocketRemoteInfo;
}

@Entry
@Component
struct CreateSocket {
  build() {
    Column() {
      Button('创建socket').onClick(async () => {
        tcpServer.on('connect', (client: socket.TCPSocketConnection) => {
          // 保存客户端的socket
          tcpConnectArray.push(client);
          // Subscribe to events of the TCPSocketConnection object.
          client.on('close', () => {
            console.log("on close success");
          });
          client.on('message', (value: SocketInfo) => {
            // 此处高概率收不到message
            let buffer = value.message;
            let dataView = new DataView(buffer);
            let str = '';
            for (let i = 0; i < dataView.byteLength; ++i) {
              str += String.fromCharCode(dataView.getUint8(i));
            }
            console.log('received message--:' + str);
          });
        })
        console.log('create socket Succeeded ');
      })

    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
