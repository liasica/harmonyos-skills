---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-128
title: Web组件如何实现页面截图
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何实现页面截图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:b6cb2f2fe61d712904983ed6f11ebcfdd686fe6c2e19f130582af1c072634358
---

## 问题现象

在Web开发过程中，如何实现将网页内容以图片形式保存并记录屏幕可见区域之外的内容。

## 背景知识

* [webPageSnapshot](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#webpagesnapshot12)：获取网页全量绘制结果。
* [SaveButton](../harmonyos-references/ts-security-components-savebutton.md)：安全控件的保存控件。应用集成保存控件后，用户首次使用保存控件展示弹窗，在点击允许后自动授权，应用会在短时间内获取访问媒体库特权接口的授权。后续使用无需弹窗授权。

## 解决方案

以webPageSnapshot+SaveButton安全控件的方式来完成前端网页的绘制以及图片保存操作。

示例代码如下：

```ts
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  promptAction: PromptAction = this.getUIContext().getPromptAction();
  @State saveButtonOptions: SaveButtonOptions = {
    icon: SaveIconStyle.FULL_FILLED,
    text: SaveDescription.SAVE_IMAGE,
    buttonType: ButtonType.Capsule
  }; // 设置安全控件按钮属性
  atManager = abilityAccessCtrl.createAtManager();

  aboutToAppear(): void {
    webview.WebviewController.enableWholeWebPageDrawing();
  }

  build() {
    Column() {
      SaveButton(this.saveButtonOptions) // 创建安全控件按钮
        .onClick(async (event, result: SaveButtonOnClickResult) => {
          console.info(`Target of event: ${event.target.id}.`);
          if (result === SaveButtonOnClickResult.SUCCESS) {
            try {
              let context: Context = this.getUIContext().getHostContext() as Context;
              this.controller.webPageSnapshot({ id: '1234', size: { width: '100%', height: '100%' } },
                async (error, result) => {
                  if (error) {
                    console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                    return;
                  }
                  if (result) {
                    let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 100 };
                    const imagePackerApi = image.createImagePacker();
                    imagePackerApi.packToData(result.imagePixelMap, packOpts).then(async (buffer: ArrayBuffer) => {
                      let file: fs.File | null = null;
                      try {
                        let helper = photoAccessHelper.getPhotoAccessHelper(context);
                        let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg');
                        file = fs.openSync(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                        fs.writeSync(file.fd, buffer);
                        this.promptAction.showToast({
                          message: '截屏成功',
                          duration: 3000
                        });
                      } catch (error) {
                        console.error(`保存失败，失败原因: ${error.code}`);
                      } finally {
                        if (file !== null) {
                          fs.closeSync(file);
                        }
                      }
                    }).catch((error: BusinessError) => {
                      console.error(`打包失败，失败原因: ${error.code}`);
                    });
                  }
                });
            } catch (err) {
              console.error(`create asset failed with error: ${err.code}, ${err.message}`);
            }
          } else {
            console.error('SaveButtonOnClickResult create asset failed');
          }
        });

      Web({
        src: 'www.example.com',
        controller: this.controller,
      })
        .domStorageAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .overScrollMode(OverScrollMode.NEVER)
        .height('100%')
        .nestedScroll({ scrollForward: NestedScrollMode.SELF_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST });
    };
  }
}
```

webPageSnapshot要求Web页面完全加载和初始化完成才能确保截图内容完整且准确，适合结构简单、静态元素的页面截图。如果网页中有动态资源或者结构相对复杂，推荐使用[滚动截图](../harmonyos-guides/arkts-long-screenshot.md#滚动截图)方案。
