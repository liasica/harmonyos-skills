---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lottie-animation-destroy-check
title: "@performance/lottie-animation-destroy-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/lottie-animation-destroy-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ad028ffb6eba46342ab8a5fb44394e261db23ee95dc26161a9fa6ba75fbe55c4
---

该规则检测使用lottie加载的动画是否都正确销毁。

当使用lottie加载动画时，一般需要先通过lottie.loadAnimation将动画加载到内存，动画执行完毕后需要在合适的时机（例如：onDisAppear，onPageHide，aboutToDisappear）通过调用animationItem的destroy方法将单个动画销毁或者调用lottie.destroy()方法将当前页面所有动画销毁，如果动画未被销毁就会造成资源浪费，影响应用性能体验。

内存优化场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/lottie-animation-destroy-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例1

```screen
import lottie from '@ohos/lottie';   //需安装@ohos/lottie依赖后import
import { AnimationItem } from '@ohos/lottie';    //需安装@ohos/lottie依赖后import

const FRAME_START: number = 60;
const FRAME_END: number = 120;

@Entry
@Component
struct LottieAnimation1 {
  private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
  private politeChicky: string = 'politeChicky';
  private politeChickyPath: string = 'media/politeChicky.json';
  private animateItem?: AnimationItem;

  build() {
    Canvas(this.politeChickyController)
      .width(160)
      .height(160)
      .borderRadius(3)
      .onReady(() => {
        this.animateItem = lottie.loadAnimation({
          container: this.politeChickyController,
          renderer: 'canvas',
          loop: true,
          autoplay: true,
          name: this.politeChicky,
          path: this.politeChickyPath,
          initialSegment: [FRAME_START, FRAME_END]
        })
      })
      .onDisAppear(() => {
        this.animateItem?.destroy();//只加载了一个Animation，可以使用animateItem的destroy接口
      })
  }
}
```

## 正例2

```screen
import lottie from '@ohos/lottie';
import { AnimationItem } from '@ohos/lottie';

// 动画播放的起始帧
const FRAME_START: number = 60; 
// 动画播放的终止帧
const FRAME_END: number = 120; 

@Entry
@Component
struct LottieAnimation2 {
  private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
  // 动画名称
  private politeChicky: string = 'politeChicky'; 
  // hap包内动画资源文件路径，仅支持json格式
  private politeChickyPath: string = 'media/politeChicky.json'; 
  private animateItem: AnimationItem | null = null;

  build() {
    Canvas(this.politeChickyController)
      .width(160)
      .height(160)
      .borderRadius(3)
      .onReady(() => {
        this.animateItem = lottie.loadAnimation({
          container: this.politeChickyController,
          renderer: 'canvas',
          loop: true,
          autoplay: true,
          name: 'anim_name1',
          path: this.politeChickyPath,
          initialSegment: [FRAME_START, FRAME_END]
        })
      })
      .onClick(() => {
        this.animateItem = lottie.loadAnimation({
          container: this.politeChickyController,
          renderer: 'canvas',
          loop: true,
          autoplay: true,
          name: 'anim_name2',
          path: this.politeChickyPath,
          initialSegment: [FRAME_START, FRAME_END]
        })
      })
  }

  onPageHide(): void {
    lottie.destroy();
  }
}
```

## 反例1

```screen
import lottie from '@ohos/lottie';
import { AnimationItem } from '@ohos/lottie';

const FRAME_START: number = 60;
const FRAME_END: number = 120;

@Entry
@Component
struct LottieAnimation1 {
  private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
  private politeChicky: string = 'politeChicky';
  private politeChickyPath: string = 'media/politeChicky.json';
  private animateItem?: AnimationItem;

  build() {
    Canvas(this.politeChickyController)
      .width(160)
      .height(160)
      .backgroundColor(Color.Gray)
      .borderRadius(3)
      .onReady(() => {
        //告警
        this.animateItem = lottie.loadAnimation({
          container: this.politeChickyController,
          renderer: 'canvas',
          loop: true,
          autoplay: true,
          name: this.politeChicky,
          path: this.politeChickyPath,
          initialSegment: [FRAME_START, FRAME_END]
        })
      })
  }
}
```

## 反例2

```screen
import lottie from '@ohos/lottie';
import { AnimationItem } from '@ohos/lottie';

// 动画播放的起始帧
const FRAME_START: number = 60; 
// 动画播放的终止帧
const FRAME_END: number = 120; 

//调用多次loadAnimation，但是只在onDisAppear销毁一次
@Entry
@Component
struct LottieAnimation4 {
  private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
  // 动画名称  
  private politeChicky: string = 'politeChicky'; 
  // hap包内动画资源文件路径，仅支持json格式
  private politeChickyPath: string = 'media/politeChicky.json'; 
  private animateItem: AnimationItem | null = null;
  // 初始化点击次数 
  @State times: number = 0; 

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      // 动画
      Canvas(this.politeChickyController)
        .width(160)
        .height(160)
        .backgroundColor(Color.Gray)
        .borderRadius(3)
        .onReady(() => {
          this.animateItem = lottie.loadAnimation({
            container: this.politeChickyController,
            renderer: 'canvas',
            loop: true,
            autoplay: true,
            name: this.politeChicky,
            path: this.politeChickyPath,
            initialSegment: [FRAME_START, FRAME_END]
          })
        })
        .onClick(() => {
          this.animateItem = lottie.loadAnimation({
            container: this.politeChickyController,
            renderer: 'canvas',
            loop: true,
            autoplay: true,
            name: this.politeChicky,
            path: this.politeChickyPath,
            initialSegment: [FRAME_START, FRAME_END]
          })
          this.times++;
        })
        .onDisAppear(()=> {
          //上报此处animateItem，描述description不一样，如果无法找到动画名称，则直接建议用lottie.destroy
          this.animateItem?.destroy();
        })
      // 响应动画的文本
      Text('text')
        .fontSize(16)
        .margin(10)
        .fontColor(Color.White)
    }.margin({ top: 20 })
  }
}
```

## 反例3

```screen
import lottie from '@ohos/lottie';
import { AnimationItem } from '@ohos/lottie';

// 动画播放的起始帧
const FRAME_START: number = 60; 
// 动画播放的终止帧
const FRAME_END: number = 120; 

//调用了销毁，但是不是全部销毁，上报
@Entry
@Component
struct LottieAnimation5 {
  private politeChickyController: CanvasRenderingContext2D = new CanvasRenderingContext2D();
  // 动画名称 
  private politeChicky: string = 'politeChicky'; 
  // hap包内动画资源文件路径，仅支持json格式
  private politeChickyPath: string = 'media/politeChicky.json'; 
  private animateItem: AnimationItem | null = null;

  build() {
    Canvas(this.politeChickyController)
      .width(160)
      .height(160)
      .backgroundColor(Color.Gray)
      .borderRadius(3)
      .onReady(() => {
        this.animateItem = lottie.loadAnimation({
          container: this.politeChickyController,
          renderer: 'canvas',
          loop: true,
          autoplay: true,
          name: 'anim_name1',
          path: this.politeChickyPath,
          initialSegment: [FRAME_START, FRAME_END]
        })
      })
      .onClick(()=> {
        this.animateItem = lottie.loadAnimation({
          container: this.politeChickyController,
          renderer: 'canvas',
          loop: true,
          autoplay: true,
          name: 'anim_name2',
          path: this.politeChickyPath,
          initialSegment: [FRAME_START, FRAME_END]
        })
      })
      .onDisAppear(()=>{
        //上报lottie,只销毁一个
        lottie.destroy('anim_name2');
      })
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
