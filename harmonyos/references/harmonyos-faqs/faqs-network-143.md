---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-143
title: 如何指定使用蜂窝网络或wifi网络发送http请求
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何指定使用蜂窝网络或wifi网络发送http请求
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:921bab74ca56c3814165bb7497ae33b7f628da1d666d2f91af9a2c90bd572d60
---

## 问题现象

wifi和蜂窝均开启的情况下，如何指定使用蜂窝网络发送请求？

## 背景知识

[@ohos.net.connection](../harmonyos-references/js-apis-net-connection.md)是HarmonyOS操作系统中用于管理网络连接的一个模块，它提供了多种功能来管理设备的网络连接，以下是这个kit的主要功能和使用方法：

* 创建网络连接：使用createNetConnection方法创建一个新的网络连接。这个方法允许指定网络特征（如网络类型）和超时时间。例如：关注默认网络可以调用connection.createNetConnection()；关注特定网络（蜂窝网络）可以指定网络特征：

  ```ts
  let netConnectionCellular = connection.createNetConnection({
      netCapabilities: {
          bearerTypes: [connection.NetBearType.BEARER_CELLULAR]
      }
  });
  ```
* 获取默认网络：申请ohos.permission.GET\_NETWORK\_INFO权限，使用getDefaultNet方法异步获取当前默认激活的数据网络并使用回调函数接收结果。

## 解决方案

1. 使用createNetConnection方法设置NetBearType监听蜂窝网络类型：

   ```ts
   let netConnectionWifi = connection.createNetConnection({
     netCapabilities: {
       bearerTypes: [connection.NetBearType.BEARER_WIFI]
     }
   });
   ```
2. 调用返回netConnectionCellular参数结果中携带register方法拉起蜂窝网状态：

   ```ts
   netConnectionWifi.register((error: BusinessError) => {
     if (error) {
       console.error(`register error: ${error.code}`);
     }
   });
   ```
3. 使用connection.setAppNet()将应用绑定到指定的网络上后，该应用的所有网络请求都会使用该网络。如若需要使用其他网络，则需要再次通过connection.setAppNet()将应用绑定到其他网络上。

   ```ts
   connection.getAllNets().then((data: connection.NetHandle[]) => {
     data.forEach(net => {
       connection.getNetCapabilities(net).then((data: connection.NetCapabilities) => {
         if (data.bearerTypes.length > 0 && data.bearerTypes[0] === connection.NetBearType.BEARER_WIFI) {
           connection.setAppNet(net).then(() => {
             console.info('setAppNet wifi success');
             return;
           }).catch((error: Error) => {
             console.error(`setAppNet wifi failed, error = ${error.message}`);
           });
         }
       }).catch((error: Error) => {
         console.error(`getNetCapabilities error = ${error.message}`);
       });
     });
   }).catch((error: Error) => {
     console.error(`getAllNets error = ${error.message}`);
   });
   ```

完整示例参考如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { connection } from '@kit.NetworkKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('设置应用网络为Wifi').onClick(() => {
        WifiManager.getInstance().startListenNetChange(true);
      })
      Button('设置应用网络为数据流量').onClick(() => {
        WifiManager.getInstance().startListenNetChange(false);
      })
    }
  }
}

class WifiManager {
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

  public startListenNetChange(isWifi: boolean): void {
    console.info('registerNetListener');
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
      console.info('netConnectionWifi netAvailable');
      if (isWifi) {
        this.bindWifiWhenConnected();
      } else {
        this.bindCellularWhenConnected();
      }
    });
    netConnectionWifi.on('netLost', () => {
      console.info('Wifi netLost');
      if (isWifi) {
        this.bindWifiWhenConnected();
      } else {
        this.bindCellularWhenConnected();
      }
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
      if (isWifi) {
        this.bindWifiWhenConnected();
      } else {
        this.bindCellularWhenConnected();
      }
    });
    netConnectionCellular.on('netLost', () => {
      console.info('Cellular netLost');
      if (isWifi) {
        this.bindWifiWhenConnected();
      } else {
        this.bindCellularWhenConnected();
      }
    });
  }

  private async bindWifiWhenConnected(): Promise<void> {
    await connection.setAppNet(connection.getDefaultNetSync()).then(() => {
      console.info('setAppNet default success');
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
            });
          }
        }).catch((error: Error) => {
          console.error(`getNetCapabilities error = ${error.message}`);
        });
      });
    }).catch((error: Error) => {
      console.error(`getAllNets error = ${error.message}`);
    });
  }

  private async bindCellularWhenConnected(): Promise<void> {
    await connection.setAppNet(connection.getDefaultNetSync()).then(() => {
      console.info('setAppNet default success');
    });
    connection.getAllNets().then((data: connection.NetHandle[]) => {
      data.forEach(net => {
        connection.getNetCapabilities(net).then((data: connection.NetCapabilities) => {
          if (data.bearerTypes.length > 0 && data.bearerTypes[0] === connection.NetBearType.BEARER_CELLULAR) {
            connection.setAppNet(net).then(() => {
              console.info('setAppNet cellular success');
              return;
            }).catch((error: Error) => {
              console.error(`setAppNet cellular failed, error = ${error.message}`);
            });
          }
        }).catch((error: Error) => {
          console.error(`getNetCapabilities error = ${error.message}`);
        });
      });
    }).catch((error: Error) => {
      console.error(`getAllNets error = ${error.message}`);
    });
  }
}
```

## 常见FAQ

Q：使用connection.getAllNetsSync获取当前所有的网络句柄，但发现只能获取当前使用的网络句柄。比如wifi和4G都是可用的，但只能获取到wifi的NetHandle。

A：拉起蜂窝需要时间，register之后，立刻调用getAllNetsSync是不会有蜂窝句柄的。

Q：如何获取蜂窝网络的ip地址？

A：使用@ohos.net.connection模块的[getconnectionproperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)接口获取ConnectionProperties信息，linkAddresses包含链路信息，dnses网络地址包含机ip地址。

Q：http请求报错2300006如何解决？

A：错误码2300006表示域名无法解析，在无网络连接的情况下会报该错误，需要检查请求的URL编写是否正确和网络是否通畅。
