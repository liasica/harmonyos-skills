---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-image-track
title: 图像跟踪（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 图像跟踪 > 图像跟踪（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:49+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:428004bb4b0d739dcb509ce53b72689107ef82b33519f2d49c0e94b5ca0be315
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

从5.1.0(18)开始，图像跟踪能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持图像跟踪特性（[ARENGINE\_FEATURE\_TYPE\_IMAGE](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR图像跟踪相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create) | 创建一个新的[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update) | 更新AR Engine的计算结果。 |
| [HMS\_AREngine\_ARSession\_Configure](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_configure) | 配置[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARFrame\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_create) | 创建一个新的[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到中\*outFrame。 |
| [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry) | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture) | 设置可用于存储相机预览流数据的openGL纹理。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem) | 从可跟踪列表中获取指定index的对象。 |
| [HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [HMS\_AREngine\_ARFrame\_AcquireCamera](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera) | 获取当前帧的相机参数对象。 |
| [HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create) | 分配并初始化一个新的位姿对象。 |
| [HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose) | 获取当前相机对象在AR世界空间中的位姿。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_create) | 创建一个空的跟踪图像数据。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_addimage) | 将图像添加到图像数据库并输出对应图像的索引。 |
| [HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize) | 获取此列表中的可跟踪对象的数量。 |
| [HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getcenterpose) | 获取跟踪图像中心点在世界坐标系中的位姿信息。 |
| [HMS\_AREngine\_ARAugmentedImage\_GetExtendX](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendx) | 以图像的中心点为坐标原点，获取在X轴上的宽度值。单位：米。 |
| [HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendz) | 以图像的中心点为坐标原点，获取在Z轴上的高度值。单位：米。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_serialize) | 序列化特征数据库，在添加完图片后，可以将特征库序列化为buffer，用户可以保存此buffer以供下次使用。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_deserialize) | 反序列化特征数据库，用户可以将上次生成的或者保存的buffer数据反序列化为特征数据库后直接使用。 |

## 开发步骤

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

首先创建一个起始UI页面“ARImage.ets”，设置两个按钮，用于实现“添加本地图片”和“读取本地数据库”两个功能，分别命名“ARImageByAdd.ets”和“ARImageByDatabase.ets”。配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { logger } from '../utils/Logger';

@Builder
export function ARImageBuilder() {
  ARImage();
}

@Component
struct ARImage {
  pageInfos: NavPathStack = new NavPathStack();
  private imagePathArray: string[] = [];

