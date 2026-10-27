---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-input-1
title: 大写字母键无效
breadcrumb: FAQ > 系统开发 > 基础功能 > 多模输入（Input） > 大写字母键无效
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:22+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:8c9969348c4cd8140f7f80beaf7386d3f54920a473743170c05d756e696a7101
---

## 问题现象

按下外接键盘CapsLock键，输入字母不是大写而是小写。

## 背景知识

* [多设备交互](../best-practices/bpta-multi-interaction.md#section11794812173816)：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/Pw4-gSPPT6eSFQS4YNy_gA/zh-cn_image_0000002628614390.png "点击放大")

  + [inputDevice.setFunctionKeyEnabled](../harmonyos-references/js-apis-inputdevice.md#inputdevicesetfunctionkeyenabled15)：设置功能键（如：CapsLock键）使能状态。使用Promise异步回调。

## 问题定位

根据Hilog日志定位，查看日志关键字CapsLockState，日志CapsLockState为false，判断应用未使能CapsLock键。

```shell
A000FF/i.hmos.inputmethod:inputMethod/HMKeyboard_HardwareInputManager: onInputStart. check result currentCapsLockState: false, this.subType?.id: InputEnLowerService
```

## 分析结论

应用未使能CapsLock键。

## 修改建议

参考以下代码使能CapsLock键：

```ts
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SetKeyEnabled {
  aboutToAppear() {
    try {
      inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK, true).then(() => {
        console.info(`Set capslock state success`);
      }).catch((error: BusinessError) => {
        console.error(`Set capslock state failed`, error);
      });
    } catch (error) {
      console.error(`Set capslock enable error`);
    }
  }

  build() {
    Row() {
      TextInput()
    }
    .height('100%')
    .width('100%')
    .padding(16);
  }
}
```
