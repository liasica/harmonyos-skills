---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-wearable-1
title: 智能表可滚动页面无法响应表冠旋转事件
breadcrumb: FAQ > 多设备场景 > 穿戴 > 常见问题 > 智能表可滚动页面无法响应表冠旋转事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:53f676f4849202042f16fa69bdfa8009ac043b92c8e2f15e7313cf81e0783d9b
---

## 问题现象

* **场景1：** 智能表中可滑动的组件（如：ArcList、List、Swiper等），如何响应表冠旋转事件？
* **场景2：** 智能表中可滑动的组件（如：ArcList、List、Swiper等）在if/else条件切换后，分支中的组件重新构建后无法响应表冠旋转事件。
* **场景3：** 智能表的列表页面中列表已设置获焦，子组件有输入框组件，点击后输入框后，列表无法响应表冠旋转事件。
* **场景4：** 智能表页面中使用Stack布局，两个子组件均为可滚动列表，默认设置前一个子组件获焦，当后一个子组件按条件展示覆盖前一个子组件后无法响应表冠旋转事件。

## 背景知识

* [表冠事件](../harmonyos-references/ts-universal-events-crown.md)：指扭动表冠时触发的事件，事件的分发依赖于应用焦点，开发者可以通过[焦点事件](../harmonyos-references/ts-universal-focus-event.md)自定义事件处理。
* [响应旋转表冠](../harmonyos-guides/arkts-layout-development-create-arclist.md#响应旋转表冠)：手表设备上弧形列表在获焦的情况下可对旋转表冠做出响应，用户可通过旋转表冠的操作滑动列表，浏览列表项数据。弧形列表可通过[焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)相关属性成为所在页面的默认焦点。
* [主动获焦/失焦](../harmonyos-guides/arkts-common-events-focus-event.md#主动获焦失焦)：使用FocusController中的requestFocus主动获取焦点，调用此接口可以主动让焦点转移至参数指定的组件上，焦点转移生效时间为下一个帧信号。

## 问题定位

1. 通过背景知识响应旋转表冠可知，组件需要设置[focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)、[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)、[focusOnTouch](../harmonyos-references/ts-universal-attributes-focus.md#focusontouch9)属性获焦，获焦后可响应表冠事件；
2. 查看需要响应旋转表冠事件的组件是否已设置以上属性，如设置后仍无法响应，则需确认是否是当前组件没有主动获焦，或者是已经失焦。

## 分析结论

* **场景1：**

  组件收到表冠事件的前提是该组件获焦，焦点控制可以通过focusable、defaultFocus、focusOnTouch进行管理。默认支持表冠事件的组件：[Slider](../harmonyos-references/ts-basic-components-slider.md)、[DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)、[TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)、[TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)、[ArcList](../harmonyos-references/ts-container-arclist.md)、[Refresh](../harmonyos-references/ts-container-refresh.md)和[Swiper](../harmonyos-references/ts-container-swiper.md)。
* **场景2：**

  当可滑动组件（如ArcList）位于if/else条件渲染中，并设置了可获焦属性时，其父容器（如Column）在条件切换后不会自动将焦点传递给重新构建后的子组件。
* **场景3：**

  点击子组件中的输入框并输入文本后，焦点在输入框上，导致列表组件失去焦点控制，旋转表冠无法再次响应。
* **场景4：**

  Stack布局中，后一个子组件按条件展示后，覆盖前一个获焦的子组件，导致当前展示的子组件无法响应表冠事件，是因为前一个子组件并未销毁，焦点仍在前一个子组件上，后一个子组件展示后需要主动获焦。

## 修改建议

* **场景1：**

  默认可滑动组件只需要添加focusable(true)、 focusOnTouch(true)、defaultFocus(true)属性获焦即可响应。

  ```ts
  import { ArcList, ArcListItem } from '@ohos.arkui.ArcList';
  import { LengthMetrics } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    @State private numItems: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    private watchSize: string = '466px'; // Wearable默认宽高：466*466
    private listSize: string = '414px'; // item宽度

    build() {
      Column() {
        ArcList({ initialIndex: 0 }) {
          ForEach(this.numItems, (item: number) => {
            ArcListItem() {
              Text('' + item)
                .width(this.listSize)
                .height(50)
                .fontSize(24)
                .borderRadius(25)
                .backgroundColor(0x17A98D);
            }.align(Alignment.Center);
          }, (item: number, index: number) => (item + index).toString());
        }
        .space(LengthMetrics.px(10))
        .borderRadius(this.watchSize)
        .focusable(true)
        .focusOnTouch(true)
        .defaultFocus(true);
      }
      .width('100%')
      .height('100%');
    }
  }
  ```
* **场景2：**

  在场景1基础上，还需要在if/else分支中的可滑动组件（如：ArcList）上添加id属性，并在onAppear方法中调用requestFocus方法绑定该id主动获焦。

  ```ts
  import { ArcList, ArcListItem, LengthMetrics } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    @State private numItems: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    private watchSize: string = '466px'; // Wearable默认宽高：466*466
    private listSize: string = '414px'; // item宽度
    @State isLoading: boolean = true;

    onPageShow(): void {
      setTimeout(() => {
        this.isLoading = false;
      }, 1000);
    }

    build() {
      Column() {
        if (this.isLoading) {
          Text('数据加载中');
        } else {
          ArcList({ initialIndex: 0 }) {
            ForEach(this.numItems, (item: number) => {
              ArcListItem() {
                Text('' + item)
                  .width(this.listSize)
                  .height(50)
                  .fontSize(24)
                  .borderRadius(25)
                  .backgroundColor(0x17A98D);
              }.align(Alignment.Center);
            }, (item: number, index: number) => (item + index).toString());
          }
          .space(LengthMetrics.px(10))
          .borderRadius(this.watchSize)
          .focusable(true)
          .focusOnTouch(true)
          .defaultFocus(true)
          .id('ArcList')
          .onAppear(() => {
            try {
              this.getUIContext().getFocusController().requestFocus('ArcList');
            } catch (error) {
              console.error('requestFocus failed code is ' + error.code + 'message is ' + error.message);
            }
          });
        }
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

* **场景3：**

  在场景1基础上，还需要在输入框TextInput之外的子组件上添加id属性，并在TextInput失焦方法onBlur中调用requestFocus方法绑定该id主动获焦。

  ```ts
  import { ArcList, ArcListItem, LengthMetrics } from '@kit.ArkUI';

  @Entry
  @ComponentV2
  struct Index {
    @Local private numItems: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    private watchSize: string = '466px'; // Wearable默认宽高：466*466
    private listSize: string = '414px'; // item宽度
    @Local content: string = '';

    build() {
      Column() {
        ArcList({ initialIndex: 0 }) {
          ArcListItem() {
            Text('Title')
              .width(this.listSize)
              .height(50)
              .focusable(true)
              .onClick(() => {
              })
              .id('Title');
          }.align(Alignment.Center);

          ArcListItem() {
            TextInput({
              text: $$this.content,
              placeholder: 'click to input'
            })
              .width(this.listSize)
              .onBlur(() => {
                try {
                  this.getUIContext().getFocusController().requestFocus('Title');
                } catch (error) {
                  console.error('requestFocus failed code is ' + error.code + 'message is ' + error.message);
                }
              });
          }
          .align(Alignment.Center);

          ForEach(this.numItems, (item: number) => {
            ArcListItem() {
              Text('' + item)
                .width(this.listSize)
                .height(50)
                .fontSize(24)
                .borderRadius(25)
                .backgroundColor(0x17A98D);
            }.align(Alignment.Center);
          }, (item: number, index: number) => (item + index).toString());
        }
        .space(LengthMetrics.px(10))
        .borderRadius(this.watchSize)
        .id('ArcList')
        .focusable(true)
        .focusOnTouch(true)
        .defaultFocus(true);
      }.width('100%')
      .height('100%');
    }
  }
  ```
* **场景4：**

  Stack布局中，后一个子组件覆盖前一个子组件展示时，将两个子组件都添加id属性并设置可获焦属性，后一个子组件展示时在onAppear方法中使用requestFocus主动获焦，销毁或隐藏时在onDisAppear中将焦点通过requestFocus再重新绑定回前一个子组件。

  ```ts
  import { ArcList, ArcListItem, LengthMetrics } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    @State private numItems: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    private watchSize: string = '466px'; // Wearable默认宽高：466*466
    private listSize: string = '414px'; // item宽度
    @State nextComponentShow: boolean = false;

    @Builder
    private nextComponent(): void {
      List({ space: 12 }) {
        ForEach(this.numItems, (item: number) => {
          ListItem() {
            Text('Item' + item)
              .width(this.listSize)
              .height(50)
              .fontSize(24)
              .borderRadius(25)
              .backgroundColor('#0A59F7')
              .onClick(() => {
                this.nextComponentShow = false;
              });
          }
          .width('100%');
        }, (item: number, index: number) => (item + index).toString());
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#FFFFFF')
      .id('NextCom')
      .focusable(true)
      .focusOnTouch(true)
      .onAppear(() => {
        try {
          this.getUIContext().getFocusController().requestFocus('NextCom');
        } catch (error) {
          console.error('requestFocus failed code is ' + error.code + 'message is ' + error.message);
        }
      })
      .onDisAppear(() => {
        try {
          this.getUIContext().getFocusController().requestFocus('ArcList');
        } catch (error) {
          console.error('requestFocus failed code is ' + error.code + 'message is ' + error.message);
        }
      });
    }

    build() {
      Stack() {
        Column() {
          ArcList({ initialIndex: 0 }) {
            ForEach(this.numItems, (item: number) => {
              ArcListItem() {
                Text('' + item)
                  .width(this.listSize)
                  .height(50)
                  .fontSize(24)
                  .borderRadius(25)
                  .backgroundColor(0x17A98D)
                  .onClick(() => {
                    this.nextComponentShow = true;
                  });
              }.align(Alignment.Center);
            }, (item: number, index: number) => (item + index).toString());
          }
          .space(LengthMetrics.px(10))
          .borderRadius(this.watchSize)
          .id('ArcList')
          .focusable(true)
          .focusOnTouch(true)
          .defaultFocus(true);
        }
        .width('100%')
        .height('100%');

        if (this.nextComponentShow) {
          this.nextComponent();
        }

      }.width('100%')
      .height('100%');
    }
  }
  ```
