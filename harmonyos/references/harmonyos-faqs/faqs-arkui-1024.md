---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1024
title: TabBar常见角标场景实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TabBar常见角标场景实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:df86b25fd97e9f8538f88f5af940e8e013569fd3eb64f3490e7a7df458eea26f
---

## 问题现象

场景一：如何实现不同类型的角标（如：红点型、字符型、数字型）？

场景二：如何实现点击TabBar后角标自动消失功能？

场景三：如何实现角标数据更新功能？

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [tabBar](../harmonyos-references/ts-container-tabcontent.md#tabbar)：用于在不同内容视图（TabContent）之间快速切换。
* [Badge](../harmonyos-references/ts-container-badge.md)：在目标组件（如图标、文本）的指定位置显示标记，用于提醒用户关注新消息、状态变更或特殊标识。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件是否可见。
* [SubTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#subtabbarstyle9)：子页签样式。打开后在切换页签时会播放跳转动画。
* [@ObservedV2装饰器和@Trace装饰器](../harmonyos-guides/arkts-new-observedv2-and-trace.md)：具有直接对嵌套类对象属性变化观测的能力。
* [update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)：用于更新WrappedBuilder对象封装的builder函数参数。

## 解决方案

TabBar角标的各种样式、消失功能、更新数据功能实现方案如下：

| 实现角标方法 | 实现场景 | | 实现方式 | 适用场景 |
| --- | --- | --- | --- | --- |
| Badge组件（直接使用组件，操作简单） | 场景一：不同类型的角标。 | 红点型 | 设置Badge组件的value属性为空，表示红点型角标。 | 引导用户发现和使用新功能，如：当应用新增了某个功能或进行了更新，可以在相关图标上显示红点。 |
| 字符型 | 设置Badge组件的value属性，表示字符型角标的具体内容。 | 自定义字符内容，提示用户当前状态，如：在某些功能或内容的状态发生变化时，可以在图标上显示字符型角标，例如“新”、“热”、“急”等信息。 |
| 数字型 | 设置Badge组件的Count属性，表示数字型角标的具体数字。 | 常用于消息或购物车场景，在消息图标或通知图标上显示未读消息的数量，帮助用户了解有多少新的消息或通知需要处理。 |
| 场景二：实现点击清除角标的功能。 | / | 方案一：使用条件渲染实现点击清除角标的功能。 | 当角标的内容是动态生成的，且需要根据某些条件来决定是否显示时，使用条件渲染更为合适。但可能会导致代码稍微复杂一些。 |
| 方案二：使用visibility属性控制点击清除角标的功能。 | 适用于简单的显示/隐藏需求，实现简单且容易添加动画效果。 |
| 方案三：使用@ObservedV2和@Trace对数据模型直接观测。 | 适用于数据驱动和复杂状态管理，实现细粒度的观测和追踪，适合大型应用。 |
| 场景三：角标数据更新功能。 | / | 方案一：使用update方法对角标数据进行更新。 | 当应用的状态管理相对简单，不需要复杂的依赖和副作用管理时，可以使用update方法进行数据更新，但手动管理状态的更新和同步，可能会容易出错。 |
| 方案二：使用@ObservedV2和@Trace对数据模型直接观测。 | 当应用的状态管理复杂，需要细粒度的依赖和副作用管理时可以使用@ObservedV2和@Trace对数据模型直接观测，但是对于简单的状态管理，可能会显得过于复杂。 |
| 自定义组件（布局自由度高，可实现复杂样式，但实现较为复杂） | 场景一：不同类型的角标。 | 红点型 | 利用Stack组件，自行绘制角标样式。 | 使用场景同上。 |
| 字符型 |
| 数字型 |
| 场景二：实现点击清除角标的功能。 | / | 实现方案同Badge组件的场景二。 |
| 场景三：角标数据更新功能。 | / | 实现方案同Badge组件的场景三。 |

* 使用Badge组件：
  + **场景一**：实现红点型、字符型、数字型的角标。

    不同类型的角标可通过设置Badge组件的属性来实现。

    1. Badge组件实现红点类型角标。

       ```ts
       // 定义单个Tab的数据结构
       interface DotsBadgeItem {
         id: string; // 唯一标识符
         targetIndex: number; // 每个页签所属的index
         title: string; // tabBar标题
         img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
         content: string; // tabBar对应的内容（可根据实际需求扩展）
       }

       @Entry
       @Component
       struct DotsBadge {
         controller: TabsController = new TabsController();
         // 模拟后端返回的数据
         private tabList: DotsBadgeItem[] = [
           {
             id: '0',
             targetIndex: 0,
             title: '首页',
             content: '首页内容',
             img: $r('app.media.house_fill') // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
           },
           {
             id: '1',
             targetIndex: 1,
             title: '消息',
             content: '消息内容',
             img: $r('app.media.ellipsis_message') // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
           },
           {
             id: '2',
             targetIndex: 2,
             title: '相册',
             content: '相册内容',
             img: $r('app.media.rectangle_on_rectangle') // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
           }
         ];
         // 控制TabContent页签
         @State currentIndex: number = 0;

         // 红点型
         @Builder
         dotsBadge(params: DotsBadgeItem) {
           Column() {
             Badge({
               value: '',
               position: { x: 26 },
               style: { badgeSize: 6, badgeColor: '#FA2A2D' }
             }) {
               Image(params.img)
                 .width(32)
                 .height(32)
                 .fillColor(this.currentIndex === params.targetIndex ? '#0A59F7' : Color.Black);
             };

             Text(params.title)
               .width('100%')
               .textAlign(TextAlign.Center)
               .fontSize(20)
               .margin(5);
           }
           .width('100%')
           .height('100%')
           .justifyContent(FlexAlign.Center);
         }

         build() {
           Column() {
             Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
               // 循环生成TabContent,标题由每个item的title决定
               ForEach(this.tabList, (item: DotsBadgeItem) => {
                 TabContent() {
                   // 每个Tab的内容,可以根据需求替换
                   Text(item.content)
                     .layoutWeight(1)
                     .padding(16)
                     .layoutWeight(1)
                     .textAlign(TextAlign.Center);
                 }
                 .tabBar(this.dotsBadge(item));
               }, (item: DotsBadgeItem) => item.id);
             }
             .animationDuration(0)
             .barMode(BarMode.Fixed)
             .onChange((index: number) => {
               this.currentIndex = index;
             });
           }
           .width('100%')
           .height('100%');
         }
       }
       ```

       效果预览：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/M0FNKhQeS6ih1eLeL0JMVw/zh-cn_image_0000002628564716.png "点击放大")
    2. Badge组件实现字符类型角标。

       ```ts
       // 定义单个Tab的数据结构
       interface StringBadgeItem {
         id: string; // 唯一标识符
         targetIndex: number; // 每个页签所属的index
         title: string; // tabBar标题
         img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
         content: string; // tabBar对应的内容（可根据实际需求扩展）
       }

       @Entry
       @Component
       struct StringBadge {
         controller: TabsController = new TabsController();
         // 模拟后端返回的数据
         private tabList: StringBadgeItem[] = [
           {
             id: '0',
             targetIndex: 0,
             title: '首页',
             content: '首页内容',
             img: $r('app.media.house_fill') // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
           },
           {
             id: '1',
             targetIndex: 1,
             title: '消息',
             content: '消息内容',
             img: $r('app.media.ellipsis_message') // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
           },
           {
             id: '2',
             targetIndex: 2,
             title: '相册',
             content: '相册内容',
             img: $r('app.media.rectangle_on_rectangle') // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
           }
         ];
         // 控制TabContent页签
         @State currentIndex: number = 0;

         // 红点型
         @Builder
         dotsBadge(params: StringBadgeItem) {
           Column() {
             Badge({
               value: 'New',
               position: { x: 26 },
               style: { badgeSize: 16, badgeColor: '#FA2A2D' }
             }) {
               Image(params.img)
                 .width(32)
                 .height(32)
                 .fillColor(this.currentIndex === params.targetIndex ? '#0A59F7' : Color.Black);
             };

             Text(params.title)
               .width('100%')
               .textAlign(TextAlign.Center)
               .fontSize(20)
               .margin(5);
           }
           .width('100%')
           .height('100%')
           .justifyContent(FlexAlign.Center);
         }

         build() {
           Column() {
             Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
               // 循环生成TabContent,标题由每个item的title决定
               ForEach(this.tabList, (item: StringBadgeItem) => {
                 TabContent() {
                   // 每个Tab的内容,可以根据需求替换
                   Text(item.content)
                     .layoutWeight(1)
                     .padding(16)
                     .layoutWeight(1)
                     .textAlign(TextAlign.Center);
                 }
                 .tabBar(this.dotsBadge(item));
               }, (item: StringBadgeItem) => item.id);
             }
             .animationDuration(0)
             .barMode(BarMode.Fixed)
             .onChange((index: number) => {
               this.currentIndex = index;
             });
           }
           .width('100%')
           .height('100%');
         }
       }
       ```

       效果预览：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/2R6fyfmUQ9O5-ijxokLXtg/zh-cn_image_0000002658924021.png "点击放大")
    3. Badge组件实现数字类型角标。

       ```ts
       // 定义单个Tab的数据结构
       interface NumberBadgeItem {
         id: string; // 唯一标识符
         targetIndex: number; // 每个页签所属的index
         title: string; // tabBar标题
         img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
         content: string; // tabBar对应的内容（可根据实际需求扩展）
       }

       @Entry
       @Component
       struct NumberBadge {
         controller: TabsController = new TabsController();
         // 模拟后端返回的数据
         private tabList: NumberBadgeItem[] = [
           {
             id: '0',
             targetIndex: 0,
             title: '首页',
             content: '首页内容',
             img: $r('app.media.house_fill') // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
           },
           {
             id: '1',
             targetIndex: 1,
             title: '消息',
             content: '消息内容',
             img: $r('app.media.ellipsis_message') // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
           },
           {
             id: '2',
             targetIndex: 2,
             title: '相册',
             content: '相册内容',
             img: $r('app.media.rectangle_on_rectangle') // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
           }
         ];
         // 控制TabContent页签
         @State currentIndex: number = 0;

         // 红点型
         @Builder
         dotsBadge(params: NumberBadgeItem) {
           Column() {
             Badge({
               count: 1,
               position: { x: 26 },
               style: { badgeSize: 16, badgeColor: '#FA2A2D' }
             }) {
               Image(params.img)
                 .width(32)
                 .height(32)
                 .fillColor(this.currentIndex === params.targetIndex ? '#0A59F7' : Color.Black);
             };

             Text(params.title)
               .width('100%')
               .textAlign(TextAlign.Center)
               .fontSize(20)
               .margin(5);
           }
           .width('100%')
           .height('100%')
           .justifyContent(FlexAlign.Center);
         }

         build() {
           Column() {
             Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
               // 循环生成TabContent,标题由每个item的title决定
               ForEach(this.tabList, (item: NumberBadgeItem) => {
                 TabContent() {
                   // 每个Tab的内容,可以根据需求替换
                   Text(item.content)
                     .layoutWeight(1)
                     .padding(16)
                     .layoutWeight(1)
                     .textAlign(TextAlign.Center);
                 }
                 .tabBar(this.dotsBadge(item));
               }, (item: NumberBadgeItem) => item.id);
             }
             .animationDuration(0)
             .barMode(BarMode.Fixed)
             .onChange((index: number) => {
               this.currentIndex = index;
             });
           }
           .width('100%')
           .height('100%');
         }
       }
       ```

       效果预览：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/zQRkOuRHR6qSDDjYqYx8FA/zh-cn_image_0000002628404812.png "点击放大")
  + **场景二**：实现点击清除角标的功能。

    上述三种类型的角标均可通过点击清除，接下来将以红点型角标为例，详细介绍其实现方式。

    - **方案一**：对角标内容条件渲染控制。
      1. 定义数据模型，其中包含控制渲染角标的变量。
      2. 创建角标时，对其内容进行条件渲染控制。
      3. 新增清除角标的方法。

      ```ts
      // 定义单个Tab的数据结构
      class DotsBadgeDisappearItem {
        id: string; // 唯一标识符
        targetIndex: number; // 每个页签所属的index
        title: string; // tabBar标题
        content: string; // tabBar对应的内容（可根据实际需求扩展）
        img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
        badgeVisible: boolean; // 控制渲染角标

        constructor(id: string, targetIndex: number, title: string, content: string, img: Resource, badgeVisible: boolean) {
          this.id = id;
          this.targetIndex = targetIndex;
          this.title = title;
          this.content = content;
          this.img = img;
          this.badgeVisible = badgeVisible;
        }
      }

      @Entry
      @Component
      struct DotsBadgeDisappear {
        controller: TabsController = new TabsController();
        // 控制TabContent页签
        @State currentIndex: number = 0;
        // 模拟后端返回的数据
        @State tabList: DotsBadgeDisappearItem[] = [
        // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem('0', 0, '首页', '首页的内容', $r('app.media.house_fill'), true),
          // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem('1', 1, '相册', '相册的内容', $r('app.media.rectangle_on_rectangle'), true),
          // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem('2', 2, '消息', '消息的内容', $r('app.media.ellipsis_message'), true)
        ];

        // 红点型
        @Builder
        dotsBadge(params: DotsBadgeDisappearItem, index: number) {
          Column() {
            if (this.tabList[index].badgeVisible) {
              Badge({
                value: '',
                position: { x: 72 },
                style: { badgeSize: 16, badgeColor: '#FA2A2D' }
              }) {
                Text('')
                  .width(0)
                  .height(0);
              };
            }
            Image(params.img)
              .width(32)
              .height(32)
              .fillColor(this.currentIndex === params.targetIndex ? '#0A59F7' : Color.Black);
            Text(params.title)
              .width('100%')
              .textAlign(TextAlign.Center)
              .fontSize(20)
              .margin(5);
          }
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center);
        }

        // 清除角标方法
        clearTips(index: number) {
          // 创建新数组
          const newList = this.tabList.map((item, i) =>
          new DotsBadgeDisappearItem(
            item.id,
            item.targetIndex,
            item.title,
            item.content,
            item.img,
            i === index ? false : item.badgeVisible
          ));
          // 强制更新数组
          this.tabList = newList;
        }

        build() {
          Column() {
            Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
              // 循环生成TabContent,标题由每个item的title决定
              ForEach(this.tabList, (item: DotsBadgeDisappearItem, index: number) => {
                TabContent() {
                  // 每个Tab的内容,可以根据需求替换
                  Text(item.content)
                    .layoutWeight(1)
                    .padding(16)
                    .layoutWeight(1)
                    .textAlign(TextAlign.Center);
                }
                .tabBar(this.dotsBadge(item, index));
              }, (item: DotsBadgeDisappearItem) => item.id);
            }
            .animationDuration(0)
            .barMode(BarMode.Fixed)
            .onChange((index: number) => {
              this.currentIndex = index;
              // 立即执行清除操作
              this.clearTips(index);
            });
          }
          .width('100%')
          .height('100%');
        }
      }
      ```
    - **方案二**：visibility属性控制。

      通过visibility通用属性控制Badge组件的显隐。

      ```ts
      // 定义单个Tab的数据结构
      class DotsBadgeDisappearItem2 {
        id: string; // 唯一标识符
        targetIndex: number; // 每个页签所属的index
        title: string; // tabBar标题
        content: string; // tabBar对应的内容（可根据实际需求扩展）
        img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
        badgeVisible: boolean; // 控制渲染角标

        constructor(id: string, targetIndex: number, title: string, content: string, img: Resource, badgeVisible: boolean) {
          this.id = id;
          this.targetIndex = targetIndex;
          this.title = title;
          this.content = content;
          this.img = img;
          this.badgeVisible = badgeVisible;
        }
      }

      @Entry
      @Component
      struct DotsBadgeDisappear2 {
        controller: TabsController = new TabsController();
        // 控制TabContent页签
        @State currentIndex: number = 0;
        // 模拟后端返回的数据
        @State tabList: DotsBadgeDisappearItem2[] = [
        // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem2('0', 0, '首页', '首页的内容', $r('app.media.house_fill'), true),
          // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem2('1', 1, '相册', '相册的内容', $r('app.media.rectangle_on_rectangle'), true),
          // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem2('2', 2, '消息', '消息的内容', $r('app.media.ellipsis_message'), true)
        ];

        // 红点型
        @Builder
        dotsBadge(params: DotsBadgeDisappearItem2, index: number) {
          Column() {
            Badge({
              value: '',
              position: { x: 72 },
              style: { badgeSize: 16, badgeColor: '#FA2A2D' }
            }) {
              Text('')
                .width(0)
                .height(0);
            }
            .visibility(this.tabList[index].badgeVisible ? Visibility.Visible : Visibility.None);
            Image(params.img)
              .width(32)
              .height(32)
              .fillColor(this.currentIndex === params.targetIndex ? '#0A59F7' : Color.Black);
            Text(params.title)
              .width('100%')
              .textAlign(TextAlign.Center)
              .fontSize(20)
              .margin(5);
          }
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center);
        }

        // 清除角标方法
        clearTips(index: number) {
          // 创建新数组
          const newList = this.tabList.map((item, i) =>
          new DotsBadgeDisappearItem2(
            item.id,
            item.targetIndex,
            item.title,
            item.content,
            item.img,
            i === index ? false : item.badgeVisible
          ));
          // 强制更新数组
          this.tabList = newList;
        }

        build() {
          Column() {
            Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
              // 循环生成TabContent,标题由每个item的title决定
              ForEach(this.tabList, (item: DotsBadgeDisappearItem2, index: number) => {
                TabContent() {
                  // 每个Tab的内容,可以根据需求替换
                  Text(item.content)
                    .layoutWeight(1)
                    .padding(16)
                    .layoutWeight(1)
                    .textAlign(TextAlign.Center);
                }
                .tabBar(this.dotsBadge(item, index));
              }, (item: DotsBadgeDisappearItem2) => item.id);
            }
            .animationDuration(0)
            .barMode(BarMode.Fixed)
            .onChange((index: number) => {
              this.currentIndex = index;
              // 立即执行清除操作
              this.clearTips(index);
            });
          }
          .width('100%')
          .height('100%');
        }
      }
      ```
    - **方案三**：使用@ObservedV2和@Trace对数据模型直接观测。

      数据模型中，对控制渲染角标的属性深度观测。

      ```ts
      // 定义单个Tab的数据结构
      @ObservedV2
      class DotsBadgeDisappearItem3 {
        id: string; // 唯一标识符
        targetIndex: number; // 每个页签所属的index
        title: string; // tabBar标题
        content: string; // tabBar对应的内容（可根据实际需求扩展）
        img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
        @Trace badgeVisible: boolean; // 控制渲染角标

        constructor(id: string, targetIndex: number, title: string, content: string, img: Resource, badgeVisible: boolean) {
          this.id = id;
          this.targetIndex = targetIndex;
          this.title = title;
          this.content = content;
          this.img = img;
          this.badgeVisible = badgeVisible;
        }
      }

      @Entry
      @ComponentV2
      struct DotsBadgeDisappear3 {
        controller: TabsController = new TabsController();
        // 控制TabContent页签
        @Local currentIndex: number = 0;
        // 模拟后端返回的数据
        @Local tabList: DotsBadgeDisappearItem3[] = [
        // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem3('0', 0, '首页', '首页的内容', $r('app.media.house_fill'), true),
          // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem3('1', 1, '相册', '相册的内容', $r('app.media.rectangle_on_rectangle'), true),
          // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
          new DotsBadgeDisappearItem3('2', 2, '消息', '消息的内容', $r('app.media.ellipsis_message'), true)
        ];

        // 红点型
        @Builder
        dotsBadge(params: DotsBadgeDisappearItem3) {
          Column() {
            Badge({
              value: '',
              position: { x: 72 },
              style: { badgeSize: 16, badgeColor: '#FA2A2D' }
            }) {
              Text('')
                .width(0)
                .height(0);
            }
            .visibility(params.badgeVisible ? Visibility.Visible : Visibility.None);
            Image(params.img)
              .width(32)
              .height(32)
              .fillColor(this.currentIndex === params.targetIndex ? '#0A59F7' : Color.Black);
            Text(params.title)
              .width('100%')
              .textAlign(TextAlign.Center)
              .fontSize(20)
              .margin(5);
          }
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center);
        }

        // 清除角标方法
        clearTips(index: number) {
          // 直接修改原对象属性
          this.tabList.forEach((item, i) =>
          new DotsBadgeDisappearItem3(
            item.id,
            item.targetIndex,
            item.title,
            item.content,
            item.img,
            item.badgeVisible = i === index ? false : item.badgeVisible
          ));
        }

        build() {
          Column() {
            Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
              // 循环生成TabContent,标题由每个item的title决定
              ForEach(this.tabList, (item: DotsBadgeDisappearItem3) => {
                TabContent() {
                  // 每个Tab的内容,可以根据需求替换
                  Text(item.content)
                    .layoutWeight(1)
                    .padding(16)
                    .layoutWeight(1)
                    .textAlign(TextAlign.Center);
                }
                .tabBar(this.dotsBadge(item));
              }, (item: DotsBadgeDisappearItem3) => item.id);
            }
            .animationDuration(0)
            .barMode(BarMode.Fixed)
            .onChange((index: number) => {
              this.currentIndex = index;
              // 立即执行清除操作
              this.clearTips(index);
            });
          }
          .width('100%')
          .height('100%');
        }
      }
      ```

      上述三种方案效果预览：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5QjC9o7lT-Kgw71Oms4xfg/zh-cn_image_0000002658804081.png "点击放大")
  + **场景三**：实现角标数据更新功能。
    - **方案一**：使用update方法进行更新。

      TabBar样式可以通过SubTabBarStyle等方式创建，Tabs页面切换后，执行清除角标的操作，使用[update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)方法更新WrappedBuilder对象封装的builder函数参数。

      ```ts
      import { ComponentContent } from '@kit.ArkUI';

      class UpdateNumberBadgeItem {
        id: string; // 唯一标识符
        targetIndex: number; // 每个页签所属的index
        title: string; // tabBar标题
        img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
        badgeValue: number; // 角标值

        constructor(id: string, targetIndex: number, title: string, img: Resource, badgeValue: number) {
          this.id = id;
          this.targetIndex = targetIndex;
          this.title = title;
          this.img = img;
          this.badgeValue = badgeValue;
        }
      }

      // 数字型
      @Builder
      function numberBadge(params: UpdateNumberBadgeItem) {
        Column() {
          Badge({
            count: params.badgeValue,
            position: BadgePosition.RightTop,
            style: { badgeSize: 16, badgeColor: '#FA2A2D' }
          }) {
            Image(params.img)
              .width(32)
              .height(32);
          }
          .width(32)
          .height(32)
          .margin({ bottom: 4 });

          Text(params.title)
            .width('100%')
            .textAlign(TextAlign.Center)
            .fontSize(20)
            .margin(5);
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center);
      }

      @Entry
      @Component
      struct UpdateNumberBadge1 {
        context: UIContext = this.getUIContext();
        controller: TabsController = new TabsController();
        // 模拟后端返回的数据
        private tabList: UpdateNumberBadgeItem[] = [
        // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
          new UpdateNumberBadgeItem('0', 0, '首页', $r('app.media.house_fill'), 0),
          // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
          new UpdateNumberBadgeItem('1', 1, '相册', $r('app.media.rectangle_on_rectangle'), 0),
          // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
          new UpdateNumberBadgeItem('2', 2, '消息', $r('app.media.ellipsis_message'), 1)
        ];
        // 红点型
        numberTabBar1: ComponentContent<UpdateNumberBadgeItem> =
          new ComponentContent<UpdateNumberBadgeItem>(this.context, wrapBuilder<[UpdateNumberBadgeItem]>(numberBadge),
            this.tabList[0]);
        numberTabBar2: ComponentContent<UpdateNumberBadgeItem> =
          new ComponentContent<UpdateNumberBadgeItem>(this.context, wrapBuilder<[UpdateNumberBadgeItem]>(numberBadge),
            this.tabList[1]);
        numberTabBar3: ComponentContent<UpdateNumberBadgeItem> =
          new ComponentContent<UpdateNumberBadgeItem>(this.context, wrapBuilder<[UpdateNumberBadgeItem]>(numberBadge),
            this.tabList[2]);
        // 控制TabContent页签
        @State currentIndex: number = 0;

        // 模拟后端数据更新
        updateBadgeValue(action: string, item: UpdateNumberBadgeItem) {
          switch (action) {
            case 'reset':
              item.badgeValue = 0;
              break;
            case 'increment':
              item.badgeValue += 10;
              break;
            case 'decrement':
              if (item.badgeValue - 10 < 0) {
                item.badgeValue = 0;
              } else {
                item.badgeValue -= 10;
              }
              break;
            case 'set99':
              item.badgeValue = 99;
              break;
            default:
              console.info('Succeeded in changing badgeValue.');
          }
          // 更新WrappedBuilder对象封装的builder函数参数
          this.numberTabBar3.update(this.tabList[2]);
        }

        build() {
          Column() {
            Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
              TabContent() {
                Column()
                  .margin({ top: 16 })
                  .width('100%')
                  .height('100%');
              }
              .tabBar(new SubTabBarStyle(this.numberTabBar1)
                .indicator({ marginTop: 12, width: 32 })
              );

              TabContent() {
                Column()
                  .width('100%')
                  .height('100%');
              }
              .tabBar(new SubTabBarStyle(this.numberTabBar2)
                .indicator({ marginTop: 12, width: 32 })
              );

              TabContent() {
                Column({ space: 16 }) {
                  Button('消息99')
                    .padding({ bottom: 16, top: 16 })
                    .width('60%')
                    .height('50vp')
                    .onClick(() => {
                      this.updateBadgeValue('set99', this.tabList[2]);
                    });
                  Button('消息归零')
                    .padding({ bottom: 16, top: 16 })
                    .width('60%')
                    .height('50vp')
                    .onClick(() => {
                      this.updateBadgeValue('reset', this.tabList[2]);
                    });
                  Button('消息增加10')
                    .padding({ bottom: 16, top: 16 })
                    .width('60%')
                    .height('50vp')
                    .onClick(() => {
                      this.updateBadgeValue('increment', this.tabList[2]);
                    });
                  Button('消息减少10')
                    .padding({ bottom: 16, top: 16 })
                    .width('60%')
                    .height('50vp')
                    .onClick(() => {
                      this.updateBadgeValue('decrement', this.tabList[2]);
                    });
                }
                .width('100%')
                .height('100%')
                .margin({ top: 50 });
              }
              .tabBar(new SubTabBarStyle(this.numberTabBar3)
                .indicator({ marginTop: 12, width: 32 })
              );
            }
            .barHeight(100)
            .vertical(false)
            .barMode(BarMode.Fixed)
            .animationMode(AnimationMode.NO_ANIMATION)
            .onChange((index: number) => {
              this.currentIndex = index;
            });
          }
          .width('100%')
          .height('100%');
        }
      }
      ```

      效果预览：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/VsjBjmWqQuGQDEew1qi9RQ/zh-cn_image_0000002628564718.png "点击放大")
    - **方案二**：使用@ObservedV2和@Trace对数据模型直接观测。

      该方案与场景二方案三的实现方式类似，不再赘述。
