---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-3
title: 在自定义扫码界面退到后台再回到前台时扫码停止该如何解决
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 在自定义扫码界面退到后台再回到前台时扫码停止该如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d3368baebb6cccfc9bb02d51653d0e969fa2f68b9a1ea50767932b8eb01ba20
---

## 问题现象

Tabs组件管理的首页面是自定义扫码界面，开启相机进行扫描，然后手动切换到后台，回到前台后无法继续扫描，页面静止不动。

问题代码示例参考如下：

```screen
@Entry
@Component
struct Index {
  build() {
    Tabs({
      barPosition: BarPosition.End
    }) {
      TabContent() {
        CustomScanPage()
      }
    }
  }
}
export struct CustomScanPage {
  onPageShow(): void {
    this.customScanStart()
  }
  onPageHide(): void{
    this.releaseCamera();
  }
  // 初始化扫码资源
  customScanStart() {
    customScan.init();
    customScan.start().then((scanResult: Array<scanBarcode.ScanResult>) => {
      // 扫码结果处理
    }).catch((error: BusinessError) => {
      // 错误信息处理
    });
  }
  // 释放扫码资源
  releaseCamera() {
    customScan.stop();
    customScan.release();
  }
}
```

## 背景知识

1. 相机切换后台再切回来，必须要重新初始化相机才可以。因为切后台，相机资源被全部回收。
2. 自定义扫码提供了扫码相机流控制接口，支持扫码界面自定义并实现基本的扫码功能。您可根据相应场景来开启、暂停和释放相机流，还可根据相应的光线条件来控制闪光灯的打开和关闭，便于用户进行扫码。

扫码时序图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/6OtglFA8QNiU973JphVNrg/zh-cn_image_0000002658791883.png "点击放大")

详情请参考：[customScan (自定义界面扫码)](../harmonyos-references/scan-customscan-api.md)。

## 问题定位

从问题代码可以看出工程中希望在onPageShow和onPageHide方法内实现扫码的初始化和释放逻辑，但是onPageShow和onPageHide方法属于页面生命周期方法，[Tabs](../harmonyos-references/ts-container-tabs.md)是容器组件，所管理的CustomScanPage页面属于子组件，所以不会调用页面的生命周期方法。

1. 组件调用的生命周期方法：
   * aboutToAppear()。
   * aboutToDisappear()。
   * aboutToReuse()。
2. 页面调用的生命周期方法：
   * onPageShow()。
   * onPageHide()。
   * onBackPress()。

## 分析结论

通过以上分析，子组件CustomScanPage页面不会调用onPageShow和onPageHide方法，导致前后台切换时不会重新初始化和释放相机资源，再进入前台后扫码界面静止。为了实现进入后台时调用release接口进行释放扫码资源，进入前台调用init接口初始化扫码资源的目标，需要通过注册[UiObserver](../harmonyos-references/arkts-apis-uicontext-uiobserver.md)方法监听自定义扫码页面是否显示。

## 修改建议

通过UiObserver方法监听自定义组件页面生命周期解决该问题。

