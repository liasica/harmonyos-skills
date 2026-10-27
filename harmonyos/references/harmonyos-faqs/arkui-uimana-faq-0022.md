---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0022
title: Tabs组件常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > Tabs组件常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:86e21cab7856ca5f0a89bd0c3693dd95c738ea6263452e033ff22b34e49911f4
---

**Q：在使用Tabs组件构建页面时，如何实现沉浸式效果？**

**A**：对Tabs设置沉浸式方案如下：

| 实现场景 | 实现方案 | 实现方法 | 实现效果 | 适用场景 |
| --- | --- | --- | --- | --- |
| 组件级 | 方案一：设置背景沉浸。 | 设置Tabs组件的background()属性。 | 将组件背景扩展至避让区，页面布局仍在安全区内。 | 仅页面背景沉浸的场景。 |
| 组件级 | 方案二：安全区域拓展实现沉浸式。 | 设置Tabs组件的expandSafeArea属性。 | 将组件的安全区域延伸至状态栏或导航条区域，同时保持子组件在安全区内布局。对子组件设置expandSafeArea时，可实现对指定页签内容实现沉浸式。 | 对指定页签内容实现沉浸式。 |
| 组件级 | 方案三：设置页面沉浸。 | 设置ignoreLayoutSafeArea()并设置高度为LayoutPolicy.matchParent适应父组件。 | 页面背景与内容均扩展至顶部状态栏和底部导航条，根据需求进行避让处理。 | 需组件背景和内容完全覆盖屏幕的场景。 |
| 窗口级 | 方案四：设置窗口沉浸。 | 调用setWindowLayoutFullScreen()设置窗口为沉浸式布局。 | 页面背景与内容均扩展至顶部状态栏和底部导航条，根据需求进行避让处理。可实现对整个应用实现沉浸式。 | 需求整个应用实现沉浸式效果的场景。 |

* 方案一：设置背景沉浸。

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/VpCWIZTMQwu2devCdoXXiw/zh-cn_image_0000002801204549.png "点击放大")
* 方案二：安全区域拓展实现沉浸式。

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/za2OO5YSTYOyWone7FLiHQ/zh-cn_image_0000002771924890.png "点击放大")
* 方案三：设置页面沉浸。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/JMaqcHl0S2CSGtjsAg8WHA/zh-cn_image_0000002771925790.png "点击放大")
* 方案四：设置窗口沉浸。

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/V6L-tZ3QSweM7MSCmTexFw/zh-cn_image_0000002801085839.png "点击放大")

**Q：设置沉浸式时，如何将TabBar隐藏？**

**A**：可通过动态设置属性barHeight和barWidth的值为0实现。

**Q：设置沉浸式时，如何控制页签内容到状态栏或底部导航条的距离？**

**A**：可通过设置Tabs的padding属性实现。

**Q：ignoreLayoutSafeArea和expandSafeArea均设置时，优先级怎么判断？**

**A**：ignoreLayoutSafeArea属性先生效，expandSafeArea在前者基础上再生效。

**Q：应用采用Tabs导航来快速实现视图内容的切换，其中视图内容之间的组件样式相互复用。由于组件复用，导致其中一个视图内容下拉刷新的时候，其他页面的数据也跟随变化，如何实现只刷新当前视图内容数据，其他视图内容保持不变？**

**A**：为了实现不同视图内容中复用组件间数据的隔离，需要为每个视图内容创建单独的刷新函数。当监听到Tabs页切换时，立即将每个视图内容独有的刷新函数与共享的刷新监听器重新绑定，以确保后续在当前页面执行刷新操作时，仅修改当前页面的数据。完整的示例代码如下：

1. 定义页面中使用的常量（实际使用时需要从后端服务器获取）：

   ```ts
   // 定义页面中使用的常量
   export class SleepStyleModel {
     name: string;
     key: string;

     constructor(name: string, key: string) {
       this.name = name;
       this.key = key;
     }
   }

   export const styleData: SleepStyleModel[] = [
     new SleepStyleModel('全部', 'ALL'),
     new SleepStyleModel('睡眠', 'FastSleep')
   ];
   ```
