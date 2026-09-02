---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-152
title: 文本内容显示乱码
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 文本内容显示乱码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:be423ed0b747c6d1c0a2c335133c0104b3fd9b2ee9764153f1567d3ff02f932d
---

## 问题现象

应用里的文字展示的是乱码。

场景一：中文显示为编码。形如%E5%8D%97%E4%BA%AC%E5%B8%82。

场景二：方框形式的乱码。形如⊠⊠⊠⊠，一个方框中间加上对角线。

## 背景知识

* HarmonyOS中解编码的API是[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)和[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)。
  + TextEncoder用于将字符串编码为字节数组，支持多种编码格式。
  + TextDecoder用于将字节数组解码为字符串，可以处理多种编码格式。
  + 编解码的类型包括UTF-8、UTF-16LE/BE、ISO-8859和Windows-1251等不同的编码格式。
  + 无论是对请求的数据还是文本Text的字符串做编解码，都可以使用[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)和[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)来解决乱码问题。
* 可通过以下方法加载自定义字体：

  | 模块 | 属性、方法 |
  | --- | --- |
  | [graphics.text](../harmonyos-references/js-apis-graphics-text.md) | [loadFontSync](../harmonyos-references/js-apis-graphics-text.md#loadfontsync)、[loadFont](../harmonyos-references/js-apis-graphics-text.md#loadfont18) |
  | [readerCore](../harmonyos-references/reader-read-core.md) | [ReaderSetting](../harmonyos-references/reader-read-core.md#readersetting)的fontPath属性 |
  | [arkui.UIContext](../harmonyos-references/js-apis-arkui-uicontext.md) | [registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont) |
* decodeURI(encodedURI)：其中encodedURI参数：完整的编码统一资源标识符。返回值：一个新字符串，表示给定编码的统一资源标识符（URI）的未编码版本。
* decodeURIComponent(encodedURI)使用与decodeURI中描述的相同的解码算法。它解码所有转义序列，包括那些不是由encodeURIComponent创建的转义序列，例如：.-.!~\*'()。
* URL编码的每个序列以%开头，后面跟着两个十六进制数组（例如：%20、%E6）。中文字符通常被编码为多个连续的%XX序列（因为中文字符在UTF-8中占3个字节，所以一个中文字符通常会被编码成三个%XX，如欢->%E6%AC%A2）。
* URL编码中，所有可能引起URL解析歧义或者不符合URL规范的字符串都需要编码。

## 问题定位

* 场景一：中文显示为编码。
  + 排查是否使用[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)和[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)。
  + 排查乱码部分是否是URL编码。
    1. 检查字符串中是否有%，如果没有，那么它可能不是URL编码。
    2. 检查%后是否紧跟两个十六进制字符。
    3. 检查连续编码序列。

       对于非ASCII字符（如中文），在UTF-8编码下，一个字符会由多个连续的%XX表示。例如，一个中文字符通常对应三个连续的%XX（如%E4%BD%A0表示你）。
    4. 使用标准URL解码函数尝试解码（如JavaScript中的decodeURIComponent或Java中的URLDecoder.decode）。
* 场景二：方框形式的乱码。
  + 代码中全局搜索loadFont、fontPath、registerFont，查看应用所使用的注册自定义字体的方法是否正确设置。
  + 若注册自定义字体的方法正确设置，则查看字体文件是否损坏。

## 分析结论

* 场景一：中文显示为编码。
  + 展示的文字无论是请求数据后还是Text渲染文字时，都没有使用[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)和[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)做解编码，导致展示出中文编码。
  + %E6%AC%A2%E8%BF%8E%E4%BD%BF%E7%94%A8%E6%96%87%E4%BB%B6%E7%AE%A1%E7%90%86.pdf，实际是欢迎使用文件管理.pdf的URL编码形式。显示的是中文编码。
* 场景二：方框形式的乱码。
  + 应用所使用的注册自定义字体的方法未正确设置，导致使用该字体时文字乱码。
  + 应用所使用的自定义字体文件已损坏，该文字在字体中缺失，导致使用该字体时文字乱码。

## 修改建议

* 场景一：中文显示为编码。使用TextEncoder和TextDecoder来做字符串的解编码：

  ```ts
  import { util } from '@kit.ArkTS';

  @Entry
  @Component
  struct EncodeDecodeTest {
    @State encodeResult: string = '';
    @State decodeResult: string = '';
    str: string = 'hello';

    aboutToAppear(): void {
      // 创建编码器
      let textEncoder = new util.TextEncoder('gbk');
      // 编码
      let encodeRes = textEncoder.encodeInto(this.str);
      console.info('Encode result: ' + encodeRes);
      this.encodeResult = encodeRes.toString();
      // 创建解码器
      let textDecoder = util.TextDecoder.create('gbk');
      // 解码
      this.decodeResult = textDecoder.decodeToString(encodeRes);
      console.info('Decode result: ', this.decodeResult);
    }

    build() {
      Column({ space: 16 }) {
        Column() {
          Text('初始文本：')
          Text(this.str)
        }

        Column() {
          Text('编码结果：')
          Text(this.encodeResult)
        }

        Column() {
          Text('解码结果：')
          Text(this.decodeResult)
        }
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/QSP66uIJRqej1nAWzT9L1w/zh-cn_image_0000002659138339.png "点击放大")

* 场景二：
  + 正确设置应用所使用的注册自定义字体的方法。
    - loadFont方法请参考[自定义字体的注册和使用](../harmonyos-guides/custom-font-arkts.md)。
    - ReaderSetting函数请参考[自定义字体](../harmonyos-guides/reader-setting-font.md)。
    - 参考[registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)中的代码部分，注册使用自定义字体。
  + 使用完整的自定义字体文件。
