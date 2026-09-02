---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1365
title: 如何实现Video组件画面尺寸跟随半模态页面bindSheet的尺寸同步变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Video组件画面尺寸跟随半模态页面bindSheet的尺寸同步变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7a919e4ce8c0f811082f16413c6f99ca5e7fcf3127f5f44abca5b9a2cc76e84e
---

## 问题现象

如何实现Video组件的预览图或播放内容随着半模态页面的拉起、关闭和跟手滑动时同步变化。

## 背景知识

* [Video组件](../harmonyos-references/ts-media-components-video.md)用于播放视频文件并控制视频播放状态，可以实现简单的视频播放功能。Video的画面填充模式可以通过设置不同的[objectFit](../harmonyos-references/ts-media-components-video.md#objectfit)属性值改变。
* 通用属性[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)可以为组件绑定半模态页面，拉起时显示模态页面。半模态页面可以在绑定时通过[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)的多个参数设置页面的属性和回调。
* 通用属性[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)、[onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)均可以监听组件的尺寸变化，并执行回调中的动作。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)是[导航根容器Navigation](../harmonyos-references/ts-basic-components-navigation.md)的子页面根容器，用于显示Navigation的内容区。通过属性mode设置NavDestination的类型，可以将其设置为弹窗模式NavDestinationMode.DIALOG，该模式下NavDestination背景默认透明，其进出路由栈时不影响下层NavDestination的生命周期。
* [从UI内部使用LocalStorage](../harmonyos-guides/arkts-localstorage.md#从ui内部使用localstorage)时，使用@Entry装饰器将LocalStorage实例添加到组件中。
* [手势处理](../harmonyos-references/gesture-handling.md)可以让被绑定的组件识别点击、长按、滑动平移、捏合、旋转等多种手势，并根据手势动作执行回调动作。

## 解决方案

* 方案一、bindSheet半模态页面。可以通过以下步骤实现：
  1. 通过onAreaChange获取外部容器的高度。
  2. Video组件设置objectFit属性为ImageFit.Contain，使画面内容保持宽高比，在边界内完全显示；同时设置组件的高度为随半模态页面高度动态变化。
  3. 容器设置半模态页面，并设置为跟手页面，通过shouldDismiss、onHeightDidChange和onWillAppear等回调，动态记录页面高度。

  完整示例代码如下，示例代码中使用了API 18中新增属性[PosterOptions](../harmonyos-references/ts-media-components-video.md#posteroptions18对象说明)和参数[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions).placement：

  ```ts
  @Entry
  @Component
  export struct VideoBindSheet {
    @State videoSrc: Resource = $rawfile('harmonyos-next-pv-video-popup.mp4'); // 资源更换为实际视频
    @State previewUri: Resource = $r('app.media.img'); // 资源更换为实际预览图
    @State curSpeed: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
    @State showFirstFrame: boolean = false;
    @State showBindSheet: boolean = false;
    @State containerHeight: number | undefined = undefined;
    @State sheetHeight: number = 0;
    controller: VideoController = new VideoController();

    // 半模态页面
    @Builder
    bindSheetBuilder() {
      Column() {
        Text('Comment')
          .height(200)
          .width('100%')
          .textAlign(TextAlign.Center)
          .fontSize('30fp');

        TextInput({ placeholder: 'comment' })
          .width('95%')
          .fontSize('18fp')
          .type(InputType.Normal);
      };
    }

    build() {
      Column() {
        Column() {
          Video({
            src: this.videoSrc,
            previewUri: this.previewUri,
            currentProgressRate: this.curSpeed,
            controller: this.controller,
            posterOptions: { showFirstFrame: this.showFirstFrame }
          })
            .width('100%')
            .height(this.containerHeight === undefined ? '100%' :
              this.containerHeight - this.sheetHeight) // 首次布局时撑满容器，后续随半模态页面高度变化
            .objectFit(ImageFit.Contain) // 边界内完全显示
            .onFinish(() => {
              this.controller.reset();
            });

          Button('Comment')
            .type(ButtonType.Capsule)
            .position({ right: 10, bottom: 50 + this.sheetHeight })
            .onClick(() => {
              // 拉起半模态页面
              this.showBindSheet = true;
            });
        }
        .height('100%')
        .width('100%')
        .bindSheet(
          !!this.showBindSheet,
          this.bindSheetBuilder(),
          {
            height: 450,
            preferType: SheetType.POPUP, // 跟手弹窗
            showClose: true,
            placement: Placement.Bottom, // 底部弹窗
            shouldDismiss: () => {
              // 页面交互式关闭时，修改显示状态为false，半模态页面高度重置为0
              this.showBindSheet = false;
              this.sheetHeight = 0;
            },
            onHeightDidChange: (height: number) => {
              // 根据每一帧高度，动态修改页面高度，需注意处理导航栏高度，导航栏高度为91px或28vp；若页面不显示，则重置为0
              this.sheetHeight = this.getUIContext().px2vp(height - 91);
              if (!this.showBindSheet) {
                this.sheetHeight = 0;
              }
            },
            onWillAppear: () => this.sheetHeight = 422 // 半模态页面高度450vp，需避让导航栏高度28vp，实际Video抬起高度为422vp
          }
        )
        .onAreaChange((oldValue, newValue) => {
          console.info(`Old Height: ${oldValue.height}`);
          // 获取容器高度
          this.containerHeight = newValue.height as number;
        });
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .expandSafeArea([SafeAreaType.SYSTEM])
      .backgroundColor(Color.Black);
    }
  }
  ```

  效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/6L665a91TXm7rwZr0u0ATg/zh-cn_image_0000002658841301.png "点击放大")
* 方案二、Navigation配合NavDestinationMode.DIALOG。可以通过以下步骤实现：
  1. 根页面使用Navigation容器，并设置为单栏模式。后续步骤需要记录弹窗高度且在页面级UI存储，使用LocalStorage创建新实例并初始化，Entry页面添加storage。
  2. Video页面使用NavDestination子页面容器，并获取内部组件高度。按钮组件跳转弹窗页面。
  3. Video组件设置objectFit属性为ImageFit.Contain，使画面内容保持宽高比，在边界内完全显示；同时设置组件的高度为随半模态页面高度动态变化。
  4. 弹窗页面使用NavDestination子页面容器，并设置为弹窗模式NavDestinationMode.DIALOG。下层使用Stack组件添加遮罩，当点击遮罩时可收起弹窗。
  5. 弹窗内容区顶部设置组件，并绑定顺序识别的手势组合（长按手势LongPressGesture与滑动手势PanGesture），在滑动手势识别后，根据纵向滑动的偏移值，动态修改弹窗高度。当弹窗页面退出路由栈时，弹窗高度重置为0。

  完整示例代码如下，示例代码中使用了API 18中新增属性[PosterOptions](../harmonyos-references/ts-media-components-video.md#posteroptions18对象说明)：

  ```ts
  import { window, KeyboardAvoidMode } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';

  // 创建LocalStorage实例并初始化
  let para: Record<string, number> = { 'dialogHeight': 0 };
  let storage: LocalStorage = new LocalStorage(para);

  // NavDestination组件构造函数
  @Builder
  function pageBuilder(name: string) {
    if (name === 'VideoPage') {
      VideoPage();
    } else if (name === 'CommentPage') {
      CommentPage();
    } else if (name === 'PersonPage') {
      PersonPage();
    }
  }

  // Entry页面添加storage
  @Entry(storage)
  @Component
  export struct VideoNavigation {
    @Provide pageInfos: NavPathStack = new NavPathStack();

    build() {
      Navigation(this.pageInfos) {
        Column() {
          Button('跳转Video')
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'VideoPage', param: this.pageInfos }); // 跳转至Video组件页面
            });
        }
        .height(200)
        .justifyContent(FlexAlign.Center);
      }
      .hideTitleBar(true)
      .mode(NavigationMode.Stack) // 单栏模式
      .navDestination(pageBuilder); // 创建NavDestination组件
    }
  }

  // Video页面
  @Component
  struct VideoPage {
    @Consume pageInfos: NavPathStack = new NavPathStack();
    controller: VideoController = new VideoController();
    @State videoSrc: Resource = $rawfile('harmonyos-next-pv-video-popup.mp4'); // 资源更换为实际视频
    @State previewUri: Resource = $r('app.media.img'); // 资源更换为实际预览图
    @State curSpeed: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
    @State showFirstFrame: boolean = false;
    @State containerHeight: number | undefined = undefined;
    @LocalStorageLink('dialogHeight') dialogHeight: number = 0; // 与LocalStorage中对应属性建立双向绑定

    build() {
      NavDestination() {
        Column() {
          Video({
            src: this.videoSrc,
            previewUri: this.previewUri,
            currentProgressRate: this.curSpeed,
            controller: this.controller,
            posterOptions: { showFirstFrame: this.showFirstFrame }
          })
            .width('100%')
            // 首次布局时撑满容器，后续随半模态页面高度变化
            .height(this.containerHeight === undefined ? '100%' : this.containerHeight - this.dialogHeight)
            .objectFit(ImageFit.Contain) // 边界内完全显示
            .onFinish(() => {
              this.controller.reset();
            });

          Button('Comments')
            .type(ButtonType.Capsule)
            .position({ right: 10, bottom: 50 + this.dialogHeight })
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'CommentPage' }); // 跳转至弹窗页面
            });
        }
        .height('96%')
        .onAreaChange((oldValue, newValue) => {
          console.info(`Old Height: ${oldValue.height}`);
          this.containerHeight = newValue.height as number; // 获取容器高度
        });
      }
      .height('100%')
      .hideTitleBar(true)
      .hideToolBar(true)
      .backgroundColor(Color.Black)
      .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM]);
    }
  }

  // 弹窗页面
  @Component
  struct CommentPage {
    @Consume pageInfos: NavPathStack;
    @LocalStorageLink('dialogHeight') dialogHeight: number = 0; // 与LocalStorage中对应属性建立双向绑定
    @State preHeight: number = 0;
    @State commentContainerHeight: number | undefined = undefined;
    @State keyboardHeight: number = 0;
    private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    aboutToAppear(): void {
      window.getLastWindow(this.context, (err, currentWindow) => {
        currentWindow.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.NONE); // 不避让键盘
        currentWindow.on('keyboardHeightChange', (data) => {
          let keyboardHgt = this.getUIContext().px2vp(data); // 获取键盘高度
          this.keyboardHeight = keyboardHgt - 28; // 获取避让高度，28为导航栏高度
        });
        console.info(`err: ${err.message}`);
      });
    }

    build() {
      NavDestination() {
        Stack({ alignContent: Alignment.Bottom }) {
          Column() {
            Text('Slips Area')
              .fontSize('16fp')
              .textAlign(TextAlign.Center)
              .width('100%')
              .backgroundColor(Color.Gray)
              .borderColor({ bottom: Color.Black })
              .gesture(
                // 顺序识别手势组合
                GestureGroup(GestureMode.Sequence,
                  LongPressGesture({ repeat: true, duration: 100 }), // 长按手势
                  PanGesture({ direction: PanDirection.Vertical }) // 滑动手势，识别纵向滑动
                    .onActionStart(() => {
                      this.preHeight = this.dialogHeight; // 当前弹窗高度
                    })
                    .onActionUpdate((event) => {
                      // 动态修改弹窗高度，通过LocalStorage同步传入Video页面，以修改Video组件高度
                      this.dialogHeight = this.preHeight - event.offsetY;
                      // 动态修改外容器高度
                      this.commentContainerHeight = this.dialogHeight;
                    })
                )
              );

            Column({ space: 24 }) {
              TextInput({ placeholder: 'My Comment' })
                .fontSize('18fp')
                .type(InputType.Normal)
                .width('92%')
                .offset({ bottom: this.keyboardHeight }); // 输入框偏移避让高度

              Button('Persons')
                .onClick(() => {
                  this.pageInfos.pushPath({ name: 'PersonPage' }); // 跳转至人员页面
                });

              Text('Comments')
                .fontSize('30fp')
                .textAlign(TextAlign.Center)
                .height(200)
                .width('100%');
            }
            .layoutWeight(1)
            .padding({ bottom: 48 })
            .reverse(true);
          }
          .height(this.commentContainerHeight ?? '60%')
          .backgroundColor(Color.White)
          .onAreaChange((oldValue, newValue) => {
            console.info(`Old Height: ${oldValue.height}`);
            this.dialogHeight = newValue.height as number; // 获取弹窗高度
            this.commentContainerHeight = this.dialogHeight; // 获取外容器高度
          });
        }
        .height('100%')
        .backgroundColor(Color.Transparent)
        .onClick(() => {
          this.pageInfos.pop(); // 点击遮罩层，弹窗页面弹出路由栈
        });
      }
      .mode(NavDestinationMode.DIALOG) // 弹窗模式
      .hideTitleBar(true)
      .onWillDisappear(() => {
        this.dialogHeight = 0;
      })
      .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM]);
    }
  }

  // 人员页面
  @Component
  struct PersonPage {
    @Consume pageInfos: NavPathStack;

    build() {
      NavDestination() {
        Column() {
          Text('Person Page')
            .fontSize('30fp');
        }
        .height(300)
        .justifyContent(FlexAlign.Center)
        .onClick(() => {
          this.pageInfos.pop(); // 当前页面弹出路由栈
        });
      };
    }
  }
  ```

  效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/QAKJ6OozRL2ufTWq94wz_Q/zh-cn_image_0000002628602034.png "点击放大")
