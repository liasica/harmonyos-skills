---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0020
title: ArkUI自定义弹窗功能实现与控制常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI自定义弹窗功能实现与控制常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:19c5e6a57e22e69aafa0c8e74a8ba775485dfc8c7912df4dda1415a27fdfa573
---

**Q：利用this.getUIContext().getPromptAction().openCustomDialog打开自定义弹窗，并且给dialog设置宽高100%依旧无法全屏，问题效果预览：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Sw7qsnzsSn-hbqibQFcwew/zh-cn_image_0000002767995142.png "点击放大")

**A**：解决方法如下：

1. 在EntryAbility中设置窗口全屏：

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       let windowClass: window.Window = windowStage.getMainWindowSync();
       // 1.设置窗口全屏
       let isLayoutFullScreen = true;
       windowClass.setWindowLayoutFullScreen(isLayoutFullScreen)
         .then(() => {
           console.info('Succeeded in setting the window layout to full-screen mode.');
         });
       // 2.设置状态栏和导航条隐藏
       windowClass.setSpecificSystemBarEnabled('status', false)
         .then(() => {
           console.info('Succeeded in setting the status bar to be invisible.');
         })
         .catch((err: BusinessError) => {
           console.error(`Failed to set the status bar to be invisible. Code is ${err.code}, message is ${err.message}`);
         });

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     }
   };
   ```
2. 把自定义弹窗的窗口高度设置为设备的屏幕高度displayHeight：

   ```ts
   import { display, PromptAction } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     private customDialogComponentId: number = 0;
     private promptAction: PromptAction = this.getUIContext().getPromptAction();
     @State displayHeight: number = 0;

     aboutToAppear() {
       this.displayHeight = this.getUIContext().px2vp(display.getDefaultDisplaySync().height);
     }

     @Builder
     customDialogComponent() {
       Column() {
         Text('弹窗').fontSize(30).margin({ top: 50});
         Row({ space: 50 }) {
           Button('取消')
             .backgroundColor(Color.Transparent)
             .fontColor('#0A59f7')
             .width('38%')
             .onClick(() => {
               this.promptAction.closeCustomDialog(this.customDialogComponentId);
             });
           Button('确认')
             .width('38%')
             .onClick(() => {
               this.promptAction.closeCustomDialog(this.customDialogComponentId);
             });
         };
       }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween);
     }

     build() {
       Row() {
         Column({ space: 20 }) {
           Text('组件内弹窗')
             .fontSize(30)
             .onClick(() => {
               this.promptAction.openCustomDialog({
                 builder: () => {
                   this.customDialogComponent();
                 },
                 width: '100%',
                 height: this.displayHeight,
               }).then((dialogId: number) => {
                 this.customDialogComponentId = dialogId;
               });
             });
         }
         .width('100%');
       }
       .height('100%');
     }
   }
   ```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/FXFkLcK6SgWyf02cuFQeMQ/zh-cn_image_0000002767836862.png "点击放大")

**Q：如何给自定义弹窗使用CustomBuilder，实现下图的功能，且确认取消按钮需要一个带有倒计时的功能，倒计时结束后才能点击。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ylgylLE_TnOAsXluvi5mFA/zh-cn_image_0000002797157915.png "点击放大")

**A**：实现弹窗按钮计时禁用效果步骤如下：

1. 使用@Builder创建自定义的组件，传入自定义的弹窗组件。
2. 使用状态变量isEnabled，初始为false，设置按钮是否禁用。
3. 设置定时器，实现倒计时功能。当计时结束时，isEnabled为true，并清除计时器。
4. 当弹窗关闭时，触发onWillDismiss回调，isEnabled为false，并重置定时功能。

代码如下：

```ts
@Entry
@Component
struct BuildPage {
  @State time: number = 3;
  @State isEnabled: boolean = false;
  private customDialogComponentId: number = 0;

  timeout() {
    let intervalID = setInterval(() => {
      this.time--;
      if (this.time === 0 || this.time < 0) {
        this.isEnabled = true;
        clearInterval(intervalID);
      }
    }, 1000);
  }

  @Builder
  customDialogComponent() {
    Column({ space: 10 }) {
      Row() {
        Text('标题')
      }
      .width('100%')
      .margin({ top: 10 })
      .justifyContent(FlexAlign.Center)

      Text('我们会不时修订本隐私权政策。未经您明确同意，我们不会减降您按照本隐私权政策的规定所享有的权利')
        .width('80%')
      Row() {
        Button(this.time === 0 || this.time < 0 ? '我已知悉' : `(${this.time})`)
          .enabled(this.isEnabled)
          .width(80)
          .onClick(() => {
            this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          })
      }.width('100%')
      .height(100)
      .justifyContent(FlexAlign.SpaceAround)
      .alignItems(VerticalAlign.Center)
    }.width('100%')
  }

