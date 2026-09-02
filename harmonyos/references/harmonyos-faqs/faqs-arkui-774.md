---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-774
title: 如何实现输入框在获焦时提示文本自动切换到左上角
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现输入框在获焦时提示文本自动切换到左上角
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4bc0df9c30b29e352d09b1c15bd191c0382dd33aa281422ce7b1954df4d8c3e4
---

## 问题现象

使用TextInput组件时，设置提示文字placeholder，当TextInput组件获取焦点时，placeholder提示文字上移到组件左上角，placeholder提示文字缩小，一半在组件外，一半在组件内，如何实现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/jcKLYY0xTsa8gtDNDsnFxw/zh-cn_image_0000002628395808.png "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)单行文本输入框组件。
* [焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)，自定义组件的走焦效果，可设置组件是否走焦和具体的走焦顺序，tab键或者方向键切换焦点。
* [显式动画](../harmonyos-references/ts-explicit-animation.md)提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

1. 使用组件堆叠模式，提示文字使用文本组件替代。
2. 确定输入框获焦、失焦时文本组件位置。
3. 定义获焦、失焦时的动画特效，以保证动画过程流畅舒适。

完整示例参考如下：

```ts
@Entry
@Component
struct CustomInputText {
  build() {
    Column() {
      Blank().height(50);
      InputComponent({ placeholder: '姓名', inputId: '1', originWeight: 40 });
      Blank().height(25);
      InputComponent({ placeholder: '电话', inputId: '2', originWeight: 40 });
      Blank().height(25);
      InputComponent({ placeholder: '户籍', inputId: '3', originWeight: 40 });
      Blank().height(25);
      InputComponent({ placeholder: '家庭住址', inputId: '4', originWeight: 70 });
    }
    .height('100%')
    .width('100%');
  }
}

@Component
struct InputComponent {
  text: string = '';
  inputId: string | undefined = undefined;
  controller: TextInputController = new TextInputController();
  placeholder: string = '';
  @State textFontSize: number = 20;
  @State textHeight: number = 40;
  originWeight: number = 0;
  @State textWeight: number = 40;
  @State textMarginTop: number = 10;
  @State textOpacity: number = 0.5;
  textBorderWidth: number = 2;
  textRadius: number = 10;

  // 提示文字缩小时组件配置位标
  textMin() {
    this.textFontSize = 12;
    this.textMarginTop = 0;
    this.textOpacity = 1;
    this.textHeight = 20;
    this.textWeight = 35;
    try {
      this.getUIContext().getFocusController().requestFocus(this.inputId);
    } catch (error) {
      // Implement error handling.
    }
  }

  // 提示文字处于初始状态时配置位标
  textMax() {
    if (this.text !== '') {
      return;
    }
    this.textFontSize = 20;
    this.textMarginTop = 10;
    this.textOpacity = 0.5;
    this.textHeight = 40;
    this.textWeight = this.originWeight;
  }

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      TextInput({})
        .id(this.inputId)
        .fontSize(20)
        .width(300)
        .height(40)
        .margin({ top: 10 })
        .opacity(0.5)
        .backgroundColor(Color.White)
        .defaultFocus(false)
        .border({
          width: this.textBorderWidth,
          color: Color.Black,
          radius: this.textRadius,
          style: BorderStyle.Solid
        })
        .onFocus(() => {
          this.textMin();
        })
        .onBlur(() => {
          this.textMax();
        })
        .onChange((value: string) => {
          this.text = value;
        });

      Column() {
        Text(this.placeholder)
          .fontSize(this.textFontSize * 0.8)
          .width(this.originWeight !== 0 ? this.originWeight : this.textWeight)
          .height(this.textHeight - this.textBorderWidth * 2)
          .opacity(this.textOpacity)
          .borderRadius(10)
          .textAlign(TextAlign.Center)
          .focusable(false)
          .renderFit(RenderFit.CENTER)
          .animation({
            duration: 1000,
            curve: Curve.Ease,
            iterations: 1,
            playMode: PlayMode.Normal
          })
          .onClick(() => {
            this.textMin();
          })

          .onBlur(() => {
            this.textMax();
          });
      }
      .borderRadius(10)
      .margin({
        top: this.textMarginTop + this.textBorderWidth,
        left: this.textBorderWidth * 3,
        bottom: this.textBorderWidth
      })
      .backgroundColor(Color.White)
      .animation({
        duration: 1000,
        curve: Curve.Ease,
        iterations: 1,
        playMode: PlayMode.Normal
      });
    };
  }
}
```

## 总结

* 组件主动获取焦点不受窗口焦点的控制，这意味着即使窗口没有焦点，组件也可能通过其他方式（如用户交互）获得焦点。
* 在组件的生命周期或事件处理逻辑中添加了代码来控制焦点的获取和释放，可以更灵活地完成一些应用操作，使得体验提升。
* 封装自定义组件，针对复用场景仅需修改提示文本相关信息，较为方便。
