---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-880
title: 调整显示大小缩放后，布局异常如何处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 调整显示大小缩放后，布局异常如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:41fa1c9c305f46594e945a7631225899c80f6fb17040b8b548126a8627093cb2
---

## 问题信息

在设置>显示和亮度>字体大小和界面缩放中调整显示大小缩放后，出现组件遮挡、截断、错乱等布局异常问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/0Hp7m5RqR3GpkDjndSgq_g/zh-cn_image_0000002658918849.png "点击放大")

## 背景知识

* [densityUpdate](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#ondensityupdate12)：监听屏幕像素密度变化。当设置中的显示大小缩放变化后，[屏幕实例](../harmonyos-references/js-apis-display.md#display)的DPI会随之变化。
* [onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)：组件尺寸变化事件。组件区域变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。
* [显示缩放对断点的影响](../best-practices/bpta-multi-device-responsive-layout.md#section677963818362)：系统修改显示大小缩放会影响页面布局。在用户变更缩放比例后DPI会随之变化，从而导致vp会发生变化，需要考虑vp变化后对断点区间的影响。
* [响应式布局](../best-practices/bpta-multi-device-responsive-layout.md)：页面可以根据不同屏幕尺寸自动调整布局，提供更舒适的界面和更好的用户体验。
* [自适应布局](../best-practices/bpta-multi-device-adaptive-layout.md)：可以使组件的尺寸根据容器组件的尺寸自行调整。

## 问题定位

1. 使用DevEco Testing的UIViewer工具查看布局异常时的UI结构。在显示大小缩放修改后，页面组件尺寸发生变化，页面布局出现异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/bJ12DtHJQbSHcUzCBmPHQA/zh-cn_image_0000002628399634.png "点击放大")
2. 排查是否采用响应式布局或自适应布局。排查代码中是否在[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)事件中更新断点。排查代码中是否使用flexGrow、justifyContent、layoutWeight等和自适应布局相关的属性。
3. 排查代码中是否使用densityUpdate、onSizeChange等监听事件，修改组件的大小和位置（如组件width、height、position等属性）。

## 分析结论

页面未采用响应式布局或自适应布局，并且未通过densityUpdate、onSizeChange等监听事件，调整组件大小或位置，导致页面布局异常。

## 修改建议

* 采用[响应式布局](../best-practices/bpta-multi-device-responsive-layout.md)。自行根据宽高断点以及分辨率、屏幕DPI等信息调整页面布局，约束组件显示的宽高以避免出现组件遮挡、截断等布局异常问题。
* 直接调整页面布局，采用自适应布局方案，配置layout属性，通过自适应缩放能力，确保组件间不会相互遮挡。

  ```ts
  @Entry
  @Component
  struct FlexLayout {
    build() {
      Flex() {
        Row() {
          Text('布局测试-偏左')
        }
        .layoutWeight(1)

        Row() {
          Row() {
            Text('布局测试-居中')
          }
          .height(40)
          .layoutWeight(2)

          Row() {
            Text('占位')
          }
          .layoutWeight(1)
        }
        .layoutWeight(1)

        Blank()
          .layoutWeight(1)
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/PvqPCTzqSg2XsQOCa6mb1Q/zh-cn_image_0000002658798899.png "点击放大")
* 在densityUpdate或onSizeChange监听事件中，调整组件大小和位置。

  ```ts
  import { display, uiObserver, window } from '@kit.ArkUI';

  @Entry
  @Component
  struct OnEventLayout {
    parentPadding: number = 12; // 左右边距
    fontSizeVp: number = 16; // 字体大小，单位vp
    // 限制组件最大宽度,为(左半屏幕-边距)/2
    @State maxWidth: number =
      (this.getUIContext().px2vp(display.getDefaultDisplaySync().width) / 2 - this.parentPadding) / 2;

    aboutToAppear(): void {
      this.getUIContext()
        .getUIObserver()
        .on('densityUpdate', (info: uiObserver.DensityInfo) => {
          // 根据屏幕DPI自行调整布局（如限制组件大小、文本超出省略换行等）
          console.info('[densityUpdate]', 'current density: ', info.density);
          // 获取窗口宽度
          window.getLastWindow(this.getUIContext().getHostContext(), (err, windowClass) => {
            let windowWidth = this.getUIContext().px2vp(windowClass.getWindowProperties().windowRect.width);
            // 设置组件最大宽度，为(左半窗口-边距)/2，左侧组件占一半，右侧组件的一半宽度也不能超过该值
            this.maxWidth = (windowWidth / 2 - this.parentPadding) / 2;
          });

          // ...
          // 如果同时采用了响应式布局，可以通过getWindowWidthBreakpoint方法直接更新断点，再根据断点数据调整页面布局
        });
    }

    build() {
      // 给组件的位置宽高等属性绑定状态变量，在densityUpdate监听事件中调整
      // 请根据实际布局情况自行计算页面布局相关的数据
      Column() {
        Column() {
          Stack() {
            Row() {
              Row() {
                Text('布局测试-偏左')
                  .constraintSize({ maxWidth: this.maxWidth }) // 限制最大宽度
              }
              .height(40)
            }
            .width('100%')
            .height(40)

            Row() {
              Row() {
                Text('布局测试-居中')
              }
              .height(40)

              Row() {
                Text('占位')
              }
              .height(40)
            }
            .constraintSize({ maxWidth: this.maxWidth * 2 }) // 限制最大宽度
            .layoutWeight(1)

          }
          .margin({
            left: 12,
            right: 12
          })
        }
        .width('100%')
        .height('100%')
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/jAAKwSzGRUemkbGFWgVUoA/zh-cn_image_0000002628559540.png "点击放大")

## 常见FAQ

Q：在卡片服务中，一多适配时，如何让子组件根据父组件的大小进行位置适配？例如在手机和平板中相同类型1\*1的卡片大小不一致，如何动态设置一个Canvas绘制的圆环的圆心，使其是总是处于卡片的中心？

A：onSizeChange事件从API11开始支持在卡片中使用，可以考虑采用onSizeChange事件获取卡片大小，然后设置Canvas绘制的圆心，分别等于卡片宽度和高度的二分之一。
