---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-11
title: 阔折叠布局适配处理方式
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > 阔折叠布局适配处理方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a7aa2962b613bb5275a870c1c70eb2001b1c7b007fbf9ec98d8fe2055abd87d6
---

## 问题现象

Pura X折叠设备布局存在显示问题，需要进行适配，是否有直接判断可折叠的API，便于做适配？

## 背景知识

* [@ohos.deviceInfo(设备信息)](../harmonyos-references/js-apis-device-info.md)：提供终端设备信息查询，如productSeries（产品系列），开发者不可配置。
* [@ohos.display(屏幕属性)](../harmonyos-references/js-apis-display.md)：提供管理显示设备的一些基础能力，包括获取默认显示设备的信息，获取所有显示设备的信息以及监听显示设备的插拔行为。
* [@ohos.window (窗口)](../harmonyos-references/arkts-apis-window.md)：提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。

## 解决方案

* 通过屏幕尺寸的方式进行布局适配。

  打开应用时使用[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)方法获取屏幕尺寸，然后通过窗口的[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法实现对窗口尺寸大小变化的监听。示例代码如下：
* EntryAbility.ets：监听窗口尺寸大小变化，并保存到AppStorage。

  ```ts
  import {  UIAbility} from '@kit.AbilityKit';

  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  export default class EntryAbility extends UIAbility {
    onCreate(): void {
    }

    onDestroy(): void {
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {

      let windowClass: window.Window | undefined = undefined;
      try {
        window.getLastWindow(this.context, (err: BusinessError, data) => {
          const errCode: number = err.code;
          if (errCode) {
            return;
          }
          windowClass = data;
          try {
            // 对窗口尺寸大小变化的监听
            windowClass.on('windowSizeChange', (data) => {
              AppStorage.setOrCreate('width', data.width);
              AppStorage.setOrCreate('height', data.height);
            });
          } catch (exception) {
          }
        });
      } catch (exception) {
      }

      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          return;
        }
      });
    }

    onWindowStageDestroy(): void {
    }

    onForeground(): void {
    }

    onBackground(): void {
    }
  }
  ```
* Index.ets：获取当前屏幕的大小，展示数据。

  ```ts
  import display from '@ohos.display';
  import { deviceInfo } from '@kit.BasicServicesKit';
  let productSeriesInfo: string = deviceInfo.productSeries;
  console.info('the value of the deviceInfo productSeries is :' + productSeriesInfo);
  @Entry
  @Component
  struct Index {
    @StorageLink('width') width1: number = 0;
    @StorageLink('height') height1: number = 0;

    aboutToAppear(): void {
      let displayClass: display.Display | null = null;
      displayClass = display.getDefaultDisplaySync();
      this.width1 = displayClass.width;
      this.height1 = displayClass.height;
    }

    build() {
      Column() {
        Text(this.width1.toString())
          .fontSize(50)
          .fontWeight(FontWeight.Bold)

        Text(this.height1.toString())
          .fontSize(50)
          .fontWeight(FontWeight.Bold)

      }
      .height('100%')
      .width('100%')
    }
  }
  ```

目前系统未提供直接判断折叠态的单一API，需通过屏幕尺寸变化监听或断点机制间接判断折叠/展开状态。另外，推荐使用断点作为折叠展开态布局判断条件。系统侧设计了横向和纵向断点分别代表窗口宽度和窗口高宽比，页面布局的一多要求使用横向和纵向断点进行判断实现，更多详情请参考[一多断点开发实践](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)与[折叠屏开发实践](../best-practices/bpta-foldable-guide.md#section7379849135810)。针对Pura X如何判断折叠展开态，可参考[Pura X开发实践](../best-practices/bpta-purax-guide.md)之【内屏适配】。

## 常见FAQ

Q：三折叠设备类型标识为手机，是否会因展开态而变成pad？

A：折叠屏设备不会因形态变化（折叠态/展开态）切换设备类型标识。

## 总结

内屏（锁屏或非锁屏状态）切换到外屏，默认显示为锁屏的亮屏状态。用户解锁后，如果应用已适配外屏，应用界面将接续到外屏。详情参考[开合接续规则](../best-practices/bpta-purax-guide.md#section1159145510419)。
