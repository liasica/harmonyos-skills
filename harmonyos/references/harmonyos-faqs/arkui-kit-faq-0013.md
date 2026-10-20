---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0013
title: 自定义弹窗弹出或关闭异常如何排查
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > 自定义弹窗弹出或关闭异常如何排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:b2f48d15782332d1825170d1cd3446d0da4a214fb2a82dbc49f7672aa169b971
---

**Q：使用promptAction.openCustomDialog创建自定义弹窗，将全局Builder构建函数作为自定义弹窗内容构造器。弹窗弹出时应用闪退。错误日志为：**

```txt
Reason:TypeError Error name:TypeError Error message:Cannot read property observeComponentCreation2 of undefined
```

问题代码为：

```ts
import { promptAction } from '@kit.ArkUI'

@Builder
function customDialogComponent() {
  Column() {
    Text('customDialogComponent')
  }
}

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('弹窗').onClick(() => {
        this.getUIContext().getPromptAction().openCustomDialog({
          builder: () => {
            customDialogComponent()
          },
          alignment: DialogAlignment.Center
        })
      })
    }
  }
}
```

**A**：自定义构建函数@Builder可以在所属组件的build方法和其他自定义构建函数中调用，但不允许在组件外调用。因此，需要将自定义构建函数@Builder移至结构体内部，示例代码如下：

```ts
@Entry
@Component
struct Index55 {
  private customDialogComponentId: number = 0;

  // 在结构体内构建定义函数
  @Builder
  customDialogComponent() {
    Column() {
      Text('温馨提示')
        .fontSize(25)
        .margin({ top: 10 });
      Text('请注意,一旦删除,该数据将从缓存中删除且不可恢复。请谨慎选择。')
        .padding({ left: 20, right: 20 });
      Row({ space: 50 }) {
        Button('确认').onClick(() => {
          try {
            this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
          }
        });
        Button('取消').onClick(() => {
          try {
            this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
          } catch (error) {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(`closeCustomDialog error code is ${code}, message is ${message}`);
          }
        });
      };
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceAround);
  }

  build() {
    RelativeContainer() {
      Button('弹窗')
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.getUIContext().getPromptAction().openCustomDialog({
            builder: () => {
              this.customDialogComponent();
            },
            alignment: DialogAlignment.Center
          }).then((dialogId: number) => {
            this.customDialogComponentId = dialogId;
          });
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/ef1lua5_RieqSxCgObrqdA/zh-cn_image_0000002766076806.png "点击放大")

**Q：如何解决弹出多个弹窗，无法关闭的问题？问题代码如下：**

```ts
closeDialog() {
  if (DialogUtils.contentNode) {
    let uiContext: UIContext | undefined = AppStorage.get<UIContext>('uiContext')
    if (uiContext) {
      uiContext.getPromptAction().closeCustomDialog(DialogUtils.contentNode)
      // 关闭一个弹窗就清空了，后面调用就都是null，所以关不掉
      DialogUtils.contentNode = null
    }
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/K8y8czDPSgK7glVfD1u2bg/zh-cn_image_0000002795315663.png "点击放大")

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/WYOyxmCHRIyUwsdt6fkFzQ/zh-cn_image_0000002795475457.png "点击放大")

**A**：弹窗关闭的代码有误，“DialogUtils.contentNode = null”关闭一个弹窗就清空了，后面调用就都是null，所以关不掉。方案如下：用个数组存储每个弹窗的contentNode，每关闭一个pop()一个，并将数组最后一个值赋值给contentNode，关闭的就是上一个弹窗的contentNode。完整示例如下：

