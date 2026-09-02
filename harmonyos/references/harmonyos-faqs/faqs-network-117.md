---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-117
title: Native侧如何实现socket连接
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > Native侧如何实现socket连接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:ef11f8f92db8601aa34ffc20b7e99823a9b759906707edcad547ebe0bbca36c3
---

## 问题现象

在ArkTS侧，声明了一个socket server并运行，然后调用Native侧方法进行socket连接。Native侧代码运行了，但是ArkTS侧未收到连接及消息。Native如何实现socket连接？

## 背景知识

* int **socket**(int af, int type, int protocol)创建套接字。

  | 参数 | 说明 |
  | --- | --- |
  | af | 地址族（Address Family）：也就是 IP 地址类型，常用的有 AF\_INET 和 AF\_INET6。AF\_INET 表示 IPv4 地址，例如 127.0.0.1；AF\_INET6 表示 IPv6 地址，例如 1030::C9B4:FF12:48AA:1A2B。 |
  | type | 数据传输方式/套接字类型：常用的有 SOCK\_STREAM（流格式套接字/面向连接的套接字） 和 SOCK\_DGRAM（数据报套接字/无连接的套接字）。 |
  | protocol | 传输协议。 |
* **sockaddr\_in**：internet环境下套接字的地址形式。
* **htons**：将主机的无符号短整形数转换成网络字节顺序。简单来说就是将一个数的高低位互换(如：1234-->3412)。
* int **inet\_pton**(int af, const character \*src, void \*dst)：用于转换互联网地址，即IP地址，以文本形式包含数字二进制格式。该函数用于将人类可读的IP地址转换为二进制格式的地址。

  | 参数 | 说明 |
  | --- | --- |
  | af | 地址族（Address Family）。 |
  | sourc | 指的是传递给它的字符串。 |
  | dst | 指向缓冲区，该缓冲区是inet\_pton()在转换后存储的数字地址的存储器。系统调用者确保缓冲区的存储能力。它确保 "dst "所分配的缓冲区足够大，以容纳数字地址。 |
* int **connect**(int sock, struct sockaddr \*serv\_addr, socklen\_t addrlen)建立连接。

  | 参数 | 说明 |
  | --- | --- |
  | sock | socket 文件描述符。 |
  | serv\_addr | sockaddr 结构体变量的指针。 |
  | addrlen | addr 变量的大小，可由 sizeof() 计算得出。 |
* int **send**(SOCKET sock, const char \*buf, int len, int flags)发送数据。

  | 参数 | 说明 |
  | --- | --- |
  | sock | 要发送数据的套接字。 |
  | buf | 要发送的数据的缓冲区地址。 |
  | len | 要发送的数据的字节数。 |
  | flags | 发送数据时的选项。 |
* **recv()**：接收数据。有阻塞模式和非阻塞模式两种工作方式，取决于套接字的设置。
  + 阻塞模式：默认模式。当调用recv函数时，如果套接字的接收缓冲区中没有数据可读，调用将一直阻塞，直到有数据到达或者发生错误。

    适用于数据到达频率较低或数据量较大的场景，简化编程逻辑。
  + 非阻塞模式：通过fcntl函数将套接字设置为非阻塞模式。调用recv时，如果套接字的接收缓冲区中没有数据可读，调用将立即返回，返回值为-1，并且errno被设置为EWOULDBLOCK或EAGAIN。

    适用于需要快速响应或处理多个连接的场景，提高程序的响应速度和处理能力。
* 在非阻塞模式下，recv函数可能会立即返回EAGAIN或EWOULDBLOCK，表示没有数据可读。为了正确处理这种情况，需要使用select或poll等函数来等待数据可读。
* 网络连接属于耗时任务，所以需要在Native侧创建子线程去执行连接任务，避免主线程因连接时间较长触发[THREAD\_BLOCK\_6S](../harmonyos-guides/appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时)。

## 解决方案

