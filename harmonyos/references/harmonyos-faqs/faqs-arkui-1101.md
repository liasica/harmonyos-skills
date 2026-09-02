---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1101
title: HarmonyOS应用侧基于Tabs组件实现胶囊样式、悬浮留空及重叠毛玻璃等常见TabBar自定义样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > HarmonyOS应用侧基于Tabs组件实现胶囊样式、悬浮留空及重叠毛玻璃等常见TabBar自定义样式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:df7bbef8b2d3462c64eebe7cac288c88a6b3a4a0bf0f38022db6163e94b97c8c
---

## 问题现象

设置TabBar常见样式时可能会遇到如下问题：

场景一：使用Tabs组件实现侧边栏时，如何实现自顶到底的效果？

场景二：如何在页签被选中时改变字体颜色？

场景三：如何实现胶囊页签样式？

场景四：如何实现页签栏和内容区重叠，并启用毛玻璃效果？

场景五：如何实现悬浮式、两端留空的Tab栏样式？

场景六：当页签数量较多时，如何设置TabBar的样式？

场景七：如何在页签被选中时，让其上移并超出TabBar区域显示？

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [TabBar](../harmonyos-references/ts-container-tabcontent.md#tabbar)：设置TabBar上显示内容。
* [TabsOptions](../harmonyos-references/ts-container-tabs.md#tabsoptions15)的barModifier用于设置TabBar的通用属性。
* [barOverlap](../harmonyos-references/ts-container-tabs.md#baroverlap10)：设置TabBar是否背后变模糊并叠加在TabContent之上。
* [barBackgroundBlurStyle](../harmonyos-references/ts-container-tabs.md#barbackgroundblurstyle11)：设置TabBar的背景模糊材质。
* [SegmentButton](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md)：分段按钮组件，适用于页面切换、单选/多选场景。

## 解决方案

| 实现场景 | 实现方案 |
| --- | --- |
| 场景一：实现自顶到底效果。 | 通过自定义组件实现，导航栏使用List实现。 |
| 场景二：在页签被选中时改变字体颜色。 | 通过自定义TabBar实现。 |
| 场景三：实现胶囊页签样式。 | 方案一：使用SegmentButton与Tabs实现。 |
| 方案二：使用自定义页签实现。 |
| 场景四：实现页签栏和内容区重叠，并启用毛玻璃效果。 | 通过设置Tabs的barOverlap为true，并设置barBackgroundBlurStyle为BlurStyle.Thin。 |
| 场景五：实现悬浮式、两端留空的Tab栏样式。 | 方案一：使用自定义组件实现。 |
| 方案二：使用HdsTabs实现。 |
| 场景六：处理页签数较多时的TabBar的样式。 | 通过设置barMode为BarMode.Scrollable实现。 |
| 场景七：在页签被选中时使页签超出TabBar区域显示。 | 通过barModifier设置TabBar的clip属性实现。 |

* **场景一：实现自顶到底效果。**

  由于Tabs组件无法实现自顶到底的效果，可以通过自定义组件来达到此效果，导航栏可使用List实现。解决方案：参考[Tabs实现自顶到底效果](faqs-arkui-809.md)。
* **场景二：在页签被选中时改变字体颜色。**

  在页签被选中时改变字体颜色，可通过自定义页签实现。解决方案：参考[示例3（自定义页签切换联动）](../harmonyos-references/ts-container-tabs.md#示例3自定义页签切换联动)。
* **场景三：实现胶囊页签样式。**
  + 方案一：使用SegmentButton与Tabs实现。

    将SegmentButton作为页签，将Tabs的属性barHeight设置为0。参考代码如下所示：

    ```ts
    import { ItemRestriction, SegmentButton, SegmentButtonOptions, SegmentButtonTextItem } from '@kit.ArkUI';

    @Entry
    @Component
    struct CapsuleOne {
      tabList: string[] = ['我的内容', '探索内容'];
      @State currentIndex: number = 0;
      @State tabSelectedIndexes: number[] = [];
      @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
        buttons: [{ text: '我的' }, { text: '探索' }] as ItemRestriction<SegmentButtonTextItem>,
        textPadding: 6
      });

      build() {
        Column() {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes,
            // 点击SegmentButton时Tabs页面切换
            onItemClicked: (index: number) => {
              this.currentIndex = index;
            }
          })
            .width('80%');
          Tabs({ index: this.currentIndex }) {
            ForEach(this.tabList, (item: string) => {
              TabContent() {
                Text(item)
                  .fontSize(16);
              };
            });
          }
          .barHeight(0)
          .backgroundColor('#FFFFFF')
          .width('100%')
          .layoutWeight(1)
          .onChange((index: number) => {
            this.currentIndex = index;
            // 页面滑动时SegmentButton切换选中状态
            this.tabSelectedIndexes = [index];
          });
        }
        .width('100%')
        .margin({ top: 16 })
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Start);
      }
    }
    ```

    效果图如下所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/LwnqO1z_Sg6dzBkNV60uww/zh-cn_image_0000002680323059.png "点击放大")
  + 方案二：使用自定义页签实现。

    设置单个页签的宽度在(页签宽度/页签数-padding值\*页签数，页签宽度/页签数)之间。参考代码如下所示：

    ```ts
    @Entry
    @Component
    struct CapsuleTwo {
      tabList: string[] = ['备忘', '待办'];
      tabbarWidth: number = 200;
      tabbarPadding: number = 2;
      @State currentIndex: number = 0;

      @Builder
      tabBuilder(index: number, name: string) {
        Column() {
          Text(name)
            .width(this.tabbarWidth / 2 -
              this.tabbarPadding * 2) // 设置宽度在(tabBar宽度/tabBar个数-padding值*tabBar个数，tabBar宽度/tabBar个数)之间
            .height('36vp')
            .textAlign(TextAlign.Center)
            .textVerticalAlign(TextVerticalAlign.CENTER)
            .fontColor(this.currentIndex === index ? '#e6000000' : '#99000000')
            .fontSize(14)
            .fontWeight(this.currentIndex === index ? 500 : 400)
            .lineHeight(40)
            .backgroundColor(this.currentIndex === index ? Color.White : '#00000000')
            .borderRadius('50vp');
        }
        .backgroundColor('#0d000000')
        .borderRadius({
          topLeft: index === 0 ? 50 : 0,
          bottomLeft: index === 0 ? 50 : 0,
          topRight: index === this.tabList.length - 1 ? 50 : 0,
          bottomRight: index === this.tabList.length - 1 ? 50 : 0
        })
        .margin({ top: 5 })
        .padding(this.tabbarPadding);
      }

      build() {
        Column() {
          Tabs() {
            ForEach(this.tabList, (item: string, index: number) => {
              TabContent() {
                Text(item)
                  .fontSize(16);
              }
              .backgroundColor('#FFFFFF')
              .tabBar(this.tabBuilder(index, item));
            });
          }
          .barWidth(this.tabbarWidth)
          .width('100%')
          .height('100%')
          .onChange((index: number) => {
            this.currentIndex = index;
          });
        };
      }
    }
    ```

    效果图如下所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/z-UH_7hrSQef-4foAr6iuQ/zh-cn_image_0000002650243726.png "点击放大")
* **场景四：实现页签栏和内容区重叠，并启用毛玻璃效果。**

  通过设置Tabs的barOverlap为true，并设置barBackgroundBlurStyle为BlurStyle.Thin，实现页签栏和内容区的重叠及毛玻璃效果。设置底部组件的padding值大于TabBar的高度防止遮挡。参考代码如下所示：

  ```ts
  @Entry
  @Component
  struct BarOverlapPage {
    tabList: string[] = ['页签1', '页签2'];
    contentList: string[] = ['区域1', '区域2', '区域3', '区域4'];
    listSpace: number = 16;

    @Builder
    tabContentBuilder() {
      List({ space: this.listSpace }) {
        ForEach(this.contentList, (item: string, index: number) => {
          ListItem() {
            Text(item)
              .width('80%')
              .height(500)
              .fontSize(16)
              .textAlign(TextAlign.Center)
              .backgroundColor('#26000000');
          }
          // 设置底部组件的padding值大于tabBar的高度
          .padding({ bottom: index === this.contentList.length - 1 ? 56 + this.listSpace : 0 });
        });
      }
      .width('100%')
      .height('100%')
      .lanes(2)
      .alignListItem(ListItemAlign.Center);
    }

    build() {
      Column() {
        Tabs({ barPosition: BarPosition.End }) {
          ForEach(this.tabList, (item: string) => {
            TabContent() {
              this.tabContentBuilder();
            }
            .tabBar(item);
          });
        }
        .barOverlap(true) // 开启背景模糊
        .barBackgroundBlurStyle(BlurStyle.Thin);
      }
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .height('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }
  ```

  效果图如下所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/wYopQ8vnTLmg2u1LGiavOA/zh-cn_image_0000002680163711.png "点击放大")
* **场景五：实现悬浮式、两端留空的Tab栏样式。**
  + 方案一：使用自定义组件实现。

    通过自定义组件实现，使用Stack容器将Tabs与自定义页签堆叠，实现悬浮式、两端留空的Tab栏样式，参考代码如下所示：

    ```ts
    interface tabInterface {
      text: string;
      icon: Resource;
    }

    @Entry
    @Component
    struct SuspensionPage {
      // 图片资源开发者可根据自身需求替换成所需资源
      tabList: tabInterface[] = [
        { text: '内容1', icon: $r('app.media.heart') },
        { text: '内容2', icon: $r('app.media.clock') },
        { text: '内容3', icon: $r('app.media.rectangle_on_rectangle') },
        { text: '内容4', icon: $r('app.media.person_2') }
      ];
      private controller: TabsController = new TabsController();
      @State currentIndex: number = 0;

      @Builder
      myTabBar() {
        Row() {
          Row() {
            ForEach(this.tabList, (item: tabInterface, index: number) => {
              Column() {
                Image(item.icon)
                  .width(50)
                  .aspectRatio(1)
                  .padding(8)
                  .backgroundColor(this.currentIndex === index ? '#26000000' : '#f1f3f5')
                  .borderRadius(12);
              }
              .onClick(() => {
                this.controller.changeIndex(index);
                this.currentIndex = index;
              })
              .alignItems(HorizontalAlign.Center)
              .justifyContent(FlexAlign.Center)
              .width(50)
              .height(50);
            });
          }
          .height(70)
          .width('90%')
          .justifyContent(FlexAlign.SpaceAround)
          .backgroundColor('#f1f3f5')
          .borderRadius(18);
        }
        .justifyContent(FlexAlign.Center)
        .height('50')
        .width('100%')
        .margin({ bottom: 20 });
      }

      build() {
        Column() {
          Stack({ alignContent: Alignment.BottomStart }) {
            Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
              ForEach(this.tabList, (item: tabInterface) => {
                TabContent() {
                  Column() {
                    Text(item.text)
                      .fontSize(20);
                  }
                  .justifyContent(FlexAlign.Center)
                  .height('100%')
                  .width('100%');
                }
                .backgroundColor('#ffffff');
              });
            }
            .barHeight(0)
            .animationDuration(200)
            .onChange((index: number) => {
              this.currentIndex = index;
            });
            // 页签
            this.myTabBar();
          }
          .width('100%');
        }
        .height('100%');
      }
    }
    ```
  + 方案二：使用HdsTabs实现。

    从API23开始，HdsTabs新增支持设置页签栏的悬浮样式。解决方案：参考[页签栏的悬浮样式](../harmonyos-guides/ui-design-hds-tabs-bar-floating.md)。

    效果图如下所示：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/fL6vQGfBS9yiJUbrvYdfog/zh-cn_image_0000002680163987.png "点击放大")
* **场景六：处理页签数较多时的TabBar的样式。**

  通过设置barMode为BarMode.Scrollable，当标签数量较多或内容超出屏幕宽度时，用户可以通过滑动来切换标签。解决方案：参考[示例2（设置Scrollable模式下的TabBar的布局样式）](../harmonyos-references/ts-container-tabs.md#示例2设置scrollable模式下的tabbar的布局样式)。
* **场景七：在页签被选中时使页签超出TabBar区域显示。**

  通过barModifier设置TabBar的clip属性，实现页签被选中时超出TabBar区域显示的效果。解决方案：参考[示例15（页签超出TabBar区域显示）](../harmonyos-references/ts-container-tabs.md#示例15页签超出tabbar区域显示)。

## 常见FAQ

Q：如何在标签页中嵌入一个动图图标？

A：通过自定义TabBar实现，在CustomBuilder中提供支持动图的gif。

Q：TabBar高度的默认值是多少？

A：CustomBuilder设置自定义样式的TabBar且vertical属性为false时，默认值为56vp。开发者可参考[barHeight](../harmonyos-references/ts-container-tabs.md#barheight20)。

Q：如何实现悬浮式导航栏并保证对低版本API的兼容性？

A：建议将悬浮效果和页面切换解耦，不要绑定在同一个高版本组件上。高版本有UIDesignKit时优先使用HdsTabs/HdsNavigation；需要兼容低版本时，使用[Tabs](../harmonyos-references/ts-container-tabs.md)负责内容切换，用[Stack](../harmonyos-references/ts-container-stack.md)额外盖一层自定义底部导航栏，避免调用不存在的高版本属性导致编译或运行异常。页面内容底部预留padding，避免被悬浮栏遮挡。
