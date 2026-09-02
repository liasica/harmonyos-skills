---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-syncmonitor
title: "@SyncMonitor：状态变量修改同步监听"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V2装饰器 > @SyncMonitor：状态变量修改同步监听
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ea61dc0b44490f2502d4865656ad352092308de4bd35667a6b0b61fb12f1d7ad
---

@SyncMonitor用于[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)，同步监听状态变量修改，使得状态变量支持深度监听。适用于需要精确监听对象嵌套属性变化、数组元素修改等深层状态变化的场景，解决了传统监听方式无法感知深层属性变化的问题，提升状态管理的精确性和开发效率。

开发指南参考：[@SyncMonitor装饰器：状态变量修改同步监听](../harmonyos-guides/arkts-new-syncmonitor.md)。

**说明** 

从API version 23开始，支持该装饰器。

## @SyncMonitor

const SyncMonitor: MonitorDecorator

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [MonitorDecorator](ts-state-management-monitor.md#monitordecorator) | @SyncMonitor装饰器类型。 |

**错误码：**

以下错误码的详细介绍请参见[状态管理错误码](errorcode-statemanagement.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 130001 | The path is invalid. |

**示例：**

```ts
@Entry
@ComponentV2
struct Index {
  @Local message: string = 'Hello World';
  @Local name: string = 'Tom';

  // 使用@SyncMonitor同时监听message和name的变化
  @SyncMonitor('message', 'name')
  onStrChange(monitor: IMonitor) {
    monitor.dirty.forEach((path: string) => {
      console.info(`${path} changed from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`);
    });
  }

  build() {
    Column() {
      Text(`message: ${this.message}`)
      Text(`name: ${this.name}`)
      Button('change string')
        .onClick(() => {
          // 修改message，同步触发onStrChange回调
          this.message += '!';
          // 修改name，同步触发onStrChange回调
          this.name = 'Jack';
        })
    }
  }
}
```
