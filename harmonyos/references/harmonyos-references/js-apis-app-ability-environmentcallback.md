---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback
title: "@ohos.app.ability.EnvironmentCallback (系统环境变化监听器)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.EnvironmentCallback (系统环境变化监听器)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e628fb32349daaa8abf6b73b96dba03fe6b82a242840210234bd3a079d949e38
---

EnvironmentCallback模块提供对系统环境变化监听回调的能力。

**说明** 

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { EnvironmentCallback } from '@kit.AbilityKit';
```

## EnvironmentCallback

### onConfigurationUpdated

onConfigurationUpdated(config: Configuration): void

注册系统环境变化的监听[ApplicationContext.on('environment')](js-apis-inner-application-applicationcontext.md#applicationcontextonenvironment)后，在系统环境变化时触发回调。

**说明** 

onConfigurationUpdated回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务。因此，不建议在该回调中释放UI组件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [Configuration](js-apis-app-ability-configuration.md) | 是 | 变化后的Configuration对象。 |

**示例：**

参见[EnvironmentCallback使用](js-apis-app-ability-environmentcallback.md#environmentcallback使用)。

### onMemoryLevel

onMemoryLevel(level: AbilityConstant.MemoryLevel): void

注册系统环境变化的监听[ApplicationContext.on('environment')](js-apis-inner-application-applicationcontext.md#applicationcontextonenvironment)后，在系统内存变化时触发回调。

**说明** 

onMemoryLevel回调运行在当前进程的主线程中，如果在该回调中做耗时的UI组件释放，会阻塞主线程任务。因此，不建议在该回调中释放UI组件。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [AbilityConstant.MemoryLevel](js-apis-app-ability-abilityconstant.md#memorylevel) | 是 | 整机可用内存级别，对应的触发场景详见[AbilityConstant.MemoryLevel](js-apis-app-ability-abilityconstant.md#memorylevel)。 |

**示例：**

参见[EnvironmentCallback使用](js-apis-app-ability-environmentcallback.md#environmentcallback使用)。

## EnvironmentCallback使用

**示例：**

```ts
import { UIAbility, EnvironmentCallback } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callbackId: number;

export default class MyAbility extends UIAbility {
  onCreate() {
    console.info('MyAbility onCreate');
    let environmentCallback: EnvironmentCallback  =  {
      onConfigurationUpdated(config){
        console.info(`onConfigurationUpdated config: ${JSON.stringify(config)}`);
      },

      onMemoryLevel(level){
        console.info(`onMemoryLevel level: ${JSON.stringify(level)}`);
      }
    };
    // 1.获取applicationContext
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2.通过applicationContext注册系统环境变化监听
      callbackId = applicationContext.on('environment', environmentCallback);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
    console.info(`registerEnvironmentCallback number: ${JSON.stringify(callbackId)}`);
  }

  onDestroy() {
    let applicationContext = this.context.getApplicationContext();
    try {
      applicationContext.off('environment', callbackId, (error, data) => {
        if (error && error.code !== 0) {
          console.error(`unregisterEnvironmentCallback fail, error: ${JSON.stringify(error)}`);
        } else {
          console.info(`unregisterEnvironmentCallback success, data: ${JSON.stringify(data)}`);
        }
      });
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
  }
}
```
