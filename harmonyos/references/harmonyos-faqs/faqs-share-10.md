---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-10
title: 如何隔空传送打开App Linking链接直达应用
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 如何隔空传送打开App Linking链接直达应用
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:26+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:dd7f28866a9a98bae2a99fe25ed8266e83826b1ebb177f47c311c5b23b3738b8
---

## 问题现象

设备A如何使用隔空传送的传递App Linking链接直达设备B打开？

## 背景知识

[App Linking Kit（应用链接服务）](../harmonyos-guides/applinking-introduction.md)：通过App Linking应用链接拉起指定应用，实现应用间跳转。当应用已安装时，优先通过应用展示内容；若应用未安装，则通过系统浏览器展示网页版内容。

[隔空传送](../harmonyos-guides/gestures-share-overview.md)：用户通过“一抓一放”手势实现跨设备文件分享（图片、视频、文档等）以及跨设备链接分享。

## 解决方案

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/uGX2mijpRj2Bc-xgV29E8w/zh-cn_image_0000002643336236.png "点击放大")

实现跨设备链接隔空传送分享流程如上，其中A设备应用为宿主应用，B设备应用为目标应用。需要分别实现目标方和宿主方应用配置。

**目标应用配置：**

1. 关联的网址域名的配置。目标应用侧需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上完成关联的网址域名的配置，具体步骤参考[目标方应用配置应用链接能力](../harmonyos-guides/app-linking-startupapp.md#配置应用链接能力)并[在AGC为应用创建关联的网址域名](../harmonyos-guides/app-linking-startupapp.md#在agc为应用创建关联的网址域名)。
2. 在应用module.json5的skills中配置应用直达链接域名。App Linking链接格式通常为：scheme://host/path。具体步骤参考[在module.json5中配置关联的网址域名](../harmonyos-guides/app-linking-startupapp.md#在modulejson5中配置关联的网址域名)，代码设置如下：

   ```json
   {
     "entities": [
       // entities必须包含"entity.system.browsable"
       "entity.system.browsable"
     ],
     "actions": [
       // actions必须包含"ohos.want.action.viewData"
       "ohos.want.action.viewData"
     ],
     "uris": [
       {
         // scheme须配置为https
         "scheme": "https",
         // host须配置为关联的网址域名，实际运行时替换为真实的App Linking链接域名
         "host": "www.example.com",
         // path可选，表示域名服务器上的目录或文件路径，例如www.example.com/path1中的path1
         // 如果应用只能处理部分特定的path，则此处应该配置应用所支持的path，避免出现应用不能处理的path链接也被引流到应用中的问题
         "path": "path1"
       }
     ],
     // domainVerify须设置为true
     "domainVerify": true
   }
   ```

   **须知** 

   * path、pathStartWith、pathRegex的取值前后均不需要加斜杠/。
   * 建议scheme和host中不要包含大写字母。
3. 在UIAbility的onCreate()方法和onNewWant()方法中接收处理收到的分享链接，代码如下：

   ```ts
   onCreate(want: Want): void {
     try {
       this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
     } catch (err) {
       hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
     }
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     let uri = want?.uri;
     if (uri) {
       let urlObject = url.URL.parseURL(uri);
       let index = urlObject.params.get('index') as string;
       AppStorage.setOrCreate('GesturesShare_shareIndex', 'Result:' + index);
       AppStorage.setOrCreate('GesturesShare_isShareLink', true);
       hilog.info(DOMAIN, 'testTag', 'EntryAbility onCreate invoked. uri: %{public}s', uri);
     }
   }

   onNewWant(want: Want): void {
     let uri = want?.uri;
     if (uri) {
       let urlObject = url.URL.parseURL(uri);
       let index = urlObject.params.get('index') as string;
       AppStorage.setOrCreate('GesturesShare_shareIndex', 'Result:' + index);
       AppStorage.setOrCreate('GesturesShare_isShareLink', true);
       hilog.info(DOMAIN, 'testTag', 'EntryAbility onCreate invoked. uri: %{public}s', uri);
     }
   }
   ```

   在Page页面显示接收的分享内容：

   ```ts
   @StorageLink('GesturesShare_isShareLink') isShareLink: boolean = false;
   @StorageLink('GesturesShare_shareIndex') shareResult: string = '隔空传送分享AppLinking';

   build() {
     RelativeContainer() {
       Text(this.shareResult)
         .fontSize('35fp')
         .fontWeight(FontWeight.Bold)
         .alignRules({
           center: { anchor: '__container__', align: VerticalAlign.Center },
           middle: { anchor: '__container__', align: HorizontalAlign.Center }
         })
     }
     .height('100%')
     .width('100%')
   }
   ```

   **须知** 

   不能使用DevEco Studio的自动签名功能，必须使用[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)，否则无法拉起应用。

**宿主应用配置：**

1. 构造华为分享事件触发后的回调[SharableTarget](../harmonyos-references/share-harmony-share.md#sharabletarget)。设置utd类型为utd.UniformDataType.HYPERLINK,表示分享内容为链接。分享链接通过目标方应用关联的网址域名和自定义参数拼接而成。代码如下：

   ```ts
   private immersiveCallback = (sharableTarget: harmonyShare.SharableTarget) => {
     let filePath = this.context.filesDir + '/gestures_immersive.png'; // 仅为示例 请替换正确的文件路径
     let shareData: systemShare.SharedData = new systemShare.SharedData({
       utd: utd.UniformDataType.HYPERLINK,
       content: `App Linking链接?index=${this.shareIndex}`, // 须替换为真实的App Linking链接，拼接自定义参数。
       thumbnailUri: fileUri.getUriFromPath(filePath),
       title: '隔空传送分享卡片标题',
       description: '隔空传送分享卡片描述'
     });
     sharableTarget.share(shareData);
     this.shareIndex++;
   };
   ```
2. 进入页面时在[onPageShow()](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)中使用[harmonyShare.on('gesturesShare')](../harmonyos-references/share-harmony-share.md#ongesturesshare)方法注册隔空传送监听事件，退出页面或者进入后台时在[onPageHide()](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)中使用[harmonyShare.off('gesturesShare')](../harmonyos-references/share-harmony-share.md#offgesturesshare)方法取消隔空传送监听事件。

   ```ts
   onPageShow(): void {
     this.immersiveListening();
   }

   onPageHide(): void {
     this.immersiveDisablingListening();
   }

   private immersiveListening() {
     harmonyShare.on('gesturesShare', this.immersiveCallback);
   }

   private immersiveDisablingListening() {
     harmonyShare.off('gesturesShare', this.immersiveCallback);
   }
   ```

***完整代码:***

EntryAbility：

```ts
import { ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { url } from '@kit.ArkTS';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    let uri = want?.uri;
    if (uri) {
      let urlObject = url.URL.parseURL(uri);
      let index = urlObject.params.get('index') as string;
      AppStorage.setOrCreate('GesturesShare_shareIndex', 'Result:' + index);
      AppStorage.setOrCreate('GesturesShare_isShareLink', true);
      hilog.info(DOMAIN, 'testTag', 'EntryAbility onCreate invoked. uri: %{public}s', uri);
    }
  }

  onNewWant(want: Want): void {
    let uri = want?.uri;
    if (uri) {
      let urlObject = url.URL.parseURL(uri);
      let index = urlObject.params.get('index') as string;
      AppStorage.setOrCreate('GesturesShare_shareIndex', 'Result:' + index);
      AppStorage.setOrCreate('GesturesShare_isShareLink', true);
      hilog.info(DOMAIN, 'testTag', 'EntryAbility onCreate invoked. uri: %{public}s', uri);
    }
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

Index.ets:

```ts
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { fileUri, fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private shareIndex: number = 0;

  aboutToAppear(): void {
    try {
      let filePath = this.context.filesDir + '/gestures_immersive.png'; // 仅为示例 请替换正确的文件路径
      let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      let writeLen = fs.writeSync(file.fd,
        (this.context.resourceManager.getMediaContentSync($r('app.media.gestures_immersive').id) as Uint8Array).buffer);
      console.info('write data to file succeed and size is:' + writeLen);
      fs.closeSync(file);
    } catch (error) {
      console.error(`getMediaContentSync error. Code: ${error?.code}, message: ${error?.message}`);
    }
  }

  private immersiveCallback = (sharableTarget: harmonyShare.SharableTarget) => {
    let filePath = this.context.filesDir + '/gestures_immersive.png'; // 仅为示例 请替换正确的文件路径
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.HYPERLINK,
      content: `App Linking链接?index=${this.shareIndex}`, // 须替换为真实的App Linking链接，拼接自定义参数。
      thumbnailUri: fileUri.getUriFromPath(filePath),
      title: '隔空传送分享卡片标题',
      description: '隔空传送分享卡片描述'
    });
    sharableTarget.share(shareData);
    this.shareIndex++;
  };

  onPageShow(): void {
    this.immersiveListening();
  }

  onPageHide(): void {
    this.immersiveDisablingListening();
  }

  private immersiveListening() {
    harmonyShare.on('gesturesShare', this.immersiveCallback);
  }

  private immersiveDisablingListening() {
    harmonyShare.off('gesturesShare', this.immersiveCallback);
  }

  @StorageLink('GesturesShare_isShareLink') isShareLink: boolean = false;
  @StorageLink('GesturesShare_shareIndex') shareResult: string = '隔空传送分享AppLinking';

  build() {
    RelativeContainer() {
      Text(this.shareResult)
        .fontSize('35fp')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
