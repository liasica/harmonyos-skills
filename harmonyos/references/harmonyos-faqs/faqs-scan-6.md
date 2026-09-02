---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scan-6
title: 如何自定义扫码组件的扫码区域
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 扫码服务（Scan） > 如何自定义扫码组件的扫码区域
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:bedaf93e44a461263700f56b7dfd24ffcb38ea66be9ea3b67521b324c1881c4f
---

## 问题现象

调用相机实现自定义扫码时，分辨率需要设置为支持比例才能正常显示。如何根据业务场景需要只展示需要的扫码区域，如设置为宽高比大于1的区域，如下图所示上方黑色区域为扫码区域。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/0-hVeU21RWagI31cMU0L-Q/zh-cn_image_0000002628392620.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：Canvas提供画布组件，用于自定义绘制图形，开发者使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。
* [Stack](../harmonyos-references/ts-container-stack.md)：层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过Stack容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。
* [自定义界面扫码](../harmonyos-guides/scan-customscan.md)：自定义界面扫码能力提供了相机流控制接口，可根据自身需求自定义扫码界面，适用于对扫码界面有定制化需求的应用开发。

## 解决方案

根据[自定义界面扫码开发步骤中的描述](../harmonyos-guides/scan-customscan.md#开发步骤)，在竖屏场景下支持的宽高分辨率比例为9:16、3:4、1:1。若需要在竖屏场景下实现宽高比大于1的部分拍摄，开发者可以通过Stack组件在自定义界面扫码渲染组件XComponent上覆盖一层背景色将下半部分遮盖，参考如下。

```ts
// 自定义扫码界面的顶部返回按钮和扫码提示
@Builder
TopTool() {
  Column() {
    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
      Text('返回')
        .onClick(async () => {
          this.getUIContext().getRouter().back();
        })
    }.padding({ left: 24, right: 24, top: 40 })

    Column() {
      Text('扫描二维码/条形码')
      Text('对准二维码/条形码，即可自动扫描')
    }.margin({ left: 24, right: 24, top: 30 })

  }
  .height(146)
  .width('100%')
}

build() {
  Stack() {
    if (this.userGrant) {
      Column() {
        XComponent({
          id: 'componentId',
          type: XComponentType.SURFACE,
          controller: this.mXComponentController
        })
          .onLoad(async () => {
            hilog.info(0x0001, TAG, 'Succeeded in loading, onLoad is called.');
            // 获取XComponent组件的surfaceId
            this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
            hilog.info(0x0001, TAG, `Succeeded in getting surfaceId: ${this.surfaceId}`);
            this.initCamera();
            // 闪光灯监听接口
            customScan.on('lightingFlash', (error, isLightingFlash) => {
              if (error) {
                hilog.error(0x0001, TAG,
                  `Failed to on lightingFlash. Code: ${error.code}, message: ${error.message}`);
                return;
              }
              if (isLightingFlash) {
                this.isFlashLightEnable = true;
              } else {
                try {
                  if (!customScan.getFlashLightStatus()) {
                    this.isFlashLightEnable = false;
                  }
                } catch (error) {
                  hilog.error(0x0001, TAG,
                    `Failed to get FlashLightStatus. Code: ${error.code}, message: ${error.message}`);
                }
              }
              this.isSensorLight = isLightingFlash;
            });
          })
          .width(this.cameraWidth)
          .height(this.cameraHeight)
          .position({ x: this.offsetX, y: this.offsetY })
      }
      .height('100%')
      .width('100%')
    }
    Column() {
      Column()
        .width('100%')
        .height(430)
        .backgroundColor(Color.White)
    }
    .width('100%')
    .height(this.cameraHeight)
    .position({ x: this.offsetX, y: this.offsetY })
    .justifyContent(FlexAlign.End)

    Canvas(this.context)
      .width('100%')
      .height(this.cameraHeight)
      .backgroundColor('#00000000') // 画布背景色为透明
      .position({ x: this.offsetX, y: this.offsetY })
      .onReady(() => {
        let scanBoxWidth = 200;
        let scanBoxHeight = 100;
        this.context.lineWidth = 5;
        this.context.strokeStyle = '#0000ff';
        this.context.strokeRect((this.cameraWidth - scanBoxWidth) / 2 - 50,
          (this.cameraHeight - scanBoxHeight) / 2 - 200, (this.cameraWidth + scanBoxWidth) / 2, 120);
      })

    Column() {
      this.TopTool();
      Column() {
      }
      .layoutWeight(1)
      .width('100%')

      Column() {
        Row() {
          // 闪光灯按钮，启动相机流后才能使用
          Button('FlashLight')
            .onClick(() => {
              let lightStatus: boolean = false;
              try {
                lightStatus = customScan.getFlashLightStatus();
              } catch (error) {
                hilog.error(0x0001, TAG,
                  `Failed to get flashLightStatus. Code: ${error.code}, message: ${error.message}`);
              }
              // 根据当前闪光灯状态，选择打开或关闭闪光灯
              if (lightStatus) {
                try {
                  customScan.closeFlashLight();
                  setTimeout(() => {
                    this.isFlashLightEnable = this.isSensorLight;
                  }, 200);
                } catch (error) {
                  hilog.error(0x0001, TAG,
                    `Failed to close flashLight. Code: ${error.code}, message: ${error.message}`);
                }
              } else {
                try {
                  customScan.openFlashLight();
                } catch (error) {
                  hilog.error(0x0001, TAG,
                    `Failed to open flashLight. Code: ${error.code}, message: ${error.message}`);
                }
              }
            })
            .visibility((this.userGrant && this.isFlashLightEnable) ? Visibility.Visible : Visibility.None)

          // 扫码成功后，点击按钮后重新扫码
          Button('Scan')
            .onClick(() => {
              // 点击按钮重启相机流，重新扫码
              this.initCamera();
            })
            .visibility(this.isShowBack ? Visibility.Visible : Visibility.None)
        }
      }
      .width('50%')
      .height(180)
    }

    // 单码、多码扫描后，显示码图蓝点位置。点击toast码图信息
    ForEach(this.scanResult, (item: scanBarcode.ScanResult) => {
      if (item.scanCodeRect) {
        Image($r('app.media.startIcon')) // 自行替换图片
          .width(40)
          .height(40)
          .markAnchor({ x: 20, y: 20 })
          .position({
            x: (item.scanCodeRect.left + item?.scanCodeRect?.right) / 2 + this.offsetX,
            y: (item.scanCodeRect.top + item?.scanCodeRect?.bottom) / 2 + this.offsetY
          })
          .onClick(() => {
            this.showScanResult(item);
          })
      }
    })
  }
  // 建议相机流设置为全屏
  .width('100%')
  .height('100%')
}
```

若条码在遮盖区域内被扫描结果返回，不符合业务逻辑。可以通过规定扫码区域，将扫码识别区域设置在上方展示区域中，当检测到条码被检测区域完全覆盖时返回扫码结果，否则触发[customScan.rescan](../harmonyos-references/scan-customscan-api.md#rescan)重新扫码，同时可以通过Canvas画布绘制出扫码框区域（与扫码识别区域大小位置保持一致），参考[自定义界面扫码如何实现扫码框](../harmonyos-guides/scan-faq-15.md)。

示例效果图如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/4jT0XRDJSBCzuTTnOag4ww/zh-cn_image_0000002658791887.png "点击放大")

完整代码如下：

```ts
import { customScan, scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { display } from '@kit.ArkUI';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = '[customScanPage]';

@Entry
@Component
struct customScanArea {
  @State userGrant: boolean = false; // 是否已申请相机权限
  @State surfaceId: string = ''; // xComponent组件生成id
  @State isShowBack: boolean = false; // 是否已经返回扫码结果
  @State isFlashLightEnable: boolean = false; // 是否开启了闪光灯
  @State isSensorLight: boolean = false; // 记录当前环境亮暗状态
  @State cameraHeight: number = 640; // 设置预览流高度，默认单位：vp
  @State cameraWidth: number = 360; // 设置预览流宽度，默认单位：vp
  private offsetX: number = 0; // 设置预览流x轴方向偏移量，默认单位：vp
  private offsetY: number = 0; // 设置预览流y轴方向偏移量，默认单位：vp
  private displayWidth: number = 0; // 屏幕宽度，单位vp
  private scanResult: Array<scanBarcode.ScanResult> = []; // 扫码结果
  private mXComponentController: XComponentController = new XComponentController();
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D();

  async onPageShow() {
    // 自定义启动第一步，用户申请权限
    await this.requestCameraPermission();
    // 多码扫码识别，enableMultiMode: true 单码扫码识别enableMultiMode: false
    let options: scanBarcode.ScanOptions = {
      scanTypes: [scanCore.ScanType.ALL],
      enableMultiMode: true,
      enableAlbum: true
    };
    // 自定义启动第二步：设置预览流布局尺寸
    this.setDisplay();
    try {
      // 自定义启动第三步，初始化接口
      customScan.init(options);
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to init customScan. Code: ${error.code}, message: ${error.message}`);
    }
  }

  async onPageHide() {
    // 页面消失或隐藏时，停止并释放相机流
    this.userGrant = false;
    this.isFlashLightEnable = false;
    this.isSensorLight = false;
    try {
      customScan.off('lightingFlash');
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to off lightingFlash. Code: ${error.code}, message: ${error.message}`);
    }
    this.customScanStop();
    try {
      // 自定义相机流释放接口
      customScan.release().then(() => {
        hilog.info(0x0001, TAG, 'Succeeded in releasing customScan by promise.');
      }).catch((error: BusinessError) => {
        hilog.error(0x0001, TAG,
          `Failed to release customScan by promise. Code: ${error.code}, message: ${error.message}`);
      });
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to release customScan. Code: ${error.code}, message: ${error.message}`);
    }
  }

  // 用户申请权限
  async reqPermissionsFromUser(): Promise<number[]> {
    hilog.info(0x0001, TAG, 'reqPermissionsFromUser start');
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let atManager = abilityAccessCtrl.createAtManager();
    let grantStatus = await atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA']);
    return grantStatus.authResults;
  }

  // 用户申请相机权限
  async requestCameraPermission() {
    let grantStatus = await this.reqPermissionsFromUser();
    for (let i = 0; i < grantStatus.length; i++) {
      if (grantStatus[i] === 0) {
        // 用户授权，可以继续访问目标操作
        hilog.info(0x0001, TAG, 'Succeeded in getting permissions.');
        this.userGrant = true;
      }
    }
  }

  setDisplay() {
    try {
      let displayClass = display.getDefaultDisplaySync();
      this.displayWidth = this.getUIContext().px2vp(displayClass.width);
      const RATIO: number = 9 / 16;
      this.cameraWidth = this.displayWidth;
      this.cameraHeight = this.cameraWidth / RATIO;

    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to getDefaultDisplaySync. Code: ${error.code}, message: ${error.message}`);
    }
  }

  // toast显示扫码结果
  async showScanResult(result: scanBarcode.ScanResult) {
    // 使用toast显示出扫码结果
    this.getUIContext().getPromptAction().showToast({
      message: JSON.stringify(result),
      duration: 5000
    });
  }

  initCamera() {
    // 根据业务逻辑计算获取扫码区域
    let scanBoxWidth = 200;
    let scanBoxHeight = 100;
    let scanBox: scanBarcode.ScanCodeRect = {
      left: (this.cameraWidth - scanBoxWidth) / 2,
      top: (this.cameraHeight - scanBoxHeight) / 2,
      right: (this.cameraWidth + scanBoxWidth) / 2,
      bottom: (this.cameraHeight + scanBoxHeight) / 2
    };

    this.isShowBack = false;
    this.scanResult = [];
    let viewControl: customScan.ViewControl = {
      width: this.cameraWidth,
      height: this.cameraHeight,
      surfaceId: this.surfaceId
    };
    try {
      // 自定义启动第四步，请求扫码接口，通过Promise方式回调
      customScan.start(viewControl)
        .then(async (result: Array<scanBarcode.ScanResult>) => {
          hilog.info(0x0001, TAG, `result: ${JSON.stringify(result)}`);
          let scanResult: scanBarcode.ScanCodeRect = {
            left: 150,
            top: 400,
            right: 450,
            bottom: 700
          };
          if (scanResult.left >= scanBox.left && scanResult.top >= scanBox.top && scanResult.right <= scanBox.right &&
            scanResult.bottom <= scanBox.bottom) {
            if (result.length) {
              // 解析码值结果跳转应用服务页
              this.scanResult = result;
              this.isShowBack = true;
              // 获取到扫描结果后暂停相机流
              this.customScanStop();
            } else {
              // 码图位置不在扫码框范围，继续扫码
              try {
                customScan.rescan();
              } catch (error) {
                hilog.error(0x0001, '[Scan Sample]',
                  `Failed to rescan. Code: ${error.code}, message: ${error.message}`);
              }
            }
          }
        });
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to start customScan. Code: ${error.code}, message: ${error.message}`);
    }
  }

  customScanStop() {
    try {
      customScan.stop();
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to stop customScan. Code: ${error.code}, message: ${error.message}`);
    }
  }

  // 自定义扫码界面的顶部返回按钮和扫码提示
  @Builder
  TopTool() {
    Column() {
      Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
        Text('返回')
          .onClick(async () => {
            this.getUIContext().getRouter().back();
          })
      }.padding({ left: 24, right: 24, top: 40 })

      Column() {
        Text('扫描二维码/条形码')
        Text('对准二维码/条形码，即可自动扫描')
      }.margin({ left: 24, right: 24, top: 30 })
    }
    .height(146)
    .width('100%')
  }

  build() {
    Stack() {
      if (this.userGrant) {
        Column() {
          XComponent({
            id: 'componentId',
            type: XComponentType.SURFACE,
            controller: this.mXComponentController
          })
            .onLoad(async () => {
              hilog.info(0x0001, TAG, 'Succeeded in loading, onLoad is called.');
              // 获取XComponent组件的surfaceId
              this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
              hilog.info(0x0001, TAG, `Succeeded in getting surfaceId: ${this.surfaceId}`);
              this.initCamera();
              // 闪光灯监听接口
              customScan.on('lightingFlash', (error, isLightingFlash) => {
                if (error) {
                  hilog.error(0x0001, TAG,
                    `Failed to on lightingFlash. Code: ${error.code}, message: ${error.message}`);
                  return;
                }
                if (isLightingFlash) {
                  this.isFlashLightEnable = true;
                } else {
                  try {
                    if (!customScan.getFlashLightStatus()) {
                      this.isFlashLightEnable = false;
                    }
                  } catch (error) {
                    hilog.error(0x0001, TAG,
                      `Failed to get FlashLightStatus. Code: ${error.code}, message: ${error.message}`);
                  }
                }
                this.isSensorLight = isLightingFlash;
              });
            })
            .width(this.cameraWidth)
            .height(this.cameraHeight)
            .position({ x: this.offsetX, y: this.offsetY })
        }
        .height('100%')
        .width('100%')
      }
      Column() {
        Column()
          .width('100%')
          .height(430)
          .backgroundColor(Color.White)
      }
      .width('100%')
      .height(this.cameraHeight)
      .position({ x: this.offsetX, y: this.offsetY })
      .justifyContent(FlexAlign.End)

      Canvas(this.context)
        .width('100%')
        .height(this.cameraHeight)
        .backgroundColor('#00000000') // 画布背景色为透明
        .position({ x: this.offsetX, y: this.offsetY })
        .onReady(() => {
          let scanBoxWidth = 200;
          let scanBoxHeight = 100;
          this.context.lineWidth = 5;
          this.context.strokeStyle = '#0000ff';
          this.context.strokeRect((this.cameraWidth - scanBoxWidth) / 2 - 50,
            (this.cameraHeight - scanBoxHeight) / 2 - 200, (this.cameraWidth + scanBoxWidth) / 2, 120);
        })

      Column() {
        this.TopTool();
        Column() {
        }
        .layoutWeight(1)
        .width('100%')

        Column() {
          Row() {
            // 闪光灯按钮，启动相机流后才能使用
            Button('FlashLight')
              .onClick(() => {
                let lightStatus: boolean = false;
                try {
                  lightStatus = customScan.getFlashLightStatus();
                } catch (error) {
                  hilog.error(0x0001, TAG,
                    `Failed to get flashLightStatus. Code: ${error.code}, message: ${error.message}`);
                }
                // 根据当前闪光灯状态，选择打开或关闭闪光灯
                if (lightStatus) {
                  try {
                    customScan.closeFlashLight();
                    setTimeout(() => {
                      this.isFlashLightEnable = this.isSensorLight;
                    }, 200);
                  } catch (error) {
                    hilog.error(0x0001, TAG,
                      `Failed to close flashLight. Code: ${error.code}, message: ${error.message}`);
                  }
                } else {
                  try {
                    customScan.openFlashLight();
                  } catch (error) {
                    hilog.error(0x0001, TAG,
                      `Failed to open flashLight. Code: ${error.code}, message: ${error.message}`);
                  }
                }
              })
              .visibility((this.userGrant && this.isFlashLightEnable) ? Visibility.Visible : Visibility.None)

            // 扫码成功后，点击按钮后重新扫码
            Button('Scan')
              .onClick(() => {
                // 点击按钮重启相机流，重新扫码
                this.initCamera();
              })
              .visibility(this.isShowBack ? Visibility.Visible : Visibility.None)
          }
        }
        .width('50%')
        .height(180)
      }

      // 单码、多码扫描后，显示码图蓝点位置。点击toast码图信息
      ForEach(this.scanResult, (item: scanBarcode.ScanResult) => {
        if (item.scanCodeRect) {
          Image($r('app.media.startIcon')) // 自行替换图片
            .width(40)
            .height(40)
            .markAnchor({ x: 20, y: 20 })
            .position({
              x: (item.scanCodeRect.left + item?.scanCodeRect?.right) / 2 + this.offsetX,
              y: (item.scanCodeRect.top + item?.scanCodeRect?.bottom) / 2 + this.offsetY
            })
            .onClick(() => {
              this.showScanResult(item);
            })
        }
      })
    }
    // 建议相机流设置为全屏
    .width('100%')
    .height('100%')
  }

  public customGetZoom(): number {
    let zoom = 1;
    try {
      zoom = customScan.getZoom();
      hilog.info(0x0001, TAG, `Succeeded in getting Zoom, zoom: ${zoom}`);
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to getZoom. Code: ${error.code}, message: ${error?.message}`);
    }
    return zoom;
  }

  public customSetZoom(pinchValue: number): void {
    try {
      customScan.setZoom(pinchValue);
      hilog.info(0x0001, TAG, `Succeeded in setting Zoom.`);
    } catch (error) {
      hilog.error(0x0001, TAG, `Failed to setZoom. Code: ${error.code}, message: ${error?.message}`);
    }
  }
}
```

## 总结

HarmonyOS中暂不支持在竖屏场景设置扫码界面宽高比大于1，若未按支持比例设置会导致扫码画面拉伸。若需实现指定区域扫码可参考以下步骤。

1. 创建自定义扫码界面，设置支持比例。
2. 利用层叠布局将非扫码区域遮盖。
3. 指定扫码识别区域，当超出扫码区域时触发重新扫描。
