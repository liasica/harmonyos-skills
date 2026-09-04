---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-music-service-form
title: 音乐服务卡片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片最佳实践 > 音乐服务卡片
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:14+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:1a298b4471749ccaf47d6c5fdc912a65490312f77a702dfe2d6b908b5e8cddb2
---

## 概述

服务卡片，简称“卡片”，是系统一种呈现信息和交互操作的载体，在应用或元服务中提取关键信息和核心操作，以卡片的形式展示在桌面上，用户通过与服务卡片交互即可实现服务直达，减少交互层级，提升用户体验。

典型的服务卡片使用场景有音乐服务卡片。音乐服务卡片将音乐应用的重要信息与核心功能操作前置到卡片上，以卡片的形式呈现给用户，如音乐播控、歌单推荐、心动歌词、动态歌词等。用户可通过音乐服务卡片快速访问音乐应用的核心功能，无需打开完整的应用界面。

**图 1** 音乐服务卡片场景效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/u4rBg9iNSZ616ZIx7Q3jiw/zh-cn_image_0000002712244416.png)

本文将以音乐服务卡片场景为例，分别介绍音乐播控、歌单推荐、心动歌词、动态歌词四种服务卡片的实现，包括卡片设计和功能开发，以及开发中常见的一些问题。通过本案例，开发者可以更加深入的了解服务卡片与应用的交互和卡片的数据更新机制，快速高效的进行精美的服务卡片开发。

## 场景介绍

### 音乐播控

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/hqU4KuVkQ5uFF7DxR9cS9g/zh-cn_image_0000002742003369.png)

场景定义：

* 体验：用户无需打开应用，直接在卡片上就能控制基本的音乐播放功能操作，节省操作步骤，提升用户体验。
* 功能：用户可以通过服务卡片直接实现音乐播放，包括播放、暂停、上一首、下一首、收藏等操作。

### 动态歌词

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/fk5N46-BRWSEmFfvOdLYhA/zh-cn_image_0000002712404382.jpg)

场景定义：

* 体验：用户不仅可以播放音乐，还可以看到与当前播放进度实时匹配的歌词内容，增强用户体验。
* 功能：用户可以通过服务卡片直接实现音乐播放并实时显示歌词，包括播放、暂停、上一首、下一首、根据播放进度显示歌词等操作。

### 歌单推荐

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/zZjC1W-ARZOgmhUUu6hw5g/zh-cn_image_0000002742123331.png)

场景定义：

* 体验：用户在播放音乐时，可以直接在卡片上看到推荐的歌曲列表，点击即可切换和收藏，增强用户对音乐选择的便捷性和个性化体验。
* 功能：服务卡片可以根据用户的音乐偏好和当前播放内容，实时推荐相关歌曲或歌单。点击“我的收藏”跳转到应用收藏列表；点击“热门歌单”，跳转到歌单列表。

### 心动歌词

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/eJDFSa8SRO63doDxxB4SXw/zh-cn_image_0000002712244418.png)

场景定义：

* 体验：以用户个性化互动为核心，通过歌词内容增强用户情感共鸣和音乐体验，通过技术创新深度链接用户情感，提供更加富有个性化的音乐体验。
* 功能：根据用户的听歌历史和偏好，推荐与其喜好相符的歌词卡片。

### 场景互动卡片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Vc5x_hLtRhCk5zK_ZMp_lQ/zh-cn_image_0000002742003371.png)

场景定义：

* 体验：客户可以通过点击卡片，卡片展示溢出屏幕的动效，提供技术创新提供富有趣味的用户体验。
* 功能：提供富有趣味的用户互动。

## 卡片设计

在设计方面，服务卡片需要遵循突出服务内容、明确划分有限的操作空间、展示必要的信息和图片以及轻量交互[体验原则](../design-guides/system-features-service-widget-0000002087671904.md#section111mcpsimp)，关于卡片内容设计遵循[卡片内容设计](../design-guides/system-features-service-widget-0000002087671904.md#section248mcpsimp)规范，例如卡片沉浸式体验设计，包含图片和用色丰富的沉浸式卡片，背景色提取内容图中的色彩。

**图 2** 音乐服务卡片沉浸效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/aWxihbmURXOB7lv-YtwACw/zh-cn_image_0000002712404384.png)

音乐播控、歌单推荐、心动歌词和动态歌词卡片设计效果如下所示：

**表 1** 音乐卡片设计效果

| 卡片名称 | 卡片规格 | 功能简介 | 卡片效果1 | 卡片效果2 | 桌面效果 |
| --- | --- | --- | --- | --- | --- |
| 音乐播控 | [2x2] [2x4] | 1. 音乐播放控制，点击上一曲/下一曲，音乐封面会跟随歌曲切换。  2. 音乐收藏/取消收藏功能 |  |  |  |
| 歌单推荐 | [1x2] [2x4] | 1. 点击我的收藏跳转到应用收藏列表。  2. 点击热门歌单，跳转到歌单列表。 |  |  |  |
| 心动歌词 | [2x4] [4x4] | 1. 展示心动歌词，以及歌曲信息。  2. 点击卡片拉起对应歌曲播放页面。 |  |  |  |
| 动态歌词 | [2x4] | 1. 音乐播放控制，点击上一曲/下一曲，音乐封面会跟随歌曲切换。  2. 当前音乐歌词会跟随播放进度，显示对应歌词。 |  | 暂无 |  |

## 实现方案

### 整体方案

音乐应用作为[卡片提供方](formkit-overview.md#服务卡片架构)，提供音乐服务卡片的内容显示、控件布局和卡片交互处理逻辑。桌面作为[卡片使用方](formkit-overview.md#服务卡片架构)，即卡片的宿主应用，控制卡片在桌面中展示的位置和内容。卡片框架管理卡片生命周期和刷新机制，负责卡片页面的渲染。关于卡片提供方、使用方和卡片框架的详细内容可参考[ArkTS卡片实现原理](arkts-form-overview.md#实现原理)。

**图 3** 音乐服务卡片运行机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/5O-vA6gCRWyUyMXOzhYKdg/zh-cn_image_0000002712404390.png)

音乐应用包含[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)（主进程）和[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)（卡片进程）两个进程。其中，主进程包含音乐播控、收藏、热门歌单、以及歌词处理等功能模块；卡片进程是卡片业务逻辑模块，提供卡片创建、刷新、销毁等生命周期回调。如下图所示：

**图 4** 音乐应用进程结构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/DbVOCvWFRhekyRzfg902HQ/zh-cn_image_0000002742123339.png)

开发者可以根据FormExtensionAbility生命周期回调，在对应回调方法中处理卡片数据持久化、卡片数据更新等操作，FormExtensionAbility生命周期回调时机和功能实现说明如下表所示：

**表 2** 卡片生命周期说明

| 生命周期 | 回调时机 |
| --- | --- |
| [onAddForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonaddform) | 长按 APP 图标/卡片后，点击“服务卡片”拉起卡片视图后 |
| [onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform) | 定时更新、定点更新、卡片使用方主动请求更新时执行回调 |
| [onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent) | 用户触发了卡片上的postCardAction或FormLink组件中的message事件时执行回调 |
| [onRemoveForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonremoveform) | 长按卡片选择“移除”后 |

### 互动卡片

场景类型互动卡片在定位上是对普通卡片能力的增强，因此开发者需首先完成普通卡片的业务开发。之后在特定业务环节通过接口请求，触发互动卡片特有的动态效果。开发者可参考[互动卡片开发](arkts-ui-liveform.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ALEqnkNfR1KQe8iB8ap1KA/zh-cn_image_0000002712244426.png)

### 关键技术

在服务卡片开发中，会使用多种关键技术共同来实现不同类型的卡片，比如卡片规格的选择、卡片的沉浸式效果、卡片的更新以及数据持久化等。具体关键技术介绍如下：

1. **卡片的选择**

   * 动态卡片支持通用事件能力和自定义动效能力，适用于有复杂业务逻辑和交互的场景，功能丰富但内存开销较大。
   * 静态卡片支持UI组件和布局能力，不支持通用事件和自定义动效能力，卡片内容以静态图显示，可以通过[FormLink](../harmonyos-references/ts-container-formlink.md)组件跳转到指定的UIAbility，适用于展示类卡片（UI相对固定），功能简单但可以有效控制内存开销。

   音乐播控卡片和动态歌词卡片具有播放/暂停、上一曲/下一曲、收藏等功能，需较强的播控逻辑和交互处理，更适合选择动态卡片；歌单推荐和心动歌词仅需要页面跳转功能，业务逻辑和交互都比较简单，选择静态卡片更合适。
