---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1070
title: 如何根据不同的路由来源执行不同的转场动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何根据不同的路由来源执行不同的转场动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dd9d0a51de7604f0514860d43c7e680633abebfde4d48cf6644454ef2c28e2f2
---

## 问题现象

设置转场动画时，如何根据来源页面的不同执行不同的转场动画？例如A页面跳转B页面时执行一种动画，C页面跳转B页面时执行另一种动画。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Cg2cuFhNRTCvYvYZ9fwm9w/zh-cn_image_0000002658926437.png "点击放大")

## 背景知识

* [pageTransition](../harmonyos-references/ts-page-transition-animation.md)是页面间转场动画，包括入场动画PageTransitionEnter和离场动画PageTransitionExit。
* [Router](../harmonyos-references/arkts-apis-uicontext-router.md)路由可以在跳转时通过params参数传递数据，并通过[getParams](../harmonyos-references/arkts-apis-uicontext-router.md#getparams)获取传递的数据。
* [customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)是Navigation路由下的转场动画设置，可以直接通过参数from，to的方式定义具体两个页面直接的转场动画。

## 解决方案

* **场景一**：Navigation导航下的实现方式。

  参考官网[示例13（自定义转场动画）](../harmonyos-references/ts-basic-components-navigation.md#示例13自定义转场动画)，通过from，to的方式即可根据不同的路由来源执行不同的转场动画。
* **场景二**：Router导航下的实现方式。

  以入场动画为例：从Index页面进入Page1时，执行一个平移的入场动画，从Page2进入Page1时，执行一个缩放的入场动画。

  1. 定义用于控制动画执行的参数类。

     ```ts
     class TransitionTranslateClass {
       x?: number | string;
       y?: number | string;
       z?: number | string;

       constructor(x?: number | string, y?: number | string, z?: number | string,) {
         this.x = x;
         this.y = y;
         this.z = z;
       }
     }

     class TransitionScaleClass {
       x?: number;
       y?: number;
       z?: number;
       centerX?: number | string;
       centerY?: number | string;

       constructor(x?: number, y?: number, z?: number, centerX?: number | string, centerY?: number | string) {
         this.x = x;
         this.y = y;
         this.z = z;
         this.centerX = centerX;
         this.centerY = centerY;
       }
     }
     ```
  2. 在组件中创建参数类的实例，并通过该实例执行动画。

     ```ts
     transitionTranslate: TransitionTranslateClass = new TransitionTranslateClass();
     transitionScale: TransitionScaleClass = new TransitionScaleClass();
     ```

     ```ts
     pageTransition() {
       PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
         .slide(this.transitionSlide)
         .opacity(this.transitionOpacity)
         .translate(this.transitionTranslate)
         .scale(this.transitionScale)
         .onEnter((type: RouteType) => {
           if (type === RouteType.Push || type === RouteType.Pop) {
           }
         });
     }
     ```
  3. 通过getParam获取的参数，决定给哪个参数类实例赋怎样的值，当不赋值时，对应的实例为undefined，因此不执行对应的动画效果。

     ```ts
     onPageShow(): void {
       let params = this.getUIContext().getRouter().getParams() as Record<string, string | number>;
       let data: string = params?.data as string;
       if (data === 'Index') {
         this.transitionTranslate = new TransitionTranslateClass(30, 30, 30);
       } else if (data === 'Page2') {
         this.transitionScale = new TransitionScaleClass(2, 2, 2);
       }
     }
     ```

  完整示例参考如下：

  ```ts
  // Index.ets
  @Entry
  @Component
  struct Index {
    build() {
      RelativeContainer() {
        Text('Index')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1', params: { data: 'Index' } });
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  ```ts
  // Page1.ets
  class TransitionTranslateClass {
    x?: number | string;
    y?: number | string;
    z?: number | string;

    constructor(x?: number | string, y?: number | string, z?: number | string,) {
      this.x = x;
      this.y = y;
      this.z = z;
    }
  }

  class TransitionScaleClass {
    x?: number;
    y?: number;
    z?: number;
    centerX?: number | string;
    centerY?: number | string;

    constructor(x?: number, y?: number, z?: number, centerX?: number | string, centerY?: number | string) {
      this.x = x;
      this.y = y;
      this.z = z;
      this.centerX = centerX;
      this.centerY = centerY;
    }
  }

  @Entry
  @Component
  struct Page1 {
    transitionSlide: SlideEffect = 0;
    transitionOpacity: number = 1;
    transitionTranslate: TransitionTranslateClass = new TransitionTranslateClass();
    transitionScale: TransitionScaleClass = new TransitionScaleClass();

    onPageShow(): void {
      let params = this.getUIContext().getRouter().getParams() as Record<string, string | number>;
      let data: string = params?.data as string;
      if (data === 'Index') {
        this.transitionTranslate = new TransitionTranslateClass(30, 30, 30);
      } else if (data === 'Page2') {
        this.transitionScale = new TransitionScaleClass(2, 2, 2);
      }
    }

    build() {
      RelativeContainer() {
        Text('Page1')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({ url: 'pages/Page2' });
          });
      }
      .height('100%')
      .width('100%');
    }

    pageTransition() {
      PageTransitionEnter({ duration: 1200, curve: Curve.Linear })
        .slide(this.transitionSlide)
        .opacity(this.transitionOpacity)
        .translate(this.transitionTranslate)
        .scale(this.transitionScale)
        .onEnter((type: RouteType) => {
          if (type === RouteType.Push || type === RouteType.Pop) {
          }
        });
    }
  }
  ```

  ```ts
  // Page2.ets
  @Entry
  @Component
  struct Page2 {
    build() {
      RelativeContainer() {
        Text('Page2')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.getUIContext().getRouter().pushUrl({ url: 'pages/Page1', params: { data: 'Page2' } });
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  main\_pages.json文件配置：

  ```json
  {
    "src": [
      "pages/Index",
      "pages/Page1",
      "pages/Page2"
    ]
  }
  ```
