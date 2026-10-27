---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0012
title: Swiper嵌套Image显示图片失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > Swiper嵌套Image显示图片失败
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:00+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:4c861e5ee6c441e3a5b9c16ae62ddd39cc9faaa66e9f5865bc7489f7029d72a5
---

## 问题现象

在Swiper组件中套用Image组件绑定onComplete事件，用图片实际绘制的宽度contentWidth、高度contentHeight作为图片的宽度和高度，Image组件不显示图片。

问题代码示例参考如下：

```ts
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

## 定位过程

程序运行的UI现象：Swiper未显示。

查看打印的数据信息：图片加载并解码后的数据。除图片实际宽高外，组件宽高和图片绘制宽高均为0。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/fDn1RiDVR-ay2xG6MOhEEA/zh-cn_image_0000002772679740.png)

## 分析结论

问题代码的组件结构为：Column->Swiper->Image。

由于初始未设置Swiper组件的宽高，则默认为0。且Image组件受限于父组件Swiper，绘制宽高为0，所以图片显示的大小为0。Swiper未设置宽高时自适应子组件大小，由于Image组件也未能撑开，所以在UI界面中，Swiper和Image均不显示。

## 修改建议

在初始化时设置Swiper的宽高，保留Image组件绘制图片的空间，则组件宽高和图片实际绘制宽高不会为0，图片能正常显示。

```ts
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/PmLnXXynRQ-hzePrfYVrTQ/zh-cn_image_0000002802119565.png)
