---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-919
title: Swiper如何实现3D立方体旋转切换动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Swiper如何实现3D立方体旋转切换动画效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b28158ee30d1520f1099e0ecdba44ed439f42ad876bd74893adce6081465915c
---

## 问题现象

通常Swiper组件，提供平面滑动轮播显示的效果，如何通过Swiper组件实现对子组件3D立方体旋转切换动画效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/97ClRHuASkWB4B2kH_GkUQ/zh-cn_image_0000002628400290.gif "点击放大")

## 背景知识

* [Swiper组件](../harmonyos-references/ts-container-swiper.md)：滑块视图容器组件，它提供了子组件滑动轮播显示的能力。
* [customContentTransition属性](../harmonyos-references/ts-container-swiper.md#customcontenttransition12)：用于实现自定义的过渡动画效果，该属性允许开发者通过回调函数动态控制轮播切换过程中的动画细节，特别是可结合进度参数进行精细化动画控制。
* [rotate属性](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)：主要用于设置组件的旋转，可使组件在以组件左上角为坐标原点的坐标系中进行旋转。其中，（x，y，z）指定一个矢量，作为旋转轴。旋转轴和旋转中心点都基于坐标系设定，组件发生位移时，坐标系不会随之移动。默认值：在x、y、z都不指定时，x、y、z的默认值分别为0、0、1。指定了x、y、z任何一个值时，x、y、z中未指定的值默认为0。

## 解决方案

1. 给Swiper组件内的子组件设置旋转属性rotate。

   ```screen
   Stack() {
     this.swiperItemSlotParam(item);
   }
   // 设置组件旋转
   .rotate({
     x: 0,
     y: 1,
     z: 0,
     angle: this.angleList[index],
     centerX: this.centerXList[index],
     centerY: '50%',
     centerZ: 0,
     perspective: 0
   });
   ```
2. 给Swiper组件设置页面切换动画属性customContentTransition，在页面切换时逐帧触发回调，在回调中设置子组件的rotate属性值。

   ```screen
   // 自定义Swiper页面切换动画
   .customContentTransition({
     // 页面移除视窗时超时1000ms下渲染树
     timeout: 1000,
     transition: (proxy: SwiperContentTransitionProxy) => {
       // 旋转角度
       let angle = 0;
       console.info('proxy.position===>' + proxy.position);
       console.info('proxy.index===>' + proxy.index);
       // position为index页面相对于selectedIndex对应页面的起始位置的移动比例，向左移动减小，向右移动增加。
       if (proxy.position < 0 && proxy.position > -1) {
         // 当前页向左滑出或上一页向右滑入
         angle = proxy.position * 90;
         // 设置index页面的旋转中心轴为右侧边缘
         this.centerXList[proxy.index] = '100%';
       } else if (proxy.position > 0 && proxy.position < 1) {
         // 当前页向右滑出或下一页向左滑入
         angle = proxy.position * 90;
         // 设置index页面的旋转中心轴为左侧边缘
         this.centerXList[proxy.index] = '0%';
       } else {
         // position小于-1时表示向左完全滑出区域，大于1时表示向右完全滑出区域，重置角度
         angle = 0;
       }
       // 修改index页的旋转角
       this.angleList[proxy.index] = angle;
     }
   });
   ```

完整示例参考如下：

```screen
@Component
@Entry
export struct Swiper3D {
  // Swiper数据
  private swiperList: MySwiperItem[] =
    [new MySwiperItem('模块1', '#4B48F7'),
      new MySwiperItem('模块2', '#46B1E3'),
      new MySwiperItem('模块3', '#61CFBE')]
  ;

  build() {
    Column() {
      // 轮播网格
      Custom3DComponentPage({
        items: this.swiperList,
        swiperItemSlotParam: (item: MySwiperItem) => {
          this.mySwiperItem(item);
        }
      });
    };
  }

  // 自定义3D立方体旋转轮播项UI内容
  @Builder
  mySwiperItem(item: MySwiperItem) {
    Column() {
      Text(item.title).fontSize(24);
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor(item.colors);
  }
}

export class MySwiperItem {
  // 标题
  title: string;
  // 颜色
  colors: Color | string;

  constructor(title: string, colors: Color | string) {
    this.title = title;
    this.colors = colors;
  }
}

@Component
export struct Custom3DComponentPage {
  // --------------------暴露外部属性----------------------------
  // 动画持续时间，默认500ms
  duration: number = 500;
  // 是否自动播放
  autoPlay: boolean = false;
  // 是否循环播放
  loop: boolean = true;
  // 轮播数据
  items: ESObject[] = [];
  // 轮播页插槽参数
  @BuilderParam swiperItemSlotParam: (item: ESObject) => void;
  // --------------------私有属性----------------------------
  // 当前项下标
  @State currentIndex: number = 0;
  // 旋转角度列表
  @State angleList: number[] = [];
  // 旋转中心点列表
  @State centerXList: Array<number | string> = [];
  // 轮播控制器
  private swiperController: SwiperController = new SwiperController();

  build() {
    Swiper(this.swiperController) {
      ForEach(this.items, (item: ESObject, index: number) => {
        Stack() {
          this.swiperItemSlotParam(item);
        }
        // 设置组件旋转
        .rotate({
          x: 0,
          y: 1,
          z: 0,
          angle: this.angleList[index],
          centerX: this.centerXList[index],
          centerY: '50%',
          centerZ: 0,
          perspective: 0
        });

      }, ((item: ESObject, index: number) => `${JSON.stringify(item)}_${index}`));
    }
    .loop(this.loop)
    .autoPlay(this.autoPlay)
    .duration(this.duration)
    .onChange((index: number) => {
      this.currentIndex = index;
    })
    // 自定义Swiper页面切换动画
    .customContentTransition({
      // 页面移除视窗时超时1000ms下渲染树
      timeout: 1000,
      transition: (proxy: SwiperContentTransitionProxy) => {
        // 旋转角度
        let angle = 0;
        console.info('proxy.position===>' + proxy.position);
        console.info('proxy.index===>' + proxy.index);
        // position为index页面相对于selectedIndex对应页面的起始位置的移动比例，向左移动减小，向右移动增加。
        if (proxy.position < 0 && proxy.position > -1) {
          // 当前页向左滑出或上一页向右滑入
          angle = proxy.position * 90;
          // 设置index页面的旋转中心轴为右侧边缘
          this.centerXList[proxy.index] = '100%';
        } else if (proxy.position > 0 && proxy.position < 1) {
          // 当前页向右滑出或下一页向左滑入
          angle = proxy.position * 90;
          // 设置index页面的旋转中心轴为左侧边缘
          this.centerXList[proxy.index] = '0%';
        } else {
          // position小于-1时表示向左完全滑出区域，大于1时表示向右完全滑出区域，重置角度
          angle = 0;
        }
        // 修改index页的旋转角
        this.angleList[proxy.index] = angle;
      }
    });
  }
}
```
