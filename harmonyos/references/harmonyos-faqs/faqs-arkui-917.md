---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-917
title: 如何实现自定义Tabs模拟浏览器页签增加删除能力
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现自定义Tabs模拟浏览器页签增加删除能力
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8e6ba74151840e49c283a4933c8e3d219800ee24afc896fe2feee8dc57c09f90
---

## 问题现象

在使用Tabs组件提供的页签进行内容视图切换时，需要使用增加或删除页签的能力，Tabs组件本身并没有提供相关能力，应该如何实现？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/rFArKA-SR7KJhubC592nfA/zh-cn_image_0000002658918985.gif "点击放大")

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)是通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。[TabContent](../harmonyos-references/ts-container-tabcontent.md)仅在Tabs中使用，对应一个切换页签的内容视图。
* Tab页签切换后会触发[onChange](../harmonyos-references/ts-container-tabs.md#onchange)事件，[changeIndex](../harmonyos-references/ts-container-tabs.md#changeindex)可控制Tabs切换到指定页签。

## 解决方案

1. 整体布局分为两部分：页签部分和页面视图部分。
   * 页签部分通过@Builder自定义封装一个组件，页面视图则用Tabs自定义组件。

     ```ts
     Row({ space: 7 }) {
       Scroll() {
         Row() {
           ForEach(this.tabArray, (item: number, index: number) => {
             this.Tab(`页签 ${item}`, item, index);
           })
         }
         .justifyContent(FlexAlign.Start)
       }
       .align(Alignment.Start)
       .scrollable(ScrollDirection.Horizontal)
       .scrollBar(BarState.Off)
       .width('90%')
       .backgroundColor('#ffb7b7b7')

       Image($r('app.media.startIcon')).onClick(() => {
         if (this.tabArray.length === 0) {
           this.tabArray = [0];
           this.focusIndex = 0;
         } else {
           this.tabArray.push(this.tabArray[this.tabArray.length - 1] + 1);
           this.focusIndex = this.tabArray.length - 1;
           let add = this.focusIndex;
           if (add == 1) {
             this.test = true;
           }
           setTimeout(() => {
             this.controller.changeIndex(add);
           }, 100);
         }
       }).width(20).height(20)
     }
     .width('100%')
     .backgroundColor('#ffb7b7b7')
     ```
   * 页面视图。

     ```ts
     Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
       ForEach(this.tabArray, (item: number) => {
         TabContent() {
           Text(`我是页面 ${item} 的内容`)
             .height(300)
             .width('100%')
             .fontSize(30)
         }
       })
     }
     ```
2. 实现页签和页面视图的联动。

   主要是通过TabsController的changeIndex来实现对应的视图跳转，但需注意由于之后会有增删数组元素的操作，所以此处传入的index值是数组元素的索引值。

   ```ts
   this.controller.changeIndex(pre - 1);
   ```
3. 被选中页签背景颜色变化。

   当用户点击页签时，给变量focusIndex赋值，在背景色属性里与当前数组元素进行比较，同时也需要在Tabs的onChange方法里进行控制。

   ```ts
   .backgroundColor(tabIndex === this.focusIndex ? '#ffffffff' : '#ffb7b7b7')
     .onClick(() => {
       this.test = true;
       this.focusIndex = tabIndex;
       this.controller.changeIndex(tabIndex);
       console.info(`foo ${tabItem}`);
     })
   ```
4. 增添数组元素实现增加页签的效果。

   增添数组元素使用push方法，但由于此demo原始定义的数组是连续的自然数，后续增删数组会打乱原有顺序，所以此处处理为先判断最后一个元素的值再加1，当把所有数组元素删除时，需要再次添加数组元素，同时也需要控制选中样式，所以此基础上加一个判断，让重新生成的页签选中样式在第一个元素上。

   ```ts
   if (this.tabArray.length === 0) {
     this.tabArray = [0];
     this.focusIndex = 0;
   } else {
     this.tabArray.push(this.tabArray[this.tabArray.length - 1] + 1);
     this.focusIndex = this.tabArray.length - 1;
     let add = this.focusIndex;
     if (add == 1) {
       this.test = true;
     }
     setTimeout(() => {
       this.controller.changeIndex(add);
     }, 100);
   }
   ```
5. 删除数组元素实现删减页签的效果。

   ```ts
   let pre = tabIndex;
   if (this.focusIndex === pre && pre === this.tabArray.length - 1) {
     this.tabArray.splice(tabIndex, 1);
     this.focusIndex = pre - 1;
     this.controller.changeIndex(pre - 1);
     this.test = true;
     setTimeout(() => {
       this.test = false;
     }, 400);
   } // 最后一个元素并且当前选中情况
   else if (this.focusIndex === pre) {
     this.tabArray.splice(pre, 1);
   } // 非最后一个元素且当前选中情况
   else if (this.focusIndex > pre) {
     this.focusIndex = this.focusIndex - 1;
     this.tabArray.splice(pre, 1);
     this.controller.changeIndex(this.focusIndex);
   } // 非当前选中且比选中的小
   else {
     this.tabArray.splice(pre, 1);
   }
   ```

完整示例参考如下：

```ts
@Entry
@Component
struct Drag {
  @State tabArray: Array<number> = [0, 1];
  @State focusIndex: number = 0;
  private controller: TabsController = new TabsController();
  @State test: boolean = false;

  // 单独的页签
  @Builder
  Tab(tabName: string, tabItem: number, tabIndex: number) {
    Row({ space: 20 }) {
      Text(tabName).fontSize(18)
      Image($r('app.media.startIcon')).width(20).height(20) // 运行时请按需替换图片资源
        .onClick(() => {
          let pre = tabIndex;
          if (this.focusIndex === pre && pre === this.tabArray.length - 1) {
            this.tabArray.splice(tabIndex, 1);
            this.focusIndex = pre - 1;
            this.controller.changeIndex(pre - 1);
            this.test = true;
            setTimeout(() => {
              this.test = false;
            }, 400);
          } // 最后一个元素并且当前选中情况
          else if (this.focusIndex === pre) {
            this.tabArray.splice(pre, 1);
          } // 非最后一个元素且当前选中情况
          else if (this.focusIndex > pre) {
            this.focusIndex = this.focusIndex - 1;
            this.tabArray.splice(pre, 1);
            this.controller.changeIndex(this.focusIndex);
          } // 非当前选中且比选中的小
          else {
            this.tabArray.splice(pre, 1);
          }
        })
    }
    .justifyContent(FlexAlign.Center)
    .constraintSize({ minWidth: 35 })
    .width(120)
    .height(30)
    .borderRadius({ topLeft: 10, topRight: 10 })
    .backgroundColor(tabIndex === this.focusIndex ? '#ffffffff' : '#ffb7b7b7')
    .onClick(() => {
      this.test = true;
      this.focusIndex = tabIndex;
      this.controller.changeIndex(tabIndex);
      console.info(`foo ${tabItem}`);
    })

  }

  build() {
    Column() {
      Column() {
        Row({ space: 7 }) {
          Scroll() {
            Row() {
              ForEach(this.tabArray, (item: number, index: number) => {
                this.Tab(`页签 ${item}`, item, index);
              })
            }
            .justifyContent(FlexAlign.Start)
          }
          .align(Alignment.Start)
          .scrollable(ScrollDirection.Horizontal)
          .scrollBar(BarState.Off)
          .width('90%')
          .backgroundColor('#ffb7b7b7')

          Image($r('app.media.startIcon')).onClick(() => {
            if (this.tabArray.length === 0) {
              this.tabArray = [0];
              this.focusIndex = 0;
            } else {
              this.tabArray.push(this.tabArray[this.tabArray.length - 1] + 1);
              this.focusIndex = this.tabArray.length - 1;
              let add = this.focusIndex;
              if (add == 1) {
                this.test = true;
              }
              setTimeout(() => {
                this.controller.changeIndex(add);
              }, 100);
            }
          }).width(20).height(20)
        }
        .width('100%')
        .backgroundColor('#ffb7b7b7')

        Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
          ForEach(this.tabArray, (item: number) => {
            TabContent() {
              Text(`我是页面 ${item} 的内容`)
                .height(300)
                .width('100%')
                .fontSize(30)
            }
          })
        }
        .onChange((index: number) => {
          if (index !== 0 && this.tabArray.length > 2) {
            this.focusIndex = index;
            console.info(`change focusIndex ${this.focusIndex}`);
          } else if (this.tabArray.length == 1) {
            this.focusIndex = index;
          } else if (this.tabArray.length == 2 && this.focusIndex == 1) {
            if (this.test) {
              this.focusIndex = 1;
            } else {
              this.focusIndex = 0;
            }
          } else if (!this.test) {
            console.info(`foo ${index}`);
            this.focusIndex = index;
          }
        })
      }
      .alignItems(HorizontalAlign.Start)
      .width('100%')
    }
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .backgroundColor('#ffebebeb')
    .height('100%')
  }
}
```

## 总结

Tabs组件可通过自定义页签与页面结合数组控制数量显示的方式，增加删除页签的功能，同时利用Tabs组件的切换事件响应实现相关操作。
