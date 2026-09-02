---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1406
title: NavPathStack跳转不存在页面时重定向
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > NavPathStack跳转不存在页面时重定向
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81d846ac543fac3dd06507b45e6dc3a1fe6b9c47572b898643499226cd07f3f3
---

## 问题现象

NavPathStack跳转不存在的页面如何能拦截，然后重定向到一个“敬请期待”自定义页面？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/JCHN5HUZTBqQrqmXesL5Lw/zh-cn_image_0000002628603240.png "点击放大")

## 背景知识

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用。[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)是Navigation路由栈，可以通过多种方法跳转至指定的NavDestination页面。

* [pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath12)、[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname11)为同步跳转页面的方法，跳转不存在页面时不会抛出异常，显示空白页面。
* [pushDestination](../harmonyos-references/ts-basic-components-navigation.md#pushdestination12)、[pushDestinationByName](../harmonyos-references/ts-basic-components-navigation.md#pushdestinationbyname11)为异步跳转页面的方法，跳转不存在页面时会抛出异常。

## 解决方案

使用pushDestination、pushDestinationByName方法进行页面跳转，捕捉跳转的回调结果，若跳转错误则重定向至指定页面。

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct NavPathStackDemo {
  navPathStack: NavPathStack = new NavPathStack();

  @Builder
  pageMap(name: string) {
    if (name === 'ErrorPage') {
      ErrorPage();
    }
  }

  build() {
    Navigation(this.navPathStack) {
      Button('跳转不存在页面')
        .fontSize('20fp')
        .margin({ top: '50vp' })
        .onClick(() => {
          // 跳转xxx页面，此页面不存在
          this.navPathStack.pushDestination({ name: 'xxx' }).catch((result: BusinessError) => {
            console.info(`${result.code} ${result.name} ${result.message}`);
            this.navPathStack.pushPathByName('ErrorPage', null, false); // 跳转失败重定向
          });
        });
    }
    .navDestination(this.pageMap)
    .height('100%')
    .width('100%');
  }
}

@Component
struct ErrorPage {
  build() {
    NavDestination() {
      Text('敬请期待')
        .fontSize('50fp')
        .margin({ top: '50vp' });
    }.height('100%').width('100%');
  }
}
```
