---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-28
title: 如何提升自定义相机拍摄照片的质感
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何提升自定义相机拍摄照片的质感
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:8b9f4d41ef78533e8aae3a36a4828878b3767fd4afef9d32af368859dc385625
---

## 问题现象

自定义相机拍摄效果不佳，图片局部出现模糊类似磨皮效果，没有质感，不够细腻。

## 背景知识

* HarmonyOS支持调用接口拍摄[HDR Vivid](../harmonyos-guides/camera-hdr-shooting.md)照片，可以拍出层次表现更细腻、光影细节更丰富的画面，提升画面质感，呈现更卓越的视觉效果。
* [setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)：支持设置色彩空间应用可以下发不同的色彩空间(ColorSpace)参数来支持P3广色域以及HDR的功能。
* [申请相机开发的权限](../harmonyos-guides/camera-preparation.md)：在开发相机应用时，需要先申请相机相关权限，确保应用拥有访问相机硬件及其他功能的权限。

## 问题定位

应用中全局搜索setColorSpace，判断应用有无使用HDR Vivid的拍照功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_X9vblpER96uEhcTlAu89w/zh-cn_image_0000002628392570.png)

## 分析结论

应用中没有setColorSpace的相关设置，未使用HDR Vivid拍照的相关能力，导致拍摄出来的照片不够细腻，没有质感。

## 修改建议

应用开发的相机功能，使用HDR Vivid拍照的能力，确保拍摄出来的照片更加细腻有质感，简单示例如下：

Index.ets：

