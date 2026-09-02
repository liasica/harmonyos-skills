---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-service-extension-ability
title: 使用AppServiceExtensionAbility组件实现后台服务
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用模型 > 应用组件 > ExtensionAbility组件 > 使用AppServiceExtensionAbility组件实现后台服务
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1bfcba89cda0e54c023c3850804f9eb215340388cedd25489ee9885e0684fc03
---

## 概述

从API version 20开始，支持开发者使用[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件，为应用提供后台服务能力，其他三方应用可通过启动或连接该AppServiceExtensionAbility组件获取相应的服务。

例如，企业部署的数据防泄漏 (DLP) 软件需要能够长期无界面运行，持续监听文件操作、网络流量，并拦截违规行为，可以使用AppServiceExtensionAbility组件来实现其核心的后台监控服务。

**说明** 

本文将被启动或被连接的AppServiceExtensionAbility组件称为服务端，将启动或连接AppServiceExtensionAbility组件的应用组件（当前仅支持UIAbility）称为客户端。

## 约束与限制

### 设备限制

AppServiceExtensionAbility组件当前仅支持2in1设备。

### 规格限制

* 应用集成AppServiceExtensionAbility组件需要申请ACL权限（ohos.permission.SUPPORT\_APP\_SERVICE\_EXTENSION）。该ACL权限当前只对企业普通应用开放申请。
* 针对AppServiceExtensionAbility接口调用限制，详情请参考 [@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md) 的约束限制。

## 运作机制

开发者可以在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)中以启动（[startAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)）或连接（[connectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)）的方式来拉起AppServiceExtensionAbility组件。

* **启动：** 客户端必须为AppServiceExtensionAbility所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用才能调用[startAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)接口。
* **连接：** 如果[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)实例未启动，客户端必须为AppServiceExtensionAbility所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用才能调用[connectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)接口。如果实例已启动，则没有上述限制。

下表展示了拉起和连接的几种场景：

**说明** 

“客户端是否可信”为是时，表示客户端属于服务端所属应用或已配置在appIdentifierAllowList中。为否时，表示客户端不属于服务端所属应用且未配置在appIdentifierAllowList中。

| 客户端操作 | 服务端状态 | 客户端是否可信 | 结果说明 |
| --- | --- | --- | --- |
| startAppServiceExtensionAbility | 未启动 | 是 | 成功，服务端通过start方式启动，服务端状态变为已启动。 |
| startAppServiceExtensionAbility | 未启动 | 否 | 失败，客户端不在允许列表中，无法调用启动服务。 |
| startAppServiceExtensionAbility | 已启动 | 是 | 成功，服务端已经启动，start操作直接返回成功。 |
| startAppServiceExtensionAbility | 已启动 | 否 | 失败，客户端不在允许列表中，无法调用启动服务。 |
| connectAppServiceExtensionAbility | 未启动 | 是 | 成功，服务端通过connect方式启动，并建立连接。 |
| connectAppServiceExtensionAbility | 未启动 | 否 | 失败，客户端不在允许列表中，无法启动服务端。 |
| connectAppServiceExtensionAbility | 已启动 | 是 | 成功，服务端已启动，直接建立连接。 |
| connectAppServiceExtensionAbility | 已启动 | 否 | 成功，服务端已启动，直接建立连接。 |

## 实现一个后台服务

在DevEco Studio工程中手动新建一个AppServiceExtensionAbility组件，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为myappserviceextability。
2. 在myappserviceextability目录，右键选择“New > ArkTS File”，新建一个文件并命名为MyAppServiceExtAbility.ets。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/hiApg2LdTzSv20aasrAiKA/zh-cn_image_0000002706673078.png)

   其目录结构如下所示：

   ```txt
   ├── ets
   │ ├── myappserviceextability
   │ │   ├── MyAppServiceExtAbility.ets
   └
   ```
