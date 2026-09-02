---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-946
title: Flex布局Text自动换行时显示不全
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Flex布局Text自动换行时显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5b46137b68bebb7fe1992eaf851c52a66f2f9487adc950c6e3f0451a84ec6731
---

## 问题现象

在下面代码中，Flex布局使用alignItems: ItemAlign.Stretch进行拉伸，并使用clip进行裁剪时会出现部分字符被裁切显示不全。

```ts
@Entry
@Component
struct Index {
  @State text: string = '1234567890123456789012345678901234567890123456789012345678901234567890123344';

  build() {
    Column() {
      Column() {
        Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Stretch }) {
          Column() {
            Text('xxxx')
          }
          .width(96)
          .flexShrink(0)

          Column() {
            Text('yyyy')
            Text('yyyy')
            Text(this.text) // 这里在自动换行时，最后一行的字符被部分遮挡
          }
          .flexGrow(1)
          .flexShrink(1)
          .padding(10)
          .borderWidth(1)
          .alignItems(HorizontalAlign.Start)
        }.width('90%')
        .border({
          width: 1,
          color: '#000000'
        })
      }.height('auto').clip(true)
      .justifyContent(FlexAlign.Center)

      Row() {
        Text(this.text)
      }.padding(12)
    }
  }
}
```

下面是字符显示不全的效果图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/2SEPNyy0S1eVsr7otmjPEQ/zh-cn_image_0000002628401232.png "点击放大")

## 背景知识

[Flex](../harmonyos-references/ts-container-flex.md)组件可以通过设置[FlexOptions](../harmonyos-references/ts-container-flex.md#flexoptions对象说明)的参数alignItems，设置子元素在交叉轴的对齐方式。子元素的[alignSelf](../harmonyos-references/ts-universal-attributes-flex-layout.md#alignself)属性也可以设置子元素在父容器交叉轴的对齐方式，且会覆盖Flex布局容器中alignItems配置。

## 问题定位

父组件设置的alignItems属性为[ItemAlign](../harmonyos-references/ts-appendix-enums.md#itemalign).Stretch时，子组件在交叉轴方向拉伸填充，拉伸效果由系统进行一个先期布局，不设置子组件的宽高时，会出现子组件溢出Flex区域的情况。

## 分析结论

在Flex容器的子组件设置alignSelf属性，可使该子组件不应用父组件的alignItems属性，从而防止子组件被过度拉伸导致溢出。

## 修改建议

可以给Flex容器中的Column组件增加alignSelf属性，Text子组件在Column父组件交叉轴的对齐格式会覆盖其alignItems设置，可以使Text子组件中的文本内容完整显示。

示例代码：

```ts
@Entry
@Component
struct StretchDemo {
  text: string = '1234567890123456789012345678901234567890123456789012345678901234567890123344';

  build() {
    Column() {
      Column() {
        Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Stretch }) {
          Column() {
            Text('xxxx');
          }
          .width(96)
          .flexShrink(0);

          Column() {
            Text('yyyy');
            Text('yyyy');
            Text(this.text); // 这里在自动换行时，最后一行的字符被部分遮挡
          }
          .flexGrow(1)
          .flexShrink(1)
          .padding(10)
          .borderWidth(1)
          .alignItems(HorizontalAlign.Start)
          .alignSelf(ItemAlign.Start);
        }.width('90%')
        .border({
          width: 1,
          color: '#000000'
        });
      }.height('auto').clip(true)
      .justifyContent(FlexAlign.Center);

      Row() {
        Text(this.text);
      }.padding(12);
    };
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/f7PCnLzqQISMVYjs2Kn1QQ/zh-cn_image_0000002658800497.png "点击放大")
