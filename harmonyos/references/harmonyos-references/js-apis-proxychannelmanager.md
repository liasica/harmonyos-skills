---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-proxychannelmanager
title: "@ohos.distributedsched.proxyChannelManager (代理通道管理)"
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > ArkTS API > @ohos.distributedsched.proxyChannelManager (代理通道管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eb21862b07baedfd84ac693e15044c16c46d9a608ceb249683cb5a425abcb9d4
---

软总线具备常驻运行能力，可为跨设备通信提供稳定可靠的底层通道。本模块基于软总线进程开发，支持手机与穿戴设备间的数据互通，可为用户提供无缝的设备互联体验，同时降低开发者跨设备通信的实现复杂度，无需自行处理底层通信协议和进程唤醒逻辑。使用场景：手机侧应用与穿戴设备侧应用协同时，当手机侧应用不在前台时，手机侧应用的下行消息经由通知服务器，通过代理模块发送给穿戴设备侧；当穿戴设备向手机发送数据时，代理模块可动态唤醒手机侧对应应用进程以接收和处理数据。模块核心功能包括：代理通道管理、数据路由管理、应用状态感知和唤醒、全链路状态监控。

* 代理通道管理：通过蓝牙 BR 协议建立手机与穿戴设备的双向数据通道，确保跨设备间可靠的双向数据通信，无需开发者自行实现底层通信协议。支持的数据通道ID范围是1~2147483647。
* 数据路由管理：基于 UUID 服务识别机制转发穿戴设备侧应用数据，实现数据的精准路由至目标服务端口，避免数据丢失或错发。UUID用于唯一标识对端设备上监听的服务，代理模块根据对端设备的UUID将数据路由至对应服务端口。
* 应用状态感知和唤醒：代理通道使能并收到穿戴设备侧应用数据后，代理模块根据module.json5中配置的action字段（如'action.ohos.pull.listener'）识别目标应用，并代理拉起对应手机侧应用进程以处理数据，无需应用常驻前台即可接收数据，节省系统资源。
* 全链路状态监控：通过回调实时感知代理通道全生命周期的连接状态变化，帮助手机侧应用及时响应连接异常并调整业务策略，提升数据传输可靠性。包括连接恢复、异常断连、配对关系删除等事件。

**说明** 

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**模型约束**：此接口仅可在Stage模型下使用。

## 导入模块

```js
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## 使用说明

调用模块接口前，需要完成如下配置：

1. 申请ohos.permission.ACCESS\_BLUETOOTH权限。如何配置和申请权限，具体操作请参考[声明权限](../harmonyos-guides/declare-permissions.md)和[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。
2. 在module.json5文件中配置action字段"action.ohos.pull.listener"，用于需要被代理拉起的手机侧应用进程。

典型调用流程：

1. 调用openProxyChannel打开代理通道，获取channelId。
2. 调用sendData发送数据，并根据业务需求订阅事件：调用on('receiveData')接收对端数据，调用on('channelStateChange')感知通道连接状态变化（断连、恢复等）。两者可同时订阅，建议在数据传输场景中同时使用，以便通道异常时及时暂停发送并处理断连恢复逻辑。
3. 使用完毕后，调用off('receiveData')/off('channelStateChange')取消订阅。
4. 调用closeProxyChannel关闭代理通道释放资源。

## proxyChannelManager.openProxyChannel

openProxyChannel(channelInfo: ChannelInfo): Promise<number>

打开代理通道，使用Promise异步回调。基于ChannelInfo中配置的链路类型和对端设备信息，通过蓝牙BR协议与对端设备协商建立双向数据通道，并返回唯一标识该通道的channelId。适用于手机侧应用需要与穿戴设备侧应用建立双向数据通道的场景，例如消息通知转发等。调用此方法后，必须在不再使用代理通道时调用[closeProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanagercloseproxychannel)关闭通道以释放资源。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**设备行为差异**：该接口在Phone/Tablet设备中可正常调用，其他支持分布式业务的设备中会返回错误码32390101，不支持分布式业务的Wearable设备中会返回错误码801。

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelInfo | [ChannelInfo](js-apis-proxychannelmanager.md#channelinfo) | 是 | 代理通道的链路类型及对端设备的MAC地址和对端监听服务的UUID信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 打开代理通道成功时resolve，返回代理通道的channelId，取值范围为1~2147483647，channelId的生命周期和代理通道生命周期相同，不关闭代理时，传入相同入参将返回相同channelId；失败时reject返回错误信息，错误码详见错误码表。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](errorcode-proxychannelmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported because bluetooth proxy function has been trimmed.  适用版本：26.0.0+ |
| 32390001 | BR is disabled. |
| 32390002 | Device not paired. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |
| 32390102 | Operation failed or Connection timed out. |

**示例：**

```ts
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          let channelInfo: proxyChannelManager.ChannelInfo = {
            linkType: proxyChannelManager.LinkType.LINK_BR,
            peerDevAddr: 'xx:xx:xx:xx:xx:xx', // 穿戴设备蓝牙MAC
            peerUuid: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', // 穿戴侧监听的UUID
          };
          // 以下为使用 try/catch 判断
          try {
            proxyChannelManager.openProxyChannel(channelInfo)
              .then((channelId: number) => {
                // 获得通道ID
              })
              .catch((error: BusinessError) => {
                console.error(`Failed to open proxy channel. Code: ${error.code}, message: ${error.message}`);
              });
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to open proxy channel. Code: ${error.code}, message: ${error.message}`);
            // 如果返回的error.code为undefined且error.message为"Cannot read property openProxyChannel of undefined"，则当前镜像不支持该API
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## proxyChannelManager.closeProxyChannel

closeProxyChannel(channelId: number): void

关闭已打开的代理通道。适用于手机侧应用不再需要与穿戴设备侧应用通信的场景，例如完成数据同步任务后主动释放通道资源等。此方法必须与[openProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanageropenproxychannel)配对使用，在使用完毕后调用此方法关闭通道以释放资源。关闭通道后，已注册的receiveData和channelStateChange回调将自动取消订阅，正在传输的数据将中断。未及时关闭代理通道可能导致通道资源泄漏。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**设备行为差异**：该接口在Phone/Tablet设备中可正常调用，其他支持分布式业务的设备中会返回错误码32390006，不支持分布式业务的Wearable设备中会返回错误码801。

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelId | number | 是 | 打开代理通道时获取的channelId，取值范围为1~2147483647。使用无效或已关闭的channelId将返回错误码32390004，超出取值范围时返回错误码32390006。channelId仅在代理通道可用时生效，通道关闭或断连后将不可用。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](errorcode-proxychannelmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported because bluetooth proxy function has been trimmed.  适用版本：26.0.0+ |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ts
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          // 以下为使用 try/catch 判断
          try {
            proxyChannelManager.closeProxyChannel(channelId); // channelId通过openProxyChannel接口的Promise返回值获取
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to close proxy channel. Code: ${error.code}, message: ${error.message}`);
            // 如果返回的error.code为undefined且error.message为"Cannot read property closeProxyChannel of undefined"，则当前镜像不支持该API
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## proxyChannelManager.sendData

sendData(channelId: number, data: ArrayBuffer): Promise<void>

向对端发送数据，使用Promise异步回调。适用于手机侧应用通过代理通道向穿戴设备侧应用发送指令或数据的场景，例如发送配置更新、通知消息等。必须在[openProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanageropenproxychannel)成功打开代理通道后才能调用此方法发送数据。当代理通道处于不可用状态（如[ChannelState](js-apis-proxychannelmanager.md#channelstate).CHANNEL\_WAIT\_RESUME、CHANNEL\_EXCEPTION\_SOFTWARE\_FAILED、CHANNEL\_BR\_NO\_PAIRED）时，调用此方法将失败，建议订阅[on('channelStateChange')](js-apis-proxychannelmanager.md#proxychannelmanageronchannelstatechange)事件监测通道状态，在通道不可用时暂停数据发送，通道恢复后继续发送。数据通过已建立的代理通道经蓝牙BR链路传输至对端设备，数据长度最大为4096字节，超出将返回错误码32390103。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**设备行为差异**：该接口在Phone/Tablet设备中可正常调用，其他支持分布式业务的设备中会返回错误码32390006，不支持分布式业务的Wearable设备中会返回错误码801。

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelId | number | 是 | 打开代理通道时获取的channelId，取值范围为1~2147483647。使用无效或已关闭的channelId将返回错误码32390004，超出取值范围时返回错误码32390006。channelId仅在代理通道可用时生效，通道关闭或断连后将不可用。 |
| data | ArrayBuffer | 是 | 向对端发送的二进制数据，数据格式由应用层自定义，最大长度为4096字节。超出长度限制时返回错误码32390103。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回值的Promise对象。数据发送成功时resolve，发送失败时reject并返回错误信息。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](errorcode-proxychannelmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported because bluetooth proxy function has been trimmed.  适用版本：26.0.0+ |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |
| 32390103 | Data too long. |
| 32390104 | Send failed. |

**示例：**

```ts
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          const data = new ArrayBuffer(10); // 创建一个长度为 10 的 ArrayBuffer
          try {
            proxyChannelManager.sendData(channelId, data) // channelId通过openProxyChannel接口的Promise返回值获取
              .then(() => {
              })
              .catch((error: BusinessError) => {
                console.error(`Failed to send data. Code: ${error.code}, message: ${error.message}`);
              });
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to send data. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## proxyChannelManager.on('receiveData')

on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void

订阅数据接收事件，使用Callback异步回调。适用于手机侧应用需要持续接收穿戴设备侧应用上报数据的场景，例如接收穿戴设备侧应用数据等。代理模块基于openProxyChannel时配置的对端UUID接收对端数据，将接收到的穿戴设备侧应用数据通过回调传递给订阅者。必须在[openProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanageropenproxychannel)成功打开代理通道后才能订阅数据接收事件。若需代理唤醒手机侧应用进程以接收和处理对端数据，使用前请在module.json5中配置action字段"action.ohos.pull.listener"。订阅后需调用[off('receiveData')](js-apis-proxychannelmanager.md#proxychannelmanageroffreceivedata)取消订阅，避免回调持续触发。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**设备行为差异**：该接口在Phone/Tablet设备中可正常调用，其他支持分布式业务的设备中会返回错误码32390004，不支持分布式业务的Wearable设备不返回错误码，不抛异常。

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型，固定取值为'receiveData'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId，取值范围为1~2147483647。使用无效或已关闭的channelId将返回错误码32390004，超出取值范围时返回错误码32390006。channelId仅在代理通道可用时生效，通道关闭或断连后将不可用。 |
| callback | Callback<[DataInfo](js-apis-proxychannelmanager.md#datainfo)> | 是 | 回调函数，用于接收代理通道的数据。回调参数为[DataInfo](js-apis-proxychannelmanager.md#datainfo)对象，包含channelId（通道ID）和data（接收到的字节数据）。需先通过openProxyChannel打开代理通道后才能接收数据。多次注册时，仅最后一次注册的生效。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](errorcode-proxychannelmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ts
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          const receiveDataCallback = (dataInfo: proxyChannelManager.DataInfo) => {
          };
          try {
            proxyChannelManager.on('receiveData', channelId, receiveDataCallback); // channelId通过openProxyChannel接口的Promise返回值获取
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to register receiveData callback. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## proxyChannelManager.off('receiveData')

off(type: 'receiveData', channelId: number, callback?: Callback<DataInfo>): void

取消订阅数据接收事件，不再通过回调接收数据。适用于手机侧应用不再需要接收穿戴设备侧应用数据的场景，例如用户切换到其他功能模块等。必须在[openProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanageropenproxychannel)成功打开代理通道后才能取消订阅。此方法必须与[on('receiveData')](js-apis-proxychannelmanager.md#proxychannelmanageronreceivedata)配对使用，用于取消之前通过on('receiveData')注册的数据接收回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**设备行为差异**：该接口在Phone/Tablet设备中可正常调用，其他支持分布式业务的设备中会返回错误码32390004，不支持分布式业务的Wearable设备不返回错误码，不抛异常。

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型，固定取值为'receiveData'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId，取值范围为1~2147483647。使用无效或已关闭的channelId将返回错误码32390004，超出取值范围时返回错误码32390006。channelId仅在代理通道可用时生效，通道关闭或断连后将不可用。 |
| callback | Callback<[DataInfo](js-apis-proxychannelmanager.md#datainfo)> | 否 | 注册的回调函数。默认效果：不传入此参数时取消订阅所有的数据接收事件。需传入on方法最后一次注册的回调函数，用于取消该回调的订阅；传入其他回调函数不会生效。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](errorcode-proxychannelmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ts
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          try {
            proxyChannelManager.off('receiveData', channelId); // channelId通过openProxyChannel接口的Promise返回值获取
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to unregister receiveData callback. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## proxyChannelManager.on('channelStateChange')

on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void

订阅通道状态事件，使用Callback异步回调。适用于手机侧应用需要实时感知代理通道连接状态的场景，例如监测通道断开后暂停数据发送、通道恢复后自动重试业务等。代理模块实时监控蓝牙BR链路状态变化，当发生连接恢复、异常断连、配对关系删除等事件时通过回调上报ChannelStateInfo。必须在[openProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanageropenproxychannel)成功打开代理通道后才能订阅通道状态事件。订阅后需调用[off('channelStateChange')](js-apis-proxychannelmanager.md#proxychannelmanageroffchannelstatechange)取消订阅，避免回调持续触发。调用[closeProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanagercloseproxychannel)关闭通道后，已注册的channelStateChange回调将自动取消订阅。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**设备行为差异**：该接口在Phone/Tablet设备中可正常调用，其他支持分布式业务的设备中会返回错误码32390004，不支持分布式业务的Wearable设备不返回错误码，不抛异常。

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型，固定取值为'channelStateChange'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId，取值范围为1~2147483647。使用无效或已关闭的channelId将返回错误码32390004，超出取值范围时返回错误码32390006。channelId仅在代理通道可用时生效，通道关闭或断连后将不可用。 |
| callback | Callback<[ChannelStateInfo](js-apis-proxychannelmanager.md#channelstateinfo)> | 是 | 回调函数，用于接收代理通道的状态变更信息。回调参数为[ChannelStateInfo](js-apis-proxychannelmanager.md#channelstateinfo)对象，包含channelId（通道ID）和state（通道连接状态）。需先通过openProxyChannel打开代理通道后才能接收通道状态。多次注册时，仅最后一次注册的回调函数生效。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](errorcode-proxychannelmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ts
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          const channelStateChangeCallback = (channelStateInfo: proxyChannelManager.ChannelStateInfo) => {
          };
          try {
            proxyChannelManager.on('channelStateChange', channelId, channelStateChangeCallback); // channelId通过openProxyChannel接口的Promise返回值获取
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to register channelStateChange callback. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## proxyChannelManager.off('channelStateChange')

off(type: 'channelStateChange', channelId: number, callback?: Callback<ChannelStateInfo>): void

取消订阅通道状态事件。适用于手机侧应用不再需要监听代理通道连接状态变化的场景，例如用户退出相关业务页面、完成数据传输流程后等。必须在[openProxyChannel](js-apis-proxychannelmanager.md#proxychannelmanageropenproxychannel)成功打开代理通道后才能取消订阅。此方法必须与[on('channelStateChange')](js-apis-proxychannelmanager.md#proxychannelmanageronchannelstatechange)配对使用，用于取消之前通过on('channelStateChange')注册的通道状态回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**设备行为差异**：该接口在Phone/Tablet设备中可正常调用，其他支持分布式业务的设备中会返回错误码32390004，不支持分布式业务的Wearable设备不返回错误码，不抛异常。

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置订阅类型，固定取值为'channelStateChange'。 |
| channelId | number | 是 | 打开代理通道时获取的channelId，取值范围为1~2147483647。使用无效或已关闭的channelId将返回错误码32390004，超出取值范围时返回错误码32390006。channelId仅在代理通道可用时生效，通道关闭或断连后将不可用。 |
| callback | Callback<[ChannelStateInfo](js-apis-proxychannelmanager.md#channelstateinfo)> | 否 | 注册的回调函数。默认效果：不传入此参数时取消订阅所有的通道状态事件。需传入on方法最后一次注册的回调函数，用于取消该回调的订阅；传入其他回调函数不会生效。 |

**错误码：**

以下错误码的详细介绍请参考[代理通道管理错误码](errorcode-proxychannelmanager.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390006 | Parameter error. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

**示例：**

```ts
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('测试')
        .onClick(() => {
          try {
            proxyChannelManager.off('channelStateChange', channelId); // channelId通过openProxyChannel接口的Promise返回值获取
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to unregister channelStateChange callback. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## DataInfo

存放接收的数据信息，包括通道ID和数据。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| channelId | number | 否 | 否 | 代理通道的channelId，取值范围为1~2147483647。 |
| data | ArrayBuffer | 否 | 否 | 接收到的字节数据，长度最大为4096字节。 |

## ChannelInfo

打开代理通道函数的入参，包括代理通道的链路类型、对端设备的MAC地址和监听服务的UUID。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| linkType | [LinkType](js-apis-proxychannelmanager.md#linktype) | 否 | 否 | 代理通道的链路类型，取值范围见[LinkType](js-apis-proxychannelmanager.md#linktype)，目前仅支持LINK\_BR（蓝牙BR协议）。 |
| peerDevAddr | string | 否 | 否 | 对端设备的MAC地址，格式为XX:XX:XX:XX:XX:XX，其中XX为十六进制字符（0~9、A~F或a~f）。对端设备必须已配对，未配对时返回错误码32390002。格式不符合要求时返回错误码32390006。 |
| peerUuid | string | 否 | 否 | 对端监听的服务的UUID，格式为标准UUID字符串，如xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。格式不符合要求时返回错误码32390006。 |

## ChannelStateInfo

当代理通道状态变化时，用于表示代理通道的连接状态。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| channelId | number | 否 | 否 | 代理通道的channelId，取值范围为1~2147483647。 |
| state | [ChannelState](js-apis-proxychannelmanager.md#channelstate) | 否 | 否 | 通道的连接状态，取值范围见[ChannelState](js-apis-proxychannelmanager.md#channelstate)。建议根据不同状态值调整业务策略，如通道断开时暂停数据发送、通道恢复后重试业务。 |

## ChannelState

通道状态发生变化时，代理通道上报的通道连接状态。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHANNEL\_WAIT\_RESUME | 0 | 连接已断开，通道不可用。 |
| CHANNEL\_RESUME | 1 | 连接已恢复，通道可用。 |
| CHANNEL\_EXCEPTION\_SOFTWARE\_FAILED | 2 | 软件异常导致通道不可用，如内部协议栈错误、资源分配失败等。建议检查日志定位具体原因。 |
| CHANNEL\_BR\_NO\_PAIRED | 3 | 蓝牙配对关系被删除，通道不可用。 |

## LinkType

链路类型。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LINK\_BR | 0 | 蓝牙BR协议，适用于通过蓝牙BR链路与穿戴设备建立双向数据通道的场景。 |