1. Native侧：服务端接口实现。

   ```cpp
   /*
    * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
    */
   // napi_init.cpp
   #include "napi/native_api.h"
   #include <arpa/inet.h>
   #include <cstring>
   #include <sys/socket.h>
   #include <unistd.h>
   #include <thread>

   #include "hilog/log.h"
   #undef LOG_DOMAIN
   #undef LOG_TAG
   #define LOG_DOMAIN 0x3200        // 全局domain宏，标识业务领域
   #define LOG_TAG "Native侧的日志" // 全局tag宏，标识模块日志tag

   #include <fcntl.h>
   #include <sys/select.h>

   // 阻塞模式
   static napi_value ConnectJoin(napi_env env, napi_callback_info info)
   {
       napi_value result;
       std::thread th([]() {
           auto clientSocket = socket(AF_INET, SOCK_STREAM, 0);
           if (clientSocket == -1) {
               OH_LOG_ERROR(LOG_APP, "创建socket失败");
               return;
           }

           sockaddr_in serverAddr;
           serverAddr.sin_family = AF_INET;
           serverAddr.sin_port = htons(1234);
           if (inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr) <= 0) {
               OH_LOG_ERROR(LOG_APP, "无效地址");
               return;
           }
           // 连接到服务器
           int res = connect(clientSocket, (sockaddr *)&serverAddr, sizeof(serverAddr));
           if (res < 0) {
               OH_LOG_ERROR(LOG_APP, "连接失败:%{public}d", res);
               return;
           }
           // 发送消息
           const char *message = "I am blocking information from Client.";
           send(clientSocket, message, strlen(message), 0);

           // 接收服务器响应
           char buffer[1024] = {0};
           int bytesReceived = recv(clientSocket, buffer, sizeof(buffer) - 1, 0);
           if (bytesReceived > 0) {
               buffer[bytesReceived] = '\0'; // 确保字符串结束
               OH_LOG_INFO(LOG_APP, "客户端接收到信息: %{public}s", buffer);
           } else {
               OH_LOG_ERROR(LOG_APP, "接收失败");
           }

           // 关闭socket
           close(clientSocket);
       });
       th.detach();
       napi_create_double(env, 1, &result);
       return result;
   }

   // 非阻塞模式
   static napi_value ConnectNotJoin(napi_env env, napi_callback_info info)
   {
       napi_value result;
       std::thread th([]() {
           auto clientSocket = socket(AF_INET, SOCK_STREAM, 0);
           if (clientSocket == -1) {
               OH_LOG_ERROR(LOG_APP, "创建socket失败");
               return;
           }

           // 设置为非阻塞模式
           int flags = fcntl(clientSocket, F_GETFL, 0);
           if (flags == -1) {
               OH_LOG_ERROR(LOG_APP, "获取文件描述符标志失败");
               close(clientSocket);
               return;
           }
           if (fcntl(clientSocket, F_SETFL, flags | O_NONBLOCK) == -1) {
               OH_LOG_ERROR(LOG_APP, "设置非阻塞模式失败");
               close(clientSocket);
               return;
           }

           sockaddr_in serverAddr;
           serverAddr.sin_family = AF_INET;
           serverAddr.sin_port = htons(1234);
           if (inet_pton(AF_INET, "127.0.0.1", &serverAddr.sin_addr) <= 0) {
               OH_LOG_ERROR(LOG_APP, "无效地址");
               close(clientSocket);
               return;
           }

           // 连接到服务器
           int res = connect(clientSocket, (sockaddr *)&serverAddr, sizeof(serverAddr));
           if (res < 0) {
               if (errno != EINPROGRESS) {
                   OH_LOG_ERROR(LOG_APP, "连接失败: %{public}d", errno);
                   close(clientSocket);
                   return;
               }

               // 使用select等待连接完成
               fd_set writefds;
               FD_ZERO(&writefds);
               FD_SET(clientSocket, &writefds);

               struct timeval timeout;
               timeout.tv_sec = 5; // 设置超时时间为5秒
               timeout.tv_usec = 0;

               res = select(clientSocket + 1, NULL, &writefds, NULL, &timeout);
               if (res <= 0) {
                   OH_LOG_ERROR(LOG_APP, "连接超时或失败: %{public}d", res);
                   close(clientSocket);
                   return;
               }

               // 检查连接是否成功
               int soError;
               socklen_t len = sizeof(soError);
               if (getsockopt(clientSocket, SOL_SOCKET, SO_ERROR, &soError, &len) < 0) {
                   OH_LOG_ERROR(LOG_APP, "获取连接状态失败: %{public}d", errno);
                   close(clientSocket);
                   return;
               }
               if (soError != 0) {
                   OH_LOG_ERROR(LOG_APP, "连接失败: %{public}d", soError);
                   close(clientSocket);
                   return;
               }
           }

           // 发送消息
           const char *message = "I am non-blocking information from Client. ";
           send(clientSocket, message, strlen(message), 0);

           // 接收服务器响应
           char buffer[1024] = {0};
           int bytesReceived = 0;

           // 使用select等待数据可读
           fd_set readfds;
           FD_ZERO(&readfds);
           FD_SET(clientSocket, &readfds);

           struct timeval timeout;
           timeout.tv_sec = 5; // 设置超时时间为5秒
           timeout.tv_usec = 0;

           res = select(clientSocket + 1, &readfds, NULL, NULL, &timeout);
           if (res > 0) {
               if (FD_ISSET(clientSocket, &readfds)) {
                   bytesReceived = recv(clientSocket, buffer, sizeof(buffer) - 1, 0);
                   if (bytesReceived > 0) {
                       buffer[bytesReceived] = '\0'; // 确保字符串结束
                       OH_LOG_INFO(LOG_APP, "客户端接收到信息: %{public}s", buffer);
                   } else if (bytesReceived == 0) {
                       OH_LOG_INFO(LOG_APP, "连接已关闭");
                   } else {
                       OH_LOG_ERROR(LOG_APP, "接收失败: %{public}d", errno);
                   }
               }
           } else if (res == 0) {
               OH_LOG_INFO(LOG_APP, "接收超时");
           } else {
               OH_LOG_ERROR(LOG_APP, "select 失败: %{public}d", errno);
           }

           // 关闭socket
           close(clientSocket);
       });
       th.detach();
       napi_create_double(env, 1, &result);
       return result;
   }

   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           {"connectJoin", nullptr, ConnectJoin, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"connectNotJoin", nullptr, ConnectNotJoin, nullptr, nullptr, nullptr, napi_default, nullptr}};
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END

   static napi_module demoModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "entry",
       .nm_priv = ((void *)0),
       .reserved = {0},
   };

   extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   {
       napi_module_register(&demoModule);
   }
   ```
