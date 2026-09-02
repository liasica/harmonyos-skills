---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1434
title: Select组件默认加粗字体
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Select组件默认加粗字体
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7ec5cb251fd5896ba865f8093744274cc5f62ebf778c435719b9ae28cbb7bb4e
---

## 问题现象

在字体大小一致的前提下，Select组件中显示的文本相较Text组件中的文本，视觉上更为粗重。

问题代码示例参考如下：

```ts
@Entry
@Component
struct SelectExample {
  @State text: string = '这是实验组';
  @State index: number = 0;

  build() {
    Column({ space: 10 }) {
      // icon可以使用其他有效资源
      Select([{ value: 'aaa', icon: $r('app.media.startIcon') }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 35 })
        .optionWidth(200)
        .optionHeight(300)
        .onSelect((index: number, text?: string | undefined) => {
          this.index = index;
          if (text) {
            this.text = text;
          }
        });
      Text('这是对照组')
        .fontSize(35);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/xzHutsn4TrKpSL57Jyw5OA/zh-cn_image_0000002628603754.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/RUJ-RIz4Q8miaG3CYu5f0w/zh-cn_image_0000002658843019.png "点击放大")

## 背景知识

* [Select](../harmonyos-references/ts-basic-components-select.md)是HarmonyOS提供的一种下拉选择菜单组件，可让用户在多个选项间选择。
* [Text](../harmonyos-references/ts-basic-components-text.md)组件的[font](../harmonyos-references/ts-basic-components-text.md#font12)属性可用于设置文本的样式，包括字体大小、字体粗细、字体族和字体风格等。

## 问题定位

* 当前Select组件和Text组件的文本内容相同，仅在font属性中设置了size大小，并未修改weight属性，但是Select组件中的文本比Text组件中的文本更粗。
* 根据Select组件中的font方法得知，下拉按钮本身的文本样式中weight的默认值为FontWeight.Medium，且后续版本没有相关变动。而Text组件字体默认粗细为FontWeight.Normal。

## 分析结论

Select组件默认会加粗字体，值默认为FontWeight.Medium，若需要修改字体粗细样式，则应该显式地定义其weight参数。

## 修改建议

为Select组件的font属性添加weight参数，并将值设置为FontWeight枚举类型的Normal。

完整示例参考如下：

```ts
@Entry
@Component
struct SelectBold {
  @State text: string = '这是实验组';
  @State index: number = 0;

  build() {
    Column({ space: 10 }) {
      // icon可以使用其他有效资源
      Select([{ value: 'aaa', icon: $r('app.media.startIcon') }])
        .selected(this.index)
        .value(this.text)
        .font({ size: 35, weight: FontWeight.Normal })
        .optionWidth(200)
        .optionHeight(300)
        .onSelect((index: number, text?: string | undefined) => {
          this.index = index;
          if (text) {
            this.text = text;
          }
        });
      Text('这是对照组')
        .fontSize(35);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
