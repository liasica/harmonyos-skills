---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/keypressed-guidelines
title: 优先响应系统功能键开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 优先响应系统功能键开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4db0e726910fa405e319608b5468a03d955b5499cb74893056a0ff1292b4075e
---

## 场景介绍

每个系统功能键均具有默认功能，由系统固定实现，比如音量键是用来调节设备音量，但是部分应用在特定场景下期望定制这部分按键的功能，本篇指导用于支撑这部分应用的诉求达成。

常见使用场景：阅读类型应用期望通过音量键翻页，相机应用期望通过音量键拍照等应用响应系统功能键做其他业务的场景。

支持功能键列表：从API version 16开始支持音量加按键和音量减按键。从API version 21开始，新增支持多媒体播放/暂停、多媒体下一首和多媒体上一首按键。从API version 26.0.0开始，新增支持智控键上滑和智控键下滑，非设备通用键值，使用前请判断当前设备是否支持相关按键事件上报。

## 约束与限制

* 应用窗口为前台焦点窗口时，优先响应才生效。
* 应用选择高于系统优先响应指定的系统功能键后，功能键的默认行为将失效，所以应用需要确保只有在确定响应时才激活该功能。

## 接口说明

按键按下事件常用接口如下表所示，接口详细介绍请参考[@ohos.multimodalInput.inputConsumer (全局快捷键)](../harmonyos-references/js-apis-inputconsumer.md)。

| 接口名称 | 描述 |
| --- | --- |
| on(type: "keyPressed", options: KeyPressedConfig, callback: Callback<KeyEvent>): void | 订阅指定按键按下事件，拦截系统默认响应。 |
| off(type: "keyPressed", callback?: Callback<KeyEvent>): void | 取消按键事件订阅，恢复系统默认响应。 |

## 开发步骤

