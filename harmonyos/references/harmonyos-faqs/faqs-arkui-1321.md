---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1321
title: 应用内提示登录信息存在特殊字符报错
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用内提示登录信息存在特殊字符报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f339515eead29aada5648b4e21ba3a87e2a3a2778c463204980b6867d6fdc5c3
---

## 问题现象

输入对应的设备名称后，提示错误码报错。

## 背景知识

服务端通常会对用户输入的数据进行校验，尤其是在[输入框](../harmonyos-guides/arkts-common-components-text-input.md#创建输入框)中输入关键字段（如用户名、密码、手机号、邮箱等），通常会设置一系列规则，比如：

* 字段长度限制；
* 字段格式限制（如只能包含字母数字、不允许特殊字符等）；
* 必填项校验等。

当校验失败时，系统通常会以[Toast](../harmonyos-guides/arkts-create-toast.md)等方式提示用户具体错误原因，以帮助用户修正输入。

## 问题定位

根据日志信息可知，服务端校验不符合要求返回报错信息。

```screen
ThrowError errCode:200099742 errMsg: "存在特殊字符，请修改"
```

问题出现在字段校验失败时的提示信息中，错误码和提示内容被一起展示。

## 分析结论

1. **提示信息不符合体验标准**：用户只需要看到“存在特殊字符，请修改”，而不需要看到“错误码：200099742”，错误码主要用于开发调试或日志记录，而不是用户提示。
2. **未对错误码进行处理**：在接收到错误信息时，未做字符串解析或字段提取，导致错误码和提示信息一同展示。

## 修改建议

1. **处理错误信息时，过滤错误码**：应对接收到的错误信息进行处理，提取提示信息部分展示。例如：

   ```screen
   // 示例：字符串处理
   let errorMsg = '错误码：200099742，存在特殊字符，请修改！';
   // 输出："存在特殊字符，请修改！"
   let friendlyMsg = errorMsg.split('，')[1] + ',' + errorMsg.split('，')[2];
   ```

   或者使用正则表达式提取提示内容：

   ```screen
   friendlyMsg = errorMsg.replace(/^.*?，/, '');
   ```
2. **统一错误提示展示逻辑**：建议封装统一的错误提示模块，对所有错误信息进行格式化处理，避免重复代码，提高可维护性。
3. **增强字段校验逻辑**：在客户端也可以进行初步校验（如正则校验），避免不必要的服务端请求，提升用户体验和系统性能。

完整的示例参考：

```screen
@Entry
@Component
struct TitpsDemo {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
          // 示例：字符串处理
          let errorMsg = '错误码：200099742，存在特殊字符，请修改！';
          // 输出："存在特殊字符，请修改！"
          let friendlyMsg = errorMsg.split('，')[1] + ',' + errorMsg.split('，')[2];
          this.message = friendlyMsg;

          friendlyMsg = errorMsg.replace(/^.*?，/, '');
          this.message = friendlyMsg;
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
