---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-gesture-judge
title: 手势冲突处理
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 添加手势响应 > 手势冲突处理
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ec321645e14a6a4b613fa87477fed588fa8f2209809cb3a953d9c8c60d7d5452
---

手势冲突是指多个手势识别器在同一组件或重叠区域同时识别时产生竞争，导致识别结果不符合预期。常见冲突场景包括：

* 同一组件上的多手势（如按钮同时添加点击与长按手势）。
* 父子组件的同类型手势识别器。
* 系统默认手势与自定义手势（如[Scroll](../harmonyos-references/ts-container-scroll.md)滑动手势与子组件点击手势冲突）。

干预手势处理可有效解决冲突，除控制组件响应热区和命中测试模式外，主要通过以下四种方式：[自定义手势判定](arkts-gesture-events-gesture-judge.md#自定义手势判定)、[手势并行动态控制](arkts-gesture-events-gesture-judge.md#手势并行动态控制)、[阻止手势参与识别](arkts-gesture-events-gesture-judge.md#阻止手势参与识别)、[自定义干预事件和手势的收集结果](arkts-gesture-events-gesture-judge.md#自定义干预事件和手势的收集结果)。

## 自定义手势判定

自定义手势判定是指在系统判定阈值已满足的条件下，应用可自行判断是否应拦截该手势，使该手势识别失败，从而将识别成功的机会留给其他手势。

**图1** 自定义手势判定流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/hY6W26SBQUOjzFmwbWw3IA/zh-cn_image_0000002712243996.png)

自定义手势判定涉及以下接口。

| 接口 | 说明 |
| --- | --- |
| [onGestureJudgeBegin](../harmonyos-references/ts-gesture-customize-judge.md#ongesturejudgebegin) | 用于手势拦截，是通用事件。在手势满足系统触发阈值场景下，回调给应用判断是否拦截手势。 |
| [onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin) | 用于手势拦截、获取手势识别器和设置手势识别器开闭状态。是onGestureJudgeBegin接口的能力扩展，可以代替onGestureJudgeBegin接口。  获取手势识别器时，会获取一次交互中手势响应链上的所有手势识别器，以及当前即将触发成功的手势识别器，此时可以设置手势的激活状态。 |

以下示例中，Image和Stack两个组件位于同一区域。长按Stack组件的上半部分可触发挂载在Stack组件上的长按手势，长按Stack组件的下半部分则会响应Image组件的拖拽操作。

**图2** 示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/RvyAme5kTtiG_ZKEgrRyCA/zh-cn_image_0000002742002949.png)

1. Image组件设置拖拽。

   ```typescript
   // $r('sys.media.ohos_app_icon') 需要替换为开发者所需的资源文件
   Image($r('sys.media.ohos_app_icon'))
     .draggable(true)
     .onDragStart(()=>{
       // ...
       // 请将$r('app.string.Allow_dragging_prompt')替换为实际资源文件，在本示例中该资源文件的value值为"Drag 下半区蓝色区域，Image响应"
       promptAction.showToast({ message: $r('app.string.Allow_dragging_prompt') });
     })
     .width('200vp').height('200vp')
   ```
2. Stack组件设置手势。

   ```typescript
   Stack() {}
   .width('200vp')
   .height('200vp')
   .hitTestBehavior(HitTestMode.Transparent)
   .gesture(GestureGroup(GestureMode.Parallel,
     LongPressGesture()
       .onAction((event: GestureEvent) => {
         // ...
         /*
         请将$r('app.string.Stop_dragging_prompt')替换为实际资源文件，在本示例中
         该资源文件的value值为"LongPressGesture 长按上半区 灰色区域，灰色区域响应"
          */
         promptAction.showToast({ message: $r('app.string.Stop_dragging_prompt')  });
       })
       .tag('longPress')
   ))
   ```
3. Stack组件设置拦截。

   ```typescript
   .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
     // 如果是长按类型手势，判断点击的位置是否在上半区
     if (gestureInfo.type == GestureControl.GestureType.LONG_PRESS_GESTURE) {
       if (event.fingerList.length > 0 && event.fingerList[0].localY < 100) {
         return GestureJudgeResult.CONTINUE;
       } else {
         return GestureJudgeResult.REJECT;
       }
     };
     return GestureJudgeResult.CONTINUE;
   })
   ```
