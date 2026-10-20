---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0005
title: RichEditor组件常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > RichEditor组件常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:09+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:4872d69e25eca015b710a44e0d3812bd00865ac83f2959023a7196230431d102
---

**Q：如何在文本框中实现图片与文字的组合场景，类似于文件符号图片加文件名的组合，并满足点击组合时光标自动后移至组合后面、组合有外间距的诉求？**

**A**：实现方式如下：

* 点击组合，光标自动后移至组合后面：
  1. 将组合中的Span分别写入RichEditor，然后记录具体的spanIndex；
  2. 当触发onSelectionChange回调时，使用getSpans获取当前光标的位置信息；
  3. 将获取到的光标位置与记录做对比，若存在则将光标移动至组合末尾。

  关键代码如下：

  ```ts
  .onSelectionChange((data) => {
            this.needNewSpan = false;
            // 根据光标位置获取对应Span信息
            let span = this.controller.getSpans(data);
            if (span.length != 0) {
              let spanLocation: number = span[0].spanPosition.spanIndex;
              let res = this.isCombinations(spanLocation);
              if (res) {
                // 判断是否是多选
                if (data.start != data.end) {
                  // 判断是否是第一次调整多选位置
                  if (!this.isSetSelection) {
                    // 将组合全选
                    this.isSetSelection = true;
                    if (span[0].spanPosition.spanIndex == this.combinationsLocation[this.needUpdateCombinations][0]) {
                      let spanText = this.controller.getSpans({ start: span[0].spanPosition.spanRange[1] + 1 });
                      this.controller.setSelection(span[0].spanPosition.spanRange[0],
                        spanText[0].spanPosition.spanRange[1]);
                    } else {
                      this.controller.setSelection(span[0].spanPosition.spanRange[0] - 1,
                        span[0].spanPosition.spanRange[1]);
                    }
                  } else {
                    this.isSetSelection = false;
                  }
                } else {
                  // 移动光标至组合末尾
                  this.controller.setCaretOffset(span[0].spanPosition.spanRange[1]);
                  this.needNewSpan = true;
                }
              }
            }
          })
  ```
* 组合有外间距：
  1. 图片Span使用RichEditorLayoutStyle配置margin属性实现外边距；
  2. 文字Span目前无直接配置外边距，建议额外添加空格实现。

  关键代码如下：

  ```ts
  // 写入Span组合
    combinations(text: string, img: PixelMap | ResourceStr) {
      this.controller.addImageSpan(img, { imageStyle: { size: [20, 20], layoutStyle: { margin: { left: 5 } } } });
      this.controller.addTextSpan(text + ' ', { style: { fontColor: Color.Blue, fontSize: 18 } });
    }
  ```
