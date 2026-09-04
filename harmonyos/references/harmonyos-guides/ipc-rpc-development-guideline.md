---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ipc-rpc-development-guideline
title: IPC与RPC通信开发指导(ArkTS)
breadcrumb: 指南 > 应用框架 > IPC Kit（进程间通信服务） > IPC与RPC通信开发指导(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:14+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:4723743f69ebdc5552798276ddffb2ad32f8179e503d8193b89973c9cef8601c
---

## 场景介绍

IPC/RPC的主要工作是跨进程建立对象通信的连接（客户端进程的Proxy和服务端进程的Stub建立一一对应关系），从而通过Proxy的接口可以和Stub进行IPC/RPC通信。

## 开发步骤

**说明** 

* 在进行IPC&RPC跨进程通信前需要通过Ability Kit获取服务端的代理对象。
* 不支持三方应用实现跨进程通信，三方应用仅可通过[connectServiceExtensionAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)连接系统提供的ServiceExtensionAbility，通过返回的代理对象[ServiceExtensionAbility](extensionability-overview.md)进行通信从而达到三方应用和系统服务通信的目的。
* 从API version 20开始，在2in1设备上，开发者可使用AppServiceExtensionAbility组件，为应用提供后台服务能力。三方应用可[connectAppServiceExtensionAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)连接AppServiceExtensionAbility，通过返回的代理对象和[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)进行通信从而达到三方和三方应用通信的目的。详细开发步骤参考[AppServiceExtensionAbility](app-service-extension-ability.md#连接一个后台服务)。
* 三方应用之间也可通过[动态订阅公共事件](common-event-subscription.md)进行进程间通信。
* 完整的IPC&RPC通信开发流程涉及系统ServiceExtensionAbility的实现，故本篇指南仅提供客户端示例代码。

### 客户端实现

1. 创建变量want，指定要连接的Ability所在应用的包名、组件名。
2. 创建变量connect，指定连接成功、连接失败和断开连接时的回调函数。
3. 连接服务，获取服务代理对象Proxy，并注册死亡监听。
4. 客户端发送消息给服务端。
5. 通信结束后，断开连接，移除服务代理对象Proxy的死亡监听。

**说明** 

* 在本文档的示例中，通过this.getUIContext().getHostContext()来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

在IPC（同设备的跨进程通信）场景中，客户端的示例如下：

导入相关依赖，并定义所需的变量；

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { PromptAction  } from '@kit.ArkUI';
import { JSON } from '@kit.ArkTS';

let proxy: rpc.IRemoteObject | undefined;
let connectId: number | undefined;

// 死亡通知
class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server is dead');
  }
}
let deathRecipient = new MyDeathRecipient();
```

连接服务，获取代理对象，发送信息给服务端，通信结束后断开连接。

```typescript
// 连接服务
function connectAbility(context:common.UIAbilityContext, promptAction: PromptAction) {
  hilog.info(0x00000, 'testTag', 'begin to connect Ability');
  let want: Want = {
    bundleName: 'com.example.ipc_stub',
    abilityName: 'ServiceAbility',
  };
  let connect: common.ConnectOptions = {
    onConnect: (elementName, remoteProxy) => {
      hilog.info(0x00000, 'testTag', 'onConnect. elementName is :' + JSON.stringify(elementName));
      proxy = remoteProxy;
      // 客户端注册死亡监听
      try {
        proxy.registerDeathRecipient(deathRecipient, 0);
        hilog.info(0x00000, 'testTag', 'registerDeathRecipient success');
      } catch (err) {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        hilog.error(0x0000, 'testTag', 'register failed, code is ' + code + ', message is ' + message);
      }
      // ...
    },

    onDisconnect: (elementName) => {
      hilog.info(0x0000, 'testTag', 'onDisconnect. elementName is ' + JSON.stringify(elementName));
      // 客户端移除死亡监听
      try {
        proxy?.unregisterDeathRecipient(deathRecipient, 0);
        hilog.info(0x00000, 'testTag', 'unregisterDeathRecipient success');
      } catch (err) {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        hilog.error(0x0000, 'testTag', 'unregister failed, code is ' + code + ', message is ' + message);
      }
      proxy = undefined;
      // ...
    },

    onFailed: (code: number) => {
      hilog.info(0x0000, 'testTag', 'onFailed. code is ' + code);
      // ...
    },
  }

  try {
    connectId = context.connectServiceExtensionAbility(want, connect);
    hilog.info(0x00000, 'testTag', 'begin to connect Ability end');
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'connectAbility failed, code is ' + code + ', message is ' + message);
  }
}