4. 代码完整示例。

   ```typescript
   import { PromptAction } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     scroller: Scroller = new Scroller();
     promptAction: PromptAction = this.getUIContext().getPromptAction();

     build() {
       Scroll(this.scroller) {
         Column({ space: 8 }) {
           /*
           请将$r('app.string.Drag_instructions')替换为实际资源文件，在本示例中该资源文件的value值为"包括上下两层组件，上层组件绑定长按手势，
           下层组件绑定拖拽。其中上层组件下半区域绑定手势拦截，使该区域响应下层拖拽手势。"
            */
           Text($r('app.string.Drag_instructions')).width('100%').fontSize(20).fontColor('#ffdd00')
           Stack({ alignContent: Alignment.Center }) {
             Column() {
               // 模拟上半区和下半区
               Stack().width('200vp').height('100vp').backgroundColor(Color.Gray)
               Stack().width('200vp').height('100vp').backgroundColor(Color.Blue)
             }.width('200vp').height('200vp')

             // Stack的下半区是绑定了拖拽手势的图像区域。
             // $r('sys.media.ohos_app_icon') 需要替换为开发者所需的资源文件
             Image($r('sys.media.ohos_app_icon'))
               .draggable(true)
               .onDragStart(() => {
                 // 请将$r('app.string.Allow_dragging_prompt')替换为实际资源文件，在本示例中该资源文件的value值为"Drag 下半区蓝色区域，Image响应"
                 try {
                   this.promptAction.showToast({ message: $r('app.string.Allow_dragging_prompt') });
                 } catch (error) {
                   console.error('ShowToast failed!')
                 }
               })
               .width('200vp').height('200vp')
             // Stack的上半区是绑定了长按手势的浮动区域。
             Stack() {
             }
             .width('200vp')
             .height('200vp')
             .hitTestBehavior(HitTestMode.Transparent)
             .gesture(GestureGroup(GestureMode.Parallel,
               LongPressGesture()
                 .onAction(() => {
                   /*
                   请将$r('app.string.Stop_dragging_prompt')替换为实际资源文件，在本示例中
                   该资源文件的value值为"LongPressGesture 长按上半区 灰色区域，灰色区域响应"
                    */
                   try {
                     this.promptAction.showToast({ message: $r('app.string.Stop_dragging_prompt') });
                   } catch (error) {
                     console.error('ShowToast failed!')
                   }
                 })
                 .tag('longPress')
             ))
             .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
               // 如果是长按类型手势，判断点击的位置是否在上半区
               if (gestureInfo.type == GestureControl.GestureType.LONG_PRESS_GESTURE) {
                 if (event.fingerList.length > 0 && event.fingerList[0].localY < 100) {
                   return GestureJudgeResult.CONTINUE;
                 } else {
                   return GestureJudgeResult.REJECT;
                 }
               };
               return GestureJudgeResult.CONTINUE;
             })
           }.width('100%')
         }.width('100%')
       }
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/ETJaR_6PQGCFOnQ3hgxbhA/zh-cn_image_0000002712403962.png)

## 手势并行动态控制

手势并行动态控制指的是手势已经成功识别，但是开发者仍然可以通过调用API接口控制手势回调是否能够响应。

**图3** 手势并行动态控制流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/NzFI2eZ8QaWUWfAVbNwCeA/zh-cn_image_0000002742122911.png)

手势并行动态控制的前提是手势识别成功，如果手势不成功则不会产生手势回调响应。

1. 业务手势作业流：指真正触发UI变化的业务手势，比如使页面滚动的[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)，触发点击的[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)等。
2. 监听手势作业流：指在监听手势运行的过程中，应根据上下文的业务状态变化动态控制手势识别器的开闭，例如判断组件嵌套滚动过程中是否已滑至边缘。这一监听事件可借助一个使用[并行手势绑定方式](arkts-gesture-events-binding.md#parallelgesture并行手势绑定方法)的PanGesture实现，或者采用Touch事件来完成。
3. 设置手势并行：此步骤并非必需，典型场景是在嵌套滚动中，设置外部组件的滚动手势与内部的滚动手势并行。
4. 动态开闭手势：指通过手势识别器的setEnabled方法，控制手势是否响应用户回调。

### 内置手势并行动态控制

内置手势并行动态控制涉及以下接口。

| 接口 | 说明 |
| --- | --- |
| [shouldBuiltInRecognizerParallelWith](../harmonyos-references/ts-gesture-blocking-enhancement.md#shouldbuiltinrecognizerparallelwith) | 用于设置系统组件内置手势与其他手势并行。 |
| [onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin) | 用于手势拦截，获取手势识别器，初始化手势识别器开闭状态。 |
| [parallelGesture](arkts-gesture-events-binding.md#parallelgesture并行手势绑定方法) | 可使开发者定义的手势，与比它优先级高的手势并行。 |

以下示例在两个[Scroll](../harmonyos-references/ts-container-scroll.md)组件的嵌套滚动场景下，使用手势控制的接口控制外部组件和内部组件的嵌套滚动联动。

1. 使用shouldBuiltInRecognizerParallelWith接口设置外部Scroll组件的PanGesture手势与内部Scroll组件的PanGesture手势并行。

   ```typescript
   .shouldBuiltInRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
     for (let i = 0; i < others.length; i++) {
       let target = others[i].getEventTargetInfo();
       if (target.getId() == 'inner' && others[i].isBuiltIn() && others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
         this.currentRecognizer = current; // 保存当前组件的识别器
         this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
         return others[i]; // 返回和当前手势将要组成并行手势的识别器
       };
     };
     return undefined;
   })
   ```
2. 使用onGestureRecognizerJudgeBegin接口获取到Scroll组件的PanGesture手势识别器，同时根据内外Scroll组件的边界条件，设置内外手势的开闭状态。

   ```typescript
   .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
     others: Array<GestureRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
     let target = current.getEventTargetInfo();
     if (target && target.getId() == 'outer' && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
       for (let i = 0; i < others.length; i++) {
         let target = others[i].getEventTargetInfo() as ScrollableTargetInfo;
         if (target instanceof ScrollableTargetInfo && target.getId() == 'inner') { // 找到响应链上对应并行的识别器
           let panEvent = event as PanGestureEvent;
           this.childRecognizer.setEnabled(true);
           this.currentRecognizer.setEnabled(false);
           if (target.isEnd()) { // 根据当前组件状态以及移动方向动态控制识别器使能状态
             if (panEvent && panEvent.offsetY < 0) {
               this.childRecognizer.setEnabled(false);
               this.currentRecognizer.setEnabled(true);
             };
           } else if (target.isBegin()) {
             if (panEvent.offsetY > 0) {
               this.childRecognizer.setEnabled(false);
               this.currentRecognizer.setEnabled(true);
             };
           };
         };
       };
     };
     return GestureJudgeResult.CONTINUE;
   })
   ```
3. 设置监听手势，监听Scroll组件状态，动态调整手势开闭状态，控制手势回调是否触发，从而控制Scroll是否滚动。

   ```typescript
   .parallelGesture( // 绑定一个Pan手势作为动态控制器
     PanGesture()
       .onActionUpdate((event: GestureEvent)=>{
         if (this.childRecognizer.getState() != GestureRecognizerState.SUCCESSFUL ||
           this.currentRecognizer.getState() != GestureRecognizerState.SUCCESSFUL) { // 如果识别器状态不是SUCCESSFUL，则不做控制
           return;
         };
         let target = this.childRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
         let currentTarget = this.currentRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
         if (target instanceof ScrollableTargetInfo && currentTarget instanceof ScrollableTargetInfo) {
           this.childRecognizer.setEnabled(true);
           this.currentRecognizer.setEnabled(false);
           if (target.isEnd()) { // 在移动过程中实时根据当前组件状态，控制识别器的开闭状态
             if ((event.offsetY - this.lastOffset) < 0) {
               this.childRecognizer.setEnabled(false);
               if (currentTarget.isEnd()) {
                 this.currentRecognizer.setEnabled(false);
               } else {
                 this.currentRecognizer.setEnabled(true);
               };
             };
           } else if (target.isBegin()) {
             if ((event.offsetY - this.lastOffset) > 0) {
               this.childRecognizer.setEnabled(false);
               if (currentTarget.isBegin()) {
                 this.currentRecognizer.setEnabled(false);
               } else {
                 this.currentRecognizer.setEnabled(true);
               };
             };
           };
         };
         this.lastOffset = event.offsetY;
       })
   )
   ```
4. 代码完整示例。

   ```typescript
   // xxx.ets
   @Entry
   @Component
   struct FatherControlChild {
     scroller: Scroller = new Scroller();
     scroller2: Scroller = new Scroller();
     private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
     private childRecognizer: GestureRecognizer = new GestureRecognizer();
     private currentRecognizer: GestureRecognizer = new GestureRecognizer();
     private lastOffset: number = 0;

     build() {
       Stack({ alignContent: Alignment.TopStart }) {
         Scroll(this.scroller) { // 外部滚动容器
           Column() {
             Text('Scroll Area')
               .width('90%')
               .height(150)
               .backgroundColor(0xFFFFFF)
               .borderRadius(15)
               .fontSize(16)
               .textAlign(TextAlign.Center)
               .margin({ top: 10 })
             Scroll(this.scroller2) { // 内部滚动容器
               Column() {
                 Text('Scroll Area2')
                   .width('90%')
                   .height(150)
                   .backgroundColor(0xFFFFFF)
                   .borderRadius(15)
                   .fontSize(16)
                   .textAlign(TextAlign.Center)
                   .margin({ top: 10 })
                 Column() {
                   ForEach(this.arr, (item: number) => {
                     Text(item.toString())
                       .width('90%')
                       .height(150)
                       .backgroundColor(0xFFFFFF)
                       .borderRadius(15)
                       .fontSize(16)
                       .textAlign(TextAlign.Center)
                       .margin({ top: 10 })
                   }, (item: string) => item)
                 }.width('100%')
               }
             }
             .id('inner')
             .width('100%')
             .height(800)
           }.width('100%')
         }
         .id('outer')
         .height(600)
         .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
         .scrollBar(BarState.On) // 滚动条常驻显示
         .scrollBarColor(Color.Gray) // 滚动条颜色
         .scrollBarWidth(10) // 滚动条宽度
         .edgeEffect(EdgeEffect.None)
         .shouldBuiltInRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
           for (let i = 0; i < others.length; i++) {
             let target = others[i].getEventTargetInfo();
             if (target.getId() == 'inner' && others[i].isBuiltIn() &&
               others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
               this.currentRecognizer = current; // 保存当前组件的识别器
               this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
               return others[i]; // 返回和当前手势将要组成并行手势的识别器
             }
           }
           return undefined;
         })
         .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
           others: Array<GestureRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
           let target = current.getEventTargetInfo();
           if (target && target.getId() == 'outer' && current.isBuiltIn() &&
             current.getType() == GestureControl.GestureType.PAN_GESTURE) {
             for (let i = 0; i < others.length; i++) {
               let target = others[i].getEventTargetInfo() as ScrollableTargetInfo;
               if (target instanceof ScrollableTargetInfo && target.getId() == 'inner') { // 找到响应链上对应并行的识别器
                 let panEvent = event as PanGestureEvent;
                 this.childRecognizer.setEnabled(true);
                 this.currentRecognizer.setEnabled(false);
                 if (target.isEnd()) { // 根据当前组件状态以及移动方向动态控制识别器使能状态
                   if (panEvent && panEvent.offsetY < 0) {
                     this.childRecognizer.setEnabled(false);
                     this.currentRecognizer.setEnabled(true);
                   }
                 } else if (target.isBegin()) {
                   if (panEvent.offsetY > 0) {
                     this.childRecognizer.setEnabled(false);
                     this.currentRecognizer.setEnabled(true);
                   }
                 }
               }
             }
           }
           return GestureJudgeResult.CONTINUE;
         })
         .parallelGesture( // 绑定一个Pan手势作为动态控制器
           PanGesture()
             .onActionUpdate((event: GestureEvent) => {
               if (this.childRecognizer?.getState() != GestureRecognizerState.SUCCESSFUL ||
                 this.currentRecognizer?.getState() != GestureRecognizerState.SUCCESSFUL) { // 如果识别器状态不是SUCCESSFUL，则不做控制
                 return;
               }
               let target = this.childRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
               let currentTarget = this.currentRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
               if (target instanceof ScrollableTargetInfo && currentTarget instanceof ScrollableTargetInfo) {
                 this.childRecognizer.setEnabled(true);
                 this.currentRecognizer.setEnabled(false);
                 if (target.isEnd()) { // 在移动过程中实时根据当前组件状态，控制识别器的开闭状态
                   if ((event.offsetY - this.lastOffset) < 0) {
                     this.childRecognizer.setEnabled(false);
                     if (currentTarget.isEnd()) {
                       this.currentRecognizer.setEnabled(false);
                     } else {
                       this.currentRecognizer.setEnabled(true);
                     };
                   };
                 } else if (target.isBegin()) {
                   if ((event.offsetY - this.lastOffset) > 0) {
                     this.childRecognizer.setEnabled(false)
                     if (currentTarget.isBegin()) {
                       this.currentRecognizer.setEnabled(false);
                     } else {
                       this.currentRecognizer.setEnabled(true);
                     };
                   };
                 };
               };
               this.lastOffset = event.offsetY;
             })
         )
       }.width('100%').height('100%').backgroundColor(0xDCDCDC)
     }
   }
   ```

### 非内置手势并行动态控制

从API版本26.0.0开始，可以使用shouldRecognizerParallelWith接口设置非内置手势与其他手势并行。

非内置手势并行动态控制涉及以下接口。

| 接口 | 说明 |
| --- | --- |
| [shouldRecognizerParallelWith](../harmonyos-references/ts-gesture-blocking-enhancement.md#shouldrecognizerparallelwith) | 用于设置组件非内置手势与其他手势并行。 |
| [onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin) | 用于获取手势识别器，再通过控制手势识别器开闭状态拦截手势。 |

以下示例在嵌套滚动场景下，使用手势控制的接口控制外部的Column组件和内部的Scroll组件的嵌套滚动联动。

1. 使用shouldRecognizerParallelWith接口设置外部Column组件的非内置PanGesture手势与内部Scroll组件的内置PanGesture手势并行。

   ```typescript
   .shouldRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
     for (let i = 0; i < others.length; i++) {
       let target = others[i].getEventTargetInfo();
       if (target) {
         if (target.getId() == 'inner' && others[i].isBuiltIn() &&
           others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
           this.currentRecognizer = current; // 保存当前组件的识别器
           this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
           return others[i]; // 返回将要组成并行手势的识别器
         }
       }
     }
     return undefined;
   })
   ```
2. 使用onGestureRecognizerJudgeBegin接口获取到Column和Scroll组件的PanGesture手势识别器，同时根据内外组件的边界条件，设置内外手势的开闭状态。

   ```typescript
   .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
     others: Array<GestureRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
     let target = current.getEventTargetInfo();
     if (target && target.getId() == 'outer' &&
       current.getType() == GestureControl.GestureType.PAN_GESTURE) {
       for (let i = 0; i < others.length; i++) {
         let target = others[i].getEventTargetInfo();
         if (target instanceof ScrollableTargetInfo && target.getId() == 'inner') { // 找到响应链上对应并行的识别器
           let panEvent = event as PanGestureEvent;
           if (target.isEnd()) { // 根据当前组件状态以及移动方向动态控制识别器使能状态
             if (panEvent && panEvent.offsetY < 0) {
               this.childRecognizer.setEnabled(false);
               this.currentRecognizer.setEnabled(true);
             } else {
               this.childRecognizer.setEnabled(true);
               this.currentRecognizer.setEnabled(false);
             }
           } else if (target.isBegin()) {
             if (panEvent.offsetY > 0) {
               this.childRecognizer.setEnabled(false);
               this.currentRecognizer.setEnabled(true);
             } else {
               this.childRecognizer.setEnabled(true);
               this.currentRecognizer.setEnabled(false);
             }
           } else {
             this.childRecognizer.setEnabled(true);
             this.currentRecognizer.setEnabled(false);
           }
         }
       }
     }
     return GestureJudgeResult.CONTINUE;
   })
   ```
3. 代码完整示例。

   ```typescript
   @Entry
   @Component
   struct CustomGestureControlGroup {
     @State offsetY: number = 0
     scroller2: Scroller = new Scroller();
     private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
     private childRecognizer: GestureRecognizer = new GestureRecognizer();
     private currentRecognizer: GestureRecognizer = new GestureRecognizer();
     private lastOffset: number = 0;

     build() {
       Stack({ alignContent: Alignment.TopStart }) {
         Column() { // 外部滚动容器
           Column() {
             Text('Scroll Area')
               .width('90%')
               .height(150)
               .backgroundColor(0xFFFFFF)
               .borderRadius(15)
               .fontSize(16)
               .textAlign(TextAlign.Center)
               .margin({ top: 10 })
             Scroll(this.scroller2) { // 内部滚动容器
               Column() {
                 Text('Scroll Area2')
                   .width('90%')
                   .height(150)
                   .backgroundColor(0xFFFFFF)
                   .borderRadius(15)
                   .fontSize(16)
                   .textAlign(TextAlign.Center)
                   .margin({ top: 10 })
                 Column() {
                   ForEach(this.arr, (item: number) => {
                     Text(item.toString())
                       .width('90%')
                       .height(150)
                       .backgroundColor(0xFFFFFF)
                       .borderRadius(15)
                       .fontSize(16)
                       .textAlign(TextAlign.Center)
                       .margin({ top: 10 })
                   }, (item: string) => item)
                 }.width('100%')
               }
             }
             .id('inner')
             .width('100%')
             .height(800)
           }
           .width('100%')
           .offset({ y: -this.offsetY })
         }
         .id('outer')
         .height(600)
         .clip(true)
         .gesture(
           PanGesture()
             .onActionStart((event: GestureEvent) => {
               this.lastOffset = this.offsetY // 手势开始时，记录当前滚动位置
             })
             .onActionUpdate((event: GestureEvent) => {
               let moveY = event.offsetY; // 手势移动时，计算新位置
               let targetOffset = this.lastOffset - moveY; // 目标位置 = 初始位置 - 移动距离
               this.offsetY = Math.max(0, Math.min(360, targetOffset));
             })
         )
         .shouldRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
           for (let i = 0; i < others.length; i++) {
             let target = others[i].getEventTargetInfo();
             if (target) {
               if (target.getId() == 'inner' && others[i].isBuiltIn() &&
                 others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
                 this.currentRecognizer = current; // 保存当前组件的识别器
                 this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
                 return others[i]; // 返回将要组成并行手势的识别器
               }
             }
           }
           return undefined;
         })
         .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
           others: Array<GestureRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
           let target = current.getEventTargetInfo();
           if (target && target.getId() == 'outer' &&
             current.getType() == GestureControl.GestureType.PAN_GESTURE) {
             for (let i = 0; i < others.length; i++) {
               let target = others[i].getEventTargetInfo();
               if (target instanceof ScrollableTargetInfo && target.getId() == 'inner') { // 找到响应链上对应并行的识别器
                 let panEvent = event as PanGestureEvent;
                 if (target.isEnd()) { // 根据当前组件状态以及移动方向动态控制识别器使能状态
                   if (panEvent && panEvent.offsetY < 0) {
                     this.childRecognizer.setEnabled(false);
                     this.currentRecognizer.setEnabled(true);
                   } else {
                     this.childRecognizer.setEnabled(true);
                     this.currentRecognizer.setEnabled(false);
                   }
                 } else if (target.isBegin()) {
                   if (panEvent.offsetY > 0) {
                     this.childRecognizer.setEnabled(false);
                     this.currentRecognizer.setEnabled(true);
                   } else {
                     this.childRecognizer.setEnabled(true);
                     this.currentRecognizer.setEnabled(false);
                   }
                 } else {
                   this.childRecognizer.setEnabled(true);
                   this.currentRecognizer.setEnabled(false);
                 }
               }
             }
           }
           return GestureJudgeResult.CONTINUE;
         })
       }.width('100%').height('100%').backgroundColor(0xDCDCDC)
     }
   }
   ```

## 阻止手势参与识别

手势识别基于[触摸测试](arkts-interaction-basic-principles.md#触摸测试)的响应链结果进行，因此在用户按下时，通过控制响应链中手势识别器的参与状态，实现高效的动态干预手势处理。

从API version 20开始，可以结合[onTouchTestDone](../harmonyos-references/ts-gesture-blocking-enhancement.md#ontouchtestdone20)接口来阻止手势参与识别。完成触摸测试后，系统通过该接口回调返回所有手势识别器对象。应用可根据类型、组件标识或关联组件信息筛选识别器，并通过调用[preventBegin](../harmonyos-references/ts-gesture-common.md#preventbegin20)接口主动禁用特定识别器。

根据手势类型进行禁用：

```typescript
.onTouchTestDone((event, recognizers) => {
  for (let i = 0; i < recognizers.length; i++) {
    let recognizer = recognizers[i];
    // 根据类型禁用所有滑动手势
    if (recognizer.getType() == GestureControl.GestureType.PAN_GESTURE) {
      recognizer.preventBegin();
    };
  };
})
```

根据手势所归属的组件禁用：

组件需要提前通过通用属性[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)配置组件标识。

```typescript
.onTouchTestDone((event, recognizers) => {
  for (let i = 0; i < recognizers.length; i++) {
    let recognizer = recognizers[i];
    // 禁用掉标识为myID的组件上的所有手势
    if (recognizer.getEventTargetInfo().getId() == 'myID') {
      recognizer.preventBegin();
    };
  };
})
```

根据是否系统内置手势禁用：

```typescript
.onTouchTestDone((event, recognizers) => {
  for (let i = 0; i < recognizers.length; i++) {
    let recognizer = recognizers[i];
    // 禁用掉所有系统内置的手势
    if (recognizer.isBuiltIn()) {
      recognizer.preventBegin();
    };
  };
})
```

根据具体情况组合使用这些条件。

**说明** 

系统由内向外执行节点上的onTouchTestDone回调。

在NDK中onTouchTestDone与preventBegin对应的接口分别为[OH\_ArkUI\_SetTouchTestDoneCallback](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_settouchtestdonecallback)和[OH\_ArkUI\_PreventGestureRecognizerBegin](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_preventgesturerecognizerbegin)，它们的使用方式及功能与ArkTS接口一致。

以下通过一个简化的视频播放界面交互为例来说明具体的用法：

父容器（video\_layer）绑定了多种手势：

* 点击：控制暂停/播放。
* 双击：切换全屏。
* 长按：快进。
* 上下滑动：调节亮度。
* 左右滑动：调整进度。

其内部下方的Slider组件（progress\_layer）未绑定长按手势，导致用户长按Slider时会触发父容器的快进手势，不符合预期。

解决方案：在Slider上注册onTouchTestDone回调，通过该回调禁用非Slider组件的手势识别器，即可解决冲突。

以下为完整示例代码：

```typescript
@Entry
@ComponentV2
struct Index {
  @Local progress: number = 496000; // 初始进度，毫秒
  @Local total: number = 27490000; // 总时长，毫秒
  @Local currentWidth: string = '100%';
  @Local currentHeight: string = '100%';
  @Local playbackProgress: string = '';
  private currentPosX: number = 0;
  private currentPosY: number = 0;
  private currentFullScreenState: boolean = true;
  private normalPlayTimer: number = -1;
  private isPlaying: boolean = true;
  private fastForwardTimer: number = -1;
  private context = this.getUIContext().getHostContext()

