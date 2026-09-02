---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-network-reconnection
title: 应用网络重连
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 连接网络 > 连接网络开发实践 > 应用网络重连
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-08-11
content_hash: sha256:a25778a3f53f03c9c0c39cad190e8fbbb8495b69112678bb3451b69fbc5eba46
---

## 概述

网络重连是指设备或应用程序在网络连接中断或出现异常时，重新建立通信链路的过程。对于高度依赖网络的业务与应用而言，网络重连机制能够在网络发生短暂中断后迅速恢复连接，从而显著缩短业务中断时间，提升服务的连续性与可靠性。特别是在在线金融交易、远程医疗及音视频实时播放等对实时性和稳定性要求极高的场景中，网络重连功能发挥着至关重要的作用。根据具体的应用场景，网络重连机制可划分为多种实现方式。

* [网络超时重连](application-network-reconnection.md#网络超时重连)：客户端向服务器发送请求后，如果发生网络超时，那么客户端将自动尝试与服务器重新建立连接。
* [网络切换重连](application-network-reconnection.md#网络切换重连)：当网络连接发生变化后，客户端应用可能会出现网络异常。应用需要检测网络状态变化，并根据网络状态进行连接。
* [应用前后台切换后重连](application-network-reconnection.md#应用前后台切换后重连)：应用切换到后台一段时间后，网络资源会被冻结释放，需要客户端重新建立连接。

## 网络超时重连

### 场景描述

在网络请求中，经常会遇到网络波动、服务器宕机等情况，从而导致网络不可用、网络超时等问题。为了减少网络超时等带来的影响，在实际应用开发中经常使用超时机制和重试机制。如HTTP请求列表数据时，设置HTTP连接超时和请求重试。

* 网络超时机制是指在网络通信过程中，当一个操作在规定的时间内没有得到预期的响应或完成时，系统会自动判定该操作失败，并触发相应的处理逻辑。其原理是通过设置一个定时器，从网络操作开始时计时，一旦超过设定的时间阈值，就认为操作超时。
* 重试机制一般配合超时机制一起使用，指的是多次发送相同的请求来避免瞬态故障和偶然性故障。

### 实现原理

网络超时分为网络连接超时和网络读取超时。

* 网络连接超时就是在程序默认的等待时间内没有得到服务器的响应。
* 网络读取超时指客户端在读取服务器响应时等待的时间。

网络重试常用的策略有定时重试、指数退避重试、随机退避重试等。

* 定时重试：设定一个固定的重试次数，当网络请求失败时，在该次数范围内进行重试，每次重试之间的时间间隔可以是固定的，也可以根据具体情况进行调整。例如，设定重试次数为 3 次，每次重试间隔为 2 秒。
* 指数退避重试：每次重试的时间间隔按照指数级增长，如重试间隔时间依次为2、4、8、16等。
* 随机退避重试：每次重试的时间间隔在一个指定的范围内随机取值。例如，设定重试间隔时间在 1 秒到 5 秒之间随机，这样可以避免多个请求同时重试，分散服务器的负载压力，提高整体的重试成功率。

在设置重试策略时，需要根据实际的场景来进行设置，既要考虑网络超时的时间，还需要关注重试的次数和时间间隔，避免网络资源浪费。

### 开发步骤

在HarmonyOS中，在Http、RCP发生错误或者超时后，都可以使用网络超时重连的机制。HTTP超时重连的实现步骤如下所示。

* 设置HTTP请求的读取超时时间、连接超时时间。
* 可以根据网络状态进行判断，然后再进行重连。这样可以在非网络问题的情况下进行重试，可以更精准地控制重试行为，提高请求的成功率和效率。例如，对于一些表示服务错误的响应码（如 500 Internal Server Error、503 Service Unavailable 等），可以进行重试。
* 使用setTimeout进行函数执行延迟，配合使用Promise，进而同步获取网络请求结果。

HTTP超时重连的代码如下所示：

```ts
async getHttpRequest(url: string, retry: number): Promise<number | undefined> {
  try {
    return await this.httpRequest?.requestInStream(url,
      { method: http.RequestMethod.GET, connectTimeout: 6000, readTimeout: 60000 })
      .then((data: number) => {
        if ((data === 408 || data === 500) && retry > 0) {
          return new Promise((resolve: Function) => {
            setTimeout(() => {
              resolve(this.getHttpRequest(url, retry - 1));
            }, 2000);
          });
        } else {
          return data;
        }
      });
  } catch (err) {
    this.isDownload = false;
    try {
      this.getUIContext().getPromptAction().showToast({ message: $r('app.string.download_error') });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0xFF00, 'NetworkReconnection', `showToast fail, code = ${err.code}, message = ${err.message}`);
    }
    return;
  }
}
```

RCP超时重连的实现与HTTP的实现步骤类似，RCP超时重连的代码如下所示：

```ts
createRCPSession(): rcp.Session | null {
  try {
    const customHttpEventsHandler: rcp.HttpEventsHandler = {
      onDownloadProgress: (totalSize: number, transferredSize: number) => {
        this.contentLength = totalSize;
        this.downloadSize = transferredSize;
        this.process = this.contentLength === 0 ? 0 : Math.floor(this.downloadSize / this.contentLength * 100);
      },
      onDataEnd: () => {
        this.contentLength = -1;
        this.downloadSize = 0;
      },
    };
    const sessionConfig: rcp.SessionConfiguration = {
      requestConfiguration: {
        transfer: {
          timeout: {
            connectMs: 6000,
            transferMs: 60000
          }
        },
        tracing: { httpEventsHandler: customHttpEventsHandler }
      }
    }
    return rcp.createSession(sessionConfig);
  } catch (error) {
    return null;
  }
}

// ...

async getRcpRequest(url: string, retry: number): Promise<rcp.Response | undefined> {
  try {
    if (this.session !== null) {
      return await this.session.get(url)
        .then((response) => {
          if ((response.statusCode === 408 || response.statusCode === 500) && retry > 0) {
            return new Promise((resolve: Function) => {
              setTimeout(() => {
                resolve(this.getRcpRequest(url, retry - 1));
              }, 2000)
            })
          } else {
            return response;
          }
        })
    } else {
      return;
    }
  } catch (err) {
    try {
      this.getUIContext().getPromptAction().showToast({ message: $r('app.string.download_error') });
      this.isDownload = false;
    } catch (error) {
      let err = error as BusinessError;
      Logger.error('NetworkReconnection', `showToast fail, code = ${err.code}, message = ${err.message}`);
    }
    return;
  }
}
```

## 网络切换重连

### 场景描述

在当下这个数字化时代，大部分的应用确实离不开网络，网络已经深度渗透到各类应用场景之中。然而，在网络状态切换后，如何继续保持网络连接是许多应用需要处理的问题。

### 实现原理

网络切换主要分为网络类型切换和无网络与有网络之间的切换。针对网络切换的场景，HarmonyOS提供了[网络连接管理](../harmonyos-references/js-apis-net-connection.md)能力，用于查询网络信息、监听网络连接的变化等。

在实现网络切换重连上，主要包含以下步骤。

* 使用网络连接管理的能力监听网络变化，并使用[AppStorage](arkts-appstorage.md)存储应用全局网络状态。
* 使用[@StorageProp](arkts-appstorage.md#storageprop)，将AppStorage存储的网络状态与对应的属性建立单向数据同步。
* 使用[@Watch](arkts-watch.md)监听状态变量的变化，当状态变量变化后，对网络进行关闭或重连。

### 开发步骤

调用connection的register()方法订阅网络变化通知，同时，订阅netCapabilitiesChange网络能力变化事件，订阅netLost网络丢失事件。在设备从有网络到无网络状态会触发netLost事件，从无网络到有网络会触发netCapabilitiesChange事件。而在网络类型切换时，也会触发netLost事件和netCapabilitiesChange事件，开发者可以根据实际场景需要在netCapabilitiesChange事件中，将网络类型及网络状态存储在AppStorage中。

```ts
private netCon: connection.NetConnection = connection.createNetConnection();

register() {
  this.netCon.register((error: BusinessError) => {
    Logger.error('net register' + JSON.stringify(error));
  });
}

netCapabilitiesChange() {
  this.netCon.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
    let netAvailable = false;
    data.netCap.networkCap?.forEach((value) => {
      if (value === connection.NetCap.NET_CAPABILITY_INTERNET) {
        netAvailable = true;
      }
    })
    Logger.info('ConnectionUtil.netAvailable:' + netAvailable);
    AppStorage.setOrCreate('netAvailable', netAvailable);
  })

  this.netCon.on('netLost', (data: connection.NetHandle) => {
    AppStorage.setOrCreate('netAvailable', false);
    Logger.info("WifiChangeListen-- Succeeded to get data: " + JSON.stringify(data));
  });
}
```

使用AppStorage存储应用全局网络状态。

```ts
@StorageProp('netAvailable') @Watch('onSocketUpdated') netAvailable: boolean = true;
```

使用@Watch监听状态变量的变化，并根据对应的变化和实际应用场景重新连接网络。

```ts
onSocketUpdated() {
  this.netAvailable ? this.tcpSocketConnect() : this.tcpSocketDisconnect();
  Logger.info('netAvailable:' + this.netAvailable);
}

// ...

tcpSocketConnect() {
  if (!this.netAvailable) {
    try {
      this.getUIContext().getPromptAction().showToast({ message: $r('app.string.connect_error') });
    } catch (error) {
      let err = error as BusinessError;
      Logger.error('NetworkReconnection', `showToast fail, code = ${err.code}, message = ${err.message}`);
    }
    return;
  }

  this.tcp = socket.constructTCPSocketInstance();
  this.tcp.on('connect', () => {
    Logger.info('on connect');
  });
  this.tcp.on('close', () => {
    Logger.info('on close');
  });
  this.tcp.on('error', (error: BusinessError) => {
    Logger.error('error:' + error.code + error.message
    );
  });
  const clientIpAddress: socket.NetAddress = {
    address: CommonConstants.IP_ADDRESS,
    port: CommonConstants.CLIENT_IP_PORT
  } as socket.NetAddress;

  this.tcp.bind(clientIpAddress, (err: BusinessError) => {
    if (err) {
      Logger.error('bind fail' + JSON.stringify(err));
      this.getUIContext().getPromptAction().showToast({ message: $r('app.string.connect_error') });
      return;
    }

    let tcpConnect: socket.TCPConnectOptions = {} as socket.TCPConnectOptions;
    const serverIpAddress: socket.NetAddress = {
      address: CommonConstants.IP_ADDRESS,
      port: CommonConstants.IP_PORT
    } as socket.NetAddress;
    tcpConnect.address = serverIpAddress;
    tcpConnect.timeout = 3000;
    this.tcp?.connect(tcpConnect, (err: BusinessError) => {
      if (err) {
        Logger.error('connect fail');
        this.getUIContext().getPromptAction().showToast({ message: $r('app.string.connect_error') });
        return;
      }
    });
  });
}
```

## 应用前后台切换后重连

### 场景描述

应用在使用TCPSocket、UDPSocket等通信时，如果未申请长时任务或短时任务，当应用退到后台一段时间后，可能遇到网络不可用或网络资源异常的情况，并且将应用切回前台后，继续使用之前的TCPSocket、UDPSocket等连接对象继续和服务器通信也可能出现网络异常。

### 实现原理

在HarmonyOS中，应用切换到后台2秒后，应用的网络资源会被冻结，并且在12秒后进行释放。此时，再继续使用网络资源，就会出现网络不可用的情况。如果应用有后台使用网络资源的场景，可以使用[短时任务](transient-task.md)或[长时任务](continuous-task.md)。

由于Socket通信是基于IP和端口进行通信的，在应用退到后台后，网络资源被冻结时会清空TCP、UDP连接对象的IP和端口，但是不会释放连接对象。在应用切换到前台后，系统会给连接对象重新分配新的IP和端口，继续使用之前的连接对象与服务器进行通信时，服务器会认为同一个连接对象前后IP和端口不一致，从而导致通信不可信、网络异常。

应用前后台切换后网络重连在实现上有以下两个关键部分。

* 结合[UIAbility组件生命周期](uiability-lifecycle.md)onForeground和onBackground，在前后台切换时，将应用前后台的状态存储在AppStorage中。
* 使用[@StorageProp](arkts-appstorage.md#storageprop)将AppStorage存储的前后台状态与对应的属性建立单向数据同步。并使用[@Watch](arkts-watch.md)监听状态变量的变化，当前后台变化后，关闭或重新连接。

### 开发步骤

前后台切换时，在UIAbility组件生命周期中存储前后台状态。

```ts
export default class EntryAbility extends UIAbility {
  // ...

  onForeground(): void {
    // ...
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // ...
    AppStorage.setOrCreate('onForeground', false);
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

使用@StorageProp同步前后台状态，并使用@Watch监听状态变化。

```ts
@StorageProp('onForeground') @Watch('onForegroundChange') onForeground: boolean = true;
// ...

onForegroundChange(): void {
  this.onForeground ? this.tcpSocketConnect() : this.tcpSocketDisconnect();
}
```

## 示例代码

* [实现应用网络重连功能](https://gitcode.com/harmonyos_samples/NetworkReconnection)
