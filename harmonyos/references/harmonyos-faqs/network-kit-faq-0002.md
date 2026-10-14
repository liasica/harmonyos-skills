---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/network-kit-faq-0002
title: 网络信息获取与状态监听常见问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 常见问题 > 网络信息获取与状态监听常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:21+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:d4eb2a8b1d0f1c38415bfabc95292b52a0a34c531dccab7d8c681e841dc80c6a
---

**Q：如何判断当前网络的IP地址版本是多少？**

**A**：使用[NetAddress](../harmonyos-references/js-apis-net-connection.md#netaddress)类获取当前网络的地址信息，NetAddress类的family属性用于指定IP地址的版本，family属性的值为1表示IPv4，为2表示IPv6 。示例代码如下：

```ts
import { connection } from '@kit.NetworkKit';

@Entry
@Component
struct Index {
  getNetworkFamily() {
    try {
      let netHandle = connection.getDefaultNetSync();
      let connectionProperties = connection.getConnectionPropertiesSync(netHandle);
      if (connectionProperties !== undefined) {
        let linkAddressesArray = connectionProperties.linkAddresses;
        if (linkAddressesArray !== undefined && linkAddressesArray instanceof Array && linkAddressesArray.length > 0) {
          for (let i = 0; i < linkAddressesArray.length; i++) {
            let address: connection.NetAddress = linkAddressesArray[i].address;
            if (address !== undefined) {
              console.info("Succeeded to get address: " + JSON.stringify(address))
              if (address.family === 1) {
                console.info('Current network IP address version is ipv4')
              } else if (address.family === 2) {
                console.info('Current network IP address version is ipv6')
              }
            }
          }
        }
      }
    } catch (e) {
      console.error(`Get exception: ${e}`);
    }
  }

  build() {
    Column({ space: 10 }) {
      Button('获取当前网络IP地址版本')
        .onClick(() => {
          this.getNetworkFamily();
        })
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

**Q：如何解决网络连接状态变化的公共事件返回内容为"NetType":1的问题？**

**A**：返回"NetType":1枚举值表示为NET\_CONN\_STATE\_IDLE网络空闲状态。

如果是监听网络变化，建议使用@ohos.net.connection的能力，请参考[@ohos.net.connection (网络连接管理)](../harmonyos-references/js-apis-net-connection.md)。

代码示例如下：

```ts
import { connection } from '@kit.NetworkKit';
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';

function  listen_network() {
  let netSpecifier: connection.NetSpecifier = {
    netCapabilities: {
      // Assuming the current default network is WiFi, a cellular network connection needs to be created, and the network type can be specified as cellular network
      bearerTypes: [connection.NetBearType.BEARER_CELLULAR, connection.NetBearType.BEARER_WIFI],
    },
  };
  let conn = connection.createNetConnection(netSpecifier);

  conn.register((err: BusinessError, data: void) => {
    console.warn('register Network ' + JSON.stringify(err))
  });

  // Subscription event, network available
  conn.on('netAvailable', ((data: connection.NetHandle) => {
    console.warn('Network available, netId is ' + data.netId);
  }));

  // Subscription event, network available
  conn.on('netCapabilitiesChange', ((data: connection.NetCapabilityInfo) => {
    console.warn('Network netCapabilitiesChange bearerTypes ' + data.netCap.bearerTypes);
    console.warn('Network netCapabilitiesChange networkCap ' + data.netCap.networkCap);
  }));

  // Subscription event, network unavailable
  conn.on('netUnavailable', ((data: void) => {
    console.warn('The network is unavailable, data is ' + JSON.stringify(data));
  }));

  // Subscription event, network disconnection
  conn.on('netLost', ((data: connection.NetHandle) => {
    console.warn('Network lost, netId is ' + data.netId);
  }));
}

// After monitoring an event, it is necessary to obtain the network status through a network interface
function sub_network() {
  console.warn('into sub_network')
  // Public event monitoring code:
  let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
    // Subscription message exception public event
    events: ['usual.event.CONNECTIVITY_CHANGE']
  }

  // Create subscriber callback
  commonEventManager.createSubscriber(subscribeInfo, (err: BusinessError, subscriber: commonEventManager.CommonEventSubscriber) => {
    if (err) {
      console.warn(`Failed to create netWorkSubscribeInfo. Code is ${err.code}, message is ${err.message}`);
      return;
    }
    if (subscribeInfo && subscribeInfo != null) {
      // Subscribe to public event callbacks
      commonEventManager.subscribe(subscriber, (err: BusinessError, data: commonEventManager.CommonEventData) => {
        if (err) {
          console.warn(`Failed to netWorkSubscribe common event. Code is ${err.code}, message is ${err.message}`);
          return;
        }
        console.warn('NET_CONNECTIVITY_CHANGE：' + JSON.stringify(data.parameters));

        setTimeout(async () => {
          connection.getDefaultNet((error, data) => {
            console.log(JSON.stringify(error))
            console.log(JSON.stringify(data))
          }) }, 500);
        // The log printed here is{'NetType':1,'moduleName':''}
      })
    }
  })
}

@Entry
@Component
struct NetWork {
  build() {
    Row() {
      Column() {
        Button('Monitor the network').onClick(() => {
          listen_network()
        })
        Button('Obtain the network status').onClick(() => {
          sub_network()
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**Q：请问设备连接Wi-Fi，或者在蜂窝网下怎样获取本机的IP？**

**A**：场景一，设备连接Wi-Fi后，如何获取当前设备的IP地址？

使用@ohos.wifiManager模块[getIpInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetipinfo)、[getLinkedInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfo)接口获取当前设备的IP地址，其中ipAddress值为number类型，需要转换为IP常用格式，具体请参考[IP格式转换](faqs-connectivity-4.md)。

场景二，设备连接蜂窝网络后，如何获取当前设备的IP地址？

使用@ohos.net.connection模块的[getconnectionproperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)接口获取ConnectionProperties信息，linkAddresses包含链路信息，dnses网络地址包含的IP地址。

注意需要权限ohos.permission.GET\_NETWORK\_INFO。

**Q：connection.getConnectionProperties方法在5.1.5.150下为何无法获取到IPv6的IP地址？**

**A**：目前6.0版本支持fe80，[connection.getconnectionproperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)可以正常获取IPv6地址。
