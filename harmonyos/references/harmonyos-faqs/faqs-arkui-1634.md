---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1634
title: 弹窗无法通过侧滑关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 弹窗无法通过侧滑关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b79510c2436cf578dfe8cff5edfba0f4e3e45c653ca81548756f330e65394664
---

## 问题现象

侧滑无法关闭弹窗，侧滑时无响应或是主页面返回上一级。

## 背景知识

* [windowStage.createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9-1)：创建该WindowStage实例下的子窗口。
* [window.destroyWindow](../harmonyos-references/arkts-apis-window-window.md#destroywindow9)：销毁当前窗口。
* [onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：当用户侧滑时触发。返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。
* [CustomDialogControllerOptions对象说明](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)：自定义弹窗的样式。其中onWillDismiss为交互式关闭回调函数。当用户执行点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。

## 问题定位

### 场景一

子窗口侧滑无响应。

1. 侧滑时输出如下日志，从日志可知消费侧滑事件的窗口不是主窗口，这种窗口是通过windowStage.createSubWindow创建的子窗口。

   ```shell
   I     [(-1:100001:active)] [com.example.myapplication][entry][100001]: OnBackPressed called
   W     [(-2:100001:active)] Fail to find subwindow in subwindowMap_, instanceId is 100001.
   E     (82)GetSingleton: can not get OHOS::Rosen::WindowInfoReporter
   I     (2888)PerformBack: PerformBack is not MainWindow, return
   ```
2. 检查子窗口是否重写onBackPress方法主动销毁子窗口。

### 场景二

弹窗组件侧滑无响应。

1. 日志过滤backPress，看到侧滑事件是被Overlay消费的，即叠加层，一般是一些弹窗组件。

   ```shell
   [(-1:100000:singleton)] [com.example][entry][100000]: OnBackPressed called
   [(100000:100000:scope)] Overlay consumed backpressed event
   ```
2. 排查弹窗组件是否注册onWillDismiss回调函数，检查拦截逻辑，看到应用只对下拉操作进行了处理。

   ```ts
   onWillDismiss:(dismissDialogAction: DismissDialogAction)=> {
     // 下拉
     if (dismissDialogAction.reason == DismissReason.SLIDE_DOWN) {
       // 关闭弹窗
       dismissDialogAction.dismiss()
     }
   }
   ```

   关闭原因类型：

   | 名称 | 值 | 描述 |
   | --- | --- | --- |
   | PRESS\_BACK | 0 | 点击三键back、左滑/右滑、键盘ESC。 |
   | TOUCH\_OUTSIDE | 1 | 点击遮障层时。 |
   | CLOSE\_BUTTON | 2 | 点击关闭按钮。 |
   | SLIDE\_DOWN | 3 | 下拉关闭。该接口仅支持在半模态转场中使用。 |

### 场景三

侧滑未关闭弹出框，而是主页面返回上一级。

1. 在日志中搜索onBackPress，可以看到onBackPress return true，说明应用重写了onBackPress方法。
2. 通过DevEco Testing查看页面，发现页面由JsView构成。商品页和评论区在同一个根节点上。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/XJW_lcbSQYWCRerBSDAw6g/zh-cn_image_0000002628777548.png "点击放大")
3. 在侧滑关闭弹窗前，通过日志发现焦点聚焦在了Column下的子节点，此时侧滑逻辑由主页面的onBackPress方法确定。因此是主页面onBackPress方法内逻辑错误，未优先关闭弹出框而是返回了上一级。

   ```shell
   12-16 15:06:11.905   64077-64077   C0391C/应用包名/AceFocus         应用包名     I     [(100001:100001:scope)] Lost focus to view root: Column
   12-16 15:06:11.905   64077-64077   C0391C/应用包名/AceFocus         应用包名     I     [(100001:100001:scope)] FocusSwitch end, Column/secure_field onBlur, Column/secure_field onFocus, start: 3, end: 1, update: 0
   12-16 15:06:11.905   64077-64077   C03933/应用包名/AceKeyboard      应用包名     I     [(100001:100001:scope)] current focus node: (Column/14). isDynamic: 0
   ```

## 分析结论

### 场景一

因为未在子窗口重写onBackPress，应用会执行默认的路由返回逻辑，由于子窗口没有可返回的上一页，所以无响应。

### 场景二

弹窗组件注册了onWillDismiss回调函数，然而未对侧滑场景做处理。

### 场景三

焦点聚焦在主页面，而主页面重写的onBackPress方法内逻辑错误，未优先关闭弹出框而是返回了上一级。

## 修改建议

### 场景一

在onBackPress方法中，调用destroyWindow主动销毁子窗口。

* EntryAbility.ets文件中配置如下，设置MainPage为主窗口，并存储windowStage至AppStorage。

  ```ts
  import { window } from '@kit.ArkUI';
  import { UIAbility } from '@kit.AbilityKit';

  export default class EntryAbility extends UIAbility {
    onDestroy(): void {
      console.info('Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage) {
      console.info('Ability onWindowStageCreate');

      windowStage.loadContent('pages/MainWindow', (err) => {
        if (err.code) {
          console.error('Failed to load the content.');
          return;
        }
        console.info('Succeeded in loading the content.');
      });
      AppStorage.setOrCreate('windowStage', windowStage);
    }

    onWindowStageDestroy(): void {
      console.info('Ability onWindowStageDestroy');
    }

    onForeground(): void {
      console.info('Ability onForeground');
    }

    onBackground(): void {
      console.info('Ability onBackground');
    }
  }
  ```
* MainPage.ets文件配置如下，获取AppStorage中的windowStage并通过createSubWindow创建该WindowStage实例下的子窗口，同时存储subWindowClass至AppStorage。

  ```ts
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  let windowStage: window.WindowStage | undefined = undefined;
  let subWindowClass: window.Window | undefined = undefined;

  @Entry
  @Component
  struct MainWindow {
    message: string = 'Hello World';

    onBackPress(): boolean | void {
      this.destroySubWindow();
      return false;
    }

    private createSubWindow() {
      // 获取windowStage
      windowStage = AppStorage.get('windowStage');
      // 1.创建应用子窗口。
      if (windowStage == null) {
        console.error('Failed to create the subwindow. Cause: windowStage_ is null');
      } else {
        windowStage.createSubWindow('mySubWindow', (err: BusinessError, data) => {
          if (err.code) {
            console.error('Failed to create the subwindow. Cause: ' + JSON.stringify(err));
            return;
          }
          subWindowClass = data;
          AppStorage.setOrCreate('subWindowClass', subWindowClass);
          if (!subWindowClass) {
            console.error('sub_windowClass is null');
            return;
          }
          console.info('Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
          // 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
          subWindowClass.moveWindowTo(380, 900, (err: BusinessError) => {
            let errCode: number = err.code;
            if (errCode) {
              console.error('Failed to move the window. Cause:' + JSON.stringify(err));
              return;
            }
            console.info('Succeeded in moving the window.');
          });
          subWindowClass.resize(500, 500, (err: BusinessError) => {
            let errCode: number = err.code;
            if (errCode) {
              console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
              return;
            }
            console.info('Succeeded in changing the window size.');
          });
          // 3.为子窗口加载对应的目标页面。
          subWindowClass.setUIContent('pages/SubWindow', (err: BusinessError) => {
            if (err.code) {
              console.error('Failed to load the content. Cause:' + JSON.stringify(err));
              return;
            }
            console.info('Succeeded in loading the content.');
            if (!subWindowClass) {
              console.error('sub_windowClass is null');
              return;
            }
            // 3.显示子窗口。
            subWindowClass.showWindow((err: BusinessError) => {
              if (err.code) {
                console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
                return;
              }
              console.info('Succeeded in showing the window.');
            });
          });
        });
      }
    }

    private destroySubWindow() {
      if (!subWindowClass) {
        console.error('sub_windowClass is null');
        return;
      }
      // 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
      subWindowClass.destroyWindow((err: BusinessError) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
          return;
        }
        console.info('Succeeded in destroying the window.');
      });
    }

    build() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize(50)
            .fontWeight(FontWeight.Bold)
          Button() {
            Text('CreateSubWindow')
              .fontSize(24)
              .fontWeight(FontWeight.Normal)
          }.width(220).height(68)
          .margin({ left: 10, top: 60 })
          .onClick(() => {
            this.createSubWindow();
          })

          Button() {
            Text('destroySubWindow')
              .fontSize(24)
              .fontWeight(FontWeight.Normal)
          }.width(220).height(68)
          .margin({ left: 10, top: 60 })
          .onClick(() => {
            this.destroySubWindow();
          })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* SubWindow.ets文件配置如下，作为子窗口获取AppStorage中的subWindowClass，并重写onBackPress用于侧滑时关闭子窗口。

  ```screen
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct SubWindow {
    message: string = 'Hello subWindow';

    onBackPress(): boolean | void {
      this.destroySubWindow();
    }

    private destroySubWindow() {
      let sub_windowClass: window.Window | undefined = AppStorage.get('subWindowClass');
      if (!sub_windowClass) {
        console.error('sub_windowClass is null');
        return;
      }
      // 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
      sub_windowClass.destroyWindow((err: BusinessError) => {
        let errCode: number = err.code;
        if (errCode) {
          console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
          return;
        }
        console.info('Succeeded in destroying the window.');
      });
    }

    build() {
      Row() {
        Column() {
          Text(this.message)
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
        }
        .width('100%')
      }
      .height('100%')
      .backgroundColor('#F1F3F5')
    }
  }
  ```

### 场景二

对侧滑场景DismissReason.PRESS\_BACK也进行关闭弹窗操作。

```ts
@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  build() {
    Column() {
      Text('这是自定义弹窗')
        .fontSize(30)
        .height(100)
      Button('关闭弹窗')
        .onClick(() => {
          if (this.controller != undefined) {
            this.controller.close();
          }
        })
        .margin(20)
    }
  }
}