  aboutToAppear(): void {
    // 请将$r('app.string.Playback_progress')替换为实际资源文件，在本示例中该资源文件的value值为"播放进度"
    try {
      this.playbackProgress = this.context!.resourceManager.getStringSync($r('app.string.Playback_progress').id);
    } catch (error) {
      console.error('Get play back progress failed!');
    }
    // 启动一个周期性定时器每隔一秒刷新一次进度
    this.startNormalPlayTimer();
  };

  startNormalPlayTimer(): void {
    if (this.normalPlayTimer != -1) {
      this.stopNormalPlayTimer()
    };
    this.normalPlayTimer = setInterval(() => {
      this.progress = this.progress + 1000
    }, 1000);
  };

  stopNormalPlayTimer(): void {
    if (this.normalPlayTimer == -1) {
      return;
    };
    clearInterval(this.normalPlayTimer);
    this.normalPlayTimer = -1;
  };

  startFastForwardTimer(): void {
    if (this.fastForwardTimer != -1) {
      this.stopFastForwardTimer();
    };
    this.fastForwardTimer = setInterval(() => {
      this.progress = this.progress + 100000;
    }, 100);
  };

  stopFastForwardTimer(): void {
    if (this.fastForwardTimer == -1) {
      return;
    };
    clearInterval(this.fastForwardTimer);
    this.fastForwardTimer = -1;
  };

