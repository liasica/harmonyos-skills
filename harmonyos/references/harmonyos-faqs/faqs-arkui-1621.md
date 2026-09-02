---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1621
title: 如何实现点击下拉菜单跳转指定页签
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现点击下拉菜单跳转指定页签
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4406891c50a97f3ccd28ca6b00be040b9bc7d88c1c08656e3d4f9f9731cc8f58
---

## 问题现象

当Tabs组件包含多个TabBar时，横向滑动切换效率较低。希望提供下拉菜单，集中展示所有TabBar选项，用户点击菜单项可直接定位至目标页。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/HoBnVb1HQr-GLBvxNtIlKg/zh-cn_image_0000002658856843.gif "点击放大")

## 背景知识

* [Menu](../harmonyos-references/ts-basic-components-menu.md)：以垂直列表形式显示的菜单。
* [bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu)：给组件绑定菜单，点击后弹出菜单。

## 解决方案

1. 创建各菜单项的id和名称。

   ```ts
   export class TabDataModel {
     id: number = 0;
     navData: string | undefined = undefined;

     constructor(id: number, navData: string) {
       this.navData = navData;
       this.id = id;
     }
   }

   export const TAB_DATA: Array<TabDataModel> = [
     new TabDataModel(0, '关注'),
     new TabDataModel(1, '推荐'),
     new TabDataModel(2, '头条'),
     new TabDataModel(3, '发现'),
     new TabDataModel(4, '娱乐'),
     new TabDataModel(5, '体育'),
     new TabDataModel(6, '财经'),
     new TabDataModel(7, '军事'),
     new TabDataModel(8, '本地'),
     new TabDataModel(9, '视频'),
   ];
   ```
2. 实现导航栏的样式和点击的跳转逻辑。

   ```ts
   @Builder
   tabBuilder(index: number, name: string | undefined) {
     Stack() {
       Column() {
       }
       .width(this.tabsIndex === index ? 97 : 71)
       .backgroundColor(this.tabsIndex === index ? '#0A59F7' : '#000000')
       .opacity(this.tabsIndex === index ? 1 : 0.05)
       .height(38)
       .borderRadius(21);

       Text(name)
         .fontSize(14)
         .fontColor(this.tabsIndex === index ? Color.White : Color.Black)
         .opacity(this.tabsIndex === index ? 1 : 0.8)
         .height('100%')
         .id('section');
     }
     .margin(index !== 0 && index !== TAB_DATA.length ? { left: 9 } : {
       left: 0,
       right: 0
     })
     .align(Alignment.Center)
     .onClick(() => {
       console.info(`index = ${index}`);
       this.tabsIndex = index;
       this.tabsController.changeIndex(index);
     });
   }
   ```
3. 添加下拉菜单内容，并添加跳转Tabs页签逻辑。

   ```screen
   // 创建下拉菜单
   @Builder
   tabsMenu() {
     Menu() {
       ForEach(TAB_DATA, (item: TabDataModel) => {
         MenuItem({ content: item.navData })
           .onClick(() => {
             this.tabsIndex = item.id;
             this.tabsController.changeIndex(item.id); // 点击菜单中选项跳转指定的tab
           })
           .id('menu_item');
       });
     };
   }
   ```
4. 绑定下拉菜单内容到下拉按钮。

   ```ts
   Row() {
     Row() {
       Image($r('app.media.startIcon'))  // 资源文件需自行替换
         .width(38)
         .id('mainPageTabsImage');
     }
     .bindMenu(this.tabsMenu) // 绑定下拉菜单
   ```

完整示例参考如下：

