---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-603
title: 自定义弹窗和子窗口间的层级关系
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 自定义弹窗和子窗口间的层级关系
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6f292a32ae4697822d91bc9326f907ab445970197337c732ec9e524bb5b8b0cd
---

## 问题现象

自定义弹窗和子窗口间的层级关系是怎样的，是否按照唤起顺序叠放？

## 背景知识

* 通过CustomDialogController类显示的[基础自定义弹窗(CustomDialog)](../harmonyos-guides/arkts-common-components-custom-dialog.md)的创建与管理必须依赖具体组件，每个弹窗都要在组件中单独声明对应的CustomDialogController。
* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)用于打开全局自定义弹窗，弹窗内容与页面解耦。
* 通过WindowStage下的[createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9)方法可以创建子窗口。

## 解决方案

本文内容分别针对CustomDialogController类实现的基础自定义弹窗和openCustomDialog实现的全局自定义弹窗作出三种场景下的对比，通过这些对比我们可以得出上述两种自定义弹窗与子窗口之间在层级的关系(结论在总结部分)：

* 场景一：在主窗口界面先打开子窗口，然后在主窗口界面打开自定义弹窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/Tu6WBg_BQIyM_1VZbS4Y7w/zh-cn_image_0000002658791979.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/fIW5X7t8QmKWkLVXmnsPYA/zh-cn_image_0000002628552604.png "点击放大")

  此时，两种自定义弹窗的层级都在主窗口之上，子窗口之下，且弹出位置在主窗口中间。
* 场景二：在主窗口界面先打开子窗口，然后在子窗口界面打开自定义弹窗：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/RH_a2NtfRluasLjowpn3ww/zh-cn_image_0000002658911919.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/UHNmM8HWRsiRwHpqKdmjhQ/zh-cn_image_0000002628392722.png "点击放大")

  此时，两种自定义弹窗的层级都在子窗口之上，且弹出位置在子窗口中间。
* 场景三：在主窗口界面通过一次点击操作，先打开子窗口，然后在一个setTimeout的延时后打开自定义弹窗。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/QIaB45GzT0qgIZ01hp2ZsA/zh-cn_image_0000002658791995.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/dqTvFHk5SFWYJamQdnqGZg/zh-cn_image_0000002628552616.png "点击放大")

  此时，基础自定义弹窗的层级在主窗口之上，子窗口之下，且弹出位置在主窗口中间；全局自定义弹窗的层级在子窗口之上，且弹出位置在子窗口中间。

以下是部分核心代码：

* 基础自定义弹窗的实现：

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
        Text('基础自定义弹窗')
          .fontSize(20)
          .height(100);
        Button('Close')
          .onClick(() => {
            if (this.controller !== undefined) {
              this.controller.close();
            }
          })
          .margin(20);
      };
    }
  }
  ```
* 全局自定义弹窗的实现：

  ```ts
  export class OMDialog {
    private uiContext: UIContext = new UIContext;
    private viewNode: ComponentContent<Object> | null = null;
    static instance: OMDialog = new OMDialog();

    static init(uiContext: UIContext) {
      OMDialog.instance.uiContext = uiContext;
    }

    open() {
      let view = new ComponentContent(this.uiContext, wrapBuilder(customDialogBuilder));
      this.uiContext.getPromptAction().openCustomDialog(view, { offset: { dx: 0, dy: 0 } }).then(() => {
        this.viewNode = view;
      });
    }

    close() {
      this.uiContext.getPromptAction().closeCustomDialog(this.viewNode);
    }
  }

  @Builder
  function customDialogBuilder() {
    TestComponent();
  }

  @Component
  struct TestComponent {
    build() {
      Column() {
        Text('全局自定义弹窗').fontSize(20).height(100);
        Row() {
          Button('Close')
            .onClick(() => {
              OMDialog.instance.close();
            })
            .margin(20);
        };
      }
      .width('90%')
      .backgroundColor($r('app.color.start_window_background'))
      .borderRadius(8);
    }
  }
  ```
* 子窗口的创建和销毁：

  ```screen
  export class SubWindowManager {
    public windowClass: window.Window | null = null;

    public creatSubWindow(): void {
      let windowStage = AppStorage.get('windowStage') as window.WindowStage;
      try {
        this.windowClass = window.findWindow('ResizeSubWindow');
      } catch (exception) {
        windowStage.createSubWindow('ResizeSubWindow', (err, windowClass) => {
          this.windowClass = windowClass;
          if (err.code > 0) {
            console.error(`failed to create subWindow Cause: ${err.message}`);
            return;
          }
          try {
            // 设置子窗口加载页
            windowClass.setUIContent('pages/SubWindowPage', () => {
            });
            // 设置子窗口左上角坐标
            windowClass.moveWindowTo(100, 1800);
            // 设置子窗口大小
            windowClass.resize(800, 800);
            // 展示子窗口
            windowClass.showWindow();
          } catch (err) {
            console.error(`failed to create subWindow Cause:${err}`);
          }
        });
      }
    }

    public closeSubWindow(): void {
      if (this.windowClass) {
        this.windowClass.destroyWindow();
      }
    }
  }
  ```

完整示例代码如下：

其中第一个文件的路径为：项目名\entry\src\main\ets\entryability。

其余文件的路径为：项目名\entry\src\main\ets\pages。

EntryAbility的onWindowStageCreate中可以存储windowStage。

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.info(`want: ${want}`);
    console.info(`launchParam: ${launchParam}`);
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
    AppStorage.setOrCreate('windowStage', windowStage);
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

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

```ts
// Utils.ets
import { ComponentContent, UIContext, window } from '@kit.ArkUI';

