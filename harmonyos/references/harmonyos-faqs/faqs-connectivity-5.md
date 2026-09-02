---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-5
title: 如何获取网络类型：Wi-Fi，3G，4G等
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何获取网络类型：Wi-Fi，3G，4G等
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e993ec46bb75e30b494d6df3df5beb4b67011ea53063f099b803089bcf8ddc1d
---

先通过[getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)去获取网络的类型，判断默认网络是Wi-Fi还是蜂窝。

如果是Wi-Fi，则直接确认网络类型是Wi-Fi。如果是在蜂窝连接情况下，可以调用[radio.getSignalInformation](../harmonyos-references/js-apis-radio.md#radiogetsignalinformation7)获取指定SIM卡槽对应的注册网络信号强度信息列表，返回[SignalInformation](../harmonyos-references/js-apis-radio.md#signalinformation)对象的数组，其中，返回的signalType代表[网络类型NetworkType](../harmonyos-references/js-apis-radio.md#networktype)，signalType的值对应网络类型如下：

* GSM：2G
* CDMA：2G
* WCDMA：3G
* TDSCDMA：3G
* LTE：4G

具体可参考如下示例代码：

```typescript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { radio } from '@kit.TelephonyKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('获取网络类型')
        .type(ButtonType.Normal)
        .width(200)
        .height(200)
        .onClick(() => {
          connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
            if (netHandle.netId == 0) {
              // When there is currently no connected network, the obtained netHandler's netid is 0, which belongs to an abnormal scenario.
              // Here, some processing mechanisms can be added according to the actual situation.
              return;
            }
            // Obtain the capability information of the network corresponding to netHandle
            connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
              if (error) {
                console.error(`Failed to get net capabilities. Code:${error.code}, message:${error.message}`);
                return;
              }
              console.info("Succeeded to get data: " + JSON.stringify(data));
              if (data.bearerTypes[0] == 1) {
                // console.info("Wi Fi network");
              } else if (data.bearerTypes[0] == 0) {
                // console.info("Cellular Network");
                let slotId: number = 0; // Slot ID, -0: Slot 1, -1: Slot 2
                radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
                  if (err) {
                    console.error(`getSignalInformation failed, callback: err->${JSON.stringify(err)}`);
                    return;
                  }
                  console.info(`getSignalInformation success, callback: data->${JSON.stringify(data)}`);
                  // Return an array of SignalInformation objects, where the returned signalType represents the network type NetworkType
                });
              }
            })
          }).catch((error: BusinessError) => {
            console.error('error: ' + JSON.stringify(error));
          });
        })
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```