2. 桥接层：index.d.ts中声明接口。

   ```ts
   // index.d.ts
   export const connectJoin: () => number;
   export const connectNotJoin: () => number;
   ```
3. ArkTS侧：服务端实现。

   ```ts
   // src/main/ets/pages/SCLocalSocket.ets
   import { socket } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   let localSocketServer: socket.TCPSocketServer = socket.constructTCPSocketServerInstance();

   /**
    * 创建本地socket服务端
    * @param listenCallBack 回调是否创建成功及失败原因
    */
   function startListenSocket(listenCallBack: (isSuccess: boolean, error?: string) => void) {

     let listenAddr: socket.NetAddress = {
       address: '127.0.0.1',
       port: 1234,
       family: 1
     };

     localSocketServer.listen(listenAddr).then(() => {
       let tcpExtraOptions: socket.TCPExtraOptions = { keepAlive: true }; // 是否保持连接
       localSocketServer.setExtraOptions(tcpExtraOptions, (error: BusinessError) => {
         if (error != undefined || error != null) {
           console.error(`tcpExtraOptions error：${error.message}`);
           return;
         }
         startListenSocketEvent();
         listenCallBack(true);
       });

     }).catch((err: Object) => {
       listenCallBack(false, 'listen fail: ' + JSON.stringify(err));
     });
   }

   /**
    * 开始监听Socket事件
    */
   function startListenSocketEvent() {

     localSocketServer.getState((err: BusinessError, data: socket.SocketStateBase) => {
       if (err) {
         console.error(`getState fail`);
         return;
       }
       console.info(`监听Socket事件：getState success:${JSON.stringify(data)}`);
     });

     localSocketServer.on("connect", (client: socket.TCPSocketConnection) => {
       console.info(`localSocketServer - connect`);
       client.on('message', (value: socket.SocketMessageInfo) => {
         const uintArray = new Uint8Array(value.message);
         let messageView = '';
         for (let i = 0; i < uintArray.length; i++) {
           messageView += String.fromCharCode(uintArray[i]);
         }
         console.info(`Message total: ${JSON.stringify(value)}`);
         console.info(`Message message information: ${messageView}`);
         sendSocketMessage("I am the information sent from the server. ", client); // 立即回复一条消息
       });

     });
   }

   /**
    * socket发送消息
    * @param msg 消息
    */
   export function sendSocketMessage(msg: string, client: socket.TCPSocketConnection) {
     if (msg.trim().length <= 0) {
       return;
     }
     let msgObj: socket.TCPSendOptions = { data: msg };
     client.send(msgObj);
   }

   /**
    * 开始配置socket
    * @param socketCallBack
    */
   export function startLocalSocket(socketCallBack: (isSuccess: boolean, error?: string) => void) {
     startListenSocket((isSuccess, error) => {
       if (!isSuccess) {
         socketCallBack(isSuccess, error);
         return;
       }
       socketCallBack(isSuccess, error);
     });
   }

   /**
    * 关闭所有本地socket订阅信息
    */
   export function stopLocalSocket() {
     localSocketServer.off("connect");
   }
   ```
4. ArkTS侧：接口调用。

   ```ts
   // src/main/ets/pages/Index.ets
   import testNapi from 'libentry.so';
   import { startLocalSocket, stopLocalSocket } from './SCLocalSocket';

   @Entry
   @Component
   struct Index {

     build() {
       Row() {
         Column() {
           Button('服务端-开启').onClick(() => {
             console.info(`开启Socket服务端`);
             startLocalSocket((isDone, error) => {
               console.error(`开启Socket服务端 = ${isDone ? "ok" : error?.toString()}`);
             });
           }).width('70%').fontSize(30).margin(16);

           Button('NDK客户端连接-阻塞').onClick(() => {
             console.info(`- 调用Native侧客户端接口 阻塞 -`);
             let aa = testNapi.connectJoin();
             console.info(`客户端连接：${aa.toString()}`);
           }).width('70%').fontSize(20).margin(16);

           Button('NDK客户端-非阻塞').onClick(() => {
             console.info(`- 调用Native侧客户端接口 非阻塞 -`);
             let aa = testNapi.connectNotJoin();
             console.info(`客户端连接-非阻塞：${aa.toString()}`);
           }).width('70%').fontSize(20).margin(16);

           Button('服务端-关闭').onClick(() => {
             console.info(`Socket服务端关闭`);
             stopLocalSocket();
           }).width('70%').fontSize(30).margin(16);

         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```
