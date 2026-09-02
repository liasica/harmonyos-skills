---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1300
title: RichEditor实现添加图文并控制图文间距
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > RichEditor实现添加图文并控制图文间距
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:17f5cdbc28b77f7fd0601849bd42ee262d21f02b1f9c8e0a1b8f1ad3503fb370
---

## 问题现象

要在文本框中实现图片与文字的组合场景，类似于文件符号图片加文件名的组合。

使用有如下诉求：

* 点击组合，光标自动后移至组合后面。
* 组合有外间距。

## 背景知识

* [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)：支持图文混排和文本交互式编辑的组件，实现精美、方便的文本编辑效果。
* [onSelectionChange](../harmonyos-references/ts-basic-components-richeditor.md#onselectionchange12)：组件内所有内容选择区域发生变化或编辑状态下光标位置发生变化时触发该回调。光标位置发生变化回调时，根据当前光标是否处于组合Span，将光标移动指定位置。
* [aboutToIMEInput](../harmonyos-references/ts-basic-components-richeditor.md#abouttoimeinput)：输入法输入内容前，触发回调。确保输入的内容不会影响组合Span。

## 解决方案

* 点击组合，光标自动后移至组合后面：
  1. 将组合中的Span分别写入RichEditor，然后记录具体的spanIndex。
  2. 当触发onSelectionChange回调时，使用getSpans获取当前光标的位置信息。
  3. 将获取到的光标位置与记录做对比，若存在则将光标移动至组合末尾。

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
  1. 图片Span使用RichEditorLayoutStyle配置margin属性实现外边距。
  2. 文字Span目前无直接配置外边距，建议额外添加空格实现。

  ```ts
  // 写入Span组合
  combinations(text: string, img: PixelMap | ResourceStr) {
    this.controller.addImageSpan(img, { imageStyle: { size: [20, 20], layoutStyle: { margin: { left: 5 } } } });
    this.controller.addTextSpan(text + ' ', { style: { fontColor: Color.Blue, fontSize: 18 } });
  }
  ```
* 完整示例参考如下：

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

## 常见FAQ

Q：为什么addBuilderSpan中信息数量过多的时候会出现当前行还未填充完毕就整体切换到下一行且无法分行？

A：目前addBuilderSpan所生成的Span仅作为一个元素使用，元素不可拆分，因此当前行不可容纳会自动换行且无法分行。

Q：部分图片是由本地HTML生成的，怎么添加到RichEditor里？

A：可以使用web组件加载本地HTML，再通过[addBuilderSpan](../harmonyos-references/ts-basic-components-richeditor.md#addbuilderspan11)添加自定义布局到RichEditor里。
