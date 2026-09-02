---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1447
title: 如何解决Swiper过早渲染导致渲染失败的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Swiper过早渲染导致渲染失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d1df423afe3fd897b6735726ecdaf6f710eb6f0af7b40c3e19df3d2ed79e808e
---

## 问题现象

在Swiper组件中，在aboutToAppear回调中调用接口方法获取图片资源，Swiper组件却无法显示图片，如何解决这种情况下Swiper渲染失败问题？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/L6EWM-OgTNmdWmEZmXyVDg/zh-cn_image_0000002658963479.png "点击放大")

## 背景知识

[Swiper](../harmonyos-references/ts-container-swiper.md)组件是滑块视图容器，能够提供给子组件滑动轮播显示的能力。[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数在创建自定义组件的新实例后，在执行其build函数之前执行。

## 解决方案

通过请求数据创建页面时，存在加载网络资源等场景，由于网速等一些条件限制，可能出现数据接收晚于页面渲染完成的情况，导致页面没有渲染对象从而显示空白。

可以通过设置状态变量，对Swiper组件设置判断来控制Swiper组件的渲染，保证Swiper组件在获取图片资源之后再渲染，避免网络波动导致Swiper在没有获取数据的情况下渲染。在aboutToAppear方法中使用计时器来模拟网络延迟的情况。

```ts
class MySpecialDataSourceTwo implements IDataSource {
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
struct SwiperPrematureRendering {
  private swiperController: SwiperController = new SwiperController();
  @State data: MySpecialDataSourceTwo = new MySpecialDataSourceTwo([]);
  @State isShow: boolean = false; // 设置一个标志位状态用来控制轮播图组件的显隐

  aboutToAppear(): void {
    // 模拟网络请求获取轮播图数据
    setTimeout(() => {
      let list: number[] = [];
      for (let i = 1; i <= 10; i++) {
        list.push(i);
      }
      this.data = new MySpecialDataSourceTwo(list);
      this.isShow = true;
    }, 3000);

  }

  build() {
    Column({ space: 5 }) {
      if (this.isShow) {
        Column() {
          Swiper(this.swiperController) {
            LazyForEach(this.data, (item: string) => {
              Text(item.toString())
                .width('90%')
                .height(160)
                .backgroundColor(0xAFEEEE)
                .textAlign(TextAlign.Center)
                .fontSize(30);
            }, (item: string) => item);
          }
          .cachedCount(2)
          .index(1)
          .autoPlay(true)
          .interval(4000)
          .loop(true)
          .duration(300);
        }.width('100%').justifyContent(FlexAlign.Center);
      } else {
        Text('loading.....').margin(20).textAlign(TextAlign.Center).width('100%');
      }
    };
  }
}
```
