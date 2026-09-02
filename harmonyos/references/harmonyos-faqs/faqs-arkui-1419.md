---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1419
title: TextArea注入长文本未自动滚动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextArea注入长文本未自动滚动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bcfdd801713e8b63a1f0bc8b3a49fd437144518a13414744ed920f4d6edae70c
---

## 问题现象

当通过TextArea的text参数给TextArea注入长文本，TextArea无法自动滚动到文本末端。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/paSjsFAJSyOpYG6FYOx70A/zh-cn_image_0000002628603740.jpg "点击放大")

## 背景知识

[TextArea](../harmonyos-references/ts-basic-components-textarea.md)是用于多行文本输入的组件，支持用户输入、自动换行、最大行数限制等功能，常用于表单输入、评论编辑等场景。

## 解决方案

* **方案一**：TextArea中并未直接提供控制滚动相关方法，当TextArea触发了滚动条，实际的显示视角会跟随光标的位置改变，为解决上述问题，可通过[caretPosition](../harmonyos-references/ts-basic-components-textarea.md#caretposition8)控制光标位置，从而实现自动滚动。

  ```ts
  @Entry
  @Component
  struct TextAreaExample {
    @State text: string = '';
    controller: TextAreaController = new TextAreaController();
    @State maxLength: number = 0;

    build() {
      Column() {
        Button('点击添加文本')
          .onClick(() => {
            this.controller.addText('这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本这是一段很长的文本');
            // 设置TextArea获焦
            focusControl.requestFocus('focus1');
          })
        TextArea({
          text: this.text,
          placeholder: 'The text area can hold an unlimited amount of text. input your word...',
          controller: this.controller,
        })
          .id('focus1')
          .placeholderFont({ size: 16, weight: 400 })
          .width(336)
          .height(100)
          .margin(20)
          .fontSize(16)
          .fontColor('#182431')
          .backgroundColor('#FFFFFF')
            // 监听文本变化事件
          .onChange((value: string) => {
            // 计算当前输入文本长度
            let length: number = value.length;
            // 更新maxLength状态：记录当前输入内容的最大长度
            if (this.maxLength < length) {
              this.maxLength = length;
            }
            // 更新text状态：保存最新输入内容
            this.text = value;
            // 调用controller的caretPosition方法：将光标定位到文本末尾
            this.controller.caretPosition(this.maxLength);
          })
      }.width('100%').height('100%').backgroundColor('#F1F3F5')
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/_tXJuZdBQwO9HWsgCfruDw/zh-cn_image_0000002658843007.jpg "点击放大")
* **方案二**：在TextArea组件外面再套一层Scroll组件，通过Scroller控制器滚动到容器边缘，从而实现自动滚动。

  ```ts
  @Entry
  @Component
  struct TextAreaPage {
    @State message: string =
      'Hello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello World';
    addMessage: string =
      'Hello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello World';
    controller: Scroller = new Scroller();

    scrollToBottom() {
      this.controller.scrollEdge(Edge.Bottom);// 通过控制器滚动到容器底部
    }

    build() {
      Column() {
        Scroll(this.controller) {
          TextArea({ text: this.message })
            .width('100%')
            .constraintSize({ minHeight: 200 })
            .onSizeChange(() => {
              this.scrollToBottom();
            })
        }
        .height(200)

        Button('button')
          .onClick(() => {
            this.message = this.message + this.addMessage;
          })
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/GyYExA28RWeM8_tlZR-h_Q/zh-cn_image_0000002628763642.gif "点击放大")
