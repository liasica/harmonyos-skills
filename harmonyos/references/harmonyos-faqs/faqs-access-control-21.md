---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-21
title: 超级隐私模式下，应用权限申请异常
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 超级隐私模式下，应用权限申请异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2ef65e137a45b9b6b578dab04d5d49ac007beae26922ce3349d139c3103dc980
---

## 问题现象

在超级隐私模式下，应用申请位置、相机和麦克风权限，结果无响应或提示未开启/无权限，未能给出有效引导。

## 背景知识

* 开启超级隐私模式后，应用将无法获取手机的麦克风、摄像头、位置数据。此时，即使应用已经被授权相关权限，也不能完成访问目标的操作。应用需要检测到这种状态，并通过适当的方式来提醒用户并辅助开启对应的全局开关。详情可见[功能被禁用处理方式](../best-practices/bpta-permission-application.md#section109832047175018)。
* 以下为判断各全局开关是否打开的方法：
  + 位置：[isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)判断位置服务是否已经使能，返回true表示位置信息开关已开启，false表示位置信息开关已关闭。
  + 相机：[isCameraMuted](../harmonyos-references/arkts-apis-camera-cameramanager.md#iscameramuted)查询相机当前的禁用状态（禁用/未禁用），返回true表示相机被禁用，false表示相机未被禁用。
  + 麦克风：[isMicrophoneMute](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#ismicrophonemute9)查询麦克风当前静音状态，返回true表示麦克风被静音，false表示麦克风未被静音。
* 提醒用户重新开启全局开关，则需要调用[requestGlobalSwitch()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)方法，之后才能继续调用所需的接口。

## 问题定位

1. 点击相应需要申请权限的功能后，未拉起权限弹窗，而是未响应或提示未开启/无权限/失败等内容。
2. 检查设备的状态栏，有盾牌外形锁孔图标，代表开启了超级隐私模式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/LVZtGCGJTt-VOOxDgTwbDA/zh-cn_image_0000002628608466.png "点击放大")
3. 查看权限申请时的代码，检查是否存在校验全局开关的方法，以及是否调用了[requestGlobalSwitch()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)方法提醒用户打开。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Y_lq4cQdS0mpD-qgEyM7Zw/zh-cn_image_0000002658847725.png "点击放大")

## 分析结论

设备开启了超级隐私模式，应用未对此情况做检测，也未能通过适当的方式来提醒用户开启全局开关。

## 修改建议

添加校验全局开关是否开启的逻辑，调用[requestGlobalSwitch()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)方法提醒用户重新开启。

具体开发可以参考如下代码，更详细代码参考[功能被禁用处理方式](../best-practices/bpta-permission-application.md#section109832047175018)文档的示例代码。

```screen
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { geoLocationManager } from '@kit.LocationKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct LocationTogglePage {
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  // 以位置权限为例
  isLocationToggle() {
    let atManager = abilityAccessCtrl.createAtManager();
    // 判断位置服务是否开启
    let isLocationEnabled = geoLocationManager.isLocationEnabled();
    if (!isLocationEnabled) {
      // 拉起弹窗提醒用户关闭超级隐私模式
      atManager.requestGlobalSwitch(this.context, abilityAccessCtrl.SwitchType.LOCATION).then((data: boolean) => {
        if (data) {
          // 已关闭，获取位置权限
        } else {
          // 依旧未关闭
        }
      }).catch((err: BusinessError) => {
        console.error(`requestGlobalSwitch failed, code is ${err.code}, message is ${err.message}`);
      });
    }
  }
  build() {
    Column() {
      Button('位置开关')
        .onClick(() => {
          this.isLocationToggle();
        })
        .margin({top: 40})
    }
    .height('100%')
    .width('100%')
  }
}
```