3. 在MyAppServiceExtAbility.ets文件中，增加导入[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)的依赖包，自定义类继承AppServiceExtensionAbility组件并实现生命周期回调。

   ```typescript
   import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
   import { rpc } from '@kit.IPCKit';
   // ···
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = '[MyAppServiceExtAbility]';
   const DOMAIN_NUMBER: number = 0xFF00;

   class StubTest extends rpc.RemoteObject {
     constructor(des: string) {
       super(des);
     }

     onRemoteMessageRequest(code: number,
       data: rpc.MessageSequence,
       reply: rpc.MessageSequence,
       options: rpc.MessageOption): boolean | Promise<boolean> {
       // 处理客户端发送的消息
       return true;
     }
   }

   export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
     onCreate(want: Want): void {
       let appServiceExtensionContext = this.context;
       hilog.info(DOMAIN_NUMBER, TAG, `onCreate, want: ${want.abilityName}`);
       // ···
     }

     onRequest(want: Want, startId: number): void {
       hilog.info(DOMAIN_NUMBER, TAG, `onRequest, want: ${want.abilityName}`);
     }

     onConnect(want: Want): rpc.RemoteObject {
       hilog.info(DOMAIN_NUMBER, TAG, `onConnect, want: ${want.abilityName}`);
       return new StubTest('test');
     }

     onDisconnect(want: Want): void {
       hilog.info(DOMAIN_NUMBER, TAG, `onDisconnect, want: ${want.abilityName}`);
     }

     onDestroy(): void {
       hilog.info(DOMAIN_NUMBER, TAG, 'onDestroy');
     }
   };
   ```
4. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册AppServiceExtensionAbility组件，type标签需要设置为“appService”，srcEntry标签表示当前ExtensionAbility组件所对应的代码路径。

   ```json5
   {
     "module": {
       // ...
       "extensionAbilities": [
         // ...
         {
           "name": "MyAppServiceExtAbility",
           "description": "appService",
           "type": "appService",
           "exported": true,
           "srcEntry": "./ets/myappserviceextability/MyAppServiceExtAbility.ets",
           "appIdentifierAllowList": [
             // 此处填写允许启动该后台服务的客户端应用的appIdentifier列表
           ]
         }
       ]
     }
   }
   ```

## 启动一个后台服务