export class OMDialog {
  private uiContext: UIContext = new UIContext;
  private viewNode: ComponentContent<Object> | null = null;
  static instance: OMDialog = new OMDialog();

  static init(uiContext: UIContext) {
    OMDialog.instance.uiContext = uiContext;
  }

  open() {
    let view = new ComponentContent(this.uiContext, wrapBuilder(customDialogBuilder));
    this.uiContext.getPromptAction().openCustomDialog(view, { offset: { dx: 0, dy: 0 } }).then(() => {
      this.viewNode = view;
    });
  }

  close() {
    this.uiContext.getPromptAction().closeCustomDialog(this.viewNode);
  }
}

@Builder
function customDialogBuilder() {
  TestComponent();
}

@Component
struct TestComponent {
  build() {
    Column() {
      Text('全局自定义弹窗').fontSize(20).height(100);
      Row() {
        Button('Close')
          .onClick(() => {
            OMDialog.instance.close();
          })
          .margin(20);
      };
    }
    .width('90%')
    .backgroundColor($r('app.color.start_window_background'))
    .borderRadius(8);
  }
}

export class SubWindowManager {
  public windowClass: window.Window | null = null;

  public creatSubWindow(): void {
    let windowStage = AppStorage.get('windowStage') as window.WindowStage;
    try {
      this.windowClass = window.findWindow('ResizeSubWindow');
    } catch (exception) {
      windowStage.createSubWindow('ResizeSubWindow', (err, windowClass) => {
        this.windowClass = windowClass;
        if (err.code > 0) {
          console.error(`failed to create subWindow Cause: ${err.message}`);
          return;
        }
        try {
          // 设置子窗口加载页
          windowClass.setUIContent('pages/SubWindowPage', () => {
          });
          // 设置子窗口左上角坐标
          windowClass.moveWindowTo(100, 1800);
          // 设置子窗口大小
          windowClass.resize(800, 800);
          // 展示子窗口
          windowClass.showWindow();
        } catch (err) {
          console.error(`failed to create subWindow Cause:${err}`);
        }
      });
    }
  }

  public closeSubWindow(): void {
    if (this.windowClass) {
      this.windowClass.destroyWindow();
    }
  }
}
```

```ts
// Index.ets
import { window } from '@kit.ArkUI';
import { OMDialog, SubWindowManager } from './Utils';

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;
  cancel: () => void = () => {
  };
  confirm: () => void = () => {
  };

  build() {
    Column() {
      Text('基础自定义弹窗')
        .fontSize(20)
        .height(100);
      Button('Close')
        .onClick(() => {
          if (this.controller !== undefined) {
            this.controller.close();
          }
        })
        .margin(20);
    };
  }
}

@Entry
@Component
struct Index {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
  });
  subWindowManager = new SubWindowManager();

  build() {
    Column({ space: 16 }) {
      Button('主窗口中打开基础customdialog')
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        });
      Button('主窗口中打开onpencustomdialog')
        .onClick(() => {
          OMDialog.instance.open();
        });
      Button('先打开子窗口再打开基础customdialog')
        .onClick(() => {
          this.subWindowManager.creatSubWindow();
          setTimeout(() => {
            if (this.dialogController != null) {
              this.dialogController.open();
            }
          }, 3000);
        });
      Button('先打开子窗口再打开onpencustomdialog')
        .onClick(() => {
          this.subWindowManager.creatSubWindow();
          setTimeout(() => {
            OMDialog.instance.open();
          }, 3000);
        });
      Button('打开子窗口')
        .onClick(() => {
          this.subWindowManager.creatSubWindow();
        });
      Button('关闭子窗口')
        .onClick(() => {
          this.subWindowManager.closeSubWindow();
        });

      Button('支付按钮')
        .onClick(() => {
          try {
            window.findWindow('ResizeSubWindow');
            let subWindowID: number = window.findWindow('ResizeSubWindow').getWindowProperties().id;
            // 获取主窗口ID
            let windowStage = AppStorage.get('windowStage') as window.WindowStage;
            let mainWindowID: number = windowStage.getMainWindowSync().getWindowProperties().id;
            // 将焦点从主窗口转移到子窗口
            let promise = window.shiftAppWindowFocus(mainWindowID, subWindowID);
            promise.then(() => {
              OMDialog.instance.open();
              console.info('Succeeded in shifting app window focus');
            });
          } catch (exception) {
            this.getUIContext().getPromptAction().showToast({ message: '请先打开子窗口' });
          }
        });

      Button('3S后打开提示弹窗')
        .onClick(() => {
          try {
            window.findWindow('ResizeSubWindow');
            setTimeout(() => {
              let subWindowID: number = window.findWindow('ResizeSubWindow').getWindowProperties().id;
              // 获取主窗口ID
              let windowStage = AppStorage.get('windowStage') as window.WindowStage;
              let mainWindowID: number = windowStage.getMainWindowSync().getWindowProperties().id;
              // 将焦点从子窗口转移到主窗口
              let promise = window.shiftAppWindowFocus(subWindowID, mainWindowID);
              promise.then(() => {
                OMDialog.instance.open();
                console.info('Succeeded in shifting app window focus');
              });
            }, 3000);
          } catch (exception) {
            this.getUIContext().getPromptAction().showToast({ message: '请先打开子窗口' });
          }
        });

    }
    .height('100%')
    .width('100%');
  }
}
```

```ts
import { OMDialog } from './Utils';

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('基础自定义弹窗')
        .fontSize(20)
        .height(100);
      Button('Close')
        .onClick(() => {
          if (this.controller !== undefined) {
            this.controller.close();
          }
        })
        .margin(20);
    };
  }
}