  build(): void {
    NavDestination() {
      Column() {
        Button($r('app.string.choose_local_image'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(async () => {

            try {
              let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
              photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
              photoOption.maxSelectNumber = 50;
              photoOption.isEditSupported = false;
              let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

              let photoResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoOption);
              if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
                this.imagePathArray = photoResult.photoUris;
                this.pageInfos.pushDestinationByName('ARImageByAdd', this.imagePathArray);
              }
            } catch (error) {
              const err: BusinessError = error as BusinessError;
              logger.error(`Failed to select by photoPicker. Code: ${err.code}, message is ${err.message}.`);
            }
          })

        Button($r('app.string.load_local_database'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.pageInfos.pushDestinationByName('ARImageByDatabase', null).catch((err: BusinessError) => {
              logger.error(
                `ARImageByDatabase Failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
            })
          })
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .width('100%')
      .height('100%')
    }
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

创建一个ARImageByAdd.ets，用于选择图片，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件加载相机预览画面，并定时触发每一帧绘制。

```typescript
import { taskpool } from '@kit.ArkTS';
import { display } from '@kit.ArkUI';
import { BusinessError, emitter, systemDateTime } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARImageByAddBuilder() {
  ARImageByAdd();
}

@Component
struct ARImageByAdd {
  pageInfos: NavPathStack = new NavPathStack();
  @State addImageLog: string = '';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State imageTotalNumbers: number = 0;
  @State rotation: number = 0;
  @State showPage: boolean = true;
  private imageAddFailedNumbers: number = 0;
  private imageAddNumbers: number = 0;
  private imagePathList: string[] = [];
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId: string = 'ARImage';
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State private isImageAddComplete: boolean = false;
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            logger.info(`XComponent onLoad ${this.idStr}.`);
            this.interval = setInterval(() => {
              if (!this.isUpdate || !this.isImageAddComplete || this.imageAddNumbers === 0) {
                return;
              }
              arEngineDemo.update(this.idStr);
            }, 33) // 将帧率设置为30fps（每33毫秒刷新一次帧）。
          })
          .onDestroy(() => {
            logger.info(`XComponent onDestroy ${this.idStr}.`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })

        Text(this.context.resourceManager.getStringByNameSync('add_image_msg_count') +
          this.imageTotalNumbers.toString() + '/' + this.imagePathList.length.toString() + '\n ' +
          this.context.resourceManager.getStringByNameSync('add_image_msg_success') +
          this.imageAddNumbers + ' \n' +
          this.context.resourceManager.getStringByNameSync('add_image_msg_fail') +
          this.imageAddFailedNumbers + '\n' + this.addImageLog)
          .width(300)
          .textAlign(TextAlign.Center)
          .fontColor(Color.Red)
          .visibility(!this.isImageAddComplete ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
    }
    .onBackPressed(() => {
      logger.error('Failed to onBackPressed.');
      return false;
    })
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);

      try {
        logger.info(`Image path length: ${this.imagePathList.length}.`);
        this.RegisterAddImageCallback();
        taskpool.execute(addImage, this.idStr, this.imagePathList, errcode).then(() => {
          logger.info('Add image task complete.');
          emitter.emit('checkAddImageResult');
        }).catch((err: BusinessError) => {
          logger.error(`Failed to execute taskpool. Code: ${err.code}, message is ${err.message}.`);
        })
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        logger.error(`Failed to promise options error. Code: ${err.code}, message is ${err.message}.`);
      }
    })
    .onWillDisappear(() => {
      if (this.imageAddNumbers > 0) {
        arEngineDemo.saveImageDataBaseToLocal(this.idStr, this.context.filesDir);
      }
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.idStr);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
      this.imagePathList = context.pathInfo.param as string[];
    })
    .hideTitleBar(true)
    .hideBackButton(false)
    .hideToolBar(true)
  }
  // ...
  private showDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: $r('app.string.warning'),
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect
        .asymmetric(TransitionEffect.OPACITY
          .animation({ duration: 1000, curve: Curve.Sharp })
          .combine(TransitionEffect
            .scale({ x: 1.5, y: 1.5 })
            .animation({ duration: 1000, curve: Curve.Sharp })
          ),
          TransitionEffect.OPACITY
            .animation({ duration: 100, curve: Curve.Smooth })
            .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
              .animation({ duration: 100, curve: Curve.Smooth })
            )
        ),
      buttons: [{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
        value: $r('app.string.back'),
        action: () => {
          logger.info('Callback when the second button is clicked');
          this.pageInfos.pop();
        }
      }]
    })
  }

  private RegisterAddImageCallback(): void {
    emitter.on('addImage', (data: emitter.EventData) => {
      if (data.data?.addImageReason === 0) {
        this.imageAddNumbers++;
        logger.info(`Succeeded in adding image, image numbers: ${this.imageAddNumbers}.`);
      } else {
        this.imageAddFailedNumbers++;
        try {
          this.addImageLog += this.context.resourceManager.getStringByNameSync('image_name_by_add') +
            data.data?.imageName + '\n' +
            this.context.resourceManager.getStringByNameSync('image_add_reason_by_add') +
            errcode.get(data.data?.addImageReason) + '\n';
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to set addImageLog. Code is ${err.code}, message is ${err.message}`);
        }
        logger.error(`Failed to add image, image numbers: ${this.imageAddFailedNumbers}.`);
      }
      this.imageTotalNumbers++;
    })

    emitter.on('checkAddImageResult', () => {
      if (this.imageAddNumbers === 0 && this.isUpdate) {
        this.showPage = false;
        try {
          this.showDialog(this.context.resourceManager.getStringByNameSync('invalid_image_added'));
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to getStringByNameSync. Code is ${err.code}, message is ${err.message}`);
        }
      }
      emitter.off('addImage');
      this.isImageAddComplete = true;
      emitter.off('checkAddImageResult');
    })
  }
}

