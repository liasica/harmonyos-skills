---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/share-kit-faq-0001
title: 系统分享与数据接收常见问题
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 常见问题 > 系统分享与数据接收常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:52+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:5d7ee9aabe55eb5adc0051e0f07209729266bdb2d7e24551fc2f2bd3a0d4500a
---

**Q：开发者在使用系统分享时，会遇到以下几个经典场景：**

* **场景一：如何实现拉起系统的分享面板，复制、另存为这些按钮？**
* **场景二：如何实现分享多张图片？**
* **场景三：如何实现分享网络图片？**
* **场景四：如何实现接收其他应用分享的文本和图片数据？**
* **场景五：如何限制分享目标应用，仅分享给指定应用？**

**A**：使用systemShare相关API前，需要先引入依赖模块，并获取UIAbilityContext上下文，后续各场景代码均基于以下导入和上下文：

```ts
import { systemShare } from '@kit.ShareKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
// 获取UIAbilityContext，用于访问应用文件目录和拉起分享面板
context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

// ...
}
```

* 针对场景一：系统分享可以自定义配置操作区：
  + 系统操作区提供了复制、保存、另存为、打印、复制到中转站等系统级快捷操作。宿主应用可以根据自己的业务体验需要判断是否给用户提供相关操作。
  + 若分享内容无需打印功能，可通过配置从操作区移除打印按钮，代码示例如下：
    1. 构造分享数据，可添加多条分享记录；

       ```ts
       // this.context为UIAbilityContext，需在组件中提前获取
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
    2. 启动分享面板，并配置不显示打印快捷操作。如需屏蔽其他系统级快捷操作，请参考[ShareAbilityType](../doccenter-capabilities/api/share-system-share.md#shareabilitytype)介绍。

       ```ts
       import { BusinessError } from '@kit.BasicServicesKit';
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
    3. 实现效果图：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/jbLzW1O1S6mm2F2k2P5UIw/zh-cn_image_0000002792063557.png "点击放大")
  + 更多实现示例代码可以参考实现华为分享功能。
