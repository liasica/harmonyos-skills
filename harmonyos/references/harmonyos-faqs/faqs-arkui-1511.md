---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1511
title: 如何获取RichEditor的段落缩进并修改
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何获取RichEditor的段落缩进并修改
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b629bc1faa71344599d9be71f49c8e0fd0f1d73d65cef0ca3ad488fc4fba91fd
---

## 问题现象

打开一个已有内容的富文本编辑，如何获取当前的段落缩进并进行修改？

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)：支持图文混排和文本交互式编辑的组件。
* [getParagraphs](../harmonyos-references/ts-basic-components-richeditor.md#getparagraphs11)：以字符串为单位获取指定范围的段落。
* [RichEditorParagraphResult](../harmonyos-references/ts-basic-components-richeditor.md#richeditorparagraphresult11)：后端返回的段落信息。
* [RichEditorParagraphStyle](../harmonyos-references/ts-basic-components-richeditor.md#richeditorparagraphstyle11)：段落样式。
* [LeadingMarginPlaceholder](../harmonyos-references/ts-basic-components-richeditor.md#leadingmarginplaceholder11)：前导边距占位符，用于表示文本段落左侧与组件边缘之间的距离。

## 解决方案

1. 通过getParagraphs方法可以获取指定范围的段落，再根据段落里面的样式信息，拿到对应的组件与边缘之间的距离。
2. 根据获取到的缩进值对不同的段落进行[updateParagraphStyle](../harmonyos-references/ts-basic-components-richeditor.md#updateparagraphstyle11)。

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

## 总结

1. leadingMargin无法直接通过方法来转换LeadingMarginPlaceholder，这里需要用JSON来进行字符串和对象间的转换。
2. [getParagraphs](../harmonyos-references/ts-basic-components-richeditor.md#getparagraphs11)方法和[updateParagraphStyle](../harmonyos-references/ts-basic-components-richeditor.md#updateparagraphstyle11)方法都涉及到选中的段落范围[RichEditorRange](../harmonyos-references/ts-basic-components-richeditor.md#richeditorrange)这里的选择范围的单位是字符。例如选择第一段落，第一段落是10个字符的就选择范围1-10。依此类推。
