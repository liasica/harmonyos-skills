---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1233
title: 识别Text组件中文本内容里的链接功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 识别Text组件中文本内容里的链接功能
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:68ec638af9eb50e1bee3b8872ca3f35b558634462c749237ffb184e0877c1d67
---

## 问题现象

某一长段文本中存在多个超链接，如何实现超链接的识别与点击功能？

## 背景知识

* [Text组件](../harmonyos-references/ts-basic-components-text.md)是常用的文本显示组件，自带链接等信息识别功能，包括但不限于对链接进行识别跳转。

* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)：ForEach接口基于数组类型数据来进行循环渲染。
* [Span](../harmonyos-references/ts-basic-components-span.md)：作为Text、ContainerSpan组件的子组件，用于显示行内文本的组件。

* 匹配字符串中的URL可以采用正则表达式的方式进行匹配。正则表达式（Regular Expression）是一种用于匹配字符串中字符组合的模式。它广泛应用于编程和文本处理中，特别是在搜索、替换和提取特定文本模式时。

## 解决方案

* **方案一**：采用Text组件的[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)属性，具体实现方式参考官方文档：[特殊文本识别跳转](../best-practices/bpta-special-text-recognition.md)。

  **说明** 

  该属性识别的URL不支持跳转自定义WebView，但是可以跳转系统浏览器。
* **方案二**：实现思路如下：
  1. 创建URL字符串的正则表达式。
  2. 通过match方法匹配原文本中的URL。
  3. 通过split方法以URL分割字符串，生成数组。
  4. 最后Text组件内通过ForEach循环渲染Span组件，匹配文本内的超链接。

  ```ts
  @Entry
  @Component
  struct ExampleText {
    @State strArr: Array<string> = [];
    @State urlArr: Array<string> = [];
    // 示例字符串
    text: string = '这是一个网址：https://developer.huawei.com，还有一个网址：https://developer.huawei.org';

    aboutToAppear(): void {
      this.splitUrls(this.text);
    }

    splitUrls(str: string) {
      let urlPattern = /(https?:\/\/|www.)[a-zA-Z_0-9\-@]+(\.\w[a-zA-Z_0-9\-:]+)+(\/[\(\)~#&\-=?\+\%/\.\w]+)?/g;
      let urlsArr = str.match(urlPattern) as Array<string>;
      if (urlsArr && urlsArr.length > 0) {
        this.strArr = this.splitString(str, urlsArr);
        this.urlArr = urlsArr;
      }
    }

    splitString(str: string, separators: Array<string>) {
      return str.split(new RegExp(separators.join('|'), 'g'));
    }

    build() {
      Column() {
        Text() {
          ForEach(this.strArr, (str: string, index: number) => {
            Span(str);
            if (this.urlArr.length > index) {
              Span(this.urlArr[index])
                .fontColor('#0a59f7')
                .onClick(() => {
                  this.getUIContext().getPromptAction().showToast({ message: '点击网址' });
                });
            }
          });
        }
        .width('90%')
        .fontSize(14);
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/vfCNiHbeSfeSWbdizyGkxQ/zh-cn_image_0000002658833297.png "点击放大")

## 总结

方案一为系统自带的Text组件的识别能力，能自动识别文本的信息并跳转，简单高效。方案二和方案三在识别到网络链接后，可以通过[App Linking](../harmonyos-guides/app-linking-startup.md)、[Deep Linking](../harmonyos-guides/deep-linking-startup.md)等方式拉起其它应用跳转指定页面，或者通过[Web组件](../harmonyos-guides/arkweb.md)显示网址的内容。
