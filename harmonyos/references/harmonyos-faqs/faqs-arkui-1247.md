---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1247
title: 每输入一个字输入法软键盘都会收回
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 每输入一个字输入法软键盘都会收回
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:501b18f9bde90ce37f1ad2a2008743861f613c171e3e021a3f9383ae468599fe
---

## 问题现象

用户在输入框打字时，每打一个字输入法软键盘都会收回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/uDcc9cNfQpGhuXECUjtApQ/zh-cn_image_0000002628595452.png "点击放大")

## 背景知识

TextArea.[onChange](../harmonyos-references/ts-basic-components-textarea.md#onchange)：输入内容发生变化时，触发该回调。

## 问题定位

1. 日志搜索Focus，查看组件聚焦情况，发现两次拉起输入法时，输入框的组件ID不同，可以判断组件发生了重新渲染，当组件重新渲染时，输入框会失焦，导致输入法收起。

   ```txt
   [(100000:100000:scope)] current focus node info : (TextArea/9077).
   ...
   [(100000:100000:scope)] current focus node info : (TextArea/9154).
   ```
2. 代码搜索onChange，检查代码逻辑，当输入变化时，onChange调用自定义函数并导致组件重新渲染。

   ```ts
   TextArea.onChange(() => {
     // 自定义函数包含组件重新渲染逻辑
   });
   ```

## 分析结论

当输入框的内容发生改变时，组件重进渲染，导致输入框失焦，输入法收起。

## 修改建议

参考以下示例，优化代码逻辑，当输入框内容发生变化时，不要进行导致组件失焦的操作。

```ts
@Entry
@Component
struct TextAreaPage {
  @State text: string = '';
  @State textStr1: string = '';
  @State textStr9: string = '';
  controller: TextAreaController = new TextAreaController();

  build() {
    Row() {
      Column() {
        Text(`${this.textStr1}\n${this.textStr9}`)
          .fontSize(20)
        TextArea({ text: this.text, placeholder: 'input your word...', controller: this.controller })
          .onChange((value: string) => {
            // 文本内容发生变化时触发该回调
            // 文本内容变化的时候不要有失焦的代码逻辑
            console.info('onChange is triggering: ', value);
            this.textStr1 = `onChange is triggering: ${value}`;
          })
          .onFocus(() => {
            // 绑定通用事件，输入框获焦时触发该回调
            console.info('onFocus is triggering');
            this.textStr9 = `onFocus is triggering`;
          })
      }.width('100%')
    }
    .height('100%')
  }
}
```