应用通过[startAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)方法启动一个后台服务，服务的[onRequest()](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md#onrequest)回调就会被调用，并在该回调方法中接收到调用者传递过来的[Want](../harmonyos-references/js-apis-app-ability-want.md)对象。后台服务启动后，其生命周期独立于客户端，即使客户端已经销毁，该后台服务仍可继续运行。因此，后台服务需要在其工作完成时通过调用[AppServiceExtensionContext](../harmonyos-references/js-apis-inner-application-appserviceextensioncontext.md)的[terminateSelf()](../harmonyos-references/js-apis-inner-application-appserviceextensioncontext.md#terminateself)来自行停止，或者由另一个组件调用[stopAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#stopappserviceextensionability20)来将其停止。

**说明** 

AppServiceExtensionAbility组件以start方式启动，并且没有连接的时候，AppServiceExtensionAbility组件进程可能被挂起（请参考[Background Tasks Kit简介](background-task-overview.md)）。

* 在应用中启动一个新的[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

  ```typescript
  import { common, Want } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  const TAG: string = '[StartAppServiceExt]';
  const DOMAIN_NUMBER: number = 0xFF00;

  @Entry
  @Component
  struct StartAppServiceExt {
    build() {
      Column() {
      // ···
        List({ initialIndex: 0 }) {
          ListItem() {
            Row() {
              // ···
            }
          // ···
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
              let want: Want = {
                deviceId: '',
                bundleName: 'com.samples.appserviceextensionability',
                abilityName: 'MyAppServiceExtAbility'
              };
              context.startAppServiceExtensionAbility(want).then(() => {
                hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in starting AppServiceExtensionAbility.');
                // 成功启动后台服务
                this.getUIContext().getPromptAction().showToast({
                  message: 'SuccessfullyStartBackendService'
                });
              }).catch((err: BusinessError) => {
                hilog.error(DOMAIN_NUMBER, TAG,
                  `Failed to start AppServiceExtensionAbility. Code is ${err.code}, message is ${err.message}`);
              });
            })
          }

          // ···
        }
      // ···
      }

      // ···
    }
  }
  ```
* 在应用中停止一个已启动的[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件。

  ```typescript
  import { common, Want } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  const TAG: string = '[StopAppServiceExt]';
  const DOMAIN_NUMBER: number = 0xFF00;

  @Entry
  @Component
  struct StopAppServiceExt {
    build() {
      Column() {
      // ···
        List({ initialIndex: 0 }) {
          ListItem() {
            Row() {
              // ···
            }
          // ···
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
              let want: Want = {
                deviceId: '',
                bundleName: 'com.samples.appserviceextensionability',
                abilityName: 'MyAppServiceExtAbility'
              };
              context.stopAppServiceExtensionAbility(want).then(() => {
                hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in stopping AppServiceExtensionAbility.');
                this.getUIContext().getPromptAction().showToast({
                  message: 'SuccessfullyStoppedAStartedBackendService'
                });
              }).catch((err: BusinessError) => {
                hilog.error(DOMAIN_NUMBER, TAG,
                  `Failed to stop AppServiceExtensionAbility. Code is ${err.code}, message is ${err.message}`);
              });
            })
          }

          // ···
        }

      // ···
      }

      // ···
    }
  }
  ```
* 已启动的[AppServiceExtensionAbility](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md)组件停止自身。

  ```typescript
  import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
  // ···
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const TAG: string = '[MyAppServiceExtAbility]';
  // ···

  export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
    onCreate(want: Want): void {
      // ···
      // 执行业务逻辑
      this.context.terminateSelf().then(() => {
        hilog.info(0x0000, TAG, '----------- terminateSelf succeed -----------');
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, TAG, `terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
      });
    }

  // ···
  };
  ```

## 连接一个后台服务

### 客户端连接服务端

客户端可以通过[connectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)连接服务端（在Want对象中指定连接的目标服务），服务端的[onConnect()](../harmonyos-references/js-apis-app-ability-appserviceextensionability.md#onconnect)就会被调用，并在该回调方法中接收到客户端传递过来的[Want](../harmonyos-references/js-apis-app-ability-want.md)对象。

服务端的AppServiceExtensionAbility组件会在onConnect()中返回[IRemoteObject](../harmonyos-references/js-apis-rpc.md#iremoteobject)对象给客户端[ConnectOptions](../harmonyos-references/js-apis-inner-ability-connectoptions.md)的[onConnect()](../harmonyos-references/js-apis-inner-ability-connectoptions.md#onconnect)方法。开发者通过该IRemoteObject定义通信接口，实现客户端与服务端的RPC交互。多个客户端可以同时连接到同一个后台服务，客户端完成与服务端的交互后，客户端需要通过调用[disconnectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#disconnectappserviceextensionability20)来断开连接。如果所有连接到某个后台服务的客户端均已断开连接，则系统会销毁该服务。

* 使用[connectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)建立与后台服务的连接。示例中的context的获取方式请参见[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

  ```typescript
  import { common, Want } from '@kit.AbilityKit';
  import { rpc } from '@kit.IPCKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const TAG: string = '[ConnectAppServiceExt]';
  const DOMAIN_NUMBER: number = 0xFF00;

  let connectionId: number;
  let want: Want = {
    deviceId: '',
    bundleName: 'com.samples.appserviceextensionability',
    abilityName: 'MyAppServiceExtAbility'
  };

  let options: common.ConnectOptions = {
    onConnect(elementName, remote: rpc.IRemoteObject): void {
      hilog.info(DOMAIN_NUMBER, TAG, 'onConnect callback');
      if (remote === null) {
        hilog.info(DOMAIN_NUMBER, TAG, `onConnect remote is null`);
        return;
      }
      // 通过remote进行通信
    },
    onDisconnect(elementName): void {
      hilog.info(DOMAIN_NUMBER, TAG, 'onDisconnect callback');
    },
    onFailed(code: number): void {
      hilog.info(DOMAIN_NUMBER, TAG, 'onFailed callback', JSON.stringify(code));
    }
  };

  @Entry
  @Component
  struct ConnectAppServiceExt {
    build() {
      Column() {
      // ···
        List({ initialIndex: 0 }) {
          ListItem() {
            Row() {
              // ···
            }
          // ···
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
              // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
              connectionId = context.connectAppServiceExtensionAbility(want, options);
              // 成功连接后台服务
              this.getUIContext().getPromptAction().showToast({
                message: 'SuccessfullyConnectBackendService'
              });
              hilog.info(DOMAIN_NUMBER, TAG, `connectionId is : ${connectionId}`);
            })
          }

          // ···
        }

      // ···
      }

      // ···
    }
  }
  ```
* 使用[disconnectAppServiceExtensionAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#disconnectappserviceextensionability20)断开与后台服务的连接。

  ```typescript
  import { common } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  const TAG: string = '[DisConnectAppServiceExt]';
  const DOMAIN_NUMBER: number = 0xFF00;

  let connectionId: number;

  @Entry
  @Component
  struct DisConnectAppServiceExt {
    build() {
      Column() {
      // ···
        List({ initialIndex: 0 }) {
          ListItem() {
            Row() {
              // ···
            }
          // ···
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
              // connectionId为调用connectServiceExtensionAbility接口时的返回值，需开发者自行维护
              context.disconnectAppServiceExtensionAbility(connectionId).then(() => {
                hilog.info(DOMAIN_NUMBER, TAG, 'disconnectAppServiceExtensionAbility success');
                // 成功断连后台服务
                this.getUIContext().getPromptAction().showToast({
                  message: 'SuccessfullyDisconnectBackendService'
                });
              }).catch((error: BusinessError) => {
                hilog.error(DOMAIN_NUMBER, TAG, 'disconnectAppServiceExtensionAbility failed');
              });
            })
          }

          // ···
        }

      // ···
      }

      // ···
    }
  }
  ```

### 客户端与服务端通信

客户端在[onConnect()](../harmonyos-references/js-apis-inner-ability-connectoptions.md#onconnect)中获取到[rpc.IRemoteObject](../harmonyos-references/js-apis-rpc.md#iremoteobject)对象后便可与服务端进行通信。

**客户端**：使用[sendMessageRequest](../harmonyos-references/js-apis-rpc.md#sendmessagerequest9)接口向服务端发送消息。

```typescript
import { common, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[ClientServerExt]';
const DOMAIN_NUMBER: number = 0xFF00;
const REQUEST_CODE = 1;
let connectionId: number;
let want: Want = {
  deviceId: '',
  bundleName: 'com.samples.appserviceextensionability',
  abilityName: 'MyAppServiceExtAbility'
};
let options: common.ConnectOptions = {
  onConnect(elementName, remote): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onConnect callback');
    if (remote === null) {
      hilog.info(DOMAIN_NUMBER, TAG, `onConnect remote is null`);
      return;
    }
    let option = new rpc.MessageOption();
    let data = new rpc.MessageSequence();
    let reply = new rpc.MessageSequence();

    try {
         // 写入请求数据
         data.writeInt(1);
         data.writeInt(2);
       } catch (error) {
         let e: BusinessError = error as BusinessError;
         hilog.error(DOMAIN_NUMBER, TAG, 'errorCode ' + e.code);
         hilog.error(DOMAIN_NUMBER, TAG, 'errorMessage ' + e.message);
       }

    remote.sendMessageRequest(REQUEST_CODE, data, reply, option).then((ret: rpc.RequestResult) => {
      if (ret.errCode === 0) {
        hilog.info(DOMAIN_NUMBER, TAG, `sendRequest got result`);
        let sum = ret.reply.readInt();
        hilog.info(DOMAIN_NUMBER, TAG, `sendRequest success, sum:${sum}`);
      } else {
        hilog.error(DOMAIN_NUMBER, TAG, `sendRequest failed`);
      }
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, `sendRequest failed, ${JSON.stringify(error)}`);
    });
  },
  onDisconnect(elementName): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onDisconnect callback');
  },
  onFailed(code): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onFailed callback');
  }
};

