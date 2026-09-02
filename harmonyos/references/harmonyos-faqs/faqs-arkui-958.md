---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-958
title: Tabs如何实现TabBar中TabItem不均匀分布
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs如何实现TabBar中TabItem不均匀分布
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0948d0f5665ef3ea0b8f6ac59654d7b0eb167a2afc7fd9a00083a6a9a594a26c
---

## 问题现象

如何实现Tabs的页签不均匀分布，两个靠左，两个靠右，中间留下一个按钮的区域。

## 背景知识

* [position](../harmonyos-references/ts-universal-attributes-location.md#position)(value:[Position](../harmonyos-references/ts-types.md#position)|[Edges](../harmonyos-references/ts-types.md#edges12)|[LocalizedEdges](../harmonyos-references/ts-types.md#localizededges12))确定子组件相对父组件内容区的位置。其中Edges类型基于父组件内容区四边确定位置，top/left/right/bottom分别为组件各边距离父组件内容区相应边的边距，通过边距来确定组件相对于父组件内容区的位置。
* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。

## 解决方案

方案一：利用组件的position属性自定义每一个TabItem的位置。

1. 使用@Builder装饰器自定义以Column为主体的TabItem组件，为Column设置position属性，以不同TabItem的Index为条件，为每一个TabItem设置不同的边距值，达到自定义每一个TabItem的位置。

   ```ts
   @Builder
   TabItem(tabName: string, tabIndex: number) {
     // 标签页项的布局
     Column({ space: 10 }) {
       Column() {
         Image($r('app.media.startIcon'))
           .width(32).height(32)
           .margin({ top: 5 });
         Text(tabName).fontSize(14)
           .margin({ top: 5 });
       }
       .width('100%')
       .height('10%')
       .justifyContent(FlexAlign.Center);
     }
     .justifyContent(FlexAlign.Center)
     .onClick(() => {
       this.controller.changeIndex(tabIndex);
       this.focusIndex = tabIndex;
     })
     .width('12%')
     .padding({ bottom: 10 })
     .backgroundColor(Color.White)
     .position( // 设置TabItem的相对位置
       tabIndex === 1 ? { left: 80 } :
         tabIndex === 2 ? { right: 90 } :
           tabIndex === 3 ? { right: 0 } : {});
   }
   ```
2. 最后用Row组件和ForEach方法依序为TabItem赋Index值。则可实现TabItem在TabBar中不均匀分布的效果。

   ```ts
   // 用Row组件实现TabBar效果
   Row() {
     ForEach(this.tabArray, (item: number, index: number) => {
       this.TabItem('页签 ' + item, index);
     });
   }
   .justifyContent(FlexAlign.SpaceBetween)
   .alignItems(VerticalAlign.Bottom)
   .width('100%')
   .backgroundColor(Color.White);
   ```

完整示例参考如下：

```ts
@Entry
@Component
export struct CusTab2 {
  @State tabArray: Array<number> = [0, 1, 2, 3];
  @State focusIndex: number = 0;
  private controller: TabsController = new TabsController();

  @Builder
  TabItem(tabName: string, tabIndex: number) {
    // 标签页项的布局
    Column({ space: 10 }) {
      Column() {
        Image($r('app.media.startIcon'))
          .width(32).height(32)
          .margin({ top: 5 });
        Text(tabName).fontSize(14)
          .margin({ top: 5 });
      }
      .width('100%')
      .height('10%')
      .justifyContent(FlexAlign.Center);
    }
    .justifyContent(FlexAlign.Center)
    .onClick(() => {
      this.controller.changeIndex(tabIndex);
      this.focusIndex = tabIndex;
    })
    .width('12%')
    .padding({ bottom: 10 })
    .backgroundColor(Color.White)
    .position( // 设置TabItem的相对位置
      tabIndex === 1 ? { left: 80 } :
        tabIndex === 2 ? { right: 90 } :
          tabIndex === 3 ? { right: 0 } : {});
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.BottomStart }) {
        // Tabs
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          ForEach(this.tabArray, (item: number) => {
            TabContent() {
              Text('我是页面 ' + item + ' 的内容')
                .height(10)
                .width('100%')
                .fontSize(30)
                .textAlign(TextAlign.Center);
            }
            .backgroundColor(Color.White);
          });
        }
        .barHeight(0)
        .animationDuration(100)
        .onChange((index: number) => {
          console.info('foo change');
          this.focusIndex = index;
        });

        // 用Row组件实现TabBar效果
        Row() {
          ForEach(this.tabArray, (item: number, index: number) => {
            this.TabItem('页签 ' + item, index);
          });
        }
        .justifyContent(FlexAlign.SpaceBetween)
        .alignItems(VerticalAlign.Bottom)
        .width('100%')
        .backgroundColor(Color.White);

      }
      .width('100%');
    }
    .height('100%');
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/z9KWFqpDQcq-Ph41r6OVRg/zh-cn_image_0000002658800929.gif "点击放大")

方案二：设置异形TabBar达到不均匀分布的效果。

1. 左右四栏设置宽度占比18%，中间构造异形导航宽度占比28%。

   ```ts
   @Builder
   Tab(tabName: string, tabIndex: number) {
     Column({ space: 10 }) {
       Stack() {
         Column() {
           Image($r('app.media.startIcon'))
             .width(32).height(32);
           Text(tabName).fontSize(14)
             .margin({ top: 5 });
         }
         .width('100%')
         .justifyContent(FlexAlign.Center);
       }
       .margin({ bottom: tabIndex === 2 ? 40 : 0 });
     }
     .justifyContent(FlexAlign.Center)
     .onClick(() => {
       this.controller.changeIndex(tabIndex);
       this.focusIndex = tabIndex;
     })
     .width(tabIndex === 2 ? '28%' : '18%')
     // 左右四栏设置宽度占比18%，中间构造异形导航宽度占比28%
     .padding({ top: 10, bottom: 10 })
     .backgroundColor(Color.White)
     .borderRadius(tabIndex === 2 ? { topLeft: '50%', topRight: '50%' } : {});
   }
   ```

完整示例参考如下：

```ts
@Entry
@Component
export struct CusTab2 {
  @State tabArray: Array<number> = [0, 1, 2, 3, 4];
  @State focusIndex: number = 0;
  private controller: TabsController = new TabsController();

  @Builder
  Tab(tabName: string, tabIndex: number) {
    Column({ space: 10 }) {
      Stack() {
        Column() {
          Image($r('app.media.startIcon'))
            .width(32).height(32);
          Text(tabName).fontSize(14)
            .margin({ top: 5 });
        }
        .width('100%')
        .justifyContent(FlexAlign.Center);
      }
      .margin({ bottom: tabIndex === 2 ? 40 : 0 });
    }
    .justifyContent(FlexAlign.Center)
    .onClick(() => {
      this.controller.changeIndex(tabIndex);
      this.focusIndex = tabIndex;
    })
    .width(tabIndex === 2 ? '28%' : '18%')
    // 左右四栏设置宽度占比18%，中间构造异形导航宽度占比28%
    .padding({ top: 10, bottom: 10 })
    .backgroundColor(Color.White)
    .borderRadius(tabIndex === 2 ? { topLeft: '50%', topRight: '50%' } : {});
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.BottomStart }) {
        // tabs
        Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
          ForEach(this.tabArray, (item: number) => {
            TabContent() {
              Text('我是页面 ' + item + ' 的内容')
                .height(10)
                .width('100%')
                .fontSize(30)
                .textAlign(TextAlign.Center);
            }
            .backgroundColor('#F1F3F5');
          });
        }
        .barHeight(0)
        .animationDuration(100)
        .onChange((index: number) => {
          console.info('foo change');
          this.focusIndex = index;
        }); // 页签

        Row() {
          ForEach(this.tabArray, (item: number, index: number) => {
            this.Tab('页签 ' + item, index);
          });
        }
        .justifyContent(FlexAlign.SpaceBetween)
        .alignItems(VerticalAlign.Bottom)
        .width('100%');
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/_WPSkHNCThKcLtEYmzDtJg/zh-cn_image_0000002628401672.gif "点击放大")

## 总结

使用@Builder装饰器自定义以Column为主体的TabItem组件，为Column设置position属性，以不同TabItem的Index为条件，为每一个TabItem设置不同的边距值，达到自定义每一个TabItem的位置。
