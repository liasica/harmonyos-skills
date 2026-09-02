---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-event-conflict-faq
title: 手势事件冲突常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 手势事件冲突常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:54+08:00
doc_updated_at: 2026-08-11
content_hash: sha256:b2e977d2ecd334dbe4af9f0db9dc5e2761ab44a9b2cca905dea0388ce596e2f8
---

## 滚动容器嵌套滚动容器事件冲突

1. Scroll组件嵌套List组件滑动事件冲突。

   Scroll组件嵌套List组件，子组件List组件的滑动手势优先级高于父组件Scroll的滑动手势，所以当List列表滚动时，不会响应Scroll组件的滚动事件，List不会和Scroll一起滚动。如果需要List和Scroll组件同步滚动可以使用[nestedScroll](../harmonyos-references/ts-container-list.md#nestedscroll10)属性来解决，设置向前向后两个方向上的嵌套滚动模式，实现与父组件的滚动联动。

   使用nestedScroll属性设置List组件的嵌套滚动方式，[NestedScrollMode](../harmonyos-references/ts-appendix-enums.md#nestedscrollmode10)设置成SELF\_FIRST时，List组件滚动到页面边缘后，父组件继续滚动。NestedScrollMode设置为PARENT\_FIRST时，父组件先滚动，滚动至边缘后通知List组件继续滚动。示例代码如下。

   ```ts
   @Entry
   @Component
   struct GesturesConflictScene1 {
     build() {
       Scroll() {
         Column() {
           Column()
             .height('30%')
             .width('100%')
             .backgroundColor(Color.Blue)
           List() {
             ForEach([1, 2, 3, 4, 5, 6], (item: string) => {
               ListItem() {
                 Text(item.toString())
                   .height(300)
                   .fontSize(50)
                   .fontWeight(FontWeight.Bold)
               }
             }, (item: number) => item.toString())
           }
           .edgeEffect(EdgeEffect.None)
           .nestedScroll({
             scrollForward: NestedScrollMode.PARENT_FIRST,
             scrollBackward: NestedScrollMode.SELF_FIRST
           })
           .height('100%')
           .width('100%')
         }
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. List、Scroller等滚动容器嵌套Web组件，滑动事件冲突。

   比如List组件嵌套Web组件，当Web加载的网页中也包含滚动视图的时候，这时候上下滚动Web组件，不能和List列表整体一起滑动。这是因为Web的滑动事件和List组件的冲突，如果想让Web随List一起整体滚动，解决方案和前面的例子一样，给Web组件添加[nestedScroll](../harmonyos-references/arkts-basic-components-web-attributes.md#nestedscroll11)属性。

   ```ts
   Web(
     // ...
   )
     .nestedScroll({
       scrollForward: NestedScrollMode.PARENT_FIRST,
       scrollBackward: NestedScrollMode.SELF_FIRST
     })
   ```

   具体实现可以参考：[Web组件嵌套滚动](web-nested-scrolling.md)。

## 使用组合手势同时绑定多个同类型手势冲突

例如给组件同时设置单击和双击的点击手势[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)，按如下方式设置会发现双击手势失效，这是因为在互斥识别的组合手势中，手势会按声明的顺序进行识别，若有一个手势识别成功，则结束手势识别。因为单击手势放在了前面，所以当双击的时候会优先识别了单击手势，单击成功后后面的双击回调就不会执行了。

```ts
@Entry
@Component
struct GesturesConflictScene2 {
  @State count1: number = 0;
  @State count2: number = 0;

  build() {
    Column() {
      Text('Exclusive gesture\n' + 'Click count is:' + this.count1 + '\nDouble click count is:' + this.count2 + '\n')
        .fontSize(28)
    }
    .height(200)
    .width('100%')
    .gesture(
      GestureGroup(GestureMode.Exclusive,
        TapGesture({ count: 1 })
          .onAction(() => {
            this.count1++;
          }),
        TapGesture({ count: 2 })
          .onAction(() => {
            this.count2++;
          })
      )
    )
  }
}
```

可以设置手势为并行识别来解决，设置对应的GestureMode为Parallel。

```ts
.gesture(
  GestureGroup(GestureMode.Parallel,
    TapGesture({ count: 2 })
      .onAction(() => {
        this.count2++;
      }),
    TapGesture({ count: 1 })
      .onAction(() => {
        this.count1++;
      })
  )
)
```

## 系统手势和自定义手势之间冲突

对于一般同类型的手势，系统手势优先于自定义手势执行，可以通过[priorityGesture](../harmonyos-references/ts-gesture-settings.md#prioritygesture)或者[parallelGesture](../harmonyos-references/ts-gesture-settings.md#parallelgesture)的方式来绑定自定义手势，例如下面这个示例。

图片长按手势响应失败或冲突，在Image控件上添加长按手势后，长按图片无法响应对应方法，而是图片放大的动画，示例代码如下。

```ts
@Entry
@Component
struct GesturesConflictScene3 {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Image($r('app.media.startIcon'))
          .margin({ top: 100 })
          .width(360)
          .height(360)
          .gesture(
            LongPressGesture({ repeat: true })
              .onAction((event: GestureEvent) => {
              })
              .onActionEnd(() => {
                try {
                  this.getUIContext().getPromptAction().showToast({ message: 'Long Press' });
                } catch (err) {
                  let error = err as BusinessError;
                  hilog.error(0x0000, 'testTag', `showToast err, code: ${error.code}, mesage: ${error.message}`);
                }
              })
          )
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

这是因为Image组件内置的长按动画和用户自定义的长按手势[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)冲突了。可以使用priorityGesture绑定手势的方式替代[gesture](../harmonyos-references/ts-gesture-settings.md#gesture)的方式，这样就会只响应自定义手势LongPressGesture了。如果需要两者都执行可以使用parallelGesture的绑定方式。

```ts
.priorityGesture(
  LongPressGesture({ repeat: true })
    .onAction((event: GestureEvent) => {
    })
    .onActionEnd(() => {
      try {
        this.getUIContext().getPromptAction().showToast({ message: 'Long Press' });
      } catch (err) {
        let error = err as BusinessError;
        hilog.error(0x0000, 'testTag', `showToast err, code: ${error.code}, mesage: ${error.message}`);
      }
    })
  )
```

## 手势事件透传

和触摸事件一样，手势事件也可以通过[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性来进行透传，例如下面这个示例，上层的Column组件设置hitTestBehavior属性为HitTestMode.None后，可以将滑动手势[SwipeGesture](../harmonyos-references/ts-basic-gestures-swipegesture.md)透传给被覆盖的Column组件。HitTestMode.None：自身不接收事件，但不会阻塞兄弟组件和子组件继续做触摸测试。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct GesturesConflictScene4 {
  build() {
    Stack() {
      Column()
        .width('100%')
        .height('100%')
        .backgroundColor(Color.Black)
        .gesture(
          SwipeGesture({ direction: SwipeDirection.Horizontal })
            .onAction((event) => {
              if (event) {
                try {
                  this.getUIContext().getPromptAction().showToast({ message: 'SwipeGesture' });
                } catch (err) {
                  let error = err as BusinessError;
                  hilog.error(0x0000, 'testTag', `showToast err, code: ${error.code}, mesage: ${error.message}`);
                }
              }
            })
        )
      Column()
        .width(300)
        .height(100)
        .backgroundColor(Color.Red)
        .hitTestBehavior(HitTestMode.None)
    }
    .width(300)
    .height(300)
  }
}
```

## 多点触控场景下手势冲突

当一个页面中有多个组件可以响应手势事件，在多个手指触控的情况下，多个组件可能会同时响应手势事件，从而导致业务异常。ArkUI提供了手势独占的属性[monopolizeEvents](../harmonyos-references/ts-universal-attributes-monopolize-events.md#monopolizeevents)，设置需要单独响应事件的组件的monopolizeEvents属性为true，可以解决这一问题。

例如下面这个示例，给按钮Button1设置了.monopolizeEvents(true)之后，当手指首先触摸在Button1之后，在手指离开之前，其它组件的手势和事件都不会触发。

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct GesturesConflictScene5 {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Row({ space: 20 }) {
        Button('Button1')
          .width(100)
          .height(40)
          .monopolizeEvents(true)
        Button('Button2')
          .width(200)
          .height(50)
          .onClick(() => {
              try {
                this.getUIContext().getPromptAction().showToast({ message: 'GesturesConflictScene5 Button2 click' });
              } catch (err) {
                let error = err as BusinessError;
                hilog.error(0x0000, 'testTag', `showToast err, code: ${error.code}, mesage: ${error.message}`);
              }
          })
      }
      .margin(20)

      Text(this.message)
        .margin(15)
    }
    .width('100%')
    .gesture(
      TapGesture({ count: 1 })
        .onAction(() => {
          console.info('GesturesConflictScene5 TapGesture onAction.');
        }),
    )
  }
}
```

## 动态控制自定义手势是否响应

在手势识别期间，开发者决定是否响应手势，例如下面的示例代码，通过[onGestureJudgeBegin](../harmonyos-references/ts-gesture-customize-judge.md#ongesturejudgebegin)回调方法在手势识别期间进行判定，当手势为GestureType.DRAG的时候，不响应该手势，所以会使定义的onDragStart事件失效。

```ts
@Entry
@Component
struct GesturesConflictScene6 {
  @State message: string = 'Hello World';

  build() {
    Column()
      .width('100%')
      .height(200)
      .backgroundColor(Color.Brown)
      .onDragStart(() => {
        console.info('GesturesConflictScene6 Drag start.');
      })
      .gesture(
        TapGesture({ count: 1 })
          .tag('tap1')
          .onAction(() => {
            console.info('GesturesConflictScene6 TapGesture onAction.');
          }),
      )
      .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
        if (gestureInfo.type === GestureControl.GestureType.LONG_PRESS_GESTURE) {
          let longPressEvent = event as LongPressGestureEvent;
          console.info('GesturesConflictScene6: ' + longPressEvent.repeat);
        }
        if (gestureInfo.type === GestureControl.GestureType.DRAG) {
          return GestureJudgeResult.REJECT;
        } else if (gestureInfo.tag === 'tap1' && event.pressure > 10) {
          return GestureJudgeResult.CONTINUE
        }
        return GestureJudgeResult.CONTINUE;
      })
  }
}
```

## 父组件如何管理子组件手势

父子组件嵌套滚动发生手势冲突，父组件有机制可以干预子组件的手势响应。下面例子介绍了如何使用[手势拦截增强](../harmonyos-references/ts-gesture-blocking-enhancement.md)，在外层Scroll组件的[shouldBuiltInRecognizerParallelWith](../harmonyos-references/ts-gesture-blocking-enhancement.md#shouldbuiltinrecognizerparallelwith)和[onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin)回调中，动态控制内外层Scroll手势事件的滚动。

1. 首先在父组件Scroll的[shouldBuiltInRecognizerParallelWith](../harmonyos-references/ts-gesture-blocking-enhancement.md#shouldbuiltinrecognizerparallelwith)方法中收集需做并行处理的手势。下面示例代码中收集到了子组件的手势识别器childRecognizer，使其和父组件的手势识别器currentRecognizer并行处理。
2. 调用onGestureRecognizerJudgeBegin方法，判断滚动组件是否滑动到顶部或者底部，做业务逻辑处理，通过动态控制手势识别器是否可用，来决定并行处理器的childRecognizer和currentRecognizer是否可用。

   ```ts
   @Entry
   @Component
   struct GesturesConflictScene7 {
     scroller: Scroller = new Scroller();
     scroller2: Scroller = new Scroller();
     private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
     private childRecognizer: GestureRecognizer = new GestureRecognizer();
     private currentRecognizer: GestureRecognizer = new GestureRecognizer();

     build() {
       Stack({ alignContent: Alignment.TopStart }) {
         Scroll(this.scroller) {
           Column() {
             Text('Scroll Area')
               .width('100%')
               .height(150)
               .backgroundColor(0xFFFFFF)
               .borderRadius(15)
               .fontSize(16)
               .textAlign(TextAlign.Center)
               .margin({ top: 10 })
             Scroll(this.scroller2) {
               Column() {
                 Text('Scroll Area2')
                   .width('100%')
                   .height(150)
                   .backgroundColor(0xFFFFFF)
                   .borderRadius(15)
                   .fontSize(16)
                   .textAlign(TextAlign.Center)
                   .margin({ top: 10 })
                 Column() {
                   ForEach(this.arr, (item: number) => {
                     Text(item.toString())
                       .width('100%')
                       .height(200)
                       .backgroundColor(0xFFFFFF)
                       .borderRadius(15)
                       .fontSize(20)
                       .textAlign(TextAlign.Center)
                       .margin({ top: 10 })
                   }, (item: string) => item)
                 }
                 .width('100%')
               }
             }
             .id('innerScroll')
             .scrollBar(BarState.Off)
             .width('100%')
             .height(800)
           }.width('100%')
         }
         .id('outerScroll')
         .height(600)
         .scrollBar(BarState.Off)
         .shouldBuiltInRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
           for (let i = 0; i < others.length; i++) {
             let target = others[i].getEventTargetInfo();
             if (target) {
               if (target.getId() === 'innerScroll' && others[i].isBuiltIn() &&
                 others[i].getType() === GestureControl.GestureType.PAN_GESTURE) {
                 this.currentRecognizer = current;
                 this.childRecognizer = others[i];
                 return others[i];
               }
             }
           }
           return undefined;
         })
         .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
           others: Array<GestureRecognizer>) => {
           if (current) {
             let target = current.getEventTargetInfo();
             if (target) {
               if (target.getId() === 'outerScroll' && current.isBuiltIn() &&
                 current.getType() === GestureControl.GestureType.PAN_GESTURE) {
                 if (others) {
                   for (let i = 0; i < others.length; i++) {
                     let target = others[i].getEventTargetInfo() as ScrollableTargetInfo;
                       if (target instanceof ScrollableTargetInfo && target.getId() == 'innerScroll') {
                       let panEvent = event as PanGestureEvent;
                       if (target.isEnd()) {
                         if (panEvent && panEvent.offsetY < 0) {
                           this.childRecognizer.setEnabled(false)
                           this.currentRecognizer.setEnabled(true)
                         } else {
                           this.childRecognizer.setEnabled(true)
                           this.currentRecognizer.setEnabled(false)
                         }
                       } else if (target.isBegin()) {
                         if (panEvent.offsetY > 0) {
                           this.childRecognizer.setEnabled(false)
                           this.currentRecognizer.setEnabled(true)
                         } else {
                           this.childRecognizer.setEnabled(true)
                           this.currentRecognizer.setEnabled(false)
                         }
                       } else {
                         this.childRecognizer.setEnabled(true)
                         this.currentRecognizer.setEnabled(false)
                       }
                     }
                   }
                 }
               }
             }
           }
           return GestureJudgeResult.CONTINUE;
         })
       }
       .width('100%')
       .height('100%')
       .backgroundColor(0xF1F3F5)
       .padding(12)
     }
   }
   ```