// 调用connectAppServiceExtensionAbility相关代码

@Entry
@Component
struct ClientServerExt {
  build() {
    Column() {
      // ...
      List({ initialIndex: 0 }) {
        ListItem() {
          Row() {
            // ...
          }
          // ...
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
            connectionId = context.connectAppServiceExtensionAbility(want, options);
            hilog.info(DOMAIN_NUMBER, TAG, `connectionId is : ${connectionId}`);
          })
        }
      }
      // ...
    }
  }
}
```

**服务端**：使用[onRemoteMessageRequest](../harmonyos-references/js-apis-rpc.md#onremotemessagerequest9)接口接收客户端发送的消息。

```typescript
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[MyAppServiceExtAbility]';
const DOMAIN_NUMBER: number = 0xFF00;

// 开发者需要在这个类型里对接口进行实现
class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption): boolean | Promise<boolean> {
    try {
         hilog.info(DOMAIN_NUMBER, TAG, 'onRemoteMessageRequest');
         let sum = data.readInt() + data.readInt();
         reply.writeInt(sum);
       } catch (error) {
         let e: BusinessError = error as BusinessError;
         hilog.error(DOMAIN_NUMBER, TAG, 'errorCode ' + e.code);
         hilog.error(DOMAIN_NUMBER, TAG, 'errorMessage ' + e.message);
       }
    return true;
  }
}