  showMessage(message: string): void {
    try {
      this.getUIContext().getPromptAction().showToast({ message: message, alignment: Alignment.Center });
    } catch (error) {
      console.error('ShowToast failed!');
    }
  };

  resetPosInfo(): void {
    this.currentPosX = 0;
    this.currentPosY = 0;
  };

  toggleFullScreenState(): void {
    this.currentFullScreenState = !this.currentFullScreenState;
    if (this.currentFullScreenState) {
      this.currentWidth = '100%';
      this.currentHeight = '100%';
    } else {
      this.currentWidth = '100%';
      this.currentHeight = '50%';
    };
    // 请将$r('app.string.Play_full_screen')替换为实际资源文件，在本示例中该资源文件的value值为"全屏播放"
    // 请将$r('app.string.Exit_play_full_screen')替换为实际资源文件，在本示例中该资源文件的value值为"取消全屏播放"
    try {
      this.showMessage(this.currentFullScreenState
        ? this.context!.resourceManager.getStringSync($r('app.string.Play_full_screen').id)
        : this.context!.resourceManager.getStringSync($r('app.string.Exit_play_full_screen').id));
    } catch (error) {
      console.error('GetStringSync failed!');
    }
  };

  togglePlayAndPause(): void {
    this.isPlaying = !this.isPlaying;
    if (!this.isPlaying) {
      this.stopNormalPlayTimer();
    } else {
      // 重新启动
      this.startNormalPlayTimer();
    };
    // 请将$r('app.string.stop_playing')替换为实际资源文件，在本示例中该资源文件的value值为"暂停播放"
    // 请将$r('app.string.Continue_playing')替换为实际资源文件，在本示例中该资源文件的value值为"继续播放"
    try {
      this.showMessage(this.isPlaying
        ? this.context!.resourceManager.getStringSync($r('app.string.stop_playing').id)
        : this.context!.resourceManager.getStringSync($r('app.string.Continue_playing').id));
    } catch (error) {
      console.error('GetStringSync failed!');
    }
  };

