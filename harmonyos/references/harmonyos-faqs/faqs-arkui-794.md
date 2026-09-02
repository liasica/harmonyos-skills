---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-794
title: TextInput实现自定义密码显隐效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TextInput实现自定义密码显隐效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1d73ed13558e1fc887932e30f8a6726dfe0d5202c6ca1d500f5c133ee9a45fc3
---

## 问题现象

如何实现TextInput组件文本输入时的密码显示效果？

## 背景知识

* [InputText](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件。
* [Password模式](../harmonyos-references/ts-basic-components-textinput.md#inputtype枚举说明)：密码显示小眼睛图标，默认输入文字短暂显示后变成圆点，从API version 12开始，特定设备上输入文字直接显示为圆点。密码输入模式不支持下划线样式。在已启用密码保险箱的情况下，支持用户名、密码的自动保存和自动填充。
* [onWillChange方法](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)：在文本内容将要发生变化时的回调。

## 解决方案

* 方案一：使用InputText的属性type(InputType.Password)。
* 方案二：使用onWillChange回调拦截输入，通过自定义方式，主动修改短暂显示的文字为圆点。

  ```ts
  @Entry
  @Component
  struct Index {
    @State actualText: string = ''; // 存储真实密码
    @State displayText: string = ''; // 显示用圆点
    @State isShowPassword: boolean = false; // 判断是否隐藏密码

    insertStringAt(str: string, index: number, insert: string) {
      return str.substring(0, index) + insert + str.substring(index);
    }

    delStringAt(str: string, index: number, end: number) {
      return str.substring(0, index) + str.substring(end);
    }

    build() {
      Column() {
        Text(this.actualText)
        TextInput({ text: $$this.displayText })
          .type(InputType.Password)
          .onSecurityStateChange((isShowPassword) => {
            this.isShowPassword = isShowPassword;
            if (isShowPassword) {
              this.displayText = this.actualText;
            }
          })
          .onWillChange((changeInfo: EditableTextChangeValue) => {
            let newContent = changeInfo.content;
            let oldContent = this.actualText;
            if (newContent == oldContent) {
              return true;
            }
            if (' '.repeat(newContent.length) == newContent && newContent.length === oldContent.length) {
              return true;
            } else {
              let options = changeInfo.options!;
              // 先删除
              let rangeBefore = options.rangeBefore;
              let afterDelStr = this.delStringAt(oldContent, rangeBefore.start!, rangeBefore.end!);
              // 再添加
              let rangeAfter = options.rangeAfter;
              let addStr = newContent.substring(rangeAfter.start!, rangeAfter.end!);
              let afterAddStr = this.insertStringAt(afterDelStr, rangeAfter.start!, addStr);
              this.actualText = afterAddStr;
              // 判断是否隐藏密码
              if (!this.isShowPassword) {
                this.displayText = ' '.repeat(afterAddStr.length);
              } else {
                this.displayText = afterAddStr;
              }
              return false;
            }
          })
      }
      .width('100%')
      .padding(16)
    }
  }
  ```
* 方案三：使用@State定义一个boolean类型的状态变量passwordState，将其作为TextInput的showPassword接口的入参，在点击按钮时改变passwordState的值，即可控制输入框密码的显隐。

  ```ts
  @Entry
  @Component
  struct PasswordInputTwo {
    @State actualText: string = ''; // 存储真实密码
    @State displayText: string = ''; // 显示用圆点
    @State isShowPassword: boolean = false; // 判断是否隐藏密码

    insertStringAt(str: string, index: number, insert: string) {
      return str.substring(0, index) + insert + str.substring(index);
    }

    delStringAt(str: string, index: number, end: number) {
      return str.substring(0, index) + str.substring(end);
    }

    build() {
      Column() {
        Text(this.actualText)
        TextInput({ text: $$this.displayText })
          .type(InputType.Password)
          .onSecurityStateChange((isShowPassword) => {
            this.isShowPassword = isShowPassword;
            if (isShowPassword) {
              this.displayText = this.actualText;
            }
          })
          .onWillChange((changeInfo: EditableTextChangeValue) => {
            let newContent = changeInfo.content;
            let oldContent = this.actualText;
            if (newContent == oldContent) {
              return true;
            }
            if (' '.repeat(newContent.length) == newContent && newContent.length === oldContent.length) {
              return true;
            } else {
              let options = changeInfo.options!;
              // 先删除
              let rangeBefore = options.rangeBefore;
              let afterDelStr = this.delStringAt(oldContent, rangeBefore.start!, rangeBefore.end!);
              // 再添加
              let rangeAfter = options.rangeAfter;
              let addStr = newContent.substring(rangeAfter.start!, rangeAfter.end!);
              let afterAddStr = this.insertStringAt(afterDelStr, rangeAfter.start!, addStr);
              this.actualText = afterAddStr;
              // 判断是否隐藏密码
              if (!this.isShowPassword) {
                this.displayText = ' '.repeat(afterAddStr.length);
              } else {
                this.displayText = afterAddStr;
              }
              return false;
            }
          })
      }
      .width('100%')
      .padding(16)
    }
  }
  ```

## 常见FAQ

Q：在模拟器中运行，TextInput组件的type设置为Password时，输入时键盘下会出现空白，为Normal时是正常的。

A：输入类型为Password时拉起的是华为安全键盘，类型为Normal时拉起是普通输入键盘，请以真机效果为准。
