---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1477
title: 状态变量随滚动重复赋值引起UI不刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 状态变量随滚动重复赋值引起UI不刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5a1cf06391e78baf67fdcf806ed7a14031bd2b84149854fa8cce122e4bc3b8b1
---

## 问题现象

在Scroll组件onDidScroll事件回调中更改状态变量UI未刷新，滚动到底部时UI才更新。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/vxDWhN0DRFK1gjJSI0s0Nw/zh-cn_image_0000002628605360.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Z-kW0u9TRC-A7QUV3rB6ZQ/zh-cn_image_0000002658844617.gif "点击放大")

## 背景知识

* [onDidScroll](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)事件，滚动组件滑动时触发，可根据滚动偏移量计算滚动进度。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件，组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。
* [onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)事件，组件区域变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。

## 问题定位

1. 代码中定义了rollingProgress是滚动进度状态变量，并在onAreaChange事件中初始化该变量。在onDidScroll中打印该状态变量的值，可知该状态变量的值会随滚动改变。

   ```ts
   .onAreaChange((oldValue: Area, newValue: Area) => {
     this.textHeight = newValue.height as number
     let ratio = Math.max(CommonConstants.SCROLL_HEIGHT / this.textHeight, 0)
     this.rollingProgress = Math.floor(ratio * this.textBuffer.length)
   })
   ```

   ```ts
   .onDidScroll(() => {
     let yOffset = this.scroller.currentOffset().yOffset
     let ratio = Math.max((yOffset + CommonConstants.SCROLL_HEIGHT) / this.textHeight, 0)
     this.rollingProgress = Math.floor(ratio * this.textBuffer.length)
   })
   ```

2. 给该状态变量添加@Watch装饰器可知，每次滚动后该状态变量被赋值为初始值，可知onAreaChange重复触发。

   ```ts
   @State @Watch('change') rollingProgress: number = 0
   change() {
     console.info(`rollingProgress: ${this.rollingProgress}`);
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/8dIsFVNGSRi4fmyn6ME8Ww/zh-cn_image_0000002628765252.png "点击放大")

## 分析结论

滚动引起组件位置变化，组件位置变化时，[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)事件的回调会被触发，导致滚动进度状态变量被重新初始化，进而导致UI不刷新的问题。建议改用[onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)事件，onSizeChange事件仅会响应由布局变化所导致的组件尺寸发生变化时的回调，不会随滚动触发。

## 修改建议

将onAreaChange改为onSizeChange。

```ts
import { PromptAction } from '@kit.ArkUI';
import { util } from '@kit.ArkTS';

@Builder
export function readPageBuilder() {
  ReadPage();
}

// 定义常量类，存放滚动区域的高度
class CommonConstants {
  static readonly SCROLL_HEIGHT = 640;
}

// 定义标题组件
@Component
struct Title {
  @Prop leftIcon: Resource | undefined = undefined;
  @Prop rightIcon: Resource | undefined = undefined;
  @Prop title: Resource | string;
  @Prop titleFontsize: number;
  @Consume('pathStack') pathStack: NavPathStack;
  clickAction: () => void = () => {
  };