* 针对场景二：将[SelectionMode](../harmonyos-references/share-system-share.md#selectionmode)设置为BATCH可支持批量模式，分享全部数据记录，可实现分享多张图片。示例代码如下：

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  private async shareBatch() {
  // this.context为UIAbilityContext，需在组件中提前获取
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
  1. 参考[访问控制-声明权限](../harmonyos-guides/declare-permissions.md)声明[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)权限。
  2. 通过网络请求下载图片，获取图片ArrayBuffer。
  3. 将图片写入应用沙箱目录并保存。
  4. 通过fileUri.getUriFromPath方法获取文件URI。
  5. 使用systemShare分享指定UTD类型和文件URI。

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { http } from '@kit.NetworkKit';
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  imageBuffer: ArrayBuffer | undefined = undefined;
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  // 通过http的request方法从网络下载图片资源
  getPicture(): Promise<void> {
  return new Promise((resolve, reject) => {
  http.createHttp()
  .request('', // 替换为真实网络图片地址
  (error: BusinessError, data: http.HttpResponse) => {
  if (error) {
  // 下载失败时弹窗提示检查网络，不执行后续逻辑
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
  // 判断网络获取到的资源是否为ArrayBuffer类型
  if (data.result instanceof ArrayBuffer) {
  this.imageBuffer = data.result as ArrayBuffer;
  }
  resolve();
  }
  );
  });
  }

  // 保存到沙箱路径
  async shareNetImage(): Promise<void> {
  this.imageBuffer = undefined;
  await this.getPicture();
  try {
  const path = this.context.filesDir + '/XXXX'; // XXXX替换为真实文件名
  const file = await fileIo.open(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  await fileIo.write(file.fd, this.imageBuffer);
  await fileIo.close(file.fd);
  // 生成应用URI
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

  完整示例代码：

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
  // Startsolution4
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  imageBuffer: ArrayBuffer | undefined = undefined;
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  // 通过http的request方法从网络下载图片资源
  getPicture(): Promise<void> {
  return new Promise((resolve, reject) => {
  http.createHttp()
  .request('', // 替换为真实网络图片地址
  (error: BusinessError, data: http.HttpResponse) => {
  if (error) {
  // 下载失败时弹窗提示检查网络，不执行后续逻辑
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
  // 判断网络获取到的资源是否为ArrayBuffer类型
  if (data.result instanceof ArrayBuffer) {
  this.imageBuffer = data.result as ArrayBuffer;
  }
  resolve();
  }
  );
  });
  }

  // 保存到沙箱路径
  async shareNetImage(): Promise<void> {
  this.imageBuffer = undefined;
  await this.getPicture();
  try {
  const path = this.context.filesDir + '/XXXX'; // XXXX替换为真实文件名
  const file = await fileIo.open(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
  await fileIo.write(file.fd, this.imageBuffer);
  await fileIo.close(file.fd);
  // 生成应用URI
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

  // Endsolution4

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
  console.info(`write data to file succeed and size is: ${writeLen}`);
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

  // Startsolution2
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
  // Endsolution2
  }
  }
  ```
* 针对场景四：接收方应用需要按照以下步骤实现分享数据的接收：
  1. 在module.json5的skills中声明支持ohos.want.action.sendData，并配置可接收的UTD（如general.image、文本类型等），可参考[目标应用处理分享内容](../harmonyos-guides/share-target-application.md)。
  2. 应用启动后，在onCreate或onNewWant回调中获取want参数，通过[systemShare.getSharedData](../harmonyos-references/share-system-share.md#getshareddata)解析分享数据，再跳转到编辑页面，可参考[应用内处理分享内容](../harmonyos-guides/share-interface-description.md)。
  3. 图片/文件建议使用[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)或系统可访问URI传递，接收方收到后如需长期编辑，应复制到自己的沙箱目录。

  发送方需使用精确UTD，图片优先使用general.image或按扩展名解析出的UTD，不要直接传应用沙箱物理路径。若需实现文字和图片一起分享，可通过多条SharedRecord添加文本和图片记录，两端需约定清楚数据结构。如需定向跳转到指定应用的指定编辑页，优先让目标应用提供明确的分享接收Ability或App Linking/深链能力。接收其他应用分享的图片示例可参考[接收分享图片示例](../architecture-guides/receive_image_share-0000002405380589.md)。
* 针对场景五：该功能仅对企业应用开放，可通过[配置目标应用名单](../harmonyos-guides/share-app-sharing-mode.md)限制分享目标应用范围。配置成功后，仅名单内的目标应用可出现在系统分享面板的分享推荐区和分享方式区。
  1. 申请受限开放权限ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST，在module.json5配置文件的requestPermissions标签中声明该权限。
  2. 启动分享面板时，通过配置appLaunchTrustInfo参数指定目标应用范围，最多支持50个应用。

**Q：使用Share Kit API分享图片，URI是本地图片地址，如何设置为http或者https开头的线上图片？**

**A**：系统分享不支持分享远端图片；应先将网络图片保存至本地，获取路径后再进行分享。

**Q：调用系统分享Share Kit后，没有分享的目标应用。**

**A**：目标应用需要具备数据处理能力组件并在配置文件中声明所支持的分享能力，可参考[目标应用处理分享内容](../harmonyos-guides/share-target-application.md)。

**Q：使用systemShare.getSharedData(want)获取分享的数据，报错1003703001，如何解决？**

**A**：数据记录数量超过限制，可以不通过getSharedData接口获取分享数据，直接从want.uri属性，即分享的链接中，解析出分享的数据。

**Q：Share Kit简介文档中"宿主应用配置[分享数据描述信息](../harmonyos-references/share-system-share.md#shareddata)总量不能超过200KB"是指分享的文件大小吗？**

**A**：Share Kit简介文档中提到的200KB限制是指分享的数据描述信息的大小限制，而不是单个文件的大小限制。即通过Share Kit分享多个文件或大量数据时，需确保这些数据的总描述信息不超过200KB的限制。

**Q：PC端用华为分享发一个文件到PAD端，PAD端接收后会自动打开文件预览，但是PAD端华为分享发给PC端一个文件，PC接收后显示的文件分享列表，并没有文件预览，这是系统规格吗？**

**A**：是的，系统规格；其他设备将文件分享至PC时，文件默认保存至华为分享目录，不会直接打开；当分享到PAD上会直接预览打开。

**Q：接入华为分享是否还需要再对接其他系统（如微信、微博等）的分享？**

**A**：统一分享提供分享入口和面板，目标应用需要对能够接收的数据类型进行定义，宿主应用需要按照规范定义分享数据。接入统一分享后，系统自动识别该分享数据可分享至哪些目标应用，在分享面板中展示。无需开发者进行主动接入。具体流程可参考[系统分享流程](../doccenter-capabilities/system-share-overview.md)。系统分享的实现宿主应用和目标应用要分别遵守[宿主应用开发规范](../harmonyos-guides/share-map-creation.md)和[目标应用开发规范](../harmonyos-guides/share-target-application.md)。

**Q：使用系统的分享，怎么拿到结果回调。**

**A**：可参考[获取分享结果](../harmonyos-guides/share-share-completed.md)，注意从5.1.0(18)版本开始，支持宿主应用获取用户分享结果。

**Q：系统分享"保存至图库"是否需要权限，按钮能否自定义？**

**A**：系统分享保存图片到图库不需要额外申请权限，保证用户体验的一致性，无法自定义面板上的公共按钮。

**Q：碰一碰分享是否可以跳过卡片分享页面直接分享数据？**

**A**：碰一碰不支持直接分享数据，存在误触的可能性，极端情况会导致数据发送给非预期的设备。

**Q：手机分享文件给PC设备，是否可以默认指定应用打开文件？**

**A**：目前不支持，PC接收到文件后会存储在文件管理"华为分享"目录，默认用文件管理高亮显示接收到的文件。

**Q：系统分享如何传递自定义参数？**

**A**：可参考[SharedData](../harmonyos-references/share-system-share.md#shareddata)接口说明。

**Q：如何区分通过隔空传送分享过来的数据和通过本地文件管理点击文件选择其他应用打开的数据？**

**A**：隔空传送接收的数据不会直接发给应用，通常通过图库或者文件管理接收，最常用的是通过预览的方式拉起应用。

**Q：如何实现自定义分享方式？**

**A**：可参考[半接模式分享](../harmonyos-guides/share-access-mode.md#半接模式示例代码片段)，开发者自行开发分享能力面板，并在分享面板中提供系统分享入口。适用于分享方式区有商业诉求，或有自己独有的业务逻辑的开发者。

**Q：分享PDF文件时，分享面板没有自己开发的应用，如何打开三方应用分享的PDF文件？**

**A**：具体操作步骤如下：

1. 目标应用注册支持分享内容的能力。在应用配置文件添加skills。

   ```ts
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             },
             // 添加skill配置
             {
               "actions": [
                 // 必需，声明数据处理能力
                 "ohos.want.action.viewData",
                 "ohos.want.action.sendData"
               ],
               "uris": [
                 {
                   "scheme": "file",
                   // 目标应用在配置支持接收的数据类型时，需穷举支持的UTD。
                   "utd": "com.adobe.pdf",
                   // maxFileSupported对于归属指定类型的文件，标识一次支持接收的最大数量。默认为0，代表不支持此类文件的分享。
                   "maxFileSupported": 1
                 },
                 {
                   "scheme": "file",
                   "utd": "general.object",
                   "maxFileSupported": 1
                 }
               ]
             }
           ]
         }
       ]
     }
   }
   ```
2. 获取三方应用分享的内容。由于存在应用沙箱隔离，被分享的目标应用无法直接操作宿主应用沙箱中的文件，需拷贝文件至本应用沙箱。

   ```ts
   import { UIAbility, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { systemShare } from '@kit.ShareKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(want: Want): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
       this.handleSharedData(want);
     }

     onNewWant(want: Want): void {
       this.handleSharedData(want);
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
       });
     }

     handleSharedData(want: Want) {
       systemShare.getSharedData(want)
         .then((data: systemShare.SharedData) => {
           data?.getRecords()?.forEach((record: systemShare.SharedRecord) => {
             if (!record.uri) {
               return;
             }

             try {
               // 获取uri，缓存至应用沙箱
               const file = fileIo.openSync(record.uri, fileIo.OpenMode.READ_ONLY);
               const destPath = this.context.cacheDir + '/' + file.name;
               const outFile = fileIo.openSync(destPath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
               const shareFilePath = outFile.path;
               fileIo.copyFileSync(file.fd, outFile.fd);
               fileIo.closeSync(file);
               fileIo.closeSync(outFile);
               AppStorage.setOrCreate('SHARE_FILE_PATH', shareFilePath);
             } catch (error) {
               console.error(`Failed to parse share data. Code: ${error.code}, message: ${error.message}`);
             }
           });
         })
         .catch((error: BusinessError) => {
           console.error(`Failed to getSharedData. Code: ${error.code}, message: ${error.message}`);
         });
     }
   };
   ```
3. 使用PdfView预览PDF文件。

   ```screen
   import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';

   @Entry
   @Component
   struct Index {
     context = this.getUIContext().getHostContext()!;
     private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();

     build() {
       Column() {
         Button('预览')
           .onClick(() => {
             const path = AppStorage.get('SHARE_FILE_PATH') as string;
             const pdfDocument: pdfService.PdfDocument = new pdfService.PdfDocument();
             pdfDocument.loadDocument(path);
             this.controller.loadDocument(path);
           })

         PdfView({
           controller: this.controller,
           pageFit: pdfService.PageFit.FIT_WIDTH,
           showScroll: true
         })
           .id('pdfview_app_view')
           .layoutWeight(1)
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

**Q：为什么WPS移动版分享PDF文件看不到目标应用？**

**A**：宿主应用在发起文件分享时，填写的UTD可能有差异，目标应用需穷举支持的UTD类型“general.object”。
