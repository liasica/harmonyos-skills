---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-811
title: 如何解决Stack组件下子组件高度与层级问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Stack组件下子组件高度与层级问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1f41bea30ec582b5491d2300d3b227b98d3db2f7643cbf12a2189bbdb13543bc
---

## 问题现象

在Stack组件中如何实现如下两种布局方式：

* 在未设置Stack高度的情况下，以子组件A的内容高度为最大高度，且子组件B高度与A保持一致。
* 在Stack容器中始终让高度小的组件显示在上层。

## 背景知识

* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)：设置组件的堆叠顺序。同一容器中兄弟组件显示层级关系。zIndex值越大，显示层级越高。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。

## 解决方案

* 针对问题一：由于Stack通常用于叠加子组件，默认情况下，它的尺寸会适应所有子组件中最大的。可以用onAreaChange监听子组件A高度变化并传递给子组件B，示例代码如下。

  ```ts
  @Entry
  @Component
  struct Page1 {
    @State heightA: number = 0;

    build() {
      Stack() {
        this.componentA();
        this.componentB();
      }
    }

    @Builder
    componentA() {
      Column() {
        Text('HarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOS')
          .width('100%')
          .backgroundColor('#f1f3f5')
        Text('HarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOS')
          .width('100%')
          .backgroundColor('#d1d1d6')
      }
      .onAreaChange((oldValue, newValue) => {
        this.heightA = newValue.height as number;
      })
    }

    @Builder
    componentB() {
      Text('我是没有设置高度也没有内容撑开的组件')
        .textAlign(TextAlign.Center)
        .fontColor(Color.White)
        .width('100%')
        .height(this.heightA)
        .backgroundColor('#66000000')
    }
  }
  ```

  运行效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/MEX3kJS4SnSn-7_EmoBVfA/zh-cn_image_0000002658917115.png "点击放大")
* 针对问题二：可以使用onAreaChange获取组件A和组件B的高度，并且通过组件的高度对比设置对应的zIndex来实现，示例代码如下。

  ```ts
  @Entry
  @Component
  struct Page2 {
    @State heightA: number = 0;
    @State heightB: number = 0;

    build() {
      Stack() {
        this.componentB();
        this.componentA();
      }
    }

    @Builder
    componentA() {
      Column() {
        Text('HarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOS')
          .width('100%')
          .backgroundColor('#f1f3f5')
        Text('HarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOSHarmonyOS')
          .width('100%')
          .backgroundColor('#d1d1d6')
      }
      .zIndex(this.heightA > this.heightB ? 1 : 2)
      .onAreaChange((oldValue, newValue) => {
        this.heightA = newValue.height as number;
      })
    }

    @Builder
    componentB() {
      Column() {
        Text('这是没有内容撑开的B组件在上层')
          .fontColor(Color.White)
          .textAlign(TextAlign.Center)
          .width('100%')
          .backgroundColor('#66000000')

      }.onAreaChange((oldValue, newValue) => {
        this.heightB = newValue.height as number;
      })
      .zIndex(this.heightB > this.heightA ? 1 : 2)
    }
  }
  ```

  运行效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/LYlx4f4aQ-6EmfGF89vuew/zh-cn_image_0000002628397894.png "点击放大")
