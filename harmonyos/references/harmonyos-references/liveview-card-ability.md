---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/liveview-card-ability
title: LiveViewCardExtensionAbility
breadcrumb: API参考 > 应用服务 > Live View Kit（实况窗服务） > ArkTS API > LiveViewCardExtensionAbility
category: harmonyos-references
scraped_at: 2026-09-02T15:02:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:74708c05169c293811480864f3783a66193952e3a523a849aaa3f9ea502231de
---

LiveViewCardExtensionAbility为实况窗卡片自定义扩展区的[ExtensionAbility](../harmonyos-guides/extensionability-overview.md)组件，适用于需要在扩展区展示自定义丰富内容的实时活动场景。开发者通过继承该类并实现应用的扩展组件，可以在实况窗扩展区呈现开发者自定义的内容。

**起始版本：** 26.0.0

## 约束限制

* LiveViewCardExtensionAbility为独立子进程，不能跨进程拉起其他Ability。
* 不允许访问网络。
* 该ExtensionAbility每次的运行时长限制在80毫秒内，超时会导致实况卡片自定义扩展区无法正常展示，因此禁止用于复杂耗时的处理。
* 为保障系统安全性和稳定性，防止LiveViewCardExtensionAbility滥用系统资源，系统对其能力进行管控，不支持部分模块的引用，详情请参考[附录](liveview-card-ability.md#附录)。

## 导入模块

```typescript
import { LiveViewCardExtensionAbility } from '@kit.LiveViewKit';
```

**设备行为差异：** 该模块在Phone、Tablet中可正常调用，在其他设备类型中无效果。

## LiveViewCardExtensionAbility

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 26.0.0

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [LiveViewCardExtensionContext](liveview-card-context.md) | 否 | 否 | LiveViewCardExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onRender

onRender(param: Record<string, string>): CardInfo

开发者继承LiveViewCardExtensionAbility并实现自身的组件，当组件实例被系统加载时，系统会触发该回调。开发者可以在onRender中实现实况窗卡片扩展区的业务逻辑和界面组件绘制，并返回要加载的[CardInfo](liveview-card-ability.md#cardinfo)给系统，由系统渲染页面。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | Record<string, string> | 是 | 开发者创建实况窗卡片自定义扩展区时传入的参数[CustomLayout.abilityParameters](liveview-liveviewmanager.md#customlayout)  默认会携带以下key值（由系统赋值，开发者手动修改也不会生效）：  'ohos.extra.param.key.colorMode'：实况卡片深浅色模式（dark：深色模式；light：浅色模式）  'ohos.extra.param.key.fontColor'：实况卡片字体颜色（"#ARGB"16进制格式，长度为9）  'ohos.extra.param.key.contentWidth'：实况窗卡片的宽度，单位为vp（自定义扩展区左右边界距离实况窗卡片边界各为12vp，即自定义扩展区宽度=实况窗卡片宽度-12\*2）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CardInfo](liveview-card-ability.md#cardinfo) | 卡片渲染信息对象。 |

## CardInfo

onRender函数接口返回的卡片渲染信息对象。

**模型约束：** 此属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.LiveView.LiveViewService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pagePath | string | 否 | 否 | 待加载到系统中的扩展区域页面的路径，系统将渲染该页面。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 否 | 是 | 页面级UI状态存储单元，用于传递pagePath内容的状态属性。 |

## 示例

```typescript
import { LiveViewCardExtensionAbility } from '@kit.LiveViewKit';
import { CardInfo } from '@hms.core.liveview.LiveViewCardExtensionAbility';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class LiveViewCardExtAbility extends LiveViewCardExtensionAbility {
  onRender(param: Record<string, string>): CardInfo {
    hilog.info(0x0000, 'LiveViewCardTag', 'LiveViewCardExtAbility onRender begin.');

    // 将param的参数构造到LocalStorage传递给页面使用。
    const storage = new LocalStorage(param);

    // 加载实况窗卡片自定义扩展区页面
    return {
      pagePath: 'pages/LiveViewCardPage',
      storage: storage
    }
  }
}
```

```typescript
@Entry({ useSharedStorage: true })
@Component
struct LiveViewCardPage {
  private storage: LocalStorage | undefined = this.getUIContext().getSharedLocalStorage();
  // 获取从AbilityParameters中传入的参数
  private words: string | undefined = this.storage?.get('words');

  // 解析获取系统实况窗卡片自定义扩展区的宽度、深浅色模式、字体颜色
  private contentWidth: string | undefined = this.storage?.get('ohos.extra.param.key.contentWidth');
  private colorMode: string | undefined = this.storage?.get('ohos.extra.param.key.colorMode');
  private fontColor: string | undefined = this.storage?.get('ohos.extra.param.key.fontColor');

  getFontColor(): string {
    // 开发者可以根据深浅色模式自定义字体颜色。也可以使用默认的字体颜色。
    let color = this.fontColor as string; // 默认的字体颜色。使用默认的字体颜色时，需要删掉下方根据colorMode进行判断的逻辑。
    // 根据colorMode的值，自定义字体颜色。
    if (this.colorMode == 'dark') {
      // 深色模式场景下，开发者根据业务自行定义字体颜色，以下示例中字体颜色为红色。
      color = '#FFFF3300';
    } else if (this.colorMode == 'light') {
      // 浅色模式场景下，开发者根据业务自行定义字体颜色，以下示例中字体颜色为绿色。
      color = '#FF33CC66';
    }
    return color;
  }

  build() {
    Column() {
      Scroll() {
        Column() {
          Text(this.words)
            .fontColor(this.getFontColor())
        }
        .width(this.contentWidth)
      }
    }
  }
}
```

## 附录

LiveViewCardExtensionAbility不允许调用的API名单如下。

| Kit名称 | 模块名称 |
| --- | --- |
| Ability Kit | [@ohos.ability.featureAbility (FeatureAbility模块)](js-apis-ability-featureability.md)  [@ohos.ability.particleAbility (ParticleAbility模块)](js-apis-ability-particleability.md)  [@ohos.bundle.launcherBundleManager (launcherBundleManager模块)](js-apis-launcherbundlemanager.md)  [@ohos.continuation.continuationManager (流转/协同管理)](js-apis-continuation-continuationmanager.md) |
| AppGallery Kit | [privacyManager（隐私管理服务）](store-privacymanager.md) |
| ArkData | [@ohos.data.distributedData (分布式数据管理)](js-apis-distributed-data.md)  [@ohos.data.distributedDataObject (分布式数据对象)](js-apis-data-distributedobject.md)  [@ohos.data.distributedKVStore (分布式键值数据库)](js-apis-distributedkvstore.md) |
| ArkUI | [@ohos.window (窗口)](arkts-apis-window.md) |
| Audio Kit | [@ohos.multimedia.audio (音频管理)](arkts-apis-audio.md) |
| AVSession Kit | [@ohos.multimedia.avsession (媒体会话管理)](arkts-apis-avsession.md)  [@ohos.multimedia.avCastPicker (投播组件)](ohos-multimedia-avcastpicker.md) |
| Background Tasks Kit | [@ohos.backgroundTaskManager (后台任务管理)](js-apis-backgroundtaskmanager.md)  [@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](js-apis-resourceschedule-backgroundtaskmanager.md)  [@ohos.reminderAgent (后台代理提醒)](js-apis-reminderagent.md)  [@ohos.reminderAgentManager (后台代理提醒)](js-apis-reminderagentmanager.md) |
| Basic Services Kit | [@ohos.account.appAccount (应用账号管理)](js-apis-appaccount.md)  [@ohos.account.distributedAccount (分布式账号管理)](js-apis-distributed-account.md)  [@ohos.account.osAccount (系统账号管理)](js-apis-osaccount.md)  [@ohos.request (上传下载)](js-apis-request.md)  [@ohos.wallpaper (壁纸)](js-apis-wallpaper.md)  [@ohos.pasteboard (剪贴板)](js-apis-pasteboard.md) |
| Calendar Kit | [@ohos.calendarManager (日程管理能力)](js-apis-calendarmanager.md) |
| Call Service Kit | [voipCall (应用内通话管理)](call-voipcall.md) |
| Camera Kit | [@ohos.multimedia.camera (相机管理)](arkts-apis-camera.md)  [@ohos.multimedia.cameraPicker (相机选择器)](js-apis-camerapicker.md) |
| Connectivity Kit | [@ohos.connectedTag (有源标签)](js-apis-connectedtag.md)  [@ohos.nfc.cardEmulation (标准NFC-cardEmulation)](js-apis-cardemulation.md)  [@ohos.nfc.controller (标准NFC)](js-apis-nfccontroller.md)  [@ohos.nfc.tag (标准NFC-Tag)](js-apis-nfctag.md)  [nfctech (标准NFC-Tag Nfc 技术)](js-apis-nfctech.md)  [tagSession (标准NFC-Tag TagSession)](js-apis-tagsession.md) |
| Contacts Kit | [@ohos.contact (联系人)](js-apis-contact.md) |
| Core File Kit | [@ohos.file.picker (选择器)](js-apis-file-picker.md) |
| Form Kit | [@ohos.app.form.formInfo (formInfo)](js-apis-app-form-forminfo.md#forminfo)  [@ohos.application.formError (formError)](js-apis-application-formerror.md) |
| Map Kit | [sceneMap（场景化控件）](map-scenemap.md) |
| MDM Kit | [@ohos.enterprise.adminManager (admin权限管理)](js-apis-enterprise-adminmanager.md)  [@ohos.enterprise.deviceInfo（设备信息管理）](js-apis-enterprise-deviceinfo.md) |
| Media Kit | [@ohos.multimedia.media (媒体服务)](arkts-apis-media.md) |
| Media Library Kit | [@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](js-apis-sendablephotoaccesshelper.md)  [@ohos.file.AlbumPickerComponent (Album Picker组件)](ohos-file-albumpickercomponent.md)  [@ohos.file.PhotoPickerComponent (PhotoPicker组件)](ohos-file-photopickercomponent.md)  [@ohos.file.RecentPhotoComponent (最近图片组件)](ohos-file-recentphotocomponent.md)  [@ohos.multimedia.movingphotoview (动态照片)](ohos-multimedia-movingphotoview.md)  [@ohos.file.photoAccessHelper (相册管理模块)](js-apis-photoaccesshelper.md) |
| Notification Kit | [@ohos.notification (Notification模块)](js-apis-notification.md)  [@ohos.notificationManager (NotificationManager模块)](js-apis-notificationmanager.md) |
| Payment Kit | [paymentService (鸿蒙支付服务)](payment-paymentservice.md) |
| Performance Analysis Kit | [@ohos.hidebug (Debug调试)](js-apis-hidebug.md) |
| Scan Kit | [customScan (自定义界面扫码)](scan-customscan-api.md)  [detectBarcode (图像识码)](scan-imagedecode.md)  [generateBarcode (码图生成)](scan-generatebarcode.md)  [scanBarcode (默认界面扫码)](scan-scanbarcode-api.md)  [scanCore (扫码公共信息)](scan-scancore.md) |
| Sensor Service Kit | [@ohos.vibrator (振动)](js-apis-vibrator.md) |
| Service Collaboration Kit | [devicePicker (设备选择控制器)](servicecollaboration-devicepicker.md)  [CollaborationDevicePicker (流转控件)](servicecollaboration-collaborationdevicepicker.md) |
| Share Kit | [systemShare（分享）](share-system-share.md)  [harmonyShare（华为分享）](share-harmony-share.md) |
| Telephony Kit | [@ohos.telephony.call (拨打电话)](js-apis-call.md)  [@ohos.telephony.data (蜂窝数据)](js-apis-telephony-data.md)  [@ohos.telephony.observer (observer)](js-apis-observer.md)  [@ohos.telephony.radio (网络搜索)](js-apis-radio.md)  [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md)  [@ohos.telephony.sms (短信服务)](js-apis-sms.md) |
| User Authentication Kit | [@ohos.userIAM.userAuth (用户认证)](js-apis-useriam-userauth.md) |
| Vision Kit | [CardRecognition（卡证识别控件）](vision-card-recognition.md)  [DocumentScanner（文档扫描控件）](vision-document-scanner.md) |
