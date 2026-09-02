---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-5
title: 系统分享常见使用场景
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 系统分享常见使用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:ef577b3e6d664aa2f05cec03f0edd066e733ff2633c0a5910ab1555321295391
---

## 问题现象

开发者在使用系统分享时，会遇到以下几个经典场景：

场景一：如何实现拉起系统的分享面板，复制、另存为这些按钮？

场景二：如何实现分享多张图片？

场景三：如何实现分享网络图片？

## 背景知识

* [系统分享服务](../harmonyos-guides/system-share.md)为应用提供文本、图片、视频等内容跨应用分享能力，用于将内容发送到其他应用甚至其他应用的用户。
* 应用把需要分享的内容和预览样式配置给系统分享服务，系统分享服务将根据分享的数据类型、数量等信息构建分享面板，为用户提供内容预览、推荐分享联系人、关联应用及操作界面，便于用户快速选择分享应用或操作，将内容分发到目标应用。
* [systemShare](../harmonyos-references/share-system-share.md)提供分享数据创建及分享面板拉起的功能，提供多种系统标准分享服务，例如分享数据给其他应用、复制、打印等。其中[SelectionMode](../harmonyos-references/share-system-share.md#selectionmode)分享面板选择模式，支持单选模式和多选模式。
* [bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)给组件绑定菜单，控制菜单显隐的触发方式为长按或右键点击。
* [标准化数据类型](../harmonyos-guides/uniform-data-type-list.md)（Uniform Type Descriptor，简称UTD）用于解决系统中的类型模糊问题，即针对同一种数据类型，存在不同的类型描述方式：MIME Type、文件扩展名等。
* [应用沙箱](../harmonyos-guides/app-sandbox-directory.md)是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”。

## 解决方案

* 针对场景一：系统分享可以**自定义配置操作区**：
  + 系统操作区提供了复制、保存、另存为、打印、复制到中转站等系统级快捷操作。宿主应用可以根据自己的业务体验需要判断是否给用户提供相关操作。
  + 若分享内容无需打印功能，可通过配置从操作区移除打印按钮，代码示例如下：
    1. 构造分享数据，可添加多条分享记录；

       ```ts
       let shareData: systemShare.SharedData = new systemShare.SharedData({
         utd: utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE),
         uri: fileUri.getUriFromPath(this.context.filesDir + '/exampleKnock1.jpg'),
         title: 'exampleKnock1',
         description: 'Image Description',
       });

       try {
         shareData.addRecord({
           utd: utd.getUniformDataTypeByFilenameExtension('.png', utd.UniformDataType.IMAGE),
           uri: fileUri.getUriFromPath(this.context.filesDir + '/exampleKnock2.png'),
           title: 'exampleKnock2',
           description: 'Image Description',
         });
       } catch (error) {
         console.error(`addRecord error. Code: ${error?.code}, message: ${error?.message}`);
       }
       ```
    2. 启动分享面板，并配置不显示打印快捷操作。如需屏蔽其他系统级快捷操作，请参考[ShareAbilityType](../harmonyos-references/share-system-share.md#shareabilitytype)介绍。

       ```ts
       let controller: systemShare.ShareController = new systemShare.ShareController(shareData);

       controller.show(this.context, {
         selectionMode: systemShare.SelectionMode.SINGLE,
         previewMode: systemShare.SharePreviewMode.DETAIL,
         excludedAbilities: [systemShare.ShareAbilityType.PRINT, systemShare.ShareAbilityType.COPY_TO_PASTEBOARD,
           systemShare.ShareAbilityType.SAVE_AS_FILE, systemShare.ShareAbilityType.SAVE_TO_MEDIA_ASSET]
       }).then(() => {
         console.info('ShareController show success.');
       }).catch((error: BusinessError) => {
         console.error(`ShareController show error. code: ${error?.code}, message: ${error?.message}`);
       });
       ```
    3. 效果预览：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ISP76NAYQvecWuSVeMyU9g/zh-cn_image_0000002628554416.png "点击放大")
  + 更多实现示例代码可以参考[实现华为分享功能](https://gitcode.com/HarmonyOS_Samples/share-kit_-sample-code_-clientdemo_-arkts)。
* 针对场景二：将[SelectionMode](../harmonyos-references/share-system-share.md#selectionmode)设置为BATCH可支持批量模式，分享全部数据记录，可实现分享多张图片。示例代码如下：

  ```ts
  private async shareBatch() {
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE),
      uri: fileUri.getUriFromPath(this.context.filesDir + '/exampleKnock1.jpg'),
      title: 'exampleKnock1',
      description: 'Image Description',
    });

    try {
      shareData.addRecord({
        utd: utd.getUniformDataTypeByFilenameExtension('.png', utd.UniformDataType.IMAGE),
        uri: fileUri.getUriFromPath(this.context.filesDir + '/exampleKnock2.png'),
        title: 'exampleKnock2',
        description: 'Image Description',
      });
    } catch (error) {
      console.error(`addRecord error. Code: ${error?.code}, message: ${error?.message}`);
    }

    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);

    controller.show(this.context, {
      previewMode: systemShare.SharePreviewMode.DETAIL,
      selectionMode: systemShare.SelectionMode.BATCH,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(`ShareController show error. code: ${error?.code}, message: ${error?.message}`);
    });
  }
  ```
* 针对场景三：
  1. 参考[访问控制-声明权限](../harmonyos-guides/declare-permissions.md)声明[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)权限;
  2. 通过网络请求下载图片，获取图片ArrayBuffer；
  3. 将图片写入应用沙箱目录并保存；
  4. 通过fileUri.getUriFromPath方法获取文件URI；
  5. 使用systemShare分享指定UTD类型和文件URI。

  ```ts
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  imageBuffer: ArrayBuffer | undefined = undefined;
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  // *通过http的request方法从网络下载图片资源*
  getPicture(): Promise<void> {
    return new Promise((resolve, reject) => {
      http.createHttp()
        .request('', // *替换为真实网络图片地址*
          (error: BusinessError, data: http.HttpResponse) => {
            if (error) {
              // *下载失败时弹窗提示检查网络，不执行后续逻辑*
              try {
                this.promptAction.showToast({
                  message: '图片加载失败，请检查网络',
                  duration: 2000
                });
              } catch (error) {
                console.error(`download error. code: ${error?.code}, message: ${error?.message}`);
              }
              reject();
              return;
            }
            // *判断网络获取到的资源是否为ArrayBuffer类型*
            if (data.result instanceof ArrayBuffer) {
              this.imageBuffer = data.result as ArrayBuffer;
            }
            resolve();
          }
        );
    });
  }

  // *保存到沙箱路径*
  async shareNetImage(): Promise<void> {
    this.imageBuffer = undefined;
    await this.getPicture();
    try {
      const path = this.context.filesDir + '/XXXX'; // *XXXX替换为真实文件名*
      const file = await fileIo.open(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      await fileIo.write(file.fd, this.imageBuffer);
      await fileIo.close(file.fd);
      // *生成应用URI*
      const uri = fileUri.getUriFromPath(path);
      const data: systemShare.SharedData = new systemShare.SharedData({
        utd: utd.UniformDataType.IMAGE,
        uri: uri
      });
      const controller: systemShare.ShareController = new systemShare.ShareController(data);

      controller.show(this.context, {
        previewMode: systemShare.SharePreviewMode.DETAIL,
        selectionMode: systemShare.SelectionMode.SINGLE
      }).then(() => {
        console.info('ShareController show success.');
      }).catch((error: BusinessError) => {
        console.error(`ShareController show error. code: ${error?.code}, message: ${error?.message}`);
      });
    } catch (error) {
      console.error(`fileIo error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }
  ```

完整示例参考如下：

```ts
import { systemShare } from '@kit.ShareKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  imageBuffer: ArrayBuffer | undefined = undefined;
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  // *通过http的request方法从网络下载图片资源*
  getPicture(): Promise<void> {
    return new Promise((resolve, reject) => {
      http.createHttp()
        .request('', // *替换为真实网络图片地址*
          (error: BusinessError, data: http.HttpResponse) => {
            if (error) {
              // *下载失败时弹窗提示检查网络，不执行后续逻辑*
              try {
                this.promptAction.showToast({
                  message: '图片加载失败，请检查网络',
                  duration: 2000
                });
              } catch (error) {
                console.error(`download error. code: ${error?.code}, message: ${error?.message}`);
              }
              reject();
              return;
            }
            // *判断网络获取到的资源是否为ArrayBuffer类型*
            if (data.result instanceof ArrayBuffer) {
              this.imageBuffer = data.result as ArrayBuffer;
            }
            resolve();
          }
        );
    });
  }

  // *保存到沙箱路径*
  async shareNetImage(): Promise<void> {
    this.imageBuffer = undefined;
    await this.getPicture();
    try {
      const path = this.context.filesDir + '/XXXX'; // *XXXX替换为真实文件名*
      const file = await fileIo.open(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
      await fileIo.write(file.fd, this.imageBuffer);
      await fileIo.close(file.fd);
      // *生成应用URI*
      const uri = fileUri.getUriFromPath(path);
      const data: systemShare.SharedData = new systemShare.SharedData({
        utd: utd.UniformDataType.IMAGE,
        uri: uri
      });
      const controller: systemShare.ShareController = new systemShare.ShareController(data);

      controller.show(this.context, {
        previewMode: systemShare.SharePreviewMode.DETAIL,
        selectionMode: systemShare.SelectionMode.SINGLE
      }).then(() => {
        console.info('ShareController show success.');
      }).catch((error: BusinessError) => {
        console.error(`ShareController show error. code: ${error?.code}, message: ${error?.message}`);
      });
    } catch (error) {
      console.error(`fileIo error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }

  aboutToAppear(): void {
    const filesDir = this.context.filesDir;
    try {
      [
        [this.context.resourceManager.getMediaContentSync($r('app.media.exampleImage').id), '/exampleImage.jpg'],
        [this.context.resourceManager.getMediaContentSync($r('app.media.exampleVideo').id), '/exampleVideo.mp4'],
        [this.context.resourceManager.getMediaContentSync($r('app.media.startIcon').id), '/icon.jpg'],
        [this.context.resourceManager.getMediaContentSync($r('app.media.exampleKnock1').id), '/exampleKnock1.jpg'],
        [this.context.resourceManager.getMediaContentSync($r('app.media.exampleKnock2').id), '/exampleKnock2.png'],
        [this.context.resourceManager.getMediaContentSync($r('app.media.exampleKnock3').id), '/exampleKnock3.jpg'],
      ].forEach(item => {
        let file = fileIo.openSync(filesDir + item[1], fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
        let writeLen = fileIo.writeSync(file.fd, (item[0] as Uint8Array).buffer);
        console.info('write data to file succeed and size is:' + writeLen);
        fileIo.closeSync(file);
      });
    } catch (error) {
      console.error(`getMediaContentSync error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }

  private async shareCustomPanel() {
    let filePath = this.context.filesDir + '/exampleImage.jpg';
    let utdTypeId = utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE);
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utdTypeId,
      uri: fileUri.getUriFromPath(filePath),
      title: 'Picture Title',
      description: 'Picture Description',
    });

    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);

    controller.show(this.context, {
      selectionMode: systemShare.SelectionMode.SINGLE,
      previewMode: systemShare.SharePreviewMode.DETAIL,
      excludedAbilities: [systemShare.ShareAbilityType.PRINT, systemShare.ShareAbilityType.COPY_TO_PASTEBOARD,
        systemShare.ShareAbilityType.SAVE_AS_FILE, systemShare.ShareAbilityType.SAVE_TO_MEDIA_ASSET]
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(`ShareController show error. code: ${error?.code}, message: ${error?.message}`);
    });
  }

  private async shareBatch() {
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.getUniformDataTypeByFilenameExtension('.jpg', utd.UniformDataType.IMAGE),
      uri: fileUri.getUriFromPath(this.context.filesDir + '/exampleKnock1.jpg'),
      title: 'exampleKnock1',
      description: 'Image Description',
    });

    try {
      shareData.addRecord({
        utd: utd.getUniformDataTypeByFilenameExtension('.png', utd.UniformDataType.IMAGE),
        uri: fileUri.getUriFromPath(this.context.filesDir + '/exampleKnock2.png'),
        title: 'exampleKnock2',
        description: 'Image Description',
      });
    } catch (error) {
      console.error(`addRecord error. Code: ${error?.code}, message: ${error?.message}`);
    }

    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);

    controller.show(this.context, {
      previewMode: systemShare.SharePreviewMode.DETAIL,
      selectionMode: systemShare.SelectionMode.BATCH,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(`ShareController show error. code: ${error?.code}, message: ${error?.message}`);
    });
  }

  build() {
    Column({ space: 5 }) {

      Button('自定义配置操作区').onClick(() => {
        this.shareCustomPanel();
      })

      Button('批量分享').onClick(() => {
        this.shareBatch();
      })

      Button('网络图片分享').onClick(() => {
        this.shareNetImage();
      })

    }
    .width('100%')
    .height('100%')
  }
}
```

## 常见FAQ

Q：使用Share kit API分享图片，URI是本地图片地址，如何设置为http或者https开头的线上图片？

A：系统分享不支持分享远端图片；应先将网络图片保存至本地，获取路径后再进行分享。

Q：调用系统分享Share kit后，没有分享的目标应用。

A：目标应用需要具备数据处理能力组件并在配置文件中声明所支持的分享能力，可参考[目标应用处理分享内容](../harmonyos-guides/share-target-application.md)。

Q：使用systemShare.getSharedData(want)获取分享的数据，报错1003703001，如何解决？

A：数据记录数量超过限制，可以不通过getSharedData接口获取分享数据，直接从want.uri属性，即分享的链接中，解析出分享的数据。

Q：Share Kit简介文档中“宿主应用配置[分享数据描述信息](../harmonyos-references/share-system-share.md#shareddata)总量不能超过200KB”是指分享的文件大小吗？

A：Share Kit简介文档中提到的200KB限制是指分享的数据描述信息的大小限制，而不是单个文件的大小限制。即通过Share Kit分享多个文件或大量数据时，需确保这些数据的总描述信息不超过200KB的限制。

Q：PC端用华为分享发一个文件到PAD端，PAD端接收后会自动打开文件预览，但是PAD端华为分享发给PC端一个文件，PC接收后显示的文件分享列表，并没有文件预览，这是系统规格吗？

A：是的，系统规格；其他设备将文件分享至PC时，文件默认保存至华为分享目录，不会直接打开；当分享到PAD上会直接预览打开。

Q：接入华为分享是否还需要再对接其他系统（如微信、微博等）的分享？

A：

* 统一分享提供分享入口和面板，目标应用需要对能够接收的数据类型进行定义，宿主应用需要按照规范定义分享数据。接入统一分享后，系统自动识别该分享数据可分享至哪些目标应用，在分享面板中展示。无需开发者进行主动接入。具体流程可参考[系统分享流程](../design-guides/share-0000001957076313.md)。
* 系统分享的实现宿主应用和目标应用要分别遵守[宿主应用开发规范](../harmonyos-guides/share-map-creation.md)和[目标应用开发规范](../harmonyos-guides/share-target-application.md)。

Q：使用系统的分享，怎么拿到结果回调。

A：可参考[获取分享结果](../harmonyos-guides/share-share-completed.md)，注意从5.1.0(18)版本开始，支持宿主应用获取用户分享结果。

Q：系统分享“保存至图库”是否需要权限，按钮能否自定义？

A：系统分享保存图片到图库不需要额外申请权限，保证用户体验的一致性，无法自定义面板上的公共按钮。

Q：碰一碰分享是否可以跳过卡片分享页面直接分享数据？

A：碰一碰不支持直接分享数据，存在误触的可能性，极端情况会导致数据发送给非预期的设备。

Q：手机分享文件给PC设备，是否可以默认指定应用打开文件？

A：目前不支持，PC接收到文件后会存储在文件管理“华为分享”目录，默认用文件管理高亮显示接收到的文件。