```ts
import { abilityAccessCtrl, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { router } from '@kit.ArkUI';

const TAG = '[CameraDemo]';

@Entry
@Component
struct Index {
  context = this.getUIContext();

  onJumpClick(){
    this.getUIContext().getRouter().pushUrl({
      url: 'pages/PhotoDemo'// 目标url
    }, router.RouterMode.Standard, (err) => {
      if (err) {
        console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
        return;
      }
      console.info('Invoke pushUrl succeeded.');
    });
  }
  checkPermissions(){
    let permissions: Array<Permissions> = [
      'ohos.permission.CAMERA'
    ];
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
    atManager.requestPermissionsFromUser(this.context?.getHostContext(), permissions).then((data: PermissionRequestResult) => {
      let grantStatus: Array<number> = data.authResults;
      let length: number = grantStatus.length;
      for (let i = 0; i < length; i++) {
        if (grantStatus[i] !== 0) {
          // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
          return;
        }
      }
      // 跳转拍照页
      this.onJumpClick();

      console.info(`${TAG} Success to request permissions from user. authResults is ${grantStatus}.`);
    }).catch((err: BusinessError) => {
      console.error(`${TAG} Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
    });
  }
  build() {
    Column({ space: 30 }) {
      Button('去拍照')
        .controlSize(ControlSize.NORMAL)
        .onClick(() => {
          this.checkPermissions();
        })
        .margin({ top: 30 })

    }
    .width('100%')
    .height('100%')
  }
}
```

PhotoDemo.ets:

注意：需要在src/main/resources/base/profile/main\_pages.json中配置对应PhotoDemo页面路径。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { camera } from '@kit.CameraKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';

const TAG = '[PhotoDemo]';

@Entry
@Component
struct PhotoDemo {
  context = this.getUIContext();
  @State hasPicture: boolean = false;
  @State finalPixelMap: image.PixelMap | undefined = undefined;
  // 设置安全控件按钮属性
  @State saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE_IMAGE,
    buttonType: ButtonType.Capsule
  };
  @State buffer: ArrayBuffer | undefined = undefined;
  @State surfaceId: string = '';
  @State imageSize: image.Size = { width: 640, height: 360 };
  private mXComponentController: XComponentController = new XComponentController;
  private cameraManager: camera.CameraManager | undefined = undefined;
  private cameraInput: camera.CameraInput | undefined = undefined;
  private photoOutput: camera.PhotoOutput | undefined = undefined;
  private previewOutput: camera.PreviewOutput | undefined = undefined;
  private cameraSession: camera.PhotoSession | undefined = undefined;
  private screenWidth: number = 1080;
  private screenHeight: number = 1080;

  aboutToAppear() {

  }

  build() {
    Column() {
      //设置返回键
      Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start }) {
        // 该图片为测试图片，自行替换相应图片
        Image($r('app.media.ic_public_back'))
          .width(30)
          .margin({ left: 16, bottom: 16 })
          .onClick(() => {
            this.getUIContext().getRouter().back();
          });
      };

      //预览框
      Column({ space: 20 }) {
        if (this.hasPicture) {
          Image(this.finalPixelMap)
            .objectFit(ImageFit.Fill)
            .width('100%')
            .height('80%');

          SaveButton(this.saveButtonOptions)// 创建安全控件按钮
            .onClick(async (event, result: SaveButtonOnClickResult) => {
              if (result === SaveButtonOnClickResult.SUCCESS) {
                if (this.finalPixelMap) {
                  try {
                    // 使用安全控件创建文件
                    let phAccessHelper: photoAccessHelper.PhotoAccessHelper =
                      photoAccessHelper.getPhotoAccessHelper(this.context?.getHostContext(),);
                    let options: photoAccessHelper.CreateOptions = {
                      title: Date.now().toString()
                    };
                    // createAsset的调用需要ohos.permission.READ_IMAGEVIDEO和ohos.permission.WRITE_IMAGEVIDEO的权限
                    let photoUri: string =
                      await phAccessHelper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png', options);
                    // 通过文件管理写入文件
                    let file = fs.openSync(photoUri, fs.OpenMode.WRITE_ONLY);

                    try {
                      fs.writeSync(file.fd, this.buffer);
                    } catch (error) {
                      let err: BusinessError = error as BusinessError;
                      console.error(`Invoke writeFile failed, code is ${err.code}, message is ${err.message}`);
                    } finally {
                      fs.closeSync(file);
                    }

                  } catch (error) {
                    let err = error as BusinessError;
                    console.error(TAG, 'isFileSaved failed with err: ' + JSON.stringify(err));
                  }
                }
              } else {
                console.error('CameraDemo SaveButtonOnClickResult createAsset failed.');
              }
              setTimeout(() => {
                this.hasPicture = false;
                this.finalPixelMap = undefined;
              }, 1000);
            });
        } else {
          XComponent({ type: XComponentType.SURFACE, controller: this.mXComponentController })
            .onLoad(() => {
              // 设置Surface宽高（1920*1080），预览尺寸设置参考previewProfilesArray获取的当前设备所支持的预览分辨率大小去设置
              let surfaceRect: SurfaceRect = {
                surfaceWidth: this.screenWidth,
                surfaceHeight: this.screenHeight
              };
              this.mXComponentController.setXComponentSurfaceRect(surfaceRect);
              // 获取Surface ID
              this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
              setTimeout(async () => {
                await this.prepareCamera();
              }, 500);
            })
            .backgroundColor(Color.Black)
            .width('100%')
            .height('75%');

          Button('拍照')
            .width(55)
            .height(57)
            .margin({ top: 32 })
            .borderRadius('50%')
            .backgroundColor(Color.White)
            .onClick(async () => {
              await this.releaseCamera();
              await this.prepareCamera();
            });

        }
      }
      .width('100%')
      .height('100%')
      .backgroundColor('#000')
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
  }

  async releaseCamera() {
    try {
      await this.previewOutput?.release();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG, `previewOutput release fail: error: ${err.message}`);
    } finally {
      this.previewOutput = undefined;
    }
    try {
      await this.photoOutput?.release();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG, `photoOutput release fail: error: ${err.message}`);
    } finally {
      this.photoOutput = undefined;
    }

    try {
      await this.cameraInput?.close();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG, `cameraInput close fail: error: ${err.message}`);
    } finally {
      this.cameraInput = undefined;
    }

    try {
      await this.cameraSession?.release();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG, `captureSession release fail: error: ${err.message}`);
    } finally {
      this.cameraSession = undefined;
    }
  }

  // 创建CameraManager对象
  createCameraManager() {
    try {
      let cameraManager: camera.CameraManager = camera.getCameraManager(this.context?.getHostContext());
      if (!cameraManager) {
        console.error('CameraDemo camera.getCameraManager error');
        return;
      }
      this.cameraManager = cameraManager;

      // 监听相机状态变化
      this.cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
        console.info(`CameraDemo camera: ${cameraStatusInfo.camera.cameraId}, status: ${cameraStatusInfo.status}`);
      });
    } catch (error) {
      console.error('CameraDemo camera.getCameraManager error');
    }
  }

  //函数中设置监听photoAvailable，在回调中生成图片
  setPhotoOutputCb(photoOutput: camera.PhotoOutput) {
    //设置回调之后，调用photoOutput的capture方法，就会将拍照的buffer回传到回调中
    photoOutput.on('photoAvailable', (errCode: BusinessError, photo: camera.Photo): void => {
      console.info(`CameraDemo getPhoto start. err: ${JSON.stringify(errCode)}`);
      if (errCode || photo === undefined || photo.main === undefined) {
        console.error('CameraDemo getPhoto failed');
        return;
      }
      let imageObj = photo.main;
      imageObj.getComponent(image.ComponentType.JPEG,
        async (errCode: BusinessError, component: image.Component): Promise<void> => {
          console.info('CameraDemo getComponent start');
          if (errCode || component === undefined) {
            console.error('CameraDemo getComponent failed');
            return;
          }
          let buffer: ArrayBuffer;
          if (component.byteBuffer) {
            buffer = component.byteBuffer;
            this.buffer = buffer;
            let sourceOptions: image.SourceOptions = {
              sourceDensity: 0, // 在不确定当前密度时传0
              sourcePixelFormat: image.PixelMapFormat.RGBA_8888,
              sourceSize: this.imageSize
            };
            let imageSource: image.ImageSource = image.createImageSource(buffer, sourceOptions);
            let opts: image.InitializationOptions = {
              editable: false,
              pixelFormat: image.PixelMapFormat.RGBA_8888,
              size: this.imageSize
            };
            let pixelMap = await imageSource.createPixelMap(opts);
            this.finalPixelMap = pixelMap;
          } else {
            console.error('CameraDemo byteBuffer is null');
            return;
          }
        });
    });
  }

  //相机准备
  async prepareCamera() {
    this.createCameraManager();
    if (!this.cameraManager) {
      console.error('CameraDemo cameraManager is undefined.');
      return;
    }

    // 获取设备支持的相机对象,根据位置可划分后置，前置，折叠态相机
    let cameraDevices: Array<camera.CameraDevice> = [];
    try {
      cameraDevices = this.cameraManager.getSupportedCameras();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo The getSupportedCameras call failed. error: ${JSON.stringify(err)}`);
    }

    cameraDevices.forEach((cameraDevice: camera.CameraDevice) => {
      console.info(`CameraDemo cameraId: ${cameraDevice.cameraId}, cameraPosition: ${cameraDevice.cameraPosition.toString()}, cameraType: ${cameraDevice.cameraType.toString()}, connectionType: ${cameraDevice.connectionType.toString()}`);
    });

    // 获取设备支持的具体某个相机对象的支持的模式类型，包含普通拍照及普通录像两种模式,cameraDevices[0]代表后置相机
    let cameraSceneModes: Array<camera.SceneMode> = [];
    try {
      cameraSceneModes = this.cameraManager.getSupportedSceneModes(cameraDevices[0]);
      cameraSceneModes.forEach((cameraSceneMode: camera.SceneMode) => {
        console.info(`CameraDemo cameraSceneMode: ${cameraSceneMode.toString()}`);
      });

      //判断支持的模式类型是否包含拍照
      let isSupportPhotoMode: boolean = cameraSceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
      if (!isSupportPhotoMode) {
        console.error('CameraDemo photo mode not support');
        return;
      }
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo The getSupportedSceneModes call failed. error: ${JSON.stringify(err)}`);
    }

    // 创建相机输入流
    try {
      this.cameraInput = this.cameraManager.createCameraInput(cameraDevices[0]);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo createCaptureSession error. error: ${JSON.stringify(err)}`);
      return;
    }
    // 监听cameraInput错误信息
    this.cameraInput.on('error', cameraDevices[0], (error: BusinessError) => {
      console.error(`CameraDemo Camera input error: ${JSON.stringify(error)}`);
    });

    // 打开相机
    try {
      await this.cameraInput.open();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo cameraInput open error. error: ${JSON.stringify(err)}`);
    }

    // 获取相机对象支持的输出流能力，包含预览，拍照，录像等信息
    let cameraOutputCapability: camera.CameraOutputCapability =
      this.cameraManager.getSupportedOutputCapability(cameraDevices[1], camera.SceneMode.NORMAL_VIDEO);
    if (!cameraOutputCapability) {
      console.error('CameraDemo cameraManager.getSupportedOutputCapability error');
      return;
    }

    //获取当前设备支持的预览能力
    let previewProfile: camera.Profile | undefined = cameraOutputCapability.previewProfiles[0];

    // 预览流和相片分辨率的宽高比要保持一致
    cameraOutputCapability.previewProfiles.forEach((profile) => {
      if (profile.size.width === this.imageSize.width && profile.size.height === this.imageSize.height) {
        previewProfile = profile;
        return;
      }
    });
    this.imageSize = previewProfile.size;

    // 创建相机预览输出流
    try {
      this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, this.surfaceId);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo createCaptureSession error. error: ${JSON.stringify(err)}`);
      return;
    }
    // 监听previewOutput错误信息
    this.previewOutput.on('error', (error: BusinessError) => {
      console.error(`CameraDemo previewOutput error: ${JSON.stringify(error)}`);
    });

    try {
      //获取当前设备支持的拍照能力
      let photoProfile = cameraOutputCapability.photoProfiles[0];
      //拍照流和相片分辨率的宽高比要保持一致
      cameraOutputCapability.photoProfiles.forEach((profile) => {
        if (profile.size.width === this.imageSize.width && profile.size.height === this.imageSize.height) {
          photoProfile = profile;
          return;
        }
      });

      //创建相机拍照输出流
      this.photoOutput = this.cameraManager.createPhotoOutput(photoProfile);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo createPhotoOutput error ${JSON.stringify(err)}`);
    }
    if (this.photoOutput === undefined) {
      console.error('CameraDemo photoOutput is undefined.');
      return;
    }

    //调用自定义函数，在定义的监听的回调中保存图片,该自定义函数需传参拍照输出流
    this.setPhotoOutputCb(this.photoOutput);

    //创建相机会话
    try {
      this.cameraSession = this.cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo createCaptureSession error. error: ${JSON.stringify(err)}`);
      return;
    }
    // 监听session错误信息
    this.cameraSession.on('error', (error: BusinessError) => {
      console.error(`CameraDemo Capture session error: ${JSON.stringify(error)}`);
    });

    // 开始配置会话
    try {
      this.cameraSession.beginConfig();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo beginConfig error. error: ${JSON.stringify(err)}`);
    }

    // 向会话中添加相机输入流
    try {
      this.cameraSession.addInput(this.cameraInput);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo addInput error. error: ${JSON.stringify(err)}`);
    }

    // 向会话中添加预览输出流
    try {
      this.cameraSession.addOutput(this.previewOutput);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo add previewOutput error. error: ${JSON.stringify(err)}`);
    }

    // 向会话中添加拍照输出流
    try {
      this.cameraSession.addOutput(this.photoOutput);
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo add photoOutput error. error: ${JSON.stringify(err)}`);
    }

    // 设置色彩空间
    this.setColorSpaceBeforeCommitConfig(this.cameraSession, true);

    // 提交会话配置
    try {
      await this.cameraSession.commitConfig();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo captureSession commitConfig error: ${JSON.stringify(err)}`);
    }

    // 启动会话
    try {
      await this.cameraSession.start();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`CameraDemo captureSession start error: ${JSON.stringify(err)}`);
    }
  }

  setColorSpaceBeforeCommitConfig(session: camera.PhotoSession, isHdr: boolean): void {
    let colorSpace: colorSpaceManager.ColorSpace =
      isHdr ? colorSpaceManager.ColorSpace.DISPLAY_P3 : colorSpaceManager.ColorSpace.SRGB;
    let colorSpaces: Array<colorSpaceManager.ColorSpace> = this.getSupportedColorSpaces(session);
    let isSupportedColorSpaces = colorSpaces.indexOf(colorSpace) >= 0;
    if (isSupportedColorSpaces) {
      console.info(`setColorSpace: ${colorSpace}`);
      try {
        session.setColorSpace(colorSpace);
        let activeColorSpace: colorSpaceManager.ColorSpace = session.getActiveColorSpace();
        console.info(`activeColorSpace: ${activeColorSpace}`);
      } catch (error) {
        console.info(`activeColorSpace: ${error}`);
      }

    } else {
      console.info(`colorSpace: ${colorSpace} is not support`);
    }
  }

  getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
    let colorSpaces: Array<colorSpaceManager.ColorSpace> = [];
    try {
      colorSpaces = session.getSupportedColorSpaces();
    } catch (error) {
      let err = error as BusinessError;
      console.error(`The getSupportedColorSpaces call failed. error code: ${err.code}`);
    }
    return colorSpaces;
  }
}
```

完整示例可参考[自定义相机预览示例代码](../harmonyos-guides/camera-preview.md#示例代码)。