  @Builder
  buildAlertDialog() {
    Column() {
      Row() {
        Text('组件内弹窗')
          .fontSize(30)
          .onClick(() => {
            this.timeout();
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
              onWillAppear: () => {
                this.time = 3;
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                // 时间归零前，禁止关闭弹窗
                if (this.time <= 0) {
                  dismissDialogAction.dismiss();
                }
              },
              onWillDisappear: () => {
                this.isEnabled = false;
              }
            })
              .then((dialogId: number) => {
                this.customDialogComponentId = dialogId;
              });
          })
      }.width('100%')
      .justifyContent(FlexAlign.SpaceAround)
    }
  }

  build() {
    Row() {
      this.buildAlertDialog();
    }
    .height('100%')
  }
}
```

**Q：PromptAction自定义弹窗如何实现在点击弹窗外围的蒙层时，弹窗不关闭？**

**A**：实现PromptAction弹窗禁用点击蒙层隐藏弹窗功能时，只需要在onWillDismiss内控制关闭信息：在dismissDialogAction.reason !== DismissReason.TOUCH\_OUTSIDE条件下调用dismiss()关闭函数即可，在该条件下除了点击蒙层不关闭弹窗外，其他关闭条件都不影响。

```ts
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  private customDialogComponentId: number = 0;

  @Builder
  customDialogComponent() {
    Column() {
      Text('弹窗').fontSize(30)
      Row({ space: 50 }) {
        Button('确认').onClick(() => {
          this.promptAction.closeCustomDialog(this.customDialogComponentId);
        })
        Button('取消').onClick(() => {
          this.promptAction.closeCustomDialog(this.customDialogComponentId);
        })
      }
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }

  build() {
    Row() {
      Column() {
        Button('click me')
          .onClick(() => {
            this.promptAction.openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                if (dismissDialogAction.reason !== DismissReason.TOUCH_OUTSIDE) {
                  dismissDialogAction.dismiss();
                }
              }
            }).then((dialogId: number) => {
              this.customDialogComponentId = dialogId;
            });
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/hSd3HGfaQGG1efNjsBGj1Q/zh-cn_image_0000002797281409.png "点击放大")

**Q：当弹窗内容高度不确定时，如何实现动态高度、最大高度限制以及滚动体验？**

**A**：实现方式如下：

1. 弹窗外层包裹滚动容器。
   * 使用Scroll作为根容器，设置滚动方向为垂直（ScrollDirection.Vertical）。
   * 通过.scrollBar(BarState.On)启用滚动条，提升交互可视性。
2. 动态高度与最大高度限制。
   * 不固定高度：弹窗内部组件（如Column/Row）不设置固定高度。
   * 约束最大高度：用constraintSize限制Scroll组件的最大高度。
3. 滚动行为优化。
   * 禁用边缘效果：设置[edgeEffect](../harmonyos-references/ts-container-scroll.md#edgeeffect)属性的值为None避免滚动到边缘时有滑动效果。
4. 弹窗控制逻辑。
   * 通过PromptAction打开/关闭弹窗，绑定自定义组件ID实现精准控制。
   * 处理物理返回键/点击外部关闭：重写[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中的onWillDismiss方法拦截DismissReason.PRESS\_BACK和DismissReason.TOUCH\_OUTSIDE。

完整代码：

```ts
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct customDialogScroll {
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  private customDialogComponentId: number = 0; // 弹窗ID，用于关闭时定位
  scroller: Scroller = new Scroller(); // 滚动控制器

  // 自定义弹窗UI
  @Builder
  customDialogComponent() {
    Column() {
      Text('弹窗标题')
        .fontSize(30)
        .padding({ top: 10, bottom: 10 });
      Scroll(this.scroller) {
        Column() {
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
          Text('这里是弹窗内容区域，可根据内容变化高度这里是弹窗内容区域，可根据内容变化高度');
        }
        .padding({left:15,right:15})
        .backgroundColor('rgba(246, 244, 244, 1.00)')
        .width('100%'); // 模拟动态内容
      }
      .scrollable(ScrollDirection.Vertical) // 启用垂直滚动
      .scrollBar(BarState.On)
      .constraintSize({ maxHeight: 100 }) //核心：限制最大高度
      .edgeEffect(EdgeEffect.None); // 禁用边缘效果
      Flex({direction:FlexDirection.Row,justifyContent:FlexAlign.SpaceEvenly,alignItems:ItemAlign.Center}){
        Button('取消')
          .fontColor('#0a59f7')
          .backgroundColor(Color.White)
          .backgroundColor('rgba(246, 244, 244, 1.00)')
          .onClick(() => this.closeDialog());
        Row()
          .width(1)
          .height(15)
          .backgroundColor(Color.Gray)
          .opacity(0.5)
        Button('确认')
          .fontColor('#0a59f7')
          .backgroundColor('rgba(246, 244, 244, 1.00)')
          .onClick(() => this.closeDialog());
      }

      .margin({ top: 8, bottom: 8 });
    }.backgroundColor('rgba(246, 244, 244, 1.00)');

  }

  // 关闭弹窗方法
  private closeDialog() {
    this.promptAction.closeCustomDialog(this.customDialogComponentId);
  }

  build() {
    Row() {
      Column() {
        Button('打开弹窗')
          .onClick(() => {
            this.promptAction.openCustomDialog({
              builder: () => this.customDialogComponent(), // 绑定UI构建器
              onWillDismiss: (action: DismissDialogAction) => {
                // 处理物理返回键/点击外部关闭
                if (action.reason === DismissReason.PRESS_BACK ||
                  action.reason === DismissReason.TOUCH_OUTSIDE) {
                  action.dismiss(); // 执行关闭
                }
              }
            }).then((dialogId: number) => {
              this.customDialogComponentId = dialogId; // 保存弹窗ID
            });
          });
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center);
    };
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/-m_bm02vRaaWtOe9AZre5g/zh-cn_image_0000002768004588.png "点击放大")

**Q：对于一个弹窗，如何使用非交互方式关闭，即支持使用代码关闭它，不是用户触摸屏幕操作关闭？**

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/mGGWr12gSK6cJoFuiqUbCw/zh-cn_image_0000002797286381.png "点击放大")

A：在aboutToAppear生命周期中调用setInterval方法实现一个倒计时功能，在倒计时结束后调用[关闭弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md#close)的方法并清理interval任务。

1. 注册自定义弹窗的onWillDismiss回调函数，并在回调内拦截用户操作关闭弹窗。

   ```ts
   dialogController: CustomDialogController | null = new CustomDialogController({
       builder: AutoCloseCustomDialog({
         cancel: ()=> { this.onCancel(); },
         confirm: ()=> { this.onAccept(); },
         timeout: 5
       }),
       cancel: this.existApp,
       autoCancel: true,
       onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
         // 拦截三键back关闭弹窗
         if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
         }
         // 拦截点击遮障层关闭弹窗
         if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
         }
       },
       alignment: DialogAlignment.Center,
       offset: { dx: 0, dy: -20 },
       customStyle: false,
       cornerRadius: 20,
       borderColor: Color.Blue,
       backgroundColor: Color.White
     });
   ```
2. aboutToAppear生命周期中通过setInterval方式对关闭按钮进行倒计时。

   ```ts
   aboutToAppear(): void {
       this.interval = setInterval(() => {
         // 倒计时结束，调用关闭弹窗方法并取消interval任务
         if (this.timeout <= 1) {
           this.closeDialog();
           return;
         }
         this.timeout -= 1;
         console.info(`interval timeout = ${this.timeout}`);
       }, 1000);
     }
   ```

完整示例参考如下：

```ts
@CustomDialog
@Component
struct AutoCloseCustomDialog {
  @State timeout: number = 10;
  interval: number = 0;
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  // 生命周期中通过setInterval方式对关闭按钮进行倒计时
  aboutToAppear(): void {
    this.interval = setInterval(() => {
      // 倒计时结束，调用关闭弹窗方法并取消interval任务
      if (this.timeout <= 1) {
        this.closeDialog();
        return;
      }
      this.timeout -= 1;
      console.info(`interval timeout = ${this.timeout}`);
    }, 1000);
  }
  closeDialog() {
    // 取消interval任务
    clearInterval(this.interval);
    // 关闭自定义弹窗
    this.controller?.close();
    console.info(`closeDialog success and interval = ${this.interval}`);
  }

  build() {
    Column() {
      Text('这是个可以自动关闭的自定义弹窗').textTitleExtend()

      Text('关闭' + this.timeout + 's')
        .textButtonExtend()
        .onClick(() => {
          if (this.controller !== undefined) {
            this.controller.close();
            // 手动关闭，取消interval任务
            clearInterval(this.interval);
          }
        });
    }
    .height(150)
    .justifyContent(FlexAlign.SpaceEvenly)
  }
}

@Extend(Text)
function textButtonExtend() {
  .fontFamily("HarmonyHeiTi")
  .fontColor("#0A59F7")
  .fontSize(16)
  .fontWeight(500)
  .lineHeight(21)
  .textAlign(TextAlign.Center);
}

@Extend(Text)
function textTitleExtend() {
  .fontFamily("HarmonyHeiTi")
  .fontColor($r('sys.color.black'))
  .fontSize(16)
  .fontWeight(500)
  .lineHeight(21)
  .textAlign(TextAlign.Center);
}

@Entry
@Component
struct AutoCloseCustomDialogIndex {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: AutoCloseCustomDialog({
      cancel: ()=> { this.onCancel(); },
      confirm: ()=> { this.onAccept(); },
      timeout: 5
    }),
    cancel: this.existApp,
    autoCancel: true,
    onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
      // 拦截三键back关闭弹窗
      if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
      }
      // 拦截点击遮障层关闭弹窗
      if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    customStyle: false,
    cornerRadius: 20,
    borderColor: Color.Blue,
    backgroundColor: Color.White
  });
  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    // 将dialogController置空
    this.dialogController = null;
  }

  onCancel() {
    console.info('Callback when the first button is clicked');
  }

  onAccept() {
    console.info('Callback when the second button is clicked');
  }

  existApp() {
    console.info('Click the callback in the blank area');
  }

  build() {
    Column() {
      Button('click me')
        .backgroundColor(0x317aff)
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        });
    }
    .width('100%')
    .margin({ top: 5 })
  }
}
```
