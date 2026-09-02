---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1367
title: 如何实现自定义分段按钮跟手滑动
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现自定义分段按钮跟手滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b439672b8b7b99f5e39afa4cb6c918892a178ab369f59dc3e6358d63476842b6
---

## 问题现象

如何实现类似于SegmentButton分段按钮并且跟手滑动效果。

## 背景知识

* [SegmentButton](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md)：分段按钮组件，包含页签类分段按钮、单选类分段按钮、多选类分段按钮。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [animateToImmediately](../harmonyos-references/ts-explicit-animatetoimmediately.md#animatetoimmediately)：提供显式动画立即下发功能。

## 解决方案

* 通过animateToImmediately实现平滑移动动画，点击切换时计算indicatorLeftMargin实现指示器位置变化。
* 使用PanGesture滑动手势事件，动态计算offsetX实现拖拽跟随效果。

  ```ts
  @Entry
  @Component
  struct SegmentButtonExample {
    @State currentIndex: number = 0;
    @State indicatorLeftMargin: number = 0;
    buttonWidth: number = 330;
    tags: string[] = ['周榜', '月榜', '日榜', '年榜'];
    indicatorWidth: number = this.buttonWidth / this.tags.length;
    @State isActive: boolean = false;
    @State offsetX: number = 0;
    @State positionX: number = 0;
    private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });

    build() {
      Stack({ alignContent: Alignment.TopStart }) {
        Row() {
          ForEach(this.tags, (tag: string, index: number) => {
            Text(tag)
              .height('100%')
              .textAlign(TextAlign.Center)
              .width(this.indicatorWidth)
              .onClick(() => {
                animateToImmediately({
                  duration: 300, // 动画时长
                  curve: Curve.Linear, // 动画曲线
                  iterations: 1, // 播放次数
                  playMode: PlayMode.Normal, // 动画模式
                  onFinish: () => {
                    this.isActive = false;
                  }
                }, () => {
                  switch (index) {
                    case 0:
                      this.indicatorLeftMargin = 0;
                      this.positionX = 0;
                      this.currentIndex = 0;
                      break;
                    case 1:
                      this.indicatorLeftMargin = 90;
                      this.positionX = 90;
                      this.currentIndex = 1;
                      break;
                    case 2:
                      this.indicatorLeftMargin = 180;
                      this.positionX = 180;
                      this.currentIndex = 2;
                      break;
                    case 3:
                      this.indicatorLeftMargin = 270;
                      this.positionX = 270;
                      this.currentIndex = 3;
                      break;
                    default:
                      break;
                  }
                });
              });
          });
        }
        .justifyContent(FlexAlign.SpaceAround)
        .height(48)
        .borderRadius(30)
        .backgroundColor('#e8eaee')
        .width(this.buttonWidth)
        .gesture(GestureGroup(GestureMode.Parallel,
          PanGesture(this.panOption)
            .onActionStart(() => {
              console.info('Pan start');
            })
            .onActionUpdate((event: GestureEvent) => {
              if (event) {
                this.offsetX = this.positionX + event.offsetX;
                animateToImmediately({
                  duration: 300, // 动画时长
                  curve: Curve.Linear, // 动画曲线
                  iterations: 1, // 播放次数
                  playMode: PlayMode.Normal, // 动画模式
                }, () => {
                  if (this.offsetX <= 0 || this.offsetX >= 360) {
                    return;
                  }
                  this.indicatorLeftMargin = this.offsetX * 270 / 360;
                });
              }
            })
            .onActionEnd(() => {
              this.positionX = this.offsetX;
              animateToImmediately({
                duration: 300, // 动画时长
                curve: Curve.Linear, // 动画曲线
                iterations: 1, // 播放次数
                playMode: PlayMode.Normal, // 动画模式
                onFinish: () => {
                  this.isActive = false;
                }
              }, () => {
                switch (true) {
                  case 0 <= this.offsetX && this.offsetX <= this.indicatorWidth:
                    this.indicatorLeftMargin = 0;
                    this.currentIndex = 0;
                    break;
                  case this.indicatorWidth < this.offsetX && this.offsetX <= this.indicatorWidth * 2:
                    this.indicatorLeftMargin = this.indicatorWidth;
                    this.currentIndex = 1;
                    break;
                  case this.indicatorWidth * 2 < this.offsetX && this.offsetX <= this.indicatorWidth * 3:
                    this.indicatorLeftMargin = this.indicatorWidth * 2;
                    this.currentIndex = 2;
                    break;
                  case this.indicatorWidth * 3 < this.offsetX && this.offsetX <= this.indicatorWidth * 4:
                    this.indicatorLeftMargin = this.indicatorWidth * 3;
                    this.currentIndex = 3;
                    break;
                }
              });
            })
        ));

        Column() {
          if (this.currentIndex === 0) {
            Text('周榜');
          } else if (this.currentIndex === 1) {
            Text('月榜');
          } else if (this.currentIndex === 2) {
            Text('日榜');
          } else {
            Text('年榜');
          }
        }
        .height(48)
        .hitTestBehavior(HitTestMode.Transparent)
        .justifyContent(FlexAlign.Center)
        .scale(this.isActive ? { x: 0.95, y: 0.95 } : { x: 1, y: 1 })
        .width(this.indicatorWidth)
        .margin({ left: this.indicatorLeftMargin })
        .borderRadius(30)
        .backgroundColor('#ffffff')
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down) {
            this.isActive = true;
          }
        });
      }.width('90%')
      .margin({ top: 50, left: 20 });
    }
  }
  ```

  效果图如图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/fn6a-_g1SDKDfrOLQVD8xw/zh-cn_image_0000002658961251.png "点击放大")
