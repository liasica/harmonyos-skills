---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agent-extension-ability
title: 使用AgentExtensionAbility组件实现智能体服务
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 方舟智能开发框架开发指导 > 端侧A2A框架开发指导 > 开发端侧智能体 > 使用AgentExtensionAbility组件实现智能体服务
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:53dd44743abdc670a1e96b3fd947e0420a2fcf2c5dd11e42e1673bcf32c279d3
---

## 概述

在跨应用协作场景下，开发者经常需要从系统应用调用其他应用提供的智能体服务，但缺少标准化的通信机制，导致集成成本高、安全认证复杂。从API version 24开始，支持开发者使用[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)类型的组件提供智能体服务。系统应用可以连接其他应用实现的[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)组件，并使用相应的智能体服务。通过使用该组件，可降低跨应用对接成本，保障通信安全，同时支持双向数据通道实时交互。

**说明** 

本文描述中称被连接的[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)为服务端，称连接[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)的组件为客户端。

## 实现AgentExtensionAbility组件

在DevEco Studio工程中手动新建一个[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)，具体步骤如下：

1. 在工程Module对应的ets目录下，右键选择"New > Directory"，新建一个目录并命名为agentextability。
2. 在AgentExtAbility目录，右键选择"New > ArkTS File"，新建一个文件并命名为AgentExtAbility.ets。

   ```txt
   ├── ets
   │ ├── agentextability
   │ │   ├── AgentExtAbility.ets
   ```
3. 在AgentExtAbility.ets文件中，补充[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)的导入模块，自定义类AgentExtAbility继承[AgentExtensionAbility](../harmonyos-references/js-apis-app-agent-agentextensionability.md)并实现生命周期回调。

   ```typescript
   import { common, AgentExtensionAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   export default class AgentExtAbility extends AgentExtensionAbility {
     private comProxy: common.AgentHostProxy | null = null;
     // 创建AgentExtensionAbility
     onCreate(want: Want) {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
     }

     // 连接
     onConnect(want: Want, proxy: common.AgentHostProxy) {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onConnect');
       this.comProxy = proxy;
     }

     // 断开连接
     onDisconnect(want: Want, proxy: common.AgentHostProxy) {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDisconnect');
       this.comProxy = null;
     }
     // 接收数据
     onData(proxy: common.AgentHostProxy, data: string) {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onData');
       try {
         let replyData = 'reply message';
         proxy.sendData(replyData);
       } catch (err) {
         let code = (err as BusinessError).code;
         let msg = (err as BusinessError).message;
         console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
       }
     }
     // 认证
     onAuth(proxy: common.AgentHostProxy, handshakeData: string) {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onAuth');
       try {
         // 处理认证逻辑
         let authResult = 'auth success';
         proxy.authorize(authResult);
       } catch (err) {
         let code = (err as BusinessError).code;
         let msg = (err as BusinessError).message;
         console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
       }
     }
     // 销毁
     onDestroy() {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
     }
   }
   ```
4. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册AgentExtensionAbility，type标签需要设置为"agent"，srcEntry标签表示当前ExtensionAbility组件所对应的代码路径。

   ```json
   {
     "module": {
       "extensionAbilities": [
         {
           "name": "AgentExtAbility",
           "icon": "$media:icon",
           "description": "agent",
           "type": "agent",
           "exported": true,
           "srcEntry": "./ets/agentextability/AgentExtAbility.ets",
           "metadata": [
             {
               "name": "ohos.extension.agent",
               "resource": "$profile:agent_config",
             }
           ]
         }
       ]
     }
   }
   ```
5. 在工程Module的resources/base/profile/目录下新建agent\_config.json文件，然后在其中配置[AgentCard](../harmonyos-references/js-apis-inner-application-agentcard.md)信息，详细操作步骤请参考[Agent配置文件说明](agent-extension-configuration.md)。

## 使用AgentExtensionAbility组件收发数据

应用可以在服务端AgentExtensionAbility组件的[onData()](../harmonyos-references/js-apis-app-agent-agentextensionability.md#ondata)方法中接收客户端传递的数据和[AgentHostProxy](../harmonyos-references/js-apis-inner-application-agenthostproxy.md)对象，并且可以通过调用[AgentHostProxy](../harmonyos-references/js-apis-inner-application-agenthostproxy.md)对象的[sendData()](../harmonyos-references/js-apis-inner-application-agenthostproxy.md#senddata)方法将数据发送给客户端。

```typescript
import { common, AgentExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class AgentExtAbility extends AgentExtensionAbility {
  // ...
  // 接收数据
  onData(proxy: common.AgentHostProxy, data: string) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onData');
    try {
      let replyData = 'reply message';
      proxy.sendData(replyData);
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
    }
  }
  // ...
}
```

## 使用AgentExtensionAbility组件接收和发送安全认证请求

应用可以在服务端AgentExtensionAbility组件的[onAuth()](../harmonyos-references/js-apis-app-agent-agentextensionability.md#onauth)方法中接收客户端的安全认证请求以及[AgentHostProxy](../harmonyos-references/js-apis-inner-application-agenthostproxy.md)对象，并且可以通过[AgentHostProxy](../harmonyos-references/js-apis-inner-application-agenthostproxy.md)的[authorize()](../harmonyos-references/js-apis-inner-application-agenthostproxy.md#authorize)方法向客户端发送安全认证请求。

```typescript
import { common, AgentExtensionAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class AgentExtAbility extends AgentExtensionAbility {
  // ...
  // 认证
  onAuth(proxy: common.AgentHostProxy, handshakeData: string) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onAuth');
    try {
      // 处理认证逻辑
      let authResult = 'auth success';
      proxy.authorize(authResult);
    } catch (err) {
      let code = (err as BusinessError).code;
      let msg = (err as BusinessError).message;
      console.error(`sendData failed, err code: ${code}, err msg: ${msg}.`);
    }
  }
  // ...
}
```
