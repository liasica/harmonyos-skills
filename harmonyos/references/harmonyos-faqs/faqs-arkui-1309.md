---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1309
title: 如何实现支持滑动调节护眼强弱的护眼模式
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现支持滑动调节护眼强弱的护眼模式
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:01+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:a64fd7cac7574bddf43258ad4587429abee5a1e012eaf8993e5c23887b39a408
---

## 问题现象

在多数场景下应用需要自行设计护眼模式，目前是否有对应的方法实现护眼的功能？

## 背景知识

* 通过[ArkUI支持ARGB字符串设置背景色](../harmonyos-references/ts-types.md#resourcecolor)的特性，可方便快捷设置背景色透明度。
* 通过[Slider滑动条组件](../harmonyos-references/ts-basic-components-slider.md#示例2设置滑动条样式)，允许用户通过滑动条，滑动调节护眼模式程度。
* 结合ArkUI的[触摸手势透传](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)特性，可以保障位于蒙层下方的组件，正常监听触摸手势。
* 若通过[Navigation](../harmonyos-references/ts-basic-components-navigation.md)路由的方式实现页面切换时，则可以通过其特殊的父子组件关系，将护眼的蒙层组件覆盖于Navigation组件上，实现所有[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)页面的护眼模式。

## 解决方案

* **场景一：阅读页面等单个页面的护眼方式。**
  1. 使用Slider组件实现滑动调节。
  2. 在页面上覆盖Canvas，设置Canvas背景色，并设置透传触摸事件。此处任意组件均可代替Canvas组件，无强制要求，主要实现的是护眼蒙层的颜色变化。
  3. 通过获取Slider值，调整Canvas背景色透明度，实现当前页面动态护眼调整。

     ```screen
     const RED_PART_SINGLE = 245;
     const YELLOW_PART_SINGLE = 222;
     const BLUE_PART_SINGLE = 73;

     @Entry
     @Component
     struct SinglePage {
       @State transparencyVal: number = 0; // 默认值(0-0.1)
       @State filterColor: string = '#D2691E'; // 动态计算
       @State txt: string = '应用内容区域';

       build() {
         RelativeContainer() {
           // 主内容区域
           Column() {
             // 这里放置你的UI组件
             this.contentTxt();
             // 色温调节滑块
             Slider({
               value: 0,
               min: 0,
               max: 0.3,
               step: 0.01
             })
               .onChange((value) => {
                 this.transparencyVal = value;
                 this.filterColor =
                   `rgba(${RED_PART_SINGLE}, ${YELLOW_PART_SINGLE}, ${BLUE_PART_SINGLE}, ${this.transparencyVal.toFixed(2)})`;
               })
               .width('80%')
               .margin(20);
           }.margin({ top: 40 })
           .width('100%')
           .height('80%')
           .backgroundColor('#FFFFFF');

           // 色温滤镜层(覆盖整个屏幕)
           Canvas()
             .width('100%')
             .height('100%')
             .backgroundColor(this.filterColor)
             .hitTestBehavior(HitTestMode.Transparent)
             .align(Alignment.Bottom)
             .position({ x: 0, y: 0 })
             .zIndex(999); // 确保在最顶层
         }
         .onAppear(() => {
           this.filterColor =
             `rgba(${RED_PART_SINGLE}, ${YELLOW_PART_SINGLE}, ${BLUE_PART_SINGLE}, ${this.transparencyVal.toFixed(2)})`;
         });
       }

       @Builder
       contentTxt() {
         // 这里放置你的UI组件
         Text(this.txt).fontSize(50).fontColor($r('sys.color.black')).onClick(() => {
           this.txt = '测试点击内容';
         });
       }
     }
     ```

     效果预览：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/r-VC69i3TLi8W_6_gB10fg/zh-cn_image_0000002628758922.gif "点击放大")

* **场景二：为整个应用设置护眼模式。**
  + 方案一：Navigation组件与护眼组件重叠。

    可以使用Navigation路由，将Canvas覆盖在Navigation上，可以实现所有页面都覆盖上护眼模式，且可以通过扩展安全区实现Canvas覆盖安全区。参考如下：

    OptionOneIndex.ets主页面：

    ```screen
    const RED_PART = 245;
    const YELLOW_PART = 222;
    const BLUE_PART = 73;

    @Entry
    @Component
    struct OptionOneIndex {
      transparencyVal: number = 0; // 默认值 (0-0.1)
      @State filterColor: string = '#D2691E'; // 动态计算
      txt: string = '应用内容区域';
      @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

      build() {
        RelativeContainer() {
          Navigation(this.pathStack) {
            // 主内容区域
            Column() {
              // 这里放置你的UI组件
              this.contentTxt();
              // 色温调节滑块
              Slider({
                value: 0,
                min: 0,
                max: 0.3,
                step: 0.01
              })
                .onChange((value) => {
                  this.transparencyVal = value;
                  this.filterColor = `rgba(${RED_PART}, ${YELLOW_PART}, ${BLUE_PART}, ${this.transparencyVal.toFixed(2)})`;
                })
                .width('80%')
                .margin(20);
            }.margin({ top: 40 })
            .width('100%')
            .height('80%')
            .backgroundColor('#FFFFFF');
          };

          // 色温滤镜层 (覆盖整个屏幕)
          Canvas()
            .width('100%')
            .height('100%')
            .backgroundColor(this.filterColor)
            .hitTestBehavior(HitTestMode.Transparent)
            .align(Alignment.Bottom)
            .position({ x: 0, y: 0 })
            .zIndex(999) // 确保在最顶层
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
        }
        .onAppear(() => {
          this.filterColor = `rgba(${RED_PART}, ${YELLOW_PART}, ${BLUE_PART}, ${this.transparencyVal.toFixed(2)})`;
        });
      }

      @Builder
      contentTxt() {
        // 这里放置你的UI组件
        Text(this.txt).fontSize(50).fontColor($r('sys.color.black'))
          .onClick(() => {
            this.pathStack.pushPathByName('OptionOneIndexTwo', '');
          });
      }
    }
    ```

    OptionOneIndexTwo.ets子页面：

    ```screen
    @Builder
    export function OptionOneIndexTwoBuilder() {
      OptionOneIndexTwo();
    }

    @Component
    struct OptionOneIndexTwo {
      build() {
        NavDestination() {
          Column() {
            Text('2');
          };
        };
      }
    }
    ```

    **说明** 

    该方案与下文方案二省略路由表配置步骤，Navigation路由表配置详见官方文档：[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)。
  + 方案二：Navigation设置[overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)浮层。

    Navigation路由下，给Navigation容器设置overlay浮层，并将浮层的宽高设置为屏幕宽高即可：

    OptionTwoIndex.ets主页面：

    ```screen
    import { display } from '@kit.ArkUI';

    const RED_PART_TWO = 245;
    const YELLOW_PART_TWO = 222;
    const BLUE_PART_TWO = 73;

    @Entry
    @Component
    struct OptionTwoIndex {
      transparencyVal: number = 0; // 默认值 (0-0.1)
      @State filterColor: string = '#D2691E'; // 动态计算
      txt: string = '应用内容区域';
      @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

      build() {
        RelativeContainer() {
          Navigation(this.pathStack) {
            // 主内容区域
            Column() {
              // 这里放置你的UI组件
              this.contentTxt();
              // 色温调节滑块
              Slider({
                value: 0,
                min: 0,
                max: 0.3,
                step: 0.01
              })
                .onChange((value) => {
                  this.transparencyVal = value;
                  this.filterColor =
                    `rgba(${RED_PART_TWO}, ${YELLOW_PART_TWO}, ${BLUE_PART_TWO}, ${this.transparencyVal.toFixed(2)})`;
                })
                .width('80%')
                .margin(20);
            }
            .margin({ top: 40 })
            .width('100%')
            .height('80%')
            .backgroundColor('#FFFFFF');
          }
          .overlay(this.OverlayNode(), { align: Alignment.Center }); // 设置浮层
        }
        .onAppear(() => {
          this.filterColor =
            `rgba(${RED_PART_TWO}, ${YELLOW_PART_TWO}, ${BLUE_PART_TWO}, ${this.transparencyVal.toFixed(2)})`;
        });
      }

      // 浮层充当遮罩
      @Builder
      OverlayNode() {
        Column() {
        }
        .width(this.getUIContext().px2vp(display.getDefaultDisplaySync().width))
        .height(this.getUIContext().px2vp(display.getDefaultDisplaySync().height))
        .backgroundColor(this.filterColor)
        .hitTestBehavior(HitTestMode.Transparent); // 点击穿透
      }

      @Builder
      contentTxt() {
        // 这里放置你的UI组件
        Text(this.txt).fontSize(50).fontColor($r('sys.color.black'))
          .onClick(() => {
            this.pathStack.pushPathByName('OptionTwoIndexTwo', '');
          });
      }
    }
    ```

    OptionTwoIndexTwo.ets子页面：

    ```screen
    @Builder
    export function OptionTwoIndexTwoBuilder() {
      OptionTwoIndexTwo();
    }

    @Component
    struct OptionTwoIndexTwo {
      build() {
        NavDestination() {
          Column() {
            Text('2');
          };
        };
      }
    }
    ```

    效果预览：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/X3UNiThdRfWFirML1i-OBA/zh-cn_image_0000002658958251.gif "点击放大")

## 总结

通过构造护眼蒙层组件，根据滑块自由设定蒙层透明度，实现可滑动调节的效果。
