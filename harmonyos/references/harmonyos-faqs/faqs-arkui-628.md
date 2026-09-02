---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-628
title: 多层级布局，上层手势事件如何透传到下层控件
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 多层级布局，上层手势事件如何透传到下层控件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b8b1d1a46460074080dffbdae80a0475a3caaab01ffeef330886c05505d14547
---

## 问题现象

由于需要做视频播控手势，以下代码无法通过手势滑动屏幕控制音量、亮度和进度。

```ts
Stack() {
   Column() {
     // 组件B
   }
   .gesture(PanGesture()) // 期望能够透传到这个地方
   Column() {
     // 组件C，内部包含DEF三个组件，期望能够把这个手势事件透传给上边的组件
     Blank()
       .parallelGesture(null, GestureMask.IgnoreInternal) 
     this.bottom()
   }
   .parallelGesture(null, GestureMask.IgnoreInternal)
 }
```

如下层叠布局：B组件表示音量控制、亮度等下层组件，D/E/F表示上层组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/n33DMqgLRpGAjow1uRM9sw/zh-cn_image_0000002658793539.png "点击放大")

预期效果：组件D、E、F上的手势操作能够透传到B组件上控制音量、亮度变化等操作，而不执行C、D、E、F上的手势操作。

实际问题：手势操作只在上层D、E、F组件上适配，无法将手势操作透传给下层目标组件B。

## 背景知识

通过设置属性[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)控制多层级手势事件竞争流程。

* HitTestMode.Transparent：自身响应触摸测试，不会阻塞兄弟节点的触摸测试。
* HitTestMode.Block：自身会响应触摸测试，阻塞子节点和兄弟节点的触摸测试，从而导致子节点和兄弟节点的onTouch事件和手势均无法触发。
* HitTestMode.None：自身不响应触摸测试，不会阻塞子节点和兄弟节点的触摸测试。

## 解决方案

针对业务场景代码梳理UI层级，预期将上层手势响应事件不作处理透传到下层组件进行处理，根据hitTestBehavior类型说明，选择HitTestMode.None模式，达到上层不响应，传递至子节点响应。

上述场景实现代码：

```ts
@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column() {
        Column() {
          Text('ColumnB').margin({ top: 10 });
        }
        .onTouch(() => {
          console.info('Executing a gesture:ComponentB');
        })
        .gesture(TapGesture({ count: 1 }))
        .backgroundColor('#f1f3f5')
        .borderRadius(10)
        .width('90%')
        .height('90%');
      };

      // 组件C设置.hitTestBehavior(HitTestMode.None)，自身不响应触摸测试
      ComponentC()
        .onTouch(() => {
          console.info('Executing a gesture:ComponentC');
        })
        .gesture(TapGesture({ count: 1 }))
        .backgroundColor('#E5E5EA')
        .borderRadius(10)
        .width('80%')
        .height('80%')
        .hitTestBehavior(HitTestMode.None);
    }
    .onTouch(() => {
      console.info('Executing a gesture:StackA');
    })
    .gesture(TapGesture({ count: 1 }))
    .width('100%')
    .height('100%')
    .hitTestBehavior(HitTestMode.None);
  }
}

@Component
struct ComponentC {
  build() {
    Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
      Text('ColumnC')
        .width('100%')
        .textAlign(TextAlign.Center);
      Column() {
        Text('ColumnD')
          .margin({ top: 10 });
      }
      .onTouch(() => {
        console.info('Executing a gesture:ComponentD');
      })
      .gesture(TapGesture({ count: 1 }))
      .backgroundColor('#D1D1D6')
      .height('28%')
      .width('100%');

      // 组件E设置.hitTestBehavior(HitTestMode.None)，自身不响应触摸测试
      Column() {
        Text('ColumnE')
          .margin({ top: 10 });
      }
      .onTouch(() => {
        console.info('Executing a gesture:ComponentE');
      })
      .gesture(TapGesture({ count: 1 }))
      .backgroundColor('#C7C7CC')
      .height('28%')
      .width('100%')
      .hitTestBehavior(HitTestMode.None);

      Column() {
        Text('ColumnF')
          .margin({ top: 10 });
      }
      .onTouch(() => {
        console.info('Executing a gesture:ComponentF');
      })
      .gesture(TapGesture({ count: 1 }))
      .backgroundColor('#999999')
      .height('28%')
      .width('100%');

      Text('ColumnC')
        .width('100%')
        .textAlign(TextAlign.Center);
    }.width('100%')
    .height('100%')
    .hitTestBehavior(HitTestMode.None);
  }
}
```

如下效果图点击图中不同颜色区域的手势传递结果验证日志：

```txt
触摸D区域：
Executing a gesture:ComponentD
Executing a gesture:ComponentB

触摸E区域：
Executing a gesture:ComponentB

触摸F区域：
Executing a gesture:ComponentF
Executing a gesture:ComponentB

触摸C区域：
Executing a gesture:ComponentB

触摸B区域：
Executing a gesture:ComponentB

触摸A区域：无相关日志打印。
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/2lhM7RCaT-e5Mn0_cVMI3g/zh-cn_image_0000002628554172.png "点击放大")

## 总结

多层级UI布局手势操作，需要于设计过程中梳理对应的手势响应操作，hitTestBehavior属性可以实现在复杂的多层级场景下决定哪些组件可以响应手势和事件，完成业务场景中的手势传递。
