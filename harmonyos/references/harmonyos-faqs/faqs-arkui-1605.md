---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1605
title: 如何解决分屏状态下页面滚动异常问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决分屏状态下页面滚动异常问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d8c91fb1adf2f79943b13c6419488fa5fae069b4c86f1e6efa693dad2edb9754
---

## 问题现象

在Grid中使用带有RelativeLayout的自定义组件时，分屏模式下，滑动页面时会出现回弹效果，无法正常滑动。

## 背景知识

* [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)：相对布局容器，用于复杂场景中元素对齐的布局。从API Version 11开始，在RelativeContainer组件中，将[width](../harmonyos-references/ts-universal-attributes-size.md#width)、[height](../harmonyos-references/ts-universal-attributes-size.md#height)设置为"auto"表示自适应子组件。
* [Grid](../harmonyos-references/ts-container-grid.md)：网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。

## 解决方案

* 分析问题可知，由于没有正确设置父组件高度，导致组件锚点异常，致使Text组件无法定位锚点而异常渲染。可以将父组件高度设置为自适应，锚点即可正常定位，解决渲染异常问题。
* RelativeContainer支持宽高自适应子组件，因此可以将其设置为auto，限制是当width设置为auto时，如果水平方向上子组件以容器作为锚点，则auto不生效，垂直方向上同理。完整示例代码如下：

```ts
@Entry
@Component
struct SplitScreenScroll {
  @State numbers: String[] = ['0', '1', '2', '3', '4'];
  scroller: Scroller = new Scroller();

  build() {
    Column({ space: 5 }) {
      Text('scroll').fontColor(0xCCCCCC).fontSize(9).width('75%').height('5%');
      Grid(this.scroller) {
        ForEach(this.numbers, () => {
          ForEach(this.numbers, (day: string) => {
            GridItem() {
              CustomGridItem({ day: day });
            };
          }, (day: string) => day);
        }, (day: string) => day);
      }
      .columnsTemplate('1fr')
      .columnsGap(10)
      .rowsGap(10)
      .width('85%')
      .height('95%');
    }.width('100%');
  }
}

@Component
struct CustomGridItem {
  day: string = '';

  build() {
    RelativeContainer() {
      Row() {
      }
      .width('100%')
      .height(50)
      .backgroundColor('#F1F2F3')
      .alignRules({})
      .id('row');
    }
    .width('auto')
    .height('auto')
    .border({ width: 2, color: '#F1F3F5' });
  }
}
```

* 实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ND7rIDUgR4qG8pNFnDMAog/zh-cn_image_0000002658852633.png "点击放大")
