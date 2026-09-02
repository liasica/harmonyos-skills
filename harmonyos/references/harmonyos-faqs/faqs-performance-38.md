---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-38
title: 左右滑动图片切换时文字没有跟随图片同步更新
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 左右滑动图片切换时文字没有跟随图片同步更新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:21f84ad08e2c8a80aa27489e4e2543b9bc76a0ae2d80629fbba4e05a90559c21
---

## 问题现象

左右滑动图片列表切换时，图片跟随手指移动距离进行切换，但图片上方的文字直到页面切换完成后才更新，有延迟。

## 背景知识

* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  Trace关键字说明：

  | 关键字 | 说明 |
  | --- | --- |
  | H:APP\_SWIPER\_SCROLL | 屏幕滑动事件（滑动期间手指不离开屏幕） |
  | H:APP\_SWIPER\_FLING | 屏幕抛滑事件（手指短暂接触屏幕触发滑动后离开屏幕） |
  | H:Create[Text][self:组件id] | 文本组件创建 |
  | H:FrameNode[Text][id:组件id]::RenderTask | 文本组件渲染绘制 |

## 问题定位

1. 使用ArkUI Inspector抓取应用布局组件树，查看图片列表和上方文字相应的组件，发现图片列表是采用Swiper组件实现，而上方的文字则是Text组件，两者均为Stack组件的子组件，Text组件覆盖在Swiper组件上。
2. 使用DevEco Profiler Frame分析工具抓取该过程的Trace信息，搜索H:APP\_SWIPER\_SCROLL和H:APP\_SWIPER\_FLING确定图片滑动切换阶段如下所示。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/oLTmXL94QU2mU_VYLDgszw/zh-cn_image_0000002628555176.png "点击放大")

   在上方搜索框中搜索文本组件渲染任务执行的Trace点H:FrameNode[Text][id:3147]::RenderTask，发现是在图片滑动切换完成之后，可知是在图片切换完成后才更新文字，导致文字更新有延迟。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/E9zaFeqRTyiNq1c9DPlIOA/zh-cn_image_0000002658914499.png "点击放大")

## 分析结论

在图片切换完成之后更新文字，导致在图片切换过程时文字没有变化，更新不同步，有延迟。

## 修改建议

可将图片和文字作为整体，当左右滑动切换图片时，文字可随图片同步切换。

```screen
import { image } from '@kit.ImageKit';

class SwiperItemData {
  content: string = ''; // 文本内容

  image: image.PixelMap | ResourceStr | DrawableDescriptor = ''; // 图片

  constructor(content: string, image: image.PixelMap | ResourceStr | DrawableDescriptor) {
    this.content = content;
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
struct ImageTextDemoPage {
  private swiperController: SwiperController = new SwiperController();

  private swiperItemDataSource: SwiperItemDataSource = new SwiperItemDataSource();

  initPageData(): void {
    // 测试需要替换成可引用到的资源
    let data1 = new SwiperItemData('页面1', $r('app.media.picture1'));
    let data2 = new SwiperItemData('页面2', $r('app.media.picture2'));
    let data3 = new SwiperItemData('页面3', $r('app.media.picture3'));
    let data4 = new SwiperItemData('页面4', $r('app.media.picture4'));
    let data5 = new SwiperItemData('页面5', $r('app.media.picture5'));
    let data6 = new SwiperItemData('页面6', $r('app.media.picture6'));
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

  @Builder
  itemBuilder(data: SwiperItemData) {
    Stack() {
      Image(data.image) // 图片
        .width('100%')
        .height('100%')
      Text(data.content) // 文本内容
        .fontSize(25)
        .fontColor(Color.White)
    }
  }

  build() {
    Swiper(this.swiperController) {
      LazyForEach(this.swiperItemDataSource, (item: SwiperItemData) => {
        this.itemBuilder(item);
      })
    }
    .autoPlay(false)
    .cachedCount(2)
    .loop(false)
    .indicator(false)
    .height('100%')
    .width('100%')
  }
}
```