```ts
export class TabDataModel {
  id: number = 0;
  navData: string | undefined = undefined;

  constructor(id: number, navData: string) {
    this.navData = navData;
    this.id = id;
  }
}

export const TAB_DATA: Array<TabDataModel> = [
  new TabDataModel(0, '关注'),
  new TabDataModel(1, '推荐'),
  new TabDataModel(2, '头条'),
  new TabDataModel(3, '发现'),
  new TabDataModel(4, '娱乐'),
  new TabDataModel(5, '体育'),
  new TabDataModel(6, '财经'),
  new TabDataModel(7, '军事'),
  new TabDataModel(8, '本地'),
  new TabDataModel(9, '视频'),
];

@Entry
@Component
export struct FunctionalScenes {
  @State tabsIndex: number = 0;
  tabsController: TabsController = new TabsController();
  private scrollController: Scroller = new Scroller();

  @Builder
  tabBuilder(index: number, name: string | undefined) {
    Stack() {
      Column() {
      }
      .width(this.tabsIndex === index ? 97 : 71)
      .backgroundColor(this.tabsIndex === index ? '#0A59F7' : '#000000')
      .opacity(this.tabsIndex === index ? 1 : 0.05)
      .height(38)
      .borderRadius(21);

      Text(name)
        .fontSize(14)
        .fontColor(this.tabsIndex === index ? Color.White : Color.Black)
        .opacity(this.tabsIndex === index ? 1 : 0.8)
        .height('100%')
        .id('section');
    }
    .margin(index !== 0 && index !== TAB_DATA.length ? { left: 9 } : {
      left: 0,
      right: 0
    })
    .align(Alignment.Center)
    .onClick(() => {
      console.info(`index = ${index}`);
      this.tabsIndex = index;
      this.tabsController.changeIndex(index);
    });
  }

  // 创建下拉菜单
  @Builder
  tabsMenu() {
    Menu() {
      ForEach(TAB_DATA, (item: TabDataModel) => {
        MenuItem({ content: item.navData })
          .onClick(() => {
            this.tabsIndex = item.id;
            this.tabsController.changeIndex(item.id); // 点击菜单中选项跳转指定的tab
          })
          .id('menu_item');
      });
    };
  }

  build() {
    Column() {
      Row() {
        Stack() {
          List({ scroller: this.scrollController }) {
            ForEach(TAB_DATA, (tabItem: TabDataModel) => {
              ListItem() {
                this.tabBuilder(tabItem.id, tabItem.navData);
              };
            });
          }
          .id("MainList")
          .margin({ top: 3 })
          .height(38)
          .listDirection(Axis.Horizontal)
          .padding({ right: 46 })
          .scrollBar(BarState.Off);

          Row() {
            Row() {
              Image($r('app.media.startIcon'))  // 资源文件需自行替换
                .width(38)
                .id('mainPageTabsImage');
            }
            .bindMenu(this.tabsMenu) // 绑定下拉菜单
            .justifyContent(FlexAlign.Center)
            .id('menu_button');
          }
          .linearGradient({
            angle: 90,
            colors: [['rgba(241, 241, 241, 0)', 0], ['#F1F3F5', 0.2], ['#F1F3F5', 1]]
          })
          .justifyContent(FlexAlign.End)
          .width(60)
          .height(43);
        }
        .alignContent(Alignment.TopEnd);
      }
      .padding({
        left: 0,
        right: 13
      })
      .margin({ top: 8 });

      Tabs({ controller: this.tabsController }) {
        ForEach(TAB_DATA, (tabItem: TabDataModel) => {
          TabContent() {
            Column() {
              Text(tabItem.navData);
            }
            .backgroundColor(Color.White)
            .width('100%')
            .height('100%')
            .alignItems(HorizontalAlign.Center)
            .justifyContent(FlexAlign.Center);
          }
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
          .align(Alignment.TopStart)
          .alignSelf(ItemAlign.Start);
        });
      }
      .margin({ top: 8 })
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
      .height('100%')
      .barWidth(0)
      .barHeight(0)
      .onChange((targetIndex: number) => {
        this.tabsIndex = targetIndex;
        this.scrollController.scrollToIndex(targetIndex, true, ScrollAlign.START);
      });
    }
    .height('100%')
    .backgroundColor("#F1F1F1")
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP]);
  }
}
```
