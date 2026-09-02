---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-129
title: 如何实现一键检测网络情况功能
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何实现一键检测网络情况功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:7f795a4fd3190a16c2ccf4ea28472b49299d6abce19aefd3d34493fbf100660d
---

## 问题现象

希望能够提供一键检测网络情况功能的文档或者思路。

## 背景知识

* 校验应用是否授予网络权限：[checkAccessToken](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)。
* [connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities-1)方法获取对应网络的能力信息。
* 通过[connection.getAddressesByName](../harmonyos-references/js-apis-net-connection.md#connectiongetaddressesbyname)方法使用对应网络解析主机名以获取所有IP地址。
* 通过[ChannelBinding](../harmonyos-references/onlineauthentication-fido-api.md#channelbinding)结构体中的serverEndPoint字段判断服务器通道状态。

## 解决方案

实现一键检测网络情况功能可以从以下几个方面参考：

1. 权限说明：
   * 使用[connection.getDefaultNet](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnet)接口，应用需要在“src/main/module.json5”的requestPermissions层级中添加允许应用获取数据网络信息权限[ohos.permission.GET\_NETWORK\_INFO](../harmonyos-guides/permissions-for-all.md#ohospermissionget_network_info)。
   * 检测APP网络权限：应用需要在“src/main/module.json5”的requestPermissions层级中添加网络权限[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，确保APP网络权限正常。
2. 检测网络类型：可以通过getNetCapabilities方法获取当前网络的类型，判断默认网络是Wi-Fi还是蜂窝：

   如果是Wi-Fi，则直接确认网络类型是Wi-Fi。如果是在蜂窝连接情况下，可以调用[radio.getSignalInformation](../harmonyos-references/js-apis-radio.md#radiogetsignalinformation7)获取指定SIM卡槽对应的注册网络信号强度信息列表，返回[SignalInformation](../harmonyos-references/js-apis-radio.md#signalinformation)对象的数组，其中，返回的signalType代表网络类型[NetworkType](../harmonyos-references/js-apis-radio.md#networktype)，signalType的值对应网络类型如下：GSM（2G）、CDMA（2G）、WCDMA（3G）、TDSCDMA（3G）、LTE（4G）、 NR（5G）。

参考示例如下：

```ts
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { radio } from '@kit.TelephonyKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('获取网络类型')
        .onClick(() => {
          connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
            if (netHandle.netId === 0) {
              return;
            }
            connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
              if (error) {
                console.error(`Failed to get net capabilities. Code:${error.code}, message:${error.message}`);
                return;
              }
              console.info(`Succeeded to get data: data->${JSON.stringify(data)}`);
              if (data.bearerTypes[0] === 1) {
              } else if (data.bearerTypes[0] === 0) {
                let slotId: number = 0;
                radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
                  if (err) {
                    console.error(`getSignalInformation failed, callback: err->${JSON.stringify(err)}`);
                    return;
                  }
                  console.info(`getSignalInformation success, callback: data->${JSON.stringify(data)}`);
                });
              }
            });
          }).catch((error: BusinessError) => {
            console.error(`error: ${JSON.stringify(error)}`);
          });
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```

* 获取公网IP：可以使用[connection.getAddressesByName](../harmonyos-references/js-apis-net-connection.md#connectiongetaddressesbyname)方法来获取公网IP地址，此方法可以解析指定网络的主机名以获取所有IP地址。
* 服务器通道状态：可以通过[ChannelBinding](../harmonyos-references/onlineauthentication-fido-api.md#channelbinding)结构体中的serverEndPoint字段判断，在进行FIDO身份认证时，需要设置serverEndPoint字段。该字段的值是TLS服务器证书的base64url编码哈希值。通过检查serverEndPoint字段是否已成功设置，可以判断服务器通道是否正常。如果该字段为空或设置为null，则表示服务器通道未正确配置或不可用。

## 常见FAQ

Q：在连接到蜂窝网络的时候，获取到的NetCapabilities中linkUpBandwidthKbps和linkDownBandwidthKbps是有值的，但是在连接Wi-Fi或者其他个人热点的时候，上述的linkUpBandwidthKbps、linkDownBandwidthKbps、ConnectionProperties都是0。

A：连接Wi-Fi或者其他个人热点的时候linkUpBandwidthKbps，linkDownBandwidthKbps，ConnectionProperties返回0是正常的，表示无法评估当前网络。

Q：如何判断当前是否有网络？

A：[connection.hasDefaultNetSync](../harmonyos-references/js-apis-net-connection.md#connectionhasdefaultnetsync10)可判断默认网络是否被激活，true表示被激活，false表示没有被激活。

Q：如何获取当前连接的Wi-Fi网速？

A：[wifiManager.getLinkedInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfo)可以获取Wi-Fi连接的相关信息，包含上行速度、下行速度。

Q：如何在手机端通过软件设置手机本身的丢包？

A：[网络领航员](../harmonyos-guides/network-navigator.md)可以进行网络模拟，通过自定义上下行丢包率、上下行延迟等模拟弱网环境。
