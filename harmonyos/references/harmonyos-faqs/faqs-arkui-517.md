---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-517
title: 计算文本分页数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 计算文本分页数据
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cb32a306ef2b2ed3b994b9c447952333f2a194bd1178bc2e766f9642e8762bb3
---

## 问题现象

一段长文本，字体大小可修改，根据文本和字体大小计算当前文本分为几页，以及每页上的行数。

## 背景知识

* [measureTextSize](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)：计算指定文本的宽度和高度。
* [getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)：获取当前默认的display对象。
* [getLineCount](../harmonyos-references/js-apis-graphics-text.md#getlinecount)用于返回文本的总行数。

## 解决方案

1. 获取导航条和状态栏的高度，在EntryAbility.ets的onWindowStageCreate()中设置。

   ```ts
   let windowClass = windowStage.getMainWindowSync();
   // 获取布局避让遮挡的区域
   let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // 导航条避让
   let avoidArea = windowClass.getWindowAvoidArea(type);
   let bottomRectHeight = avoidArea.bottomRect.height; // 获取到导航条区域的高度
   AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);

   type = window.AvoidAreaType.TYPE_SYSTEM; // 状态栏避让
   avoidArea = windowClass.getWindowAvoidArea(type);
   let topRectHeight = avoidArea.topRect.height; // 获取状态栏区域高度
   AppStorage.setOrCreate('topRectHeight', topRectHeight);
   ```
2. 每页能展示的行数：获取页面的真实高度后，每页能展示的行数即为总高度/每行的高度（通过MeasureText.measureTextSize获取）。

   ```ts
   // 每页能展示的行数
   heightCalculator() {
     if (this.displayClass) {
       // 将设备高度减去顶部状态栏和底部导航条得到页面的真实高度
       let trueHeight = this.displayClass.height - this.topRectHeight - this.bottomRectHeight;
       console.info(`屏幕高度:${trueHeight}`);
       // 每页能展示的行数
       this.pageLines = Math.ceil(trueHeight / this.lineHeight);
     }
   }
   ```
3. 页面的数量：通过getLineCount方法获取组件内容的总行数，再用总行数/每页展示的行数即为总页数。

   ```ts
   // 计算页面数量
   pageNum() {
     let layoutManager: LayoutManager = this.controller.getLayoutManager();
     let lineCount = layoutManager.getLineCount();
     this.lineCount = lineCount;
     console.info(`总行数:${this.lineCount}`);
     // 最终的页面数量
     let pagesNum: number = Math.ceil(this.lineCount / this.pageLines);
     console.info(`每页行数:${this.pageLines}`);
     console.info(`总页数:${pagesNum} `);
   }
   ```

完整示例参考如下：

```ts
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private lineSize: SizeOptions = { height: 0, width: 0 }; // 文本的总长度
  private displayClass: display.Display | null = null;
  private str: string =
    '应用在开发和布局时，经常需要针对文本元素和内容进行排版、测量、绘制和显示等。字体引擎开发框架提供了一系列接口能力用于支持应用布局文本和管理字体。应用在开发和布局时，经常需要针对文本元素和内容进行排版、测量、绘制和显示等。字体引擎开发框架提供了一系列接口能力用于支持应用布局文本和管理字体。应用在开发和布局时，经常需要针对文本元素和内容进行排版、测量、绘制和显示等。字体引擎开发框架提供了一系列接口能力用于支持应用布局文本和管理字体。应用在开发和布局时，经常需要针对文本元素和内容进行排版、测量、绘制和显示等。字体引擎开发框架提供了一系列接口能力用于支持应用布局文本和管理字体。应用在开发和布局时，经常需要针对文本元素和内容进行排版、测量、绘制和显示等。字体引擎开发框架提供了一系列接口能力用于支持应用布局文本和管理字体。应用在开发和布局时，经常需要针对文本元素和内容进行排版、测量、绘制和显示等。字体引擎开发框架提供了一系列接口能力用于支持应用布局文本和管理字体';
  private lineHeight: number = 0;
  @StorageProp('topRectHeight') topRectHeight: number = 0;
  @StorageProp('bottomRectHeight') bottomRectHeight: number = 0;
  @State lineCount: number = 0;
  private controller: TextController = new TextController();
  @State pageLines: number = 0; // 每页展示的行数

  aboutToAppear(): void {
    this.lineSize = this.getUIContext().getMeasureUtils().measureTextSize({ textContent: this.str, fontSize: '100px' });
    this.displayClass = display.getDefaultDisplaySync(); // 获取设备的页面高度和宽度
    this.lineHeight = this.lineSize.height as number;
    console.info(`文本高度:${this.lineHeight}`);
    this.heightCalculator();
  }

  // 每页能展示的行数
  heightCalculator() {
    if (this.displayClass) {
      // 将设备高度减去顶部状态栏和底部导航条得到页面的真实高度
      let trueHeight = this.displayClass.height - this.topRectHeight - this.bottomRectHeight;
      console.info(`屏幕高度:${trueHeight}`);
      // 每页能展示的行数
      this.pageLines = Math.ceil(trueHeight / this.lineHeight);
    }
  }

  // 计算页面数量
  pageNum() {
    let layoutManager: LayoutManager = this.controller.getLayoutManager();
    let lineCount = layoutManager.getLineCount();
    this.lineCount = lineCount;
    console.info(`总行数:${this.lineCount}`);
    // 最终的页面数量
    let pagesNum: number = Math.ceil(this.lineCount / this.pageLines);
    console.info(`每页行数:${this.pageLines}`);
    console.info(`总页数:${pagesNum} `);
  }

  build() {
    Column() {
      Scroll() {
        Text(this.str, { controller: this.controller })
          .fontSize('100px')
          .width('100%')
          .onAreaChange(() => {
            // 当文本区域变化时（渲染完成）触发
            this.pageNum();
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

**说明** 

build中的字体大小和MeasureText.measureTextSize的字体大小需保持一致。
