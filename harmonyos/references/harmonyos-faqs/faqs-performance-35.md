---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-35
title: 应用启动后停留闪屏页时间过长
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 应用启动后停留闪屏页时间过长
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ecc248673a500b54f823eabb970b9e592a0bc85a952a57ceb4cfef6d88eea6ce
---

## 问题现象

应用每次启动后都会长时间停留在闪屏页。

## 背景知识

* ArkUI Inspector是DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* [冷启动：Launch分析](../harmonyos-guides/ide-launch-overview.md)是DevEco Profiler工具提供的冷启动场景性能分析能力，可以拆解应用冷启动过程，抓取不同阶段的耗时数据，帮助开发者快速分析启动过程的耗时瓶颈，识别出导致启动缓慢的原因。
* [Timer（定时器）](../harmonyos-references/js-apis-timer.md)功能支持按照指定的时间执行对应函数，通过[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)设置指定时间。

## 问题定位

1. 使用ArkUI Inspector分别抓取引导页和登录页的布局，得知两个页面分别是SplashPage和LoginPage。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/QoCOwzEMS4W0L5H_stN7ig/zh-cn_image_0000002658794533.png)
2. 使用DevEco Profiler中的Launch模板抓取应用启动时的Trace，分别搜索SplashPage和LoginPage的创建时间，搜索关键字H:Create[XXXPage]。发现两个页面创建时间间隔10s左右，期间应用包名主线程长时间Sleeping，基本没有进行任何处理，且多次复现后发现SplashPage和LoginPage两个页面创建时间稳定在10s左右。因此推测是应用侧设置了固定的跳转时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Wiq1u7maQiiXMGHdJz08FA/zh-cn_image_0000002628555170.png "点击放大")
3. 如以下示例代码，由于设置了闪屏页10s延迟跳转登录页，造成启动后停留引导页过久的问题。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct LongSplashPage {
     message: string = `我是闪屏页，10秒后我将跳转登录页`;

     onPageShow(): void {
       setTimeout(() => {
         this.getUIContext().getRouter().pushUrl({
           url: 'pages/Index' // 目标url
         }).catch((error: BusinessError) => {
           console.error(`jump error: ${error.code}, ${error.message}`);
         });
       }, 10000); // 设置10s后跳转
     }

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('LongSplashPageHelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             this.message = 'Welcome';
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```

## 分析结论

应用通过定时器设置了从闪屏页跳转登录页的固定时间，这个固定时间过长造成了在闪屏页的停留时间过长。

## 修改建议

应用酌情减少定时器设置的时间，避免用户长时间等待。

闪屏页设置：

```ts
@Entry
@Component
struct ShortSplashPage {
  message: string = `我是闪屏页，5秒后我将跳转登录页`;

  onPageShow(): void {
    setTimeout(() => {
      this.getUIContext().getRouter().pushUrl({
        url: 'pages/Index' // 目标url
      }).catch((error: BusinessError) => {
        console.error(`jump error: ${error.code}, ${error.message}`);
      });
    }, 5000); // 设置5s后跳转
  }

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('ShortSplashPageHelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

登录页：

```ts
@Entry
@Component
struct Index {
  @State message: string = '我是登录页';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