2. **沉浸式卡片**

   沉浸式卡片设计能给用户带来更好的视觉体验，开发者可以使用[@ohos.effectKit](../harmonyos-references/js-apis-effectkit.md)模块的ColorPicker的[getMainColor()](../harmonyos-references/js-apis-effectkit.md#getmaincolor)方法获取歌曲封面图像主色，作为卡片的背景色，使卡片和歌曲封面融为一体达到卡片沉浸效果。此外，在一些场景下，还可以给卡片添加背景图片，使用Image组件的blur属性或者@ohos.effectKit模块的[blur()](../harmonyos-references/js-apis-effectkit.md#blur)方法给图片做模糊化处理，来达到卡片沉浸效果。
3. **卡片更新与数据交互**

   针对音乐服务卡片这种多类型多规格的卡片场景，推荐使用关系型数据库[relationalStore](../harmonyos-references/js-apis-data-relationalstore.md)进行卡片数据持久化存储。

   应用主进程通过FormProvider的[updateForm()](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)方法实现卡片的主动刷新，例如更新歌曲信息、歌词信息等；在FormExtensionAbility的onUpdateForm()生命周期回调方法中实现卡片被动刷新逻辑，例如定时和定点刷新。

   关于服务卡片的数据交互和更新机制，具体可以参考：[卡片更新与数据交互](../best-practices/bpta-card-update-and-data-interaction.md)。

### 卡片实现方案

**音乐播控卡片**

* 音乐播控卡片具有播放/暂停、上一曲/下一曲、收藏等功能，需较强的播控逻辑和交互处理，选择动态卡片实现。
* 音乐播控卡片和应用之间存在较多的交互，选择使用动态卡片来实现。动态卡片支持通用事件能力和自定义动效能力，适用于有复杂业务逻辑和交互的场景。动态卡片的创建可以参考：[创建ArkTS卡片](arkts-ui-widget-creation.md)**。**
* 卡片与应用主进程之间通过call事件进行交互，比如播放、暂停、收藏等。call事件的发送和订阅可以参考：[通过router或call事件刷新卡片内容](arkts-ui-widget-event-overview.md)。
* 本示例音乐播放功能使用的是AVPlayer，具体实现可以参考[使用AVPlayer播放音频(ArkTS)](using-avplayer-for-playback.md)。为保证音乐能在后台播放或熄屏播放，需要接入[AVSession（媒体会话）](avsession-access-scene.md)和[申请长时任务](continuous-task.md)，避免播放被系统强制中断。
* 场景动效类型互动卡片采用的是LiveFormExtensionAbility完成其页面的布局和渲染。

**动态歌词卡片**

* 该卡片支持切换歌曲、播控、跳转功能，可参考前面[音乐播控卡片](arkts-ui-music-service-form.md#卡片实现方案)相关介绍。
* 动态歌词可实时显示与当前播放进度匹配的歌词内容。切换歌曲时，除更新歌曲基本信息外，歌词部分会同步更新并从头开始跟随播放进度显示，需要开发者在实际开发中获取相应歌曲的歌词信息。歌词在播放期间以及切换不同歌曲的时候，需要通过动画实现歌词的平滑[过渡效果](../harmonyos-references/ts-transition-animation-component.md)。在卡片初始化的时候，需要预处理好歌词数组，在音频进度回调中，需根据当前时间匹配对应歌词，并更新卡片。
* 应用内添加卡片到桌面功能。在应用内长按指定元素，将弹出包含"添加至桌面"选项的菜单，点击后弹出应用支持的卡片。长按添加至桌面菜单可以参考：[FormMenu](../harmonyos-references/ohos-arkui-advanced-formmenu.md)组件。

**歌单推荐卡片**

* 歌单推荐卡片没有复杂的业务逻辑和数据交互，选择使用静态卡片来实现，歌单推荐的交互动作主要是点击卡片对应组件之后，拉起应用主进程进行页面跳转。
* 页面跳转通过[FormLink](../harmonyos-references/ts-container-formlink.md)组件router类型事件来实现。
* 卡片创建的时候会加载网络图片，网络图片的刷新可以参考：[刷新本地图片和网络图片](arkts-ui-widget-image-update.md)。

**心动歌词卡片**

* 心动歌词卡片和应用主进程之间交互逻辑比较简单，仅有点击卡片跳转到应用播放页面的交互，所以选择静态卡片实现，通过FormLink组件实现点击卡片跳转。
* 心动歌词卡片内容主要是通过被动刷新的方式进行卡片数据刷新，在FormExtensionAbility的onUpdateForm()回调方法中，对卡片数据进行刷新，在卡片配置文件form\_config中配置updateDuration参数实现定时刷新。具体实现可以参考：[卡片定时刷新和定点刷新](arkts-ui-widget-passive-refresh.md)。

## 场景实现

### 音乐播控卡片

**实现步骤**

音乐播控卡片的主要实现步骤如下：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/l23WzpDtTtC3-upjkEUpwA/zh-cn_image_0000002742003379.png)

其中“实现音乐播控功能”需要通过卡片、数据库、媒体播放等多个模块之间的数据交互来实现，音乐播控功能实现时序图如下：

**图 5** 卡片音乐播控时序图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/sbxbuYPmSvKDteSm1vrJEw/zh-cn_image_0000002712404392.png)

音乐播控卡片的详细开发流程如下：

1. **开发卡片UI布局**

   **图 6** 音乐播控卡片效果图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zHHnAS3TQg2Zpex0z9VWXA/zh-cn_image_0000002742123341.png)

   分别创建2x2和2x4两个规格的动态卡片，动态卡片的创建可以参考[创建ArkTS卡片](arkts-ui-widget-creation.md)。对于比较复杂的布局，优先考虑使用相对布局 [RelativeContainer](arkts-layout-development-relative-layout.md)来减少性能开销。由于2x4卡片包含了2x2卡片的功能，下面将以2x4卡片为例介绍音乐播控卡片的实现。

   在卡片布局文件中定义卡片所需要的变量信息，使用[@LocalStorageProp](arkts-localstorage.md#localstorageprop)装饰器修饰，用于接收应用侧传递过来的数据，其中isPlay与isCollected分别表示歌曲的播放和收藏状态，根据状态的不同展示不同的图标，示例代码如下：

   ```ts
   // src/main/ets/widget/pages/PlayControlCard2x4.ets
   let storageUpdateCall = new LocalStorage();

   @Entry(storageUpdateCall)
   @Component
   struct PlayControlCard2x4 {
     @LocalStorageProp('formId') formId: string = '';
     @LocalStorageProp('isNeedRequestUpdate') @Watch('requestData') isNeedRequestUpdate: boolean = false;
     @LocalStorageProp('isPlay') isPlay: boolean = false;
     @LocalStorageProp('title') title: string = 'SongName';
     @LocalStorageProp('isCollected') isCollected: boolean = false;
     @LocalStorageProp('musicCover') musicCover: Resource = $r('app.media.ic_dream');
     @LocalStorageProp('singer') singer: string = 'Singer';
     @LocalStorageProp('songId') songId: string = '';
     @LocalStorageProp('imageColor') imageColor: string = 'rgba(76, 72, 68, 1)';
     @LocalStorageProp('imageColorHex') imageColorHex: string = '18191d';

     requestData() {
       ActionUtils.updateControlCardAction(this, this.formId);
     }

     build() {
       RelativeContainer() {
         Image(this.musicCover)
           // ...
         SymbolGlyph(this.isCollected ? $r('sys.symbol.heart_fill') : $r('sys.symbol.heart'))
           // ...
         Row() {
           SymbolGlyph($r('sys.symbol.backward_end_fill'))
             // ...
           SymbolGlyph(this.isPlay ? $r('sys.symbol.pause') : $r('sys.symbol.play_fill'))
             // ...
           SymbolGlyph($r('sys.symbol.forward_end_fill'))
             // ...
         }
         // ...
       }
       // ...
     }
   }
   ```
2. **卡片数据初始化**

   用户长按桌面应用图标，桌面弹出卡片添加弹窗时，需要对卡片数据进行初始化，能让用户直观的理解到卡片所提供的服务内容、功能和样式。同时，音乐播控卡片的预览数据和应用当前播放歌曲应该保持一致。

   **图 7** 音乐播控卡片预览效果

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/eUx38ysiTRWn1WGYmVZBgA/zh-cn_image_0000002712244428.png)

   在音乐应用中，EntryFormAbility继承了FormExtensionAbility类并实现了其生命周期回调方法。当预览卡片时，会触发EntryFormAbility的onAddForm()回调方法，在此方法中可以获取卡片名称、卡片ID等信息。开发者可以根据卡片名称判断是否为音乐播控卡片，如果是，则调用FormUtils.updateMusicControlCard()方法更新卡片数据。FormUtils是卡片管理工具类，封装了卡片添加、删除、更新等相关功能。示例代码如下：

   ```ts
   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       // ...
       if (want.parameters) {
         let formId = want.parameters['ohos.extra.param.key.form_identity'] as string;
         let formName = want.parameters['ohos.extra.param.key.form_name'] as string;
         // ...
         this.trigger3DLiveRequest(formId);

         if (formName.includes('PlayControlCard')) {
           FormUtils.updateMusicControlCard(formId, true);
         }
         // ...
       }
       return formBindingData.createFormBindingData('');
     }

     // ...
   }
   ```

   由于在卡片进程FormExtensionAbility中无法直接获取歌曲播放状态，需要应用主进程来主动更新卡片播放状态。可以通过FormExtensionAbility给卡片传递一个isNeedRequestUpdate标识，当卡片收到该标识后，给应用主进程发送call事件主动更新卡片信息。

   ```ts
   // src/main/ets/utils/FormUtils.ets
   class FormUtils {
     // ...
     public updateMusicControlCard(formId: string, needUpdate: boolean) {
       Logger.info(TAG, `updateMusicControlCard formId:${formId},needUpdate:${needUpdate}`);
       let updateData: UpdateData = {
         isNeedRequestUpdate: needUpdate,
         formId: formId,
       };
       this.updateForm(formId, updateData);
     }

     // ...

     private updateForm(formId: string, updateData: object) {
       Logger.info(TAG, `updateForm  updateData: ${JSON.stringify(updateData)}}`);
       let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(updateData);
       formProvider
         .updateForm(formId, formMsg)
         .then(() => {
           Logger.info(TAG, `updateForm success formId:  ${formId}}`);
         })
         .catch((error: BusinessError) => {
           Logger.error(TAG, `updateForm failed: ${JSON.stringify(error)}`);
         });
     }

   }
   ```

   音乐播控卡片订阅到isNeedRequestUpdate变化后，发送call事件请求卡片更新。

   ```ts
   // src/main/ets/widget/pages/PlayControlCard2x4.ets
   let storageUpdateCall = new LocalStorage();

   @Entry(storageUpdateCall)
   @Component
   struct PlayControlCard2x4 {
     @LocalStorageProp('formId') formId: string = '';
     @LocalStorageProp('isNeedRequestUpdate') @Watch('requestData') isNeedRequestUpdate: boolean = false;
     // ...
     requestData() {
       ActionUtils.updateControlCardAction(this, this.formId);
     }

     // ...
   }
   ```

   ```ts
   // src/main/ets/widget/model/ActionUtils.ets
   public updateControlCardAction(component: Object, formId: string) {
     postCardAction(component, {
       action: FormCarAction.CALL,
       abilityName: ENTRY_ABILITY,
       params: {
         method: CallMethod.REQUEST_UPDATE_CARD,
         formId: formId,
       },
     });
   }
   ```

   应用主进程EntryAbility收到call事件后，根据卡片ID对卡片数据进行更新。

   ```ts
   // src/main/ets/entryability/EntryAbility.ets
   export default class EntryAbility extends UIAbility {
     // ...
     requestUpdatePlayCard = (data: rpc.MessageSequence) => {
       try {
         Logger.info(TAG, 'requestUpdatePlayCard');
         let params: Record<string, string> = JSON.parse(data.readString());
         let formId = params.formId;
         if (formId) {
           FormUtils.updateMusicControlSingle(context, formId);
         }
       } catch (err) {
         let error = err as BusinessError;
         Logger.error(TAG, `requestUpdatePlayCard err, code: ${error.code}, mesage: ${error.message}`);
       }
       return null;
     };
     // ...
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
       // ...
         this.callee.on('requestUpdatePlayCard', this.requestUpdatePlayCard);
         // ...
   }
   ```

   在卡片更新前需要获取卡片更新的相关数据，获取音乐播放状态isPlay、播放的歌曲信息songItem以及从数据库中获取歌曲的收藏状态，然后调用FormUtils的updateForm()方法更新卡片。

   ```ts
   // src/main/ets/utils/FormUtils.ets
   class FormUtils {
     // ...

     // src/main/ets/utils/FormUtils.ets
     public async updateMusicControlSingle(context: Context, formId: string) {
       let isPlay = AppStorage.get('isPlay') as boolean;
       let songItem: SongItem = AppStorage.get('currentSong') as SongItem;
       // ...
       let collectedSongList: Array<SongItem> = await SongRdbHelper.getInstance(context).queryCollectedSongs();
       // ...
       let formData = new FormControlData();
       formData.isPlay = isPlay;
       formData.formId = formId;
       formData.singer = songItem.singer;
       formData.title = songItem.title;
       formData.songId = songItem.id;
       formData.musicCover = songItem.label;
       formData.isCollected = collectedSongList.findIndex((item) => item.id === songItem.id) >= 0;
       // ...
       this.updateForm(formData.formId, formData);
     }

     // ...
   }
   ```
