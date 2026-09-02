---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1160
title: 如何在bindSheet中实现页面切换的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在bindSheet中实现页面切换的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:addb633b22ab6235c3410e707c5fd18d63d1531eea3a1c40d76eedc4ffe9d5dc
---

## 问题现象

在使用bindSheet时，只能显示一个弹窗内容，如何在bindSheet中实现页面切换的效果？

## 背景知识

* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)：半模态页面（bindSheet）默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见，帮助用户在与半模态交互时保留其父视图环境。半模态页面适用于展示简单的任务或信息面板，例如，个人信息、文本简介、分享面板、创建日程、添加内容等。若需展示可能影响父视图的半模态页面，半模态支持配置为非模态交互形式。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供animateTo接口来指定由于闭包代码导致的状态变化插入过渡动效。
* [translate](../harmonyos-references/ts-page-transition-animation.md#translate)：设置页面转场时的平移效果。

## 解决方案

实现思路如下：

* 半模态页面实现：使用Stack容器层叠布局两个组件，通过@State变量动态控制组件显隐状态，从而实现组件切换。
* 动画效果优化：为组件绑定onClick点击事件，使用animateTo设置动画持续时间，再指定由于闭包代码导致的状态变化插入过渡动效。

  ```ts
  .onClick(() => {
    this.title = '子集标题';
    this.getUIContext()?.animateTo({
      duration: 800, // 动画持续时间，单位为毫秒。
      curve: Curve.EaseOut, // 动画曲线。
      playMode: PlayMode.Normal, // 动画播放模式，默认播放完成后重头开始播放。  默认值：PlayMode.Normal
      onFinish: () => {
        console.info('play end');
      }
    }, () => {
      // 指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。
      this.flag = !this.flag;
    });
  });
  ```
* 页面切换实现：translate属性实现页面切换效果，平移距离通过onAreaChange回调动态获取弹窗宽度，避免不同设备动画的移动尺寸不同。

  ```ts
  SheetBuilder2({ title: this.title, flag: this.flag })
    .width('100%')
    .height('100%')
    .translate(this.flag ? { x: 0 } : { x: this.translateX })
    .onAreaChange((oldValue: Area, newValue: Area) => {
      console.info('testTag', `获取到oldValue、newValue:${oldValue.width}、${newValue.width}`);
      // 适配其他尺寸设备时，使用onAreaChange获取宽度，动画的移动尺寸直接取弹窗的宽度。
      this.translateX = newValue.width as number;
    });
  ```

完整代码如下：

```ts
@Entry
@Component
struct SheetDemo {
  @State isShowSheet: boolean = false;
  private items: number[] = [0, 1, 2, 3, 4];
  @State title: string = '标题';
  @State flag: boolean = false;
  @State translateX: number = 0;

  @Builder
  SheetBuilder() {
    Stack() {

      Column() {
        Row() {
          Text(this.title);
        }
        .padding({ left: 20, right: 20 })
        .height('50')
        .width('100%');

        List({ space: '10vp' }) {
          ForEach(this.items, (item: number) => {
            ListItem() {
              Text(String(item)).fontSize(16).fontWeight(FontWeight.Bold);
            }
            .width('90%')
            .height('80vp')
            .backgroundColor('#E5E5E5')
            .borderRadius(10)
            .onClick(() => {
              this.title = '子集标题';
              this.getUIContext()?.animateTo({
                duration: 800, // 动画持续时间，单位为毫秒。
                curve: Curve.EaseOut, // 动画曲线。
                playMode: PlayMode.Normal, // 动画播放模式，默认播放完成后重头开始播放。  默认值：PlayMode.Normal
                onFinish: () => {
                  console.info('play end');
                }
              }, () => {
                // 指定显示动效的闭包函数，在闭包函数中导致的状态变化系统会自动插入过渡动画。
                this.flag = !this.flag;
              });
            });

          });
        }
        .alignListItem(ListItemAlign.Center)
        .margin({ top: '10vp' })
        .width('100%')
        .height('100%');
      }.width('100%').height('100%')
      .translate(this.flag ? { x: -this.translateX } : { x: 0 });

      SheetBuilder2({ title: this.title, flag: this.flag })
        .width('100%')
        .height('100%')
        .translate(this.flag ? { x: 0 } : { x: this.translateX })
        .onAreaChange((oldValue: Area, newValue: Area) => {
          console.info('testTag', `获取到oldValue、newValue:${oldValue.width}、${newValue.width}`);
          // 适配其他尺寸设备时，使用onAreaChange获取宽度，动画的移动尺寸直接取弹窗的宽度。
          this.translateX = newValue.width as number;
        });

    };
  }

  build() {

    Column() {
      Button('Open Sheet').width('90%')
        .onClick(() => {
          this.isShowSheet = !this.isShowSheet;
        })
        .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
          detents: [SheetSize.MEDIUM, SheetSize.LARGE, 600],
          preferType: SheetType.BOTTOM,
        });
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center);
  }
}

@Component
struct SheetBuilder2 {
  @Link title: string;
  @Link flag: boolean;

  build() {
    Column() {
      Row() {
        Column() {
          Image($r('sys.media.ohos_ic_compnent_titlebar_back'))
            .height(24)
            .width(24)
            .fillColor('#313232');

        }
        .borderRadius(40)
        .width(40)
        .height(40)
        .justifyContent(FlexAlign.Center)
        .alignItems(HorizontalAlign.Center)
        .backgroundColor('#e6e8e9')
        .margin({ right: 8 })
        .onClick(() => {
          this.title = '标题';
          this.getUIContext()?.animateTo({
            duration: 500,
            curve: Curve.EaseOut,
            playMode: PlayMode.Normal,
            onFinish: () => {
              console.info('play end');
            }
          }, () => {
            this.flag = !this.flag;
          });
        });
        Text(this.title);
      }
      .height('50')
      .width('100%');
      Column() {
        Text('子集页面');
      }
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
      .width('100%')
      .layoutWeight(1);
    }.width('100%').height('100%').padding({ right: 18, left: 18 });
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/_qU1ejD1QaidARMbC-I4GA/zh-cn_image_0000002639986766.png "点击放大")

## 总结

适用于弹窗内页面切换效果场景。
