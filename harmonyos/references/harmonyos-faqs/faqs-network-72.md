---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-72
title: 多种网络同时连接时如何优先使用wifi网络
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 多种网络同时连接时如何优先使用wifi网络
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:276329d5dacf7070da07e95eca3ee03d88e809f18b33888903320cb8e53ff43a
---

**问题现象**

使用video组件加载网络视频，发现使用蓝牙网络时视频加载较慢，而WiFi网络较快，需要优先使用WiFi网络。

**解决措施**

1. 申请权限ohos.permission.INTERNET,ohos.permission.GET\_NETWORK\_INFO。Stage模型中，在module.json5配置文件中声明权限：

   ```json
   {
     "module": {
       // ...
       "requestPermissions":[
         {
           "name": "ohos.permission.INTERNET",
           "reason": "$string:internet_reason",
           "usedScene": {
             "abilities": [
               "EntryAbility"
             ],
             "when": "inuse"
           }
         },
         {
           "name" : "ohos.permission.GET_NETWORK_INFO",
           "reason": "$string:internet_reason",
           "usedScene": {
             "abilities": [
               "EntryAbility"
             ],
             "when":"inuse"
           }
         },
       ]
     }
   }
   ```
2. 编写优先使用wifi网络管理类。

   ```typescript
   // WifiManager.ets
   import { BusinessError } from '@kit.BasicServicesKit';
   import { connection } from '@kit.NetworkKit';

   export class WifiManager {
     private static instance?: WifiManager;

     /**
      * Get singleton
      *
      * @returns Singleton object
      */
     public static getInstance(): WifiManager {
       if (!WifiManager.instance) {
         WifiManager.instance = new WifiManager();
       }
       return WifiManager.instance;
     }

     /**
      * Start listening for network changes (Wi-Fi network / Bluetooth network / cellular data)
      */
     public startListenNetChange(): void {
       console.info("registerNetListener");
       let netConnectionWifi = connection.createNetConnection({
         netCapabilities: {
           bearerTypes: [connection.NetBearType.BEARER_WIFI]
         }
       });
       netConnectionWifi.register((error: BusinessError) => {
         if (error) {
           console.error(`register error: ${error.code}`);
         }
       });
       netConnectionWifi.on('netAvailable', () => {
         console.info("netConnectionWifi netAvailable");
         this.bindWifiWhenConnected();
       });
       netConnectionWifi.on('netLost', () => {
         console.info("Wifi netLost");
         this.bindWifiWhenConnected();
       });
       let netConnectionBluetooth = connection.createNetConnection({
         netCapabilities: {
           bearerTypes: [connection.NetBearType.BEARER_BLUETOOTH]
         }
       });
       netConnectionBluetooth.register((error: BusinessError) => {
         if (error) {
           console.error(`register error: ${error.code}`);
         }
       });
       netConnectionBluetooth.on('netAvailable', () => {
         console.info('netConnectionBluetooth netAvailable');
         this.bindWifiWhenConnected();
       });
       netConnectionBluetooth.on('netLost', () => {
         console.info('Bluetooth netLost');
         this.bindWifiWhenConnected();
       });
       let netConnectionCellular = connection.createNetConnection({
         netCapabilities: {
           bearerTypes: [connection.NetBearType.BEARER_CELLULAR]
         }
       });
       netConnectionCellular.register((error: BusinessError) => {
         if (error) {
           console.error(`register error: ${error.message}`);
         }
       });
       netConnectionCellular.on('netAvailable', () => {
         console.info('netConnectionCellular netAvailable');
         this.bindWifiWhenConnected();
       });
       netConnectionCellular.on('netLost', () => {
         console.info('Cellular netLost');
         this.bindWifiWhenConnected();
       });
     }

     /**
      * Connect the App to the Wi-Fi network asynchronously
      */
     private async bindWifiWhenConnected(): Promise<void> {
       await connection.setAppNet(connection.getDefaultNetSync()).then(() => {
         console.info('setAppNet default success')
       });
       connection.getAllNets().then((data: connection.NetHandle[]) => {
         data.forEach(net => {
           connection.getNetCapabilities(net).then((data: connection.NetCapabilities) => {
             if (data.bearerTypes.length > 0 && data.bearerTypes[0] === connection.NetBearType.BEARER_WIFI) {
               connection.setAppNet(net).then(() => {
                 console.info('setAppNet wifi success');
                 return;
               }).catch((error: Error) => {
                 console.error(`setAppNet wifi failed, error = ${error.message}`);
               })
             }
           }).catch((error: Error) => {
             console.error(`getNetCapabilities error = ${error.message}`);
           });
         })
       }).catch((error: Error) => {
         console.error(`getAllNets error = ${error.message}`);
       });
     }
   }
   ```
3. 获取实例并调用监听方法。

   ```typescript
   import { WifiManager } from './WifiManager'

   // Register for change monitoring
   WifiManager.getInstance().startListenNetChange();
   ```

**参考链接**

[connection.createNetConnection](../harmonyos-references/js-apis-net-connection.md#connectioncreatenetconnection)

[connection.setAppNet](../harmonyos-references/js-apis-net-connection.md#connectionsetappnet9-1)

[connection.getAllNets](../harmonyos-references/js-apis-net-connection.md#connectiongetallnets-1)

[connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities-1)
