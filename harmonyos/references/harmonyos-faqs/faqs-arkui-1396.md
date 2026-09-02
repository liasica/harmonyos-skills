---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1396
title: 文本和富文本宽高计算
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 文本和富文本宽高计算
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:61b5b4fa6df8a4945b0ce340f30468302721c2fed4f2539db2022573ced30ac7
---

## 问题现象

在HarmonyOS应用开发中，开发者需要知道如何动态计算文本在UI中的占用宽高，以确保正确布局。

## 背景知识

文本宽高计算对于自适应UI设计非常重要，尤其是在不同设备、字体大小和格式的情况下。常见的需要获取文本宽高组件有Text组件、Canvas组件和Web组件。

* Text组件：使用[@ohos.measure](../harmonyos-references/js-apis-measure.md)来计算文本的宽高。
* Canvas组件：使用[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)的[measureText](../harmonyos-references/ts-components-canvas-common-method.md#measuretext)方法来计算文本的宽高。
* Web组件：利用Web组件加载富文本时，本身没有提供API可以获取富文本的宽高，但是可以通过[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)来调用JS方法获取富文本区域的宽高。

## 解决方案

1. Text组件可以使用MeasureUtils（原[@ohos.measure](../harmonyos-references/js-apis-measure.md)）计算文本总体的宽度和高度。常见应用场景如下：
   * 组件宽度自适应Text文本宽度，代码示例如下：

     ```ts
     import { MeasureUtils } from '@kit.ArkUI';

     @Entry
     @Component
     struct MeasureTextExample {
       msg: string = 'Harmony你好\n测试一下换行的测试一下换行\n测试制表\t哈哈';
       uiContext: UIContext = this.getUIContext();
       uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();
       textWidth: number = this.uiContextMeasure.measureText({
         textContent: this.msg,
         fontSize: '16px'
       });

       build() {
         Column() {
           Text(this.msg).fontSize(16).fontColor(Color.Black);
           // 这里设置Row的宽度为MeasureText.measureText获取到的文本宽度
           Row().height(30).width(this.textWidth).borderColor(Color.Blue).borderWidth(1)
         }
         .padding(16)
       }
     }
     ```
   * 文本展开与收起场景，代码示例可参考[文字展开收起案例](https://gitee.com/harmonyos-cases/cases/blob/master/CommonAppDevelopment/feature/textexpand/README.md)。另外，对于富文本内容，使用[measureTextSize](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)计算时结果不准确。此时可以使用[ParagraphBuilder](../harmonyos-references/js-apis-graphics-text.md#paragraphbuilder)进行段落排版，根据排版内容计算截断位置，进而实现富文本的折叠展开功能。富文本收起展开的代码示例可参考[TextExpand](https://gitee.com/harmonyos_samples/TextExpand)。

2. Canvas组件可以使用CanvasRenderingContext2D的[measureText](../harmonyos-references/ts-components-canvas-common-method.md#measuretext)方法获取文本的宽度和高度。常见应用场景如下：
   * 绘制矩形覆盖文本，代码示例如下：

     ```ts
     @Entry
     @Component
     struct CanvasTestPage {
       private settings: RenderingContextSettings = new RenderingContextSettings(true);
       private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
       drawText: string = 'Harmony你好\n测试一下换行的测试一下换行\n测试制表\t哈哈';

       build() {
         Column() {
           Canvas(this.context)
             .width('100%')
             .height('100%')
             .onReady(() => {
               this.context.textBaseline = 'top';
               this.context.font = '20vp sans-serif';
               let text: TextMetrics = this.context.measureText(this.drawText);
               this.context.fillStyle = 'rgba(0,0,0,0.3)';
               this.context.fillRect(0, 100, text.width, text.height);
               this.context.fillStyle = 'rgb(0,0,255)';
               this.context.fillText(this.drawText, 0, 100, text.width);
             })
         }.margin(10)
       }
     }
     ```
   * Canvas使绘制的长文本自动换行，核心代码如下：

     ```ts
     import { window } from '@kit.ArkUI';

     @Entry
     @Component
     struct CanvasTestPage1 {
       private settings: RenderingContextSettings = new RenderingContextSettings(true);
       private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
       drawText: string = 'Harmony你好\n测试一下换行的测试一下换行\n测试制表\t哈哈';
       @State screenWidth: number = 0;

       // aboutToAppear中获取屏幕宽高
       aboutToAppear() {
         window.getLastWindow(this.getUIContext().getHostContext())
           .then((windowClass: window.Window) => {
             windowClass.setWindowLayoutFullScreen(true);
             let windowProperties = windowClass.getWindowProperties();
             this.screenWidth = this.getUIContext().px2vp(windowProperties.windowRect.width);
           });
       }

       build() {
         Column() {
           Canvas(this.context)
             .width('100%')
             .height('100%')
             // Canvas绘制时判断添加下一个字符会超出最大宽度，如果是则换行
             .onReady(() => {
               let currentX = 10;
               let currentY = 60;
               let line: string = '';
               let chars: Array<string> = this.drawText.split('');
               for (let char of chars) {
                 this.context.font = '20vp sans-serif';
                 if (this.context.measureText(line + char).width > (this.screenWidth - 10)) {
                   this.context.fillStyle = 'rgba(0,0,0,0.3)';
                   this.context.fillText(line, currentX, currentY);
                   currentY += this.context.measureText(line + char).height;
                   line = char;
                 } else {
                   line += char;
                 }
               }
               // 绘制最后一行
               this.context.fillText(line, currentX, currentY);
             })
         }.margin(10)
       }
     }
     ```

3. Web组件可以通过[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)获取H5代码片段中富文本的宽度和高度。常见应用场景如下：

   获取指定区域内宽高，代码示例如下：

   ```ts
   import web_webview from '@ohos.web.webview';

   @Entry
   @Component
   struct WebComponent {
     controller: web_webview.WebviewController = new web_webview.WebviewController();
     @State richTextHeight: number = 0;
     @State richTextWidth: number = 0;

     build() {
       Column() {
         Web({ src: '', controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
           .onControllerAttached(() => {
             this.controller.loadData(
               "<html>" +
                 '<div id="box"><h1 style="text-align: center;">h1标题</h1>' +
                 '<h1 style="text-align: center;"><i>h1斜体</i></h1>' +
                 '<h1 style="text-align: center;"><u>h1下划线</u></h1>' +
                 '<h2 style="text-align: center;">h2标题</h2>' +
                 '<h3 style="text-align: center;">h3标题</h3>' +
                 '<p style="text-align: center;">p常规</p><hr/>' +
                 '</div>' +
                 "</html>",
               "text/html",
               "UTF-8"
             );
           })
           .onPageEnd(() => {
             this.controller.runJavaScript(`
               function getSize() {
                 return {
                   width: document.getElementById('box').offsetWidth,
                   height: document.getElementById('box').offsetHeight
                 };
               };
               getSize()`)
               .then((result: string) => {
                 let res: ESObject = JSON.parse(result);
                 this.richTextHeight = this.getUIContext().px2vp(res.height);
                 this.richTextWidth = this.getUIContext().px2vp(res.width);
               });
           }).layoutWeight(1)
         Column() {
           Text(`The width of 'richText': ${this.richTextWidth}`);
           Text(`The height of 'richText': ${this.richTextHeight}`);
         }.layoutWeight(1)
       }
     }
   }
   ```

效果如下：

| 方案一 | 方案二 | 方案三 |
| --- | --- | --- |
|  |  |  |

## 总结

文本和富文本都没有提供API可以给其他组件用于获取其宽度和高度，但是提供了文本计算的方式用于获取，三种方式区别如下：

| 组件 | 用法 | 应用场景 |
| --- | --- | --- |
| Text组件 | [@ohos.measure](../harmonyos-references/js-apis-measure.md) | 自适应Text文本宽度、文本展开与收起 |
| Canvas组件 | [measureText](../harmonyos-references/ts-components-canvas-common-method.md#measuretext) | 绘制矩形覆盖文本、绘制长文本自动换行 |
| Web组件 | [runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript) | 获取H5代码片段中富文本的宽度和高度 |

另外，对于富文本的收起展开场景，使用measureTextSize计算带有富文本的内容时结果不准确，可以使用[ParagraphBuilder](../harmonyos-references/js-apis-graphics-text.md#paragraphbuilder)进行段落排版来计算截断位置。