3. **卡片信息持久化**

   音乐播控卡片有2x2和2x4两种规格，每种规格都可创建多个卡片。为确保切换歌曲时所有相关卡片的信息能够同步更新，需根据每个卡片的唯一ID和类型进行统一管理。因此，应将这些信息持久化存储，以便在需要时查询并准确刷新卡片内容，保持数据一致性。

   当用户长按桌面应用图标以展示卡片列表时，会触发EntryFormAbility的生命周期方法onAddForm()。在此回调函数中，可以利用关系型数据库relationalStore保存卡片的相关信息，如卡片ID、名称等。而当卡片被移除时，则应在onRemoveForm()回调函数中同步删除数据库中的相应记录，示例代码如下：

   ```ts
   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want) {
       hilog.info(0x0000, TAG, 'onAddForm');
       if (want.parameters) {
         let formId = want.parameters['ohos.extra.param.key.form_identity'] as string;
         let formName = want.parameters['ohos.extra.param.key.form_name'] as string;
         let formDimension = want.parameters['ohos.extra.param.key.form_dimension'] as string;

         let formInfo = new FormInfo();
         formInfo.formId = formId;
         formInfo.formDimension = formDimension;
         formInfo.formName = formName;
         hilog.info(0x0000, TAG, `onAddForm formInfo: ${JSON.stringify(formInfo)}`);
         FormRdbHelper.getInstance(this.context).insertForm(formInfo);
         // ...
       }
       return formBindingData.createFormBindingData('');
     }

     // ...
     onRemoveForm(formId: string) {
       hilog.info(0x0000, TAG, 'onRemoveForm');
       // Called to notify the form provider that a specified form has been destroyed.
       FormRdbHelper.getInstance(this.context).deleteForm(formId);
     }

     // ...
   }
   ```
4. **实现卡片播控功能**

   为了确保卡片和应用的播放状态始终保持同步，无论是在音乐应用的播放页面还是在桌面卡片上点击播放、暂停、上一首或下一首按钮，都应即时更新卡片和应用的播放界面信息。

   1. 发送音乐播控相关的call事件。

      给“播放/暂停”等播控相关的组件绑定onClick事件，调用[postCardAction](../harmonyos-references/js-apis-postcardaction.md)接口触发call事件，向音乐应用发送音乐播控信息。postCardAction方法封装在ActionUtils里面，参数action为事件类型，值为FormCarAction.CALL（枚举值为“call”）；method为方法名，用于触发UIAbility中对应的方法；type为播控操作类型，例如PlayActionType.PLAY表示播放。

      ```ts
      // src/main/ets/widget/pages/PlayControlCard2x4.ets
      let storageUpdateCall = new LocalStorage();

      @Entry(storageUpdateCall)
      @Component
      struct PlayControlCard2x4 {
        @LocalStorageProp('formId') formId: string = '';
        // ...
        @LocalStorageProp('isPlay') isPlay: boolean = false;
        // ...
        build() {
          RelativeContainer() {
            // ...
            Row() {
              SymbolGlyph($r('sys.symbol.backward_end_fill'))
                .fontSize(24)
                .fontColor(['#E5FFFFFF'])
                .onClick(() => {
                  ActionUtils.playByAction(this, PlayActionType.PREVIOUS, this.formId);
                })
              SymbolGlyph(this.isPlay ? $r('sys.symbol.pause') : $r('sys.symbol.play_fill'))
                // ...
                .onClick(() => {
                  if (this.isPlay) {
                    ActionUtils.playByAction(this, PlayActionType.PAUSE, this.formId);
                  } else {
                    ActionUtils.playByAction(this, PlayActionType.PLAY, this.formId);
                  }
                })
              SymbolGlyph($r('sys.symbol.forward_end_fill'))
                // ...
                .onClick(() => {
                  ActionUtils.playByAction(this, PlayActionType.NEXT, this.formId);
                })
            }
            // ...

          }
          // ...
        }
      }
      ```

      ```ts
      // src/main/ets/widget/model/ActionUtils.ets
      public playByAction(component: Object, type: PlayActionType, formId: string) {
        postCardAction(component, {
          action: FormCarAction.CALL,
          abilityName: ENTRY_ABILITY,
          params: {
            method: CallMethod.PLAY_BY_ACTION,
            playActionType: type,
            formId: formId,
          },
        });
      }
      ```
   2. 订阅和处理卡片发送的call事件。

      在EntryAbility（即应用主进程的入口UIAbility）的onCreate方法中，使用callee.on()方法订阅卡片发送的call事件。当EntryAbility接收到call事件后，根据事件类型playActionType，调用MediaService中的playByAction()方法来控制音乐播放。MediaService封装了[AVPlayer](media-kit-intro.md#avplayer)的媒体播放功能，如歌曲资源加载、播放/暂停等，具体实现可以参考[音乐服务卡片](https://gitcode.com/harmonyos_samples/MusicCard)示例代码中的MediaService.ets源码。

      ```ts
      // src/main/ets/entryability/EntryAbility.ets
      export default class EntryAbility extends UIAbility {
        playByActionCall = (data: rpc.MessageSequence) => {
          try {
            let params: Record<string, string> = JSON.parse(data.readString());
            Logger.info(TAG, `playByActionCall playActionType:${params.playActionType}`);
            if (params.playActionType) {
              let playActionType: PlayActionType = params.playActionType as PlayActionType;
              if (isInitSuccess) {
                MediaService.getInstance().playByAction(playActionType);
              } else {
                this.initSongData().then(() => {
                  MediaService.getInstance().playByAction(playActionType);
                });
              }
            }
          } catch (err) {
            let error = err as BusinessError;
            Logger.error(TAG, `playByActionCall err, code: ${error.code}, mesage: ${error.message}`);
          }
          return null;
        };

        // ...
        onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
          // ...
          try {
            this.callee.on('playByAction', this.playByActionCall);
            // ...
          } catch (error) {
            Logger.error(TAG, `playByAction register failed with error ${JSON.stringify(error)}`);
          }
          // ...
        onDestroy() {
          try {
            Logger.info(TAG, 'Ability onDestroy');
            this.callee.off('playByAction');
            // ...
          } catch (err) {
            let error = err as BusinessError;
            Logger.error(TAG, `onDestroy err, code: ${error.code}, mesage: ${error.message}`);
          }
        }

        // ...
      }
      ```

      ```ts
      // src/main/ets/utils/MediaService.ets
      public playByAction(action: PlayActionType): void {
        switch (action) {
          case PlayActionType.PAUSE:
            this.pause();
            break;
          case PlayActionType.PLAY:
            this.isFirstLoadAsset = false;
            this.play();
            break;
          case PlayActionType.PREVIOUS:
            this.playPrevious();
            break;
          case PlayActionType.NEXT:
            this.playNext();
            break;
          default:
            break;
        }
      }
      ```
   3. 根据媒体播放状态更新卡片和应用播放界面信息。

      点击卡片的播放/暂停等按钮，拉起EntryAbility至后台播放/暂停歌曲时，卡片上的播放状态需要同步更新。

      在EntryAbility的onCreate方法中，调用MediaService的setOnPlayStateCall()方法监听播放状态（如播放/暂停、上一曲/下一曲）变化。在setOnPlayStateCall()回调函数中，将播放状态isPlay和歌曲信息保存到AppStorage，以同步刷新应用界面。然后调用FormUtils的updateMusicControlCards()方法更新卡片数据，示例代码如下：

      ```ts
      // src/main/ets/entryability/EntryAbility.ets
      export default class EntryAbility extends UIAbility {
        // ...
        onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
          // ...
          MediaService.getInstance().setOnPlayStateCall(async (data: SongChangedData) => {
            // ...
            AppStorage.setOrCreate('isPlay', data.isPlay);
            AppStorage.setOrCreate('selectIndex', data.selectIndex);
            AppStorage.setOrCreate('currentSong', data.songItem);
            PreferencesUtil.getInstance().putCurrentSong(context, data.songItem);
            FormUtils.updateMusicControlCards(this.context, data.songItem, data.isPlay);

            // ...
          });

          // ...
      }
      ```

      卡片的更新需要根据卡片的ID进行更新，通过调用formProvider.updateForm()方法来实现。所以在更新卡片之前，需先从数据库中获取所有待更新的卡片集合，随后遍历该集合，依据formId批量更新2x2和2x4两种规格的所有相关音乐播控卡片，确保它们的数据一致性。更新的内容包括播放状态（isPlay）、歌手名（singer）和歌曲封面（musicCover）等。

      ```ts
      // src/main/ets/utils/FormUtils.ets
      class FormUtils {
        // ...

        public async updateMusicControlCards(context: Context, songItem: SongItem, isPlay: boolean) {
          // ...
          let formList: Array<FormInfo> = await FormRdbHelper.getInstance(context).queryFormByName('PlayControlCard');
          let formData = new FormControlData();
          formData.isPlay = isPlay;
          formData.singer = songItem.singer;
          formData.title = songItem.title;
          formData.songId = songItem.id;
          formData.musicCover = songItem.label;
          formData.isCollected = isCollected;
          formData.imageColor = imageDealData.imageColor;
          formData.imageColorHex = imageDealData.imageColorHex;

          formList.forEach((formInfo) => {
            this.updateForm(formInfo.formId, formData);
          });
        }

        // ...

        private updateForm(formId: string, updateData: object) {
          Logger.info(TAG, `updateForm  updateData: ${JSON.stringify(updateData)}}`);
          let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(updateData);
          formProvider
            .updateForm(formId, formMsg)
            .then(() => {
              Logger.info(TAG, `updateForm success formId:  ${formId}}`);
            })
            .catch((error: BusinessError) => {
              Logger.error(TAG, `updateForm failed: ${JSON.stringify(error)}`);
            });
        }

      }
      ```

      **表 3** 音乐播控卡片更新效果图

      | 批量更新卡片 | 通过卡片切换歌曲，卡片和应用均更新数据 | 通过应用切换歌曲，卡片和应用均更新数据 |
      | --- | --- | --- |
      |  |  |  |
   4. 应用进程被销毁前更新播放状态。

      当应用进程被销毁的时候，如果此时音乐卡片处于播放状态（显示暂停图标），应用应该更新卡片为未播放的状态（显示播放图标），并将状态更新同步到卡片UI。应用主进程被销毁前会触发EntryAbility里面的onDestroy()生命周期回调方法，在此方法中执行卡片更新逻辑，更新卡片播放状态isPlay为false。示例代码如下：

      ```ts
      // src/main/ets/entryability/EntryAbility.ets
      export default class EntryAbility extends UIAbility {
        // ...
        onDestroy() {
          try {
            // ...
            let isPlay = AppStorage.get('isPlay') as boolean;
            // ...
            if (isPlay) {
              FormUtils.updateCardPlayStatus(this.context, false);
              // ...
            }
          } catch (err) {
            let error = err as BusinessError;
            Logger.error(TAG, `onDestroy err, code: ${error.code}, mesage: ${error.message}`);
          }
        }

        // ...
      }
      ```

      ```ts
      public async updateCardPlayStatus(context: Context, isPlay: boolean) {
        class CardUpdateData {
          isPlay: boolean = isPlay;
        }

        let data = new CardUpdateData();
        let formList: Array<FormInfo> = await FormRdbHelper.getInstance(context).queryFormByName('PlayControlCard');
        Logger.info(TAG, `updateCardPlayStatus formList length:  ${formList.length}`);
        formList.forEach((formInfo) => {
          this.updateForm(formInfo.formId, data);
        });
      }
      ```
