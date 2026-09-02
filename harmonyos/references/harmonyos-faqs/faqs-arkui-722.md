---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-722
title: Swiper嵌套Image显示图片失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper嵌套Image显示图片失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8e047e22e55cc254c720ec05ccdfe5a564567cee6c299ff8a72adff236885cba
---

## 问题现象

在Swiper组件中套用Image组件绑定onComplete事件，用图片实际绘制的宽度contentWidth、高度contentHeight作为图片的宽度和高度，Image组件不显示图片。

问题代码示例参考如下：

```screen
@Entry
@Component
struct SwiperImageDemo {
  @State contentWidth: number = 0;
  @State contentHeight: number = 0;

  build() {
    Column() {
      Swiper() {
        Image($r('app.media.img1')) // 图片资源需自行配置
          .onComplete((event) => {
            this.contentWidth = event!.contentWidth;
            console.info('this.contentWidth', this.contentWidth);
            this.contentHeight = event!.contentWidth;
            console.info('this.contentHeight', this.contentHeight);
            console.info('complete', JSON.stringify(event, null, 2));
          })
          .width(this.contentWidth + 'px')
          .height(this.contentHeight + 'px');
      };
    }
    .width('100%')
    .height('100%');
  }
}
```

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)滑块视图容器，提供子组件滑动轮播显示的能力。
* Image加载图片的使用和注意事项请参考[存档图类型数据源](../harmonyos-guides/arkts-graphics-display.md#存档图类型数据源)。
* [onComplete](../harmonyos-references/ts-basic-components-image.md#oncomplete)在图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸，其中包含以下数据：
  + width、height为图片实际宽高。
  + componentWidth、componentHeight为Image组件宽高。
  + contentWidth、contentHeight为图片实际绘制宽高。

## 问题定位

程序运行的UI现象：Swiper未显示。

查看打印的数据信息：图片加载并解码后的数据。除图片实际宽高外，组件宽高和图片绘制宽高均为0。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/BrdtZeKYRrKOqQi0EJfbTA/zh-cn_image_0000002658794583.png)

## 分析结论

问题代码的组件结构为：Column->Swiper->Image。

由于初始未设置Swiper组件的宽高，则默认为0。且Image组件受限于父组件Swiper，绘制宽高为0，所以图片显示的大小为0。Swiper未设置宽高时自适应子组件大小，由于Image组件也未能撑开，所以在UI界面中，Swiper和Image均不显示。

## 修改建议

在初始化时设置Swiper的宽高，保留Image组件绘制图片的空间，则组件宽高和图片实际绘制宽高不会为0，图片能正常显示。

```screen
@Entry
@Component
struct SwiperImageDemo {
  @State contentWidth: number = 0;
  @State contentHeight: number = 0;

  build() {
    Column() {
      Swiper() {
        Image($r('app.media.img1')) // 图片资源需自行配置
          .onComplete((event) => {
            this.contentWidth = event!.contentWidth;
            console.info('this.contentWidth', this.contentWidth);
            this.contentHeight = event!.contentHeight;
            console.info('this.contentHeight', this.contentHeight);
            console.info('complete', JSON.stringify(event, null, 2));
          })
          .width(this.contentWidth + 'px')
          .height(this.contentHeight + 'px');
      }.height('100%')
      .width('100%'); // 为Swiper设置宽高
    }
    .width('100%')
    .height('100%');
  }
}
```

查看打印的图片尺寸信息：组件宽高和图片实际绘制宽高大于0。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/ZnFXejk_S6y75VgMigt6XA/zh-cn_image_0000002628555216.png)
