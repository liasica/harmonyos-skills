---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-35
title: 如何解决自定义扫码界面创建的截图与预览流中不一致问题
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何解决自定义扫码界面创建的截图与预览流中不一致问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a542f8d891f772ea51e4e6372caaf301d76578a9476e6f1f6fca9b036cef97cf
---

## 问题现象

自定义相机，使用createPixelMapFromSurface创建XComponent的截图和自定义扫码预览流XComponent中显示的不一致，createPixelMapFromSurface创建的截图不完整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/GghghiX5SAC8VpRPpbyM_Q/zh-cn_image_0000002658791851.png "点击放大")

## 背景知识

* 开发者可通过XComponent显示[自定义界面扫码](../harmonyos-guides/scan-customscan.md)。
* [image.createPixelMapFromSurface](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmapfromsurface11)这个方法可以通过传入XComponent的surfaceId，以及region选定区域的信息来获取XComponent显示的截图。
* 相机预览流支持的像素获取[cameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability).previewProfiles。
* [ViewControl](../harmonyos-references/scan-customscan-api.md#viewcontrol)相机控制参数。width和height需和XComponent的保持一致，start接口根据设置宽高值会匹配最接近相机分辨率。

## 问题定位

按照如下步骤进行排查：

1. 查看自定义扫码中预览流的宽高比。

   ```ts
   [GetPreviewBufferMeta:648] surface buffer info width: 1280, height: 960, stride: 1280, actualSize: 1847296,
   ```
2. 若XComponent的宽高是根据自定义的大小设置的，自定义扫码返回的预览流中size大小和XComponent实际的size大小是不一致的。比如现在使用XComponent的宽是1216px、高是1478px，但是其实扫码预览流实际宽为1280px、高为960px，XComponent对预览流进行了拉伸处理。
3. 如果image.createPixelMapFromSurface截图的image.Region设置为XComponent的宽高，截图就只会截取部分相机返回的预览流，因此推断像素不对导致截取的图片不对。

## 分析结论

截图像素区域设置不正确导致截取的图片不对，问题代码如下：

获取的是XComponent的宽高而不是预览流的宽高。

```ts
.onAreaChange((oldValue: Area, newValue: Area) => {
  this.xComponentWidth = newValue.width as number
  this.xComponentHeight = newValue.height as number
})
width: this.xComponentWidth } }
```

```ts
let region: image.Region = { x: 0, y: 0, size: { height: this.xComponentHeight, width: this.xComponentWidth } }
```

## 修改建议

通过相机预览回调的宽高设置createPixelMapFromSurface的image.Region。

1. 获取自定义扫码界面回调的[相机预览流](../harmonyos-references/scan-customscan-api.md#scanframe)。代码示例如下：

   ```ts
   private frameCallback: AsyncCallback<customScan.ScanFrame> =
     async (error: BusinessError, scanFrame: customScan.ScanFrame) => {
       if (error) {
         console.error(`Failed to get ScanFrame by callback. Code: ${error.code}, message: ${error.message}`);
         return;
       } else {
         if (this.previewHeight === scanFrame.height && this.previewWidth === scanFrame.width) {
           return;
         }
         this.previewHeight = scanFrame.height;
         this.previewWidth = scanFrame.width;

         // 通过setXComponentSurfaceRect设置surfaceRect，避免xComponent拉伸预览流
         let aspectRatio = 1478 / 1216;
         let resultRatio = scanFrame.width / scanFrame.height;
         let surfaceWidth = 0;
         let surfaceHeight = 0;
         let offsetX = 0;
         let offsetY = 0;

         if (resultRatio <= aspectRatio) {
           surfaceWidth = xComponentWidth;
           surfaceHeight = xComponentWidth * resultRatio;
           offsetX = 0;
           offsetY = (xComponentHeight - surfaceHeight) / 2;
         } else {
           surfaceWidth = xComponentHeight / resultRatio;
           surfaceHeight = xComponentHeight;
           offsetX = (xComponentWidth - surfaceWidth) / 2;
           offsetY = 0;
         }

         this.mXComponentController.setXComponentSurfaceRect({
           offsetX,
           offsetY,
           surfaceWidth,
           surfaceHeight
         });
       }
     };
   ```
2. 获取相机预览流的宽高后设置image.Region的宽高。

   ```ts
   let region: image.Region =
     { x: 0, y: 0, size: { height: this.previewHeight, width: this.previewWidth } };
   image.createPixelMapFromSurface(this.surfaceId, region).then(async (pixmap: image.PixelMap) => {
     console.info('Succeeded in creating pixelmap from Surface');
     await pixmap.rotate(90);
     this.pixmap = pixmap;
   }).catch((error: BusinessError) => {
     console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
   });
   ```

完整示例代码：

```ts
import { customScan, scanBarcode, scanCore } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { abilityAccessCtrl, bundleManager, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { AsyncCallback } from '@ohos.base';

const xComponentWidth = 1216;
const xComponentHeight = 1478;
const permissions: Array<Permissions> = ['ohos.permission.CAMERA'];

@Entry
@Component
struct CustomCameraPage {
  private mXComponentController: XComponentController = new XComponentController();
  private surfaceId?: string; //内部实现，不需要初始化
  private viewControl?: customScan.ViewControl; //内部实现，不需要初始化
  @State @Watch('startScan') isPageShow: boolean = false;
  @State @Watch('startScan') isLoaded: boolean = false;
  @State previewHeight: number = 400; //单位像素px
  @State previewWidth: number = 400; //单位像素px
  @State pixmap: PixelMap | undefined = undefined; //单位像素px
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  async checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

    // 获取应用程序的accessTokenID。
    let tokenId: number = 0;
    try {
      let bundleInfo: bundleManager.BundleInfo =
        await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
      let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      tokenId = appInfo.accessTokenId;
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to get bundle info for self, code: ${err.code}, message: ${err.message}`);
    }

    // 校验应用是否被授予权限。
    try {
      grantStatus = await atManager.checkAccessToken(tokenId, permission);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
    }
    return grantStatus;
  }

  startScan() {
    if (this.isPageShow && this.isLoaded) {
      if (this.viewControl != undefined) {
        this.checkPermissionAndInitCamera();
      }
    } else {
      this.releaseCamera();
    }
  }

  releaseCamera() {
    try {
      customScan.release().then(() => {
        console.info('Succeeded in releasing scan by promise');
      }).catch((error: BusinessError) => {
        console.error(`Failed to release scan by promise. Code: ${error.code}, message: ${error.message}`);
      });
    } catch (error) {
      console.error(`Failed to release customScan. Code: ${error.code}, message: ${error.message}`);
    }
  }

  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    async (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error) {
        console.error(`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      }
      console.info(`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}`);
    };
  // 回调获取ScanFrame
  private frameCallback: AsyncCallback<customScan.ScanFrame> =
    async (error: BusinessError, scanFrame: customScan.ScanFrame) => {
      if (error) {
        console.error(`Failed to get ScanFrame by callback. Code: ${error.code}, message: ${error.message}`);
        return;
      } else {
        if (this.previewHeight === scanFrame.height && this.previewWidth === scanFrame.width) {
          return;
        }
        this.previewHeight = scanFrame.height;
        this.previewWidth = scanFrame.width;

        // 通过setXComponentSurfaceRect设置surfaceRect，避免xComponent拉伸预览流
        let aspectRatio = 1478 / 1216;
        let resultRatio = scanFrame.width / scanFrame.height;
        let surfaceWidth = 0;
        let surfaceHeight = 0;
        let offsetX = 0;
        let offsetY = 0;

        if (resultRatio <= aspectRatio) {
          surfaceWidth = xComponentWidth;
          surfaceHeight = xComponentWidth * resultRatio;
          offsetX = 0;
          offsetY = (xComponentHeight - surfaceHeight) / 2;
        } else {
          surfaceWidth = xComponentHeight / resultRatio;
          surfaceHeight = xComponentHeight;
          offsetX = (xComponentWidth - surfaceWidth) / 2;
          offsetY = 0;
        }

        this.mXComponentController.setXComponentSurfaceRect({
          offsetX,
          offsetY,
          surfaceWidth,
          surfaceHeight
        });
      }
    };

  init() {
    let options: scanBarcode.ScanOptions = {
      scanTypes: [scanCore.ScanType.ALL],
      enableMultiMode: false,
      enableAlbum: false
    };
    //初始化相机
    try {
      customScan.init(options);
      customScan.start(this.viewControl, this.callback, this.frameCallback);
    } catch (error) {
      console.error(`Failed to init. Code: ${error.code}, message: ${error.message}`);
    }
  }

  //检查相机权限打开相机
  async checkPermissionAndInitCamera() {
    let cameraPermissionGrant = await this.checkPermissionGrant('ohos.permission.CAMERA');
    if (cameraPermissionGrant === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
      this.init();
    } else {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
      atManager.requestPermissionsFromUser(this.context, permissions).then((data: PermissionRequestResult) => {
        let grantStatus: Array<number> = data.authResults;
        let length: number = grantStatus.length;
        for (let i = 0; i < length; i++) {
          if (grantStatus[i] != 0) {
            atManager.requestPermissionOnSetting(this.context, permissions)
              .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
                this.init();
                console.info(`requestPermissionOnSetting success, result: ${data}`);
              })
              .catch((err: BusinessError) => {
                console.error(`requestPermissionOnSetting fail, code: ${err.code}, message: ${err.message}`);
              });
            // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
            return;
          }
        }
        this.init();
        console.info(`Success to request permissions from user. authResults is ${grantStatus}.`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
      });
    }
  }

  onPageShow(): void {
    this.isPageShow = true;
  }

  onPageHide(): void {
    this.isPageShow = false;
  }

  build() {
    Column() {
      Row()
        .width('100%')
        .height(55)
      Stack() {
        XComponent({
          type: XComponentType.SURFACE,
          controller: this.mXComponentController
        })
          .id('root')
          .onLoad(() => {
            // 获取XComponent的surfaceId
            this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
            this.isLoaded = true;
            this.viewControl = {
              width: xComponentWidth,
              height: xComponentHeight,
              surfaceId: this.surfaceId,
            };
            this.checkPermissionAndInitCamera();
          })
          .width(xComponentWidth + 'px')
          .height(xComponentHeight + 'px')
          .enableAnalyzer(false)
      }
      .backgroundColor(Color.Transparent)

      Row() {
        Image(this.pixmap)
          .objectFit(ImageFit.Contain)
          .width('50%')
          .height('100%')
      }
      .layoutWeight(1)
      .padding(20)

      Column() {
        Row() {
          Row() {
            Button('拍照')
              .width(70)
              .onClick(() => {
                let region: image.Region =
                  { x: 0, y: 0, size: { height: this.previewHeight, width: this.previewWidth } };
                image.createPixelMapFromSurface(this.surfaceId, region).then(async (pixmap: image.PixelMap) => {
                  console.info('Succeeded in creating pixelmap from Surface');
                  await pixmap.rotate(90);
                  this.pixmap = pixmap;
                }).catch((error: BusinessError) => {
                  console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
                });
              })
          }
          .justifyContent(FlexAlign.Center)
          .layoutWeight(1)
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceAround)
        .padding({
          top: 15,
          bottom: 15
        })
      }
      .width('100%')
    }
    .backgroundColor(Color.Black)
    .width('100%')
    .height('100%')
  }
}
```
