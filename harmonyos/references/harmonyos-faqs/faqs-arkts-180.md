---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-180
title: String的静态方法详解
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > String的静态方法详解
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:31+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:e96415d3d9f5960aca728aac20d0b0bb453ecac994d45bdc024e18d9924f86f2
---

## 问题现象

在开发HarmonyOS应用时，开发者需根据字符编码生成字符串，或处理包含转义字符的模板字符串。若不了解String.fromCharCode()、String.fromCodePoint()和String.raw()三个静态方法的使用场景与差异，容易导致字符生成错误或模板字符串处理异常。

## 背景知识

在JavaScript中，String是一个内置对象，提供一系列静态方法用于处理字符与字符串。在HarmonyOS应用开发中，基于JS语言的ArkTS（ArkUI TypeScript）同样支持这些方法。

* String.fromCharCode()：将一组Unicode码点（0–65535）转换为对应的字符串。仅支持16位的BMP（基本多文种平面）字符。
* String.fromCodePoint()：支持更广范围的Unicode码点（包括代理对），能正确处理超出BMP的字符（如Emoji表情、古文字等）。
* String.raw()：用于创建“原始模板字符串”（raw template string），其中转义字符（如\n、\t）不会被解析，而是作为字面量保留。

## 解决方案

1. 使用String.fromCharCode()生成基础字符。

   当需要根据Unicode码点（0–65535）生成字符串时，使用String.fromCharCode()。

   示例代码：

   ```ts
   // 生成字母'A'和'Z'
   const charA = String.fromCharCode(65);
   const charZ = String.fromCharCode(90);

   hilog.info(0x0000, 'testTag', charA);
   hilog.info(0x0000, 'testTag', charZ);

   // 生成数字'0'到'9'
   const digits: string[] = [];
   for (let i = 48; i <= 57; i++) {
     digits.push(String.fromCharCode(i));
   }
   hilog.info(0x0000, 'testTag', digits.join(''));
   ```

   **说明** 

   适用场景：处理ASCII或基本拉丁字符，不涉及Emoji或特殊符号。
2. 使用String.fromCodePoint()支持完整Unicode。

   当需要处理超出16位范围的Unicode字符（如：、、）时，必须使用String.fromCodePoint()。

   示例代码：

   ```ts
   // 生成地球Emoji
   const earth = String.fromCodePoint(0x1F30D);
   hilog.info(0x0000, 'testTag', earth);

   // 生成程序员Emoji
   const programmer = String.fromCodePoint(0x1F469, 0x200D, 0x1F4BB);
   hilog.info(0x0000, 'testTag', programmer);

   // 生成家庭Emoji
   const family = String.fromCodePoint(0x1F468, 0x200D, 0x1F469, 0x200D, 0x1F467, 0x200D, 0x1F466);
   hilog.info(0x0000, 'testTag', family);
   ```

   **说明** 

   String.fromCharCode()对于代理对（如0xD83D和0xDCCD）会返回错误字符，而fromCodePoint()可正确处理。
3. 使用String.raw()获取原始模板字符串。

   当需要在模板字符串中保留原始的转义字符（如\n、\t、\\）时，应使用String.raw()。

   示例代码：

   ```ts
   // 普通模板字符串：转义字符会被解析
   const normalStr = `第一行\n第二行`;
   hilog.info(0x0000, 'testTag', normalStr);

   // 使用String.raw()：转义字符作为字面量保留
   const rawStr = String.raw`第一行\n第二行`;
   hilog.info(0x0000, 'testTag', rawStr);

   // 处理路径字符串（避免反斜杠被转义）
   const filePath = String.raw`C:\Users\John\Documents`;
   hilog.info(0x0000, 'testTag', filePath);
   ```

   **说明** 

   适用场景：构建正则表达式、路径字符串、日志格式、多行文本模板等需要保留转义字符的场景。

完整示例代码如下：

```ts
import hilog from '@ohos.hilog';

@Entry
@Component
struct StringStaticMethod {
  build() {
    Column() {
      Button('fromCharCode')
        .onClick(() => {
          // 生成字母'A'和'Z'
          const charA = String.fromCharCode(65);
          const charZ = String.fromCharCode(90);

          hilog.info(0x0000, 'testTag', charA);
          hilog.info(0x0000, 'testTag', charZ);

          // 生成数字'0'到'9'
          const digits: string[] = [];
          for (let i = 48; i <= 57; i++) {
            digits.push(String.fromCharCode(i));
          }
          hilog.info(0x0000, 'testTag', digits.join(''));
        }).margin({ bottom: 10 });
      Button('fromCodePoint')
        .onClick(() => {
          // 生成地球Emoji
          const earth = String.fromCodePoint(0x1F30D);
          hilog.info(0x0000, 'testTag', earth);

          // 生成程序员Emoji
          const programmer = String.fromCodePoint(0x1F469, 0x200D, 0x1F4BB);
          hilog.info(0x0000, 'testTag', programmer);

          // 生成家庭Emoji
          const family = String.fromCodePoint(0x1F468, 0x200D, 0x1F469, 0x200D, 0x1F467, 0x200D, 0x1F466);
          hilog.info(0x0000, 'testTag', family);
        }).margin({ bottom: 10 });
      Button('String.raw')
        .onClick(() => {
          // 普通模板字符串：转义字符会被解析
          const normalStr = `第一行\n第二行`;
          hilog.info(0x0000, 'testTag', normalStr);

          // 使用String.raw()：转义字符作为字面量保留
          const rawStr = String.raw`第一行\n第二行`;
          hilog.info(0x0000, 'testTag', rawStr);

          // 处理路径字符串（避免反斜杠被转义）
          const filePath = String.raw`C:\Users\John\Documents`;
          hilog.info(0x0000, 'testTag', filePath);
        });
    }.width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：String.fromCharCode()和String.fromCodePoint()有什么区别？

A：String.fromCharCode()仅支持16位码点（0–65535），不支持代理对；而String.fromCodePoint()支持完整的Unicode码点（包括Emoji和生僻字），能正确处理超出BMP的字符。

Q：为什么在处理Emoji时推荐使用String.fromCodePoint()？

A：Emoji通常由多个码点组成（如0x1F469+0x200D+0x1F4BB），这些码点可能包含代理对。String.fromCodePoint()能正确解析并组合这些码点，而fromCharCode()会失败或产生乱码。

Q：String.raw()与模板字符串中的raw属性有何关系？

A：String.raw()是一个静态方法，用于创建“原始模板字符串”。它实际上等价于调用模板字符串的raw属性，例如：String.raw等价于templateString.raw。

## 总结

掌握String.fromCharCode()、String.fromCodePoint()和String.raw()三个静态方法，是编写高质量、跨平台兼容的HarmonyOS应用开发中不可或缺的能力。

* 使用fromCharCode()处理常见ASCII字符；
* 使用fromCodePoint()处理Emoji、多语言字符；
* 使用raw()保留模板字符串中的转义字符。

**说明** 

举一反三：在处理国际化文本、日志输出、配置文件生成等场景时，可灵活结合这三个方法，提升代码可读性与健壮性。