  doFastForward(start: boolean): void {
    if (!start) { // 停止快进，恢复正常播放
      this.stopFastForwardTimer();
      this.startNormalPlayTimer();
      // 请将$r('app.string.Cancel_FastForwarding')替换为实际资源文件，在本示例中该资源文件的value值为"取消快进"
      try {
        this.showMessage(
          this.context!.resourceManager.getStringSync($r('app.string.Cancel_FastForwarding').id));
      } catch (error) {
        console.error('GetStringSync failed!');
      }
      return;
    };

    this.stopNormalPlayTimer();
    this.startFastForwardTimer();
    // 请将$r('app.string.Start_FastForwarding')替换为实际资源文件，在本示例中该资源文件的value值为"开始快进"
    try {
      this.showMessage(
        this.context!.resourceManager.getStringSync($r('app.string.Start_FastForwarding').id));
    } catch (error) {
      console.error('GetStringSync failed!');
    }
  };

  updateBrightness(start: boolean, event: BaseGestureEvent): void {
    let newY = event.fingerList[0].localY;
    if (start) {
      this.currentPosY = newY;
      // 请将$r('app.string.Start_adjusting_brightness')替换为实际资源文件，在本示例中该资源文件的value值为"开始调整 亮度"
      try {
        this.showMessage(this.context!.resourceManager
          .getStringSync($r('app.string.Start_adjusting_brightness').id));
      } catch (error) {
        console.error('GetStringSync failed!');
      }
      return;
    };
    let offsetY = newY - this.currentPosY;
    if (Math.abs(offsetY) > 10) {
      // 请将$r('app.string.Reduce_brightness')替换为实际资源文件，在本示例中该资源文件的value值为"降低亮度"
      // 请将$r('app.string.Increase_brightness')替换为实际资源文件，在本示例中该资源文件的value值为"提高亮度"
      try {
        this.showMessage((offsetY > 0)
          ? this.context!.resourceManager.getStringSync($r('app.string.Reduce_brightness').id)
          : this.context!.resourceManager.getStringSync($r('app.string.Increase_brightness').id))
      } catch (error) {
        console.error('GetStringSync failed!');
      }
      this.currentPosY = newY;
    };
  };

