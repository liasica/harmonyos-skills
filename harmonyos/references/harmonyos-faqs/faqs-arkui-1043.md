---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1043
title: TextInput组件实现验证码输入框
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput组件实现验证码输入框
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b0c7cd015ad6b8a1682e4dcb1d252bc4d18b24b423e0e6fbc5ffc4be35b91050
---

## 问题现象

如何实现验证码输入框效果，并设置输入框内容居中显示？

效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Xwd_ecRmSreGk_bR7IgCog/zh-cn_image_0000002628565450.png "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)是单行文本输入框组件，可以通过type属性设置输入框模式，具体模式可以参考[InputType](../harmonyos-references/ts-basic-components-textinput.md#inputtype枚举说明)枚举值。
* [ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)：接口基于数组循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。
* [requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)：方法语句中可使用的全局接口，调用此接口可以主动让焦点在下一帧渲染时转移至参数指定的组件上。

## 解决方案

* 方案一：
  1. 通过inputIndex变量定义输入框个数。
  2. 通过ForEach循环渲染，将所有输入框横排展示在Row组件中。
  3. 编辑输入框时通过回调函数onDidDelete、onChange做状态变更，实现变焦效果。

  ```ts
  @Entry
  @Component
  struct FourTextInput {
    @State inputValue: string[] = ['', '', '', ''];
    @State inputEnable: boolean[] = [true, false, false, false];
    inputIndex: number[] = [0, 1, 2, 3];

    build() {
      Row() {
        ForEach(this.inputIndex, (index: number) => {
          RelativeContainer() {
            TextInput({ text: this.inputValue[index] })
              .fontSize('30vp')
              .textAlign(TextAlign.Center)
              .maxLength(1)
              // .type(InputType.NUMBER_PASSWORD) // 如需要启动安全模式，添加此处属性
              .showPasswordIcon(false)
              .height(80)
              .border({
                width: 1,
                color: this.inputEnable[index] ? '#1b91e0' : '#999999',
                radius: 4,
                style: BorderStyle.Solid,
              })
              .id(index.toString())
              .onDidDelete(() => {
                if (this.inputValue[index].length === 0) {
                  // 不是第一个输入框且输入框内没有文字，则删除上一个输入框内容，并且使上一个输入框获取焦点
                  if (index !== 0) {
                    this.inputValue[index - 1] = '';
                    this.inputEnable[index] = false;
                    this.inputEnable[index - 1] = true;
                    this.getUIContext().getFocusController().requestFocus((index - 1).toString());
                  } else {
                    // 如果输入框内有文字，则只删除当前输入框内容
                    this.inputValue[index] = '';
                  }
                }
                ;
              })
              .onChange((value: string) => {
                this.inputValue[index] = value;
                if (value.length !== 1) {
                  return;
                }
                if (index !== 3) {
                  this.inputEnable[index + 1] = true;
                  this.inputEnable[index] = false;
                  this.getUIContext().getFocusController().requestFocus((index + 1).toString());
                }
              })
          }.layoutWeight(1).margin({ right: 5, left: index === 0 ? 5 : 0 })
        })
      }.onAppear(() => {
        this.getUIContext().getFocusController().requestFocus('0');
      })
    }
  }
  ```

* 方案二：参照[多种验证码场景](https://gitcode.com/HarmonyOS_Samples/verification-code-scenario/blob/master/README.md)demo示例，当前包含五个验证码场景：
  + 文本框显示光标：输入数字光标会移动到下一个文本框，同时下边框变色。
  + 底部加横条：在输入框内输入6位数字。
  + 背景颜色改变：输入数字后背景颜色改变。
  + 选择验证码：按照提示文字的顺序点击图片上的文字，然后点击提交。
  + 滑块验证码：点击滑块按钮向右滑动，直到将图片拼接完整时松手。
