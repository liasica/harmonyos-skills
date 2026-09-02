---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-image-track
title: 图像跟踪（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 图像跟踪 > 图像跟踪（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:49+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:616b7c564103443a85b74d7a394b1c4692b9345a12e18df93bd22a0d1b6e5cf6
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

从5.1.0(18)开始，图像跟踪能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持图像跟踪特性（[ARENGINE\_FEATURE\_TYPE\_IMAGE](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

图像识别主要依赖[ARAugmentedImageDatabase](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabase)、[ARImage](../harmonyos-references/arengine-api-arengine.md#arimage)，以下接口为图像识别相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [arEngine.createARAugmentedImageDatabase](../harmonyos-references/arengine-api-arengine.md#arenginecreatearaugmentedimagedatabase) | 创建一个增强型图像数据库。 |
| [ARAugmentedImageDatabase.deserialize](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasedeserialize) | 将增强图像数据库数据反序列化为一个新的增强图像数据库对象。 |
| [ARAugmentedImageDatabase.serialize](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabaseserialize) | 将增强图像数据库序列化为一个缓冲区。 |
| [ARAugmentedImageDatabase.addImage](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabaseaddimage) | 将图像添加到图像数据库，并输出对应图像的索引。 |
| [ARAugmentedImageDatabase.getImageCount](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasegetimagecount) | 获取图像数据库中图像的数量。 |
| [ARAugmentedImageDatabase.getCapacity](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasegetcapacity) | 可以添加的最大图像数量。 |
| [ARAugmentedImageDatabase.getImageAddMode](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasegetimageaddmode) | 获取图片添加模式。 |
| [ARAugmentedImageDatabase.setImageAddMode](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasesetimageaddmode) | 设置图片添加模式。 |
| [ARAugmentedImageDatabase.release](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabaserelease) | 释放增强图像数据库对象[ARAugmentedImageDatabase](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabase)占用的内存。 |
| [ARImage.release](../harmonyos-references/arengine-api-arengine.md#arimagerelease) | 释放相机视频流帧对象[ARImage](../harmonyos-references/arengine-api-arengine.md#arimage)占用的内存。 |
| [ARAugmentedImage](../harmonyos-references/arengine-api-arengine.md#araugmentedimage) | 表示可被追踪的增强图像对象。 |

## 开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)绘制识别的平面。关于AGP的介绍可以查看[ArkGraphics 3D简介](arkgraphics3d-overview.md)和[AGP引擎](https://gitcode.com/openharmony/graphic_graphic_3d)。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 创建UI页面

首先创建一个初始UI页面“ARImage.ets”，设置两个按钮，用于实现“添加本地图片”和“读取本地数据库”两个功能，分别命名“ARImageByAdd.ets”和“ARImageByDatabase.ets”。并配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

### ARImage页面

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { logger } from '../utils/Logger';

@Builder
export function ARImageBuilder(): void {
  ARImage();
}

@Component
struct ARImage {
  pageInfos: NavPathStack = new NavPathStack();

  build(): void {
    NavDestination() {
      Column() {
        Button($r('app.string.choose_local_image'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.chooseImageToTrack();
          })

        Button($r('app.string.load_local_database'), { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .width('50%')
          .height('5%')
          .onClick(() => {
            this.loadDatabaseToTrack();
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

  private chooseImageToTrack(): void {
    try {
      let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
      photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
      photoOption.maxSelectNumber = 50; // 默认值
      photoOption.isEditSupported = false;
      let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

      photoPicker.select(photoOption).then((photoResult) => {
        if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
          this.pageInfos.pushDestinationByName('ARImageByAdd', photoResult.photoUris).catch((err: BusinessError) => {
            logger.error(`Failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
          });
        }
      }).catch((err: BusinessError) => {
        logger.warn(`Failed to select photos. Code is ${err.code}, message is ${err.message}.`);
      })
    } catch (error) {
      logger.error(`Failed to select by photoPicker. Code: ${error.code}.`);
    }
  }

  private loadDatabaseToTrack(): void {
    this.pageInfos.pushDestinationByName('ARImageByDatabase', null).catch((err: BusinessError) => {
      logger.error(`ARImageByDatabase failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
    })
  }
}
```

### ARImageByAdd页面

加载本地图片模式。

1. 选择本地图片进行图像识别能力所需要导入的模块如下：

   ```typescript
   import { arEngine, ARView, arViewController } from '@kit.AREngine';
   import {
     CustomGeometry,
     Geometry,
     Image,
     Material,
     MaterialType,
     MeshResource,
     Node,
     PrimitiveTopology,
     Scene,
     SceneResourceFactory,
     Shader,
     ShaderMaterial,
     Vec3
   } from '@kit.ArkGraphics3D';
   import { collections } from '@kit.ArkTS';
   import { Matrix4 } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { image } from '@kit.ImageKit';
   import { logger } from '../utils/Logger';
   import { calculatePoint, createImageIndex, getImageVertices, getResourceString } from '../utils/Utils';
   ```
2. 配置页面路由信息，定义数据库dataBase。

   ```typescript
   @Builder
   export function ARImageByAddBuilder(): void {
     ARImageByAdd();
   }

   let dataBase: arEngine.ARAugmentedImageDatabase;
   ```
3. 在设备界面上显示图片添加情况，无可用图片则弹窗提示，加载AR场景。

   ```typescript
   @Component
   struct ARImageByAdd {
     pageInfos: NavPathStack = new NavPathStack();
     @State arContext?: arViewController.ARViewContext = undefined;
     @State context: Context = this.getUIContext().getHostContext() as Context;
     @State addFailedImageCounts: number = 0;
     @State succeedImageCounts: number = 0;
     @State addFailedMessage: string[] = [];
     private imagePathArray: string[] = [];
     @State totalImageCounts: number = this.imagePathArray.length;
     // 当destroy设置为true时，addImage函数用于判断是否继续添加图片。
     private isProgramExits: boolean = false;
     private isSaveDatabase: boolean = false;

     build(): void {
       NavDestination() {
         RelativeContainer() {
           Column() {
             Text(`${getResourceString(this.context, 'add_image_msg_count')} ${this.succeedImageCounts +
               this.addFailedImageCounts} / ${this.totalImageCounts}`)
             Text(`${getResourceString(this.context, 'add_image_msg_success') + this.succeedImageCounts}`)
             Text(`${getResourceString(this.context, 'add_image_msg_fail') + this.addFailedImageCounts}`)

             if (this.addFailedMessage) {
               ForEach(this.addFailedMessage, (item: string) => {
                 Text(`${item}`)
                   .fontColor(Color.Red)
               }, (item: string) => item)
             }
           }
           .visibility(this.addFailedImageCounts + this.succeedImageCounts < this.totalImageCounts ? Visibility.Visible :
             Visibility.None)
           .foregroundColor(Color.Red)
           .zIndex(1)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })

           if (this.arContext) {
             ARView({ context: this.arContext })
               .height('100%')
               .width('100%')
               .alignRules({
                 center: { anchor: '__container__', align: VerticalAlign.Center },
                 middle: { anchor: '__container__', align: HorizontalAlign.Center }
               })
           }
         }
       }
       .onAppear(() => {
         arEngine.createARAugmentedImageDatabase()
           .then((arDataBase) => {
             dataBase = arDataBase;

             this.addImage(dataBase).then(() => {
               if (this.addFailedImageCounts === this.totalImageCounts) {
                 this.ShowDialog(getResourceString(this.context, 'invalid_image_added'));
               }
               if (this.totalImageCounts === this.succeedImageCounts + this.addFailedImageCounts) {
                 this.initARView();
                 this.isSaveDatabase = true;
               }
             })
           }).catch((err: BusinessError) => {
           logger.warn(`Failed to create database. Code is ${err.code}, message is ${err.message}`);
         })
       })
       .onWillDisappear(async () => {
         this.stopARView();
       })
       .onShown(() => {
         this.resumeARView();
       })
       .onHidden(() => {
         this.pauseARView();
       })
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
         this.imagePathArray = context.pathInfo.param as string[];
         this.totalImageCounts = this.imagePathArray.length;
       })
       .hideTitleBar(true)
       .hideBackButton(true)
       .hideToolBar(true)
     }

     // 异步执行添加图片的任务。
     async addImage(dataBase: arEngine.ARAugmentedImageDatabase): Promise<void> {
       // ...
     }

     private initARView(): void {
       // ...
     }

     private async stopARView(): Promise<void> {
       if (!this.arContext) {
         return;
       }
       try {
         this.isProgramExits = true;
         if (this.isSaveDatabase) {
           saveBufferToLocal(dataBase, this.context);
         }

         await dataBase.release();
         await this.arContext?.destroy();
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
       }
     }

     private resumeARView(): void {
       // ...
     }

     private pauseARView(): void {
       // ...
     }

     private ShowDialog(msg: string): void {
       // ...
     }
   }
   ```
4. 退出应用时，缓存图片特征到本地。

   ```typescript
   // 将文件保存到本地。
   async function saveBufferToLocal(dataBase: arEngine.ARAugmentedImageDatabase, context: Context): Promise<void> {
     let filesDir: string = context.filesDir;
     let file: fileIo.File;
     try {
       file = fileIo.openSync(filesDir + '/test.bin',
         fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       logger.error(`Failed to open database. Code is ${err.code}, message is ${err.message}.`);
       return;
     }
     let buf: ArrayBuffer;
     try {
       buf = await dataBase.serialize();
       try {
         let writeLen: number = fileIo.writeSync(file.fd, buf);
         logger.info(`The length of buffer is: ${writeLen}.`);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to write database. Code is ${err.code}, message is ${err.message}.`);
       }
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       logger.error(`Failed to serialize database. Code is ${err.code}, message is ${err.message}.`);
     }

     try {
       fileIo.closeSync(file);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       logger.error(`Failed to close database file. Code is ${err.code}, message is ${err.message}.`);
     }
   }
   ```
5. 调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，识别到目标图像则打印日志。

   ```typescript
   class ARViewCallbackImpl extends arViewController.ARViewCallback {
     // ...
     onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
     }

     onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
     }

     async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
       if (!ctx.session || !dataBase) {
         return;
       }

       let session: arEngine.ARSession = ctx.session;
       this.scene = ctx.scene;

       try {
         let imageNumber: number = dataBase.getImageCount();
         logger.info(`The number of images in the database is ${imageNumber}.`);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to get image count. Code is ${err.code}, message is ${err.message}`);
       }

       try {
         let imageCapacity: number = dataBase.getCapacity();
         logger.info(`The dataBase image capacity is: ${imageCapacity}.`);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to get capacity. Code is ${err.code}, message is ${err.message}`);
       }

       let trackables: arEngine.ARTrackable[];
       try {
         trackables = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to get capacity. Code is ${err.code}, message is ${err.message}`);
         return;
       }

       // 目标图像颜色由plane.shader文件控制。
       let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
       this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
       this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/plane.shader') });
       this.material.colorShader = this.shader;
       (this.material as CustomerMaterial).blend = { enabled: true };

       logger.info(`The image trackable size: ${trackables.length}.`);
       let validImage: number = 0;
       for (let i = 0; i < trackables.length; ++i) {
         if (trackables[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
           let arImage: arEngine.ARAugmentedImage = trackables[i] as arEngine.ARAugmentedImage;
           if (arEngine.ARTrackingState.TRACKING !== arImage.state) {
             continue;
           }
           validImage += 1;
           let centerPose: arEngine.ARPose;
           try {
             centerPose = arImage.getPose();
           } catch (error) {
             const err: BusinessError = error as BusinessError;
             logger.error(`Failed to get pose. Code is ${err.code}, message is ${err.message}`);
             return;
           }
           // ...
         }
       }
       // ...
     }
   }

   const errcode: collections.Map<number, string> = new collections.Map<number, string>([
     [0, 'success'],
     [1, 'size not match'],
     [2, 'too bright or too dark'],
     [3, 'image color is relatively single'],
     [4, 'other error']
   ])
   ```

### ARImageByDatabase页面

加载本地数据库模式。

1. 选择本地数据库进行图像识别能力所需要导入的模块如下：

   ```typescript
   import { arEngine, ARView, arViewController } from '@kit.AREngine';
   import {
     CustomGeometry,
     Geometry,
     Image,
     Material,
     MaterialType,
     MeshResource,
     Node,
     PrimitiveTopology,
     Scene,
     SceneResourceFactory,
     Shader,
     ShaderMaterial,
     Vec3
   } from '@kit.ArkGraphics3D';
   import { Matrix4 } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo, ReadOptions } from '@kit.CoreFileKit';
   import { logger } from '../utils/Logger';
   import { calculatePoint, createImageIndex, getImageVertices } from '../utils/Utils';
   ```
2. 配置页面路由信息，定义数据库dataBase。

   ```typescript
   @Builder
   export function ARImageByDatabaseBuilder(): void {
     ARImageByDatabase();
   }

   let dataBase: arEngine.ARAugmentedImageDatabase;
   ```
3. 加载AR场景，加载图像数据库，无可用数据库则弹窗提示。

   ```typescript
   @Component
   struct ARImageByDatabase {
     pageInfos: NavPathStack = new NavPathStack();
     @State arContext?: arViewController.ARViewContext = undefined;
     @State context: Context = this.getUIContext().getHostContext() as Context;

     build() {
       NavDestination() {
         RelativeContainer() {
           if (this.arContext) {
             ARView({ context: this.arContext })
               .height('100%')
               .width('100%')
               .alignRules({
                 center: { anchor: '__container__', align: VerticalAlign.Center },
                 middle: { anchor: '__container__', align: HorizontalAlign.Center }
               })
           }
         }
       }
       .onAppear(() => {
         arEngine.createARAugmentedImageDatabase()
           .then((arDataBase) => {
             dataBase = arDataBase;

             try {
               let databaseBuffer: ArrayBuffer = readBuffer(this.context);
               dataBase.deserialize(databaseBuffer).then(() => {
                 this.initARView();
               })
                 .catch((err: BusinessError) => {
                   logger.error(`Failed to deserialize database. Code is ${err.code}, message is ${err.message}.`);
                 })
             } catch (error) {
               const err: BusinessError = error as BusinessError;
               logger.error(`Failed to init context. Code is ${err.code}, message is ${err.message}.`);
               this.ShowDialog(this.context.resourceManager.getStringByNameSync('invalid_image_added'));
             }
           })
           .catch((err: BusinessError) => {
             logger.warn(`Failed to create database. Code is ${err.code}, message is ${err.message}`);
           })
       })
       .onWillDisappear(async () => {
         this.stopARView();
       })
       .onShown(() => {
         this.resumeARView();
       })
       .onHidden(() => {
         this.pauseARView();
       })
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
       })
       .hideTitleBar(true)
       .hideBackButton(true)
       .hideToolBar(true)
     }

     ShowDialog(msg: string): void {
       this.getUIContext().showAlertDialog({
         title: $r('app.string.warning'),
         message: msg,
         autoCancel: true,
         alignment: DialogAlignment.Center,
         offset: { dx: 0, dy: -20 },
         gridCount: 3,
         transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
           .animation({ duration: 1000, curve: Curve.Sharp })
           .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 })
             .animation({ duration: 1000, curve: Curve.Sharp })),
           TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
             .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
               .animation({ duration: 100, curve: Curve.Smooth }))),
         buttons: [{
           enabled: true,
           defaultFocus: true,
           style: DialogButtonStyle.HIGHLIGHT,
           value: $r('app.string.back'),
           action: () => {
             logger.info('Callback when the second button is clicked.');
             this.pageInfos.pop();
             return;
           }
         }]
       })
     }

     private initARView(): void {
       Scene.load().then(async (scene: Scene) => {
         let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
         viewContext.scene = scene;
         viewContext.callback = new ARViewCallbackImpl();
         viewContext.config = {
           type: arEngine.ARType.IMAGE,
           planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
           powerMode: arEngine.ARPowerMode.NORMAL,
           semanticMode: arEngine.ARSemanticMode.NONE,
           poseMode: arEngine.ARPoseMode.GRAVITY,
           depthMode: arEngine.ARDepthMode.AUTOMATIC,
           meshMode: arEngine.ARMeshMode.DISABLED,
           focusMode: arEngine.ARFocusMode.AUTO
         }
         viewContext.init().then(() => {
           this.arContext = viewContext;
           logger.info('Succeeded in initting ARView.');
         }).catch((err: BusinessError) => {
           logger.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
         })
       })
     }

     private async stopARView(): Promise<void> {
       if (!this.arContext) {
         return;
       }
       try {
         await dataBase.release();
         await this.arContext?.destroy();
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
       }
     }

     private resumeARView(): void {
       // ...
     }

     private pauseARView(): void {
       // ...
     }
   }
   ```
4. 读取本地数据库缓存文件的方法。

   ```typescript
   // 将本地文件读取到缓冲区。
   function readBuffer(context: Context): ArrayBuffer {
     let filesDir: string = context.filesDir;
     let srcFile: fileIo.File;
     try {
       srcFile = fileIo.openSync(filesDir + '/test.bin', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       logger.error(`Failed to open file. Code is ${err.code}, message is ${err.message}.`);
       return new ArrayBuffer(0);
     }
     let fileStat: fileIo.Stat;
     let buf: ArrayBuffer;
     try {
       fileStat = fileIo.statSync(srcFile.fd);
       // 读取源文件的内容并写入目标文件。
       let readSize: number = 0;
       buf = new ArrayBuffer(fileStat.size);
       let readOptions: ReadOptions = {
         offset: readSize,
         length: fileStat.size
       }
       try {
         fileIo.readSync(srcFile.fd, buf, readOptions);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to read buffer. Code is ${err.code}, message is ${err.message}.`);
       }
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       logger.error(`Failed to get file stat. Code is ${err.code}, message is ${err.message}.`);
       return new ArrayBuffer(0);
     }

     try {
       fileIo.closeSync(srcFile);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       logger.error(`Failed to close database file. Code is ${err.code}, message is ${err.message}.`);
     }
     return buf;
   }
   ```
5. 调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，识别到目标图像则打印日志。

   ```typescript
   class ARViewCallbackImpl extends arViewController.ARViewCallback {
     // ...
     onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
     }

     onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
     }

     async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
       if (!ctx.session || !dataBase) {
         return;
       }

       let session: arEngine.ARSession = ctx.session;
       this.scene = ctx.scene;

       try {
         let imageNumber: number = dataBase.getImageCount();
         logger.info(`The number of images in the database is ${imageNumber}.`);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to got image count. Code is ${err.code}, message is ${err.message}.`);
       }

       try {
         let imageCapacity: number = dataBase.getCapacity();
         logger.info(`The dataBase image capacity = ${imageCapacity}.`);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to getCapacity. Code is ${err.code}, message is ${err.message}`);
       }

       let trackables: arEngine.ARTrackable[] = [];
       try {
         trackables = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);
       } catch (error) {
         const err: BusinessError = error as BusinessError;
         logger.error(`Failed to get all trackables. Code is ${err.code}, message is ${err.message}`);
       }

       // 目标图像颜色由plane.shader文件控制。
       let rf: SceneResourceFactory = ctx.scene.getResourceFactory();
       this.material = await rf.createMaterial({ name: 'CustomMaterial' }, MaterialType.SHADER);
       this.shader = await rf.createShader({ name: 'CustomShader', uri: $rawfile('shaders/custom_shader/plane.shader') });
       this.material.colorShader = this.shader;
       (this.material as CustomerMaterial).blend = { enabled: true };

       logger.info(`The image trackable size: ${trackables.length}.`);
       let validImage: number = 0;
       for (let i = 0; i < trackables.length; ++i) {
         if (trackables[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
           let arImage: arEngine.ARAugmentedImage = trackables[i] as arEngine.ARAugmentedImage;
           if (arEngine.ARTrackingState.TRACKING !== arImage.state) {
             continue;
           }
           validImage++;
           let centerPose: arEngine.ARPose;
           try {
             centerPose = arImage.getPose();
           } catch (error) {
             const err: BusinessError = error as BusinessError;
             logger.error(`Failed to get pose. Code is ${err.code}, message is ${err.message}`);
             return;
           }
           // ...
         }
       }
       // ...
     }
   }
   ```
