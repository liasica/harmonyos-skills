---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1588
title: 如何解决Tabs和滚动组件的嵌套滑动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Tabs和滚动组件的嵌套滑动问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aab1d7eb8e9afa92c2e001b1a21e99a9f81ff111a5ca961294823d39fda8183b
---

## 问题现象

Tabs组件存在横向滑动的控制手势，当其内部嵌套Tabs或横向的List、Scroll、Swiper、Grid等滚动与滑动组件时，会产生横向滚动手势冲突，导致外部的Tabs无法横向切换。以Grid为例问题现象如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/zRj0PjIGR5Cn2z6XFc_UyA/zh-cn_image_0000002628770204.png "点击放大")

当Grid组件滑动到右侧底部时，预期触发Tabs从“首页1”切换到“首页2”，实际未触发。

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)是通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。可以通过控制器[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)控制Tabs组件进行页签切换，不支持一个TabsController控制多个Tabs组件。
* [List](../harmonyos-references/ts-container-list.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[Grid](../harmonyos-references/ts-container-grid.md)是官方提供的滑动与滚动组件，支持[滚动组件通用接口](../harmonyos-references/ts-container-scrollable-common.md)。且都可以通过自身属性控制横向或纵向滚动，当为横向滚动时，与Tabs嵌套时会发生手势冲突。
* [Swiper](../harmonyos-references/ts-container-swiper.md)组件是滑块视图容器，提供子组件滑动轮播显示的能力，可以通过[SwiperController](../harmonyos-references/ts-container-swiper.md#swipercontroller)控制Swiper的切换。

## 解决方案

* **方案一**：基于滚动组件通用接口[nestedScroll](../harmonyos-references/ts-container-scrollable-common.md#nestedscroll11)解决滚动冲突。

  List、Scroll、Grid滚动组件支持nestedScroll通用属性，可以设置滚动优先级。以Tabs嵌套横向滚动的Grid为例，在开启Tabs滑动切换的前提下给Grid设置嵌套滚动nestedScroll属性。

  ```ts
  @Entry
  @Component
  struct TabsGridDemo {
    tabsController: TabsController = new TabsController();
    gridData: Resource[] = [];
    @State selectIndex: number = 0;

    @Builder
    tabContent(nam: string, targetIndex: number) {
      Text(nam)
        .fontColor(this.selectIndex === targetIndex ? '#0a59f7' : '#99000000')
    }

    aboutToAppear(): void {
      for (let i = 1; i <= 10; i++) {
        this.gridData.push($r(`app.media.${i}`));
      }
    }

    build() {
      Column() {
        Tabs({ controller: this.tabsController }) {
          TabContent() {
            Column() {
              Grid() {
                ForEach(this.gridData, (item: Resource) => {
                  GridItem() {
                    Image(item)
                      .height(150)
                      .width(150)
                  };
                });
              }
              .height('25%')
              .columnsGap(16)
              .rowsTemplate('1fr')
              // 设置Grid优先滚动
              .nestedScroll({
                scrollForward: NestedScrollMode.SELF_FIRST,
                scrollBackward: NestedScrollMode.SELF_FIRST,
              });
            }
            .width('100%')
            .height('100%')
            .padding({
              left: 20
            })
          }.tabBar(this.tabContent('首页1', 0));

          TabContent() {
          }.tabBar(this.tabContent('首页2', 1));
        }
        .onSelected((index: number) => {
          this.selectIndex = index;
        })

      }.height('100%').width('100%');
    }
  }
  ```
* **方案二**：通过自定义手势判断[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)实现Tabs嵌套内部组件滚动逻辑判断。
  + Tabs嵌套Swiper组件的实现逻辑如下：
    1. 当Swiper显示位置为第一个卡片时，若继续往右滑，执行Tabs切换到上一个页签。
    2. 当Swiper显示位置为最后一个卡片时，若继续往左滑，执行Tabs切换到下一个页签。
    3. 其他时候左右滑动手势执行Swiper切换功能，左滑切换上一个卡片，右滑切换下一个卡片。

       ```ts
       @Entry
       @Component
       struct TabsSwiperDemo {
         tabsController: TabsController = new TabsController();
         swiperController: SwiperController = new SwiperController();
         data: number[] = [1, 2, 3];
         @State selectIndex: number = 0;

         @Builder
         tabContent(nam: string, targetIndex: number) {
           Text(nam)
             .fontColor(this.selectIndex === targetIndex ? '#0a59f7' : '#99000000')
         }

         build() {
           Column() {
             Tabs({ controller: this.tabsController }) {
               TabContent() {
                 Text('首页的内容').fontSize(30);
               }.tabBar(this.tabContent('首页', 0));

               TabContent() {
                 // Swiper在第二个TabContent内。
                 Swiper(this.swiperController) {
                   ForEach(this.data, (item: number, index: number) => {
                     Text(item.toString())
                       .width('100%')
                       .height('100%')
                       .textAlign(TextAlign.Center)
                       .fontSize(30)
                       .gesture(
                         PanGesture()
                           .onActionStart(() => {
                             console.info('Pan start');
                           })
                           .onActionUpdate(() => {
                             console.info('Pan update');
                           })
                           .onActionEnd((event: GestureEvent) => {
                             // Swiper在Tabs第二页内采用if/else逻辑优先判定Swiper边缘滑动情况。
                             if (index === 0 && event.offsetX > 0) {
                               this.tabsController.changeIndex(0); // Swiper滑动到第一页继续右滑，Tabs控制器跳转到第一页。
                             } else if (index === (this.data.length - 1) && event.offsetX < 0) {
                               this.tabsController.changeIndex(2); // Swiper滑动到最后一页继续左滑，Tabs控制器跳转到第三页。
                             } else if (event.offsetX < 0) {
                               this.swiperController.showNext(); // Swiper控制器。
                             } else if (event.offsetX > 0) {
                               this.swiperController.showPrevious(); // Swiper控制器。
                             }
                           })
                       );
                   }, (item: string) => item);
                 };
               }.tabBar(this.tabContent('发现', 1));

               TabContent() {
                 Text('推荐的内容').fontSize(30);
               }.tabBar(this.tabContent('推荐', 2));

               TabContent() {
                 Text('我的内容').fontSize(30);
               }.tabBar(this.tabContent('我的', 3));
             }
             .onSelected((index: number) => {
               this.selectIndex = index;
             })
           }.width('100%').height('100%');
         }
       }
       ```
  + Tabs嵌套Tabs组件的实现逻辑和上述Swiper相似，只需在内层Tabs的第一个和最后一个TabContent绑定手势处理PanGesture即可。完整示例代码如下：

    ```ts
    @Entry
    @Component
    struct TabsTabsDemo {
      tabsController: TabsController = new TabsController();
      @State selectIndex0: number = 0; // 外部页签
      @State selectIndex1: number = 0; // 内部页签

      @Builder
      tabContent0(nam: string, targetIndex: number) { // 外层Tab栏
        Text(nam)
          .fontColor(this.selectIndex0 === targetIndex ? '#0a59f7' : '#99000000')
      }

      @Builder
      tabContent1(nam: string, targetIndex: number) { // 内层Tab栏
        Text(nam)
          .fontColor(this.selectIndex1 === targetIndex ? '#0a59f7' : '#99000000')
      }

      build() {
        Column() {
          Tabs({ controller: this.tabsController }) {
            TabContent() {
              Text('首页的内容').fontSize(30);
            }.tabBar(this.tabContent0('首页', 0));

            TabContent() {
              Tabs({ barPosition: BarPosition.Start }) {
                TabContent() {
                  Text('tab1').fontSize('30fp');
                }.tabBar(this.tabContent1('tab1', 0))
                .gesture(
                  PanGesture({ fingers: 1, distance: 1, direction: PanDirection.Right })
                    .onActionStart(() => {
                      console.info('Pan start');
                    })
                    .onActionEnd(() => {
                      this.tabsController.changeIndex(0);
                    })
                );

                // 中间的其它TabContent
                TabContent() {
                  Text('tab2').fontSize('30fp');
                }.tabBar(this.tabContent1('tab2', 1))
                .gesture(
                  PanGesture({ fingers: 1, distance: 1, direction: PanDirection.Left })
                    .onActionStart(() => {
                      console.info('Pan start');
                    })
                    .onActionEnd(() => {
                      this.tabsController.changeIndex(2);
                    })
                );
              }
              .onSelected((index: number) => {
                this.selectIndex1 = index;
              })
            }.tabBar(this.tabContent0('发现', 1));

            TabContent() {
              Text('推荐的内容').fontSize(30);
            }.tabBar(this.tabContent0('推荐', 2));

            TabContent() {
              Text('我的内容').fontSize(30);
            }.tabBar(this.tabContent0('我的', 3));
          }
          .onSelected((index: number) => {
            this.selectIndex0 = index;
          })
        }.width('100%').height('100%');
      }
    }
    ```
* **方案三**：使用[onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13)拦截内部组件滑动。

  可以使用手势拦截增强解决Tabs多层嵌套滑动冲突问题。使用示例请参考[嵌套场景下拦截内部容器手势](../harmonyos-references/ts-gesture-blocking-enhancement.md#示例2嵌套场景下拦截内部容器手势)，通过onGestureRecognizerJudgeBegin监听手势事件，内层Tabs到头/尾时拒绝手势传递，允许外层Tabs响应。

## 总结

| 方案 | 局限性 | 本知识适用场景 | 拓展适用场景 |
| --- | --- | --- | --- |
| 方案一：基于滚动组件通用接口nestedScroll解决滚动冲突。 | 内部组件必须支持滚动与滑动组件的通用nestedScroll接口。 | Tabs嵌套List、Scroll、Grid组件。 | List、Scroll、Grid组件嵌套List、Scroll、Grid组件。 |
| 方案二：通过自定义手势判断PanGesture实现Tabs嵌套内部组件滚动逻辑判断。 | 内部为List、Scroll、Grid等组件时实现较麻烦。 | Tabs嵌套Swiper、Tabs组件。 | Swiper组件嵌套Swiper、Tabs组件。 |
| 方案三：使用onGestureRecognizerJudgeBegin拦截内部组件滑动。 | 不支持内部为Scroll、List、Grid组件。 | Tabs嵌套Swiper、Tabs组件。 | Swiper组件嵌套Swiper、Tabs组件。 |

综上所述，总结如下：

1. Swiper组件的[nestedScroll](../harmonyos-references/ts-container-swiper.md#nestedscroll11)属性与Scroll、List、Grid的nestedScroll属性不一致。且Swiper不支持滚动组件通用属性。所以当Tabs嵌套Swiper时方案一并不适用。
2. Tabs组件属于导航与切换组件，也不支持nestedScroll和滚动组件通用属性，所以当Tabs嵌套Tabs时方案一也不适用。
3. 当Tabs内部嵌套List、Scroll、Grid组件时，优先选用方案一，内部嵌套Tabs或Swiper时，优先选用方案二，方案三。

## 常见FAQ

Q：Tabs嵌套Web组件出现左右滑动问题如何解决？

A：请参考[Tabs组件嵌套Web，无法左右滑动](faqs-arkweb-152.md)中的解决方案。

Q：Tabs嵌套Scroll组件，如何实现每个TabContent页签中的Scroll容器可以垂直滑动，横向滑动时可以切换页签？

A：Tabs组件的[vertical](../harmonyos-references/ts-container-tabs.md#vertical)属性设置为false，[scrollable](../harmonyos-references/ts-container-tabs.md#scrollable)属性设置为true，即可通过左右滑动页面内容切换页签。Scroll组件的[scrollable](../harmonyos-references/ts-container-scroll.md#scrollable)属性设置为ScrollDirection.Vertical，可以竖直方向滚动其中内容。