let errcode: Map<number, string> = new Map<number, string>([[0, 'success'], [1, 'size not match'],
  [2, 'too bright or too dark'], [3, 'image color is relatively single'], [4, 'other error']]);

// 异步执行添加图片的任务。
@Concurrent
async function addImage(componentId: string, imagePathList: string[],
  errcode: Map<number, string>): Promise<void> {
  for (let index = 0; index < imagePathList.length; index++) {
    const magePath: string = imagePathList[index];
    let file: fileIo.File = fileIo.openSync(magePath, fileIo.OpenMode.READ_ONLY);
    let imageName: string = file.name;
    const imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
    try {
      fileIo.closeSync(file);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`Failed to closeSync. Code is ${err.code}, message is ${err.message}.`);
      imageSourceApi.release();
      continue;
    }
    const imageInfo: image.ImageInfo = imageSourceApi.getImageInfoSync();
    if (!imageInfo) {
      logger.error(`Failed to obtain the image pixel map information.`);
      imageSourceApi.release();
      continue;
    }
    const opts: image.DecodingOptions = {
      editable: true,
      desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
      desiredSize: { width: imageInfo.size.width, height: imageInfo.size.height }
    }
    const pixelMap: image.PixelMap = imageSourceApi.createPixelMapSync(opts);
    if (!pixelMap) {
      logger.error('Failed to create pixelMap.');
      imageSourceApi.release();
      continue;
    }
    const readBuffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
    await pixelMap.readPixelsToBuffer(readBuffer);
    pixelMap.release();

    let result: number = arEngineDemo.initImage(componentId, imageInfo.size.width, imageInfo.size.height, readBuffer);
    if (errcode.has(result) === false) {
      logger.error('Failed to add image, break.');
      imageSourceApi.release();
      break;
    }
    if (result !== 0) {
      logger.error(`Failed to Add image, reason is: ${errcode.get(result)}, imageName is: ${imageName}.`);
    }
    let eventData: emitter.EventData = {
      data: {
        'addImageReason': result,
        'imageName': imageName,
      }
    }
    emitter.emit('addImage', eventData);
    imageSourceApi.release();
  }
}
```

创建一个ARImageByDatabase.ets，用于加载本地数据库，加载相机预览画面，并定时触发每一帧绘制。

```typescript
import { display } from '@kit.ArkUI';
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARImageByDatabaseBuilder() {
  ARImageByDatabase();
}

@Component
struct ARImageByDatabase {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State rotation: number = 0;
  @State showPage: boolean = true;
  private isSurfaceDestroy: boolean = false;
  private interval: number = -1;
  private isUpdate: boolean = false;
  private xComponentId: string = 'ARImage';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .visibility(this.showPage ? Visibility.Visible : Visibility.None)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            logger.info(`XComponent onLoad ${this.idStr}.`);
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                arEngineDemo.update(this.idStr);
              }
            }, 33) // 将帧率设置为30fps（每33毫秒刷新一次帧）。
          })
          .onDestroy(() => {
            logger.info(`XComponent onDestroy ${this.idStr}.`);
            this.isSurfaceDestroy = true;
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);

      arEngineDemo.setPath(this.idStr, this.context.filesDir);

      let imageCountInDatabase: number = arEngineDemo.getImageCount(this.idStr);
      logger.info(`ImageCountInDatabase: ${imageCountInDatabase}.`);
      if (imageCountInDatabase <= 0) {
        try {
          this.showDialog(this.context.resourceManager.getStringByNameSync('invalid_image_added'));
        } catch (error) {
          const err: BusinessError = error as BusinessError;
          logger.error(`Failed to showDialog. Code is ${err.code}, message is ${err.message}`);
        }
      }
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      if (!this.isSurfaceDestroy) {
        arEngineDemo.hide(this.idStr);
      }
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  showDialog(msg: string): void {
    this.getUIContext().showAlertDialog({
      title: $r('app.string.warning'),
      message: msg,
      autoCancel: true,
      alignment: DialogAlignment.Center,
      offset: { dx: 0, dy: -20 },
      gridCount: 3,
      transition: TransitionEffect
        .asymmetric(TransitionEffect.OPACITY
          .animation({ duration: 1000, curve: Curve.Sharp })
          .combine(TransitionEffect
            .scale({ x: 1.5, y: 1.5 })
            .animation({ duration: 1000, curve: Curve.Sharp })
          ),
          TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
            .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
              .animation({ duration: 100, curve: Curve.Smooth })
            )
        ),
      buttons: [{
        enabled: true,
        defaultFocus: true,
        style: DialogButtonStyle.HIGHLIGHT,
        value: $r('app.string.back'),
        action: () => {
          logger.info('Callback when the second button is clicked.');
          this.pageInfos.pop();
        }
      }]
    })
  }
}
```

配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话

创建AR会话并配置ARType为图像跟踪。

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// 设置AR类型为ARENGINE_TYPE_IMAGE。
CHECK(HMS_AREngine_ARConfig_SetARType(mArSession, arConfig, ARENGINE_TYPE_IMAGE));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
```

