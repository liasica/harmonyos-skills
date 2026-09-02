---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-928
title: 如何解决点击非菜单控制区域事件穿透到下层组件的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决点击非菜单控制区域事件穿透到下层组件的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:49a852b5a3451e498cb122debe3af1b5349d2d92de952d9fa0b28ef5d276404e
---

## 问题现象

使用bindContextMenu绑定菜单后，长按弹出菜单时，点击非菜单区域会导致菜单关闭，同时触发下层组件的点击事件（如ListItem的点击事件）。

现象如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/8FSxBFgjTMqQKwXcbPOunQ/zh-cn_image_0000002658919533.png "点击放大")

## 背景知识

使用[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)并设置预览图，此时为模态。使用[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu)或[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)未设置预览图时，菜单弹出无蒙层，此时为非模态。

## 解决方案

* 方案一：长按触发弹窗的时候，通过设置preview或mask参数将弹窗变成模态弹窗，此时操作不会透传到页面上，但会存在蒙层。

  ```ts
  @Entry
  @Component
  struct Index {
    private scroller = new Scroller();
    private list: string[] = [];

    aboutToAppear(): void {
      for (let i = 0; i < 15; i++) {
        this.list.push(i + '');
      }
    }

    @Builder
    menu() {
      Menu() {
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单1' });
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单2' });
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单3' });
      };
    }

    build() {
      Column() {
        List({ scroller: this.scroller, initialIndex: this.list.length - 1, space: 10 }) {
          ForEach(this.list, (item: string) => {
            ListItem() {
              Row() {
                Text(item);
              }
              .backgroundColor('#F1F3F5')
              .borderRadius(8)
              .justifyContent(FlexAlign.Center)
              .padding(24)
              .width('95%')
              .onClick(() => {
                this.getUIContext().getPromptAction().showToast({ message: item });
              });
            }
            .width('100%')
            .padding(2)
            .bindContextMenu(this.menu(), ResponseType.LongPress, {
              preview: () => {
              },
            });
          });
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .width('100%')
        .height('100%');
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/0HLON65BTju27BnaYdX-ZQ/zh-cn_image_0000002628400332.png "点击放大")
* 方案二：bindContextMenu可以通过绑定一个状态变量来控制菜单的显隐，代码案例如下：

  ```ts
  @Entry
  @Component
  struct Index1 {
    private scroller = new Scroller();
    private list: string[] = [];
    @State flag: boolean[] = new Array(10).fill(false);

    aboutToAppear(): void {
      for (let i = 0; i < 15; i++) {
        this.list.push(i + '');
      }
    }

    @Builder
    menu() {
      Menu() {
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单1' });
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单2' });
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单3' });
      };
    }

    build() {
      Column() {
        List({ scroller: this.scroller, initialIndex: this.list.length - 1, space: 10 }) {
          ForEach(this.list, (item: string, index: number) => {
            ListItem() {
              Row() {
                Text(item);
              }
              .backgroundColor('#F1F3F5')
              .borderRadius(8)
              .justifyContent(FlexAlign.Center)
              .padding(24)
              .width('95%')
              .onClick(() => {
                if (this.flag.some(Boolean)) {
                  return;
                }
                this.getUIContext().getPromptAction().showToast({ message: item });
              });
            }
            .width('100%')
            .padding(2)
            // 长按手势，将控制菜单显隐的值修改为true
            .gesture(LongPressGesture().onAction(event => {
              console.info(`${event}`);
              this.flag[index] = true;
            }))
            // 绑定菜单
            .bindContextMenu(!!this.flag[index], this.menu(), {
              onDisappear: () => {
                this.flag[index] = false;
              }
            });
          });
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .width('100%')
        .height('100%');
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/BLtg_z8pSVuduxb-s220HA/zh-cn_image_0000002658799599.png "点击放大")
* 方案三：popup气泡弹窗默认会带一个透明蒙层，可以使用popup气泡弹窗模拟菜单弹窗。

  ```ts
  @Entry
  @Component
  struct Index2 {
    private scroller = new Scroller();
    private list: string[] = [];
    @State flag: boolean[] = new Array(10).fill(false);

    aboutToAppear(): void {
      for (let i = 0; i < 15; i++) {
        this.list.push(i + '');
      }
    }

    @Builder
    menu(index: number) {
      Menu() {
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单1' })
          .onClick(() => {
            this.flag[index] = false;
          });
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单2' });
        MenuItem({ startIcon: $r('app.media.startIcon'), content: '菜单3' });
      };
    }

    build() {
      Column() {
        List({ scroller: this.scroller, initialIndex: this.list.length - 1, space: 10 }) {
          ForEach(this.list, (item: string, index: number) => {
            ListItem() {
              Row() {
                Text(item);
              }
              .backgroundColor('#F1F3F5')
              .borderRadius(8)
              .justifyContent(FlexAlign.Center)
              .padding(24)
              .width('95%')
              .onClick(() => {
                this.getUIContext().getPromptAction().showToast({ message: item });
              });
            }
            .width('100%')
            .padding(2)
            // 长按手势，将控制菜单显隐的值修改为true
            .gesture(LongPressGesture().onAction(() => {
              this.flag[index] = true;
            }))
            // 通过Popup气泡弹窗来模拟一个菜单
            .bindPopup(!!this.flag[index], {
              enableArrow: false,
              mask: true, // 设置蒙层，默认值为true.也可以设置蒙层颜色
              builder: this.menu(index),
              onWillDismiss: () => {
                this.flag[index] = false;
              }
            });
          });
        }
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
        .width('100%')
        .height('100%');
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/FZ3VCm1CSY-u034bXXq0ng/zh-cn_image_0000002628560240.png "点击放大")