* 自定义角标：
  + **场景一**：实现红点型、字符型、数字型的角标。

    三种类型角标实现方式类似，下文将以红点型角标举例。

    ```ts
    // 定义单个Tab的数据结构
    interface DotsCustomItem {
      id: string; // 唯一标识符
      targetIndex: number; // 每个页签所属的index
      title: string; // tabBar标题
      img: Resource; // icon图片仅供示例，开发者可以根据实际需求替换
      content: string; // tabBar对应的内容（可根据实际需求扩展）
    }

    @Entry
    @Component
    struct DotsCustom {
      controller: TabsController = new TabsController();
      // 控制TabContent页签
      @State currentIndex: number = 0;
      // 模拟后端返回的数据
      private tabList: DotsCustomItem[] = [
        {
          id: '0',
          targetIndex: 0,
          title: '首页',
          content: '首页内容',
          img: $r('app.media.house_fill') // 图片资源$r('app.media.house_fill')仅供示例，开发者可根据需求替换
        },
        {
          id: '1',
          targetIndex: 1,
          title: '消息',
          content: '消息内容',
          img: $r('app.media.ellipsis_message') // 图片资源$r('app.media.ellipsis_message')仅供示例，开发者可根据需求替换
        },
        {
          id: '2',
          targetIndex: 2,
          title: '相册',
          content: '相册内容',
          img: $r('app.media.rectangle_on_rectangle') // 图片资源$r('app.media.rectangle_on_rectangle')仅供示例，开发者可根据需求替换
        }
      ];

      // 红点型
      @Builder
      dotsBadge(item: DotsCustomItem) {
        Stack() {
          Column({ space: 10 }) {
            Image(item.img)
              .size({ height: 26, width: 26 })
              .fillColor(this.currentIndex === item.targetIndex ? '#0A59F7' : Color.Black);
            Text(item.title)
              .fontSize(16)
              .fontColor(this.currentIndex === item.targetIndex ? '#0A59F7' : Color.Black);
          }
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center);

          // 小红点
          Text('')
            .textAlign(TextAlign.Center)
            .fontSize(12)
            .width(8)
            .height(8)
            .borderRadius(4)
            .backgroundColor('#FA2A2D')
            .position({ x: 70, y: 0 });
        }
        .key(item.id.toString());
      }

      build() {
        Column() {
          Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
            // 循环生成TabContent,标题由每个item的title决定
            ForEach(this.tabList, (item: DotsCustomItem) => {
              TabContent() {
                // 每个Tab的内容,可以根据需求替换
                Text(item.content)
                  .layoutWeight(1)
                  .padding(16)
                  .layoutWeight(1)
                  .textAlign(TextAlign.Center);
              }
              .tabBar(this.dotsBadge(item));
            }, (item: DotsCustomItem) => item.id);
          }
          .animationDuration(0)
          .barMode(BarMode.Fixed)
          .onChange((index: number) => {
            this.currentIndex = index;
          });
        }
        .width('100%')
        .height('100%');
      }
    }
    ```

    效果预览：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/HPTWNwFVQNGK_ziwg772VQ/zh-cn_image_0000002658924025.png "点击放大")
  + 场景二、三：实现角标清除与更新。

    自定义角标的清除与数据更新功能，实现方式与Badge组件类似，此处不再赘述。
