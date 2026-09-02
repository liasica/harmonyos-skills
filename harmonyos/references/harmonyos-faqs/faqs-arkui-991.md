---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-991
title: 如何实现旋转共享元素转场
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现旋转共享元素转场
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:75d799f406aeefc864816a8180d52b4e6f4b2853e1de361e0ed5478d0c8ef14c
---

## 问题现象

利用共享元素转场实现页面跳转，跳转前页面是竖向展示，跳转后页面是横向展示，如何实现该场景？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Awck5x6eSaKFIpwqxqcPqQ/zh-cn_image_0000002628561716.png "点击放大")

## 背景知识

* [组件内隐式共享元素转场 (geometryTransition)](../harmonyos-references/ts-transition-animation-geometrytransition.md)：在视图切换过程中提供丝滑的上下文传承过渡。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)：设置组件旋转。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

在NavDestination子页面中实现该共享元素转场场景，步骤如下：

1. 定义页面路由关系，在页面加载时切换到页面B。

   ```screen
   aboutToAppear(): void {
     this.navPathStack.replacePath({ name: 'nextA' }, false);
   }

   @Builder
   navPathMapBuilder(name: string) {
     if (name === 'nextA') {
       NextA();
     } else if (name === 'nextB') {
       NextB();
     }
   }

   build() {
     Navigation(this.navPathStack)
       .navDestination(this.navPathMapBuilder)
       .hideNavBar(true);
   }
   ```
2. 在页面B和页面C上都绑定geometryTransition属性。

   ```screen
   .geometryTransition('sharedId')
   ```
3. 在页面跳转时增加显示动画效果。

   ```screen
   .onClick(() => {
     this.getUIContext().animateTo({ duration: 1000 }, () => {
       this.navPathStack.pushPath({ name: 'nextB' }, false);
     });
   });
   ```
4. 在页面返回时拦截onBackPressed方法增加显示动画效果。

   ```screen
   .onBackPressed(() => {
     this.getUIContext().animateTo({ duration: 1000 }, () => {
       this.navPathStack.pop(false);
     });
     return true;
   });
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct RotateGeometryTransition {
  @Provide('navPS') navPathStack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.navPathStack.replacePath({ name: 'nextA' }, false);
  }

  @Builder
  navPathMapBuilder(name: string) {
    if (name === 'nextA') {
      NextA();
    } else if (name === 'nextB') {
      NextB();
    }
  }

  build() {
    Navigation(this.navPathStack)
      .navDestination(this.navPathMapBuilder)
      .hideNavBar(true);
  }
}

@Component
struct NextA {
  @Consume('navPS') navPathStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Row() {
          Text('hello world').fontSize(16);
        }
        .width('100%')
        .height(200)
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.Gray)
        .geometryTransition('sharedId')
        .onClick(() => {
          this.getUIContext().animateTo({ duration: 1000 }, () => {
            this.navPathStack.pushPath({ name: 'nextB' }, false);
          });
        });
      }
      .width('100%')
      .height('100%');
    }
    .title('Next A');
  }
}

@Component
struct NextB {
  @Consume('navPS') navPathStack: NavPathStack;

  build() {
    NavDestination() {
      Column() {
        Row() {
          Row() {
            Text('hello world !!!').fontSize(32);
          }.rotate({ angle: 90 })
          .width('100%')
          .height('100%');
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.Gray)
        .geometryTransition('sharedId')
        .onClick(() => {
          this.getUIContext().animateTo({ duration: 1000 }, () => {
            this.navPathStack.pop(false);
          });
        });
      }
      .width('100%')
      .height('100%');
    }
    .title('Next B')
    .onBackPressed(() => {
      this.getUIContext().animateTo({ duration: 1000 }, () => {
        this.navPathStack.pop(false);
      });
      return true;
    });
  }
}
```