// 断开连接
function disconnectAbility(context: common.UIAbilityContext) {
  hilog.info(0x00000, 'testTag', 'begin to disconnect Ability. connectId is ' + connectId);
  if (connectId != undefined) {
    try {
      context.disconnectServiceExtensionAbility(connectId);
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(0x0000, 'testTag', 'disconnect failed, code is ' + code + ', message is ' + message);
    }
  }
}

// 发送消息
async function sendString(promptAction: PromptAction) : Promise <void> {
  hilog.info(0x00000, 'testTag', 'begin to send String');
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  // 在data里写入参数，以传递字符串为例
  data.writeString('hello world');
  if (proxy != undefined) {
    await proxy.sendMessageRequest(1, data, reply, option)
      .then((result: rpc.RequestResult) => {
        if (result.errCode != 0) {
          hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode is ' + result.errCode);
        }
        // 从result.reply里读取结果
        let str = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'sendMessageRequest receive str is ' + str);
        // ...
      })
      .catch((e: Error) => {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error is ' + JSON.stringify(e));
        // ...
      })
      .finally(() => {
        data.reclaim();
        reply.reclaim();
      })
  } else {
    hilog.error(0x0000, 'testTag', 'proxy is invalid');
    // ...
  }
  hilog.info(0x0000, 'testTag', 'sendString end');
}
```

在RPC（跨设备的跨进程通信）场景中，具体客户端的示例如下：

导入相关依赖，并定义所需的变量；

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { abilityAccessCtrl, PermissionRequestResult, common, Want} from '@kit.AbilityKit';
import { JSON } from '@kit.ArkTS';
import { PromptAction  } from '@kit.ArkUI';

let proxy: rpc.IRemoteObject | undefined;
let connectId: number | undefined;
let dmInstance: distributedDeviceManager.DeviceManager;
let deviceList: Array<distributedDeviceManager.DeviceBasicInfo> | undefined;
let deviceId: string| undefined;

// 死亡通知
class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server is dead');
  }
};
let deathRecipient = new MyDeathRecipient();
```

