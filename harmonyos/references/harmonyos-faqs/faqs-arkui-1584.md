---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1584
title: 如何设置Tabs沉浸式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何设置Tabs沉浸式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0455c8f2b9cf98b275818a782cdc07326dec3b3017c3a7b8d2106a160ee1c9a8
---

## 问题现象

在使用Tabs组件构建页面时，如何实现沉浸式效果？

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。从API version 11开始，支持安全区域避让特性，其expandSafeArea属性的默认值为expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])。
* [background](../harmonyos-references/ts-universal-attributes-background.md#background10)：设置组件背景。从API version 20开始，新增了背景向父组件的安全区扩展的能力。
* [expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)：控制组件扩展其安全区域。
* [ignoreLayoutSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#ignorelayoutsafearea20)：扩展组件布局时的安全区。若宽度或高度设置了[LayoutPolicy.matchParent](../harmonyos-references/ts-universal-attributes-size.md#layoutpolicy15:~:text=说明-,matchParent,-LayoutPolicy)，其大小和位置都会改变。
* [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：设置应用主窗口或应用子窗口的布局是否为沉浸式布局。
* [getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)：获取当前窗口避让区域。

## 解决方案

对Tabs设置沉浸式方案如下：

| **实现场景** | **实现方案** | 实现方法 | 实现效果 | 适用场景 |
| --- | --- | --- | --- | --- |
| **组件级** | **方案一：设置背景沉浸。** | 设置Tabs组件的background()属性。 | 将组件背景扩展至避让区，页面布局仍在安全区内。 | 仅页面背景沉浸的场景。 |
| **组件级** | **方案二：安全区域拓展实现沉浸式。** | 设置Tabs组件的expandSafeArea属性。 | 将组件的安全区域延伸至状态栏或导航条区域，同时保持子组件在安全区内布局。对子组件设置expandSafeArea时，可实现对指定页签内容实现沉浸式。 | 对指定页签内容实现沉浸式。 |
| **组件级** | **方案三：设置页面沉浸。** | 设置ignoreLayoutSafeArea()并设置高度为LayoutPolicy.matchParent适应父组件。 | 页面背景与内容均扩展至顶部状态栏和底部导航条，根据需求进行避让处理。 | 需组件背景和内容完全覆盖屏幕的场景。 |
| **窗口级** | **方案四：设置窗口沉浸。** | 调用setWindowLayoutFullScreen()设置窗口为沉浸式布局。 | 页面背景与内容均扩展至顶部状态栏和底部导航条，根据需求进行避让处理。可实现对整个应用实现沉浸式。 | 需求整个应用实现沉浸式效果的场景。 |

* **方案一：设置背景沉浸。**

  对Tabs组件设置background属性，将组件背景扩展至避让区，页面布局仍在安全区内。代码如下：

  ```ts
  @Entry
  @Component
  struct BackgroundPage {
    build() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          Row({ space: 20 }) {
            Text('内容1')
              .fontSize(18)
              .fontColor('#000000');
            Text('文本1')
              .fontSize(18)
              .fontColor('#000000');
            Text('文字1')
              .fontSize(18)
              .fontColor('#000000');
          }
          .justifyContent(FlexAlign.SpaceAround)
          .alignItems(VerticalAlign.Top)
          .width('100%')
          .height('100%')
          .margin({ top: 12 });
        }
        .tabBar(BottomTabBarStyle.of('', '首页1').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }));

        TabContent() {
          Row() {
            Text('推荐1的内容')
              .fontSize(18)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .height('100%');
        }
        .tabBar(BottomTabBarStyle.of('', '推荐1').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }));
      }
      .background('#F1F3F5')
      .width('100%')
      .height('100%');
    }
  }
  ```

  参考图如下所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/UuOsAO9aSxSY3UYmZ22zvA/zh-cn_image_0000002658849563.png "点击放大")

* **方案二：安全区域拓展实现沉浸式。**

  Tabs的expandSafeArea属性具有默认值，默认对底部导航条实现沉浸式效果，本文设置expandSafeArea属性为expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])，将组件的安全区域延伸至状态栏和导航条区域，同时保持子组件在安全区内布局，对子组件TabContent设置expandSafeArea时，可实现对指定页签内容实现沉浸式。代码如下：

  ```ts
  @Entry
  @Component
  struct ExpandPage {
    build() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          Row({ space: 20 }) {
            Text('内容2')
              .fontSize(18)
              .fontColor('#000000');
            Text('文本2')
              .fontSize(18)
              .fontColor('#000000');
            Text('文字2')
              .fontSize(18)
              .fontColor('#000000');
          }
          .justifyContent(FlexAlign.SpaceAround)
          .alignItems(VerticalAlign.Top)
          .width('100%')
          .height('100%')
          .margin({ top: 12 });
        }
        .clip(false)
        .tabBar(BottomTabBarStyle.of('', '首页2').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }))
        .backgroundColor('#FFFFFF')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);

        TabContent() {
          Row() {
            Text('推荐2的内容')
              .fontSize(18)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .height('100%');
        }
        .tabBar(BottomTabBarStyle.of('', '推荐2').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }));
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5');
    }
  }
  ```

  参考图如下所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/zt5kIqiYRoOklZ-n6sfRDw/zh-cn_image_0000002628770198.png "点击放大")