1. DialogUtils.ets：

   ```ts
   import { ComponentContent, promptAction } from '@kit.ArkUI';

   export class Params {
     content: string = '';
     callback: (isGranted: boolean, msg?: string) => void = (): void => {
     };

     constructor(content: string, callback: (isGranted: boolean, msg?: string) => void) {
       this.content = content;
       this.callback = callback;
     }
   }

   @Builder
   export function buildText(params: Params) {
     Column() {
       Column() {
         // 内容
         Text(params.content)
           .width('100%')
           .textAlign(TextAlign.Start)
           .padding(15)
           .fontSize(18)
           .fontColor('#2c2c2c')

         Column()
           .width('100%')
           .height(0.5)
           .backgroundColor('#E6E6E6')

         // 取消、确定按钮
         Row() {
           // 取消按钮
           Text('取消按钮')
             .width(0)
             .layoutWeight(1)
             .textAlign(TextAlign.Center)
             .padding({ top: 20, bottom: 20 })
             .fontColor('#BDBDBD')
             .borderRadius({ bottomLeft: 5 })
             .fontSize(15)
             .onClick(() => {
               DialogUtils.closeDialog();
             })
           Text('确定按钮')
             .width(0)
             .layoutWeight(1)
             .textAlign(TextAlign.Center)
             .padding({ top: 20, bottom: 20 })
             .fontColor('#BDBDBD')
             .borderRadius({ bottomLeft: 5 })
             .fontSize(15)
             .onClick(() => {
               DialogUtils.closeDialog();
               params.callback(false, 'okk');
             })
         }
         .width('100%')
         .alignItems(VerticalAlign.Center)
         .justifyContent(FlexAlign.SpaceAround)
       }
       .backgroundColor(Color.White)
       .borderRadius(5)
       .margin({ left: 15, right: 15 })
     }
     .height('100%')
     .width('100%')
     .justifyContent(FlexAlign.Center)
     .backgroundColor(Color.Transparent)
   }

   export default class DialogUtils {
     static contentNode: ComponentContent<Params> | null = null;
     static contentNodes: Array<ComponentContent<Params>> = [];

     static showDialog(content: string, callback: (isGranted: boolean, msg?: string) => void) {
       let uiContext: UIContext | undefined = AppStorage.get<UIContext>('uiContext');

       if (uiContext) {
         let promptAction = uiContext.getPromptAction();
         DialogUtils.contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(content, callback));
         DialogUtils.contentNodes.push(DialogUtils.contentNode);

         let options: promptAction.BaseDialogOptions = {
           alignment: DialogAlignment.Top,
           autoCancel: false,
           maskColor: '#cd000000',
         };
         promptAction.openCustomDialog(DialogUtils.contentNode, options);
       }
     }

     public static closeDialog() {
       if (DialogUtils.contentNode) {
         let uiContext: UIContext | undefined = AppStorage.get<UIContext>('uiContext');
         if (uiContext) {
           let promptAction = uiContext.getPromptAction();
           promptAction.closeCustomDialog(DialogUtils.contentNode);
           if (DialogUtils.contentNodes.length > 0) {
             DialogUtils.contentNodes.pop();
             if (DialogUtils.contentNodes.length > 0) {
               DialogUtils.contentNode = DialogUtils.contentNodes[DialogUtils.contentNodes.length - 1];
             } else {
               DialogUtils.contentNode = null;
             }
           }
         }
       }
     }
   }
   ```
2. Index.ets：

   ```ts
   import DialogUtils from './DialogUtils';

   AppStorage.setOrCreate('uiContext', undefined);

   @Entry
   @Component
   struct Index {
     pageInfos: NavPathStack = new NavPathStack();
     @StorageLink('uiContext') uiContext: UIContext | undefined = undefined;

     build() {
       Navigation(this.pageInfos) {
         RelativeContainer() {
           Text('首页')
             .fontSize(22)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
         }
         .width('100%')
         .height('100%')
         .backgroundColor(Color.White)
       }
       .hideTitleBar(false)
       .hideToolBar(false)
     }

     aboutToAppear(): void {
       this.uiContext = this.getUIContext();
       let nums: number = 8;
       for (let i = 0; i < nums; i++) {
         DialogUtils.showDialog(`hello world: ${i}`, (isGrant: boolean, msg?: string) => {
           console.log(`${isGrant}--------${msg}`);
         });
       }
     }
   }
   ```