@Entry
@Component
struct SubWindowPage {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
  });

  build() {
    Column({ space: 16 }) {
      Button('打开opencustomdialog')
        .onClick(() => {
          OMDialog.instance.open();
        });
      Button('打开基础customdialog')
        .onClick(() => {
          if (this.dialogController != null) {
            this.dialogController.open();
          }
        })
    }
    .padding({ top: 16 })
    .height('100%')
    .width('100%')
    .backgroundColor('#aaa');
  }
}
```

通过以上两种自定义弹窗在三种场景下的对比，我们可以得出结论：

* 自定义弹窗会在打开时确定它所属的窗口，弹窗是窗口的一部分。当自定义弹窗所在的窗口层级低于另一个窗口时，弹窗的层级也会低于另一个窗口。
* 自定义弹窗的层级与唤起的顺序无关，只与它所属的窗口有关。
* 对于CustomDialogController类实现的基础自定义弹窗，由于用于打开弹窗的弹窗控制器需要在组件中声明，它会与其绑定的组件在同一个窗口之中，即在哪个窗口调用的基础自定义弹窗，弹窗的层级便在这个窗口页面之上，并低于层级更高的其他窗口。
* 对于openCustomDialog实现的全局弹窗，它所在的窗口取决于自身锚点的UI上下文，它所属的窗口是在打开时确定的，此时焦点处于哪个窗口，它就会在哪个窗口上打开：
  + 在场景一中，它通过主窗口页面的点击操作唤起，因此锚点在主窗口上，其层级也就高于主窗口页面而低于子窗口。
  + 在场景二中，它通过子窗口页面的点击操作唤起，因此锚点在子窗口上，其层级也就在子窗口页面之上。
  + 在场景三中，它虽然通过主窗口的点击操作唤起，但打开时机在子窗口打开之后，因此锚点在子窗口上，其层级也就在子窗口页面之上。

基于上述结论，我们可以明确自定义弹窗在多窗口下的打开层级，确保其能正确依附于预期的窗口上。例如，使用openCustomDialog全局自定义弹窗时，可以通过在不同窗口转移焦点的方式使其打开在我们想要的窗口上。以下是两种示例场景：

* 出于UI设计的考虑，一个支付按钮需要放置在主窗口页面且不能放置在子窗口页面，在我们已经打开子窗口的情况下，对主窗口中的该按钮进行点击操作会使弹窗在主窗口中打开，如果弹窗打开位置与子窗口重叠，则会被子窗口遮挡。但由于弹窗内容比较重要，设计上希望它必须被用户操作，我们可以在打开弹窗时将焦点从主窗口转移到子窗口，使弹窗在子窗口中打开从而不被遮挡。

  ```ts
  let subWindowID: number = window.findWindow('ResizeSubWindow').getWindowProperties().id;
  // 获取主窗口ID
  let windowStage = AppStorage.get('windowStage') as window.WindowStage;
  let mainWindowID: number = windowStage.getMainWindowSync().getWindowProperties().id;
  // 将焦点从主窗口转移到子窗口
  let promise = window.shiftAppWindowFocus(mainWindowID, subWindowID);
  promise.then(() => {
    OMDialog.instance.open();
    console.info('Succeeded in shifting app window focus');
  });
  ```

* 主窗口页面中有一个预约某节目的按钮，节目开始后弹出提示弹窗。如果用户此时在子窗口中进行操作，则焦点在子窗口上，弹窗也会出现在子窗口中，但由于该提示弹窗重要程度较低，我们不希望它弹在子窗口上打断用户的操作。则可以在打开弹窗前先将焦点转移到主窗口上，使其在主窗口上弹出。