应用开启时调用[on](../harmonyos-references/js-apis-inputconsumer.md#inputconsumeronkeypressed16)方法订阅按键按下事件，应用关闭时再用[off](../harmonyos-references/js-apis-inputconsumer.md#inputconsumeroffkeypressed16)方法取消订阅按键按下事件。

### 应用内优先响应系统功能键

在电子书或新闻阅读应用中，用户希望通过音量键或智控键滑动控制翻页（例如：音量加键向上翻页、音量减键向下翻页、智控键上滑向上翻页、智控键下滑向下翻页），需注意智控键上滑及下滑非设备通用键值，使用前请判断当前设备是否支持相关按键事件上报；在相机或扫码类应用中，用户按音量键可直接拍照，而不跳转系统相机应用。

```typescript
import { inputConsumer, KeyEvent, inputDevice, KeyCode } from '@kit.InputKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

@Entry
@Component
struct TestDemo14 {
  @State showComponent: boolean = false
  @State text: string = "Default monitoring for Volume Up and Down keys has been added."
  private volumeUpCallBackFunc: (event: KeyEvent) => void = () => {
  }
  private volumeDownCallBackFunc: (event: KeyEvent) => void = () => {
  }
  private slideUpCallBackFunc: (event: KeyEvent) => void = () => {
  }
  private slideDownCallBackFunc: (event: KeyEvent) => void = () => {
  }
  options1: inputConsumer.KeyPressedConfig = {
    key: KeyCode.KEYCODE_VOLUME_UP,
    action: 1, // 按下按键的行为
    isRepeat: false, // 优先消费掉按键事件，不上报
  }
  options2: inputConsumer.KeyPressedConfig = {
    key: KeyCode.KEYCODE_VOLUME_DOWN,
    action: 1, // 按下按键的行为
    isRepeat: false, // 优先消费掉按键事件，不上报
  }
  options3: inputConsumer.KeyPressedConfig = {
    key: KeyCode.KEYCODE_FINGERPRINT_SLIDE_UP,
    action: 1, // 按下按键的行为
    isRepeat: false, // 优先消费掉按键事件，不上报
  }
  options4: inputConsumer.KeyPressedConfig = {
    key: KeyCode.KEYCODE_FINGERPRINT_SLIDE_DOWN,
    action: 1, // 按下按键的行为
    isRepeat: false, // 优先消费掉按键事件，不上报
  }
  // 判断设备是否支持KEYCODE_FINGERPRINT_SLIDE_UP 和 KEYCODE_FINGERPRINT_SLIDE_DOWN
  private isFingerprintSlideKeySupported(): Promise<boolean> {
    return new Promise<boolean>((resolve) => {
      inputDevice.getDeviceList((error: BusinessError, ids: Array<Number>) => {
        if (error) {
          console.error(`keyPressed Failed to get device id list, error: ${
            JSON.stringify(error, ['code', 'message'])}`);
          resolve(false);
          return;
        }
        console.info(`keyPressed Device id list: ${JSON.stringify(ids)}`);
        for (let idTemp of ids) {
          let res = inputDevice.supportKeysSync(Number(idTemp), [KeyCode.KEYCODE_FINGERPRINT_SLIDE_UP,
            KeyCode.KEYCODE_FINGERPRINT_SLIDE_DOWN]);
          if (res[0] && res[1]) {
            console.info(`keyPressed ${idTemp} Device id list supportKeysSync : ${JSON.stringify(res)}`);
            resolve(true);
            return;
          }
        }
        resolve(false);
      });
    });
  }

  aboutToAppear(): void {
    try {
      // 点击了音量按键上事件回调
      this.volumeUpCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: 'Volume Up key pressed' })
        // do something
      }

      // 点击了音量按键下事件回调
      this.volumeDownCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: 'Volume Down key pressed' })
        // do something
      }
      // 智控键事件上滑回调
      this.slideUpCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: 'Slide Up key pressed' })
        // do something
      }

      // 智控键事件下滑回调
      this.slideDownCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: 'Slide Down key pressed' })
        // do something
      }
      this.isFingerprintSlideKeySupported().then((supported: boolean) => {
        this.showComponent = supported;
      }).catch((error: Error) => {
        console.error(`Failed to check fingerprint support: ${JSON.stringify(error)}`);
        this.showComponent = false;
      });
    } catch (error) {
      hilog.error(DOMAIN, 'InputConsumer', `Subscribe execute failed, error: %{public}s`,
        JSON.stringify(error, ["code", "message"]));
    }
  }

  build() {
    Column() {
      // 注册及去注册音量键事件
      Row() {
        Button('Add monitoring for Volume Up key')
          .onClick(() => {
            try {
              // 添加指定回调函数
              inputConsumer.on('keyPressed', this.options1, this.volumeUpCallBackFunc);
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Successfully added monitoring for Volume Up key!' })
              this.text = "Monitoring for Volume Up key has been added."
            } catch (error) {
              hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                JSON.stringify(error, ["code", "message"]));
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Failed to add monitoring for Volume Up key!' })
              this.text = `Failed to add monitoring for Volume Up key: ${JSON.stringify(error, ["code", "message"])}`
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 20 })

      Row() {
        Button('Remove monitoring for Volume Up key')
          .onClick(() => {
            try {
              // 取消指定回调函数
              inputConsumer.off('keyPressed', this.volumeUpCallBackFunc);
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Successfully removed monitoring for Volume Up key!' })
              this.text = "Monitoring for Volume Up key has been removed."
            } catch (error) {
              hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                JSON.stringify(error, ["code", "message"]));
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Failed to remove monitoring for Volume Up key!' })
              this.text = `Failed to remove monitoring for Volume Up key: ${JSON.stringify(error, ["code", "message"])}`
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 20 })

      Row() {
        Button('Add monitoring for Volume Down key')
          .onClick(() => {
            try {
              // 添加指定回调函数
              inputConsumer.on('keyPressed', this.options2, this.volumeDownCallBackFunc);
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Successfully added monitoring for Volume Down key!' })
              this.text = "Monitoring for Volume Down key has been added."
            } catch (error) {
              hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                JSON.stringify(error, ["code", "message"]));
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Failed to add monitoring for Volume Down key!' })
              this.text = `Failed to add monitoring for Volume Down key: ${JSON.stringify(error, ["code", "message"])}`
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 20 })

      Row() {
        Button('Remove monitoring for Volume Down key')
          .onClick(() => {
            try {
              // 取消指定回调函数
              inputConsumer.off('keyPressed', this.volumeDownCallBackFunc);
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Successfully removed monitoring for Volume Down key!' })
              this.text = "Monitoring for Volume Down key has been removed."
            } catch (error) {
              hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                JSON.stringify(error, ["code", "message"]));
              this.getUIContext()
                .getPromptAction()
                .showToast({ message: 'Failed to remove monitoring for Volume Down key!' })
              this.text =
                `Failed to remove monitoring for Volume Down key: ${JSON.stringify(error, ["code", "message"])}`
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 20 })

      // 注册及去注册智控键事件
      // 若不支持智控键上滑及智控键下滑按键，则关闭用户入口
      if (this.showComponent) {
        Row() {
          Button('Add monitoring for Slide Up key')
            .onClick(() => {
              try {
                // 添加指定回调函数
                inputConsumer.on('keyPressed', this.options3, this.slideUpCallBackFunc);
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Successfully added monitoring for Slide Up key!' })
                this.text = "Monitoring for Slide Up key has been added."
              } catch (error) {
                hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                  JSON.stringify(error, ["code", "message"]));
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Failed to add monitoring for Slide Up key!' })
                this.text = `Failed to add monitoring for Slide Up key: ${JSON.stringify(error, ["code", "message"])}`
              }
            })
        }.width('100%')
        .justifyContent(FlexAlign.Center)
        .margin({ top: 20, bottom: 20 })

        Row() {
          Button('Remove monitoring for Slide Up key')
            .onClick(() => {
              try {
                // 取消指定回调函数
                inputConsumer.off('keyPressed', this.slideUpCallBackFunc);
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Successfully removed monitoring for Slide Up key!' })
                this.text = "Monitoring for Slide Up key has been removed."
              } catch (error) {
                hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                  JSON.stringify(error, ["code", "message"]));
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Failed to remove monitoring for Slide Up key!' })
                this.text =
                  `Failed to remove monitoring for Slide Up key: ${JSON.stringify(error, ["code", "message"])}`
              }
            })
        }.width('100%')
        .justifyContent(FlexAlign.Center)
        .margin({ top: 20, bottom: 20 })

        Row() {
          Button('Add monitoring for Slide Down key')
            .onClick(() => {
              try {
                // 添加指定回调函数
                inputConsumer.on('keyPressed', this.options4, this.slideDownCallBackFunc);
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Successfully added monitoring for Slide Down key!' })
                this.text = "Monitoring for Slide Down key has been added."
              } catch (error) {
                hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                  JSON.stringify(error, ["code", "message"]));
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Failed to add monitoring for Slide Down key!' })
                this.text = `Failed to add monitoring for Slide Down key: ${JSON.stringify(error, ["code", "message"])}`
              }
            })
        }.width('100%')
        .justifyContent(FlexAlign.Center)
        .margin({ top: 20, bottom: 20 })

        Row() {
          Button('Remove monitoring for Slide Down key')
            .onClick(() => {
              try {
                // 取消指定回调函数
                inputConsumer.off('keyPressed', this.slideDownCallBackFunc);
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Successfully removed monitoring for Slide Down key!' })
                this.text = "Monitoring for Slide Down key has been removed."
              } catch (error) {
                hilog.error(DOMAIN, 'InputConsumer', `Unsubscribe execute failed, error: %{public}s`,
                  JSON.stringify(error, ["code", "message"]));
                this.getUIContext()
                  .getPromptAction()
                  .showToast({ message: 'Failed to remove monitoring for Slide Down key!' })
                this.text =
                  `Failed to remove monitoring for Slide Down key: ${JSON.stringify(error, ["code", "message"])}`
              }
            })
        }.width('100%')
        .justifyContent(FlexAlign.Center)
        .margin({ top: 20, bottom: 20 })
      }

      Row() {
        Text(this.text)
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
    }.width('100%').height('100%')
  }
}
```