* **方案三：设置页面沉浸。**

  对Tabs组件设置ignoreLayoutSafeArea属性并设置高度为LayoutPolicy.matchParent，页面背景与布局均扩展至顶部状态栏和底部导航条。代码如下：

  ```ts
  @Entry
  @Component
  struct IgnorePage {
    @StorageLink('statusBarHeight') statusBarHeight: number = AppStorage.get<number>('statusBarHeight') || 0;
    @StorageLink('navigationIndicatorHeight') navigationIndicatorHeight: number =
      AppStorage.get<number>('navigationIndicatorHeight') || 0;

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End }) {
          TabContent() {
            Row({ space: 20 }) {
              Text('内容3')
                .fontSize(18)
                .fontColor('#000000');
              Text('文本3')
                .fontSize(18)
                .fontColor('#000000');
              Text('文字3')
                .fontSize(18)
                .fontColor('#000000');
            }
            .justifyContent(FlexAlign.SpaceAround)
            .alignItems(VerticalAlign.Top)
            .width('100%')
            .height('100%')
            .margin({ top: 12 });
          }
          .width('100%')
          .tabBar(BottomTabBarStyle.of('', '首页3').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }));

          TabContent() {
            Row() {
              Text('推荐3的内容')
                .fontSize(18)
                .width('100%')
                .height('100%')
                .textAlign(TextAlign.Center);
            }
            .height('100%');
          }
          .tabBar(BottomTabBarStyle.of('', '推荐3').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }));
        }
        .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
        .height(LayoutPolicy.matchParent)
        .backgroundColor('#F1F3F5')
        .width('100%')
        .padding({
          top: `${this.statusBarHeight}px`,
          bottom: `${this.navigationIndicatorHeight}px`
        });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  若页面内容与避让区发生冲突时，需进行避让处理：

  1. 如上代码，若需页签栏的内容扩张至导航条区域，开发者可根据需求控制padding属性。
  2. 在EntryAbility文件中实现避让区高度的获取与保存，并监听安全区变化。代码如下：

     ```ts
     import { UIAbility } from '@kit.AbilityKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import { display, window } from '@kit.ArkUI';
     import { BusinessError } from '@kit.BasicServicesKit';

     const DOMAIN = 0x0000;

     export default class EntryAbility extends UIAbility {
       onWindowStageCreate(windowStage: window.WindowStage): void {
         windowStage.loadContent('pages/WindowPage', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
           // 获取避让区信息并保存
           let windowClass = windowStage.getMainWindowSync();
           let type = window.AvoidAreaType.TYPE_SYSTEM;
           let avoidArea = windowClass.getWindowAvoidArea(type);
           let typeNavigation = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR;
           let avoidAreaNavigation = windowClass.getWindowAvoidArea(typeNavigation);
           let statusBarHeight = avoidArea.topRect.height; // 获取状态栏区域高度
           let navigationIndicatorHeight = avoidAreaNavigation.bottomRect.height; // 获取导航条区域高度
           let displayClass = display.getDefaultDisplaySync(); // 获取屏幕实例
           displayClass.getCutoutInfo((err: BusinessError, data: display.CutoutInfo) => {
             if (err.code) {
               console.error(`Failed to get cutoutInfo. Code: ${err.code}, message: ${err.message}`);
               return;
             }
             console.info(`Succeeded in getting cutoutInfo. data: ${data}`);
           });
           AppStorage.setOrCreate('statusBarHeight', statusBarHeight); // 保存状态栏区域的高度
           AppStorage.setOrCreate('navigationIndicatorHeight', navigationIndicatorHeight); // 保存底部导航条区域的高度
           // 监听安全区变化
           windowClass.on('avoidAreaChange', (data) => {
             if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
               AppStorage.setOrCreate('statusBarHeight', data.area.topRect.height);
             } else if (data.type === window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
               AppStorage.setOrCreate('bottomRectHeight', data.area.bottomRect.height);
             }
           });
         });
       }
     };
     ```

     参考图如下所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/R1krGLJZT36lGoXu_qMXGA/zh-cn_image_0000002658969521.png "点击放大")
* **方案四：设置窗口沉浸。**

  调用aboutToAppear，在执行build()函数前，设置主窗为沉浸式布局，可实现对整个应用实现沉浸式效果。代码如下：

  ```ts
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@ohos.base';

  @Entry
  @Component
  struct WindowPage {
    @StorageLink('statusBarHeight') statusBarHeight: number = AppStorage.get<number>('statusBarHeight') || 0;
    @StorageLink('navigationIndicatorHeight') navigationIndicatorHeight: number =
      AppStorage.get<number>('navigationIndicatorHeight') || 0;

    aboutToAppear(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, windowClass: window.Window) => {
        if (err.code) {
          console.error(`Failed to obtain the window. Code: ${err.code}, message: ${err.message}`);
          return;
        }
        windowClass.setWindowLayoutFullScreen(true);
      });
    }

    build() {
      Tabs({ barPosition: BarPosition.End }) {
        TabContent() {
          Row({ space: 20 }) {
            Text('内容4')
              .fontSize(18)
              .fontColor('#000000');
            Text('文本4')
              .fontSize(18)
              .fontColor('#000000');
            Text('文字4')
              .fontSize(18)
              .fontColor('#000000');
          }
          .justifyContent(FlexAlign.SpaceAround)
          .alignItems(VerticalAlign.Top)
          .width('100%')
          .height('100%')
          .margin({ top: 12 });
        }
        .width('100%')
        .height('100%')
        .tabBar(BottomTabBarStyle.of('', '首页4').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }));

        TabContent() {
          Row() {
            Text('推荐4的内容')
              .fontSize(18)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .height('100%');
        }
        .tabBar(BottomTabBarStyle.of('', '推荐4').labelStyle({ font: { size: 20 }, selectedColor: '#0A59F7' }));
      }
      .backgroundColor('#F1F3F5')
      .height('100%')
      .width('100%')
      .padding({
        top: `${this.statusBarHeight}px`,
        bottom: `${this.navigationIndicatorHeight}px`
      });
    }
  }
  ```

  避让操作与方案三类似，不再赘述。

  参考图如下所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/Eo6c8OhjS9KtsSzEDimp1A/zh-cn_image_0000002628610302.png "点击放大")

## 常见FAQ

Q：设置沉浸式时，如何将TabBar隐藏？

A：可通过动态设置属性barHeight和barWidth的值为0实现。

Q：设置沉浸式时，如何控制页签内容到状态栏或底部导航条的距离？

A：可通过设置Tabs的padding属性实现。

Q：ignoreLayoutSafeArea和expandSafeArea均设置时，优先级怎么判断？

A：ignoreLayoutSafeArea属性先生效，expandSafeArea在前者基础上再生效。