5. **实现卡片收藏功能**

   收藏功能和音乐播控的实现方式相同，都是通过call事件拉起应用主进程至后台，应用主进程通过callee.on()监听到收藏的call事件后，进行收藏业务处理，然后更新卡片。

   1. 卡片发送收藏call事件给应用。

      首先在卡片侧给收藏图标添加onClick事件，绑定postAction事件，发送收藏操作call事件。变量isCollected表示收藏状态，用于接收应用更新的收藏状态数据。

      ```ts
      // src/main/ets/widget/pages/PlayControlCard2x4.ets
      let storageUpdateCall = new LocalStorage();

      @Entry(storageUpdateCall)
      @Component
      struct PlayControlCard2x4 {
        @LocalStorageProp('formId') formId: string = '';
        // ...
        @LocalStorageProp('isPlay') isPlay: boolean = false;
        // ...
        @LocalStorageProp('isCollected') isCollected: boolean = false;
        @LocalStorageProp('musicCover') musicCover: Resource = $r('app.media.ic_dream');
        @LocalStorageProp('singer') singer: string = 'Singer';
        @LocalStorageProp('songId') songId: string = '';
        // ...
        // ...
        build() {
          RelativeContainer() {
            Image(this.musicCover)
              // ...
            SymbolGlyph(this.isCollected ? $r('sys.symbol.heart_fill') : $r('sys.symbol.heart'))
              // ...
              .onClick(() => {
                if (this.isCollected) {
                  ActionUtils.collectAction(this, CollectAction.UNCOLLECTED, this.formId, this.songId);
                } else {
                  ActionUtils.collectAction(this, CollectAction.COLLECTED, this.formId, this.songId);
                }
              })
            // ...
            Row() {
              // ...
            }
            // ...

          }
          // ...
        }
      }
      ```

      ```ts
      // src/main/ets/widget/model/ActionUtils.ets
      collectAction(component: Object, type: string, formId: string, songId: string) {
        postCardAction(component, {
          action: FormCarAction.CALL,
          abilityName: ENTRY_ABILITY,
          params: {
            method: CallMethod.COLLECT_ACTION,
            collectActionType: type,
            formId: formId,
            songId: songId,
          },
        });
      }
      ```
   2. 订阅和处理卡片发送的收藏call事件。

      在EntryAbility的onCreate方法中订阅卡片发送的收藏call事件，获取call事件携带的参数collectActionType，collectActionType为CollectAction.COLLECTED的时候表示收藏操作，为CollectAction.UNCOLLECTED的时候，表示取消收藏。根据collectActionType的值更新数据库中的收藏状态数据，再更新卡片的收藏状态。

      ```ts
      // src/main/ets/entryability/EntryAbility.ets
      export default class EntryAbility extends UIAbility {
        // ...

        collectActionCall = (data: rpc.MessageSequence) => {
          try {
            let params: Record<string, string> = JSON.parse(data.readString());
            if (params.collectActionType) {
              let songRdbHelper = SongRdbHelper.getInstance(context);
              if (params.collectActionType === CollectAction.COLLECTED) {
                songRdbHelper.updateCollected(params.songId, CollectAction.COLLECTED);
                FormUtils.updateCardCollectStatus(context, true);
                context.eventHub.emit('collected', params.songId, CollectAction.COLLECTED);
              } else {
                songRdbHelper.updateCollected(params.songId, CollectAction.UNCOLLECTED);
                FormUtils.updateCardCollectStatus(context, false);
                context.eventHub.emit('collected', params.songId, CollectAction.UNCOLLECTED);
              }
            }
          } catch (err) {
            let error = err as BusinessError;
            Logger.error(TAG, `collectActionCall err, code: ${error.code}, mesage: ${error.message}`);
          }
          return null;
        };
        // ...
        onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
          // ...
          try {
            // ...
            this.callee.on('collectAction', this.collectActionCall);
            // ...
          } catch (error) {
            Logger.error(TAG, `playByAction register failed with error ${JSON.stringify(error)}`);
          }
          // ...
        onDestroy() {
          try {
            // ...
            this.callee.off('collectAction');
            // ...
          } catch (err) {
            let error = err as BusinessError;
            Logger.error(TAG, `onDestroy err, code: ${error.code}, mesage: ${error.message}`);
          }
        }

        // ...
      }
      ```
   3. 批量更新卡片。

      卡片的收藏状态更新，和播控状态更新逻辑相同，同样需要批量更新多个播控卡片，在更新前需要在数据库中查询所有桌面上的音乐播控卡片，然后遍历更新。

      ```ts
      // src/main/ets/utils/FormUtils.ets
      class FormUtils {
        // ...

        public async updateCardCollectStatus(context: Context, isCollected: boolean) {
          let updateData: UpdateData = {
            isCollected: isCollected,
          };
          let formList: Array<FormInfo> = await FormRdbHelper.getInstance(context).queryFormByName('PlayControlCard');
          formList.forEach((formInfo) => {
            this.updateForm(formInfo.formId, updateData);
          });
        }

        // ...
      }
      ```

      同理应用主进程进行收藏/取消收藏操作时，也需要更新卡片，使卡片和应用主进程收藏状态保持一致。给歌曲列表项的收藏图标，绑定onClick事件，调用FormUtils工具类的updateCardCollectStatus()方法更新卡片收藏状态。

      ```ts
      @Reusable
      @Component
      export struct SongListItem {
        // ...

        async collected() {
          let context = this.getUIContext().getHostContext()!
          let songRdbHelper = SongRdbHelper.getInstance(context);
          if (this.item.isCollected) {
            await songRdbHelper.updateCollected(this.item.id, '0');
            FormUtils.updateCardCollectStatus(context, false);
            this.item.isCollected = false;
            context.eventHub.emit('collected', this.item.id, '0');
          } else {
            await songRdbHelper.updateCollected(this.item.id, '1');
            FormUtils.updateCardCollectStatus(context, true);
            this.item.isCollected = true;
            context.eventHub.emit('collected', this.item.id, '1');
          }
        }

        build() {
          Row() {
            // ...
              Image(this.item.isCollected ? $r('app.media.ic_item_collected') :
              $r('app.media.ic_item_uncollected'))// ...
                .onClick(() => {
                  this.collected();
                })
            }
          }
          // ...
        }
      }
      ```