获取[允许多设备协同的权限](permissions-for-all-user.md#ohospermissiondistributed_datasync)，在组网的情况下获取到对端的设备ID（组网场景下对应设备的唯一网络标识符，可以使用distributedDeviceManager获取目标设备的NetworkId）后连接服务，获取代理对象并发送信息给服务端，当代理对象与服务端的通信结束后，进行断连。

```typescript
// 获取权限
function getPermission(context:common.UIAbilityContext) {
  hilog.info(0x00000, 'testTag', 'begin to requestPermissions');
  try {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(context, ['ohos.permission.DISTRIBUTED_DATASYNC'],
      (err: BusinessError, data: PermissionRequestResult) => {
      if (err) {
        hilog.error(0x0000, 'testTag', 'requestPermissions failed, code is ' + err.code);
        hilog.error(0x0000, 'testTag', 'requestPermissions failed, message is ' + err.message);
      } else {
        hilog.info(0x0000, 'testTag', 'requestPermissions success, result is ' + JSON.stringify(data));
        hilog.info(0x0000, 'testTag', 'data permissions is ' + data.permissions);
        hilog.info(0x0000, 'testTag', 'data authResults is ' + data.authResults);
        hilog.info(0x0000, 'testTag', 'data dialogShownResults is ' + data.dialogShownResults);
      }
    });
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'getPermission failed, code is ' + code + ', message is ' + message);
  }
}

// 获取对端设备信息
function getDeviceId(promptAction: PromptAction) {
  hilog.info(0x00000, 'testTag', 'begin to getDeviceId');
  try {
    dmInstance = distributedDeviceManager.createDeviceManager('com.example.rpc_client');
    hilog.info(0x0000, 'testTag', 'createDeviceManager success');
    deviceList = dmInstance.getAvailableDeviceListSync();
    hilog.info(0x0000, 'testTag', 'deviceList is ' + JSON.stringify(deviceList));
    if (deviceList.length !== 0) {
      deviceId = deviceList[0].networkId;
      hilog.info(0x0000, 'testTag', 'networkId is ' + deviceId);
      // ...
    }
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'getDeviceId failed, code is ' + code + ', message is ' + message);
    // ...
  }
}

// 连接服务
function connectAbility(context:common.UIAbilityContext, promptAction: PromptAction) {
  hilog.info(0x00000, 'testTag', 'begin to connect Ability');
  let want: Want = {
    bundleName: 'com.example.rpc_stub',
    abilityName: 'ServiceAbility',
    deviceId: deviceId,
  }

  let connect: common.ConnectOptions = {
    onConnect: (elementName, remoteProxy) => {
      hilog.info(0x00000, 'testTag', 'onConnect. elementName is ' + JSON.stringify(elementName));
      proxy = remoteProxy;
      // 客户端注册死亡监听
      try {
        proxy.registerDeathRecipient(deathRecipient, 0);
        hilog.info(0x00000, 'testTag', 'registerDeathRecipient success');
      } catch (err) {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        hilog.error(0x0000, 'testTag', 'register failed, code is ' + code + ', message is ' + message);
      };
      // ...
    },
    onDisconnect: (elementName) => {
      hilog.info(0x0000, 'testTag', 'onDisconnect. elementName is ' + JSON.stringify(elementName));
      // 客户端移除死亡监听
      try {
        proxy?.unregisterDeathRecipient(deathRecipient, 0);
        hilog.info(0x00000, 'testTag', 'unregisterDeathRecipient success');
      } catch (err) {
        let code = (err as BusinessError).code;
        let message = (err as BusinessError).message;
        hilog.error(0x0000, 'testTag', 'unregister failed, code is ' + code + ', message is ' + message);
      }
      proxy = undefined;
      // ...
    },
    onFailed: (code: number) => {
      hilog.info(0x0000, 'testTag', 'onFailed. code is ' + code);
      // ...
    },
  }

  try {
    connectId = context.connectServiceExtensionAbility(want, connect);
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    hilog.error(0x0000, 'testTag', 'connectService failed, code is ' + code + ', message is ' + message);
  }
}

// 断开连接
function disconnectAbility(context: common.UIAbilityContext) {
  hilog.info(0x00000, 'testTag', 'begin to disconnect Ability');
  if (connectId != undefined) {
    try {
      context.disconnectServiceExtensionAbility(connectId);
    } catch (err) {
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      hilog.error(0x0000, 'testTag', 'disconnectService failed, code is ' + code + ', message is ' + message);
    }
  }
}

// 发送消息
async function sendString(promptAction: PromptAction) : Promise <void> {
  hilog.info(0x00000, 'testTag', 'begin to send string');
  let option = new rpc.MessageOption();
  let data = rpc.MessageSequence.create();
  let reply = rpc.MessageSequence.create();
  // 在data里写入参数，以传递字符串为例
  data.writeString('hello world');

  if (proxy != undefined) {
    await proxy.sendMessageRequest(1, data, reply, option)
      .then((result: rpc.RequestResult) => {
        if (result.errCode != 0) {
          hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, errCode is ' + result.errCode);
        }
        // 从result.reply里读取结果
        let str = result.reply.readString();
        hilog.info(0x0000, 'testTag', 'sendMessageRequest receive str is ' + str);
        // 弹窗显示发送消息成功
        // ...
      })
      .catch((e: Error) => {
        hilog.error(0x0000, 'testTag', 'sendMessageRequest failed, error is ' + JSON.stringify(e));
        // 弹窗显示发送消息失败
        // ...
      })
      .finally(() => {
        data.reclaim();
        reply.reclaim();
      })
  } else {
    hilog.error(0x0000, 'testTag', 'proxy is invalid');
    // 弹窗显示发送消息失败
    // ...
  }
}
```

## 完整示例

**说明** 

* 以下完整示例涉及到ServiceExtensionAbility，需要使用full-SDK。参考示例前，请先阅读对应示例的ReadMe进行相应的配置后，再进行编译。

针对IPC与RPC通信开发，端到端的完整示例，请参考：

* [IPC通信完整示例-使用Parcelable/ArrayBuffer通信](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/SystemFeature/IPC/ObjectTransfer)
* [IPC通信完整示例-传递字符串及死亡监听使用](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/IPC/IPC_sendMessage)
* [RPC通信完整示例-传递字符串及死亡监听使用](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/IPC/RPC_sendMessage)