2. 定义监听器：

   ```ts
   // 定义监听器
   export class RefreshListener {
     // key: string;
     onRefresh = (key: string) => {
       // return key
       console.info(key);
     };
   }
   ```
3. 定义Tab页中复用组件：

   ```ts
   @Component({ freezeWhenInactive: true })
   export struct StyleList {
     @Prop typeKey: string;
     @Prop isRefreshing: boolean = false;
     @State list: string[] = [];
     // 监听Tabs切换
     @Prop @Watch('onIndexChange') currentIndex: number;
     listener: RefreshListener = new RefreshListener();
     private onRefresh = (key: string) => {
       console.info(`key==============: ${key}`);
       this.typeKey = key;
       this.loadData();
     };

     // 监听回调函数
     onIndexChange() {
       console.info('---------------------监听切换视图页面');
       if (styleData[this.currentIndex].key == this.typeKey) {
         // 重新绑定刷新函数
         console.info(`---------------------重新绑定监听函数${this.currentIndex}`);
         this.listener.onRefresh = this.onRefresh;
       }
     }

     aboutToAppear(): void {
       this.listener.onRefresh = this.onRefresh;
       this.loadData();
     }

     loadData() {
       const arr: string[] = [];
       switch (this.typeKey) {
         case 'ALL':
           for (let i = 0; i < 5; i++) {
             arr.push(this.typeKey + i.toString());
           }
           this.list = arr;
           break;
         case 'FastSleep':
           for (let i = 5; i < 10; i++) {
             arr.push(this.typeKey + i.toString());
           }
           this.list = arr;
           break;
       }
     }

     build() {
       Column() {
         List() {
           ForEach(this.list, (item: string) => {
             ListItem() {
               Text('' + item)
                 .width('70%')
                 .height(80)
                 .margin(10)
                 .textAlign(TextAlign.Center)
                 .borderRadius(10)
                 .backgroundColor(0xFFFFFF);
             };
           }, (item: string) => item + new Date().getTime());
         }
         .width('100%')
         .height('100%')
         .alignListItem(ListItemAlign.Center)
         .scrollBar(BarState.Off);
       };
     }
   }
   ```
