---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-37
title: 蓝牙传输网络图片
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 蓝牙传输网络图片
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4427a426f04975dc6d2d204ceb25a0a97e7d101f9354ea98487d6e811e2df2ca
---

## 问题现象

如何将网络图片下载，并通过蓝牙传输到对端展示？

## 背景知识

* 使用[蓝牙socket](../harmonyos-references/js-apis-bluetooth-socket.md)建立设备之间连接，将通过[数据请求](../harmonyos-references/js-apis-http.md#httpcreatehttp)下载的网络图片传输到另一台设备。
* [socket.sppWrite](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppwrite)：通过socket向远端发送数据，入参clientSocket由sppAccept或sppConnect接口获取。
* [socket.sppWriteAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppwriteasync18)：通过socket向远端发送数据的异步接口，该接口支持断开连接时SPP操作异常错误返回。

## 解决方案

建立蓝牙socket通道需要通过如下步骤：

1. 服务端和客户端获取蓝牙权限，客户端下载图片需要网络权限。
2. 服务端建立socket并获取id：sppListen。
3. 服务端启动根据id启动对应socket的监听：sppAccept。
4. 客户端根据设备地址发起连接请求：sppConnect。
5. 建立socket通道成功后，获得socket的id。
6. 通过id，使用sppWrite发送数据，使用on('sppRead')监听数据。
7. 将数据转为图片并展示。

**说明** 

运行示例代码请首先将设备配对，并将设备处于蓝牙配对列表的首位。如果要变动图片链接，因为涉及图片转化，需同步更改接收容器的大小与图片本身保持一致。

1. 配置权限列表module.json5。

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
2. 申请权限。

   ```ts
   import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
   import { bundleManager } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   export async function checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

     // 获取应用程序的accessTokenID。
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

     // 校验应用是否被授予权限。
     try {
       grantStatus = await atManager.checkAccessToken(tokenId, permission);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
     }

     return grantStatus;
   }

   export function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): boolean {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let res: boolean = false;
     // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗。
     atManager.requestPermissionsFromUser(context, permissions).then((data) => {
       let grantStatus: Array<number> = data.authResults;
       let length: number = grantStatus.length;
       for (let i = 0; i < length; i++) {
         if (grantStatus[i] === 0) {
           // 用户授权，可以继续访问目标操作。
           res = true;
         } else {
           // 当用户拒绝授权时，系统应提示用户必须授予相应权限才能使用当前页面的功能，并指导用户前往系统设置开启所需权限。
         }
       }
       // 授权成功
     }).catch((err: BusinessError) => {
       console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
     });

     return res;
   }

   export async function checkPermissions(permissions: Permissions, context: common.UIAbilityContext): Promise<void> {
     let grantStatus: boolean =
       await checkPermissionGrant(permissions) === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
     if (grantStatus) {
       return;
     }
     reqPermissionsFromUser([permissions], context);
   }
   ```
3. 服务端需要启动socket并启动监听，将获取的数据进行处理并展示。

   ```ts
   // 服务端启动监听并接收图片
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
     flag: number = 0;
     // 数据接收存储，实际使用过程中替换为真实图片大小
     arr: Uint8Array = new Uint8Array(2114);

     aboutToAppear(): void {
       const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       checkPermissions('ohos.permission.ACCESS_BLUETOOTH', context);
     }

     infoAccept() {
       let acceptClientSocket = (code: BusinessError, number: number) => {
         if (code) {
           console.error(`sppListen error, code is ${code}`);
           return;
         } else {
           this.clientNumber = number; // 获取的clientNumber用作客户端后续读/写操作socket的id。
           console.info(`sppListen success, serverNumber = ${this.clientNumber}`);
           this.dataRead();
         }
       };
       try {
         socket.sppAccept(this.serverNumber, acceptClientSocket); // serverNumber是sppListen回调中得到的serverNumber。
       } catch (err) {
         console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
       }
     }

     dataRead() {
       let dataRead = (dataBuffer: ArrayBuffer) => {
         let data = new Uint8Array(dataBuffer);
         this.arr.set(data, this.flag);
         this.flag += dataBuffer.byteLength;
         if (this.flag > 2113) { // 图片长度为2114
           const imageSource = image.createImageSource(this.arr.buffer);
           this.img = imageSource.createPixelMapSync();
         }
       };
       try {
         socket.on('sppRead', this.clientNumber, dataRead);
       } catch (err) {
         console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
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

             let sppOption: socket.SppOptions = { uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0 };
             try {
               socket.sppListen('server1', sppOption, serverSocket);
             } catch (err) {
               console.error(`errCode: ${(err as BusinessError).code}, errMessage:${(err as BusinessError).message}`);
             }
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
4. 客户端需要下载图片，并将下载的数据通过建立的socket连接传输。

   ```ts
   // 客户端下载并传输图片
   import { http } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { connection, socket } from '@kit.ConnectivityKit';
   import { common } from '@kit.AbilityKit';
   import { checkPermissions } from './RequestPermission';

   @Entry
   @Component
   struct Index {
     clientNumber: number = -1;

     aboutToAppear(): void {
       const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       checkPermissions('ohos.permission.ACCESS_BLUETOOTH', context);
     }

     // 连接蓝牙设备
     connectDevice(deviceId: string, callback: Function) {
       let uuid = '00001810-0000-1000-8000-00805F9B34FB';
       // socket等待客户端连接，连接成功返回clientId
       // 连接对端设备
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
         callback(this.clientNumber + "");
       });
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
             let result: Array<string> = connection.getPairedDevices();
             let deviceId = result[0];
             this.connectDevice(deviceId, (clientSocketID: string) => {
               let clientNumber: number = Number(clientSocketID);
               setTimeout(() => {
                 // 写入数据
                 this.sendImage(clientNumber);
               }, 200);
             });
           })
       }
       .height('100%')
       .width('100%')
     }

     sendImage(clientNumber: number) {
       // 此处地址实际使用过程中替换为真实图片地址
       let imageUrl = 'xx.xx.xx';
       let httpRequest = http.createHttp();
       httpRequest.on("dataReceive", async (imageBuffer: ArrayBuffer) => {
         // 传输数据
         socket.sppWrite(clientNumber, imageBuffer);
       });
       httpRequest.requestInStream(imageUrl, (err: BusinessError<void>) => {
         if (!err) {
           console.info("requestInStream OK!");
         } else {
           console.info(`requestInStream ERROR : err = ${err.code}`);
         }
       });
     }
   }
   ```

## 常见FAQ

Q：为何接收设备的数据是乱码？

A：通过调试方式，检查sppWrite传输的数据和socket.on('sppRead')接收的数据是否是正常数据，是否在传输前后进行转码等操作导致数据变化。

Q：经典蓝牙连接成功以后如何监听对端设备断开连接？

A：可以通过[socket.sppReadAsync](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppreadasync18)读取接口，该接口通过socket读取对端所发送数据的异步接口，该接口支持断开连接时SPP操作异常错误返回。

Q：在进行蓝牙发送大量数据时，调用socket.sppWrite后卡死。

A：接口调用时间过长，可考虑使用系统自带的TaskPool多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞。
