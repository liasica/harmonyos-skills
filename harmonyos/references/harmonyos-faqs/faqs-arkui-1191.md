---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1191
title: 应用未显示系统导航栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 应用未显示系统导航栏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9bcc9e009ecb88057b465b87aa9924420df9096db1206c4854197f91fdcad141
---

## 问题现象

页面沉浸式全屏显示，不显示底部系统导航栏。

期望效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/KHr49reYSjquwGrvhCA1MQ/zh-cn_image_0000002628752866.png "点击放大")

实际效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/xMVMLGsBSeeoyxo7zFn4Sg/zh-cn_image_0000002658952185.png "点击放大")

## 背景知识

* [setSpecificSystemBarEnabled](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)：在全屏主窗口下设置主窗口三键导航栏、状态栏、底部导航条的显示和隐藏。
* [setWindowSystemBarEnable](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)可设置主窗口状态栏、底部导航（根据用户设置，可表现为导航条或三键导航栏）的可见模式，状态栏和底部导航通过status控制、navigation参数无效果，使用Promise异步回调。

## 问题定位

全局搜索关键字setSpecificSystemBarEnabled和setWindowSystemBarEnable，查看页面是否通过接口设置状态栏导航栏的具体显示/隐藏状态。

* 场景一：使用setSpecificSystemBarEnabled设置导航栏隐藏。

  ```ts
  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setSpecificSystemBarEnabled('navigationIndicator', false); // 设置导航栏隐藏
      });
  }
  ```
* 场景二：使用setWindowSystemBarEnable设置导航栏隐藏。

  ```ts
  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowSystemBarEnable([]); // 设置导航栏隐藏
      });
  }
  ```

## 分析结论

场景一：应用在不应该隐藏导航栏的界面，错误的使用setSpecificSystemBarEnabled方法对系统导航栏进行隐藏。

场景二：应用在不应该隐藏导航栏的界面，错误的使用setWindowSystemBarEnable方法对系统导航栏进行隐藏。

## 修改建议

* 场景一：使用setSpecificSystemBarEnabled方法设置导航条显示。

  ```screen
  import { window } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct SituationOne {
    aboutToAppear(): void {
      let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setSpecificSystemBarEnabled('navigationIndicator', true); // 设置导航栏显示
      })
        .catch((err: BusinessError) => {
          console.error('Failed to get last window:', err);
        });
    }

    build() {
      Column() {
        Text('Hello World')
          .width('100%')
          .height('100%')
          .fontSize(30)
          .textAlign(TextAlign.Center);
      }
      .width('100%')
      .height('100%')
      .padding({ top: 20 })
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/xV53pdbXRmmwq1L2wWfhbg/zh-cn_image_0000002628592972.png "点击放大")
* 场景二：使用setSpecificSystemBarEnabled方法设置导航条显示。

  ```ts
  import { window } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct SituationTwo {
    aboutToAppear(): void {
      let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowSystemBarEnable(['status', 'navigation']); // 设置导航栏显示
      })
        .catch((err: BusinessError) => {
          console.error('Failed to get last window:', err);
        });
    }

    build() {
      Column() {
        Text('Hello World')
          .width('100%')
          .height('100%')
          .fontSize(30)
          .textAlign(TextAlign.Center);
      }
      .width('100%')
      .height('100%')
      .padding({ top: 20 })
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Uqwe0unrR5ebCIeuKf5T0A/zh-cn_image_0000002658832227.png "点击放大")