**Q：首次打开APP时，通知权限申请弹窗与自定义弹窗冲突，只弹出了通知权限申请弹窗，而自定义弹窗未弹出。问题代码如下：**

```ts
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { notificationManager } from '@kit.NotificationKit';

@CustomDialog
struct CustomDialogExample {
  controller: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({}),
  })

  build() {
    Column() {
      Text('我是内容')
        .fontSize(20)
    }.height(60).justifyContent(FlexAlign.Center)
  }
}

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample(),
  })

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const DOMAIN_NUMBER: number = 0xFF00;
    const TAG: string = '[PublishOperation]';
    notificationManager.isNotificationEnabled().then((data: boolean) => {
      hilog.info(DOMAIN_NUMBER, TAG, `isNotificationEnabled success, data: ${data}`);
      if(!data){
        notificationManager.requestEnableNotification(context).then(() => {
          this.dialogController.open()
          hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
        }).catch((err : BusinessError) => {
          if(1600004 == err.code){
            hilog.error(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
          } else {
            hilog.error(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
          }
        });
      }
    }).catch((err : BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {
    RelativeContainer() {
      Text('Hello World')
        .fontSize($r('app.float.page_text_font_size'))
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%')
  }
}
```

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/aff-LNCVQ62hxZjxAlXEgA/zh-cn_image_0000002765917346.png "点击放大")

**A**：由于系统级弹窗的模态化窗口级别较高，不可与CustomDialog或openCustomDialog同时弹出，因此禁止直接弹出子窗口或其他弹窗，必须按照先后顺序展示。

若使用了系统级别弹窗，不能在requestEnableNotification接口回调中进行调用CustomDialog或openCustomDialog，打开自定义弹窗的代码需要在requestEnableNotification回调结束后调用。代码修复如下：

```ts
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { notificationManager } from '@kit.NotificationKit';

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column() {
      Text('这是自定义弹窗')
        .fontSize(30)
        .height(100);
      Button('点我关闭弹窗')
        .onClick(() => {
          if (this.controller != undefined) {
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
    backgroundColor: Color.White,
    backgroundBlurStyle: BlurStyle.Thin,

  });

  aboutToAppear(): void {
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const DOMAIN_NUMBER: number = 0xFF00;
    const TAG: string = '[PublishOperation]';
    notificationManager.isNotificationEnabled().then((data: boolean) => {
      hilog.info(DOMAIN_NUMBER, TAG, `isNotificationEnabled success, data: ${data}`);
      if (!data) {
        notificationManager.requestEnableNotification(context).then(() => {
          hilog.info(DOMAIN_NUMBER, TAG, `[ANS] requestEnableNotification success`);
        }).catch((err: BusinessError) => {
          if (1600004 == err.code) {
            hilog.error(DOMAIN_NUMBER, TAG,
              `[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
          } else {
            hilog.error(DOMAIN_NUMBER, TAG,
              `[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
          }
        });
      }
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, `isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
    });
    // 系统通知授权后，弹窗
    this.dialogController.open();
  }

  build() {
    RelativeContainer() {
      Text('Hello World')
        .fontSize($r('app.float.page_text_font_size'))
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/kEFMXX5PSoeF7hAWdzZYPQ/zh-cn_image_0000002795475973.png "点击放大")

**Q：点击Web内组件同时弹出alert弹窗和系统弹窗，拉起alert弹窗时，Web进程会阻塞等待应用恢复如何规避？**

**A**：可以给[AlertDialog](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialogparam对象说明)设置LevelMode属性（弹窗显示层级模式），设置[LevelMode](../harmonyos-references/js-apis-promptaction.md#levelmode15枚举说明)：LevelMode.EMBEDDED，会将分享弹窗和alert弹窗都显示出来，也不会卡死。