### 创建跟踪图像数据库并添加图像

1.调用[HMS\_AREngine\_ARAugmentedImageDatabase\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_create)函数，创建跟踪图像数据库。

```
CHECK(HMS_AREngine_ARAugmentedImageDatabase_Create(&mDataBase));
```

2.调用[HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_addimage)函数，添加图像到数据库，将添加失败的结果保存在reason中。

```
AREngine_ARAugmentedImageSource image;
 // ...
uint32_t outputIndex = 0;
AREngine_ARAddAugmentedImageReason reason = ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE;
auto addRet = HMS_AREngine_ARAugmentedImageDatabase_AddImage(dataBase, &image, &outputIndex, &reason);
```

### 识别环境中的可跟踪图像

调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有跟踪图像，并将结果存放在augmentList中。

```
AREngine_ARTrackableList *augmentList = nullptr;
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &augmentList));
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_AUGMENTED_IMAGE, augmentList));
```

### 获取环境中的可跟踪图像数量

调用[HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)函数获取平面数量，结果存放在augmentSize中。

```
int32_t augmentSize = 0;
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, augmentList, &augmentSize));
```

应用环境中，可能存在0个、1个或多个可跟踪图像。

当augmentSize等于0时，表示当前环境中不存在可跟踪图像。

当augmentSize等于1时，表示当前环境中仅存在1个可跟踪图像。

当augmentSize大于1时，表示当前环境中存在多个可跟踪图像。

### 获取跟踪图像示例

当存在1个或多个跟踪图像时，可以依次遍历augmentList获取所有跟踪图像。

```cpp
for (int i = 0; i < augmentSize; ++i) {
    // ...
}
```

对于第i个跟踪图像，创建并获取跟踪对象，并将其转化为跟踪图像对象[AREngine\_ARAugmentedImage](../harmonyos-references/arengine-capi-arengine.md#arengine_araugmentedimage)。

```
AREngine_ARTrackable *augment = nullptr;
CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, augmentList, i, &augment));
AREngine_ARAugmentedImage *arImage = reinterpret_cast<AREngine_ARAugmentedImage*>(augment);
```

### 获取跟踪图像中心点在世界坐标系中的位姿信息

调用[HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getcenterpose)函数，获取跟踪图像中心点的位姿信息，位姿信息可参考[获取设备位姿](arengine-c-get-pose.md)。

```
AREngine_ARPose *imagePose = nullptr;
HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &imagePose);
auto getPoseResult = HMS_AREngine_ARAugmentedImage_GetCenterPose(arSession, image, imagePose);
```

### 获取跟踪图像的宽度

调用[HMS\_AREngine\_ARAugmentedImage\_GetExtendX](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendx)函数，获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到X轴上的估计值。

```
float extent_x;
HMS_AREngine_ARAugmentedImage_GetExtendX(arSession, image, &extent_x);
```

调用[HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendz)函数，获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到Z轴上的估计值。

```
float extent_z;
HMS_AREngine_ARAugmentedImage_GetExtendZ(arSession, image, &extent_z);
```
