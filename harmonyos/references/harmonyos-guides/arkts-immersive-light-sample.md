---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-immersive-light-sample
title: 沉浸光感典型场景
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 沉浸光感 > 沉浸光感典型场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:50+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9e640658441feb7e601e95e72788d906c3fa46a41902b5b54f73d0ee6942799a
---

本文档提供沉浸光感两个典型场景的开发指导，包括搜索框标题栏效果和内容区标题栏开启沉浸光感。

## 搜索框标题栏效果

在信息浏览类应用（如新闻、贴吧、小说阅读等应用）的场景中，用户上滑首页内容区后，标题栏显示范围可随之缩小，同时通过沉浸光感提升标题栏的交互体验。

1. 设置底部Tabs悬浮并为Tabs组件开启沉浸光感，同时使用[ExpandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)将显示内容延伸至状态栏区域，使应用整体体验更加一致。

   ```ts
   @Entry
   @ComponentV2
   struct BestPractise {
     @Local currentTab: number = 0
     exploreStack: NavPathStack = new NavPathStack()
     gameStack: NavPathStack = new NavPathStack()

     @Builder
     BottomTabBarItem(title: string, icon: Resource, index: number) {
       Column() {
         SymbolGlyph(icon)
           .fontSize(22)
           .fontColor(this.currentTab === index ? ['#007dff'] : ['#999999'])
         Text(title)
           .fontSize(10)
           .fontColor(this.currentTab === index ? '#007dff' : '#999999')
          .margin({ top: 2 })
       }.justifyContent(FlexAlign.Center)
       .width('100%')
       .height('100%')
     }

     @Builder
     tabExploreContent() {
       // 通过系统路由表的方式配置对应的页面跳转
       Navigation(this.exploreStack, {name: 'explore'})
         .hideTitleBar(true)
         .expandSafeArea([SafeAreaType.SYSTEM])
     }

     @Builder
     tabGameContent() {
       // 通过系统路由表的方式配置对应的页面跳转
       Navigation(this.gameStack, {name: 'game'})
         .hideTitleBar(true)
         .expandSafeArea([SafeAreaType.SYSTEM])
     }

     build() {
       Tabs({ index: this.currentTab }) {
         TabContent() {
           this.tabExploreContent()
         }.tabBar(this.BottomTabBarItem('探索', $r('sys.symbol.compass'), 0))
         // 内容区延伸到状态栏区域，形成整体的交互体验
         .expandSafeArea([SafeAreaType.SYSTEM])

         TabContent() {
           this.tabGameContent()
         }.tabBar(this.BottomTabBarItem('游戏', $r('sys.symbol.gamecontroller'), 1))
         .expandSafeArea([SafeAreaType.SYSTEM])

         TabContent() {
         }.tabBar(this.BottomTabBarItem('应用', $r('sys.symbol.grid'), 2))

         TabContent() {
         }.tabBar(this.BottomTabBarItem('元服务', $r('sys.symbol.gearshape'), 3))
       }
       .barPosition(BarPosition.End)
       .barMode(BarMode.Fixed)
       .barOverlap(true)
       .barHeight(56)
       .barFloatingStyle({ barBottomMargin: 8, systemMaterial: new uiMaterial.ImmersiveMaterial({}) })
       .scrollable(true)
       .expandSafeArea([SafeAreaType.SYSTEM])
       .onChange((index: number) => {
         this.currentTab = index
       })
     }
   }
   ```
