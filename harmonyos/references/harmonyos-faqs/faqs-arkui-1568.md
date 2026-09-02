---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1568
title: 密码输入框在弹出密码保险箱并自动填充密码后，会自动清空密码
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 密码输入框在弹出密码保险箱并自动填充密码后，会自动清空密码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a0576ffa6a868a86d561bda77d504f352a9f43238dba64b33b5197ed20f00bb3
---

## 问题现象

首次登录账号输入密码后，弹出密码保险箱后密码被保存到密码保险箱。重新登录时，输入账号后，在点击密码输入框时弹出密码保险箱自动填充密码，填充完成后焦点回到密码输入框，刚刚填充的密码被清空。

## 背景知识

* [文本输入 (TextInput/TextArea)](../harmonyos-guides/arkts-common-components-text-input.md)：TextInput、TextArea是输入框组件，用于响应用户输入，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法请参考[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)。
* [焦点事件](../harmonyos-references/ts-universal-focus-event.md#onfocus)：焦点事件指页面焦点在可获焦组件间移动时触发的事件，组件可使用焦点事件来处理相关逻辑。

## 问题定位

1. 使用DevEco Testing For Device工具中的UIViewer查看页面布局，可以看到密码输入框使用的是TextInput组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/zhWgf_vgSVGgGhgFcbHw4g/zh-cn_image_0000002658969077.png "点击放大")
2. 分析清空密码时的相关日志，没有打印明显清空密码的操作，打印了输入框获焦的日志，如下：

   ```txt
   C0391C/应用包名/AceFocus  应用包名  I     [(100000:100000:scope)] WinFocusMove end, NULL/secure_field onBlur, TextInput/secure_field onFocus, start: 1, end: 1, update: 2
   ```
3. 并且在手动输入密码，然后焦点切到账号输入框，再切回密码输入框，刚刚输入的密码被清空，说明是TextInput控件在获取焦点后密码被自动清空。
4. 分析应用代码，应该是给密码输入框设置了通用的焦点事件，在获取焦点时对输入框内容做了重置操作。如下代码所示：

   ```ts
   @Entry
   @Component
   struct Index {
     @State text: string = '';
     controller: TextInputController = new TextInputController();

     build() {
       Row() {
         Column() {
           TextInput({ text: this.text, placeholder: '', controller: this.controller })
             .type(InputType.Password)
             .onFocus(() => {
               // 绑定通用事件，输入框获焦时触发该回调，对输入框内容做了重置。
               console.info('onFocus is triggering')
               this.text = '';
             })
         }.width('100%')
       }
       .height('100%')
     }
   }
   ```

## 分析结论

给密码输入框设置了通用的onFocus焦点事件，在获取焦点时对输入框内容做了重置操作。

## 修改建议

1. 如果考虑高度安全性，不想使用密码保险箱的密码，可以禁用密码箱：不要将密码TextInput输入框的type属性设置为InputType.Password或InputType.NEW\_PASSWORD。
2. 正常场景密码输入框在获取焦点后无需重置输入内容。
