---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-36
title: 单元测试如何调用Socket服务
breadcrumb: FAQ > DevEco Studio > 应用测试 > 单元测试如何调用Socket服务
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:599b728a0973b05fde1893736e064779d987b01889b0f2e6f448c8361ea5eab2
---

## 问题现象

在[单元测试框架](../harmonyos-guides/unittest-guidelines.md#概述)中，如何对Socket服务进行测试。

## 背景知识

在[NetWork Kit](../harmonyos-guides/net-mgmt-overview.md)中，[Socket连接](../harmonyos-guides/socket-connection.md#简介)是实现网络通信的重要功能模块，支持TCP/UDP/Multicast/TLS协议。

## 解决方案

将待测设备既作为服务端又作为客户端，启动服务端和客户端，完成消息的自发自收。

1. 使用Socket服务需要在module.json5中申请ohos.permission.INTERNET权限。

   ```screen
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET",
     }
   ],
   ```
2. 在entry/src/ohosTest/ets/test目录下新建socketSelf.test.ets，实现服务端监听127.0.0.1:8080，客户端连接统一端口并发送HelloHypium，服务端收到原文后，在前面拼接Echo:再发回，客户端把回包内容与预期值做断言，判断是否相同。

   ```ts
   import { describe, it, expect } from '@ohos/hypium';
   import { socket } from '@kit.NetworkKit'
   const TAG: string = 'SocketSelfTest';

   export default function socketSelfTest() {
     describe('SocketSelfCommunicationTest', () => {
       it('手机自发自收 – 服务端+客户端在同一设备', 0, async (done: Function) => {
         /* ================= 1. 启动服务端 ================= */
         const server = socket.constructTCPSocketServerInstance();
         const addr: socket.NetAddress = {
           address: '127.0.0.1',
           port: 8080,
           family: 1
         };

         // 一步完成“绑定+监听”
         await new Promise<void>((resolve, reject) => {
           server.listen(addr, (err) => {
             if (err) {
               console.error(`${TAG} server listen fail: ${JSON.stringify(err)}`);
               reject(err);
             } else {
               console.info(`${TAG} server listening...`);
               resolve();
             }
           });
         });

         // 订阅server的connect事件，客户端与服务端建立连接后，返回一个TCPSocketConnection对象，用于与客户端通信（仅注册事件，不阻塞）
         server.on('connect', (clientSocket: socket.TCPSocketConnection) => {
           console.info(`${TAG} client on connected`);
           // clientSocket即为建立连接后获取到的连接对象，可以通过该对象订阅TCPSocketConnection相关的事件
           // 服务端接收到客户端发送的信息HelloHypium
           clientSocket.on('message', (value: socket.SocketMessageInfo) => {
             let buffer = value.message;
             let dataView = new DataView(buffer);
             let str = "";
             for (let i = 0; i < dataView.byteLength; ++i) {
               str += String.fromCharCode(dataView.getUint8(i));
             }
             console.info(`${TAG} server received message: ${str}`);
             console.info(`${TAG} server received address: ${value.remoteInfo.address}`);
             // 向客户端发送数据Echo:HelloHypium
             clientSocket.send({ data: `Echo:${str}` });
             console.info(`${TAG} server send message: Echo:${str}`)
           });
         });

         /* ================= 2. 启动客户端 ================= */
         const client = socket.constructTCPSocketInstance();
         const resp = await new Promise<string>((resolve, reject) => {
           client.connect({ address: addr, timeout: 5000 }, (err) => {
             if (err) {
               console.error(`${TAG} client connect fail: ${JSON.stringify(err)}`);
               reject(err);
               return;
             }
             console.info(`${TAG} client start connected`);

             // 连接成功之后，向服务端发送数据HelloHypium
             client.send({ data: 'HelloHypium' }, (err) => {
               if (err) {
                 console.error(`${TAG} client send fail: ${JSON.stringify(err)}`);
                 reject(err);
                 return;
               }
               console.info(`${TAG} client send message: HelloHypium`);
             });

             // 监听message事件，接收到消息时，执行回调函数
             client.on('message', (value: socket.SocketMessageInfo) => {
               let buffer = value.message;
               let dataView = new DataView(buffer);
               let str = "";
               for (let i = 0; i < dataView.byteLength; ++i) {
                 str += String.fromCharCode(dataView.getUint8(i));
               }
               console.info(`${TAG} client received: ${str}`);
               client.close();
               resolve(str);
             });
           });
         });

         /* ================= 3. 断言 & 清理 ================= */
         console.info(`${TAG} resp: ${resp}`);
         expect(resp).assertEqual('Echo:HelloHypium');
         server.off("connect");
         client.off("message");
         client.off("close");
         done();
       });
     });
   }
   ```
