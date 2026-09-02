---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-119
title: 应用启动时页面周边有白边
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用启动时页面周边有白边
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:94d36a20f26cb62144120ee931964e70767816f7e335d63dae98bbbaa9c91f85
---

## 问题现象

应用启动时动效异常，启动图片未铺满屏幕，周边有空白。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/9wV7LFJFRGyAAmU7ycQNvA/zh-cn_image_0000002628789130.png "点击放大")

## 背景知识

* [abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)：描述UIAbility组件的配置信息，标签值为数组类型，该标签下的配置只对当前UIAbility生效。
* startWindowIcon标识当前UIAbility组件启动页面图标资源文件。目前startWindowIcon的大小是放多大画多大，没有能力根据设备屏幕或窗口大小自适应调整。

## 问题定位

1. 根据entry\src\main\module.json5配置文件中startWindowIcon设置的图片资源，查看该图片资源的大小。

   ```screen
   {
     "abilities": [{
       "name": "EntryAbility",
       "srcEntry": "./ets/entryability/EntryAbility.ets",
       "launchType":"singleton",
       "description": "$string:description_main_ability",
       "icon": "$media:layered_image",
       "label": "Login",
       "startWindow": "$profile:start_window",
       "startWindowIcon": "$media:startWindow",
       "startWindowBackground": "$color:red",
       "process": ":processTag"
     }]
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/TfESL9vCSYyjIhM1Dif8IA/zh-cn_image_0000002658988441.png "点击放大")
2. 在系统设置中查看屏幕的尺寸，启动页图片的大小与屏幕尺寸不一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/kk-aTxyzScuXGBKb86yTUw/zh-cn_image_0000002628629220.png "点击放大")

## 分析结论

启动页图片的大小与设备分辨率不一致，导致应用启动动画周边有空白。

## 修改建议

* 更换启动页图片为与屏幕宽高一致的图片。
* 开发一个自定义的启动页的方式来实现自定义启动图，而不是只在module.json5配置文件中通过startWindowIcon字段设置启动图。

  ```screen
  @Entry
  @Component
  struct Index {
    pageInfos: NavPathStack = new NavPathStack();

    aboutToAppear(): void {
      this.pageInfos.pushPath({ name: 'Splash' }); // 跳转到启动页
    }

    build() {
      Navigation(this.pageInfos) {
        Stack() {
          Text('Hello World')
            .fontSize(20)
            .fontWeight(FontWeight.Bold);
        }
        .height('100%')
        .width('100%');
      }
      .hideTitleBar(true)
      .height('100%')
      .width('100%')
      .mode(NavigationMode.Stack);
    }
  }
  ```

  src/main/ets/pages/Splash.ets：

  ```screen
  import { window } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';

  @Builder
  export function SplashBuilder() {
    Splash();
  }

  @Entry
  @Component
  export struct Splash {
    pageInfos: NavPathStack = new NavPathStack();

    setFull(isFull: boolean) {
      let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((windowClass) => {
        windowClass.setWindowLayoutFullScreen(isFull); // 启动页全屏显示
        let systemBarPropertiesFull: window.SystemBarProperties = {
          statusBarColor: '#00000000',
          statusBarContentColor: '#ffffff'
        };
        let systemBarPropertiesOut: window.SystemBarProperties = {
          statusBarColor: '#ffffff',
          statusBarContentColor: '#000000'
        };
        windowClass.setWindowSystemBarProperties(isFull ? systemBarPropertiesFull : systemBarPropertiesOut);
      });
    }

    build() {
      NavDestination() {
        Stack() {
          Image($r('app.media.startWindow')) // $r('app.media.startIcon')需要替换为开发者需要的图片资源文件
            .width('100%')
            .height('100%')
            .syncLoad(true); // 设置图片为同步加载

          Column()
            .width('100%')
            .height('123px')
            .linearGradient({
              angle: 0,
              colors: [[0x11000000, 0.0], [0x00000000, 1.0]]
            })
            .position({ y: 0 });
        }
        .height('100%')
        .width('100%');
      }
      .onBackPressed(() => {
        this.pageInfos.pop(); // 弹出路由栈栈顶元素
        return true;
      })
      .onDisAppear(() => {
        this.setFull(false);
      })
      .onReady((navContext: NavDestinationContext) => {
        this.pageInfos = navContext.pathStack;
        this.setFull(true);
        setTimeout(() => {
          this.pageInfos.pop();
        }, 2000);
      })
      .hideTitleBar(true)
      .systemTransition(NavigationSystemTransitionType.NONE)
      .height('100%')
      .width('100%')
      .backgroundColor(Color.White);
    }
  }
  ```

  src/main/resources/base/profile/router\_map.json：

  ```screen
  {
    "routerMap": [
      {
        "name": "Splash",
        "pageSourceFile": "src/main/ets/pages/Splash.ets",
        "buildFunction": "SplashBuilder"
      }
    ]
  }
  ```

  src/main/module.json5文件中需添加"routerMap": "$profile:router\_map"。

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/Dv2VsCWTTwiu3VpfeeCOew/zh-cn_image_0000002658868495.png "点击放大")
