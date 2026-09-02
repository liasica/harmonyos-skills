---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-60
title: 如何解决网络连接状态变化的公共事件返回内容为"NetType":1的问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决网络连接状态变化的公共事件返回内容为"NetType":1的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0fc8d904d4a9922f866209ac821cde0c1b514ef6585ddc368d5705b913c116d6
---

返回"NetType":1枚举值表示为NET\_CONN\_STATE\_IDLE网络空闲状态。

如果是监听网络变化，建议使用@ohos.net.connection的能力，请参考[@ohos.net.connection (网络连接管理)](../harmonyos-references/js-apis-net-connection.md)。

代码示例如下：

```typescript
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