  build() {
    Row() {
      Row() {
        if (this.leftIcon) {
          Image(this.leftIcon)
            .width(40)
            .height(40)
            .onClick(() => {
              this.pathStack.pop();
            });
        }

        Text(this.title)
          .fontWeight(FontWeight.Bold)
          .fontSize(this.titleFontsize)
          .margin({ left: this.leftIcon ? 10 : 0 });
      }
      .justifyContent(FlexAlign.Start);

      if (this.rightIcon) {
        Image(this.rightIcon)
          .width(40)
          .height(40)
          .onClick(() => {
            this.clickAction();
          });
      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .width('100%')
    .height(56)
    .padding({ left: 16, right: 16 });
  }
}

// 定义主页面样式
@Entry
@Component
struct ReadPage {
  @StorageProp('topRectHeight') topRectHeight: number = 0;
  @StorageProp('bottomRectHeight') bottomRectHeight: number = 0;
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();
  @Provide('readChapterArray') readChapterArray: string[] = [];
  @Provide('contents') contents: string[] = ['HarmonyOS背景'];
  @Provide('ProgressValue') progressValue: number = 0;
  @State rollingProgress: number = 0;
  @State textBuffer: string = '';
  @State textHeight: number = 1;
  @State currentText: string = '';
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  params: number[] = [];
  chapterIndex: number = 0;
  lastedLearnIndex: number = 0;
  private scroller: Scroller = new Scroller;
  private controller: TextController = new TextController();

  aboutToAppear(): void {
    this.params = this.pathStack.getParamByName('ReadPage') as number[];
    this.chapterIndex = this.params[0];
    this.lastedLearnIndex = this.chapterIndex;
    this.readText('content.txt');
  }

  build() {
    NavDestination() {
      Column() {
        Title({
          leftIcon: $r('app.media.arrow_left'),
          title: this.contents[0],
          titleFontsize: 20
        });
        Row() {
          Text('热爱学习')
            .fontColor('#E6000000')
            .fontWeight(FontWeight.Bold)
            .fontSize(18);
        }
        .width('100%')
        .justifyContent(FlexAlign.Start)
        .padding({ left: 16, right: 16 })
        .margin({ top: 24 });

        Column() {
          Scroll(this.scroller) {
            Text('', { controller: this.controller }) {
              Span(this.currentText.replace(/\n/g, '\n       '));
            }
            .width('100%')
            .fontSize(16)
            .textIndent(30)
            .textAlign(TextAlign.Start)
            .padding({ top: 10 })
            .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
              this.textHeight = newValue.height as number;
              let ratio = Math.max(CommonConstants.SCROLL_HEIGHT / this.textHeight, 0);
              this.rollingProgress = Math.floor(ratio * this.textBuffer.length);
            });
          }
          .height(CommonConstants.SCROLL_HEIGHT)
          .align(Alignment.Top)
          .scrollBar(BarState.Off)
          .onDidScroll(() => {
            let yOffset = this.scroller.currentOffset().yOffset;
            let ratio = Math.max((yOffset + CommonConstants.SCROLL_HEIGHT) / this.textHeight, 0);
            this.rollingProgress = Math.floor(ratio * this.textBuffer.length);
          })
          .onReachEnd(() => {
            this.promptAction.showToast({
              message: '已完成',
              textColor: '#0A59F7',
              offset: { dx: 0, dy: 0 }
            });
            if (this.readChapterArray.indexOf(this.contents[this.chapterIndex]) === -1) {
              this.readChapterArray.push(this.contents[this.chapterIndex]);
            }
            this.progressValue = Math.floor((this.readChapterArray.length / this.contents.length) * 100);
          });

          Text(this.rollingProgress + '/' + this.textBuffer.length)
            .fontColor(Color.Grey)
            .fontSize(16)
            .textAlign(TextAlign.End)
            .margin({ right: 20 })
            .width('100%');
        }
        .borderRadius(16)
        .backgroundColor(Color.White)
        .padding({ left: 16, right: 16 })
        .margin({
          top: 10,
          left: 16,
          right: 16
        });
      }
      .padding({ top: this.getUIContext().px2vp(this.topRectHeight) })
      .backgroundColor('#F1F3F5');
    }
    .hideTitleBar(true)
    .backgroundColor('#F1F3F5');
  }
  // 读取文本文章
  private readText(path: string) {
    let context = this.getUIContext().getHostContext() as Context;
    let fileName: string = path;
    context.resourceManager.getRawFileContent(fileName, (_err, value) => {
      this.textBuffer = this.uint8ArrayToString(value);
      this.currentText = this.textBuffer;
    });
  }
  // 解码二进制数据
  private uint8ArrayToString(u8Array: Uint8Array): string {
    let desString = '';
    if (u8Array && u8Array.length > 0) {
      let textDecode = util.TextDecoder.create('utf-8');
      desString = textDecode.decodeToString(u8Array);
    }
    return desString;
  }
}
```

完整示例参考如下：

```ts
import { PromptAction } from '@kit.ArkUI';
import { util } from '@kit.ArkTS';

@Builder
export function readPageBuilder() {
  ReadPage();
}

// 定义常量类，存放滚动区域的高度
class CommonConstants {
  static readonly SCROLL_HEIGHT = 640;
}

// 定义标题组件
@Component
struct Title {
  @Prop leftIcon: Resource | undefined = undefined;
  @Prop rightIcon: Resource | undefined = undefined;
  @Prop title: Resource | string;
  @Prop titleFontsize: number;
  @Consume('pathStack') pathStack: NavPathStack;
  clickAction: () => void = () => {
  };