@Entry
@Component
struct CustomDialogPage {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: () => {
        this.onCancel();
      },
      confirm: () => {
        this.onAccept();
      }
    }),
    cancel: this.existApp,
    autoCancel: true,
    onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
      console.info(`reason= ${dismissDialogAction.reason}`);
      console.info('dialog onWillDismiss');
      if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
        dismissDialogAction.dismiss();
      }
      if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
        dismissDialogAction.dismiss();
      }
    },
    alignment: DialogAlignment.Center,
    offset: { dx: 0, dy: -20 },
    customStyle: false,
    cornerRadius: 20,
    width: 300,
    height: 200,
    borderWidth: 1,
  });

  // 在自定义组件即将析构销毁时将dialogController置空
  aboutToDisappear() {
    this.dialogController = null; // 将dialogController置空
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
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        }).backgroundColor(0x317aff)
    }.width('100%').margin({ top: 5 })
  }
}
```

### 场景三

修改onBackPress逻辑，在存在弹出框时优先关闭弹出框。

```ts
@Entry
@Component
struct MainPage {
  @State isShowDialog: boolean = false;
  @State isShowPage1: boolean = true;

  onBackPress(): boolean | void {
    if (this.isShowDialog) { // 如果已打开弹出框，则优先关闭弹出框
      this.isShowDialog = false;
      return true;
    } else if (!this.isShowPage1) { // 如果在第二个页面，则返回第一个页面
      this.isShowPage1 = true;
      return true;
    }
    return false;
  }

  build() {
    Stack() {
      if (this.isShowPage1) {
        Page1({ isShowPage1: this.isShowPage1 })
      } else {
        Page2({ isShowDialog: this.isShowDialog })
      }
      if (this.isShowDialog) {
        Dialog()
      }
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct Page1 {
  @Link isShowPage1: boolean;

  build() {
    Stack() {
      Text('页面一')
        .fontSize(22)
        .margin({ bottom: 100 })
      Button('点击跳转页面二')
        .onClick(() => {
          this.isShowPage1 = false;
        })
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct Page2 {
  @Link isShowDialog: boolean;

  build() {
    Stack() {
      Text('页面二')
        .fontSize(22)
        .margin({ bottom: 100 })
      Button('点击弹出弹出框')
        .onClick(() => {
          this.isShowDialog = true;
        })
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct Dialog {
  build() {
    Stack() {
      Text('这是弹出框')
        .fontSize(20)
        .fontColor(Color.White)
    }
    .backgroundColor('#383838')
    .opacity(0.9)
    .width('70%')
    .height('24%')
  }
}
```
