---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilityconnectmanager-guidelines
title: 跨设备连接UIAbility开发指南
breadcrumb: 指南 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > 应用跨设备连接管理 > 跨设备连接UIAbility开发指南
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ecca276925420ddfb0a8b6e8f00b6500ae40e6dd1b1e6d181567dd675c513f3
---

## 简介

自API version 18起，系统新增支持应用跨设备协同连接与通信能力（含数据传输）。该特性通过分布式组件管理框架实现多端应用协作（即多个终端设备上的应用协同完成同一业务场景），成为分布式能力体系的核心功能之一。典型应用场景如智能手表端的拍照控制应用，可远程调用手机端相机功能并实现跨设备的实时双向数据交互。

### 能力范围

* 跨设备拉起应用：支持在分布式组网环境下拉起关联应用，实现多端业务协同（需应用适配开发）
* 跨设备数据交互：实现跨设备数据传输，跨设备数据交互能力随不同应用类型存在差异。具体为系统应用可传输文本、字节流、图片及传输流，三方应用仅支持文本信息。

### 基本概念

在进行应用跨设备连接管理开发前，开发者应了解以下基本概念：

* **DMS**

  DMS（Distributedsched Management Service）是分布式组件管理框架，提供分布式组件的管理能力。
* **UIAbility**

  [UIAbility](uiability-overview.md)描述应用程序的界面交互能力，负责管理应用界面的生命周期、用户交互以及界面渲染等任务。
* **字节流**

  字节流是数据类型为[ArrayBuffer](arraybuffer-object.md)类型的数据。可以被用于存储二进制数据，例如图像或音频数据。

### 实现原理

应用跨设备连接管理依托分布式组件管理框架，在分布式组件管理框架上进行了JS对象型的封装，能通过分布式组件管理框架服务建立协同关系并进行应用间的连接，数据的交互能力由系统支持。

**图1** 应用跨设备连接运行机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/tW-vKxbzQYGsroESK_8A6Q/zh-cn_image_0000002706674400.png)

### 约束与限制

* 仅限于API version 18及以上版本设备。
* 双端设备登录同账号的场景下，支持相同或不同bundleName的应用间协同；非同账号场景下，系统侧会校验应用AppID，仅支持相同AppID的应用间协同。
* 业务协同完毕后需及时结束协同状态。为了系统的安全和资源合理利用考虑，未申请长时任务的应用，在锁屏或退至后台5秒以上，会被结束掉协同生命周期。
* 分布式组件管理框架在协同过程中不会对传输内容进行审查。涉及隐私敏感数据时，建议业务通过弹框提醒等方式提醒用户。

## 模拟器支持情况

本Kit暂不支持模拟器。

## 环境准备

### 环境要求

可登录华为账号的设备A和设备B，设备间需要组网成功（设备组网通过调用[Device Manager](devicemanager-guidelines.md)的接口实现）。

### 搭建环境

1. 在PC上安装[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio)，要求版本在4.1及以上。
2. 将public-SDK更新到API 18或以上。
3. 用USB线缆将任意一台调试设备（设备A或者设备B）连接到PC。
4. 打开设备A和设备B的Wi-Fi和蓝牙。如果登录同一个华为账号，则设备间会进行自组网；非同账号环境下，需先通过[设备发现](devicemanager-guidelines.md#设备发现开发指导)和[设备绑定](devicemanager-guidelines.md#设备绑定开发指导)建立可信关系以完成组网。

### 检验环境是否搭建成功

PC上执行shell命令：

```shell
hdc shell
hidumper -s 4700 -a "buscenter -l remote_device_info"
```

组网成功时可显示组网设备数量的信息，如“remote device num = 1”。

## 开发指导

应用跨设备连接管理可以通过分布式组件管理框架，拉起对端设备并发送消息。具体案例提供如下。

### 接口说明

应用跨设备连接管理接口如下表所示。具体API说明详见API参考：[abilityConnectionManager](../harmonyos-references/js-apis-distributed-abilityconnectionmanager.md)。

**表1** abilityConnectionManager接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo, connectOptions: ConnectOptions): number; | 创建应用间的会话。 |
| destroyAbilityConnectionSession(sessionId: number): void; | 销毁应用间的会话。 |
| connect(sessionId: number): Promise<ConnectResult>; | source侧进行ability的连接。 |
| acceptConnect(sessionId: number, token: string): Promise<void>; | sink侧进行ability的连接。 |
| disconnect(sessionId: number): void; | 断开ability的连接。 |
| on(type: 'connect' | 'disconnect' | 'receiveMessage' | 'receiveData', sessionId: number, callback: Callback<EventCallbackInfo>): void | 监听事件。 |
| off(type: 'connect' | 'disconnect' | 'receiveMessage' | 'receiveData', sessionId: number, callback?: Callback<EventCallbackInfo>): void | 取消事件的监听。 |
| sendMessage(sessionId: number, msg: string): Promise<void>; | 发送文本信息。 |
| sendData(sessionId: number, data: ArrayBuffer): Promise<void>; | 发送ArrayBuffer字节流。 |

