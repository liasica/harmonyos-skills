---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-10
title: 如何解决活体检测报错1008302000
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 如何解决活体检测报错1008302000
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f76c2aa7f31e89268258356b0b39791e2f99f675acd084cf124ef266d544a494
---

## 问题现象

使用活体检测进行人脸检测，检测结果数据接收时报错1008302000。

## 解决方案

startLivenessDetection调用结束后检测流程并没有立刻完成，所以立刻调用getInteractiveLivenessResult接口并没有完成检测，获取不到检测结果，则是返回1008302000：Detection algorithm initialization的错误。建议startLivenessDetection使用callback回调检测。

```screen
import { common, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index{
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private array: Array<Permissions> = ["ohos.permission.CAMERA"];
  @State actionsNum: number = 3;
  isSilentMode: string = "INTERACTIVE_MODE";
  @State routeMode: string = "replace";
  @State resultInfo: interactiveLiveness.InteractiveLivenessResult = {
    livenessType: 0
  };
  @State failResult: Record<string, number | string> = {
    "code": 1008302000,
    "message": ""
  };

  build() {
    Stack({
      alignContent: Alignment.Top
    }) {
      Column() {
        Row() {
          Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
            Text("验证完的跳转模式：")
              .fontSize(18)
              .width("25%")
            Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
              Row() {
                Radio({ value: "replace", group: "routeMode" }).checked(true)
                  .height(24)
                  .width(24)
                  .onChange(() => {
                    this.routeMode = "replace";
                  })
                Text("replace")
                  .fontSize(16)
              }
            }
            .width("75%")
          }
        }
        .margin({ bottom: 30 })

        Row() {
          Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
            Text("检测动作数量：")
              .fontSize(18)
              .width("25%")
            TextInput({
              placeholder: this.actionsNum != 0 ? this.actionsNum.toString() : "动作数量为3或4个"
            })
              .type(InputType.Number)
              .placeholderFont({
                size: 18,
                weight: FontWeight.Normal,
                family: "HarmonyHeiTi",
                style: FontStyle.Normal
              })
              .fontSize(18)
              .fontWeight(FontWeight.Bold)
              .fontFamily("HarmonyHeiTi")
              .fontStyle(FontStyle.Normal)
              .width("65%")
              .onChange((value: string) => {
                this.actionsNum = Number(value) as interactiveLiveness.ActionsNumber;
              })
          }
        }
      }
      .margin({ left: 24, top: 80 })
      .zIndex(1)

      Stack({
        alignContent: Alignment.Bottom
      }) {
        if (this.resultInfo?.mPixelMap) {
          Image(this.resultInfo?.mPixelMap)
            .width(260)
            .height(260)
            .align(Alignment.Center)
            .margin({ bottom: 260 })
          Circle()
            .width(300)
            .height(300)
            .fillOpacity(0)
            .strokeWidth(60)
            .stroke(Color.White)
            .margin({ bottom: 250, left: 0 })
        }

        Text(this.resultInfo.mPixelMap ?
          "检测成功" :
          this.failResult.code !== 1008302000 ?
            "检测失败" :
            "")
          .width("100%")
          .height(26)
          .fontSize(20)
          .fontColor("#000000")
          .fontFamily("HarmonyHeiTi")
          .margin({ top: 50 })
          .textAlign(TextAlign.Center)
          .fontWeight("Medium")
          .margin({ bottom: 240 })

        if(this.failResult.code !== 1008302000) {
          Text(this.failResult.message as string)
            .width("100%")
            .height(26)
            .fontSize(16)
            .fontColor(Color.Gray)
            .textAlign(TextAlign.Center)
            .fontFamily("HarmonyHeiTi")
            .fontWeight("Medium")
            .margin({ bottom: 200 })
        }

        Button("开始检测", { type: ButtonType.Normal, stateEffect: true })
          .width(192)
          .height(40)
          .fontSize(16)
          .backgroundColor(0x317aff)
          .borderRadius(20)
          .margin({
            bottom: 56
          })
          .onClick(() => {
            this.startDetection();
          })
      }
      .height("100%")
    }
  }

  onPageShow() {
    this.resultRelease();
    this.getDetectionResultInfo();
  }

  // 跳转到人脸活体检测控件
  private routerLibrary() {
    let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
      isSilentMode: this.isSilentMode as interactiveLiveness.DetectionMode,
      routeMode: this.routeMode as interactiveLiveness.RouteRedirectionMode,
      actionsNum: this.actionsNum
    };

    if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
      interactiveLiveness.startLivenessDetection(routerOptions, (err: BusinessError,
        result: interactiveLiveness.InteractiveLivenessResult | undefined) => { // 当路由跳转错误时，获取结果失败，result返回undefined
        if(err.code !== 0 && !result) { // 在发生错误如路由跳转失败/参数错误/权限被拒绝时，会抛出错误码，详见ArkTS API错误码
          hilog.error(0x0001, "LivenessCollectionIndex", `Failed to detect. Code：${err.code}，message：${err.message}`);
          return;
        }else{
          if(result?.mPixelMap) {
            console.info('有图片信息');
          }else {
            console.info('没有图片信息');
          }
        }
        hilog.info(0x0001, 'LivenessCollectionIndex', `Succeeded in detecting result：${result}`);
      }).catch(() => {
        hilog.error(0x0001, 'LivenessCollectionIndex', `Failed to startLivenessDetection`);
      });
    } else {
      hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
    }
  }

  // 校验CAMERA权限
  private startDetection() {
    abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.array).then((res) => {
      for (let i = 0; i < res.permissions.length; i++) {
        if (res.permissions[i] === "ohos.permission.CAMERA" && res.authResults[i] === 0) {
          this.routerLibrary();
        }
      }
    }).catch((err: BusinessError) => {
      hilog.error(0x0001, "LivenessCollectionIndex", `Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
    });
  }

  // 获取验证结果
  private getDetectionResultInfo() {
    // getInteractiveLivenessResult接口调用完会释放资源
    if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
      interactiveLiveness.getInteractiveLivenessResult().then(data => {
        this.resultInfo = data;
      }).catch((err: BusinessError) => {
        this.failResult = {
          "code": err.code,
          "message": err.message
        };
      });
    } else {
      hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
    }
  }

  // result release
  private resultRelease() {
    this.resultInfo = {
      livenessType: 0
    };
    this.failResult = {
      "code": 1008302000,
      "message": ""
    };
  }
}
```