4. 定义首页，调用复用组件：

   ```ts
   @Entry
   @Component
   export struct SleepMusicPage {
     @State styleList: SleepStyleModel[] = styleData;
     @State currentIndex: number = 0;
     @State selectedIndex: number = 0;
     @State isRefreshing: boolean = false;
     private controller: TabsController = new TabsController();
     private listener: RefreshListener = new RefreshListener();
     private currentKey: string = 'ALL';

     @Builder
     tabBuilder(index: number, name: string) {
       Column() {
         Text(name)
           .fontColor(this.selectedIndex === index ? '#1E2029' : '#91979F')
           .fontSize(12)
           .fontWeight(this.selectedIndex === index ? 500 : 400)
           .lineHeight(22)
           .margin({
             top: 17,
             bottom: 7
           });
         Divider()
           .strokeWidth(2)
           .color('#1E2029')
           .opacity(this.selectedIndex === index ? 1 : 0);
       }.width('100%');
     }

     build() {
       Refresh({
         refreshing: $$this.isRefreshing
       }) {
         Column() {
           Tabs({
             barPosition: BarPosition.Start,
             index: this.currentIndex,
             controller: this.controller
           }) {
             ForEach(this.styleList, (item: SleepStyleModel, index: number) => {
               TabContent() {
                 // 外部调用复用组件
                 StyleList({
                   typeKey: item.key,
                   isRefreshing: this.isRefreshing,
                   // 共享的刷新监听器
                   listener: this.listener,
                   currentIndex: this.currentIndex
                 });
               }.tabBar(this.tabBuilder(index, item.name));
             }, (item: SleepStyleModel) => JSON.stringify(item.key) + new Date().getTime());
           }
           .animationDuration(400)
           .onChange((index: number) => {
             this.currentIndex = index;
             this.selectedIndex = index;
             this.currentKey = this.styleList[this.selectedIndex].key;
           });
         }.width('100%').height('100%');
       }
       .onRefreshing(() => {
         this.isRefreshing = true;
         this.listener.onRefresh(this.currentKey);
         setTimeout(() => {
           this.isRefreshing = false;
         }, 1000);
       })
       .backgroundColor(0x89CFF0)
       .refreshOffset(64)
       .pullToRefresh(true);
     }
   }
   ```

   完整代码为：

   ```ts
   // 定义页面中使用的常量
   export class SleepStyleModel {
     name: string;
     key: string;

     constructor(name: string, key: string) {
       this.name = name;
       this.key = key;
     }
   }

   export const styleData: SleepStyleModel[] = [
     new SleepStyleModel('全部', 'ALL'),
     new SleepStyleModel('睡眠', 'FastSleep')
   ];

   // 定义监听器
   export class RefreshListener {
     // key: string;
     onRefresh = (key: string) => {
       // return key
       console.info(key);
     };
   }

   @Component({ freezeWhenInactive: true })
   export struct StyleList {
     @Prop typeKey: string;
     @Prop isRefreshing: boolean = false;
     @State list: string[] = [];
     // 监听Tabs切换
     @Prop @Watch('onIndexChange') currentIndex: number;
     listener: RefreshListener = new RefreshListener();
     private onRefresh = (key: string) => {
       console.info(`key==============: ${key}`);
       this.typeKey = key;
       this.loadData();
     };

     // 监听回调函数
     onIndexChange() {
       console.info('---------------------监听切换视图页面');
       if (styleData[this.currentIndex].key == this.typeKey) {
         // 重新绑定刷新函数
         console.info(`---------------------重新绑定监听函数${this.currentIndex}`);
         this.listener.onRefresh = this.onRefresh;
       }
     }

     aboutToAppear(): void {
       this.listener.onRefresh = this.onRefresh;
       this.loadData();
     }

     loadData() {
       const arr: string[] = [];
       switch (this.typeKey) {
         case 'ALL':
           for (let i = 0; i < 5; i++) {
             arr.push(this.typeKey + i.toString());
           }
           this.list = arr;
           break;
         case 'FastSleep':
           for (let i = 5; i < 10; i++) {
             arr.push(this.typeKey + i.toString());
           }
           this.list = arr;
           break;
       }
     }

     build() {
       Column() {
         List() {
           ForEach(this.list, (item: string) => {
             ListItem() {
               Text('' + item)
                 .width('70%')
                 .height(80)
                 .margin(10)
                 .textAlign(TextAlign.Center)
                 .borderRadius(10)
                 .backgroundColor(0xFFFFFF);
             };
           }, (item: string) => item + new Date().getTime());
         }
         .width('100%')
         .height('100%')
         .alignListItem(ListItemAlign.Center)
         .scrollBar(BarState.Off);
       };
     }
   }

   @Entry
   @Component
   export struct SleepMusicPage {
     @State styleList: SleepStyleModel[] = styleData;
     @State currentIndex: number = 0;
     @State selectedIndex: number = 0;
     @State isRefreshing: boolean = false;
     private controller: TabsController = new TabsController();
     private listener: RefreshListener = new RefreshListener();
     private currentKey: string = 'ALL';

     @Builder
     tabBuilder(index: number, name: string) {
       Column() {
         Text(name)
           .fontColor(this.selectedIndex === index ? '#1E2029' : '#91979F')
           .fontSize(12)
           .fontWeight(this.selectedIndex === index ? 500 : 400)
           .lineHeight(22)
           .margin({
             top: 17,
             bottom: 7
           });
         Divider()
           .strokeWidth(2)
           .color('#1E2029')
           .opacity(this.selectedIndex === index ? 1 : 0);
       }.width('100%');
     }

     build() {
       Refresh({
         refreshing: $$this.isRefreshing
       }) {
         Column() {
           Tabs({
             barPosition: BarPosition.Start,
             index: this.currentIndex,
             controller: this.controller
           }) {
             ForEach(this.styleList, (item: SleepStyleModel, index: number) => {
               TabContent() {
                 // 外部调用复用组件
                 StyleList({
                   typeKey: item.key,
                   isRefreshing: this.isRefreshing,
                   // 共享的刷新监听器
                   listener: this.listener,
                   currentIndex: this.currentIndex
                 });
               }.tabBar(this.tabBuilder(index, item.name));
             }, (item: SleepStyleModel) => JSON.stringify(item.key) + new Date().getTime());
           }
           .animationDuration(400)
           .onChange((index: number) => {
             this.currentIndex = index;
             this.selectedIndex = index;
             this.currentKey = this.styleList[this.selectedIndex].key;
           });
         }.width('100%').height('100%');
       }
       .onRefreshing(() => {
         this.isRefreshing = true;
         this.listener.onRefresh(this.currentKey);
         setTimeout(() => {
           this.isRefreshing = false;
         }, 1000);
       })
       .backgroundColor(0x89CFF0)
       .refreshOffset(64)
       .pullToRefresh(true);
     }
   }
   ```

