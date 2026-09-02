---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1498
title: 侧边栏的显示隐藏与常见使用问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 侧边栏的显示隐藏与常见使用问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d78d1befd41d9a0a3195e2ec2de8b7db065764e08b82dfe5302c8823affa63b4
---

## 问题现象

在使用SideBarContainer组件开发时，侧边栏的显示与隐藏有如下几个经典场景：

* 场景一：将SideBarContainer组件中的type设置为Overlay时，如何实现点击空白区域退出侧滑状态？
* 场景二：如何实现页面内容随着侧边栏弹出平移，侧边栏跟随手指滑动，松手后如有收起趋势，侧边栏将自动收起？

## 背景知识

* [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)：提供侧边栏可以显示和隐藏的侧边栏容器，通过子组件定义侧边栏和内容区，第一个子组件表示侧边栏，第二个子组件表示内容区。
* [组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)：组件内转场主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [HdsSideBar](../harmonyos-references/ui-design-hdssidebar.md)：本模块支持显示和隐藏的侧边栏容器，并且可以自定义侧边栏和内容区。注意：起始版本：6.0.0(20)。

## 解决方案

* 场景一：设置两个按钮分别用于打开、关闭侧边栏，使用transition和定时器自定义侧边栏出场、退场动画，通过SideBarContainer组件的showSideBar属性控制侧边栏的显隐状态，将关闭侧边栏的点击事件添加在空白区域上即可实现。完整示例参考如下：

  ```ts
  @Entry
  @Component
  struct SideBarContainerDemo {
    arr: number[] = [1, 2, 3];
    @State current: number = 1;
    @State showSideBar: boolean = false;
    @State showFlag: Visibility = Visibility.Hidden;

    // 延迟关闭侧边栏，让自定义的出场动画显示
    cancel() {
      this.showFlag = Visibility.Hidden;
      setTimeout(() => {
        this.showSideBar = !this.showSideBar;
      }, 1000);
    }

    build() {
      // 将SideBarContainer中的type设置为Overlay
      SideBarContainer(SideBarContainerType.Overlay) {
        Column() {
          ForEach(this.arr, (item: number) => {
            Column({ space: 5 }) {
              Text('Index0' + item)
                .fontSize(25)
                .fontColor(this.current === item ? '#0A59F7' : '#999')
                .fontFamily('source-sans-pro,cursive,sans-serif');
            }
            .width(110)
            .height(50)
            .borderRadius(10)
            .backgroundColor('#f2f2f3')
            .justifyContent(FlexAlign.Center)
            .onClick(() => {
              this.current = item;
            });
          }, (item: string) => item);
        }
        .visibility(this.showFlag)
        // 通过transition自定义出场动画
        .transition(TransitionEffect.OPACITY
          .animation({ duration: 1000 })
          .combine(TransitionEffect.translate({ x: 100 })))
        .width('100%')
        .justifyContent(FlexAlign.SpaceEvenly)
        .backgroundColor(Color.White)
        .shadow({
          radius: 100,
          color: '#ffcccccd',
          offsetX: -10,
          offsetY: -10
        });

        Column() {
          Button('open sidebar')
            .width('80%')
            .onClick(() => {
              this.showFlag = Visibility.Visible;
              this.showSideBar = true;
            })
            .margin({ top: 30, bottom: 30 });
          Button('close sidebar')
            .width('80%')
            .onClick(() => {
              this.cancel();
            });
        }.height('100%')
        // 点击空白区域退出侧滑状态
        .onClick(() => {
          this.cancel();
        });
      }
      .divider(null)
      .sideBarPosition(SideBarPosition.End)
      // 是否显示侧边栏
      .showSideBar(this.showSideBar)
      .showControlButton(false)
      .sideBarWidth(150)
      .minSideBarWidth(50)
      .maxSideBarWidth(300)
      .minContentWidth(0)
      .onChange((value: boolean) => {
        console.info(`status: ${value}`);
      });
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/LV8isYKRRP6opDrLNtSBzQ/zh-cn_image_0000002658845793.png "点击放大")
* 场景二：使用Stack布局将底层主界面、灰色半透明蒙层、侧边栏界面依次堆叠，然后通过组件内转场中的TransitionEffect.move实现底层主界面的平移，通过PanGesture手势实现滑动效果，示例代码如下：

  ```ts
  import { window } from '@kit.ArkUI';

  // 侧边栏容器
  @Component
  export struct SideBar {
    build() {
      Column() {
        Text('Side Bar')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
          })
      }
      .justifyContent(FlexAlign.Center)
      .backgroundColor('#F1F3F5')
      .height('100%')
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    }
  }

  @Entry
  @Component
  struct Index {
    private windowClass: window.Window | undefined = undefined;
    @State showSideBar: boolean = false; // 显示侧边栏
    isLeft: boolean = true; // 设置左侧弹出或右侧弹出
    sideBarWidth = 290; // 设置侧边栏宽度
    duration = 250; // 设置侧边栏动画时长
    @State xValue: number = 0; // 底层主界面距离边缘距离
    maxX: number = this.sideBarWidth; // 最大距离值
    minX: number = 0; // 最小距离值

    aboutToAppear(): void {
      // 获取窗口实例
      window.getLastWindow(this.getUIContext().getHostContext(),
        (err, windowObj) => {
          if (err.code) {
            console.error(`Failed to getLastWindow. Code：${err.code}，message：${err.message}`);
          }
          this.windowClass = windowObj;
          this.windowClass.setWindowLayoutFullScreen(true); // 设置窗口全屏
          this.windowClass.setWindowSystemBarEnable(['status', 'navigation']);
        });
    }

    build() {
      // 底层主界面
      Stack({ alignContent: this.isLeft ? Alignment.TopStart : Alignment.TopEnd }) {
        Column() {
          Text('Open Side')
            .fontSize(30)
            .onClick(() => {
              this.getUIContext().animateTo({
                duration: this.duration,
                curve: Curve.EaseOut,
              }, () => {
                this.showSideBar = true;
                this.xValue = this.sideBarWidth;
              });
            })
        }
        .justifyContent(FlexAlign.Center)
        .margin({
          right: !this.isLeft ? this.xValue : 0,
          left: this.isLeft ? this.xValue : 0,
        })
        .height('100%')
        .width('100%')

        // 灰色半透明蒙层
        if (this.showSideBar) {
          Column()
            .backgroundColor('#000')
            .opacity(0.4)
            .height('100%')
            .width('100%')
            .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
            .onClick(() => {
              this.getUIContext().animateTo({
                duration: this.duration,
                curve: Curve.EaseOut,
              }, () => {
                this.showSideBar = false;
                this.xValue = 0;
              });
            })
        }

        // 侧边栏
        if (this.showSideBar) {
          Column() {
            SideBar()
          }
          .margin({
            left: this.isLeft ? this.xValue - this.sideBarWidth : 0,
            right: !this.isLeft ? this.xValue - this.sideBarWidth : 0,
          })
          .width(this.sideBarWidth)
          .visibility(this.showSideBar ? Visibility.Visible : Visibility.Hidden)
          .transition(TransitionEffect.OPACITY.animation({ duration: this.duration, curve: Curve.EaseInOut })
            .combine(TransitionEffect.move(this.isLeft ? TransitionEdge.START : TransitionEdge.END)))
          .gesture(PanGesture(new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right }))
          // 滑动手势
            .onActionUpdate((event: GestureEvent) => {
              if (event) {
                let a = this.isLeft ? this.maxX + event.offsetX : this.maxX - event.offsetX;
                if (this.xValue >= this.maxX) { // 如果xValue大于最大值，将最大值赋给xValue
                  // 当前值为手势起始位置加上偏移量
                  this.xValue = a >= this.maxX ? this.maxX : a;
                } else if (this.xValue <= this.minX) { // 如果xValue小于最小值，将最小值赋给xValue
                  // 当前值为手势起始位置加上偏移量
                  this.xValue = a <= this.minX ? this.minX : a;
                } else { // 区间内直接赋值
                  this.xValue = a;
                }
              }
            })
            .onActionEnd((event: GestureEvent) => {
              if (event.velocityX > 0) {
                // 滑动方向向右
                this.getUIContext().animateTo({
                  duration: 250,
                  curve: Curve.EaseOut,
                }, () => {
                  this.xValue = this.isLeft ? this.maxX : this.minX;
                  this.showSideBar = this.isLeft ? true : false;
                });
              } else {
                // 滑动方向向左
                this.getUIContext().animateTo({
                  duration: 250,
                  curve: Curve.EaseOut,
                }, () => {
                  this.xValue = this.isLeft ? this.minX : this.maxX;
                  this.showSideBar = this.isLeft ? false : true;
                });
              }
            })
          )
        }
      }
      .height('100%')
      .width('100%')
    }
  }
  ```

  通过设置isLeft可以控制左侧弹出或者右侧弹出。

  效果如下：

  | 左侧弹出 | 右侧弹出 |
  | --- | --- |
  |  |  |

## 常见FAQ

Q：如何判断SideBarContainer侧边栏区域是否关闭？

A：通过[onChange](../harmonyos-references/ts-container-sidebarcontainer.md#onchange)事件可以判断，当侧边栏的状态在显示和隐藏之间切换时会触发该回调，通过该事件回调，可记录侧边栏的状态。

Q：如何实现点击右箭头显示侧边栏，页面内容区缩小并向右移动，点击左箭头收回侧边栏，并且可以通过手势向左滑动收回侧边栏。

A：请参考HdsSideBar[示例](../harmonyos-references/ui-design-hdssidebar.md#示例)，将sideBarContainerType设置为SideBarContainerType.Embed即可实现显示侧边栏会导致内容区缩小，隐藏侧边栏会扩大内容区效果。
