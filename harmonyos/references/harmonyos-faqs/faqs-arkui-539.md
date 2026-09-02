---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-539
title: 页面退出时，旧页面的内容与新页面的内容重叠
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面退出时，旧页面的内容与新页面的内容重叠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ca20d739c0c3c18a08a488271b46b9b69d701c5deba22339924d68b474d82af0
---

## 问题现象

页面退出时，新页面与正在退出的页面显示重叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/uJd54rYNSh6prAe94EzHWQ/zh-cn_image_0000002628391616.png "点击放大")

## 背景知识

使用[pageTransition](../harmonyos-references/ts-custom-component-lifecycle.md#pagetransition9)实现页面转场动画时，可通过设置[PageTransitionEnter](../harmonyos-references/ts-page-transition-animation.md#pagetransitionenter)和[PageTransitionExit](../harmonyos-references/ts-page-transition-animation.md#pagetransitionexit)的[slide](../harmonyos-references/ts-page-transition-animation.md#slide)属性定义从其他页面进入/退出该页面时的效果。

## 问题定位

查看该问题页面的相关设置，该页面使用PageTransitionEnter设置了转场动画，返回后的页面未使用转场动画。

```screen
// PageOne.ets
@Entry
@Component
export struct PageOne {
  build() {
    Stack() {
      Button('返回')
        .fontSize(20)
        .fontColor(Color.White)
        .type(ButtonType.Capsule)
        .width(200)
        .height(50)
        .margin({ top: 20 })
        .backgroundColor('#0A59F7')
        .onClick(() => {
          this.getUIContext().getRouter().back();
        })
    }
    .height('100%')
    .width('100%')
  }

  pageTransition() {
    // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionEnter({ duration: 1000 })
      .slide(SlideEffect.Right)
    // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Right)
  }
}
```

```screen
@Entry
@Component
struct Index {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('点击跳转')
        .fontSize(20)
        .fontColor(Color.White)
        .type(ButtonType.Capsule)
        .width(200)
        .height(50)
        .margin({ top: 20 })
        .backgroundColor('#0A59F7')
        .onClick(() => {
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/PageOne'
          });
        });
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
  // 该页面未使用转场动画
}
```

## 分析结论

该页面使用PageTransitionEnter设置了转场动画，而返回后的页面未使用转场动画，页面跳转时目的页面立即显示，原页面仍在执行转场动画，导致页面内容重叠显示。

## 修改建议

返回后的页面也使用转场动画。

```screen
@Entry
@Component
struct Index {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('点击跳转')
        .fontSize(20)
        .fontColor(Color.White)
        .type(ButtonType.Capsule)
        .width(200)
        .height(50)
        .margin({ top: 20 })
        .backgroundColor('#0A59F7')
        .onClick(() => {
          this.getUIContext().getRouter().pushUrl({
            url: 'pages/PageOne'
          });
        });
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }

  // 该页面也使用转场动画
  pageTransition() {
    // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Left);
    // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Left);
  }
}
```

PageOne.ets：

```screen
@Builder
export function PageOneBuilder() {
  PageOne();
}

@Entry
@Component
export struct PageOne {
  build() {
    Stack() {
      Button('返回')
        .fontSize(20)
        .fontColor(Color.White)
        .type(ButtonType.Capsule)
        .width(200)
        .height(50)
        .margin({ top: 20 })
        .backgroundColor('#0A59F7')
        .onClick(() => {
          this.getUIContext().getRouter().back();
        });
    }
    .height('100%')
    .width('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }

  pageTransition() {
    // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionEnter({ duration: 1000 })
      .slide(SlideEffect.Right);
    // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Right);
  }

}
```

src/main/resources/base/profile/router\_map.json：

```screen
{
  "routerMap": [
    {
      "name": "pageOne",
      "pageSourceFile": "src/main/ets/pages/PageOne.ets",
      "buildFunction": "PageOneBuilder"
    }
  ]
}
```

src/main/module.json5文件中需添加"routerMap": "$profile:router\_map"。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/DdL4pt9eQvyhh5NuB4zbzw/zh-cn_image_0000002658910833.png "点击放大")
