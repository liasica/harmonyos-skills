---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dragcontroller
title: Class (DragController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (DragController)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7c0c40749a4a27220336ef93d0314f80e8c8a40a14bf1d8b6dbe58d01463ab3f
---

提供拖拽控制能力，支持在应用接收到触摸或长按等事件时主动发起拖拽并携带拖拽信息，也支持创建拖拽Action、获取拖拽背板、控制拖拽事件上报和拖拽启动请求、取消拖拽数据加载，以及设置不允许落入目标区域时的禁止角标显示。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 11开始支持。
* 本模块接口仅可在Stage模型下使用。
* 以下API需先使用UIContext中的[getDragController()](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取DragController实例，再通过此实例调用对应方法。

## executeDrag11+

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo, callback: AsyncCallback<dragController.DragEventParam>): void

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。通过回调返回拖拽事件结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | 是 | 拖拽发起后跟手效果所拖拽的对象。当仅需通过builder生成当次拖拽中显示的图片时，使用CustomBuilder；当需要同时提供pixelMap、builder或extraInfo等拖拽项信息时，使用DragItemInfo。  **说明：**  CustomBuilder不支持全局builder。如果builder中使用了[Image](ts-basic-components-image.md)组件，建议开启同步加载，即配置Image的[syncLoad](ts-basic-components-image.md#syncload8)为true。该builder只用于生成当次拖拽中显示的图片。builder的根组件宽高为0时，无法生成拖拽显示的图片导致拖拽失败。builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。 |
| dragInfo | [dragController.DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息对象，用于指定发起拖拽的触摸点、拖拽过程中携带的数据、额外信息等拖拽配置信息。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[dragController.DragEventParam](js-apis-arkui-dragcontroller.md#drageventparam12)> | 是 | 拖拽结束返回结果的回调，回调参数包括err和data：err表示错误信息，data表示拖拽事件结果；data.event为拖拽事件信息，仅包括拖拽结果，data.extraParams为拖拽事件额外信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

```ts
import { dragController } from '@kit.ArkUI';
import { unifiedDataChannel } from '@kit.ArkData';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry
@Component
struct DragControllerPage {
  @Builder
  DraggingBuilder() {
    Column() {
      Text('DraggingBuilder')
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .onTouch((event?: TouchEvent) => {
          if (event) {
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.Text();
              let unifiedData = new unifiedDataChannel.UnifiedData(text);

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              };
              let eve: DragInfo = new DragInfo();
              this.getUIContext().getDragController().executeDrag(() => {
                this.DraggingBuilder()
              }, dragInfo, (err, eve) => {
                if (eve.event) {
                  if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
                    // ...
                  } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
                    // ...
                  }
                }
              });
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/jqqt7rIWT8WbEn3G24Ze1Q/zh-cn_image_0000002736434671.gif)

## executeDrag11+

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo): Promise<dragController.DragEventParam>

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。通过Promise返回拖拽事件结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | 是 | 拖拽发起后跟手效果所拖拽的对象。当仅需通过builder生成当次拖拽中显示的图片时，使用CustomBuilder；当需要同时提供pixelMap、builder或extraInfo等拖拽项信息时，使用DragItemInfo。  **说明：**  CustomBuilder不支持全局builder。如果builder中使用了[Image](ts-basic-components-image.md)组件，应尽量开启同步加载，即配置Image的[syncLoad](ts-basic-components-image.md#syncload8)为true。该builder只用于生成当次拖拽中显示的图片。builder的根组件宽高为0时，无法生成拖拽显示的图片导致拖拽失败。builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。 |
| dragInfo | [dragController.DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[dragController.DragEventParam](js-apis-arkui-dragcontroller.md#drageventparam12)> | Promise对象。resolve返回拖拽结束结果：  - event：拖拽事件信息，仅包括拖拽结果。  - extraParams：拖拽事件额外信息。reject返回错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

```ts
import { dragController } from '@kit.ArkUI';
import { image } from '@kit.ImageKit';
import { unifiedDataChannel } from '@kit.ArkData';

class DragInfo {
  event: DragEvent | undefined = undefined;
  extraParams: string = '';
}

@Entry
@Component
struct DragControllerPage {
  @State pixmap: image.PixelMap | null = null;

  @Builder
  DraggingBuilder() {
    Column() {
      Text('DraggingBuilder')
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  @Builder
  PixmapBuilder() {
    Column() {
      Text('PixmapBuilder')
    }
    .width(100)
    .height(100)
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      Button('touch to execute drag')
        .onTouch((event?: TouchEvent) => {
          if (event) {
            if (event.type == TouchType.Down) {
              let text = new unifiedDataChannel.Text();
              let unifiedData = new unifiedDataChannel.UnifiedData(text);

              let dragInfo: dragController.DragInfo = {
                pointerId: 0,
                data: unifiedData,
                extraParams: ''
              };
              let pixmapBuilder: CustomBuilder = (): void => {
                this.PixmapBuilder()
              };
              this.getUIContext().getComponentSnapshot().createFromBuilder(pixmapBuilder).then((pixelMap: image.PixelMap) => {
                this.pixmap = pixelMap;
                let dragItemInfo: DragItemInfo = {
                  pixelMap: this.pixmap,
                  builder: () => {
                    this.DraggingBuilder()
                  },
                  extraInfo: 'DragItemInfoTest'
                };
                let eve: DragInfo = new DragInfo();
                this.getUIContext()
                  .getDragController()
                  .executeDrag(dragItemInfo, dragInfo)
                  .then((eve) => {
                    if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
                      // ...
                    } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
                      // ...
                    }
                  })
                  .catch((err: Error) => {
                  })
              });
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/EtHtRoz0QJqYPaUSTKfBIA/zh-cn_image_0000002706835524.gif)

## createDragAction11+

createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction

创建拖拽的Action对象，需要显式指定拖拽背板图（可多个），以及拖拽的数据，跟手点等信息；当通过一个已创建的Action对象发起的拖拽未结束时，无法再次创建新的Action对象，接口会抛出异常；当Action对象的生命周期结束后，注册在该对象上的回调函数会失效，因此需要在一个尽量长的作用域下持有该对象，并在每次发起拖拽前通过createDragAction返回新的对象覆盖旧值。

**说明** 

建议控制传递的拖拽背板数量，避免因拖拽背板数量增加导致拖起耗时增加。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customArray | Array<[CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo)> | 是 | 拖拽发起后跟手效果所拖拽的对象。  **说明：**  CustomBuilder不支持全局builder。如果builder中使用了[Image](ts-basic-components-image.md)组件，应尽量开启同步加载，即配置Image的[syncLoad](ts-basic-components-image.md#syncload8)为true。builder用于生成拖拽中显示的图片。builder的根组件宽高为0时，无法生成拖拽显示的图片导致拖拽失败。builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。 |
| dragInfo | [dragController.DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [dragController.DragAction](js-apis-arkui-dragcontroller.md#dragaction11) | 创建拖拽Action对象，主要用于后面实现注册监听拖拽状态改变事件和启动拖拽服务。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

1. 在EntryAbility.ets中获取UI上下文并保存至LocalStorage中。

   ```ts
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window, UIContext } from '@kit.ArkUI';

   let uiContext: UIContext;
   let localStorage: LocalStorage = new LocalStorage('uiContext');

   export default class EntryAbility extends UIAbility {
     storage: LocalStorage = localStorage;

     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', this.storage, (err, data) => {
         if (err.code) {
           hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
           return;
         }
         hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
         windowStage.getMainWindow((err, data) => {
           if (err.code) {
             console.error(`Failed to obtain the main window. Cause:${err.message}`);
             return;
           }
           let windowClass: window.Window = data;
           uiContext = windowClass.getUIContext();
           this.storage.setOrCreate<UIContext>('uiContext', uiContext);
           // 获取UIContext实例
         });
       });
     }

     onWindowStageDestroy(): void {
       // Main window is destroyed, release UI related resources
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
     }

     onForeground(): void {
       // Ability has brought to foreground
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
     }

     onBackground(): void {
       // Ability has back to background
       hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
     }
   }
   ```
2. 调用this.getUIContext().getSharedLocalStorage()获取上下文，再获取DragController对象以执行后续拖拽操作。

   ```ts
   import { dragController, UIContext } from '@kit.ArkUI';
   import { image } from '@kit.ImageKit';
   import { unifiedDataChannel } from '@kit.ArkData';

   @Entry()
   @Component
   struct DragControllerPage {
     private dragAction: dragController.DragAction | null = null;
     customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();
     storages = this.getUIContext().getSharedLocalStorage();

     @Builder
     DraggingBuilder() {
       Column() {
         Text('DraggingBuilder')
       }
       .width(100)
       .height(100)
       .backgroundColor(Color.Blue)
     }

     build() {
       Column() {
         Button('多对象dragAction customBuilder拖拽').onTouch((event?: TouchEvent) => {
           if (event) {
             if (event.type == TouchType.Down) {
               console.info('multi drag Down by listener');
               this.customBuilders.push(() => {
                 this.DraggingBuilder()
               });
               this.customBuilders.push(() => {
                 this.DraggingBuilder()
               });
               this.customBuilders.push(() => {
                 this.DraggingBuilder()
               });
               let text = new unifiedDataChannel.Text();
               let unifiedData = new unifiedDataChannel.UnifiedData(text);
               let dragInfo: dragController.DragInfo = {
                 pointerId: 0,
                 data: unifiedData,
                 extraParams: ''
               };
               try {
                 this.dragAction = this.getUIContext().getDragController().createDragAction(this.customBuilders, dragInfo);
                 if (!this.dragAction) {
                   console.info('listener dragAction is null');
                   return;
                 }
                 this.dragAction.on('statusChange', (dragAndDropInfo) => {
                   if (dragAndDropInfo.status == dragController.DragStatus.STARTED) {
                     console.info('drag has start');
                   } else if (dragAndDropInfo.status == dragController.DragStatus.ENDED) {
                     console.info('drag has end');
                     if (!this.dragAction) {
                       return;
                     }
                     // 拖拽结束后，清空拖拽背板数组并取消状态监听。
                     this.customBuilders.splice(0, this.customBuilders.length);
                     this.dragAction.off('statusChange');
                   }
                 });
                 this.dragAction.startDrag().then(() => {
                 }).catch((err: BusinessError) => {
                   console.error(`Failed to start drag. Code: ${err.code}, message: ${err.message}`);
                 });
               } catch (err) {
                 const error = err as BusinessError;
                 console.error(`Failed to create dragAction. Code: ${error.code}, message: ${error.message}`);
               }
             }
           }
         }).margin({ top: 20 })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/HkoWmBDMSj6LN2WTZ7sWCw/zh-cn_image_0000002736314629.gif)

## getDragPreview11+

getDragPreview(): dragController.DragPreview

返回一个代表拖拽背板的对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [dragController.DragPreview](js-apis-arkui-dragcontroller.md#dragpreview11) | 一个代表拖拽背板的对象，提供背板样式设置的接口，在onDrop和onDragEnd回调中使用不生效。 |

**错误码：** 通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

**示例：**

请参考[animate](js-apis-arkui-dragcontroller.md#animate11)示例。

## setDragEventStrictReportingEnabled12+

setDragEventStrictReportingEnabled(enable: boolean): void

当目标从父组件拖拽到子组件时，通过该方法设置是否会触发父组件的onDragLeave的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 将目标从父组件拖拽到子组件时，是否会触发父组件的onDragLeave的回调。true表示触发父组件的onDragLeave的回调，false表示不触发。 |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { window, UIContext } from '@kit.ArkUI';

 export default class EntryAbility extends UIAbility {
   onWindowStageCreate(windowStage: window.WindowStage): void {
       windowStage.loadContent('pages/Index', (err, data) => {
         if (err.code) {
         return;
       }
       windowStage.getMainWindow((err, data) => {
         if (err.code) {
           return;
         }
         let windowClass: window.Window = data;
         let uiContext: UIContext = windowClass.getUIContext();
         uiContext.getDragController().setDragEventStrictReportingEnabled(true);
     });
   });
 }
}
```

## cancelDataLoading15+

cancelDataLoading(key: string): void

当使用[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)获取拖拽数据时，可调用该接口取消数据传输。仅可在拖拽释放后调用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 拖拽数据的标识，用于区分每次拖拽。key可通过startDataLoading接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[拖拽事件错误码](errorcode-drag-event.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 190004 | Operation failed. |

## notifyDragStartRequest18+

notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void

控制应用是否可以发起拖拽。该接口通常与组件的onPreDrag和onDragStart回调配合使用：在拖拽开始但数据尚未准备完成时，可在onDragStart回调中调用notifyDragStartRequest(DragStartRequestStatus.WAITING)，阻止立即发起拖拽；待拖拽数据和预览资源准备完成后，再调用notifyDragStartRequest(DragStartRequestStatus.READY)，允许继续发起拖拽。若未按拖拽准备流程正确上报状态，可能导致拖拽无法按预期启动，或启动时拖拽数据尚未准备完成。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestStatus | [dragController.DragStartRequestStatus](js-apis-arkui-dragcontroller.md#dragstartrequeststatus18) | 是 | 定义应用是否可以发起拖拽。取值为WAITING时，表示应用数据仍在准备阶段，暂不允许发起拖拽；取值为READY时，表示应用数据已准备完成，允许继续发起拖拽。 |

**示例：**

```ts
// xxx.ets
import { unifiedDataChannel } from '@kit.ArkData';
import { image } from '@kit.ImageKit';
import { dragController } from '@kit.ArkUI';

@Entry
@Component
struct NormalEts {
  @State finished: boolean = false;
  @State timeout1: number = 1;
  @State pixmap: image.PixelMap | undefined = undefined;
  @State unifiedData1: unifiedDataChannel.UnifiedData | undefined = undefined;
  @State previewData: DragItemInfo | undefined = undefined;

  loadData() {
    // 设置4s后才能发起拖拽
    let timeout = setTimeout(() => {
      this.getUIContext().getComponentSnapshot().get('image1', (error: Error, pixmap: image.PixelMap) => {
        if (error) {
          return;
        }
        this.pixmap = pixmap;
        this.previewData = {
          pixelMap: this.pixmap
        };
      });

      let data: unifiedDataChannel.Image = new unifiedDataChannel.Image();
      data.imageUri = 'app.media.startIcon';
      let unifiedData = new unifiedDataChannel.UnifiedData(data);
      this.unifiedData1 = unifiedData;
      this.finished = true;

      this.getUIContext().getDragController().notifyDragStartRequest(dragController.DragStartRequestStatus.READY);
    }, 4000);
    this.timeout1 = timeout;
  }

  build() {
    Column({ space: 20 }) {
      Image($r('app.media.startIcon'))
        .width(150)
        .height(150)
        .id('image1')
        .draggable(true)
        .dragPreview(this.previewData)
        .onPreDrag((status: PreDragStatus) => {
          if (status == PreDragStatus.PREPARING_FOR_DRAG_DETECTION) {
            this.loadData();
          } else {
            clearTimeout(this.timeout1);
          }
        })
        .onDragStart((event: DragEvent) => {
          if (this.finished == false) {
            this.getUIContext()
              .getDragController()
              // 应用数据准备阶段，无法发起拖拽
              .notifyDragStartRequest(dragController.DragStartRequestStatus.WAITING);
          } else {
            event.setData(this.unifiedData1);
          }
        })
        .onDragEnd(() => {
          this.finished = false;
        })
    }
    .width('100%')
    .height(400)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/2VJELpLDTsWY4bkVxAIlDw/zh-cn_image_0000002706675586.gif)

## enableDropDisallowedBadge20+

enableDropDisallowedBadge(enabled: boolean): void

当拖拽数据类型与组件配置的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)允许接收的数据类型无交集时，可显示禁用角标。通常，当组件可以接收或处理拖拽数据，或当它返回DragBehavior.COPY向系统声明数据以复制方式处理时，拖拽对象会显示加号及数据编号的角标。如果返回DragBehavior.MOVE以向系统声明数据以剪切方式处理，拖拽对象将只显示数据编号的角标。当目标进行拖拽时，若系统决定或组件显式声明无法处理拖拽数据，可通过该方法检查是否应显示拖拽禁止角标。该接口暂不支持[UIExtension](js-apis-arkui-uiextension.md)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 当拖拽数据类型与组件配置的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)允许接收的数据类型无交集时，可显示禁用角标；对目标组件进行拖拽时，通过enableDropDisallowedBadge方法检查是否显示拖拽禁止角标。true表示显示拖拽禁止角标，false表示不显示拖拽禁止角标。默认值为false。 |

**示例：**

该示例通过enableDropDisallowedBadge接口实现了拖拽对象经过不允许落入的目标区域时显示拖拽禁止角标的功能。

1. 在EntryAbility.ets中调用enableDropDisallowedBadge接口，设置enabled参数为true。

   ```ts
   import { UIAbility } from '@kit.AbilityKit';
   import { window, UIContext } from '@kit.ArkUI';

    export default class EntryAbility extends UIAbility {
      onWindowStageCreate(windowStage: window.WindowStage): void {
          windowStage.loadContent('pages/Index', (err, data) => {
            if (err.code) {
            return;
          }
          windowStage.getMainWindow((err, data) => {
            if (err.code) {
              return;
            }
            let windowClass: window.Window = data;
            let uiContext: UIContext = windowClass.getUIContext();
            uiContext.getDragController().enableDropDisallowedBadge(true);
        });
      });
    }
   }
   ```
2. 在Index.ets中拖拽图标icon至下方空白区域，显示拖拽禁止角标。

   ```ts
   @Entry
   @Component
   struct Index {
     build() {
       Column({ space: 20 }) {
         // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
         Image($r('app.media.startIcon'))
           .width(120)
           .height(120)
         Text('这里是不能落入区域')
         Column()
           .width('100%')
           .layoutWeight(1)
           .allowDrop(null)
           .onDrop(() => {
           })
       }.width('100%')
     }
   }
   ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/2VzJ4uhLRpO5gQWtjGs2Pg/zh-cn_image_0000002736434673.png)