### 开发步骤

通过应用跨设备管理模块，设备A拉起并连接设备B上的应用。连接成功后，设备A和设备B通过on接口注册相应事件的回调监听。设备A或设备B通过sendMessage、sendData接口发送消息、字节流。对端通过监听到的回调信息进行后续协同业务。

**导入AbilityConnectionManager模块文件**

```typescript
import {abilityConnectionManager, distributedDeviceManager } from '@kit.DistributedServiceKit';
```

**发现设备**

设备A上的应用，需要发现并选择设备B的[networkId](../harmonyos-references/js-apis-distributeddevicemanager.md#devicebasicinfo)来作为协同接口的入参。可调用分布式设备管理模块接口，进行对端设备的发现和选择，详情可参考[设备信息查询开发指导](devicemanager-guidelines.md#设备信息查询开发指导)。

**应用间创建会话并进行连接**

设备A和设备B在创建会话和连接时要执行的操作不同，接下来的开发步骤中，以设备A作为连接发起方，设备B作为连接接收端。

**1.设备A**

应用主动调用createAbilityConnectionSession()接口创建会话，获得sessionId。之后调用connect()方法启动ability会话连接（此时设备B上应用会被拉起）。

```typescript
let dmClass: distributedDeviceManager.DeviceManager;

function initDmClass(): void {
  // 其中createDeviceManager接口为系统API
  try {
    dmClass = distributedDeviceManager.createDeviceManager('com.example.remotephotodemo');
  } catch (err) {
    hilog.info(0x0000, 'testTag', 'createDeviceManager err');
  }
}

// 获取设备B的设备ID
function getRemoteDeviceId(): string | undefined {
  initDmClass();
  if (typeof dmClass === 'object' && dmClass !== null) {
    hilog.info(0x0000, 'testTag', 'getRemoteDeviceId begin');
    let list = dmClass.getAvailableDeviceListSync();
    if (typeof (list) === 'undefined' || typeof (list.length) === 'undefined') {
      hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is null');
      return;
    }
    if (list.length === 0) {
      hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is empty');
      return;
    }
    // 弹框选择设备
    return list[0].networkId;
  } else {
    hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: dmClass is null');
    return;
  }
}
```

```typescript
  createSession(): void {
    // 定义peer信息
    const peerInfo: abilityConnectionManager.PeerInfo = {
      deviceId: getRemoteDeviceId()!,
      bundleName: 'com.example.myapplication',
      moduleName: 'entry',
      abilityName: 'EntryAbility',
    };
    const myRecord: Record<string, string> = {
      'newKey1': 'value1',
    };

    // 定义连接选项
    const connectOption: abilityConnectionManager.ConnectOptions = {
      needSendData: true,
      startOptions: abilityConnectionManager.StartOptionParams.START_IN_FOREGROUND,
      parameters: myRecord
    };
    console.info(TAG + JSON.stringify(peerInfo))
    console.info(TAG + JSON.stringify(connectOption))
    let context = this.getUIContext().getHostContext();
    try {
      this.sessionId = abilityConnectionManager.createAbilityConnectionSession('collabTest', context, peerInfo, connectOption);
      hilog.info(0x0000, 'testTag', 'createSession sessionId is', this.sessionId);
      abilityConnectionManager.connect(this.sessionId).then((connectResult) => {
        if (!connectResult.isConnected) {
          hilog.info(0x0000, 'testTag', 'connect failed');
          return;
        }
      }).catch(() => {
        hilog.error(0x0000, 'testTag', 'connect failed');
      })
    } catch (error) {
      hilog.error(0x0000, 'testTag', error);
    }
  }
```

**2.设备B**

设备A的应用调用connect()后，设备B的应用会通过协同的方式被拉起，拉起时会触发协同生命周期函数onCollaborate()，可在该接口中配置createAbilityConnectionSession()接口以及acceptConnect()接口的调用。

```typescript
onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
  hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
  let param = wantParam['ohos.extra.param.key.supportCollaborateIndex'] as Record<string, Object>
  this.onCollab(param);
  return 0;
}

onCollab(collabParam: Record<string, Object>) {
  const sessionId = this.createSessionFromWant(collabParam);
  if (sessionId == -1) {
    return;
  }
  this.registerSessionEvent(sessionId);
  const collabToken = collabParam['ohos.dms.collabToken'] as string;
  abilityConnectionManager.acceptConnect(sessionId, collabToken).then(() => {
    AppStorage.setOrCreate<number>('sessionId', sessionId);
  }).catch(() => {
    console.error(TAG + `acceptConnect failed` );
  })
}

createSessionFromWant(collabParam: Record<string, Object>): number {
  let sessionId = -1;
  const peerInfo = collabParam['PeerInfo'] as abilityConnectionManager.PeerInfo;
  if (peerInfo == undefined) {
    return sessionId;
  }
  // 定义连接选项
  const options = collabParam['ConnectOption'] as abilityConnectionManager.ConnectOptions;
  try {
    sessionId = abilityConnectionManager.createAbilityConnectionSession('collabTest', this.context, peerInfo, options);
  } catch (error) {
    console.error(error);
  }
  return sessionId;
}
```

**注册事件监听**

在应用创建会话成功并获得sessionId后，开发者可调用on()方法进行对应事件的监听，通过触发回调函数的方式通知监听者，以便执行对应业务。

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

abilityConnectionManager.on("connect", this.sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'session connect, sessionId is', callbackInfo.sessionId);
});
abilityConnectionManager.on("disconnect", this.sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'session disconnect, sessionId is', callbackInfo.sessionId);
});
abilityConnectionManager.on("receiveMessage", this.sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'session receiveMessage, sessionId is', callbackInfo.sessionId);
});
```

**发送消息**

应用连接成功后，开发者可在设备A或者设备B上调用sendMessage()方法给对端应用发送文本信息。

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

abilityConnectionManager.sendMessage(this.sessionId, "message send success").then(() => {
  hilog.info(0x0000, 'testTag', "sendMessage success");
}).catch(() => {
  hilog.error(0x0000, 'testTag', "connect failed");
})
```