1. 使用自定义扫码功能时，需要在module.json5中配置[ohos.permission.CAMERA](../harmonyos-guides/permissions-for-all-user.md#ohospermissioncamera)权限，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 在aboutToAppear()方法中注册监听方法。

   ```screen
   async aboutToAppear() {
     // 添加监听
     this.getUIContext().getUIObserver().on('routerPageUpdate', (info) => {
       if (info.state == uiObserver.RouterPageState.ON_PAGE_SHOW) {
         this.onPageShow();
       } else if (info.state == uiObserver.RouterPageState.ON_PAGE_HIDE) {
         this.onPageHide();
       }
     });
     if (this.userGrant === false) {
       this.requestCameraPermission();
     }
   }
   ```
3. 通过监听调用的方法中实现初始化和销毁逻辑。

   ```screen
   async onPageShow() {
     if (!this.userGrant) {
       // 申请权限
       this.requestCameraPermission();
     } else {
       this.customScanStart();
     }
   }

   async onPageHide() {
     this.releaseCamera();
   }
   ```
4. 在aboutToDisappear()方法中注销监听方法。

   ```screen
   async aboutToDisappear() {
     // 取消监听，不选择回调时，取消所有监听的回调
     this.getUIContext().getUIObserver().off('routerPageUpdate');
   }
   ```

完整示例参考如下：

```screen
import { customScan, scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { display, uiObserver } from '@kit.ArkUI';
import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';

const TAG: string = '[Scan Sample]';

@Entry
@Component
struct PageOne {
  build() {
    Tabs({
      barPosition: BarPosition.End
    }) {
      TabContent() {
        CustomScanCode();
      }.tabBar('首页');
    };
  }
}

@Component
export struct CustomScanCode {
  @State userGrant: boolean = false; // 是否已申请相机权限
  // 设置预览流高度，默认单位：vp
  @State cameraHeight: number = 640; // 设置预览流高度，默认单位：vp
  @State cameraWidth: number = 360; // 设置预览流宽度，默认单位：vp
  private mXComponentController: XComponentController = new XComponentController();
  @State isReleaseCamera: boolean = false; // 是否已释放相机流
  displayHeight: number = 0; // 屏幕高度，单位vp
  displayWidth: number = 0; // 屏幕宽度，单位vp

  async aboutToAppear() {
    // 添加监听
    this.getUIContext().getUIObserver().on('routerPageUpdate', (info) => {
      if (info.state == uiObserver.RouterPageState.ON_PAGE_SHOW) {
        this.onPageShow();
      } else if (info.state == uiObserver.RouterPageState.ON_PAGE_HIDE) {
        this.onPageHide();
      }
    });
    if (this.userGrant === false) {
      this.requestCameraPermission();
    }
  }

  async aboutToDisappear() {
    // 取消监听，不选择回调时，取消所有监听的回调
    this.getUIContext().getUIObserver().off('routerPageUpdate');
  }

  // 用户申请权限
  async reqPermissionsFromUser(): Promise<number[]> {
    hilog.info(0x0001, TAG, 'reqPermissionsFromUser start');
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let atManager = abilityAccessCtrl.createAtManager();
    try {
      const grantStatus: PermissionRequestResult =
        await atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']);
      return grantStatus.authResults;
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to requestPermissionsFromUser. Code: ${error.code}, message: ${error.message}`);
      return [];
    }
  }

  // 用户申请相机权限
  async requestCameraPermission() {
    let grantStatus = await this.reqPermissionsFromUser();
    for (let i = 0; i < grantStatus.length; i++) {
      if (grantStatus[i] === 0) {
        // 用户授权，可以继续访问目标操作
        hilog.info(0x0001, TAG, 'Succeeded in getting permissions.');
        this.userGrant = true;
        break;
      }
    }
  }

  async onPageShow() {
    if (!this.userGrant) {
      // 申请权限
      this.requestCameraPermission();
    } else {
      this.customScanStart();
    }
  }

  async onPageHide() {
    this.releaseCamera();
  }

  // 释放相机流
  async releaseCamera() {
    if (!this.isReleaseCamera) {
      await this.stopCamera();
      await customScan.release();
      this.isReleaseCamera = true;
    }
  }

  // 暂停相机流
  async stopCamera() {
    if (!this.isReleaseCamera) {
      customScan.stop();
    }
  }

  // 竖屏时获取屏幕尺寸，设置预览流全屏示例
  async setDisplay() {
    try {
      // 默认竖屏
      let displayClass = display.getDefaultDisplaySync();
      this.displayHeight = this.getUIContext().px2vp(displayClass.height);
      this.displayWidth = this.getUIContext().px2vp(displayClass.width);
      let maxLen: number = Math.max(this.displayWidth, this.displayHeight);
      const RATIO: number = 16 / 9;
      this.cameraHeight = maxLen;
      this.cameraWidth = maxLen / RATIO;
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to getDefaultDisplaySync. Code: ${error.code}, message: ${error.message}`);
    }
  }

  build() {
    Column() {
      if (this.userGrant) {
        Stack() {
          XComponent({
            id: 'componentId',
            type: XComponentType.SURFACE,
            controller: this.mXComponentController
          })
            .onLoad(() => {
              // 获取XComponent的surfaceId
              this.customScanStart();
            })
            .height(this.cameraHeight)
            .width(this.cameraWidth)
            .position({ x: 0, y: 0 });
        }
        .width('100%')
        .height('100%');
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }

  private customScanStart() {
    this.isReleaseCamera = false;
    let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
    let options: scanBarcode.ScanOptions = {
      scanTypes: [scanCore.ScanType.ALL],
      enableMultiMode: true,
      enableAlbum: true
    };
    this.setDisplay();
    try {
      customScan.init(options);
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to init customScan. Code: ${error.code}, message: ${error.message}`);
    }
    // 设置ViewControl相应字段
    let viewControl: customScan.ViewControl = {
      width: this.cameraWidth,
      height: this.cameraHeight,
      surfaceId: surfaceId
    };
    customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
      hilog.info(0x0001, '[Scan Sample]',
        `Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}`);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to get ScanResult by promise. Code: ${error.code}, message: ${error.message}`);
    });
  }
}
```

## 总结

1. 当前后台切换导致相机功能出现画面静止时，都可以通过每次进入后台先释放相机资源、进入前台再初始化相机资源的方案解决。
2. Tabs组件管理的页面属于子组件，所以不会调用页面生命周期方法。
