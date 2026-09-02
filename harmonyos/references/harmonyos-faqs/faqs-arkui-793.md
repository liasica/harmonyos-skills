---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-793
title: Swiper组件导航点颜色重叠问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper组件导航点颜色重叠问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3b0d0b3d2c06c516e8acedac33c5100bbc6f3e9d8efdf9f9537fd9a25248e99e
---

## 问题现象

Swiper组件中圆点指示器会出现选中页面的导航点和选中前颜色重合的情况。

指示器设置如下：

```ts
export class YDSwiperIndicatorStyles implements AttributeModifier<SwiperAttribute> {
  // 通过构造函数，创建时传参
  constructor() {
  }

  applyNormalAttribute(instance: SwiperAttribute): void {
    // instance为Button的属性对象，可以通过instance对象对属性进行修改
    instance
      .indicator(
        Indicator.dot()
          .left(0)
          .bottom(0)
          .itemWidth(15)
          .itemHeight(15)
          .color('#33000000')
          .selectedItemWidth(28)
          .selectedItemHeight(15)
          .selectedColor('#80000000')
      )
  }
}
```

效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/XWDu41DoRIivhZYpnvPEdg/zh-cn_image_0000002658797001.png "点击放大")

## 背景知识

* [indicator](../harmonyos-references/ts-container-swiper.md#indicator15)可以设置外部绑定的导航点组件控制器，当使用单独导航点指示器控制器时，可以与外部单独导航点进行绑定，但是绑定的单独导航点和内置导航点不能同时存在。
* [color](../harmonyos-references/ts-container-swiper.md#color)可以设置Swiper组件圆点导航指示器的颜色，[selectedColor](../harmonyos-references/ts-container-swiper.md#selectedcolor)用于设置选中Swiper组件圆点导航指示器的颜色，颜色取值参考[ResourceColor](../harmonyos-references/ts-types.md#resourcecolor)。

## 问题定位

定义圆点导航点的color和selectedColor时颜色设置了透明度，导致在颜色叠加后会出现重合现象。

## 分析结论

* 设置color和selectedColor的颜色使用了八位颜色编码，其中前两位表示颜色的透明度，范围从00到FF(0到255)，00表示完全透明，FF表示完全不透明，后六位表示红(R)、绿（G）、蓝（B）三种颜色的值，每种颜色占两位，范围也是从00到FF(00到255)，分别对应红、绿、蓝三种颜色的强度。
* color('#33000000')的透明度的值为33，selectedColor('#80000000')的透明度的值为80，导致出现选中导航点区域有颜色叠加效果。将selectedColor的透明度值设置为FF，选中导航点的颜色就可以完全不受圆形导航点影响。

## 修改建议

设置selectedColor时，选取非透明颜色可以避免出现颜色叠加，比如设置为selectedColor('#FFA8A8A8')，也可以使用selectedColor(Color.Gray)达到相同效果。

完整代码如下：

```ts
class YDSwiperIndicatorStyles implements AttributeModifier<SwiperAttribute> {
  // 通过构造函数，创建时传参
  constructor() {
  }

  applyNormalAttribute(instance: SwiperAttribute): void {
    // instance为Button的属性对象，可以通过instance对象对属性进行修改
    instance
      .indicator(
        Indicator.dot()
          .left(0)
          .bottom(0)
          .itemWidth(15)
          .itemHeight(15)
          .color('#33000000')
          .selectedItemWidth(28)
          .selectedItemHeight(15)
          .selectedColor(Color.Gray)
      );
  }
}

@Entry
@Component
struct swiperDemo {
  build() {
    Column() {
      Swiper() {
        Repeat(['1', '2', '3'])
          .each(() => {
            Column() {
              Text('测试文字A')
                .fontColor('#0A59F7')
                .margin({ bottom: 10 });
              Text('测试文字B')
                .fontColor('#0A59F7');
            }.height(90);
          });
      }
      .width('30%')
      .attributeModifier(new YDSwiperIndicatorStyles());
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```

效果参考如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/wHTzfijpQRiwDQD0Fy4MFw/zh-cn_image_0000002628557638.png "点击放大")