2. 针对跳转的目标页面，通过[NavigationTitleOptions](../harmonyos-references/ts-basic-components-navigation.md#navigationtitleoptions11)为对应的页签页面标题栏区域开启沉浸光感。建议将Navigation组件的BarStyle设置为STACK模式，使内容区显示在标题栏下方，从而实现透底的效果。下面代码实现以下效果：

* 标题栏以及标题栏子组件开启沉浸光感。
* 上滑时搜索框隐藏，分类列表保留并突出显示。分类列表项开启沉浸光感，提升用户交互体验和内容曝光率。

  ```ts
  @ComponentV2
  struct ExploreHomePage {
    @Local currentIndex: number = 0
    @Local searchOpacity: number = 1
    @Local classifyType: Array<string> = [
       '策略', '动作', '竞技', '射击', '卡牌', '体育', '休闲', '音乐'
     ]
    titleHeight:number = 150
    @Local scrollOffset: number = 0
    @Local titleOffset: number = 0
    @Builder
    exploreTitleBar() {
      Column() {
        Row() {
          Text('探索').fontSize(28).fontWeight(FontWeight.Bold).fontColor('#1A1A1A')
          Blank()
          Search({ placeholder: '探索探索' })
            .searchButton('搜索')
            .height(40)
            .width(220)
            .systemMaterial(new uiMaterial.ImmersiveMaterial({}))
        }.expandSafeArea([SafeAreaType.SYSTEM])
        .width('100%')
        .opacity(this.searchOpacity)
        .height(50)

        List({space: 12}) {
          ForEach(this.classifyType, (item: string, index: number) => {
            ListItem() {
              Row() {
                SymbolGlyph($r('sys.symbol.star_fill'))
                  .fontSize(20)
                  .fontColor(['#d3d3d3'])
                  .margin({left: 16})
                Text(item)
                  .fontSize(16)
                  .fontColor(this.currentIndex === index ? Color.White : '#666666')
                  .padding({ left: 4, right: 12, top: 6, bottom: 6})
              }.borderRadius(16)
              .systemMaterial(new uiMaterial.ImmersiveMaterial({
                materialColor: this.currentIndex === index ? '#333333' : undefined,
                lightEffect: {color: Color.White}
              }))
            }
          })
        }.listDirection(Axis.Horizontal)
        .width('100%')
        .scrollBar(BarState.Off)
        .margin(5)
      }.expandSafeArea([SafeAreaType.SYSTEM])
      .width('100%')
      .height(this.titleHeight)
      .padding({ left: 20, right: 20})
      .position({x: 0, y: -this.titleOffset})
      // 设置Column组件开启沉浸光感
      .systemMaterial(new uiMaterial.ImmersiveMaterial({}))
    }

    build() {
      NavDestination() {
        Scroll() {
          // 滑动区域的具体内容
          Column() {
            Image($r('app.media.startIcon')).width('100%').height(180)
              .borderRadius(12)
              .backgroundColor('#e0e0e0')
              .objectFit(ImageFit.Cover)

            List() {
              // 开发者需要自定义参数listItems, 示例中的数据结构为 interface ListItemData { name: string; image: Resource; id: string}
              ForEach(listItems, (item: ListItemData) => {
                ListItem() {
                  Row() {
                    SymbolGlyph(item.image).fontSize(36)
                      .fontColor(['#007dff'])
                      .margin({ right: 16})
                    Text(item.name).fontSize(16)
                      .fontColor('#333333')
                  }.width('100%')
                  .padding({ left: 20, right: 20, top: 14, bottom: 14 })
                }
              }, (item: ListItemData) => item.id)
            }
          }
        }
        // 避让标题栏显示区域
        .contentStartOffset(this.titleHeight)
        .scrollable(ScrollDirection.Vertical)
        .scrollBar(BarState.Off)
        .edgeEffect(EdgeEffect.Spring)
        .width('100%')
        .height('100%')
        .onDidScroll((xOffset: number, yOffset: number, state: ScrollState) => {
          this.scrollOffset += yOffset
          // 搜索框大小范围内
          if (this.scrollOffset <= 50) {
            this.titleOffset = this.scrollOffset;
            this.searchOpacity = 1 - this.titleOffset / 50
          }
        })
      }.title(
        { builder: this.exploreTitleBar, height: this.titleHeight },
        { barStyle: BarStyle.STACK,
          systemMaterial: new uiMaterial.ImmersiveMaterial({})
       }
     ).hideBackButton(true)
      .expandSafeArea([SafeAreaType.SYSTEM])
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/YNCm_gu0Szm_a6E38g8HqA/zh-cn_image_0000002736461699.gif)

## 内容区标题栏开启沉浸光感

当前沉浸光感存在生效约束，具体约束参考[沉浸光感功耗优化](arkts-immersive-light-sense-constraints.md)。针对内容区滑动且内容区存在多层标题的场景，当内容区的标题滑动到标题栏区域时，可将对应的内容嵌入标题栏中显示，实现内容区标题在NavDestination标题栏区域的展示，从而提升用户交互体验。

1. 提取内容区中小标题为独立组件。

   ```ts
   @ComponentV2
   export struct ClassifyComponent {
     classifyType: Array<string> = [
       '策略', '动作', '竞技', '射击', '卡牌', '体育', '休闲', '音乐'
     ]

     @Local currentIndex: number = 0

     build() {
       List({space: 12}) {
         ForEach(this.classifyType, (item: string, index) => {
           ListItem() {
             Row() {
               SymbolGlyph($r('sys.symbol.star_fill'))
                 .fontSize(20)
                 .fontColor(['#d3d3d3'])
                 .margin({ left: 16})
               Text(item)
                 .fontColor(this.currentIndex === index ? Color.White : '#666666')
                 .fontSize(16)
                 .padding({ left: 4, right: 12, top: 6, bottom: 6})
             }.borderRadius(16)
             .systemMaterial(new uiMaterial.ImmersiveMaterial({
               materialColor: this.currentIndex === index ? '#333333' : undefined,
               lightEffect: { color: Color.White }
             }))
             .onClick(() => {
               this.currentIndex = index
             })
           }
         })
       }.listDirection(Axis.Horizontal)
       .width('100%')
       .scrollBar(BarState.Off)
       .expandSafeArea([SafeAreaType.SYSTEM])
       .margin(5)
       .alignListItem(ListItemAlign.Center)
     }
   }
   ```
2. 滑动内容区，当内容区标题滑动到标题栏区域时，将其切换到标题栏中显示。

   ```ts
   // 添加系统路由表入口
   @ComponentV2
   struct GamePage {
     @Local titleHeight: number = 100
     @Local scrollOffset: number = 0
     @Local showTitle: boolean = false
     @Local titleOpacity: number = 1
     @Local contentOffset: number = 0
     totalOffset: number = 0
     @Local textOffset: number = 0
     titleEnd: number = 0
     titleStart: number = 0
     @Local listVisible: Visibility = Visibility.Visible

     @Builder
     gameTitleBar() {
       Row() {
         if (this.showTitle) {
           ClassifyComponent()
         } else {
           Text('游戏')
             .fontSize(28)
             .fontWeight(FontWeight.Bold)
             .fontColor('#1A1A1A')
             .opacity(this.titleOpacity)
             .id('text')
           Blank()
         }
         Button() {
           SymbolGlyph($r('sys.symbol.AI_search')).fontSize(20)
         }.borderRadius(180).width(40).height(40)
           .systemMaterial(new uiMaterial.ImmersiveMaterial({
             lightEffect: { color: Color.White },
             materialColor: '#d3d3d3'
         }))
         .backgroundColor(Color.Transparent)
       }.expandSafeArea([SafeAreaType.SYSTEM])
       .width('100%')
       .height('100%')
       .padding({ left: 20, right: 20 })
       .systemMaterial(new uiMaterial.ImmersiveMaterial({}))
       .alignItems(VerticalAlign.Center)
     }

     build() {
       NavDestination() {
         Scroll() {
           Column() {
             // 请开发者替换为实际的资源文件
             Image($r('app.media.background'))
               .width('100%')
               .height(180)
               .borderRadius(12)
               .backgroundColor('#fff3e0')
               .objectFit(ImageFit.Cover)
             ClassifyComponent().id('content').visibility(this.showTitle ? Visibility.Hidden : Visibility.Visible)
             List() {
               // 开发者需要自定义参数listItems, 示例中的数据结构为 interface ListItemData { name: string; image: Resource; id: string}
               ForEach(listItems, (item: ListItemData) => {
                 ListItem() {
                   Row() {
                     SymbolGlyph(item.image).fontSize(36).fontColor(['#ff6d00']).margin({ right: 16 })
                     Text(item.name).fontSize(16).fontColor('#333333')
                   }.width('100%')
                   .padding({ left: 20, right: 20, top: 14, bottom: 14 })
                 }
               }, (item: ListItemData) => item.id)
             }.width('100%')
             .margin({top: 8})
             .nestedScroll({scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST})
             .divider({strokeWidth: 5, color: '#e0e0e0', startMargin: 72, endMargin: 20})
           }.padding({left: 16, right: 16, top: 8, bottom: 16})
         }
         .contentStartOffset(this.titleHeight)
         .scrollable(ScrollDirection.Vertical)
         .scrollBar(BarState.Off)
         .edgeEffect(EdgeEffect.Spring)
         .width('100%')
         .height('100%')
         .onDidScroll((xOffset: number, yOffset: number) => {
           this.totalOffset += yOffset
           let curOffset = this.contentOffset - this.totalOffset
           if (curOffset > this.titleEnd) {
             this.showTitle = false;
             this.listVisible = Visibility.Hidden
             return
           }
           if (curOffset < this.titleEnd) {
             this.showTitle = true;
             this.listVisible = Visibility.Visible
             return
           }
           this.titleHeight = (curOffset - this.titleEnd) / (this.titleHeight - this.titleEnd)
         })
       }.onShown(() => {
         let titleInfo = this.getUIContext().getComponentUtils().getRectangleById('text');
         this.titleStart = this.getUIContext().px2vp(titleInfo.windowOffset.y)
         this.titleEnd = this.getUIContext().px2vp(titleInfo.size.height)
         this.contentOffset = this.getUIContext().px2vp(this.getUIContext().getComponentUtils().getRectangleById('content').windowOffset.y)
       })
       .expandSafeArea([SafeAreaType.SYSTEM])
       .hideBackButton(true)
       .title({ builder: this.gameTitleBar, height: this.titleHeight }, {
         barStyle: BarStyle.STACK,
         systemMaterial: new uiMaterial.ImmersiveMaterial({})
       })
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ULj_6XfySu22pqaDb0ptOg/zh-cn_image_0000002736582479.gif)
