---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-510
title: 自定义弹窗如何使用WrappedBuilder封装的样式实现倒计时效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 自定义弹窗如何使用WrappedBuilder封装的样式实现倒计时效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2b9e72daa712d37a03cf47ced02e6da9b839e59851ffc18eb1f57b206453208d
---

## 问题现象

需要实现以下场景：页面中有个按钮，点击按钮弹出弹窗，弹窗中有个10s倒计时，文案显示的是10到0的数字，显示为0时弹窗消失。

## 背景知识

* [ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)：ComponentContent表示组件内容的实体封装，其对象支持在非UI组件中创建与传递，便于开发者对弹窗类组件进行解耦封装。
* [update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)：用于更新WrappedBuilder对象封装的builder函数参数，与constructor传入的参数类型保持一致。
* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)：重复调用一个函数，在每次调用之间具有固定的时间延迟。

## 解决方案

实现弹窗倒计时效果可以参考如下方案进行，其中更新WrappedBuilder对象封装的builder函数参数要用update()方法实现。具体步骤如下：

1. 使用ComponentContent创建自定义组件内容。
2. 通过openCustomDialog打开弹窗。
3. 设置timer定时器，并通过update()方法更新builder函数参数。

完整示例参考如下：

```screen
import { BusinessError } from '@ohos.base';
import { ComponentContent } from '@ohos.arkui.node';

class Params {
  text: number = 0;

  constructor(text: number) {
    this.text = text;
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text.toString())
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .margin({
        bottom: 5,
        top: 5,
        right: 5,
        left: 5
      });
  }.backgroundColor('#FFF0F0F0');
}

@Entry
@Component
struct TimeIndex {
  // 使用@State装饰器管理状态，记录动态更新的数值
  @State message: number = 10;
  @State isEnabled: boolean = true;

  timeout(contentNode: ComponentContent<Params>) {
    let intervalID = setInterval(() => {
      contentNode.update(new Params(--this.message)); // 使用update方法更新对话框内容
      if (this.message === 0 || this.message < 0) {
        this.isEnabled = true;
        clearInterval(intervalID);
        // 关闭对话框并重置状态
        this.getUIContext().getPromptAction().closeCustomDialog(contentNode);
        this.message = 10;
      }
    }, 1000);
  }

  build() {
    Row() {
      Column() {
        Button('click me')
          .enabled(this.isEnabled)

          .onClick(() => {
            let uiContext = this.getUIContext();
            let promptAction = uiContext.getPromptAction();
            // 创建自定义组件内容，包含渲染函数和参数
            let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
            try {

              this.timeout(contentNode);
              // 打开自定义对话框
              promptAction.openCustomDialog(contentNode, {
                onWillAppear: () => {
                  this.isEnabled = false;
                },
                onWillDismiss: () => {
                  this.isEnabled = false;
                },
                onDidDisappear: () => {

                  this.message = 10;
                }
              });
            } catch (error) {
              let message = (error as BusinessError).message;
              let code = (error as BusinessError).code;
              console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
            }
          });
      }
      .width('100%')
      .height('100%');
    }
    .height('100%');
  }
}
```