6. **实现沉浸式卡片效果**

   整个卡片的色调跟随歌曲封面图片来进行变化，这种沉浸式效果会给用户不断变化的视觉感受，防止了固定的UI色彩造成用户的审美疲劳。可以利用[effectKit](../harmonyos-references/js-apis-effectkit.md)图像效果的智能取色[ColorPicker](../harmonyos-references/js-apis-effectkit.md#colorpicker)取出歌曲封面图片的主颜色，以实现沉浸式UI效果。当歌曲切换的时候，可以先对歌曲封面图片进行取色，将歌曲封面图片的颜色imageColorHex更新给卡片。

   ```ts
   // src/main/ets/utils/FormUtils.ets
   class FormUtils {
     // ...

     public async updateMusicControlCards(context: Context, songItem: SongItem, isPlay: boolean) {
       let isCollected = await SongRdbHelper.getInstance(context).isCollected(songItem.id);
       let imageDealData = await ImageUtils.getImageDealData(context, songItem.label);
       let formList: Array<FormInfo> = await FormRdbHelper.getInstance(context).queryFormByName('PlayControlCard');
       let formData = new FormControlData();
       // ...
       formData.imageColorHex = imageDealData.imageColorHex;

       formList.forEach((formInfo) => {
         this.updateForm(formInfo.formId, formData);
       });
     }

     // ...
   }
   ```

   使用effectKit模块的colorPicker.getMainColorSync()方法，获取封面图片主要颜色，转化为十六进制格式数据。

   ```ts
   class ImageUtils {
     // ...
     public getImageDealData(context: Context, imgRes: Resource): Promise<ImageDealData> {
       return new Promise(async (resolve, reject) => {
         try {
           let value = context.resourceManager.getMediaContentSync(imgRes.id);
           let imageData = await this.getImageDealDataByArr(value.buffer as ArrayBuffer);
           resolve(imageData);
         } catch (err) {
           Logger.info(TAG, `getImageDealData err :${JSON.stringify(err)}`);
           reject(err);
         }
       });
     }

     // ...
     public getImageDealDataByArr(buffer: ArrayBuffer): Promise<ImageDealData> {
       return new Promise(async (resolve, reject) => {
         try {
           let pixelMap = image.createImageSource(buffer).createPixelMapSync();
           if (buffer.byteLength > 2048 * 1024) {
             pixelMap = await this.compressImage(pixelMap, 2048);
           }
           let imageData = new ImageDealData();
           let colorPicker = await effectKit.createColorPicker(pixelMap);
           let mainColor = colorPicker.getMainColorSync();
           let colorArr = this.dealColor(mainColor.red, mainColor.green, mainColor.blue);
           let imageColor = `rgba(${colorArr[0]}, ${colorArr[1]}, ${colorArr[2]}, 1)`;
           let imageColorHex = `${colorArr[0].toString(16)}${colorArr[1].toString(16)}${colorArr[2].toString(16)}`;
           // ...
           imageData.imageColorHex = imageColorHex;
           // ...
           resolve(imageData);
         } catch (err) {
           Logger.info(TAG, `getImageDealDataByArr err :${JSON.stringify(err)}`);
           reject(err);
         }
       });
     }
   }
   ```

   卡片侧获取到图片颜色imageColorHex后\*\* \*\*，颜色的数据格式为rgb，可以使用linearGradient属性，给imageColorHex设置不同的透明度，做渐变色处理，使卡片背景平滑过渡自然。

   ```ts
   // src/main/ets/widget/pages/PlayControlCard2x4.ets
   let storageUpdateCall = new LocalStorage();

   @Entry(storageUpdateCall)
   @Component
   struct PlayControlCard2x4 {
     // ...
     @LocalStorageProp('imageColorHex') imageColorHex: string = '18191d';

     // ...
     build() {
       RelativeContainer() {
         // ...
       }
       .height('100%')
       .width('100%')
       .padding(12)
       .onClick(() => {
         ActionUtils.jumpPlayPage(this);
       })
       // ...
     }
   }
   ```

   效果图如下：

   **图 8** 卡片沉浸效果图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/79mrwPdOSRen-1EqaV5KmQ/zh-cn_image_0000002712244430.gif)

   **说明** 

   智能取色Picker目前支持取出PixelMap图片中的主要颜色、平均颜色、饱和度最高、以及占比靠前的颜色。在沉浸式UI中应避免出现纯白色或者纯黑色的色调背景，防止服务卡片的其他组件及内容受到影响。
7. **从播控卡片拉起播放页面**

   当用户点击卡片播控组件（“播放/暂停”等播控相关组件）以外的区域时，可以通过router事件来实现，拉起应用主进程的EntryAbility。

   给卡片最外层布局RelativeContainer绑定onClick事件，通过postCardAction发送router事件，设置参数type的值为RouterType.PLAYER，表示该router事件的目的是拉起播放页面。

   ```ts
   // src/main/ets/widget/pages/PlayControlCard2x4.ets
   let storageUpdateCall = new LocalStorage();

   @Entry(storageUpdateCall)
   @Component
   struct PlayControlCard2x4 {
     // ...
     @LocalStorageProp('songId') songId: string = '';
     // ...
     build() {
       RelativeContainer() {
         // ...
       }
       .height('100%')
       .width('100%')
       .padding(12)
       .onClick(() => {
         ActionUtils.jumpPlayPage(this);
       })
       // ...
     }
   }
   ```

   ```ts
   // src/main/ets/widget/model/ActionUtils.ets
   jumpPlayPage(component: Object) {
     postCardAction(component, {
       action: FormCarAction.ROUTER,
       abilityName: ENTRY_ABILITY,
       params: {
         type: RouterType.PLAYER,
       },
     });
   }
   ```

   如果EntryAbility未在后台运行，拉起UIAbility的时候会触发onCreate生命周期回调；如果EntryAbility已在后台运行，会触发onNewWant()生命周期回调。可以分别在EntryAbility的onCreate和onNewWant中获取卡片传递过来的router事件参数type。当type为RouterType.PLAYER时，使用AppStorage设置isShowPlay为true，用来拉起播放界面。

   ```ts
   // src/main/ets/entryability/EntryAbility.ets
   export default class EntryAbility extends UIAbility {
     // ...
     onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
       // ...
       this.handleParams(want);
       // ...
     }

     onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
       this.handleParams(want);
     }

     handleParams(want: Want) {
       Logger.info(TAG, 'handleParams');
       if (want?.parameters?.params) {
         let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
         let type = params.type as string;
         // ...
         if (type === RouterType.PLAYLISTS) {
           AppStorage.setOrCreate('isToHotPlaylist', true);
         }

         if (type === RouterType.COLLECTED) {
           AppStorage.setOrCreate('mainTabIndex', 1);
           AppStorage.setOrCreate('isShowPlay', false);
         }
       }
     }

     // ...
   }
   ```

   播放页面是通过bindContentCover方法绑定的一个弹窗，通过状态变量isShowPlay来控制其显示和隐藏，isShowPlay使用@StorageLink装饰器修饰用于接收EntryAbility中isShowPlay的值，示例代码如下：

   ```ts
   // src/main/ets/components/PlayController.ets
   @Component
   export struct PlayController {
     // ...
     @StorageLink('isShowPlay') isShowPlay: boolean = false;
     // ...

     build() {
       Row() {
         Row() {
           // ...
         .onClick(() => {
           this.isShowPlay = true;
         })
         // ...
     }

     @Builder
     MusicPlayBuilder() {
       PlayerView({ isShowPlay: this.isShowPlay })
         .height('100%')
         .width('100%')
         // ...
     }
   }
   ```

   效果图如下：

   **图 9** 点击卡片跳转到播放页面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/wSizPONERIuupIrpwhqm3Q/zh-cn_image_0000002742003383.gif)

### 动态歌词卡片

**动态歌词场景实现步骤**

动态歌词卡片的主要实现步骤如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/1EL9pTUnSxGdWh8m4kw_JA/zh-cn_image_0000002712404396.png)

动态歌词目前支持2\*4规格的卡片，效果图如下：

**图 10** 动态歌词卡片效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/2qzaoHqkQC-6il-T0uRtuw/zh-cn_image_0000002742123345.png)

