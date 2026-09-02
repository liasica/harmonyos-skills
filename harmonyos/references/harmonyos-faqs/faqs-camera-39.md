---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-39
title: 自定义相机拍照如何自定义快门声音
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 自定义相机拍照如何自定义快门声音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f17d45b8c1f25bfa1bae7d61c47b89a7ad1d2964442ef8f670de5b632cbb3e5b
---

## 问题现象

在自定义相机中，自定义快门声音可以让用户根据个人喜好选择不同的快门声音，获得更加个性化的体验，如何自定义快门声音？

## 背景知识

* [自定义相机拍照](../harmonyos-guides/camera-shooting.md)前需要创建拍照输出流、进行拍照设置（如图片质量、旋转角度、是否镜像等），然后再调用[capture](../harmonyos-references/arkts-apis-camera-photooutput.md#capture-3)方法将拍照设置传递到拍照输出流中。
* 应用开发时，经常需要使用一些急促简短的音效（如相机快门音效、系统通知音效等），此时可以使用[SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#soundpool)实现一次加载、多次低时延播放，详情可以参考[使用SoundPool播放短音频](../harmonyos-guides/using-soundpool-for-playback.md)。

## 解决方案

1. 定义SoundPoolUtil类，使用SoundPool完成快门音效的播放。

   ```ts
   import { media } from '@kit.MediaKit';
   import { audio } from '@kit.AudioKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const DOMAIN: number = 0x0000;
   const TAG: string = '[SoundPoolPage]';

   export class SoundPoolUtil {
     private soundPool: media.SoundPool | undefined = undefined;
     private soundId: number = 0;
     private streamId: number = 0;
     private currentContext: Context;

     constructor(uiContext: Context) {
       this.currentContext = uiContext;
       this.create();
     }

     async create() {
       try {
         // audioRenderInfo中的参数usage取值为STREAM_USAGE_UNKNOWN，STREAM_USAGE_MUSIC，STREAM_USAGE_MOVIE
         // STREAM_USAGE_AUDIOBOOK时，SoundPool播放短音时为混音模式，不会打断其他音频播放
         let audioRendererInfo: audio.AudioRendererInfo = {
           usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐
           rendererFlags: 1 // 音频渲染器标志
         };
         // 创建soundPool实例
         this.soundPool = await media.createSoundPool(14, audioRendererInfo);
         // 注册监听
         this.loadCallback();
         this.finishPlayCallback();
         this.setErrorCallback();

         // 加载音频资源，开发者需要在resources/rawfile目录下替换成快门音频资源
         let fileDescriptor = await this.currentContext!.resourceManager.getRawFd('shutter.mp3');
         hilog.info(DOMAIN, TAG, `Successfully get the fileDescriptor: ${fileDescriptor}`);
         this.soundId = await this.soundPool!.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
         hilog.info(DOMAIN, TAG, `Successfully load soundPool soundId: ${this.soundId}`);
       } catch (e) {
         hilog.error(DOMAIN, TAG, `CreateSoundPool error: ${e}`);
       }
     }

     async loadCallback() {
       // 加载完成回调
       this.soundPool!.on('loadComplete', (soundId_: number) => {
         this.soundId = soundId_;
         hilog.info(DOMAIN, TAG, `Successfully loadComplete soundId: ${soundId_}`);
       });
     }

     // 设置播放完成监听
     async finishPlayCallback() {
       this.soundPool!.on('playFinished', () => {
         hilog.info(DOMAIN, TAG, 'receive play finished message');
       });
     }

     // 设置错误类型监听
     async setErrorCallback() {
       this.soundPool!.on('error', (error: BusinessError) => {
         hilog.error(DOMAIN, TAG, `error happened,message is: ${error.code}`);
         hilog.error(DOMAIN, TAG, `error happened,message is: ${error.message}`);
       });
     }

     async PlaySoundPool() {
       let playParameters: media.PlayParameters = {
         loop: 0, // 循环0次，即播放1次
         rate: 1, // 1倍速播放
         leftVolume: 0.5, // 取值范围0.0-1.0
         rightVolume: 0.5, // 取值范围0.0-1.0
         priority: 0, // 最低优先级
       };
       // 开始播放，请在音频资源加载完毕，即收到loadComplete回调之后再执行play操作
       this.soundPool!.play(this.soundId, playParameters, (error, streamID: number) => {
         if (error) {
           hilog.error(DOMAIN, TAG, `play sound Error: errCode is ${error.code}, errMessage is ${error.message}`);
         } else {
           this.streamId = streamID;
           hilog.info(DOMAIN, TAG, `play success soundid: ${this.streamId}`);
         }
       });

       // 设置循环播放次数
       await this.soundPool!.setLoop(this.streamId, 1);
       // 设置对应流的优先级
       await this.soundPool!.setPriority(this.streamId, 1);
       // 设置音量
       await this.soundPool!.setVolume(this.streamId, 0.5, 0.5);
     }

     async release() {
       // 终止指定流的播放
       await this.soundPool!.stop(this.streamId);
       // 卸载音频资源
       await this.soundPool!.unload(this.soundId);
       // 关闭监听
       this.setOffCallback();
       // 释放SoundPool
       await this.soundPool!.release();
     }

     async setOffCallback() {
       this.soundPool!.off('loadComplete');
       this.soundPool!.off('playFinished');
       this.soundPool!.off('error');
     }
   }
   ```
2. 定义相机管理类CameraShooter，完成相机会话配置、拍照、保存至媒体库等操作：

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   import { colorSpaceManager } from '@kit.ArkGraphics2D';
   import { image } from '@kit.ImageKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const DOMAIN: number = 0x0000;
   const TAG: string = '[CameraShooterPage]';

   let previewOutput: camera.PreviewOutput;
   let cameraInput: camera.CameraInput;
   let photoSession: camera.PhotoSession;
   let photoOutPut: camera.PhotoOutput;
   let currentContext: Context;
   // 期望的拍照图片尺寸
   let imageSize: image.Size = { width: 1920, height: 1440 };

   export async function cameraShooting(cameraPosition: number, surfaceId: string, context: Context): Promise<void> {
     currentContext = context;
     releaseCamera();
     try {
       // 获取相机管理对象
       let cameraManager: camera.CameraManager = camera.getCameraManager(context);
       let cameraArray: camera.CameraDevice[] = cameraManager.getSupportedCameras();
       if (cameraArray.length <= 0) {
         hilog.error(DOMAIN, TAG, 'No camera devices found!');
         return;
       }
       // 创建相机输入流
       cameraInput = cameraManager.createCameraInput(cameraArray[cameraPosition]);
       await cameraInput.open();
       // 获取支持的相机模式
       let sceneModes: camera.SceneMode[] = cameraManager.getSupportedSceneModes(cameraArray[cameraPosition]);
       // 获取支持的相机输出能力
       let cameraOutputCap: camera.CameraOutputCapability =
         cameraManager.getSupportedOutputCapability(cameraArray[cameraPosition], camera.SceneMode.NORMAL_PHOTO);
       let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
       if (!isSupportPhotoMode) {
         hilog.error(DOMAIN, TAG, 'No supported photo mode found!');
         return;
       }
       if (!cameraOutputCap) {
         hilog.error(DOMAIN, TAG, 'No supported camera OutputCap found!');
         return;
       }
       // 获取预览流的Profile列表
       let previewProfilesArray: camera.Profile[] = cameraOutputCap.previewProfiles;
       // 创建预览输出流，surfaceId为显示组件的id
       let previewProfile: camera.Profile | undefined = undefined;
       for (let index = previewProfilesArray.length - 1; index >= 0; index--) {
         if (previewProfilesArray[index].size.width / previewProfilesArray[index].size.height ===
           imageSize.width / imageSize.height) {
           previewProfile = previewProfilesArray[index];
           break;
         }
       }

       previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);
       if (previewOutput === undefined) {
         return;
       }

       // 获取支持的拍照流profile
       let photoProfilesArray: camera.Profile[] = cameraOutputCap.photoProfiles.slice().reverse();
       let photoProfile: camera.Profile | undefined = undefined;
       if (previewProfile !== undefined) {
         // 选择与预览流分辨率宽高比一致的拍照流分辨率
         photoProfile = photoProfilesArray.find((profile: camera.Profile) => {
           return profile.size.height * previewProfile!.size.width === previewProfile!.size.height * profile.size.width;
         });
       }
       // 获取支持的拍照输出能力
       photoOutPut = cameraManager.createPhotoOutput(photoProfile);

       if (photoOutPut === undefined) {
         return;
       }
       // 保存图片
       setPhotoOutputCb(photoOutPut);
       // 创建相机会话
       photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
       if (photoSession === undefined) {
         return;
       }
       // 开始相机会话
       photoSession.beginConfig();
       photoSession.addInput(cameraInput);
       photoSession.addOutput(previewOutput);
       photoSession.addOutput(photoOutPut);
       photoSession.setColorSpace(colorSpaceManager.ColorSpace.DISPLAY_P3);
       await photoSession.commitConfig();
       await photoSession.start();
     } catch (error) {
       hilog.error(DOMAIN, TAG, `The cameraShooting call failed. error: ${JSON.stringify(error)}`);
     }
   }

   // 拍照方法
   export async function capture(isFront: boolean) {
     try {
       let settings: camera.PhotoCaptureSetting = {
         quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
         rotation: camera.ImageRotation.ROTATION_0,
         mirror: isFront
       };
       photoOutPut.capture(settings);
     } catch (error) {
       hilog.error(DOMAIN, TAG, `The capture call failed. error: ${error.code}`);
     }
   }

   // 释放相机相关资源
   export async function releaseCamera(): Promise<void> {
     try {
       if (photoSession) {
         photoSession.stop();
       }
       if (cameraInput) {
         cameraInput.close();
       }
       if (previewOutput) {
         previewOutput.release();
       }
       if (photoSession) {
         photoSession.release();
       }
       if (photoOutPut) {
         photoOutPut.off('photoAssetAvailable');
         photoOutPut.off('captureReady');
         photoOutPut.release();
       }
     } catch (error) {
       hilog.error(DOMAIN, TAG, `The releaseCamera call failed. error: ${error.code}`);
     }
   }

   // 拍照后将图片保存至媒体库
   export function setPhotoOutputCb(photoOutput: camera.PhotoOutput): void {
     photoOutput.on('photoAssetAvailable',
       async (_err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): Promise<void> => {
         let accessHelper: photoAccessHelper.PhotoAccessHelper =
           photoAccessHelper.getPhotoAccessHelper(currentContext);
         let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
           new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
         try {
           assetChangeRequest.saveCameraPhoto();
           await accessHelper.applyChanges(assetChangeRequest);
           AppStorage.setOrCreate('photoUri', await photoAsset.getThumbnail());
         } catch (error) {
           hilog.error(DOMAIN, TAG, `The setPhotoOutputCb call failed. error: ${error.code}`);
         }
       });
   }
   ```
3. 在主页面中引入SoundPoolUtil类和CameraShooter类，并在点击拍照时调用SoundPool播放函数：

   ```ts
   import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
   import { display } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import {
     cameraShooting, capture,
   } from '../utils/CameraShooter';
   import { SoundPoolUtil } from '../utils/SoundPoolUtil';

   const DOMAIN: number = 0x0000;
   const TAG: string = '[XComponentPage]';

   let cameraPosition = 0;
   let surfaceId = '';
   let storage = new LocalStorage();

   @Component
   @Entry(storage)
   export struct CameraPage {
     mXComponentController: XComponentController = new XComponentController;
     permissions: Array<Permissions> = [
       'ohos.permission.CAMERA',
     ];
     private isFront: boolean = false;
     // 全局context
     private context: Context = this.getUIContext().getHostContext()!;
     private displayWidth = display.getDefaultDisplaySync().width;
     private soundPoolUtil = new SoundPoolUtil(this.context);

     async aboutToAppear() {
       try {
         // 在aboutToAppear页面申请相机权限
         abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.permissions).then(() => {
           setTimeout(() => {
             cameraShooting(cameraPosition, surfaceId, this.context);
           }, 200);
         });
       } catch (error) {
         hilog.error(DOMAIN, TAG, `The cameraShooting failed. error: ${JSON.stringify(error)}`);
       }
     }

     build() {
       RelativeContainer() {
         // XComponent主视图
         XComponent({
           type: XComponentType.SURFACE,
           controller: this.mXComponentController
         })
           .onLoad(async () => {
             this.mXComponentController.setXComponentSurfaceRect({
               surfaceWidth: this.displayWidth,
               surfaceHeight: this.displayWidth * 4 / 3
             });
             surfaceId = this.mXComponentController.getXComponentSurfaceId();
           })

         Row() {
           Stack() {
             // 拍照按钮
             Image($r('app.media.capture'))
               .height(70)
               .onClick(() => {
                 capture(this.isFront);
                 // 播放自定义快门声音
                 this.soundPoolUtil?.PlaySoundPool();
               })
           }
         }
         .id('controlPanel')
         .width('100%')
         .justifyContent(FlexAlign.SpaceAround)
         .alignRules({
           bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
         })
         .margin({ bottom: '40vp' })
       }
       .height('100%')
       .backgroundColor(Color.Black)
     }
   }

   export async function fromBack(context: Context): Promise<void> {
     cameraShooting(cameraPosition, surfaceId, context);
   }
   ```
