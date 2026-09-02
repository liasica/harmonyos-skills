---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/navigating-between-web-and-apps
title: Web和应用的跳转与拉起
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用间跳转 > 应用间跳转典型场景 > Web和应用的跳转与拉起
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:10+08:00
doc_updated_at: 2026-08-11
content_hash: sha256:b5cf9cfc908b7ca8f8fa7a14d42e1d1f97cc9329c25efe2267de27960c00d071
---

## 概述

在使用ArkTS与ArkWeb进行混合开发时，应用内的部分页面使用了前端相关能力进行了开发，结合Web组件进行了页面加载，在这种场景下涉及到从ArkWeb加载的页面向其他页面跳转，以及从ArkWeb页面拉起应用。

本文将从以下几个方面介绍ArkWeb页面跳转以及拉起应用相关的知识。

* [ArkWeb页面与ArkTS页面互相跳转](navigating-between-web-and-apps.md#arkweb页面与arkts页面互相跳转)
* [ArkWeb页面指定应用跳转](navigating-between-web-and-apps.md#arkweb页面指定应用跳转)
* [ArkWeb页面指定类型跳转](navigating-between-web-and-apps.md#arkweb页面指定类型跳转)
* [ArkWeb页面跳转系统应用页面](navigating-between-web-and-apps.md#arkweb页面跳转系统应用页面)

## ArkWeb页面与ArkTS页面互相跳转

### ArkWeb页面跳转ArkWeb页面

开发者在做Hybrid App混合开发时，Web页面的跳转可以直接在前端侧使用HTML提供的a标签来进行跳转，修改href为跳转后的地址即可。

```html
<a href="www.example.com">跳转到其他页面</a>
```

### ArkTS页面跳转ArkWeb页面

在HarmonyOS应用开发中，会有Web页面和ArkTS页面互相之间进行跳转的场景，例如列表页用了ArkTS进行开发，而详情页设计上只有简单的内容展示并没有复杂的逻辑操作，于是使用了Web开发并使用了ArkTS中的Web组件进行了加载，在这种场景下，从列表页跳转到详情页就是从ArkTS页面跳转到Web页面，在这种场景下，开发者只需要在ArkTS页面对应的事件回调函数中使用路由栈提供的跳转功能即可实现。关于Navigation组件的使用开发者可以参考：[组件导航（Navigation）](arkts-navigation-navigation.md)。

```typescript
NavDestination() {
  Column() {
    Button($r('app.string.back_to_web_page'))
      .width('100%')
      .height(40)
      .onClick(() => {
        this.navPathStack.pop();
      })
  }
  // ...
}
```

### ArkWeb页面跳转ArkTS页面

同样开发者也会有从Web页面跳转到ArkTS页面的场景，例如刚刚的场景中希望返回到ArkTS页面，就是从Web页面跳转回ArkTS页面的场景，在这种场景下，实现步骤如下：

1. 在HTML页面内使用a标签的href属性自定义跳转链接。

   ```html
    <a class="function_item" href="arkts://pages/toOriginPage">跳转到ArkTS页面</a>
   ```

   **说明** 

   开发者可以根据业务场景自行定义href，此处定义的href并不作为a标签跳转后的地址，而是会在ArkTS侧进行跳转拦截，当检测到该链接时执行自定义逻辑。
2. 然后在Web页面中，需要在[onLoadIntercept()](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调函数中进行跳转拦截，拦截后通过路由栈进行页面跳转。

   ```typescript
   Navigation(this.navPathStack) {
     Column() {
       Web({
         src: $rawfile(this.la == Constants.ENGLISH_LANGUAGE ? 'index_en.html' : 'index_cn.html'),
         controller: webviewController
       })
         .zoomAccess(false)
         .onLoadIntercept((event) => {
           const url: string = event.data.getRequestUrl();
           if (url === 'arkts://pages/toOriginPage') {
             this.navPathStack.pushPath({ name: Constants.ORIGIN_PAGE });
           }
           // ...
         })
     }
   }
   ```

## ArkWeb页面指定应用跳转

开发者在HarmonyOS应用内使用了Web页面做了部分页面的实现，同时出于推广，或者需要在其他应用内处理一些逻辑等目的，需要拉起其他的指定应用，例如跳转到支付应用进行支付，在这些场景下，就需要用到指定应用跳转的相关知识，首先在实现方案上，指定应用跳转建议使用如下两种方案：

1. 使用[Deep Linking](deep-linking-startup.md)实现应用拉起。
2. 使用[App Linking](app-linking-startup.md)实现应用拉起。

方案1：使用Deep Linking。

1. 在目标方配置module.json5文件，保证entities中包含entity.system.browsable、actions中包含ohos.want.action.viewData，最后再配置uris，用户可以自定义scheme，host，port以及path。具体含义可以参考：[uris标签说明](module-configuration-file.md#skills标签)。

   ```json5
   {
     "module": {
       // ...
       "abilities": [
         {
           // ...
           "skills": [
             // ...
             {
               "entities": [
                 "entity.system.browsable"
               ],
               "actions": [
                 "ohos.want.action.viewData"
               ],
               "uris": [
                 {
                   "scheme": "appScheme",
                   "host": "www.test.com",
                   "port": "80",
                   "path": "path1"
                 }
               ]
             }
           ]
         }
       ],
       // ...
     }
   }
   ```
2. 在调用方的module.json5文件中配置[querySchemes](module-configuration-file.md#配置文件标签)，标识允许当前应用进行跳转查询的URL schemes。

   ```json5
   "querySchemes": [
     "appScheme"
   ],
   ```
3. 根据目标方的uris配置拼凑出完整的link地址，拼接方式为：scheme://host:port/path，例如上述配置对应的拉起地址为：appScheme://www.test.com:80/path1。

   ```typescript
   const link: string = 'appScheme://www.test.com:80/path1';
   ```
4. 通过[canOpenLink()](canopenlink.md)接口判断link是否可以打开，如不能打开链接开发者可以自定义响应逻辑，此处直接返回。

   ```typescript
   if (!bundleManager.canOpenLink(link)) {
     return true;
   }
   ```
5. 配置拉起时的启动参数[openLinkOptions](../harmonyos-references/js-apis-app-ability-openlinkoptions.md)，在该配置中可以进行参数传递以及配置appLinkingOnly属性。代码参考如下：

   ```typescript
   Navigation(this.navPathStack) {
     Column() {
       Web({
         src: $rawfile(this.la == Constants.ENGLISH_LANGUAGE ? 'index_en.html' : 'index_cn.html'),
         controller: webviewController
       })
         .zoomAccess(false)
         .onLoadIntercept((event) => {
           const url: string = event.data.getRequestUrl();
           // ...
           else if (url === 'third-party://pages/toThirdPage') {
             const link: string = 'appScheme://www.test.com:80/path1';
             try {
               if (!bundleManager.canOpenLink(link)) {
                 return true;
               }
             } catch (error) {
               hilog.error(0x0000, 'testTag', 'canOpenLink failed, code = %{public}d, message = %{public}s',
                 error.code, error.message);
             }
             this.context.openLink(link).then(() => {
               Logger.info('Succeeded in starting FuncAbility');
             }).catch((err: BusinessError) => {
               Logger.error(`Failed to start FuncAbility. Code is ${err.code}, message: ${err.message}`);
             });
           }
           // ...
         })
     }
   }
   ```

方案2：当开发者希望无论应用是否已安装，用户都可以访问到链接对应的内容，当应用安装时优先打开应用去呈现内容；当应用未安装时，则打开浏览器呈现Web版的内容，就可以使用App Linking的方式，App Linking配置可以参考：[使用App Linking实现应用间跳转](app-linking-startup.md)，以下为在ArkWeb页面中使用App Linking进行跳转的操作步骤。

1. 在HTML文件中直接使用a标签的href配置为要跳转应用详情的App Linking地址（需要应用已上架到应用市场），此处以华为应用市场中的华为商城为例。

   ```html
   <a class="function_item" href="https://appgallery.huawei.com/app/detail?id=com.huawei.hmos.vmall">去应用市场下载</a>
   <a class="function_item" href="https://www.huawei.com">打开应用</a>
   ```
2. ArkWeb组件内部完成了对App Linking的自动适配，不需要开发者再做拦截处理，执行默认逻辑即可打开应用市场中的华为商城。

**说明** 

1. ArkWeb内核已完成对App Linking的自动适配，集成了ArkWeb内核的应用，在ArkWeb中访问目标应用的App Linking地址时，系统将在应用已安装时自动拉端，未安装时跳转到对应网页，ArkWeb的宿主应用无需特殊处理。
2. 如果网页嵌入的拉端链接为App Linking时，需要注意App Linking链接的域名与当前访问网页的域名不能相同，即Host部分不可以完全相同，否则会认为用户希望继续停留在网页中访问，不跳转目标端。因此在该场景下需要跨域处理，建议使用子域名的方式区分App Linking的链接与H5网页中嵌入的链接。
3. 直接在浏览器地址栏中输入App Linking链接，不会触发自动拉端逻辑，需要在Web页面中嵌入代码逻辑进行实现链接跳转的功能。
4. 若开发者不希望触发App Linking应用跳转逻辑，而是在应用内以ArkWeb继续浏览，可以在onLoadIntercept()回调中拦截对应的App Linking地址，并手动通过loadUrl()的方式加载网页内容，需注意获取到的链接地址末尾会被自动添加“/”。
5. 无法在浏览器地址栏输入App Linking或Deep Linking打开应用，只能通过网页内的跳转代码实现（a标签、window.open()、window.location.href等）。
6. 目前HarmonyOS设备上华为浏览器对上述两种链接地址做了支持。
7. App Linking跳转失败时，默认配置下将会打开开发者自定义的网页版应用提供给用户进行浏览，通常此时网页内会嵌入按钮实现“在应用市场下载”，目前HarmonyOS设备的跳转逻辑与其他品类设备并不一致，所以需要开发者通过区分UA标识来判断是否为HarmonyOS设备，从而定制HarmonyOS设备上的跳转体验，实现上开发者可以参考[通过UserAgent识别HarmonyOS设备](web-default-useragent.md#如何通过user-agent来识别harmonyos操作系统中不同设备)。

**图 1** Web页面打开效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/akKDTOUeQR-WNI7Y6XLItw/zh-cn_image_0000002736432205.png)

因此，Deep Linking适用于需要在已安装的应用之间进行跳转，实现相对简单，但当无应用匹配时用户体验不佳。而App Linking适用于社交分享、广告引流等需要外部链接访问应用的场景，以及对安全性和用户体验要求较高的场景。AppLinking在Deep Linking的基础上增加了域名校验，提高了链接的安全性和可靠性，且无论应用是否安装，用户都能访问内容。

## ArkWeb页面指定类型跳转

在某些场景下，系统存在多个同类的应用，希望由用户按个人偏好自行选择在哪个应用中进行处理，例如用户收到了一个地址，而系统内有多个导航软件，希望让用户自行选择偏好的软件进行导航。实现上开发者可以参考：[拉起指定类型的应用](start-intent-panel.md)。以下参考代码以调用方拉起地图导航类应用为例。

1. 在HTML页面中使用a标签规定拉起指定应用的字符串。

   ```html
   <a class="function_item" href="arkts://pullSpeciallyApp">拉起指定类型应用</a>
   ```
2. 在Web组件中，当匹配到对应的文本时，执行拉起指定类型的操作。

   ```typescript
   Navigation(this.navPathStack) {
     Column() {
       Web({
         src: $rawfile('index.html'),
         controller: this.controller
       })
         .zoomAccess(false)
         .onLoadIntercept((event) => {
           const url: string = event.data.getRequestUrl();
           if (url === 'navigation://pages/toNavigation') {
             const wantParam: Record<string, Object> = {
               'sceneType': 1,
               'destinationLatitude': 32.060844,
               'destinationLongitude': 118.78315,
               'destinationName': 'xx City xx Road xx Number',
               'destinationPoiIds': {
                 1: '111111111111',
                 2: '222222222222'
               } as Record<number, string>,
               'originName': 'xx City xx Park',
               'originLatitude': 31.060844,
               'originLongitude': 120.78315,
               'originPoiIds': {
                 1: '333333333333',
                 2: '444444444444'
               } as Record<number, string>,
               'vehicleType': 0
             };
             const abilityStartCallback: common.AbilityStartCallback = {
               onError: (code: number, name: string, message: string) => {
                 hilog.error(0x0000, 'testTag', 'onError code %{public}d, name: %{public}s, message: %{public}s',
                   code, name, message);
               }
             };
             this.context.startAbilityByType('navigation', wantParam, abilityStartCallback)
               .catch((err: BusinessError) => {
                 hilog.error(0x0000, 'testTag', 'startAbilityByType failed, code = %{public}d, message = %{public}s',
                   err.code, err.message);
               });
           }
           // ...
         })
     }
   }
   ```

## ArkWeb页面跳转系统应用页面

从ArkWeb页面拉起系统应用界面，也是一个常见的场景，例如开发者有发布图片的需求，而且图片上传的界面在前端界面已经有了实现并且做了多端适配，现在希望复用原有的界面，但是具体的图片选择的逻辑以及上传的逻辑希望修改成ArkTS侧的实现。实现步骤如下：

1. 在Web页面内配置跳转的链接地址。此处使用a标签并不意味着上传的HTML元素就是a标签，而是以它为例，理论上开发者可以用任何HTML元素绑定点击事件，通过设置window.location.href属性进行页面跳转。

   ```html
   <a class="function_item" href="photo://pages/selectPhoto">拉起系统应用</a>
   ```
2. 使用系统提供的照片选择Picker进行图片的选择以及后续逻辑的开发。

   ```typescript
   Navigation(this.navPathStack) {
     Column() {
       Web({
         src: $rawfile('index.html'),
         controller: this.controller
       })
         .zoomAccess(false)
         .onLoadIntercept((event) => {
           const url: string = event.data.getRequestUrl();
           if (url === 'photo://pages/selectPhoto') {
             const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
             photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
             photoSelectOptions.maxSelectNumber = 5;
             let uris: Array<string> = [];
             const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
             photoViewPicker.select(photoSelectOptions)
               .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
                 uris = photoSelectResult.photoUris;
                 console.info('photoViewPicker.select to file succeed and uris are:' + uris);
               })
               .catch((err: BusinessError) => {
                 console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
               })
           }
           // ...
         })
     }
   }
   ```

更多拉起系统应用的方式，开发者可以参考：[拉起系统应用](system-app-startup.md)。

## 示例代码

* [基于应用拉起相关能力实现Web跳转功能](https://gitcode.com/harmonyos_samples/web-application-jump)