**Q：Tabs组件如何在TabBar添加页签之外的自定义组件，如文字和图片等？**

**A**：使用浮层overlay可以实现，步骤如下：

1. 通过Builder设置浮层。值得注意的是：为了避免阻塞对TabBar的操作，需在浮层Builder的最外层组件上配置.hitTestBehavior(HitTestMode.Transparent)。

   ```ts
   @Builder
     overlayExample() {
       Flex({ justifyContent: FlexAlign.SpaceBetween, direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
         Text('登录').fontSize(18).fontColor('#ffcd6c18');
         Image($r('app.media.search'))
           .width(24)
           .height(24);
       }
       .padding({ left: 20, right: 20 })
       .width('100%')
       .height(56)
       .hitTestBehavior(HitTestMode.Transparent); // 配置浮层不阻塞交互
     }
   ```
2. 将浮层添加到Tabs上，注意设置barWidth限制页签大小，腾出浮层容纳的空间，barHeight与浮层的最外层组件高度保持一致。

   ```ts
   Tabs() {
           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Pink);
           }.tabBar(SubTabBarStyle.of('订阅'));

           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Green);
           }.tabBar(SubTabBarStyle.of('推荐'));

           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Blue);
           }.tabBar(SubTabBarStyle.of('热门'));
         }
         .width('100%')
         .height('100%')
         .backgroundColor(0xf1f3f5)
         .barMode(this.barMode)
         .barWidth(200)
         .overlay(this.overlayExample(), { align: Alignment.Top });
   ```

   完整示例参考如下：

   ```ts
   @Entry
   @Component
   struct TabsExample {
     text: string = '文本';
     barMode: BarMode = BarMode.Fixed;

     @Builder
     overlayExample() {
       Flex({ justifyContent: FlexAlign.SpaceBetween, direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
         Text('登录').fontSize(18).fontColor('#ffcd6c18');
         Image($r('app.media.search'))
           .width(24)
           .height(24);
       }
       .padding({ left: 20, right: 20 })
       .width('100%')
       .height(56)
       .hitTestBehavior(HitTestMode.Transparent); // 配置浮层不阻塞交互
     }

     build() {
       Column() {
         Tabs() {
           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Pink);
           }.tabBar(SubTabBarStyle.of('订阅'));

           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Green);
           }.tabBar(SubTabBarStyle.of('推荐'));

           TabContent() {
             Column().width('100%').height('100%').backgroundColor(Color.Blue);
           }.tabBar(SubTabBarStyle.of('热门'));
         }
         .width('100%')
         .height('100%')
         .backgroundColor(0xf1f3f5)
         .barMode(this.barMode)
         .barWidth(200)
         .overlay(this.overlayExample(), { align: Alignment.Top });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

**Q：在Tabs组件中，由于Tabs组件自带滑动切换页面动画，所以在点击tabBar切换页面时会从当前页面滑动到目标页面，导致当前页面和目标页面的中间页面也被加载，如何只展示对应的TabContent的内容页？**

**A**：方案一：

* 由于Tabs组件自带滑动切换页面动画，在点击tabBar切换页面、会从当前页面滑动到目标页面，导致当前页面和目标页面的中间页面也被加载。可以使用自定义切换动画去规避Tabs组件自带的动画。参考customContentTransition使用说明。示例代码如下：

  ```ts
  @Entry
  @Component
  struct TabsExample {
    @State currentIndex: number = 0;
    private tabsController: TabsController = new TabsController();
    // 设置页面切换动画，代替滑动跳转页面动画
    private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition =
      (from: number, to: number) => {
        console.info(`from ${from} to ${to}`);
        let tabContentAnimatedTransition = {
          timeout: 1000,
          transition: (proxy: TabContentTransitionProxy) => {
            this.getUIContext().animateTo({
              duration: 0,
              onFinish: () => {
                proxy.finishTransition();
              }
            }, () => {
            });
          }
        } as TabContentAnimatedTransition;
        return tabContentAnimatedTransition;
      };

    build() {
      Column() {
        Tabs({ index: this.currentIndex, controller: this.tabsController }) {
          TabContent() {
            MyComponent({ color: '#00CB87' });
          }.tabBar(SubTabBarStyle.of('green'));

          TabContent() {
            MyComponent({ color: '#007DFF' });
          }.tabBar(SubTabBarStyle.of('blue'));

          TabContent() {
            MyComponent({ color: '#FFBF00' });
          }.tabBar(SubTabBarStyle.of('yellow'));

          TabContent() {
            MyComponent({ color: '#E67C92' });
          }.tabBar(SubTabBarStyle.of('pink'));
        }
        .customContentTransition(this.customContentTransition)
        .width('100%')
        .height(296)
        .onChange((index: number) => {
          this.currentIndex = index;
        });
      };
    }
  }

  @Component
  struct MyComponent {
    private color: string = "";

    aboutToAppear(): void {
      console.info(`------aboutToAppear backgroundColor: ${this.color}`); // 通过打印日志可以观察到没有加载中间页面
    }

    aboutToDisappear(): void {
      console.info(`------aboutToDisappear backgroundColor: ${this.color}`);
    }

    build() {
      Column() {
        Text(this.color)
          .width('90%')
          .height(200)
          .borderRadius(10)
          .backgroundColor($r('sys.color.comp_background_focus'))
          .textAlign(TextAlign.Center)
          .fontSize(30);
      };
    }
  }
  ```

方案二：

* 若要同时规避加载中间页面、又要保留手势滑动切换页面功能，可以使用Swiper自定义实现Tabs组件。通过调用SwiperController的[changeIndex](../harmonyos-references/ts-container-swiper.md#changeindex12)方法翻至指定页面，useAnimation设置为false时没有动效。示例代码如下：

  ```ts
  class MyDataSource implements IDataSource {
    private list: number[] = [];

    constructor(list: number[]) {
      this.list = list;
    }

    totalCount(): number {
      return this.list.length;
    }

    getData(index: number): number {
      return this.list[index];
    }

    registerDataChangeListener(): void {
    }

    unregisterDataChangeListener() {
    }
  }

  @Entry
  @Component
  struct SwiperExample {
    private swiperController: SwiperController = new SwiperController();
    private data: MyDataSource = new MyDataSource([]);

    aboutToAppear(): void {
      let list: number[] = [];
      for (let i = 1; i <= 10; i++) {
        list.push(i);
      }
      this.data = new MyDataSource(list);
    }

    build() {
      Column({ space: 5 }) {
        Swiper(this.swiperController) {
          LazyForEach(this.data, (item: string) => {
            Text(item.toString())
              .width('90%')
              .height(160)
              .borderRadius(10)
              .backgroundColor($r('sys.color.comp_background_focus'))
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .cachedCount(2)
        .index(1)
        .autoPlay(true)
        .interval(4000)
        .loop(true)
        .duration(1000)
        .itemSpace(0)
        .indicator(false);

        Row({ space: 12 }) {
          Button('change to index:4')
            .onClick(() => {
              this.swiperController.changeIndex(3, false);
            });
          Button('change to index:7')
            .onClick(() => {
              this.swiperController.changeIndex(6, false);
            });
        }.margin(5);
      }.width('100%')
      .margin({ top: 5 });
    }
  }
  ```
