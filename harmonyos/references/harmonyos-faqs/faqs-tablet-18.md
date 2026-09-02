---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-18
title: 自由多窗模式关闭后状态栏与页面内容重叠
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 自由多窗模式关闭后状态栏与页面内容重叠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9ca78e271b44e61e90604afed8b232a015d025b9d1b5d0c378b0493ce49692b5
---

## 问题现象

平板从自由多窗模式退出后，应用页面内容与状态栏有重叠。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/MhOBzrTGR6a6nMT4--kn-w/zh-cn_image_0000002628552230.png "点击放大")

## 背景知识

1. [setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：设置主窗口或子窗口的布局是否为沉浸式布局，应用开发时为了使页面状态栏和导航栏的底色与页面内容底色一致，保证体验，一般会开启沉浸式布局。
2. [padding](../harmonyos-references/ts-universal-attributes-size.md#padding)：表示组件的内边距，在沉浸式布局中，一般通过对根组件设置内边距padding来避让状态栏和导航栏。
3. [getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)：获取当前应用窗口避让区。避让区指系统栏区域、刘海屏区域、手势区域、软键盘区域等与窗口内容重叠时，需要窗口内容避让的区域。可以通过此接口，获取系统状态栏和导航栏的高度，在开启沉浸式时，将状态栏和导航栏的高度赋值给页面根组件的padding。

## 问题定位

1. 排查EntryAbility文件中是否调用窗口强制全屏布局接口setWindowLayoutFullScreen()，例如下面的代码。

   ```js
   let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
   // 设置窗口全屏
   let isLayoutFullScreen = true;
   windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
     console.info('Succeeded in setting the window layout to full-screen mode.');
   }).catch((err: BusinessError) => {
     console.error(JSON.stringify(err));
   });
   ```
2. 排查应用根组件中是否设置padding属性用于动态设置状态栏和底部导航栏避让区域，例如下面的代码。

   ```js
   build() {
     Column(){
     }
     .padding({
           top: this.getUIContext().px2vp(this.topRectHeight),
           bottom: this.getUIContext().px2vp(this.bottomRectHeight)
         })
   }
   ```

## 分析结论

1. 如果已开启了沉浸式布局，未给根组件设置padding属性，那是由于根组件padding属性缺失导致的页面内容与状态栏重叠。
2. 如果开启了沉浸式布局，根组件也设置了padding属性，且padding属性是状态变量，怀疑是一多适配时将padding的top值改小了未恢复，导致自由多窗模式退出后，页面内容与状态栏重叠。

## 修改建议

全局窗口布局：

在EntryAbility中的按步骤进行如下设置：

* 步骤一：onWindowStageCreate调用setWindowLayoutFullScreen()接口设置窗口全屏。
* 步骤二：使用getWindowAvoidArea()接口获取当前布局遮挡区域（此处以状态栏、导航区域为例）。
* 步骤三：注册监听函数，动态获取避让区域的实时数据。

EntryAbility中相关代码如下：

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      return;
    }

    let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
    // 1.设置窗口全屏
    let isLayoutFullScreen = true;
    windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
      console.info('Succeeded in setting the window layout to full-screen mode.');
    }).catch((err: BusinessError) => {
      console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
    });

    // 2.获取布局避让遮挡的区域（可以开始就设置，也可以通过代码手动开启）
    let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // 此处以导航条避让为例
    let avoidArea = windowClass.getWindowAvoidArea(type);
    let bottomRectHeight = avoidArea.bottomRect.height; // 获取到导航区域的高度
    AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);

    type = window.AvoidAreaType.TYPE_SYSTEM; // 以状态栏避让为例
    avoidArea = windowClass.getWindowAvoidArea(type);
    let topRectHeight = avoidArea.topRect.height; // 获取状态栏区域高度
    AppStorage.setOrCreate('topRectHeight', topRectHeight);

    // 3.注册监听函数，动态获取避让区域数据（可以开始就设置，也可以通过代码手动开启）
    windowClass.on('avoidAreaChange', (data) => {
      if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
        let topRectHeight = data.area.topRect.height;
        AppStorage.setOrCreate('topRectHeight', topRectHeight);
      } else if (data.type == window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
        let bottomRectHeight = data.area.bottomRect.height;
        AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
      }
    });
  });
}
```

Index代码如下：

```ts
@Entry
@Component
struct TabsExample {
  private controller: TabsController = new TabsController();
  @StorageProp('bottomRectHeight')
  bottomRectHeight: number | undefined = AppStorage.get('bottomRectHeight');
  @StorageProp('topRectHeight')
  topRectHeight: number | undefined = AppStorage.get('topRectHeight');

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
        TabContent() {
          Column() {
            // 设置全屏渲染
            Flex({ justifyContent: FlexAlign.SpaceBetween }) {
              Row() {
                Text('设置全屏渲染效果');
              };
            };

            // 设置顶部padding
            Flex({ justifyContent: FlexAlign.SpaceBetween }) {
              Row() {
                Text('顶部添加padding效果');
              };
            };

            // 设置底部padding
            Flex({ justifyContent: FlexAlign.SpaceBetween }) {
              Row() {
                Text('底部添加padding效果');
              };
            };
          }
          .width('100%')
          .height('100%')
          .backgroundColor('#00CB87')
          .alignItems(HorizontalAlign.Center)
          .padding({ left: 20, right: 20 })
          .justifyContent(FlexAlign.Center);
        }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'green'));

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF');
        }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'blue'));

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00');
        }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'yellow'));

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#E67C92');
        }.tabBar(BottomTabBarStyle.of($r('app.media.startIcon'), 'pink'));
      }
      .width('100%')
      .height('100%')
      .barBackgroundColor('#F1F3F5')
      // top数值与状态栏区域高度保持一致；bottom数值与导航区域高度保持一致
      .padding({
        top: this.getUIContext().px2vp(this.topRectHeight),
        bottom: this.getUIContext().px2vp(this.bottomRectHeight)
      });
    }
    .width('100%');
  }
}
```
