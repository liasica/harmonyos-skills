---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-event
title: "@Event：规范组件输出"
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V2装饰器 > @Event：规范组件输出
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0cbea0894298b3c16ea726852a42005e85826715cfc1b3a44f8f519c197583f6
---

@Event装饰回调方法，用于[状态管理V2](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)中，作为自定义组件的输出。@Event通常与[@Param](ts-state-management-param.md)配合使用，@Param负责由父组件向子组件传递数据，@Event负责定义子组件向父组件传递消息的回调接口，适用于需要在子组件中触发父组件状态变更或事件处理的场景。

开发指南参考：[@Event：规范组件输出](../harmonyos-guides/arkts-new-event.md)。

**说明** 

从API version 12开始，支持该装饰器。

## @Event

const Event: PropertyDecorator

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
@Entry
@ComponentV2
struct Index {
  @Local name: string = 'Tom';

  build() {
    Column() {
      Child({
        name: this.name,
        changeFactory: (type: number) => {
          // @Event装饰的函数，在实现中修改父组件中的状态变量
          if (type == 1) {
            this.name = 'Tom';
          } else if (type == 2) {
            this.name = 'Jerry';
          }
        }
      })
    }
  }
}

@ComponentV2
struct Child {
  @Param name: string = '';
  // @Event装饰函数，用于向父组件传递消息
  @Event changeFactory: (type: number) => void = (type: number) => {};

  build() {
    Column() {
      Text(`name: ${this.name}`)
      Button('change to Tom')
        .onClick(() => {
          this.changeFactory(1);
        })
      Button('change to Jerry')
        .onClick(() => {
          this.changeFactory(2);
        })
    }
  }
}
```
