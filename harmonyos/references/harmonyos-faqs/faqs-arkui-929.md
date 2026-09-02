---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-929
title: 如何解决自定义组件设置margin后，点击下层区域无响应的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决自定义组件设置margin后，点击下层区域无响应的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:368a952b16c12a8abf9a29c852693688890e38194017334bd0ff70d5af61799b
---

## 问题现象

在如下图所示的Stack组件中，有个Row组件A，以及堆叠顺序在A上方的自定义组件IconView（设置了IconView的zIndex(1)），IconView的组件区域为Row组件B，C区域是通过margin形成的布局边界。点击C区域，不会响应A组件的点击事件。如何使得布局边界C也能响应A组件的点击事件？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/noq67_9vTQSXoYI5R9Axpg/zh-cn_image_0000002658919545.png "点击放大")

示例代码如下：

```ts
@Entry
@Component
struct Index {
  build() {
    Stack({
      alignContent: Alignment.BottomStart
    }) {

      IconView()
        .zIndex(1)

      Row() {
      }
      .id('A')
      .height('100%')
      .width('100%')
      .backgroundColor(Color.Blue)
      .onClick(() => {
        try {
          this.getUIContext().getPromptAction().showToast({
            message: '点击A组件'
          })
        } catch (error) {
          console.error(error)
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}

@Component
export struct IconView {
  build() {
    Row() {

    }
    .margin({
      bottom: 110
    })
    .size({
      width: 100,
      height: 200
    })
    .id('B')
    .backgroundColor(Color.Black)
    .onClick(() => {
      try {
        this.getUIContext().getPromptAction().showToast({
          message: '点击B组件'
        })
      } catch (error) {
        console.error(error)
      }
    })
  }
}
```

## 背景知识

* [布局元素组成](../harmonyos-guides/arkts-layout-development-overview.md#布局元素的组成)：margin在组件布局中的位置位于组件最外围。
* [自定义组件通用样式](../harmonyos-guides/arkts-create-custom-components.md#自定义组件通用样式)：ArkUI给自定义组件设置样式时，相当于给ChildComponent套了一个不可见的容器组件，这些样式是设置在容器组件上，而非直接设置给ChildComponent的Button组件。渲染结果显示，背景颜色红色并没有直接设置到Button上，而是设置在Button所在的不可见容器组件上。
* [触摸测试响应模式](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)：hitTestBehavior属性用于设置不同的触摸测试响应模式，影响触摸测试收集结果及后续事件分发。

## 解决方案

自定义组件IconView设置zIndex后，B区域和C区域都属于IconView的一部分，点击C区域时响应的是IconView的点击事件，设置IconView().onClick(() => {})可以观察到。

触摸测试响应的默认模式HitTestMode.Default会阻塞兄弟节点的触摸测试，即IconView的触摸响应阻塞A组件的触摸响应，因此点击C区域，不会响应A组件的点击事件。若需要点击C区域时可以响应A组件的点击事件，存在如下两种解决方案：

* 方案一：设置IconView的触摸测试响应模式为HitTestMode.None。此时IconView自身不响应触摸测试，且不会阻塞子节点B和兄弟节点A的触摸测试。

  ```ts
  IconView()
    .zIndex(1)
    .hitTestBehavior(HitTestMode.None);
  ```
* 方案二：IconView不设置任何属性，而把z序控制设置在B组件上。此时IconView不存在不可见的容器组件，C区域仅为布局边界，不阻塞A组件的触摸测试。

  ```screen
  @Entry
  @Component
  struct HitTestBehaviorDemo2 {
    build() {
      Stack({
        alignContent: Alignment.BottomStart
      }) {

        IconView();

        Row() {
        }
        .id('A')
        .height('100%')
        .width('100%')
        .backgroundColor(Color.Blue)
        .onClick(() => {
          try {
            this.getUIContext().getPromptAction().showToast({
              message: '点击A组件'
            });
          } catch (error) {
            console.error(error);
          }
        });
      }
      .height('100%')
      .width('100%');
    }
  }

  @Component
  export struct IconView {
    build() {
      Row() {

      }
      .margin({
        bottom: 110
      })
      .zIndex(1) // z序控制设置在自定义组件中
      .size({
        width: 100,
        height: 200
      })
      .id('B')
      .backgroundColor(Color.Black)
      .onClick(() => {
        try {
          this.getUIContext().getPromptAction().showToast({
            message: '点击B组件'
          });
        } catch (error) {
          console.error(error);
        }
      });
    }
  }
  ```