动态歌词卡片的**播控**相关内容，具体实现请参考[音乐播控卡片](arkts-ui-music-service-form.md#音乐播控卡片)的详细开发流程。

动态歌词卡片的**歌词切换功能**开发流程如下：

1. 动态歌词卡片更新，具体请参考音乐播控卡片的[卡片数据初始化](arkts-ui-music-service-form.md#音乐播控卡片)内容。
2. 更新动态歌词卡片时，需要处理歌词相关的数据，在音乐播控卡片的[卡片数据初始化](arkts-ui-music-service-form.md#音乐播控卡片)基础上，新增getSongLyricsArray()方法获取当前歌曲的歌词数组lrcArray，通过调用FormUtils的updateForm()方法更新卡片。

   ```ts
   // src/main/ets/utils/FormUtils.ets
   public async updateMusicControlSingle(context: Context, formId: string) {
     let isPlay = AppStorage.get('isPlay') as boolean;
     let songItem: SongItem = AppStorage.get('currentSong') as SongItem;
     // ...
     let dynamicLrcStr = getSongLyricsArray(context, songItem);
     let formData = new FormControlData();
     formData.isPlay = isPlay;
     formData.formId = formId;
     // ...
     formData.lrcArray = dynamicLrcStr;
     // ...
     this.updateForm(formData.formId, formData);
   }
   ```
3. 卡片页面使用页面级的UI状态存储[LocalStorage](arkts-localstorage.md)接收onAddForm()接口传递的数据，参考音乐播控卡片的[卡片数据初始化](arkts-ui-music-service-form.md#音乐播控卡片)内容。使用装饰器@LocalStorageProp装饰的状态变量接收数据类的详细信息，装饰器@LocalStorageProp(key)中的key值需与数据类的键值一一对应。动态歌词卡片展示歌词的时候，用的就是更新卡片所新增的lrcArray歌词数组字段，用户点击播放歌曲后，就会根据播放进度显示对应歌词信息。

   ```ts
   @Entry(storageUpdateCall1)
   @Component
   struct DynamicLyrics {
     @LocalStorageProp('lrcArray') lrcArray: Array<string> =
       ['This is lyrics sample', 'This is lyrics sample', 'This is lyrics sample', 'This is lyrics sample'];
     @LocalStorageProp('formId') formId: string = '';
     @LocalStorageProp('isPlay') isPlay: boolean = false;
     // ...
   }
   ```
4. 为了实现歌词上一句与下一句之间平滑的切换效果，使用ForEach新增/删除组件结合[组件内转场](../harmonyos-references/ts-transition-animation-component.md)给每一行歌词Text组件绑定transition属性，实现歌词之间显示的过渡效果。

   ```ts
   Column() {
     ForEach(this.lrcArray.slice(0, 2), (item: string, index: number) => {
       Text(item)
         .fontSize(index <= this.currentLyricIndex ? 16 : 13)
         .fontWeight(700)
         .fontColor(index <= this.currentLyricIndex ? Color.White : '#99FFFFFF')
         .lineHeight(30)
         .margin({ top: index === 0 ? 0 : 12 })
         .displayPriority(this.lrcArray.length - index)
         .transition(TransitionEffect.OPACITY.animation({ duration: 200, curve: Curve.Smooth,tempo:2 }))
     }, (item: string, index: number) => (item + index))
   }
   ```

   动态歌词最终效果图如下：

   **图 11** 动态歌词最终效果图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/1UKuFOM5TOmfWKD3WKHmJg/zh-cn_image_0000002712244432.gif)

**应用内添加卡片到桌面场景实现步骤**

应用内**添加卡片到桌面**功能开发流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/x7nJnBXMRBibFlwdYXOWOw/zh-cn_image_0000002742003385.png)

1. 配置好添加卡片的相关数据（ cardRealName：卡片名称；cardDimension：卡片类型； displayName：显示名称； description：卡片描述； url：预览图），已完成卡片布局开发。

   ```ts
   @Component
   export struct MenuComp {
     // ...
     @State card: CardInfo = new CardInfo();
     @State cardInfos: CardInfo[] = [{
       cardRealName: 'PlayControlCard2x2',
       cardDimension: 2,
       displayName: 'app.string.widget_display_name_control',
       description: 'app.string.widget_desc_control',
       url: 'app.media.PlayControlCard2x2'
     },
       // ...
     ]
     // ...
   }
   ```
2. 在实现添加至桌面功能时，需要用到[FormMenu](../harmonyos-references/ohos-arkui-advanced-formmenu.md)菜单组件。首先需要导入[AddFormMenuItem](../harmonyos-references/ohos-arkui-advanced-formmenu.md#addformmenuitem)模块，在AddFormMenuItem里面配置好相关参数，在其中的参数options回调中，获取添加是否成功的信息，提示用户，以便用户感知。最后在应用内点击按钮后显示交互菜单。

   ```ts
   import { AddFormMenuItem } from '@kit.ArkUI';
   // ...

     @Builder
     MyMenu() {
       Menu() {
         AddFormMenuItem(
           {
             bundleName: 'com.huawei.music.card', // Package Name
             abilityName: 'PhoneFormAbility', // Module Capability Name
             parameters: {
               'ohos.extra.param.key.form_dimension': this.card.cardDimension, // Card size, 1 represents 1*2 card, 2 represents 2*2 card, 3 represents 2*4 card, 4 represents 4*4 card, 7 represents 6*4 card, 6 represents 1*1 card
               'ohos.extra.param.key.form_name': this.card.cardRealName, // Card Name
               'ohos.extra.param.key.module_name': 'entry' // Module name to which the card belongs
             },
           },
           this.compId,
           {
             formBindingData: formBindingData.createFormBindingData({}),
             callback: (error, formId) => {
               hilog.info(0x3900, tag, `callback info：error = ${JSON.stringify(error)}, formId = ${formId}`);
               if (error?.code === 0) {
                 this.getUIContext().getPromptAction().showToast({
                   message: $r('app.string.successfully_added_to_desktop'),
                   duration: 1000
                 });
                 this.isShow = false
               } else {
                 this.getUIContext().getPromptAction().showToast({
                   message: $r('app.string.error_added_to_desktop'),
                   duration: 1000
                 });
               }
             },
             style: {}
           }
         )
       }
     }
   ```
3. 在"我的"tab 页面，右上角点击"+"号，触发下拉菜单，点击选项："添加桌面小组件"。

   ```ts
   build() {
     Column() {
       Text('+')
         .height(40)
         .fontSize(30)
         .textAlign(TextAlign.Center)
         .lineHeight(40)
         .fontWeight(300)
         .bindSheet($$this.isShow, this.SheetModal(), {
           detents: [600, SheetSize.MEDIUM, SheetSize.LARGE],
           backgroundColor: '#ededeb',
           dragBar: true,
           title: { title: $r('app.string.add_desktop_widget'), subtitle: "" },
           onDisappear: () => {
             this.isShow = false
           }
         })
     }
   ```
4. 弹出模态窗。

   在[模态窗](../harmonyos-references/ts-universal-attributes-sheet-transition.md)组件中，通过[Menu](../harmonyos-references/ts-basic-components-menu.md)结合[FormMenu](../harmonyos-references/ohos-arkui-advanced-formmenu.md)组件生成可选的卡片类型列表。通过前置条件配置好的信息，拿到所有卡片预览图，采用[轮播图](../harmonyos-references/ts-container-swiper.md)的方式，提供给用户选择不同的卡片预览图，给每一个预览图绑定[bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu8)属性，预览图支持长按后，添加到桌面。

   用户通过轮播图选择需要添加的卡片之后，也可以通过模态窗下方“添加到桌面”按钮，把卡片添加到桌面。

   ```ts
   @Builder
   SheetModal() {
     Column() {
       // ...

       Button($r('app.string.long_pressc_btn'))
         .fontSize(16)
         .width(328)
         .height(40)
         .bindContextMenu(this.MyMenu(), ResponseType.LongPress, {
           placement: Placement.TopLeft
         })
     }
     .alignItems(HorizontalAlign.Center)
     .width('100%')
     .height('100%')
   }
   ```

   应用内添加到桌面效果图如下：

   **图 12** 应用内添加到桌面

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/tniO6R_mSbKRW7NAtAAu4g/zh-cn_image_0000002712404398.gif)

### 音乐播控互动卡片

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/ee7jze6aQCqsRBHKxxmU0A/zh-cn_image_0000002742123347.png)/

**实现步骤**

1. 用户点击普通卡片播放按钮，卡片会通过FormExtensionAbility的onFormEvent()方法触发溢出接口。

   ```ts
   onFormEvent(formId: string, message: string) {
     // Called when a specified message event defined by the form provider is triggered.
     let shortMessage: string = JSON.parse(message)['message'];
     hilog.info(0x0000, TAG, 'onFormEvent');
     if (shortMessage === 'requestOverFlow') {
       this.trigger3DLiveRequest(formId);
     }
   }
   ```

   请求溢出接口如下

   ```ts
   private trigger3DLiveRequest(formId: string) {
     formProvider.getFormRect(formId).then((data: formInfo.Rect) => {
       let cardWidth = data.width * CommonConstants.LIVE_CARD_RATIO;
       let cardHeight = data.height * CommonConstants.LIVE_CARD_RATIO;
       let leftOffset = (data.width - cardWidth) / 2;
       let topOffset = (data.height - cardHeight) / 2;
       formProvider.requestOverflow(formId, {
         area: {
           left: leftOffset,
           top: topOffset,
           width: cardWidth,
           height: cardHeight
         },
         duration: 3500
       }).then(() => {
         hilog.info(0x0000, TAG, 'requestOverflow result succeed');
       }).catch((error: BusinessError) => {
         hilog.error(0x0000, TAG, `requestOverflow catch error, code: ${error.code}, message: ${error.message}`)
       })
     }).catch((error: BusinessError) => {
       hilog.error(0x0000, TAG, `getFormRect catch error, code: ${error.code}, message: ${error.message}`)
     })
     return;
   }
   ```
2. LiveFormExtensionAbility中配置卡片激活态ui文件，并设置背景图。

   ```ts
   export default class UIExtensionAbility extends LiveFormExtensionAbility {
     async onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
       hilog.info(0x0000, TAG, `onLiveFormCreate, liveformInfo: ${JSON.stringify(liveFormInfo)}`);

       let storage: LocalStorage = new LocalStorage();
       storage.setOrCreate('context', this.context);

       let formId: string = liveFormInfo.formId;
       AppStorage.setOrCreate('formId', formId);
       storage.setOrCreate('formId', formId);

       let formRect: formInfo.Rect = liveFormInfo.rect;
       storage.setOrCreate('formRect', formRect);

       let borderRadius: number = liveFormInfo.borderRadius;
       storage.setOrCreate('radius', borderRadius);

       try {
         session.loadContent('uiextensionability/pages/Index', storage);
       } catch (error) {
         hilog.error(0x0000, TAG, `loadContent catch error, code: ${error.code}, message: ${error.message}`)
       }

       let songRdbHelper = SongRdbHelper.getInstance(this.context);
       let initSongs: Array<SongItem> = await songRdbHelper.queryAllSongs();
       if (initSongs.length <= 0) {
         initSongs = getSongListData(this.context);
         songRdbHelper.insertSongs(initSongs);
       }
       AppStorage.setOrCreate('songList', initSongs);
       let currentSong = await PreferencesUtil.getInstance().getCurrentSong(this.context);
       if (!currentSong) {
         currentSong = initSongs[0];
         PreferencesUtil.getInstance().putCurrentSong(this.context, currentSong);
       }
       AppStorage.setOrCreate('currentSong', currentSong);
     }

     onLiveFormDestroy(liveFormInfo: LiveFormInfo): void {
       hilog.info(0x0000, TAG, `onLiveFormDestroy, liveFormInfo: ${JSON.stringify(liveFormInfo)}`);
     }
   }
   ```

   **说明** 

   设置背景图的目的是为了盖住普通卡片的布局，重新绘制激活态卡片。
3. 在激活态UI文件中绘制与普通卡片文件相同的ui布局，并描绘溢出动效。

   ```ts
   build() {
     Stack({ alignContent: Alignment.BottomStart }) {
       RelativeContainer() {
         // ...
       }
       .height(this.formHeight)
       .width(this.formWidth)
       .borderRadius(this.formRadius)
       .padding(12)
       .linearGradient({
         direction: GradientDirection.Bottom,
         repeating: false,
         colors: [[`#ff${this.imageColorHex}`, 0.0], [`#ff${this.imageColorHex}`, 0.5],
           [`#ff${this.imageColorHex}`, 1.0]]
       })
       .margin({
         left: this.formLeft,
         bottom: this.formBottom
       })

       Stack({ alignContent: Alignment.Center }) {
         Image($r('app.media.blackVinyl'))
           .height(88)
           .width(88)

         Button()
           .backgroundImage(this.currentSong.label)
           .backgroundImageSize(ImageSize.Cover)
           .height(58)
           .width(58)
           .backgroundColor($r('sys.color.titlebar_icon_background_color'))
       }
       .alignRules(CoverAlignRules)
       .margin({
         left: CommonConstants.ANIMATE_COMPONENT_LEFT,
         bottom: CommonConstants.ANIMATE_COMPONENT_BOTTOM
       })
       .scale({
         x: this.columnScale,
         y: this.columnScale
       })
       .translate({
         x: this.columnTranslate,
         y: this.rowTranslate
       })
       .rotate({
         x: 0,
         y: 0,
         z: 1,
         angle: this.rotateAngle
       })
       .onAppear(() => {
         this.runEnlargeAnimation();
       })
     }
     .width('100%')
     .height('100%')
   }
   ```

### 歌单推荐卡片

歌单推荐有1x2和2x4两个规格的卡片，效果图如下：

**图 13** 歌单推荐卡片效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/dmU5UqIKT_Oo2iBDqSr3Cg/zh-cn_image_0000002712244434.png)

**实现步骤**

1. **更新卡片图片**

   歌单推荐封面图片加载的是网络图片，加载网络图片需要申请ohos.permission.INTERNET权限。在卡片预览的时候会下载网络图片，并更新到卡片。网络图片的下载以及如何更新到卡片，开发者可以参考：[刷新本地图片和网络图片](arkts-ui-widget-image-update.md)。

   1. 首先在EntryFormAbility的onAddForm()方法中，调用FormUtils的updateRecommendedCard()方法更新卡片，示例代码如下。

      ```ts
      export default class EntryFormAbility extends FormExtensionAbility {
        onAddForm(want: Want) {
          hilog.info(0x0000, TAG, 'onAddForm');
          if (want.parameters) {
            let formId = want.parameters['ohos.extra.param.key.form_identity'] as string;
            let formName = want.parameters['ohos.extra.param.key.form_name'] as string;
            // ...

            if (formName === 'RecommendedMusic1x2' || formName === 'RecommendedMusic2x4') {
              FormUtils.updateRecommendedCard(this.context, formInfo.formId, IMAGE_URL1);
            }
          }
          return formBindingData.createFormBindingData('');
        }

        // ...
      }
      ```
   2. 然后通过updateRecommendedCard()方法下载网络图片，并将图片添加到缓存中，接着调用updateForm()方法更新卡片。

      ```ts
      // src/main/ets/utils/FormUtils.ets
      class FormUtils {
        // ...
        public async updateRecommendedCard(context: Context, formId: string, imageUrl: string) {
          try {
            let tempDir = context.getApplicationContext().tempDir;
            let fileName = 'file' + Date.now();
            let tmpFile = tempDir + '/' + fileName + '.jpg';
            let httpRequest = http.createHttp();
            let data = await httpRequest.request(imageUrl);
            let imgMap: Record<string, number> = {};

            class FormDataClass {
              imgBg: string = fileName;
              formImages: Record<string, number> = imgMap;
              isLoaded: boolean = true;
              imageColorHex: string = '';
            }

            if (data.responseCode === http.ResponseCode.OK) {
              let imgFile = fileIo.openSync(tmpFile, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
              imgMap[fileName] = imgFile.fd;
              try {
                let imageBuffer: ArrayBuffer = data.result as ArrayBuffer;
                let writeLen: number = fileIo.writeSync(imgFile.fd, imageBuffer);
                let imageDealData = await ImageUtils.getImageDealDataByArr(imageBuffer);
                Logger.info(TAG, `write data to file succeed and size is: ${writeLen}`);
                Logger.info(TAG, `ArkTSCard download complete: ${tmpFile}`);
                let formData = new FormDataClass();
                formData.imageColorHex = imageDealData.imageColorHex;
                this.updateForm(formId, formData);
              } catch (err) {
                Logger.error(TAG, `write data to file failed with error: ${JSON.stringify(err)}`);
              } finally {
                fileIo.closeSync(imgFile);
                httpRequest.destroy();
              }
            } else {
              Logger.error(TAG, `ArkTSCard download task failed`);
            }
          } catch (err) {
            let error = err as BusinessError;
            Logger.error(TAG, `updateRecommendedCard err, code: ${error.code}, mesage: ${error.message}`);
          }
        }

        // ...
      }
      ```
   3. 最后Image组件通过入参(memory://fileName)的方式来进行加载缓存中的图片。

      ```ts
      // src/main/ets/widget/pages/RecommendedMusic2x4.ets
      @Entry(storageUpdateCall2)
      @Component
      struct RecommendedMusic2x4 {
        readonly ABILITY_NAME: string = 'EntryAbility';
        readonly ACTION_TYPE: string = 'router';
        @LocalStorageProp('imgBg') imgBg: ResourceStr = '';
        @LocalStorageProp('isLoaded') isLoaded: boolean = false;
        // ...

        build() {
          FormLink({
            action: this.ACTION_TYPE,
            abilityName: this.ABILITY_NAME,
          }) {
            Row() {
              Image(this.isLoaded ? `memory://${this.imgBg}` : $r('app.media.ic_avatar16'))
                .height('100%')
                .borderRadius(10)
                .layoutWeight(1)
                .margin({ right: 6 })
              // ...
            }
            // ...
          }
        }
      }
      ```

   **说明** 

   卡片加载的图片过大可能会导致卡片白屏，建议卡片加载的图片大小不超过2M，在加载卡片图片前需要判断下图片是否过大，如果过大可以采取压缩的方案，图片压缩可以参考FAQ：[如何将PixelMap压缩到指定大小以下](../harmonyos-faqs/faqs-image-16.md)。
2. **卡片跳转功能实现**

   下面将以2x4卡片实现为例进行介绍，歌单推荐卡片使用的是静态卡片，通过[FormLink](../harmonyos-references/ts-container-formlink.md)组件进行跳转，有以下三种跳转场景。

   * 点击“我的收藏”方块跳转到收藏页面。
   * 点击“热门歌单”跳转到热门歌单页面。
   * 点击其他区域直接拉起应用。
   1. 在卡片中使用FormLink组件绑定router事件。

      ```ts
      // src/main/ets/widget/pages/RecommendedMusic2x4.ets
      @Entry(storageUpdateCall2)
      @Component
      struct RecommendedMusic2x4 {
        readonly ABILITY_NAME: string = 'EntryAbility';
        readonly ACTION_TYPE: string = 'router';
        // ...

        build() {
          FormLink({
            action: this.ACTION_TYPE,
            abilityName: this.ABILITY_NAME,
          }) {
            Row() {
              Image(this.isLoaded ? `memory://${this.imgBg}` : $r('app.media.ic_avatar16'))
                // ...
              Column() {
                FormLink({
                  action: this.ACTION_TYPE,
                  abilityName: this.ABILITY_NAME,
                  params: {
                    type: RouterType.COLLECTED
                  }
                }) {
                  Column() {
                    Text($r('app.string.my_collect'))
                      // ...
                    Text('Favorite songs')
                      // ...
                  }
                  // ...
                }

                FormLink({
                  action: this.ACTION_TYPE,
                  abilityName: this.ABILITY_NAME,
                  params: {
                    type: RouterType.PLAYLISTS
                  }
                }) {
                  Column() {
                    Text($r('app.string.hot_playlists'))
                      // ...
                    Text('Hot playlists')
                      // ...
                  }
                  // ...
                }
              }
              .layoutWeight(1)
              .margin({ left: 6 })
            }
            // ...
          }
        }
      }
      ```
   2. 在EntryAbility的生命周期中处理跳转事件。

      通过router事件拉起应用后，在应用侧EntryAbility的onCreate和onNewWant中接收到这三个事件以及事件携带的参数，为了区分，此处新增一个参数type，根据type，应用侧收到事件后可以做相应的业务处理。此处最外层的FormLink仅仅是拉起应用，不需要处理。后续处理“跳转收藏页面”和“跳转热门歌单”两个事件，示例代码如下：

      ```ts
      // src/main/ets/entryability/EntryAbility.ets
      export default class EntryAbility extends UIAbility {
        // ...
        onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
          // ...
          this.handleParams(want);
          // ...
        }

        onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
          this.handleParams(want);
        }

        handleParams(want: Want) {
          Logger.info(TAG, 'handleParams');
          if (want?.parameters?.params) {
            let params: Record<string, Object> = JSON.parse(want.parameters.params as string);
            let type = params.type as string;
            // ...
            if (type === RouterType.PLAYLISTS) {
              AppStorage.setOrCreate('isToHotPlaylist', true);
            }

            if (type === RouterType.COLLECTED) {
              AppStorage.setOrCreate('mainTabIndex', 1);
              AppStorage.setOrCreate('isShowPlay', false);
            }
          }
        }

        // ...
      }
      ```
   3. 在MainPage中根据参数跳转收藏页和热门歌单页面。

      在音乐应用中，“我的收藏”页面是首页Tabs的一个页签。通过更新AppStorage中的mainTabIndex值来切换页面，其中1表示“我的收藏”标签页。首页通过@StorageLink监听mainTabIndex的变化以实现页面切换。

      ```ts
      // src/main/ets/pages/MainPage.ets
      @Entry
      @Component
      struct MainPage {
        @StorageLink('mainTabIndex') currentIndex: number = 0;
        @Provide('pageStack') pageStack: NavPathStack = new NavPathStack();
        // ...
        build() {
          Navigation(this.pageStack) {
            Column() {
              Tabs({ index: this.currentIndex, barPosition: BarPosition.End }) {
                TabContent() {
                  RecommendedMusic()
                }

                TabContent() {
                  CollectedMusic()
                }
              }
              // ...
              .onChange((index) => {
                this.currentIndex = index;
              })

              // ...
            }
            .padding({
              top: AppStorage.get<number>('statusBarHeight') ?? 0,
              bottom: AppStorage.get<number>('naviIndicatorHeight') ?? 0
            })
            .backgroundColor('#F1F3F5')

          }
          .hideTitleBar(true)
          .navDestination(this.PageMap)
          .mode(NavigationMode.Stack)
        }
      }
      ```

      跳转热门歌单，是当用户点击卡片上的“热门歌单”拉起应用后，音乐应用会从首页自动跳转到热门歌单列表页面。这一过程通过在MainPage的onPageShow回调函数中判断isToPlaylists参数来实现，如果该参数为true，则使用pageStack.pushPathByName()方法跳转到热门歌单页面。示例代码如下：

      ```ts
      // src/main/ets/pages/MainPage.ets
      @Entry
      @Component
      struct MainPage {
        @StorageLink('mainTabIndex') currentIndex: number = 0;
        @Provide('pageStack') pageStack: NavPathStack = new NavPathStack();
        @StorageLink('isToHotPlaylist') isToHotPlaylist: boolean = false;
        // ...

        @Builder
        PageMap(name: string) {
          if (name === 'Playlists') {
            HotPlaylist()
          }
        }

        onPageShow(): void {
          if (this.isToHotPlaylist) {
            this.isToHotPlaylist = false;
            // ...
            if (stackIndexArray.length > 0 && stackIndexArray[stackIndexArray.length-1] === 'Playlists') {
              this.pageStack.replacePathByName('Playlists', this.playlistsTitle);
            } else {
              this.pageStack.pushPathByName('Playlists', this.playlistsTitle);
            }
          }
        }

        build() {
          Navigation(this.pageStack) {
            // ...
          }
          .hideTitleBar(true)
          .navDestination(this.PageMap)
          .mode(NavigationMode.Stack)
        }
      }
      ```

   **说明** 

   在通过卡片多次拉起应用进行页面路由时，可能会导致页面栈中同一页面出现多次，从而使得返回操作需要执行多次。为了避免这种情况，应对页面跳转逻辑进行优化，具体处理方法可以参考：[多次点击服务卡片拉起应用指定页面后，该页面在路由栈内存在多个，导致返回上一面需要多次返回操作](arkts-ui-music-service-form.md#多次点击服务卡片拉起应用指定页面后该页面在路由栈内存在多个导致返回上一面需要多次返回操作)。

   跳转效果如下图所示：

   **图 14** 点击卡片跳转效果图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/qnpLFHK7Tw-rucVHMBO-Og/zh-cn_image_0000002742003387.gif)

### 心动歌词卡片

本章将介绍心动歌词卡片的两大核心功能：歌词卡片数据更新和沉浸式卡片设计。歌词卡片数据通过定时刷新来更新卡片数据，而沉浸式卡片则通过设置背景色和背景图片来增强视觉体验。

**实现步骤**

1. 歌词卡片数据更新实现。

   本示例中歌词卡片是通过定时刷新的方式进行刷新，首先需要在卡片配置文件form\_config中进行配置，设置updateEnabled参数的值为true，表示卡片支持周期性刷新（包含定时刷新和定点刷新），设置updateDuration参数的值为1，表示每隔30分钟会进行刷新卡片，参数配置如下：

   ```json5
   // src/main/resources/base/profile/form_config.json
   {
     "forms": [
       // ...
       {
         "name": "LyricsCard",
         // ...
         "updateDuration": 1,
         "defaultDimension": "2*4",
         "supportDimensions": [
           "2*4",
           "4*4"
         ]
       }
     ]
   }
   ```

   接着在EntryFormAbility的onUpdateForm()回调方法中，对卡片数据进行刷新。由于onUpdateForm()方法中的参数只有formId，而本示例涉及三种类型的卡片（音乐播控、歌单推荐和心动歌词），因此需要依据formId查询数据库以获取卡片的具体信息。若查询到卡片的formName为"LyricsCard"，则执行相应的数据更新操作。示例代码如下：

   ```ts
   export default class EntryFormAbility extends FormExtensionAbility {
     // ...

     onUpdateForm(formId: string) {
       // ...
       FormRdbHelper.getInstance(this.context)
         .queryFormById(formId)
         .then((formInfo) => {
           // ...
           if (formInfo.formName === 'LyricsCard') {
             FormUtils.updateLyricsCard(this.context, formInfo.formId);
           }
           // ...
         });
     }
     // ...
   }
   ```

   ```ts
   // src/main/ets/utils/FormUtils.ets
   class FormUtils {
     // ...
     public async updateLyricsCard(context: Context, formId: string) {
       let songData = getRandomLyrics(context);
       let songItem: SongItem = songData.songItem as SongItem;
       let imageDealData = await ImageUtils.getImageDealData(context, songItem.label);

       class CardUpdateData {
         lrcArray: Array<string> = songData.randomLrcStr as Array<string>;
         formId: string = formId;
         singer: string = songItem.singer;
         title: string = songItem.title;
         songId: string = songItem.id;
         musicCover: Resource = songItem.label;
         imageColor = imageDealData.imageColor;
       }

       this.updateForm(formId, new CardUpdateData());
     }
     // ...
   }
   ```
2. 卡片沉浸式方案实现。

   使用Stack堆叠布局，将歌曲封面作为底部背景图，设置图片大小'200%'、透明度0.5、以及模糊度100，开发者可以根据设计自行调节。使用歌曲封面图片的颜色imageColor作为卡片背景色，imageColor的获取可参考[音乐播控](arkts-ui-music-service-form.md#音乐播控)卡片章节。示例代码如下：

   ```ts
   // src/main/ets/widget/pages/LyricsCard.ets
   @Entry(storageUpdateCall1)
   @Component
   struct LyricsCard {
     @LocalStorageProp('musicCover') musicCover: Resource = $r('app.media.ic_dream');
     @LocalStorageProp('imageColor') imageColor: string = 'rgba(76, 72, 68, 1)';
     // ...
     build() {
       FormLink({
         action: FormCarAction.ROUTER,
         abilityName: ENTRY_ABILITY,
         params: {
           songId: this.songId,
           type: RouterType.LYRICS
         }
       }) {
         Stack() {
           Image(this.musicCover)
             .height('200%')
             .width('200%')
             .objectFit(ImageFit.Cover)
             .opacity(0.5)
             .blur(100)

           Column() {
             // ...
           }
           // ...
         }
         .backgroundColor(this.imageColor)
       }
     }
   }
   ```

   效果图如下：

   **图 15** 心动歌词卡片效果图

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/SCRQWJRJTw2pCYMBidrqqg/zh-cn_image_0000002712404400.png)

## 常见问题

### 多次点击服务卡片拉起应用指定页面后，该页面在路由栈内存在多个，导致返回上一面需要多次返回操作。

应用在接收到对应的router跳转事件后，处理跳转的时候需要判断跳转的页面是否已经在路由栈的栈顶，如果在的话需要替换当前的页面，如果不在的话，重新push这个页面到栈。下面以Navigation跳转路由页面为例：

```ts
let stackIndexArray = this.pageStack.getAllPathName();
if (stackIndexArray.length > 0 && stackIndexArray[stackIndexArray.length-1] === 'Playlists') {
  this.pageStack.replacePathByName('Playlists', this.playlistsTitle);
} else {
  this.pageStack.pushPathByName('Playlists', this.playlistsTitle);
}
```

### 手机重启/解锁后卡片内图片消失，出现白屏

该问题可能是卡片加载的图片过大导致的，在加载卡片图片前需要判断图片是否过大，如果过大可以采取压缩的方案，图片压缩可以参考FAQ：[如何将PixelMap压缩到指定大小以下](../harmonyos-faqs/faqs-image-16.md)。关于卡片图片加载规格限制说明可以参考：[刷新本地图片和网络图片](arkts-ui-widget-image-update.md)。

### 手机重启后卡片数据变回兜底内容

卡片框架在重启时是使用onAddForm()回调方法的返回值，若应用重启前调用updateForm()更新的数据和onAddForm()方法返回的数据不一致，可能导致设备重启前后卡片数据不一致，因此需要对数据做持久化处理。例如使用关系型数据库存储卡片最新数据，在FormExtensionAbility的onAddForm()生命周期回调中，获取数据库中的最新数据后，使用updateForm()方法更新卡片。

### 在卡片生命周期和应用UIAbility生命周期获取的temp目录不同，需要分别获取，不能一次存储两端使用。

卡片更新时图片存储在从UIAbility的context获取的temp路径下，与创建时拉起的FormExtensionAbility的temp路径不同。若直接用数据库取出的数据进行卡片更新，会导致图片不能加载。因此，如果在FormExtensionAbility中，从数据库中取到卡片最新数据后，需要再次获取FormExtensionAbility下的temp路径打开本地/网络图片，获取到对应的fd之后再进行数据绑定刷新。

### 如何进行卡片渲染问题定位？

可以在DevEco Studio中查看日志，选择“com.ohos.formrenderservice”卡片渲染服务，通过error日志查看具体卡片渲染报错原因。

## 示例代码

* [基于Form Kit实现音乐服务卡片](https://gitcode.com/HarmonyOS_Samples/MusicCard)