// 服务端实现
export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
  onCreate(want: Want): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onDestroy');
  }

  onConnect(want: Want): rpc.RemoteObject {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onConnect');
    return new Stub('test');
  }

  onDisconnect(): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onDisconnect');
  }
}
```

### 服务端对客户端身份校验

部分开发者需要使用AppServiceExtensionAbility组件提供一些较为敏感的服务，可以通过如下方式对客户端身份进行校验。

**通过callerTokenId对客户端进行鉴权**

通过调用[getCallingTokenId()](../harmonyos-references/js-apis-rpc.md#getcallingtokenid8)接口获取客户端的tokenID，再调用[verifyAccessTokenSync()](../harmonyos-references/js-apis-abilityaccessctrl.md#verifyaccesstokensync9)接口判断客户端是否有某个具体权限，由于当前不支持自定义权限，因此只能校验当前[系统所定义的权限](app-permissions.md)。示例代码如下：

```typescript
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { abilityAccessCtrl, bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[AppServiceExtImpl]';
const DOMAIN_NUMBER: number = 0xFF00;

// 开发者需要在这个类里进行实现

class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(
    code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption): boolean | Promise<boolean> {
    // 开发者自行实现业务逻辑
    hilog.info(DOMAIN_NUMBER, TAG, `onRemoteMessageRequest: ${data}`);
    let callerUid = rpc.IPCSkeleton.getCallingUid();
    bundleManager.getBundleNameByUid(callerUid).then((callerBundleName) => {
      hilog.info(DOMAIN_NUMBER, TAG, 'getBundleNameByUid: ' + callerBundleName);
      // 对客户端包名进行识别
      if (callerBundleName !== 'com.samples.stagemodelabilitydevelop') { // 识别不通过
        hilog.info(DOMAIN_NUMBER, TAG, 'The caller bundle is not in trustlist, reject');
        return;
      }
      // 识别通过，执行正常业务逻辑
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, 'getBundleNameByUid failed: ' + err.message);
    });

    let callerTokenId = rpc.IPCSkeleton.getCallingTokenId();
    let accessManager = abilityAccessCtrl.createAtManager();
    // 所校验的具体权限由开发者自行选择，此处ohos.permission.GET_BUNDLE_INFO_PRIVILEGED只作为示例
    let grantStatus = accessManager.verifyAccessTokenSync(callerTokenId, 'ohos.permission.GET_BUNDLE_INFO_PRIVILEGED');
    if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_DENIED) {
      hilog.error(DOMAIN_NUMBER, TAG, 'PERMISSION_DENIED');
      return false;
    }
    hilog.info(DOMAIN_NUMBER, TAG, 'verify access token success.');
    return true;
  }
}

export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
  onConnect(want: Want): rpc.RemoteObject {
    return new Stub('test');
  }
  // 其他生命周期
}
```