  build() {
    Row() {
      Row() {
        if (this.leftIcon) {
          Image(this.leftIcon)
            .width(40)
            .height(40)
            .onClick(() => {
              this.pathStack.pop();
            });
        }

        Text(this.title)
          .fontWeight(FontWeight.Bold)
          .fontSize(this.titleFontsize)
          .margin({ left: this.leftIcon ? 10 : 0 });
      }
      .justifyContent(FlexAlign.Start);

      if (this.rightIcon) {
        Image(this.rightIcon)
          .width(40)
          .height(40)
          .onClick(() => {
            this.clickAction();
          });
      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .width('100%')
    .height(56)
    .padding({ left: 16, right: 16 });
  }
}

// 定义主页面样式
@Entry
@Component
struct ReadPage {
  @StorageProp('topRectHeight') topRectHeight: number = 0;
  @StorageProp('bottomRectHeight') bottomRectHeight: number = 0;
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();
  @Provide('readChapterArray') readChapterArray: string[] = [];
  @Provide('contents') contents: string[] = ['HarmonyOS背景'];
  @Provide('ProgressValue') progressValue: number = 0;
  @State rollingProgress: number = 0;
  @State textBuffer: string = '';
  @State textHeight: number = 1;
  @State currentText: string = '';
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  params: number[] = [];
  chapterIndex: number = 0;
  lastedLearnIndex: number = 0;
  private scroller: Scroller = new Scroller;
  private controller: TextController = new TextController();

  aboutToAppear(): void {
    this.params = this.pathStack.getParamByName('ReadPage') as number[];
    this.chapterIndex = this.params[0];
    this.lastedLearnIndex = this.chapterIndex;
    this.readText('content.txt');
  }

  build() {
    NavDestination() {
      Column() {
        Title({
          leftIcon: $r('app.media.arrow_left'),
          title: this.contents[0],
          titleFontsize: 20
        });
        Row() {
          Text('热爱学习')
            .fontColor('#E6000000')
            .fontWeight(FontWeight.Bold)
            .fontSize(18);
        }
        .width('100%')
        .justifyContent(FlexAlign.Start)
        .padding({ left: 16, right: 16 })
        .margin({ top: 24 });

        Column() {
          Scroll(this.scroller) {
            Text('', { controller: this.controller }) {
              Span(this.currentText.replace(/\n/g, '\n       '));
            }
            .width('100%')
            .fontSize(16)
            .textIndent(30)
            .textAlign(TextAlign.Start)
            .padding({ top: 10 })
            .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
              this.textHeight = newValue.height as number;
              let ratio = Math.max(CommonConstants.SCROLL_HEIGHT / this.textHeight, 0);
              this.rollingProgress = Math.floor(ratio * this.textBuffer.length);
            });
          }
          .height(CommonConstants.SCROLL_HEIGHT)
          .align(Alignment.Top)
          .scrollBar(BarState.Off)
          .onDidScroll(() => {
            let yOffset = this.scroller.currentOffset().yOffset;
            let ratio = Math.max((yOffset + CommonConstants.SCROLL_HEIGHT) / this.textHeight, 0);
            this.rollingProgress = Math.floor(ratio * this.textBuffer.length);
          })
          .onReachEnd(() => {
            this.promptAction.showToast({
              message: '已完成',
              textColor: '#0A59F7',
              offset: { dx: 0, dy: 0 }
            });
            if (this.readChapterArray.indexOf(this.contents[this.chapterIndex]) === -1) {
              this.readChapterArray.push(this.contents[this.chapterIndex]);
            }
            this.progressValue = Math.floor((this.readChapterArray.length / this.contents.length) * 100);
          });

          Text(this.rollingProgress + '/' + this.textBuffer.length)
            .fontColor(Color.Grey)
            .fontSize(16)
            .textAlign(TextAlign.End)
            .margin({ right: 20 })
            .width('100%');
        }
        .borderRadius(16)
        .backgroundColor(Color.White)
        .padding({ left: 16, right: 16 })
        .margin({
          top: 10,
          left: 16,
          right: 16
        });
      }
      .padding({ top: this.getUIContext().px2vp(this.topRectHeight) })
      .backgroundColor('#F1F3F5');
    }
    .hideTitleBar(true)
    .backgroundColor('#F1F3F5');
  }
  // 读取文本文章
  private readText(path: string) {
    let context = this.getUIContext().getHostContext() as Context;
    let fileName: string = path;
    context.resourceManager.getRawFileContent(fileName, (_err, value) => {
      this.textBuffer = this.uint8ArrayToString(value);
      this.currentText = this.textBuffer;
    });
  }
  // 解码二进制数据
  private uint8ArrayToString(u8Array: Uint8Array): string {
    let desString = '';
    if (u8Array && u8Array.length > 0) {
      let textDecode = util.TextDecoder.create('utf-8');
      desString = textDecode.decodeToString(u8Array);
    }
    return desString;
  }
}
```