* 总体代码实现如下：

  ```ts
  @Entry
  @Component
  struct Index4RichEditor {
    controller: RichEditorController = new RichEditorController();
    option: RichEditorOptions = { controller: this.controller };
    img: Resource = $r('app.media.startIcon');
    // 需要组合的Span记录
    combinationsLocation: Array<Array<number>> = [[0, 1], [3, 4], [6, 7], [8, 9], [11, 12]];
    // 当输入的文字处于组合末尾时，需要新建Span
    needNewSpan: boolean = false;
    // 是否需要更新组合Span记录
    needUpdateCombinations: number = 0;
    // 判断是否已经更新过选中区域
    isSetSelection: boolean = false;

    // 写入Span组合
    combinations(text: string, img: PixelMap | ResourceStr) {
      this.controller.addImageSpan(img, { imageStyle: { size: [20, 20], layoutStyle: { margin: { left: 5 } } } });
      this.controller.addTextSpan(text + ' ', { style: { fontColor: Color.Blue, fontSize: 18 } });
    }
    // 判断位置是否处于组合内
    isCombinations(spanLocation: number): boolean {
      for (let index = 0; index < this.combinationsLocation.length; index++) {
        if (spanLocation == this.combinationsLocation[index][0] || spanLocation === this.combinationsLocation[index][1]) {
          this.needUpdateCombinations = index;
          return true;
        } else if (spanLocation < this.combinationsLocation[index][1]) {
          return false;
        }
      }
      return false;
    }

    // 更新组合所处位置
    updateCombinationsLocation() {
      for (let index = this.needUpdateCombinations; index < this.combinationsLocation.length; index++) {
        this.combinationsLocation[index][0] += 1;
        this.combinationsLocation[index][1] += 1;
      }
    }

    build() {
      Column() {
        RichEditor(this.option)
          .onReady(() => {
            this.combinations('@PyLo', this.img);
            this.controller.addTextSpan('请来会议室领取礼品，清单如下');
            this.combinations('领取礼品清单', this.img);
            this.controller.addTextSpan('，请参考清单到指定会议室');
            this.combinations('身体健康', this.img);
            this.combinations('万事如意', this.img);
            this.controller.addImageSpan(this.img, { imageStyle: { size: [20, 20], objectFit: ImageFit.Contain } });
            this.combinations('体锻如武夫', this.img);
            this.controller.addImageSpan(this.img, { imageStyle: { size: [20, 20], objectFit: ImageFit.Contain } });
          })
          .onSelectionChange((data) => {
            this.needNewSpan = false;
            // 根据光标位置获取对应Span信息
            let span = this.controller.getSpans(data);
            if (span.length != 0) {
              let spanLocation: number = span[0].spanPosition.spanIndex;
              let res = this.isCombinations(spanLocation);
              if (res) {
                // 判断是否是多选
                if (data.start != data.end) {
                  // 判断是否是第一次调整多选位置
                  if (!this.isSetSelection) {
                    // 将组合全选
                    this.isSetSelection = true;
                    if (span[0].spanPosition.spanIndex == this.combinationsLocation[this.needUpdateCombinations][0]) {
                      let spanText = this.controller.getSpans({ start: span[0].spanPosition.spanRange[1] + 1 });
                      this.controller.setSelection(span[0].spanPosition.spanRange[0],
                        spanText[0].spanPosition.spanRange[1]);
                    } else {
                      this.controller.setSelection(span[0].spanPosition.spanRange[0] - 1,
                        span[0].spanPosition.spanRange[1]);
                    }
                  } else {
                    this.isSetSelection = false;
                  }
                } else {
                  // 移动光标至组合末尾
                  this.controller.setCaretOffset(span[0].spanPosition.spanRange[1]);
                  this.needNewSpan = true;
                }
              }
            }
          })
          .aboutToIMEInput((value: RichEditorInsertValue) => {
            if (this.needNewSpan) {
              // 处理键入文字时光标位于组合末尾，防止与组合内文字Span拼接
              this.controller.addTextSpan(value.insertValue, { offset: value.insertOffset });
              this.updateCombinationsLocation();
              return false;
            } else if (value.insertOffset === 0) {
              // 处理光标位于行首的特殊情况
              this.needUpdateCombinations = 0;
              this.updateCombinationsLocation();
            }
            return true;
          })
          .padding(6)
          .borderRadius(6)
          .backgroundColor('#d8d8d9')
          .width("100%")
          .height("30%");
      }
      .padding(6)
      .width("100%")
      .height("70%");
    }
  }
  ```

**Q：为什么addBuilderSpan中信息数量过多的时候会出现当前行还未填充完毕就整体切换到下一行且无法分行？**

**A**：目前addBuilderSpan所生成的Span仅作为一个元素使用，元素不可拆分，因此当前行不可容纳会自动换行且无法分行。

**Q：部分图片是由本地HTML生成的，怎么添加到RichEditor里？**

**A**：可以使用web组件加载本地HTML，再通过[addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)添加自定义布局到RichEditor里。

**Q：在使用RichEditor组件时，需要将获取的字符串转换成HTML文本，再用RichEditor展示出HTML文本。**

**A**：在RichEditor组件中使用onReady和onIMEInputComplete回调函数获取输入内容，其中onReady(callback:Callback)和onIMEInputComplete(callback:Callback)参数callback都不可省略。

具体实现步骤为：