  updateProgress(start: boolean, event: BaseGestureEvent): void {
    let newX = event.fingerList[0].localX;
    if (start) {
      this.currentPosX = newX;
      // 请将$r('app.string.Adjust_schedule')替换为实际资源文件，在本示例中该资源文件的value值为"开始调整 进度"
      try {
        this.showMessage(this.context!.resourceManager
          .getStringSync($r('app.string.Adjust_schedule').id));
      } catch (error) {
        console.error('GetStringSync failed!');
      }
      return;
    };
    let offsetX = newX - this.currentPosX;
    this.progress = Math.floor(this.progress + offsetX * 10000);
    this.currentPosX = newX;
  };

  build() {
    Stack({ alignContent: Alignment.Center }) {
      Column() {
        Column() {
          Text(this.playbackProgress + this.progress)
        }
        .width('100%').height('90%')

        Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
          Slider({
            value: this.progress,
            min: 0,
            max: this.total,
            style: SliderStyle.OutSet
          })
            .onChange((value: number, mode: SliderChangeMode) => {
              this.progress = value;
            })
            .id('progress_layer')
            .onTouchTestDone((event, allRecognizers: Array<GestureRecognizer>) => {
              for (let i = 0; i < allRecognizers.length; i++) {
                let recognizer = allRecognizers[i];
                let inspectorInfo = recognizer.getEventTargetInfo().getId();
                if (inspectorInfo !== 'progress_layer') {
                  // 用户操作到进度条区域时，禁用掉所有非progress_layer上的手势
                  recognizer.preventBegin();
                };
              };
            })
            .margin({ left: 5 })
            .trackColor(Color.Blue)
            .blockColor(Color.Gray)
            .selectedColor(Color.White)
            .trackThickness(2)
            .flexShrink(1)
            .flexGrow(1)
        }
        .flexGrow(1)
        .flexShrink(1)
        .id('id_progress_view')
      }
    }
    .id('video_layer')
    .backgroundColor('#E0E0E0')
    .gesture(
      GestureGroup(GestureMode.Exclusive,
        PanGesture({ direction: PanDirection.Vertical, distance: 10 })
          .tag('pan_for_brightness_control')
          .onActionStart((event) => {
            this.updateBrightness(true, event);
          })
          .onActionUpdate((event) => {
            this.updateBrightness(false, event);
          }),
        PanGesture({ direction: PanDirection.Horizontal, distance: 10 })
          .tag('pan_for_play_progress_control')
          .onActionStart((event) => {
            this.updateProgress(true, event);
          })
          .onActionUpdate((event) => {
            this.updateProgress(false, event);
          }),

        LongPressGesture()
          .tag('long_press_for_fast_forward_control')
          .onAction(() => {
            this.doFastForward(true); // 开始快进
          })
          .onActionEnd(() => {
            this.doFastForward(false); // 停止快进
          })
          .onActionCancel(() => {
            this.doFastForward(false);
          }),

        TapGesture({ count: 2 })
          .tag('double_tap_on_video')
          .onAction(() => {
            this.toggleFullScreenState();
          }),

        TapGesture()
          .tag('single_tap_on_video')
          .onAction(() => {
            this.togglePlayAndPause();
          })
      )
    )
    .width(this.currentWidth)
    .height(this.currentHeight)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/-paRXmbZRh6tCWt7UtqWDQ/zh-cn_image_0000002712243998.gif)

