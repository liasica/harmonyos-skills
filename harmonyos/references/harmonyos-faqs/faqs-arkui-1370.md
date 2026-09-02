---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1370
title: 如何自定义一个既可输入也可下拉选择的文本行
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何自定义一个既可输入也可下拉选择的文本行
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3173b1e88a5aa6a94c8e075c2b3cc57acc26ff9df5e3bf1ddd6fc904505dca89
---

## 问题现象

如何快速实现一个自定义文本框，既能自己输入文本，又能通过下拉框选择已有文本？

## 背景知识

TextInput组件的[showUnit](../harmonyos-references/ts-basic-components-textinput.md#showunit10)属性设置控件作为文本框单位。需搭配[showUnderline](../harmonyos-references/ts-basic-components-textinput.md#showunderline10)使用，当showUnderline为true时生效。以此实现下拉框功能。

## 解决方案

* **方案一**：使用TextInput组件的showUnit属性，示例代码如下：

  ```screen
  @Entry
  @Component
  struct SelectExample {
    @State text: string = '请输入...';

    @Builder
    itemEnd() {
      Select([{ value: 'selectedOptionFont' },
        { value: 'optionFont' },
        { value: 'backgroundColor' },
        { value: 'responseRegion' }])
        .height('48vp')
        .borderRadius(0)
        .selected(2)
        .align(Alignment.Center)
        .value('选择一个词')
        .font({ size: 20, weight: 500 })
        .fontColor('#182431')
        .selectedOptionFont({ size: 20, weight: 400 })
        .optionFont({ size: 20, weight: 400 })
        .backgroundColor(Color.Transparent)
        .responseRegion({
          height: '40vp',
          width: '80%',
          x: '10%',
          y: '6vp'
        })
        .onSelect((index: number, text: string) => {
          console.info('Select:' + index);
          this.text = text;
        })
    }

    build() {
      Column() {
        TextInput({ placeholder: 'underline style', text: this.text })
          .showUnderline(true)
          .width(350)
          .height(60)
          .showUnit(this.itemEnd) // 设置文本下拉框

      }.width('100%')
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/z512Bw0aRzKckaT9stbd-A/zh-cn_image_0000002628602038.png "点击放大")
* **方案二**：组合使用Stack组件和margin属性自定义实现，示例代码：

  ```screen
  @Entry
  @Component
  struct SelectExample2 {
    @State selectVal: undefined = undefined;
    @State currentSearchContent: string | undefined = '';
    private controller = new TextInputController();

    build() {
      Column() {
        Stack() {
          // 输入框组件
          TextInput({ placeholder: '请输入内容', controller: this.controller, text: this.currentSearchContent })
            .height(40)
            .width('100%')
            .fontSize(16)
            .placeholderColor(Color.Grey)
            .placeholderFont({ size: 16, weight: 400 })
            .borderStyle(BorderStyle.Solid)
            .backgroundColor('#E6E8E9')

          Row() {
            // 下拉框组件
            Select([
              { value: 'aaa' },
              { value: 'bbb' },
              { value: 'ccc' },
              { value: 'ddd' }
            ])
              .value(this.selectVal!!)
              .font({ size: 16, weight: 500 })
              .selectedOptionFont({ size: 16, weight: 400 })
              .optionFont({ size: 16, weight: 400 })
              .menuAlign(MenuAlignType.START, { dx: -260, dy: 0 })
              .optionWidth(200)
              .optionHeight(200)
              .backgroundColor('#E6E8E9')
              .onSelect((index: number, text?: string | undefined) => {
                this.selectVal = undefined;
                this.currentSearchContent = text;
                console.info('index:', index);
              })

            // 自定义图标
            Image($r('app.media.startIcon'))
              .width(24)
              .height(24)
              .margin({ left: -36 })
              .hitTestBehavior(HitTestMode.Transparent)
          }
          .width('100%')
          .hitTestBehavior(HitTestMode.None)
          .justifyContent(FlexAlign.End)
          .padding({ right: '10' })
        }
        .padding({ left: 16, right: 16 })
        .alignContent(Alignment.Start)
        .width('100%')
      }
      .width('100%')
      .height('100%')
      .backgroundColor($r('sys.color.icon_on_primary'))
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/n9q0Vi2YSui3Y0pS9e2cVA/zh-cn_image_0000002628761924.png "点击放大")
