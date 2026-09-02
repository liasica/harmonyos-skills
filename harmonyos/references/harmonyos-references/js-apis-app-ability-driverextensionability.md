---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-driverextensionability
title: "@ohos.app.ability.DriverExtensionAbility (驱动程序扩展能力)"
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > ArkTS API > @ohos.app.ability.DriverExtensionAbility (驱动程序扩展能力)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7146e4a9fa0d6603c972442bf4ce6b0fa44521539a389543be8f8ae331545974
---

DriverExtensionAbility模块提供驱动相关扩展能力，提供驱动创建、销毁、连接、断开等生命周期回调。

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 约束限制

为保障系统安全性和稳定性，防止 DriverExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](js-apis-app-ability-driverextensionability.md#附录)。

## 导入模块

```ts
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
```

## DriverExtensionAbility

### 属性

DriverExtensionAbility类，包含驱动扩展的上下文环境定义。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [DriverExtensionContext](js-apis-inner-application-driverextensioncontext.md) | 否 | 否 | DriverExtension的上下文环境，继承自ExtensionContext。 |

### onInit

onInit(want: Want): void

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**示例：**

```ts
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  onInit(want: Want) {
    console.info(`onInit, want: ${want.abilityName}`);
  }
}
```

### onRelease

onRelease(): void

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**示例：**

```ts
class DriverExt extends DriverExtensionAbility {
  onRelease() {
    console.info('onRelease');
  }
}
```

### onConnect

onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>

Extension生命周期回调，会在[onCreate](js-apis-app-ability-abilitystage.md#oncreate)之后回调。返回一个[RemoteObject](js-apis-rpc.md#remoteobject)对象，用于客户端和服务端进行通信。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| rpc.[RemoteObject](js-apis-rpc.md#remoteobject) | Promise<rpc.[RemoteObject](js-apis-rpc.md#remoteobject)> | 一个RemoteObject对象，用于客户端和服务端进行通信；或一个Promise对象，返回用于通信的RemoteObject对象。 |

**示例：**

```ts
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class StubTest extends rpc.RemoteObject {
    constructor(des: string) {
        super(des);
    }
    onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
      // 必须重写此接口
      return true;
    }
}
class DriverExt extends DriverExtensionAbility {
  onConnect(want: Want) {
    console.info(`onConnect , want: ${want.abilityName}`);
    return new StubTest('test');
  }
}
```

如果生成返回值[RemoteObject](js-apis-rpc.md#remoteobject)依赖一个异步接口，可以使用异步生命周期：

```ts
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { rpc } from '@kit.IPCKit';
import { Want } from '@kit.AbilityKit';

class StubTest extends rpc.RemoteObject {
    constructor(des: string) {
        super(des);
    }
    onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
      // 必须重写此接口
      return true;
    }
}
async function getDescriptor() {
    // 调用异步函数...
    return 'asyncTest';
}
class DriverExt extends DriverExtensionAbility {
  async onConnect(want: Want) {
    console.info(`onConnect , want: ${want.abilityName}`);
    let descriptor = await getDescriptor();
    return new StubTest(descriptor);
  }
}
```

### onDisconnect

onDisconnect(want: Want): void | Promise<void>

Extension的生命周期回调，客户端执行断开连接服务时回调。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 返回值为空；或一个Promise对象，无返回结果。 |

**示例：**

```ts
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  onDisconnect(want: Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
  }
}
```

在执行完onDisconnect生命周期回调后，应用可能会退出，从而可能导致onDisconnect中的异步函数未能正确执行，比如异步写入数据库。可以使用异步生命周期，以确保异步onDisconnect完成后再继续后续的生命周期。

```ts
import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';

class DriverExt extends DriverExtensionAbility {
  async onDisconnect(want: Want) {
    console.info(`onDisconnect, want: ${want.abilityName}`);
    // 调用异步函数...
  }
}
```

### onDump

onDump(params: Array<string>): Array<string>

转储客户端信息时调用，建议不要转储敏感信息。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array<string> | 是 | 转储命令的参数列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 一个string类型的数组，包含转储的客户端信息。 |

**示例：**

```ts
class DriverExt extends DriverExtensionAbility {
    onDump(params: Array<string>) {
        console.info(`dump, params: ${JSON.stringify(params)}`);
        return ['params'];
    }
}
```

## DriverExtensionContext

type DriverExtensionContext = \_DriverExtensionContext;

DriverExtensionAbility的上下文环境。

**系统能力**：SystemCapability.Driver.ExternalDevice

| 类型 | 说明 |
| --- | --- |
| \_DriverExtensionContext | DriverExtensionAbility的上下文环境，继承自ExtensionContext，其具体使用方法可参考[DriverExtensionContext](js-apis-inner-application-driverextensioncontext.md)。 |

## 附录

DriverExtensionAbility不支持以下模块的引用。

| Kit | 模块 |
| --- | --- |
| Ability Kit（程序框架服务） | [@ohos.abilityAccessCtrl (程序访问控制管理)](js-apis-abilityaccessctrl.md) |
| Ability Kit（程序框架服务） | [@ohos.ability.particleAbility (ParticleAbility模块)](js-apis-ability-particleability.md) |
| Ability Kit（程序框架服务） | [@ohos.app.ability.abilityManager (Ability信息管理)](js-apis-app-ability-abilitymanager.md) |
| Ability Kit（程序框架服务） | [@ohos.app.ability.appManager (应用管理)](js-apis-app-ability-appmanager.md) |
| Ability Kit（程序框架服务） | [@ohos.application.appManager (appManager)](js-apis-application-appmanager.md) |
| Ability Kit（程序框架服务） | [@ohos.bundle (Bundle模块)](js-apis-bundle.md) |
| Ability Kit（程序框架服务） | [@ohos.bundle.bundleManager (应用程序包管理模块)](js-apis-bundlemanager.md) |
| Ability Kit（程序框架服务） | [@ohos.bundle.defaultAppManager (默认应用管理)](js-apis-defaultappmanager.md) |
| Ability Kit（程序框架服务） | [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](js-apis-launcherbundlemanager.md) |
| Ability Kit（程序框架服务） | [Context (Stage模型的上下文基类)](js-apis-inner-application-context.md) |
| Ability Kit（程序框架服务） | [@ohos.continuation.continuationManager (流转/协同管理)](js-apis-continuation-continuationmanager.md) |
| ArkData（方舟数据管理） | [@ohos.data.distributedData (分布式数据管理)](js-apis-distributed-data.md) |
| ArkData（方舟数据管理） | [@ohos.data.distributedDataObject (分布式数据对象)](js-apis-data-distributedobject.md) |
| ArkData（方舟数据管理） | [@ohos.data.distributedKVStore (分布式键值数据库)](js-apis-distributedkvstore.md) |
| ArkData（方舟数据管理） | [@ohos.data.rdb (关系型数据库)](js-apis-data-rdb.md) |
| ArkUI（方舟UI框架） | [@ohos.screenshot (屏幕截图)](js-apis-screenshot.md) |
| Background Tasks Kit（后台任务开发服务） | [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md) |
| Background Tasks Kit（后台任务开发服务） | [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| Background Tasks Kit（后台任务开发服务） | [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md) |
| Background Tasks Kit（后台任务开发服务） | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md) |
| Background Tasks Kit（后台任务开发服务） | [@ohos.bundleState (设备使用信息统计)](js-apis-deviceusagestatistics.md) |
| Basic Services Kit（基础服务） | [@ohos.account.appAccount (应用账号管理)](js-apis-appaccount.md) |
| Basic Services Kit（基础服务） | [@ohos.account.distributedAccount (分布式账号管理)](js-apis-distributed-account.md) |
| Basic Services Kit（基础服务） | [@ohos.account.osAccount (系统账号管理)](js-apis-osaccount.md) |
| Basic Services Kit（基础服务） | [@ohos.deviceInfo (设备信息)](js-apis-device-info.md) |
| Basic Services Kit（基础服务） | [@ohos.power (系统电源管理)](js-apis-power.md) |
| Basic Services Kit（基础服务） | [@ohos.request (上传下载)](js-apis-request.md) |
| Basic Services Kit（基础服务） | [@ohos.runningLock (RunningLock锁)](js-apis-runninglock.md) |
| Basic Services Kit（基础服务） | [@ohos.settings (设置数据项名称)](js-apis-settings.md) |
| Basic Services Kit（基础服务） | [@ohos.systemTime (系统时间、时区)](js-apis-system-time.md) |
| Basic Services Kit（基础服务） | [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md) |
| Connectivity Kit（短距通信服务） | [@ohos.bluetooth (蓝牙)](js-apis-bluetooth.md) |
| Connectivity Kit（短距通信服务） | [@ohos.bluetoothManager (蓝牙)](js-apis-bluetoothmanager.md) |
| Connectivity Kit（短距通信服务） | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md) |
| Connectivity Kit（短距通信服务） | [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md) |
| Connectivity Kit（短距通信服务） | [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md) |
| Connectivity Kit（短距通信服务） | [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md) |
| Connectivity Kit（短距通信服务） | [@ohos.wifi (WLAN)](js-apis-wifi.md) |
| Connectivity Kit（短距通信服务） | [@ohos.wifiext (WLAN扩展接口)](js-apis-wifiext.md) |
| Connectivity Kit（短距通信服务） | [@ohos.wifiManager (WLAN)](js-apis-wifimanager.md) |
| Connectivity Kit（短距通信服务） | [@ohos.wifiManagerExt (WLAN扩展接口)](js-apis-wifimanagerext.md) |
| Contacts Kit（联系人服务） | [@ohos.contact (联系人)](js-apis-contact.md) |
| Core File Kit（文件基础服务） | [@ohos.file.storageStatistics (应用空间统计)](js-apis-file-storage-statistics.md) |
| Form Kit（卡片开发服务） | [@ohos.application.formError (formError)](js-apis-application-formerror.md) |
| IME Kit（输入法开发服务） | [@ohos.inputMethod (输入法框架)](js-apis-inputmethod.md) |
| Location Kit | [@ohos.geolocation (位置服务)](js-apis-geolocation.md) |
| Location Kit | [@ohos.geoLocationManager (位置服务)](js-apis-geolocationmanager.md) |
| MDM Kit（企业设备管理服务） | [@ohos.enterprise.adminManager（admin权限管理）](js-apis-enterprise-adminmanager.md) |
| MDM Kit（企业设备管理服务） | [@ohos.enterprise.deviceInfo（设备信息管理）](js-apis-enterprise-deviceinfo.md) |
| MultimediaKit | @ohos.multimedia.mediaLibrary (媒体库管理) |
| Network Kit（网络服务） | [@ohos.net.connection (网络连接管理)](js-apis-net-connection.md) |
| Network Kit（网络服务） | [@ohos.net.ethernet (以太网连接管理)](js-apis-net-ethernet.md) |
| Network Kit（网络服务） | [@ohos.net.http (数据请求)](js-apis-http.md) |
| Network Kit（网络服务） | [@ohos.net.sharing (网络共享管理)](js-apis-net-sharing.md) |
| Network Kit（网络服务） | [@ohos.net.socket (Socket连接)](js-apis-socket.md) |
| Network Kit（网络服务） | [@ohos.net.webSocket (WebSocket连接)](js-apis-websocket.md) |
| Notification Kit（用户通知服务） | [@ohos.notification (Notification模块)](js-apis-notification.md) |
| Notification Kit（用户通知服务） | [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| Performance Analysis Kit（性能分析服务） | [@ohos.hidebug (Debug调试)](js-apis-hidebug.md) |
| Sensor Service Kit（传感器服务） | [@ohos.sensor (传感器)](js-apis-sensor.md) |
| Sensor Service Kit（传感器服务） | [@ohos.vibrator (振动)](js-apis-vibrator.md) |
| Telephony Kit（蜂窝通信服务） | [@ohos.telephony.call (拨打电话)](js-apis-call.md) |
| Telephony Kit（蜂窝通信服务） | [@ohos.telephony.data (蜂窝数据)](js-apis-telephony-data.md) |
| Telephony Kit（蜂窝通信服务） | [@ohos.telephony.observer (observer)](js-apis-observer.md) |
| Telephony Kit（蜂窝通信服务） | [@ohos.telephony.radio (网络搜索)](js-apis-radio.md) |
| Telephony Kit（蜂窝通信服务） | [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md) |
| Telephony Kit（蜂窝通信服务） | [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
