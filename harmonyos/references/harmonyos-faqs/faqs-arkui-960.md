---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-960
title: stateStyles：多态样式如何设置不向父组件冒泡
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > stateStyles：多态样式如何设置不向父组件冒泡
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:7d8ef59b2e331dbc36441553c6b28bb39492c462857abe35c4be2c8b8cf01055
---

## 问题现象

stateStyles多态样式，父组件和子组件都设置了stateStyles，子组件满足stateStyles状态时，父组件也同样满足，也会跟着改变，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Jn6WxA_1SYaf8rHlhJOE6g/zh-cn_image_0000002663716957.png "点击放大")

* 蓝色背景为父组件，绿色背景为子组件。
* 子组件常态（normal）为绿色，按压态（pressed）为黄色。
* 父组件常态（normal）为蓝色，按压态（pressed）为灰色。
* 当前的效果是，按压子组件“Hello World2”，子组件会由绿色变为黄色，父组件也会由蓝色变为灰色；按压父组件区域，父组件会由蓝色变为灰色，子组件（Hello World2）不会变。
* 期望的效果是：按压子组件“Hello World2”，子组件由绿色变为黄色，父组件不变。

如何设置可以不向父组件冒泡，子组件改变不影响父组件？

## 背景知识

[stateStyles](../harmonyos-guides/arkts-statestyles.md)：多态样式，可以依据组件的内部状态的不同，快速设置不同样式。ArkUI提供以下六种状态：

* focused：获焦态。
* normal：正常态。
* pressed：按压态。
* disabled：不可用态。
* clicked：点击态。
* selected：选中态。

[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)：基础事件在响应链上的传递遵循冒泡机制，即最内层组件优先处理，再逐层往父组件传递该事件，任意一层组件可主动终止本次事件的继续传递，即终止冒泡（stopPropagation可终止冒泡）。但需要注意的是，终止冒泡并不会中断父组件对手势的响应处理。

[基础输入事件](../harmonyos-references/basic-raw-input-event.md)中，[触摸事件](../harmonyos-references/ts-universal-events-touch.md)由手指、手写笔或鼠标左键在组件上按下、滑动或抬起时触发。触摸事件默认冒泡，会被多个组件消费。

## 解决方案

在子组件绑定[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)回调，并在回调中通过stopPropagation方法阻止按下的事件传递到父组件，父组件不会变为按压态。

示例demo：

```ts
@Entry
@Component
struct StateStylesDemo {
  build() {
    Row() {
      Column() {
        Text('Hello World1')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold);

        Text('Hello World2')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .stateStyles({
            focused: {
              .backgroundColor('#ffffeef0');
            },
            pressed: {
              .backgroundColor('#F7CE00');
            },
            normal: {
              .backgroundColor('#ff50be33');
            }
          })
          .onTouch((event: TouchEvent) => {
            event.stopPropagation();
          });

        Text('Hello World3')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold);
      }
      .stateStyles({
        focused: {
          .backgroundColor('#ffffeef0');
        },
        pressed: {
          .backgroundColor(Color.Gray);
        },
        normal: {
          .backgroundColor('#ff2787d9');
        }
      })
      .justifyContent(FlexAlign.SpaceEvenly)
      .height('50%')
      .width('100%');
    }
    .height('100%')
    .width('100%');
  }
}
```

按压子组件后，不会触发父组件stateStyles的按压设置效果，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/DLAsk2IBR4eWUfaAz_upLQ/zh-cn_image_0000002663797649.png "点击放大")

## 总结

stopPropagation干预事件冒泡时，应注意对同一事件的不同类型（如Down/Move/Up）采用一致的规则，避免上层节点仅接收到部分类型事件，导致事件不闭环的情况，例如当节点仅接收到Down事件，而未接收到Up事件，这会影响节点上的事件完整性（对于指向性按下操作类交互产生的事件，确保事件的完整性是必要的）。
