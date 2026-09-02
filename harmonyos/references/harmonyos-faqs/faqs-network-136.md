---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-136
title: 如何解决LocalSocket创建报错
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决LocalSocket创建报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:36ab6ea7821442ae7c2dee13b9775a96f06d2a3c4bdfcfb9dfdf0c61efa008ce
---

## 问题现象

LocalSocket无法正常使用，常见问题：

1. 创建LocalSocket报错：2301111 Connection refused。
2. 创建LocalSocket/LocalSocketServer报错：2301002 No such file or directory。
3. 客户端发送数据，服务端没有监听到消息。

## 背景知识

* [LocalSocket](../harmonyos-references/js-apis-socket.md#localsocket11)：基于本地套接字文件建立数据流读写，相比TCP Scoket更加安全，不能通过抓包监听传输的数据，适用于同应用内不同进程间大量数据通信。跨应用间进程通信可参考[IPC与RPC通信开发指导](../harmonyos-guides/ipc-rpc-development-guideline.md)实现。
* [SOCKET 错误码](../harmonyos-references/errorcode-net-socket.md)：错误码映射关系为2301000+[内核错误码](../harmonyos-references/errorcode-kernel.md)，Server映射关系为2303100+[内核错误码](../harmonyos-references/errorcode-kernel.md)。比如2301111就是2301000+内核错误码111，在LocalSocket发起连接时出现。

## 问题定位

1. 报错2301111 Connection refused通常需要排查服务端是否可连接，在LocalSocket连接前需要创建并启动[LocalSocketServer](../harmonyos-references/js-apis-socket.md#localsocketserver11)，并检查LocalAddress是否一致。
2. 报错2301002 No such file or directory。对于LocalSocketServer，通常是没有本地套接字文件路径的权限，无法自动创建此文件。对于LocalSocket，除检查路径外，需要保证已提前创建LocalSocketServer并调用其[listen](../harmonyos-references/js-apis-socket.md#listen11)函数自动创建套接字文件。
3. 对于服务端无法监听到发送的消息，需要确保LocalSocket客户端在发送数据前，服务端已开启了[on('connect')](../harmonyos-references/js-apis-socket.md#onconnect11-1)以及回调中连接的[on('message')](../harmonyos-references/js-apis-socket.md#onmessage11-1)监听。否则服务端没有监听到客户端连接事件，就无法再监听到对应连接的其他事件。

## 分析结论

1. 2301002 No such file or directory问题：应用没有权限访问LocalAddress的address，或客户端没有使用同一个套接字文件。
2. 2301111 Connection refused和服务端没有接收到客户端发送的消息问题：使用LocalSocket时没有先启动LocalSocketServer，再启动客户端。

## 修改建议

1. LocalAddress的address配置应用沙箱路径，并且客户端和服务端使用同一个套接字文件：

   ```ts
   genLocalAddress(socketFileName: string) {
     let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let sandboxPath: string = context.filesDir + '/' + socketFileName;
     let localAddress: socket.LocalAddress = {
       address: sandboxPath
     };
     return localAddress;
   }
   ```
2. LocalSocket使用需要先启动LocalSocketServer：

   ```ts
   // 创建并绑定本地套接字文件，进行监听。
   this.server.listen(this.localAddress).then(() => {
     console.info('LocalSocket Server listen success');
   }).catch((err: BusinessError) => {
     console.error('LocalSocket Server listen fail: ' + JSON.stringify(err));
   });

   // 订阅LocalSocketServer的connect事件。
   this.server.on('connect', (connection: socket.LocalSocketConnection) => {
     console.info('LocalSocket Server 监听到客户端连接: ' + JSON.stringify(connection.clientId));
     // 订阅LocalSocketConnection相关的事件。
     connection.on('message', (value: socket.LocalSocketMessageInfo) => {
       console.info('LocalSocket Server total: ' + JSON.stringify(value));
       console.info('LocalSocket Server message information: ' + this.decodeMessage(value));
       // ...
     });

     connection.on('error', (err: BusinessError) => {
       console.error('LocalSocket Server err:' + JSON.stringify(err));
     });

     // 向客户端发送数据。
     this.sendMessage(connection, 'Hello Client!');
     // ...
   });
   ```
3. 再启动LocalSocket客户端发送消息：

   ```ts
   // 启动客户端端前，需要先启动LocalSocketServer，否则报错：2301111 Connection refused
   let connectOpt: socket.LocalConnectOptions = {
     address: this.localAddress,
     timeout: 6000
   };

   this.client.connect(connectOpt).then(() => {
     console.info('LocalSocket Client connect success');
   }).catch((err: BusinessError) => {
     console.error('LocalSocket Client connect fail: ' + JSON.stringify(err));
   });

   this.client.on('message', (value: socket.LocalSocketMessageInfo) => {
     console.info('LocalSocket Server total: ' + JSON.stringify(value));
     console.info('LocalSocket Server message information: ' + this.decodeMessage(value));
   });
   this.client.on('connect', () => {
     console.info('LocalSocket Client on connect');
   });
   this.client.on('close', () => {
     console.info('LocalSocket Client on close');
   });
   ```

完整示例如下：

```ts
import { socket } from '@kit.NetworkKit';
import { common } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct LocalSocketPage {
  private server: socket.LocalSocketServer = socket.constructLocalSocketServerInstance();
  private client: socket.LocalSocket = socket.constructLocalSocketInstance();
  private localAddress: socket.LocalAddress = this.genLocalAddress('socket_1'); // 创建本地文件，server和client均需对此路径具备访问权限

  genLocalAddress(socketFileName: string) {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let sandboxPath: string = context.filesDir + '/' + socketFileName;
    let localAddress: socket.LocalAddress = {
      address: sandboxPath
    };
    return localAddress;
  }

  decodeMessage(data: socket.LocalSocketMessageInfo): string {
    if (data?.message) {
      let decoder = util.TextDecoder.create('utf-8');
      let message = decoder.decodeToString(new Uint8Array(data.message));
      return message;
    }
    return '';
  }

  sendMessage(socket: socket.LocalSocket | socket.LocalSocketConnection, message: string): void {
    let sendOpt: socket.LocalSendOptions = {
      data: message
    };
    socket.send(sendOpt).then(() => {
      console.info('LocalSocket send message success');
    }).catch((err: BusinessError) => {
      console.info('LocalSocket send message failed: ' + JSON.stringify(err));
    });
  }

  build() {
    Column({ space: 24 }) {
      Button('启动LocalSocket服务端')
        .onClick(() => {
          // 创建并绑定本地套接字文件，进行监听。
          this.server.listen(this.localAddress).then(() => {
            console.info('LocalSocket Server listen success');
          }).catch((err: BusinessError) => {
            console.error('LocalSocket Server listen fail: ' + JSON.stringify(err));
          });

          // 订阅LocalSocketServer的connect事件。
          this.server.on('connect', (connection: socket.LocalSocketConnection) => {
            console.info('LocalSocket Server 监听到客户端连接: ' + JSON.stringify(connection.clientId));
            // 订阅LocalSocketConnection相关的事件。
            connection.on('message', (value: socket.LocalSocketMessageInfo) => {
              console.info('LocalSocket Server total: ' + JSON.stringify(value));
              console.info('LocalSocket Server message information: ' + this.decodeMessage(value));
              // ...
            });

            connection.on('error', (err: BusinessError) => {
              console.error('LocalSocket Server err:' + JSON.stringify(err));
            });

            // 向客户端发送数据。
            this.sendMessage(connection, 'Hello Client!');
            // ...
          });
        });
      Button('启动LocalSocket客户端').onClick(() => {
        // 启动客户端端前，需要先启动LocalSocketServer，否则报错：2301111 Connection refused
        let connectOpt: socket.LocalConnectOptions = {
          address: this.localAddress,
          timeout: 6000
        };

        this.client.connect(connectOpt).then(() => {
          console.info('LocalSocket Client connect success');
        }).catch((err: BusinessError) => {
          console.error('LocalSocket Client connect fail: ' + JSON.stringify(err));
        });

        this.client.on('message', (value: socket.LocalSocketMessageInfo) => {
          console.info('LocalSocket Server total: ' + JSON.stringify(value));
          console.info('LocalSocket Server message information: ' + this.decodeMessage(value));
        });
        this.client.on('connect', () => {
          console.info('LocalSocket Client on connect');
        });
        this.client.on('close', () => {
          console.info('LocalSocket Client on close');
        });
      });
      Button('客户端发送数据').onClick(() => {
        // 需要服务端先使用on('connect')、on('message')监听到客户端连接，否则无法监听到消息
        this.sendMessage(this.client, 'Hello Server!');
      });
    }
    .height('100%')
    .width('100%');
  }
}
```