**2.发送字节流数据**

应用连接成功后，开发者可在设备A或者设备B上调用sendData()方法给对端应用发送字节数据。

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

let textEncoder = util.TextEncoder.create("utf-8");
const arrayBuffer  = textEncoder.encodeInto("data send success");

abilityConnectionManager.sendData(this.sessionId, arrayBuffer.buffer).then(() => {
  hilog.info(0x0000, 'testTag', "sendMessage success");
}).catch(() => {
  hilog.info(0x0000, 'testTag', "sendMessage failed");
})
```

**结束协同**

业务协同完毕后需及时结束协同状态。若是后续短期内还有协同需要，可调用disconnect()方法断开应用间的连接，保留sessionId，以便下次继续使用该sessionId进行连接。若是短期无需使用协同业务，可直接调用destroyAbilityConnectionSession()接口销毁会话，此时会自动断开连接。

```ts
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'disconnectRemoteAbility begin');
if (this.sessionId == -1) {
  hilog.info(0x0000, 'testTag', 'Invalid session ID.');
return;
}
abilityConnectionManager.disconnect(this.sessionId);

hilog.info(0x0000, 'testTag', 'destroyAbilityConnectionSession called');
abilityConnectionManager.destroyAbilityConnectionSession(this.sessionId);
```

### 调测验证

应用侧开发完成后，可在设备A和设备B上安装应用，测试步骤如下：

1. 点击设备A应用的“连接”按钮，此时设备B上的应用被拉起。
2. 点击设备A应用的“sendMessage”按钮，此时设备B上的应用会触发on()方法的回调，接收该字符串。
3. 点击设备A应用的“sendData”按钮，此时设备B上的应用会触发on()方法的回调，接收该字节流。
4. 点击设备A或设备B应用的“disconnect”按钮，此时双端会断开连接，触发connect()接口的回调，将断连信息上报给双端应用。

## 常见问题

### 设备A应用无法拉起设备B应用

**可能原因**

* 【原因1】：设备间没有相互组网，导致设备A发起连接时，createAbilityConnectionSession()接口中的peerInfo.deviceId属性未设置正确。
* 【原因2】：有多台设备相互组网，设备A发起连接时，createAbilityConnectionSession()接口中的peerInfo.deviceId属性设置为其他设备的deviceId，未正确指定到B设备上。

**解决措施**

* 针对原因1，设备A和设备B开启USB调试功能，用USB线连接设备和PC。执行shell命令：

  ```shell
  hdc shell
  hidumper -s 4700 -a "buscenter -l remote_device_info"
  ```

  回显信息为“remote device num = 0”即为组网失败，请确保登录同一华为账号并使用蓝牙连接。组网成功时可显示组网设备数量的信息，如“remote device num = 1”。
* 针对原因2，查询并选择指定设备时，添加设备选择列表，确保指定到期望的设备。

### 应用锁屏或者退后台一段时间后，正在执行的协同业务被断开

**可能原因**

应用在协同过程中，DMS会对应用的生命周期进行监听。发生锁屏、退后台操作持续五秒后，未申请长时任务的应用会被结束协同状态。

**解决措施**

应用申请[长时任务(ArkTS)](continuous-task.md)，消除此限制。