1. 创建[RichEditorController](../harmonyos-references/ts-basic-components-richeditor.md#richeditorcontroller)类的实例对象controller；
2. 在onReady回调函数中调用[controller.addTextSpan](../harmonyos-references/ts-basic-components-richeditor.md#addtextspan)方法传入HTML的内容部分data；
3. 在onIMEInputComplete回调函数中传入整个HTML标签字符串。

示例代码如下：

```ts
@Entry
@Component
struct RichEditorShow {
  private header: string = '<html>\n' +
    '<head>\n' +
    ' <meta charset=\'UTF-8\'>\n' +
    '</head>';
  private end: string = '</html>';
  @State data: string = '<h1 style= \'text-align: center; \'>h1标题</h1>' +
    '<h1 style=\'text-align: center;\'><i>h1斜体</i></h1>' +
    '<h1 style=\'text-align: center;\'><u>h1下划线</u></h1>' +
    '<h2 style=\'text-align: center;\'>h2标题</h2>' +
    '<h3 style=\'text-align: center;\'>h3标题</h3>';
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    Flex({
      direction: FlexDirection.Column, alignItems: ItemAlign.Start,
      justifyContent: FlexAlign.Start
    }) {
      RichText(this.data)
        .onStart(() => {
          console.info('RichText onStart');
        })
        .onComplete(() => {
          console.info('RichText onComplete');
        })
        .width('100%')
        .height(300)
        .backgroundColor(0XBDDB69);
      RichEditor(this.options)
        .onReady(() => {
          this.controller.addTextSpan(this.data,
            {
              style:
              {
                fontColor: Color.Orange,
                fontSize: 18
              }
            });
        })
        .onIMEInputComplete((value: RichEditorTextSpanResult) => {
          this.data = this.header + value.value + this.end;
        })
        .borderWidth(1)
        .borderColor(Color.Green)
        .width('100%')
        .height(400);
    };
  }
}
```

**Q：打开一个已有内容的富文本编辑，如何获取当前的段落缩进并进行修改？**

**A**：获取并修改段落缩进的步骤如下：

1. 通过getParagraphs方法可以获取指定范围的段落，再根据段落里面的样式信息，拿到对应的组件与边缘之间的距离。
2. 根据获取到的缩进值对不同的段落进行[updateParagraphStyle](../harmonyos-references/ts-basic-components-richeditor.md#updateparagraphstyle11)。示例代码如下：

   ```ts
   @Entry
   @Component
   struct LineBreakStrategyExample {
     controller: RichEditorController = new RichEditorController();
     private spanParagraphs: RichEditorParagraphResult[] = [];
     testStr: string = '0123456789,0123456789,0123456789,0123456789,0123456789.';
     @State left: number = 0;
     @State right: number = 0;

     build() {
       Column() {
         RichEditor({ controller: this.controller })
           .onReady(() => {
             this.controller.addTextSpan(this.testStr, {
               style: {
                 fontColor: Color.Black,
                 fontSize: '32'
               },
               paragraphStyle: {
                 textAlign: TextAlign.Start,
                 lineBreakStrategy: LineBreakStrategy.GREEDY,
                 leadingMargin: {
                   pixelMap: undefined,
                   size: [16, 6]
                 }
               }
             });
           })
           .width(400)
           .height(300)
           .margin({ bottom: 20 })
           .draggable(false);

         Column({ space: 10 }) {
           Button('获取距离').onClick(() => {
             this.spanParagraphs = this.controller.getParagraphs({ start: 1, end: 30 });
             for (let i = 0; i < this.spanParagraphs.length; i++) {
               let margin: LeadingMarginPlaceholder | Dimension | undefined = this.spanParagraphs[i].style.leadingMargin;
               let str = JSON.stringify(margin);
               let jsonObj: Object | null = JSON.parse(str);
               if (jsonObj) {
                 let commObj = (jsonObj as Record<string, Object>);
                 let commRecord = (commObj['size'] as Record<string, Object>);
                 let arrayJson = JSON.stringify(commRecord);
                 // sArray即为缩进的值
                 let sArray = JSON.parse(arrayJson) as Array<string>;
                 this.left = Number(sArray[0].split('.')[0]);
                 this.right = Number(sArray[1].split('.')[0]);
               }
             }
           });
           Button('段落对齐').onClick(() => {
             this.controller.updateParagraphStyle({
               // 以字符串为单位选择要更新的段落。
               start: -1, end: -1,
               style: {
                 // leadingMargin的值根据上面获取到的值，进行计算后赋予新值。
                 leadingMargin: { pixelMap: null, size: [this.left + 10, this.right + 20] }
               }
             });
           });
         };
       };
     }
   }
   ```

**Q：RichEditor支持输入带有样式的图文，在复制有样式的图文后，粘贴时如何去除复制的图文样式？**

**A**：实现的思路如下：

1. 监听页面粘贴事件：在RichEditor组件中设置onPaste事件处理函数，当用户粘贴内容时触发。
2. 阻止默认粘贴行为：在事件处理函数中调用event.preventDefault()，阻止RichEditor默认的粘贴行为，避免保留原有样式。
3. 获取剪贴板数据：使用pasteboard.getSystemPasteboard()获取系统剪贴板实例，然后调用getData方法获取剪贴板中的数据。
4. 提取纯文本内容：从剪贴板数据中提取纯文本内容，使用pasteData.getPrimaryText()方法获取纯文本。
5. 插入指定样式的文本：使用RichEditorController的addTextSpan方法，将提取的纯文本以指定的样式（如字体大小和颜色）插入到编辑器中，从而去除原有样式。

参考代码如下：

```ts
import pasteboard from '@ohos.pasteboard';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct richEditorPage {
  controller: RichEditorController = new RichEditorController();
  options: RichEditorOptions = { controller: this.controller };

  build() {
    RelativeContainer() {
      RichEditor(this.options)
        .width(300)
        .height(400)
        .backgroundColor('#fafafa')
        // 粘贴时，触发回调。
        .onPaste((event?: PasteEvent) => {
          if (event !== undefined && event.preventDefault) {
            // 阻止默认粘贴行为
            event.preventDefault();
            // 获取系统剪贴板实例
            let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
            // 获取剪贴板数据
            systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
              if (err) {
                console.error(`Failed to get PasteData. Code:${err.code} ,message:${err.message}`);
                return;
              }
              // 提取纯文本内容
              let text: string = pasteData.getPrimaryText();
              this.controller.addTextSpan(text, { style: { fontSize: 16, fontColor: Color.Gray } });
            });
          }
        })
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
