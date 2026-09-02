---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-remote-state
title: 远端状态订阅开发实例
breadcrumb: 指南 > 应用框架 > IPC Kit（进程间通信服务） > 远端状态订阅开发实例
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c7f87ce514333d438b9ab7a97f185cfef31e02ae6e6f5949085598d763399954
---

IPC/RPC提供了订阅远端Stub对象状态的机制。当远端Stub对象死亡时，可以自动触发本端Proxy注册的死亡通知。这种死亡通知订阅需要调用指定接口[registerDeathRecipient](../harmonyos-references/js-apis-rpc.md#registerdeathrecipient9-1)完成。不再需要订阅时，也需要调用指定接口[unregisterDeathRecipient](../harmonyos-references/js-apis-rpc.md#unregisterdeathrecipient9-1)取消订阅。

使用这种订阅机制的用户需要继承死亡通知类[DeathRecipient](../harmonyos-references/js-apis-rpc.md#deathrecipient)，并实现[onRemoteDied](../harmonyos-references/js-apis-rpc.md#onremotedied)方法清理资源。该方法会在远端Stub对象所在进程退出或当前RPC通信依赖的软总线连接断开时被回调。

**注意** 

* 首先，Proxy订阅Stub死亡通知，若在订阅期间Stub状态正常，则在不再需要时取消订阅。
* 其次，若在订阅期间，Stub所在进程退出或当前RPC通信依赖的软总线连接断开，则会自动触发执行业务已向Proxy注册的自定义的[onRemoteDied](../harmonyos-references/js-apis-rpc.md#onremotedied)方法。

## 使用场景

IPC/RPC的订阅机制适用于以下场景：

1. IPC通信，Proxy对象需要感知远端Stub对象所在进程的状态。
2. RPC通信，Proxy对象需要感知远端Stub对象所在进程的状态，或者RPC通信依赖的软总线连接断开。

当Proxy感知到Stub端死亡后，应该清理本地Proxy对象以及相关资源。

**注意** 

RPC不支持匿名Stub对象（没有向SAMgr注册）的死亡通知，IPC支持匿名Stub对象的死亡通知。

## ArkTS侧接口

**说明** 

* 此文档中的示例代码描述的是系统应用跨进程通信。
* 使用场景约束：客户端是第三方/系统应用，服务端是系统应用/服务

| 接口名 | 返回值类型 | 功能描述 |
| --- | --- | --- |
| [registerDeathRecipient](../harmonyos-references/js-apis-rpc.md#registerdeathrecipient9-1) | void | 注册用于接收远程对象死亡通知的回调，该方法应该在proxy侧调用。 |
| [unregisterDeathRecipient](../harmonyos-references/js-apis-rpc.md#unregisterdeathrecipient9-1) | void | 注销用于接收远程对象死亡通知的回调。 |
| [onRemoteDied](../harmonyos-references/js-apis-rpc.md#onremotedied) | void | Proxy侧注册死亡通知成功后，当远端Stub对象所在进程死亡时，将自动回调本方法。 |

### 参考代码

在IPC（同设备的跨进程通信）场景中，示例代码如下：

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

连接服务，获取代理对象，然后注册死亡监听。在断开连接时，移除死亡监听。

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
```

在RPC（跨设备的跨进程通信）场景中，示例代码如下：

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

获取[允许多设备协同的权限](permissions-for-all-user.md#ohospermissiondistributed_datasync)，在组网的情况下获取到对端的设备ID（组网场景下对应设备的唯一网络标识符，可以使用distributedDeviceManager获取目标设备的NetworkId）后连接服务，获取代理对象并注册死亡监听。当代理对象与服务端的通信结束后，在断开连接时，移除死亡监听。

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
```

## Stub反向感知Proxy死亡状态（匿名Stub的特殊用法）

正向的死亡通知是Proxy感知Stub的状态，要实现反向的死亡通知（即Stub感知Proxy的状态），可以利用反向死亡通知。例如，进程A（原Stub所在进程）和进程B（原Proxy所在进程），进程B获取到进程A的原Proxy对象后，在B进程新建一个匿名Stub对象（未向SAMgr注册），称为回调Stub，通过[sendMessageRequest](../harmonyos-references/js-apis-rpc.md#sendmessagerequest9-2)接口将回调Stub传给进程A的原Stub，进程A就可以获取到进程B的回调Proxy。只要向回调Proxy注册了死亡通知，当进程B（回调Stub）死亡或者RPC通信依赖的软总线连接断开时，回调Proxy会感知并通知进程A（原Stub），从而实现反向死亡通知。

**注意** 

* 反向死亡通知仅限设备内跨进程通信使用，不可用于跨设备。
* 当匿名Stub对象没有被任何一个Proxy引用时，对象会被自动释放。