## 自定义干预事件和手势的收集结果

从API版本26.0.0开始，在手势、触摸事件发起时，系统会收集已绑定手势和触摸识别器的识别结果。开发者可以通过onGestureCollectIntercept回调对收集结果进行干预，通过返回不同的干预策略来动态控制识别结果的收集行为，例如阻止触摸事件向父组件透传、丢弃当前节点的手势等。

手势收集干预涉及以下接口。

| 接口 | 说明 |
| --- | --- |
| [onGestureCollectIntercept](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturecollectintercept) | 在当前节点及更高优先级节点上的事件和手势被收集完成后触发该回调。回调返回干预策略，控制后续收集流程。 |
| [getUniqueId](../harmonyos-references/ts-gesture-common.md#getuniqueid) | 通过识别器的[getEventTargetInfo()](../harmonyos-references/ts-gesture-common.md#geteventtargetinfo12)获取的组件信息对象上调用，返回当前组件的唯一数字ID，可用于与其他组件的唯一ID进行比对。 |
| [isHostBelongsTo](../harmonyos-references/ts-gesture-common.md#ishostbelongsto) | 判断当前手势或触摸识别器绑定的节点是否为指定组件的后代节点。传入组件的唯一ID，返回布尔值。该接口在[GestureRecognizer](../harmonyos-references/ts-gesture-common.md#gesturerecognizer12)和[TouchRecognizer](../harmonyos-references/ts-gesture-common.md#touchrecognizer20)上均可调用。 |

下面通过示例介绍如何实现自定义干预事件和手势的收集结果。示例中构建了如下组件树。

```mermaid
graph TD
    A((outerColumn))
    B((innerColumn))
    C((Row))
    D((Button1))
    E((Button2))

    A --> B
    A --> C
    C --> D
    C --> E
```

Button1未绑定点击事件，Button2绑定了点击事件。当用户点击Button2时，innerColumn上的onGestureCollectIntercept回调会对触摸识别器进行干预，阻止触摸事件继续向outerColumn透传；点击Button1时则允许正常透传。

1. 在innerColumn组件上绑定onGestureCollectIntercept回调，在回调中获取触摸识别器列表。

   ```typescript
   .onGestureCollectIntercept((recognizers: Array<GestureRecognizer>,
     touchRecognizers?: Array<TouchRecognizer> | undefined) => {
     if (!touchRecognizers) {
       return GestureCollectIntervention.CONTINUE;
     }
     // 遍历所有触摸识别器，获取目标组件信息
     for (let i = 0; i < touchRecognizers.length; i++) {
       let touchRecognizer = touchRecognizers[i];
       let targetInfo = touchRecognizer.getEventTargetInfo();
       let uniqueId = targetInfo.getUniqueId();
       // 使用 isHostBelongsTo 判断识别器是否属于 innerColumn 的后代
       if (touchRecognizer.isHostBelongsTo(uniqueId)) {
         console.info('Touch belongs to innerColumn subtree');
       }
       if (targetInfo.getId() == 'button2') {
         // 丢弃低优先级节点的收集，阻止事件透传到 outerColumn
         return GestureCollectIntervention.DISCARD_LOWER;
       }
     }
     return GestureCollectIntervention.CONTINUE;
   })
   ```
2. 代码完整示例。

   ```typescript
   @Entry
   @Component
   struct InterceptGestureCollection {
     @State backgroundColorButton1: string = '#D5D5D5';
     @State backgroundColorButton2: string = '#D5D5D5';
     @State backgroundColorRow: string = '#FFFFFF';
     @State backgroundColorColumn: string = '#FFFFFF';

     build() {
       Column() {
         Column() {
           Row() {
             Button('button1')
               .width('30%')
               .height(40)
               .id('button1')
               .onTouch((e?: TouchEvent) => {
                 this.backgroundColorButton1 = '#E5E5E5';
               })
               .backgroundColor(this.backgroundColorButton1)
             Button('button2')
               .width('30%')
               .height(40)
               .id('button2')
               .onTouch((e?: TouchEvent) => {
                 this.backgroundColorButton2 = '#E5E5E5';
               })
               .onClick((e?: ClickEvent) => {
                 console.info('button2 is clicked')
               })
               .backgroundColor(this.backgroundColorButton2)
           }
           .id('row')
           .justifyContent(FlexAlign.Center)
           .width('90%')
           .height(200)
           .margin(25)
           .onTouch((e?: TouchEvent) => {
             this.backgroundColorRow = '#666666';
           })
           .backgroundColor(this.backgroundColorRow)
         }
         .id('innerColumn')
         .margin(25)
         .padding(20)
         .width('90%')
         .height(250)
         .borderWidth(2)
         .onGestureCollectIntercept((recognizers: Array<GestureRecognizer>,
           touchRecognizers?: Array<TouchRecognizer> | undefined) => {
           if (!touchRecognizers) {
             return GestureCollectIntervention.CONTINUE;
           }
           // 遍历所有触摸识别器，获取目标组件信息
           for (let i = 0; i < touchRecognizers.length; i++) {
             let touchRecognizer = touchRecognizers[i];
             let targetInfo = touchRecognizer.getEventTargetInfo();
             let uniqueId = targetInfo.getUniqueId();
             // 使用 isHostBelongsTo 判断识别器是否属于 innerColumn 的后代
             if (touchRecognizer.isHostBelongsTo(uniqueId)) {
               console.info('Touch belongs to innerColumn subtree');
             }
             if (targetInfo.getId() == 'button2') {
               // 丢弃低优先级节点的收集，阻止事件透传到 outerColumn
               return GestureCollectIntervention.DISCARD_LOWER;
             }
           }
           return GestureCollectIntervention.CONTINUE;
         })
       }
       .id('outerColumn')
       .padding(15)
       .onTouch((e?: TouchEvent) => {
         this.backgroundColorColumn = '#E5E5E5';
       })
       .backgroundColor(this.backgroundColorColumn)
     }
   }
   ```

经过上述处理后，点击Button2时，onGestureCollectIntercept返回DISCARD\_LOWER，触摸事件不会透传至outerColumn；点击Button1时，返回CONTINUE，触摸事件正常透传，outerColumn响应变色。
