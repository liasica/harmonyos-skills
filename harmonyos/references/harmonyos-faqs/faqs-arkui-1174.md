---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1174
title: 如何解决Swiper组件未显示页面无法截图的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何解决Swiper组件未显示页面无法截图的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7ae057f454fd5a4bac57ad34b17b4f87b5f32f12b37c7c4ce998187c1f14703f
---

## 问题现象

通过getComponentSnapshot.get接口识别组件id进行截图时，Swiper第一个页面能正常截图，后续的页面会截图失败。

问题代码示例参考如下：

```screen
@Builder
buildPreviewContent() {
  RelativeContainer() {
    Swiper() {
      LazyForEach(this.timeRecordTextPreviewVM.lazyTextList, (item: string, index: number) => {
        this.buildPreviewContentItem(item, index) // 需要截图的组件
      }, (item: TimeTextPictureTemplateModel) => JSON.stringify(item))
    }

    .id('swiperShot')
  }
  .width('100%')
  .height(this.timeRecordTextPreviewVM.imageHeight + 22)
}

// 预览样式内容item
@Builder
buildPreviewContentItem(item: string, index: number) {
  RelativeContainer() {
    Stack() {
      // ...
    }
    .id('containerShot' + index)
  }
  .width('100%')
  .height(this.timeRecordTextPreviewVM.imageHeight)
  .borderRadius(20)
  .backgroundColor('#FFFFFFFF')
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/ctEG3dmeQi64IDcCdRFmIg/zh-cn_image_0000002658809147.gif "点击放大")

## 背景知识

* [UIContext.getComponentSnapshot().get()](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12)：获取已加载的组件的截图，传入组件的组件标识，找到对应组件进行截图。通过回调返回结果。
* [Swiper](../harmonyos-references/ts-container-swiper.md)：滑块视图容器，提供子组件滑动轮播显示的能力。该组件会按需加载Swiper页面。

## 解决方案

由于Swiper后续页面未加载渲染，导致componentSnapshot.get方法无法获取到未加载的组件，所以第一个页面截图成功，后续页面截图失败，可以考虑以下两种方案实现Swiper后续页面截图：

* **方案一**：采用[UIContext.getComponentSnapshot().createFromBuilder()](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfrombuilder12)方法。该方法在应用后台渲染CustomBuilder自定义组件，并输出其截图。通过回调返回结果并支持在回调中获取离屏组件绘制区域坐标和大小。实现方式可参考[componentSnapshot.createFromBuilder示例](../harmonyos-references/js-apis-arkui-componentsnapshot.md#componentsnapshotcreatefrombuilderdeprecated)。
* **方案二**：采用[cachedCount](../harmonyos-references/ts-container-swiper.md#cachedcount15)预加载的方式加载Swiper后续页面，再用componentSnapshot.get方法进行截图。

  实现方式如下：

  1. Swiper使用cachedCount属性预加载5个页面。
  2. componentSnapshot.get获取第4个页面，并赋值给Image显示。

     ```ts
     import { image } from '@kit.ImageKit';

     class MyDataSource implements IDataSource {
       private list: number[] = [];

       constructor(list: number[]) {
         this.list = list;
       }

       totalCount(): number {
         return this.list.length;
       }

       getData(index: number): number {
         return this.list[index];
       }

       registerDataChangeListener(): void {
       }

       unregisterDataChangeListener() {
       }
     }

     @Entry
     @Component
     struct SwiperExample {
       private swiperController: SwiperController = new SwiperController();
       private data: MyDataSource = new MyDataSource([]);
       @State pixmap: image.PixelMap | undefined = undefined;
       @State pixmap2: image.PixelMap | undefined = undefined;
       @State myScale: number = 1.0;
       @State myOpacity: number = 1.0;

       aboutToAppear(): void {
         let list: number[] = [];
         for (let i = 1; i <= 10; i++) {
           list.push(i);
         }
         this.data = new MyDataSource(list);
       }

       build() {
         Column({ space: 5 }) {
           Text('预加载5个Swiper页面');
           Swiper(this.swiperController) {
             LazyForEach(this.data, (item: string) => {
               Column() {
                 Text(item.toString())
                   .width('90%')
                   .height(160)
                   .backgroundColor(0xAFEEEE)
                   .textAlign(TextAlign.Center)
                   .fontSize(30)
                   .scale({
                     x: this.myScale,
                     y: this.myScale
                   }) // 设置x轴/y轴的缩放
                   .opacity(this.myOpacity);
               }
               .width('90%')
               .height(160)
               .id(item.toString()); // 设置Swiper页面标识
             }, (item: string) => item);
           }
           .cachedCount(5, true) // 预加载5个页面,同时挂载运行
           .curve(Curve.Linear);

           Button('开始动画')
             .onClick(() => {
               this.getUIContext().animateTo({
                 duration: 3000,
                 curve: Curve.EaseInOut,
                 iterations: -1, // 设置-1表示动画无限循环
                 playMode: PlayMode.Normal
               },
                 () => {
                   this.myOpacity = 0.5;
                   this.myScale = 0.5;
                 });
             });
           Button('获取第1个与第4个Swiper页面')
             .onClick(() => {
               // 获取Swiper第四个页面截图
               this.getUIContext().getComponentSnapshot().get('4', (error: Error, pixmap: image.PixelMap) => {
                 if (error) {
                   console.info(`error:${JSON.stringify(error)}`);
                   return;
                 }
                 this.pixmap = pixmap;
               }, { scale: 2, waitUntilRenderFinished: true });
               // 获取Swiper第一个页面截图
               this.getUIContext().getComponentSnapshot().get('1', (error: Error, pixmap: image.PixelMap) => {
                 if (error) {
                   console.info(`error:${JSON.stringify(error)}`);
                   return;
                 }
                 this.pixmap2 = pixmap;
               }, { scale: 2, waitUntilRenderFinished: true });
             });
           Text('显示截下的第4个Swiper页面');
           Image(this.pixmap)
             .width('90%')
             .height(160)
             .margin(5);
           Text('显示截下的第1个Swiper页面');
           Image(this.pixmap2)
             .width('90%')
             .height(160)
             .margin(5);
         }.width('100%')
         .margin({ top: 5 });
       }
     }
     ```

## 常见FAQ

Q：如何解决LazyForEach渲染的List列表，超出屏幕外ListItem截图失败的问题？

A：LazyForEach渲染数据时也是按需加载，未加载的Item无法采用componentSnapshot.get截图，采取的解决方案与Swiper一致，上述两种方案均可实现。

## 总结

由上述方案及FAQ可知Swiper组件由于本身是按需加载的，与LazyForEach渲染的其它滚动与滑动组件一样，都存在未显示的Item无法截图的问题，都可以采用方案一和方案二解决，其区别如下：

| 方案 | 优缺点 |
| --- | --- |
| 方案一 | 1. builder中的组件不支持设置动画相关的属性，如transition等。 2. 部分执行耗时任务的组件可能无法及时在截图前加载完成，因此会截取不到加载成功后的图像。例如：加载网络图片的Image组件、Web组件。 |
| 方案二 | 1. 只是适用于List、Swiper、Grid等有cachedCount属性的滑动与滚动组件，适用范围较小。 2. 当需要截图的组件在列表的靠后组件时，由于cachedCount同时预加载过多组件会消耗更多性能。 3. API15的cachedCount属性支持componentSnapshot.get在动画过程中截图，若截图的组件有动画，该方案可以实现动画属性过程中截图，该优点能保证截图与当前页面截图效果一致。 |
