---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1617
title: 如何实现通过手势涂抹选择文字的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现通过手势涂抹选择文字的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cbff79f31493a40ddfe8bbc33e8a311ae10815120854e5c9b3b1a61d291f2959
---

## 问题现象

如何实现通过手势涂抹选择文字的效果？

1. 涂抹过文字的选中。当反向涂抹选中的文字时，能够取消选中状态。
2. 单击某个选中的Text也能取消选中状态。
3. 当文字有多行时，涂抹到下一行某个位置，该位置之前的文字都被选中。同样地，反向涂抹选中的文字，能取消选中状态。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/1cabDG_1SW-s76ygYa8gtg/zh-cn_image_0000002658852647.gif "点击放大")

## 背景知识

* [绑定手势方法](../harmonyos-references/ts-gesture-settings.md)为组件绑定不同类型的手势事件，并设置事件的响应方法。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)组件区域变化时触发该回调，可用来获取组件长宽以及相对于父组件的坐标位置。
* [Flex](../harmonyos-references/ts-container-flex.md)是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。

## 解决方案

* 整体方案实现逻辑。
  1. 外层使用Flex弹性布局，内层使用Text组件显示文字。
  2. 使用onAreaChange获取所有Text组件相对于Flex的位置，用于后续判断手势是否滑过该文字。
  3. 监听Flex的手势事件，将手势滑过的坐标位置，与Text的所在位置比对，判断滑动选择的文字。
* 核心代码-数据处理解析。
  1. 创建textRects数组保存Text在Flex中的坐标，selectedStatus数组保存每个Text选取状态，upOrDown用来记录手指滑动方向。
  2. 在Flex长按滑动手势事件触发后，计算出当前手指所在Text的索引curIndex。与上次文本状态更新的最后索引endIndexOfLast比对，将索引在(endIndexOfLast,curIndex]左闭右开区间内的Text文本状态更新。
  3. 对特殊情况单独处理，如手指滑动区域不在Text文本范围内、手指下滑后转而上滑。

     ```ts
     @Entry
     @Component
     struct TextSelectionDemo {
       private textContents: number[] = new Array(64).fill(12);
       @State selectedStatus: boolean[] = new Array(this.textContents.length).fill(false); // textContents选中状态，1选中，0未选中
       private textRects: RectText[] = []; // 存储文本区域坐标
       endIndexOfLast: number = -1; // 记录上次滑动最后更新的文本索引
       upOrDown: number = 0; // 1手指下滑，2手指上滑，记录手指滑动状态，判断是否反向

       // 获取当前手势所在文本的索引
       touchItemIndex(touchX: number, touchY: number): number {
         // 检测触摸点是否在文本区域内
         let ret: number = -1;
         for (let index = 0; index < this.textContents.length; ++index) {
           const rect = this.textRects[index];
           if (rect &&
             touchX >= rect.left && touchX <= rect.right &&
             touchY >= rect.top && touchY <= rect.bottom) {
             ret = index;
           }
         }
         return ret;
       }

       updateSelectedIndexes(start: number, end: number) {
         // 过滤特殊情况：滑动非文本区域||在一个文本区域内滑动（文本会闪烁）
         if (end === -1 || start === end) {
           return;
         }
         console.info(`endIndex: ${start}, curIndex: ${end}`);
         // 手指刚按下滑动的情况
         if (start === -1) {
           this.selectedStatus[end] = !this.selectedStatus[end];
           this.upOrDown = 0;
           // 向下滑动
         } else if (start < end) {
           // 特殊情况：手指向上滑动转下滑
           if (this.upOrDown === 2) {
             this.selectedStatus[start] = !this.selectedStatus[start];
           }
           for (let index = start + 1; index <= end; index++) {
             this.selectedStatus[index] = !this.selectedStatus[index];
           }
           this.upOrDown = 1; // 手指滑动方向设置向下
           // 向上滑动
         } else if (start > end) {
           // 特殊情况：手指向下滑动转上滑
           if (this.upOrDown === 1) {
             this.selectedStatus[start] = !this.selectedStatus[start];
           }
           for (let index = start - 1; index >= end; index--) {
             this.selectedStatus[index] = !this.selectedStatus[index];
           }
           this.upOrDown = 2; // 手指滑动方向设置向上
         }
         this.endIndexOfLast = end; // 记录最后一个更新的文本
       }

       build() {
         Column() {
           Scroll() {
             // 可滑动选择的Flex容器
             Flex({ direction: FlexDirection.Row, wrap: FlexWrap.Wrap }) {
               ForEach(this.textContents, (item: number, index: number) => {
                 Text(`${index}${item}item`)
                   .fontSize(16)
                   .padding(10)
                   .borderRadius(8)
                   .backgroundColor(this.selectedStatus[index] ? '#E6F3FF' : '#F1F3F5')
                   .margin(5)
                   .onAreaChange((oldVal: Area, newVal: Area) => {
                     console.info(`oldVal：${oldVal} newVal：${newVal}`);
                     // 记录每个Text的布局区域
                     this.textRects[index] = {
                       left: newVal.position.x as number,
                       right: (newVal.position.x as number) + (newVal.width as number),
                       top: newVal.position.y as number,
                       bottom: (newVal.position.y as number) + (newVal.height as number)
                     };
                   })
                   .onClick(() => {
                     this.selectedStatus[index] = !this.selectedStatus[index];
                   });
               });
             }
             .gesture(
               GestureGroup(
                 GestureMode.Sequence,
                 LongPressGesture({ repeat: false }), // 长按手势
                 PanGesture({ fingers: 1 }) // 长按后滑动
                   .onActionStart((event: GestureEvent) => {
                     console.info(`${event.offsetX}, ${event.offsetY}`);
                   })
                   .onActionUpdate((event: GestureEvent) => {
                     let curIndex: number = this.touchItemIndex(event.fingerList[0].localX, event.fingerList[0].localY);
                     console.info(`endIndex: ${this.endIndexOfLast}, curIndex: ${curIndex}`);
                     this.updateSelectedIndexes(this.endIndexOfLast, curIndex);
                   })
                   .onActionEnd(() => {
                     this.endIndexOfLast = -1;
                     this.upOrDown = 0;
                   })
               )
             ).width('100%').padding(10);
           }.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
           .width('100%').height('100%');
         };
       }
     }

     interface RectText {
       left: number;
       right: number;
       top: number;
       bottom: number;
     }
     ```

     **说明** 

     要提取出选中的文本数据进行后续处理，只需遍历一遍文本选中状态数组selectedStatus即可。
* 效果预览：单独点击文本项选取和取消文本；长按之后滑动文本；对于已选取的文本，再次滑过则会取消选取状态。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/HJeZmygNR_-BX5ik_jaw5A/zh-cn_image_0000002628773284.gif "点击放大")
