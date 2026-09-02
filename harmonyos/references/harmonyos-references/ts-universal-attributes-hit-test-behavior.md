---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior
title: 触摸测试控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 触摸交互控制 > 触摸测试控制
category: harmonyos-references
scraped_at: 2026-09-02T15:00:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:791a2c86383d30f57a0d41917f7c93dbedce5839416e6653853a7736a934abdf
---

设置组件的[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)类型。在ArkUI开发框架中，处理触屏事件和鼠标事件时，会在事件触发前进行按压点与组件响应热区的触摸测试，以收集需响应事件的组件。基于测试结果，框架会分发相应的事件。hitTestBehavior属性用于设置不同的触摸测试响应模式，影响触摸测试收集结果及后续事件分发。具体影响参考[HitTestMode](ts-appendix-enums.md#hittestmode9)枚举说明。影响[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)、[拖拽事件](ts-universal-events-drag-drop.md)、[鼠标事件](ts-universal-mouse-key.md)、[轴事件](ts-universal-events-axis.md)、[悬浮事件](ts-universal-events-hover.md)、[无障碍悬浮事件](ts-universal-accessibility-hover-event.md)和[手势事件](ts-gesture-settings.md)的分发。

**说明** 

* 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 当Stack组件中有多个节点触摸区域重叠时，如果最上层节点的子组件命中，则默认只会对显示在最上层的节点做触摸测试。此时只有给显示在最上层的节点设置hitTestBehavior为HitTestMode.Transparent时，才能使显示在下层的节点触发触摸测试。
* 存在新增节点时，如需该节点响应触摸测试，需要对其设置[HitTestMode](ts-appendix-enums.md#hittestmode9)。当新增节点存在多层级节点时，仅需设置根节点的HitTestMode。

## hitTestBehavior

hitTestBehavior(value: HitTestMode): T

设置组件的触摸测试类型。如果组件不设置hitTestBehavior，其默认触摸测试类型为HitTestMode.Default。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [HitTestMode](ts-appendix-enums.md#hittestmode9) | 是 | 设置当前组件的触摸测试类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## 示例

### 示例1（触摸测试模式为Block和Transparent的触摸测试效果）

该示例通过设置不同的[HitTestMode](ts-appendix-enums.md#hittestmode9)值演示了Block和Transparent的触摸测试效果。

```ts
// xxx.ets
@Entry
@Component
struct HitTestBehaviorExample {
  build() {
    // outer stack
    Stack() {
      Button('outer button')
        .onTouch((event) => {
          console.info(`outer button touched type: ${(event as TouchEvent).type}`);
        })
      // inner stack
      Stack() {
        Button('inner button')
          .onTouch((event) => {
            console.info(`inner button touched type: ${(event as TouchEvent).type}`);
          })
      }
      .width('100%').height('100%')
      // 设置触摸测试类型为Block，自身响应触摸测试但阻止兄弟节点参与触摸测试
      .hitTestBehavior(HitTestMode.Block)
      .onTouch((event) => {
        console.info(`stack touched type: ${(event as TouchEvent).type}`);
      })

      Text('Transparent')
        // 设置触摸测试类型为Transparent，自身不拦截触摸测试，允许下层节点响应触摸测试
        .hitTestBehavior(HitTestMode.Transparent)
        .width('100%').height('100%')
        .onTouch((event) => {
          console.info(`text touched type: ${(event as TouchEvent).type}`);
        })
    }.width(300).height(300)
  }
}
```

### 示例2（触摸测试类型为BLOCK\_HIERARCHY时的触摸测试效果）

从API version 20开始，该示例演示了设置触摸测试类型为BLOCK\_HIERARCHY时的触摸测试效果。

```ts
// xxx.ets
@Entry
@Component
struct BlockHierarchy {
  build() {
    // outer stack
    Stack() {
      Stack() {
        Button('outer button')
          .onTouch((event) => {
            console.info(`HitTestMode outer button touched type: ${(event as TouchEvent).type}`);
          })
          .width(200)
          .height(200)
          .backgroundColor('#D5D5D5')
        // inner stack
        Stack() {
          Button()
            .id('button150')
            .backgroundColor('#F7F7F7')
            .width(150)
            .height(150)
            .onTouch((event) => {
              console.info(`HitTestMode button150 touched type: ${(event as TouchEvent).type}`);
            })
            .hitTestBehavior(HitTestMode.Transparent)
          Button()
            .id('button100')
            .backgroundColor('#707070')
            .width(100)
            .height(100)
            .onTouch((event) => {
              console.info(`HitTestMode button100 touched type: ${(event as TouchEvent).type}`);
            })
            .hitTestBehavior(HitTestMode.Transparent)
          Button()
            .id('button050')
            .backgroundColor('#D5D5D5')
            .width(50)
            .height(50)
            .onTouch((event) => {
              console.info(`HitTestMode button050 touched type: ${(event as TouchEvent).type}`);
            })
            .hitTestBehavior(HitTestMode.Transparent)
        }
        .width('100%').height('100%')
        // 设置触摸测试模式，自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试
        .hitTestBehavior(HitTestMode.BLOCK_HIERARCHY)
        .onTouch((event) => {
          console.info(`HitTestMode stack touched type: ${(event as TouchEvent).type}`);
        })

        Text('Transparent')
          .hitTestBehavior(HitTestMode.Transparent)
          .width('100%').height('100%')
          .onTouch((event) => {
            console.info(`HitTestMode text touched type: ${(event as TouchEvent).type}`);
          })
      }.width(300).height(300)
      .borderWidth(2)
      .onTouch((event) => {
        console.info(`HitTestMode father stack touched type: ${(event as TouchEvent).type}`);
      })
    }.width(500).height(500)
    .borderWidth(2)
    .onTouch((event) => {
      console.info(`HitTestMode grandfather stack touched type: ${(event as TouchEvent).type}`);
    })
  }
}
```

### 示例3（触摸测试类型为BLOCK\_DESCENDANTS时的触摸测试效果）

从API version 20开始，该示例演示了设置触摸测试类型为BLOCK\_DESCENDANTS时的触摸测试效果。

```ts
// xxx.ets
@Entry
@Component
struct BlockDescendants {
  build() {
    // outer stack
    Stack() {
      Stack() {
        Button('outer button')
          .onTouch((event) => {
            console.info(`HitTestMode outer button touched type: ${(event as TouchEvent).type}`);
          })
          .width(200)
          .height(200)
          .backgroundColor('#D5D5D5')
        // inner stack
        Stack() {
          Button('inner button')
            .width(100)
            .height(100)
            .onTouch((event) => {
              console.info(`HitTestMode inner button touched type: ${(event as TouchEvent).type}`);
            })
        }
        .width('100%').height('100%')
        // 设置触摸测试模式，自身不响应触摸测试，并且所有的后代（孩子、孙子等）也不响应触摸测试，不会影响祖先节点的触摸测试
        .hitTestBehavior(HitTestMode.BLOCK_DESCENDANTS)
        .onTouch((event) => {
          console.info(`HitTestMode stack touched type: ${(event as TouchEvent).type}`);
        })

        Text('Transparent')
          .hitTestBehavior(HitTestMode.Transparent)
          .width('100%').height('100%')
          .onTouch((event) => {
            console.info(`HitTestMode text touched type: ${(event as TouchEvent).type}`);
          })
      }.width(300).height(300)
      .borderWidth(2)
      .onTouch((event) => {
        console.info(`HitTestMode father stack touched type: ${(event as TouchEvent).type}`);
      })
    }.width(500).height(500)
    .borderWidth(2)
    .onTouch((event) => {
      console.info(`HitTestMode grandfather stack touched type: ${(event as TouchEvent).type}`);
    })
  }
}
```

### 示例4（Stack组件中多节点重合时的触摸测试效果）

该示例演示了在Stack组件中存在多节点触摸区域重叠时的触摸测试效果。此时设置[HitTestMode](ts-appendix-enums.md#hittestmode9)为None时，重叠的背景区域无法响应触摸测试；只有设置为Transparent时，背景区域才能响应触摸测试。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  @State @Watch('onModeChange') mode: number = HitTestMode.None;
  @State modeStr: string = 'None';

  onModeChange() {
    this.modeStr = this.mode === HitTestMode.None ? 'None' : 'Transparent';
  }

  build() {
    Stack() {
      Column()
        .height('100%')
        .width('100%')
        .onTouch(() => {
          console.info('background hit test!');
        })
      Stack() {
        // 点击按钮进行触摸测试
        Button('HitTest')
        // 点击按钮切换不同的触摸测试模式
        Button('HitTestMode: ' + this.modeStr)
          .margin({ top: 100 })
          .onClick(() => {
            this.mode = this.mode === HitTestMode.None ?
              HitTestMode.Transparent : HitTestMode.None;
          })
      }
      .height('100%')
      .width('100%')
      // 只有上层节点的HitTestMode设置为Transparent时，下层节点才能响应触摸测试
      .hitTestBehavior(this.mode)
    }
    .height('100%')
    .width('100%')
  }
}
```
