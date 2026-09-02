---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-52
title: 左右滑动页面切换卡顿无动效
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 左右滑动页面切换卡顿无动效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8a12c362378cf7cfb12e61eba5a35c128383a0216e4c56acb6e794f994db388c
---

## 问题现象

左右滑动页面切换时卡顿，无页面切换过渡动画效果。

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。可以通过设置[duration](../harmonyos-references/ts-container-swiper.md#duration)参数控制子组件切换的动画时长，默认时长为400毫秒，在设置duration时需要和[curve](../harmonyos-references/ts-container-swiper.md#curve8)一起使用。Swiper组件滑动过程中的关键日志如下：

  | 日志关键字 | 描述 |
  | --- | --- |
  | Swiper HandleTouchDown | 处理点击按下事件 |
  | Swiper HandleTouchUp | 处理点击抬起事件 |
  | Swiper start property animation with | 开始位移属性动画 |
  | Swiper finish property animation with | 完成位移属性动画 |
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。

## 问题定位

左右滑动页面切换时卡顿无过渡动效，可先确认采用了什么组件显示页面内容。使用ArkUI Inspector抓取页面布局，如下图可看到Swiper组件，可在右侧属性栏中查看curve和duration属性值确定页面切换的动画曲线和时长，可看到动画曲线为线性动画，而动画时长为50毫秒，可知动画时长过短，造成了卡顿、无动效的现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/6Zas30eiQoyVPRPO2HvIxA/zh-cn_image_0000002628395296.png "点击放大")

除了使用ArkUI Inspector工具，可以在日志中搜索Swiper start property animation with|Swiper finish property animation with，查看两个日志打印的时间间隔来确定Swiper组件的切换动画时长。

```shell
08-29 10:54:57.982   18874-18874  C03915/com.exa...ion/AceSwiper ...  I     Swiper start property animation ...
08-29 10:54:58.036   18874-18874  C03915/com.exa...ion/AceSwiper ...  I     Swiper finish property animation ...
```

## 分析结论

Swiper组件设置的切换动画时长较短，导致页面切换卡顿无动效。

## 修改建议

设置较长的切换动画时长。

```ts
import { image } from '@kit.ImageKit';

class SwiperItemData {
  image: image.PixelMap | ResourceStr | DrawableDescriptor = ''; // 图片

  constructor(image: image.PixelMap | ResourceStr | DrawableDescriptor) {
    this.image = image;
  }
}

class SwiperItemDataSource implements IDataSource {
  private dataArray: SwiperItemData[] = [];

  private listeners: DataChangeListener[] = [];

  totalCount(): number {
    return this.dataArray.length;
  }

  getData(index: number): SwiperItemData {
    return this.dataArray[index];
  }

  addData(data: SwiperItemData): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    this.listeners.push(listener);
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    let index = this.listeners.indexOf(listener);
    if (index >= 0) {
      this.listeners.splice(index, 1);
    }
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }
}

@Entry
@Component
struct ImageSwiperPage {
  private swiperController: SwiperController = new SwiperController();

  private swiperItemDataSource: SwiperItemDataSource = new SwiperItemDataSource();

  initPageData(): void {
    // 测试需要替换成可引用到的资源
    let data1 = new SwiperItemData($r('app.media.picture1'));
    let data2 = new SwiperItemData($r('app.media.picture2'));
    let data3 = new SwiperItemData($r('app.media.picture3'));
    let data4 = new SwiperItemData($r('app.media.picture4'));
    let data5 = new SwiperItemData($r('app.media.picture5'));
    let data6 = new SwiperItemData($r('app.media.picture6'));
    this.swiperItemDataSource.addData(data1);
    this.swiperItemDataSource.addData(data2);
    this.swiperItemDataSource.addData(data3);
    this.swiperItemDataSource.addData(data4);
    this.swiperItemDataSource.addData(data5);
    this.swiperItemDataSource.addData(data6);
  }

  aboutToAppear(): void {
    this.initPageData();
  }

  build() {
    Swiper(this.swiperController) {
      LazyForEach(this.swiperItemDataSource, (item: SwiperItemData) => {
        Image(item.image)
          .width('100%')
          .height('100%')
      })
    }
    .duration(300) // 切换动画时长设置成300ms
    .curve(Curve.Linear)
    .autoPlay(false)
    .cachedCount(2)
    .loop(false)
    .indicator(false)
    .height('100%')
    .width('100%')
  }
}
```
