---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-19
title: 如何拦截系统音量调节的上下键
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何拦截系统音量调节的上下键
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:27f1933ef864c89ed00448aee106de7fb633b4877f3eb6d234df0fe5a49794ce
---

## 问题现象

在特定业务场景中，开发者需要拦截设备音量调节键的事件上报，以完成业务特定功能，比如阅读场景中，通过按音量上下键实现翻页的功能。

## 解决措施

通过[监听系统的多模态按键事件](../harmonyos-references/js-apis-inputconsumer.md#inputconsumeronkeypressed16)，拦截手机的音量的上下键的系统事件上报，并插入开发者自己的业务逻辑（比如相机拍摄、翻页阅读等功能），具体示例代码如下：

```ts
import { inputConsumer, KeyEvent } from '@kit.InputKit';
import { KeyCode } from '@kit.InputKit';

@Entry
@Component
struct TestDemo14 {
  private volumeUpCallBackFunc: (event: KeyEvent) => void = () => {
  }
  private volumeDownCallBackFunc: (event: KeyEvent) => void = () => {
  }

  aboutToAppear(): void {
    try {
      let options1: inputConsumer.KeyPressedConfig = {
        key: KeyCode.KEYCODE_VOLUME_UP,
        action: 1, // 按下按键的行为
        isRepeat: false, // 优先消费掉按键事件，不上报
      }
      let options2: inputConsumer.KeyPressedConfig = {
        key: KeyCode.KEYCODE_VOLUME_DOWN,
        action: 1, // 按下按键的行为
        isRepeat: false, // 优先消费掉按键事件，不上报
      }

      // 点击了音量按键上事件回调
      this.volumeUpCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: '点击了音量按键上' })
        // do something
      }

      // 点击了音量按键下事件回调
      this.volumeDownCallBackFunc = (event: KeyEvent) => {
        this.getUIContext().getPromptAction().showToast({ message: '点击了音量按键下' })
        // do something
      }
      // 注册监听事件
      inputConsumer.on('keyPressed', options1, this.volumeUpCallBackFunc);
      inputConsumer.on('keyPressed', options2, this.volumeDownCallBackFunc);
    } catch (error) {
      console.error(`Subscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('取消监听音量按键上的监听')
          .onClick(() => {
            try {
              // 取消指定回调函数
              inputConsumer.off('keyPressed', this.volumeUpCallBackFunc);
              this.getUIContext().getPromptAction().showToast({ message: '取消监听音量按键上的监听事件成功！' })
            } catch (error) {
              console.error(`Unsubscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 50 })

      Row() {
        Button('取消监听音量按键下的监听')
          .onClick(() => {
            try {
              // 取消指定回调函数
              inputConsumer.off('keyPressed', this.volumeDownCallBackFunc);
              this.getUIContext().getPromptAction().showToast({ message: '取消监听音量按键下的监听事件成功！' })
            } catch (error) {
              console.error(`Unsubscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
            }
          })
      }.width('100%')
      .justifyContent(FlexAlign.Center)
      .margin({ top: 20, bottom: 50 })
      Row(){
        Text('已默认添加监听音量按键上和下的监听')
      }
      .width('100%')
      .justifyContent(FlexAlign.Center)
    }.width('100%').height('100%')
  }
}
```
