---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1204
title: 如何跨Text组件选择文本
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何跨Text组件选择文本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:43c2c7bd6b95c52b374eb59c701552f4498f512dd8d1c7b7eb4f6afdc101776a
---

## 问题现象

使用多个Text组件时，如何跨组件选中文本。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/QpFlLpriT7SeQY_HyThicA/zh-cn_image_0000002658832831.png "点击放大")

## 背景知识

* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)用于给组件添加滑动手势事件，通过onActionStart、onActionUpdate、onActionEnd来判断当前手势状态。
* [getLayoutManager](../harmonyos-references/ts-basic-components-text.md#getlayoutmanager12)：调用文本的布局管理对象获取文本信息。
* [getRectsForRange](../harmonyos-references/ts-text-common.md#getrectsforrange14)：获取给定的矩形区域宽度以及矩形区域高度的规格下，文本中任意区间范围内的字符或占位符所占的绘制区域信息。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。

## 解决方案

实现思路：通过自定义光标组件结合手势事件，调整文本选区范围，并通过Canvas绘制区域高亮，实现跨Text组件选择文本。

1. 自定义光标组件，并绑定了PanGesture，处理拖动事件，更新光标位置并调整选中区域：

   ```ts
   // 自定义光标组件
   @Builder
   caretBuilder(info: CaretInfo) {
     Column() {
       Column()
         .width(1.5)
         .height(22)
         .backgroundColor('rgba(10, 89, 247, 1)');
       Column()
         .width(19)
         .aspectRatio(1)
         .border({ width: 2, color: 'rgba(10, 89, 247, 1)', radius: 10 });
     }
     .position(info.position)
     // 拖拽时更新贯标位置
     .gesture(
       PanGesture()
         .onActionStart(() => {
           this.lastStartCaretPosition = this.startCaretInfo.position;
           this.lastEndCaretPosition = this.endCaretInfo.position;
         })
         .onActionUpdate(event => {
           this.getCaretInfo(event.fingerList[event.fingerList.length - 1].globalX,
             event.fingerList[event.fingerList.length - 1].globalY - this.TOP_HEIGHT, info);
           if (this.startCaretInfo.lessThan(this.endCaretInfo)) {
             this.getTextInfos(this.startCaretInfo, this.endCaretInfo);
           } else {
             this.getTextInfos(this.endCaretInfo, this.startCaretInfo);
           }
         })
     );
   }
   ```
2. 调用getTextInfos来获取选中的文本区域信息，最后通过paint方法在Canvas上绘制高亮，实现跨Text组件选择文本：

   ```ts
   // 历起始和结束位置之间的列表项，获取每个项的选区矩形，计算光标的位置，并调用paint进行绘制。
   getTextInfos(start: CaretInfo, end: CaretInfo) {
     this.textInfos = [];
     for (let i = start.listItemIndex; i <= end.listItemIndex; i++) {
       let itemRect = this.scroller.getItemRect(i);
       let startIndex = start.listItemIndex == i ? start.caretIndex : 0;
       let endIndex = end.listItemIndex == i ? end.caretIndex : this.data[i].length;
       let layoutManager = this.controllers[i].getLayoutManager();
       let rects = this.getRectForRange(startIndex, endIndex, layoutManager);
       this.textInfos.push(new TextInfo(i, itemRect, rects, startIndex, endIndex, this.yOffset));
     }
     if (this.textInfos.length <= 0) {
       return;
     }
     let startCaretPosition = this.textInfos[0].getPosition(false);
     let endCaretPosition = this.textInfos[this.textInfos.length - 1].getPosition();
     if (startCaretPosition) {
       start.position = startCaretPosition;
     }
     if (endCaretPosition) {
       end.position = endCaretPosition;
     }
     this.paint();
   }
   ```

完整示例参考如下：

```ts
import text from '@ohos.graphics.text';
import { common2D } from '@kit.ArkGraphics2D';
import { window } from '@kit.ArkUI';
import cryptoFramework from '@ohos.security.cryptoFramework';

class TextInfo {
  index: number;
  itemRect: RectResult;
  textRects: common2D.Rect[] = [];
  start: number;
  end: number;
  yOffset: number;

  constructor(index: number, itemRect: RectResult, textRects: common2D.Rect[], start: number, end: number,
    yOffset: number) {
    this.index = index;
    this.itemRect = itemRect;
    this.textRects = textRects;
    this.start = start;
    this.end = end;
    this.yOffset = yOffset;
  }

  getPosition(isEnd: boolean = true): Position | undefined {
    if (this.textRects.length <= 0) {
      return;
    }
    if (isEnd) {
      return {
        x: this.itemRect.x + this.textRects[this.textRects.length - 1].right - 10,
        y: this.itemRect.y + this.textRects[this.textRects.length - 1].top
      };
    } else {
      return { x: this.itemRect.x + this.textRects[0].left - 10, y: this.itemRect.y + this.textRects[0].top };
    }
  }
}

@ObservedV2
class CaretInfo {
  listItemIndex: number = -1;
  caretIndex: number = -1;
  @Trace position: Position = { x: -100, y: -100 };

  lessThan(another: CaretInfo) {
    return !(this.listItemIndex > another.listItemIndex) &&
      (this.listItemIndex < another.listItemIndex || this.caretIndex < another.caretIndex);
  }
}

@Entry
@Component
export struct ListSelectText {
  private startCaretInfo: CaretInfo = new CaretInfo();
  private endCaretInfo: CaretInfo = new CaretInfo();
  private lastStartCaretPosition: Position = { x: -100, y: -100 };
  private lastEndCaretPosition: Position = { x: -100, y: -100 };
  @State data: string[] = [];
  private controllers: TextController[] = [];
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private scroller = new Scroller();
  private textInfos: TextInfo[] = [];
  private TOP_HEIGHT: number = 0;
  private yOffset: number = 0;
  private random: cryptoFramework.Random = cryptoFramework.createRandom();

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      let randData = this.random.generateRandomSync(3);
      let length: number = Math.floor(randData.data[0] / 255 * 200) + 1;
      let text: string = '';
      for (let j = 0; j < length; j++) {
        text += '啊';
      }
      this.data.push(text);
      this.controllers.push(new TextController());
    }
    window.getLastWindow(this.getUIContext().getHostContext())
      .then(win => {
        this.TOP_HEIGHT =
          this.getUIContext().px2vp(win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
      });
  }

  // 自定义光标组件
  @Builder
  caretBuilder(info: CaretInfo) {
    Column() {
      Column()
        .width(1.5)
        .height(22)
        .backgroundColor('rgba(10, 89, 247, 1)');
      Column()
        .width(19)
        .aspectRatio(1)
        .border({ width: 2, color: 'rgba(10, 89, 247, 1)', radius: 10 });
    }
    .position(info.position)
    // 拖拽时更新贯标位置
    .gesture(
      PanGesture()
        .onActionStart(() => {
          this.lastStartCaretPosition = this.startCaretInfo.position;
          this.lastEndCaretPosition = this.endCaretInfo.position;
        })
        .onActionUpdate(event => {
          this.getCaretInfo(event.fingerList[event.fingerList.length - 1].globalX,
            event.fingerList[event.fingerList.length - 1].globalY - this.TOP_HEIGHT, info);
          if (this.startCaretInfo.lessThan(this.endCaretInfo)) {
            this.getTextInfos(this.startCaretInfo, this.endCaretInfo);
          } else {
            this.getTextInfos(this.endCaretInfo, this.startCaretInfo);
          }
        })
    );
  }

  // 获取文本中字符位置
  getTextIndex(x: number, y: number, layoutManager: LayoutManager) {
    let lineCount = layoutManager.getLineCount();
    let lineNum: number = -1;
    for (let i = 0; i < lineCount; i++) {
      let lineMetrics = layoutManager.getLineMetrics(i);
      if (y >= this.getUIContext().px2vp(lineMetrics.topHeight) &&
        y <= this.getUIContext().px2vp(lineMetrics.topHeight + lineMetrics.height)) {
        lineNum = i;
        break;
      }
    }
    let line = layoutManager.getLineMetrics(lineNum);
    let textIndex: number = -1;
    if (x >= this.getUIContext().px2vp(line.left + line.width)) {
      return line.endIndex + 1;
    }
    for (let i = line.startIndex; i < line.endIndex; i++) {
      let rects = this.getRectForRange(i, line.endIndex, layoutManager);
      if (x < rects[0].left) {
        textIndex = i - 1;
        break;
      }
    }
    return textIndex;
  }

  getCaretInfo(x: number, y: number, info: CaretInfo): void {
    let listIndex = this.scroller.getItemIndex(x, y);
    if (listIndex < 0) {
      return;
    }
    let itemRect = this.scroller.getItemRect(listIndex);
    let layoutManager = this.controllers[listIndex].getLayoutManager();
    let textIndex = this.getTextIndex(x - itemRect.x, y - itemRect.y, layoutManager);
    info.listItemIndex = listIndex;
    info.caretIndex = textIndex;
  }

  getRectForRange(start: number, end: number, layoutManager: LayoutManager) {
    return layoutManager.getRectsForRange({ start: start, end: end }, text.RectWidthStyle.TIGHT,
      text.RectHeightStyle.TIGHT).map((item): common2D.Rect => {
      return {
        left: this.getUIContext().px2vp(item.rect.left),
        right: this.getUIContext().px2vp(item.rect.right),
        top: this.getUIContext().px2vp(item.rect.top),
        bottom: this.getUIContext().px2vp(item.rect.bottom)
      };
    });
  }

  // 历起始和结束位置之间的列表项，获取每个项的选区矩形，计算光标的位置，并调用paint进行绘制。
  getTextInfos(start: CaretInfo, end: CaretInfo) {
    this.textInfos = [];
    for (let i = start.listItemIndex; i <= end.listItemIndex; i++) {
      let itemRect = this.scroller.getItemRect(i);
      let startIndex = start.listItemIndex == i ? start.caretIndex : 0;
      let endIndex = end.listItemIndex == i ? end.caretIndex : this.data[i].length;
      let layoutManager = this.controllers[i].getLayoutManager();
      let rects = this.getRectForRange(startIndex, endIndex, layoutManager);
      this.textInfos.push(new TextInfo(i, itemRect, rects, startIndex, endIndex, this.yOffset));
    }
    if (this.textInfos.length <= 0) {
      return;
    }
    let startCaretPosition = this.textInfos[0].getPosition(false);
    let endCaretPosition = this.textInfos[this.textInfos.length - 1].getPosition();
    if (startCaretPosition) {
      start.position = startCaretPosition;
    }
    if (endCaretPosition) {
      end.position = endCaretPosition;
    }
    this.paint();
  }

  // 使用Canvas绘制黄色高亮背景
  paint() {
    this.context.reset();
    this.context.translate(0, -this.yOffset);
    this.context.fillStyle = 'rgba(10, 89, 247, 0.2)';
    this.textInfos.forEach(info => {
      info.textRects.forEach(item => {
        this.context.fillRect(info.itemRect.x + item.left, info.itemRect.y + item.top + info.yOffset,
          item.right - item.left, item.bottom - item.top);
      });
    });
  }

  build() {
    Stack() {
      Canvas(this.context);
      List({ space: 10, scroller: this.scroller }) {
        Repeat(this.data)
          .each(item => {
            ListItem() {
              Text(item.item, { controller: this.controllers[item.index] })
                .fontColor('rgba(0, 0, 0, 0.9)');
            };
          });
      }
      .onScrollStart(() => {
        this.lastStartCaretPosition = this.startCaretInfo.position;
        this.lastStartCaretPosition.y = this.lastStartCaretPosition.y as number + this.yOffset;
        this.lastEndCaretPosition = this.endCaretInfo.position;
        this.lastEndCaretPosition.y = this.lastEndCaretPosition.y as number + this.yOffset;
      })
      .onDidScroll(() => {
        this.yOffset = this.scroller.currentOffset().yOffset;
        this.startCaretInfo.position =
          { x: this.lastStartCaretPosition.x, y: (this.lastStartCaretPosition.y as number) - this.yOffset };
        this.endCaretInfo.position =
          { x: this.lastEndCaretPosition.x, y: (this.lastEndCaretPosition.y as number) - this.yOffset };
        this.paint();
      })
      .gesture(
        LongPressGesture()
          .onAction(event => {
            this.getCaretInfo(event.fingerList[0].localX, event.fingerList[0].localY, this.startCaretInfo);
            this.endCaretInfo.listItemIndex = this.startCaretInfo.listItemIndex;
            this.endCaretInfo.caretIndex = this.startCaretInfo.caretIndex + 1;
            this.getTextInfos(this.startCaretInfo, this.endCaretInfo);
          })
      );

      this.caretBuilder(this.startCaretInfo);
      this.caretBuilder(this.endCaretInfo);
    }
    .margin({ left: 16, right: 16 });
  }
}
```
