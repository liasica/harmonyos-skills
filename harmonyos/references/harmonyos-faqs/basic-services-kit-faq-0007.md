---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/basic-services-kit-faq-0007
title: 蓝牙SPP传输网络图片常见问题
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 常见问题 > 蓝牙SPP传输网络图片常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:19+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:cce99409a3e01ddaf809742640fa98b4da164d2a342f3fdaae0c1269cc48f248
---

**Q：如何将网络图片下载，并通过蓝牙传输到对端展示？**

**A**：@ohos.bluetooth.socket模块支持phone 12+、2in1 13+、tablet 12+、tv 19+、wearable 18+设备。[socket.sppWriteAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppwriteasync18)、[socket.sppReadAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppreadasync18)自API 18起支持，[socket.getMaxTransmitDataSize](../harmonyos-references/js-apis-bluetooth-socket.md#socketgetmaxtransmitdatasize22)自API 22起支持。

建立蓝牙socket通道需要通过如下步骤：

1. 服务端和客户端获取蓝牙权限，客户端下载图片需要网络权限。
2. 服务端建立socket并获取id：[socket.sppListen](../harmonyos-references/js-apis-bluetooth-socket.md#socketspplisten)。
3. 服务端根据id启动对应socket的监听：[socket.sppAccept](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppaccept)。
4. 客户端根据设备地址发起连接请求：[socket.sppConnect](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppconnect)。
5. 建立socket通道成功后，获得socket的id。
6. 通过id，使用[socket.sppWrite](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppwrite)发送数据，使用[socket.on('sppRead')](../harmonyos-references/js-apis-bluetooth-socket.md#socketonsppread)监听数据。
7. 将数据转为图片并展示。

示例代码如下：

注意，运行示例代码请首先将设备配对。示例中getPairedDevices()[0]仅用于演示，实际开发中应遍历配对列表供用户选择目标设备。发送端采用应用层帧定界协议：先发送固定长度头（4字节大端序表示数据总长度），再发送图片载荷。接收端根据头部声明的长度动态扩容并重组，长度齐即解码。

1. 配置权限列表module.json5：

   ```json
   "requestPermissions": [
         {
           "name": "ohos.permission.INTERNET"
         },
         {
           "name": "ohos.permission.ACCESS_BLUETOOTH",
           "reason": "$string:bluetooth_reason",
           "usedScene": {
             "when": "always",
             "abilities": ["EntryAbility"]
           }
         }
       ],
   ```
2. 申请权限：

   ```ts
   import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
   import { bundleManager } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   export async function checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

     let tokenId: number = 0;
     try {
       let bundleInfo: bundleManager.BundleInfo =
         await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
       let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
       tokenId = appInfo.accessTokenId;
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to get bundle info for self, code: ${err.code}, message: ${err.message}`);
     }

     try {
       grantStatus = await atManager.checkAccessToken(tokenId, permission);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
     }

     return grantStatus;
   }

   export async function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): Promise<boolean> {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     try {
       let data = await atManager.requestPermissionsFromUser(context, permissions);
       let grantStatus: Array<number> = data.authResults;
       for (let i = 0; i < grantStatus.length; i++) {
         if (grantStatus[i] !== 0) {
           return false;
         }
       }
       return true;
     } catch (err) {
       const error: BusinessError = err as BusinessError;
       console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
       return false;
     }
   }

   export async function checkPermissions(permissions: Permissions, context: common.UIAbilityContext): Promise<void> {
     let grantStatus: abilityAccessCtrl.GrantStatus = await checkPermissionGrant(permissions);
     if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
       return;
     }
     await reqPermissionsFromUser([permissions], context);
   }
   ```
3. 服务端需要启动socket并启动监听，将获取的数据按帧定界协议重组并展示：

   ```screen
   import { BusinessError } from '@kit.BasicServicesKit';
   import { socket } from '@kit.ConnectivityKit';
   import image from '@ohos.multimedia.image';
   import { common } from '@kit.AbilityKit';
   import { checkPermissions } from './RequestPermission';

   @Entry
   @Component
   struct ServerPage {
     @State img: PixelMap | undefined = undefined;
     serverNumber: number = -1;
     clientNumber: number = -1;
     // 帧定界协议相关状态
     headerReceived: boolean = false;
     dataLength: number = 0;
     receiveBuffer: Uint8Array = new Uint8Array(0);

     aboutToAppear(): void {
       const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       checkPermissions('ohos.permission.ACCESS_BLUETOOTH', context);
     }

     infoAccept() {
       let acceptClientSocket = (code: BusinessError, number: number) => {
         if (code) {
           console.error(`sppAccept error, code is ${code}`);
           return;
         } else {
           this.clientNumber = number;
           console.info(`sppAccept success, clientNumber = ${this.clientNumber}`);
           this.dataRead();
         }
       };
       try {
         socket.sppAccept(this.serverNumber, acceptClientSocket);
       } catch (err) {
         console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
       }
     }

     dataRead() {
       let dataRead = (dataBuffer: ArrayBuffer) => {
         let data = new Uint8Array(dataBuffer);
         // 拼接新数据到接收缓冲区
         let newBuffer = new Uint8Array(this.receiveBuffer.length + data.length);
         newBuffer.set(this.receiveBuffer);
         newBuffer.set(data, this.receiveBuffer.length);
         this.receiveBuffer = newBuffer;

         // 解析帧头（4字节大端序长度）
         if (!this.headerReceived && this.receiveBuffer.length >= 4) {
           this.dataLength = (this.receiveBuffer[0] << 24) | (this.receiveBuffer[1] << 16) |
             (this.receiveBuffer[2] << 8) | this.receiveBuffer[3];
           this.headerReceived = true;
         }

         // 判断数据是否接收完整
         if (this.headerReceived && this.receiveBuffer.length >= 4 + this.dataLength) {
           let imageData = this.receiveBuffer.slice(4, 4 + this.dataLength);
           const imageSource = image.createImageSource(imageData.buffer);
           this.img = imageSource.createPixelMapSync();
         }
       };
       try {
         socket.on('sppRead', this.clientNumber, dataRead);
       } catch (err) {
         console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
       }
     }

     // 断开连接与资源释放
     releaseResources() {
       try {
         socket.off('sppRead', this.clientNumber);
       } catch (err) {
         console.error(`off sppRead error: ${(err as BusinessError).message}`);
       }
       try {
         socket.sppCloseClientSocket(this.clientNumber);
       } catch (err) {
         console.error(`sppCloseClientSocket error: ${(err as BusinessError).message}`);
       }
       try {
         socket.sppCloseServerSocket(this.serverNumber);
       } catch (err) {
         console.error(`sppCloseServerSocket error: ${(err as BusinessError).message}`);
       }
     }

     build() {
       Column() {
         Button('启动监听')
           .onClick(async () => {
             let serverSocket = (code: BusinessError, number: number) => {
               if (code) {
                 console.error(`sppListen error, code is ${code}`);
                 return;
               } else {
                 this.serverNumber = number;
                 console.info(`sppListen success, serverNumber = ${this.serverNumber}`);
                 this.infoAccept();
               }
             };

             // 使用标准Serial Port UUID，两端必须一致
             let sppOption: socket.SppOptions = { uuid: '00001101-0000-1000-8000-00805F9B34FB', secure: false, type: 0 };
             try {
               socket.sppListen('server1', sppOption, serverSocket);
             } catch (err) {
               console.error(`errCode: ${(err as BusinessError).code}, errMessage:${(err as BusinessError).message}`);
             }
           })
         Button('断开连接')
           .onClick(() => {
             this.releaseResources();
           })
         Image(this.img)
           .width(100)
           .height(100)
       }
       .justifyContent(FlexAlign.SpaceAround)
       .height('100%')
       .width('100%')
     }
   }
   ```
4. 客户端需要下载图片，并将下载的数据通过建立的socket连接传输：

   ```ts
   import { http } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { connection, socket } from '@kit.ConnectivityKit';
   import { common } from '@kit.AbilityKit';
   import { checkPermissions } from './RequestPermission';

   @Entry
   @Component
   struct Index {
     clientNumber: number = -1;
     httpRequest: http.HttpRequest | null = null;

     aboutToAppear(): void {
       const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       checkPermissions('ohos.permission.ACCESS_BLUETOOTH', context);
     }

     connectDevice(deviceId: string, callback: Function) {
       // 使用标准Serial Port UUID，两端必须一致
       let uuid = '00001101-0000-1000-8000-00805F9B34FB';
       socket.sppConnect(deviceId, {
         uuid: uuid,
         secure: false,
         type: 0
       }, (err: BusinessError, clientSocketID: number) => {
         if (err != null) {
           console.error(`sppConnect error, code = ${err.code}`);
           return;
         }
         this.clientNumber = clientSocketID;
         callback(this.clientNumber);
       });
     }

     // 断开连接与资源释放
     releaseResources() {
       if (this.httpRequest) {
         this.httpRequest.off('dataReceive');
         this.httpRequest.destroy();
         this.httpRequest = null;
       }
       try {
         socket.sppCloseClientSocket(this.clientNumber);
       } catch (err) {
         console.error(`sppCloseClientSocket error: ${(err as BusinessError).message}`);
       }
     }

     build() {
       RelativeContainer() {
         Button("下载并传递图片")
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             // 仅演示用，实际开发中应遍历配对列表供用户选择目标设备
             let result: Array<string> = connection.getPairedDevices();
             let deviceId = result[0];
             this.connectDevice(deviceId, (clientSocketID: number) => {
               // 注意：此处直接开始发送数据，假设接收端已完成sppRead订阅。
               // 生产环境中建议使用应用层握手（接收端订阅完成后回一个ready帧，发送端收到再发数据），
               // 避免接收端尚未订阅即开始接收数据导致丢包。
               this.sendImage(clientSocketID);
             });
           })
         Button("断开连接")
           .onClick(() => {
             this.releaseResources();
           })
       }
       .height('100%')
       .width('100%')
     }

     sendImage(clientNumber: number) {
       let imageUrl = 'https://www.example.com/image.png';
       this.httpRequest = http.createHttp();
       let totalData: Uint8Array = new Uint8Array(0);

       this.httpRequest.on("dataReceive", (imageBuffer: ArrayBuffer) => {
         // 累积下载的数据
         let newData = new Uint8Array(imageBuffer);
         let combined = new Uint8Array(totalData.length + newData.length);
         combined.set(totalData);
         combined.set(newData, totalData.length);
         totalData = combined;
       });

       this.httpRequest.requestInStream(imageUrl, (err: BusinessError<void>) => {
         if (err) {
           console.info(`requestInStream ERROR : err = ${err.code}`);
           return;
         }
         console.info("requestInStream OK!");
         // 下载完成后，先发送4字节大端序长度头，再发送图片数据
         let header = new Uint8Array(4);
         header[0] = (totalData.length >>> 24) & 0xFF;
         header[1] = (totalData.length >>> 16) & 0xFF;
         header[2] = (totalData.length >>> 8) & 0xFF;
         header[3] = totalData.length & 0xFF;
         let fullData = new Uint8Array(4 + totalData.length);
         fullData.set(header);
         fullData.set(totalData, 4);
         socket.sppWrite(clientNumber, fullData.buffer);
       });
     }
   }
   ```
5. 断开与资源释放：使用完成后，需要先取消读取数据的订阅，再断开连接。服务端还需调用[socket.sppCloseServerSocket](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppcloseserversocket)删除已注册的UUID服务，否则客户端再次发起连接会连接失败。客户端需调用[socket.sppCloseClientSocket](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppcloseclientsocket)关闭套接字。若使用了http请求，需调用httpRequest.destroy()销毁请求并调用off('dataReceive')取消订阅。

**Q：为何接收设备的数据是乱码？**

**A**：当链路类型为SPP\_RFCOMM时，[socket.on('sppRead')](../harmonyos-references/js-apis-bluetooth-socket.md#socketonsppread)每次接收数据大小范围为[1, 1024]字节，接收数据超过1024字节时会自动分多次回调。若接收端按单次回调即解码展示，会导致数据不完整或乱码。正确做法是：接收端按分片累积重组完整数据后再解码。sppRead回调给出的是二进制ArrayBuffer，不可按字符串处理。本知识示例中传输的图片数据会被拆成多次回调，服务端代码已采用帧定界协议按头部声明的长度动态重组。

**Q：经典蓝牙连接成功以后如何监听对端设备断开连接？**

**A**：可以通过[socket.sppReadAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppreadasync18)循环读取数据，当蓝牙SPP断开连接时，该接口会返回2901054错误码，据此可判定对端已断开。

**Q：在进行蓝牙发送大量数据时，调用socket.sppWrite后卡死。**

**A**：优先使用[socket.sppWriteAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppwriteasync18)异步发送接口，避免阻塞主线程。发送大量数据时，可调用[socket.getMaxTransmitDataSize](../harmonyos-references/js-apis-bluetooth-socket.md#socketgetmaxtransmitdatasize22)获取当前链路最大发送数据大小，按该值对数据进行分片发送。如需并发处理，可使用系统TaskPool多线程能力将耗时任务交由子线程执行，但需注意@Concurrent函数不得使用闭包、ArrayBuffer默认转移等约束，蓝牙socket在工作线程中的可用性需自行验证。

**Q：蓝牙数据通道长时间无数据交互后，再次发送数据出现延迟。**

**A**：蓝牙子系统实现上，通道在5-7s内没有数据交互时会进入休眠模式，下次调用发送数据接口前会耗费500ms左右退出休眠模式才开始发送数据。建议每3s左右往数据通道上发送一次心跳数据保活，代价为功耗上升。
