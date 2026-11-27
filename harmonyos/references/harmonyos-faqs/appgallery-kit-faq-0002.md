---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/appgallery-kit-faq-0002
title: 应用跳转下载及市场详情页常见问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 常见问题 > 应用跳转下载及市场详情页常见问题
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:45+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:3a1def5d284366a4d3da50ce1b7a889008a9758ddf1025cf5f52a69c40ced69b
---

**Q：在视频类App、社交类App、浏览器App中，如何通过链接的方式跳转到目标应用的指定页面，并在用户未安装该应用时跳转到应用市场下载页面提示用户安装？**

**A**：拉起应用市场并跳转至应用详情的方式如下：

* Deep Linking：构造拼接bundleName的DeepLink链接，其中bundleName为需要打开的应用包名，其格式为：

  ```txt
  store://appgallery.huawei.com/app/detail?id= + bundleName
  ```

  在应用中调用context.startAbility()方法，拉起应用市场应用详情页示例代码：

  ```ts
  // DeepLink拉起应用市场对应的应用详情页面
  function startAppGalleryDetailAbility(context: common.UIAbilityContext, bundleName: string): void {
    let want: Want = {
      action: 'ohos.want.action.appdetail', // 隐式指定action为ohos.want.action.appdetail
      uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName, // bundleName为需要打开应用详情的应用包名
    };
    context.startAbility(want).then(() => {
      hilog.info(0x0001, 'TAG', 'Succeeded in starting Ability successfully.');
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, 'TAG', `Failed to startAbility.Code: ${error.code}, message is ${error.message}`);
    });
  }
  ```

  在网页中打开DeepLink链接拉起应用市场应用详情页示例代码：

  ```txt
  window.open('store://appgallery.huawei.com/app/detail?id=com.xxxx.xxxx')
  ```

* App Linking：

  构造拼接bundleName的App Linking链接，其中bundleName为需要打开的应用包名，其格式为：

  ```txt
  https://appgallery.huawei.com/app/detail?id= + bundleName
  ```

  在应用中调用openLink()接口拉起App Linking链接的示例代码：

  ```ts
  // App Linking拉起应用市场对应的应用详情页面
  function openAppbyOpenlink(context: common.UIAbilityContext, bundleName: string): void {
    // 需要拼接不同的应用包名，用以打开不同的应用详情页,例如：bundleName:'com.huawei.hmsapp.books'
    // 将下方的域名替换成'https://appgallery.huawei.com/app/detail?id='
    let link: string = '域名' + bundleName;
    // 以App Linking优先的方式在应用市场打开指定包名的应用详情页
    context.openLink(link, { appLinkingOnly: false })
      .then(() => {
        hilog.info(0x0001, 'TAG', 'openlink success.');
      })
      .catch((error: BusinessError) => {
        hilog.error(0x0001, 'TAG', `openlink failed. Code: ${error.code}, message is ${error.message}`);
      });
  }
  ```

  在网页中打开App Linking链接的示例代码：[AppLinking跳转示例](https://appgallery.huawei.com/app/detail?id=com.huawei.hmsapp.books)。

* 调用[loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)方法拉起应用详情页面：

  ```ts
  productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, {
                parameters: {
                  // 必填，此处填入要加载的应用包名，例如： bundleName: 'com.huawei.hmsapp.books'
                  bundleName: 'com.huawei.hmsapp.books',
                }
              });
  ```

  完整示例如下：

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import type { common, Want } from '@kit.AbilityKit';
  import { productViewManager } from '@kit.AppGalleryKit';
  import { webview } from '@kit.ArkWeb';

  // DeepLink拉起应用市场对应的应用详情页面
  function startAppGalleryDetailAbility(context: common.UIAbilityContext, bundleName: string): void {
    let want: Want = {
      action: 'ohos.want.action.appdetail', // 隐式指定action为ohos.want.action.appdetail
      uri: 'store://appgallery.huawei.com/app/detail?id=' + bundleName, // bundleName为需要打开应用详情的应用包名
    };
    context.startAbility(want).then(() => {
      hilog.info(0x0001, 'TAG', 'Succeeded in starting Ability successfully.');
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, 'TAG', `Failed to startAbility.Code: ${error.code}, message is ${error.message}`);
    });
  }

  // App Linking拉起应用市场对应的应用详情页面
  function openAppbyOpenlink(context: common.UIAbilityContext, bundleName: string): void {
    // 需要拼接不同的应用包名，用以打开不同的应用详情页,例如：bundleName:'com.huawei.hmsapp.books'
    // 将下方的域名替换成'https://appgallery.huawei.com/app/detail?id='
    let link: string = '域名' + bundleName;
    // 以App Linking优先的方式在应用市场打开指定包名的应用详情页
    context.openLink(link, { appLinkingOnly: false })
      .then(() => {
        hilog.info(0x0001, 'TAG', 'openlink success.');
      })
      .catch((error: BusinessError) => {
        hilog.error(0x0001, 'TAG', `openlink failed. Code: ${error.code}, message is ${error.message}`);
      });
  }

  @Entry
  @Component
  struct StartAppGalleryDetailAbilityView {
    message: string = '拉起应用市场详情页';
    pageStack: NavPathStack = new NavPathStack();
    uiContext = this.getUIContext();

    @Builder
    PageMap(name: string) {
      if (name === 'WebPage') {
        WebPage()
      }
    }

    build() {
      Navigation(this.pageStack) {
        Column({ space: 20 }) {
          Button(this.message)
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              const context: common.UIAbilityContext = this.uiContext?.getHostContext() as common.UIAbilityContext;
              // 按实际需求获取应用的bundleName，例如bundleName: 'com.huawei.hmsapp.books'
              const bundleName = 'com.huawei.hmsapp.books';
              startAppGalleryDetailAbility(context, bundleName);
            });
          Button('App Linking打开')
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              openAppbyOpenlink(this.getUIContext().getHostContext() as common.UIAbilityContext,
                'com.huawei.hmsapp.books');
            });
          Button('网页中DeepLink打开')
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              this.pageStack.pushPathByName('WebPage', null);
            });
          Button('loadProduct方法拉起应用详情')
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, {
                parameters: {
                  // 必填，此处填入要加载的应用包名，例如： bundleName: 'com.huawei.hmsapp.xxx.xxx'
                  bundleName: 'com.huawei.hmsapp.books',
                }
              });
            });
        }
        .width('100%')
        .justifyContent(FlexAlign.Center)
        .margin({ top: 50 });
      }
      .title('详情页跳转演示')
      .navDestination(this.PageMap)
      .height('100%')
      .width('100%');
    }
  }

  /**
   * Web 预览页面组件
   */
  @Component
  struct WebPage {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      NavDestination() {
        Column() {
          Web({
            // resources/rawfile 目录下存在 detail.html 文件
            src: $rawfile('detail.html'),
            controller: this.controller
          })
            .onLoadIntercept((event) => {
              const url = event.data.getRequestUrl();
              hilog.info(0x0001, 'TAG', `WebView Intercepted URL: ${url}`);

              if (url.startsWith('store://')) {
                const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                startAppGalleryDetailAbility(context, 'com.huawei.hmsapp.books');
                return true; // 拦截并停止 Web 组件继续加载该非法 URL
              }
              return false;
            })
            .fileAccess(true)
            .geolocationAccess(false)
            .domStorageAccess(true)
            .javaScriptAccess(true)
            .width('100%')
            .height('100%')
        }
        .width('100%')
        .height('100%')
      }
      .title('网页预览')
      .onBackPressed(() => {
        return false;
      })
    }
  }
  ```

  H5代码：

  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
          body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; background: #f0f2f5; }
          .card { background: white; padding: 30px; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 80%; text-align: center; }
          .logo { width: 64px; height: 64px; margin-bottom: 15px; }
          .btn { display: inline-block; padding: 12px 24px; background: #007DFF; color: white; text-decoration: none; border-radius: 8px; font-weight: bold; transition: background 0.2s; }
          .btn:active { background: #0056b3; }
      </style>
  </head>
  <body>
  <div class="card">
      <h3>网页跳转测试</h3>
      <p>通过 Rawfile 加载的本地页面</p>

      <a class="btn" href="store://appgallery.huawei.com/app/detail?id=com.huawei.hmsapp.books">立即打开详情页</a>
  </div>
  </body>
  </html>
  ```

**Q：非公开发布应用，如何跳转至应用详情？**

**A**：应用选择[非公开发布](../app/agc-help-non-public-release-0000002278016482.md)上架后，发布类型下方展示非公开发布链接，链接形式为：https://appgallery.huawei.com/app/detail?id=包名，可以通过App Linking方式跳转。在已知应用包名的情况下也可以自行构造Deep Linking链接实现。

**Q：构造DeepLink拉起应用下载安装的链接store://enterprise/manifest?url=https://xxx.xxx/xxx.json5，其中的url必须是公网可以访问的吗？**

**A**：是的。应用市场也会有下载校验。

**Q：productViewManager.loadProduct调用的时候，会显示有个正在加载的动画图标，是否有参数控制可以去除？**

**A**：productViewManager.loadProduct没有参数控制去除正在加载的动画图标，可以使用DeepLink、App Linking接口，这两个接口没有加载的动画图标。

**Q：我们设计了应用的下载页面，页面会展示当前我们在架应用的应用信息。HarmonyOS NEXT是否支持外部网页查询我们自己已上架应用的应用信息？**

**A**：可以使用Publishing API的[查询应用信息](../app/agc-help-publish-api-appinfo-query-0000002236041422.md)接口来查询应用信息。因为外部H5直接访问华为的接口，一般都会存在跨域问题。所以建议从开发者自己的服务端调用华为接口获取信息然后返回给前端H5页面。

**Q：如何通过二维码下载应用？**

**A**：使用构造拼接bundleName的链接生成二维码，扫码即可跳转到应用市场应用详情页，即可下载。

**Q：小艺智能对话页面如何通过点击高亮字体跳转应用市场？**

**A**：高亮可以通过markdown的文本格式构造，然后点击跳转可以通过App Linking的方式拉起应用市场。

**Q：应用使用公开测试渠道发布时，正式详情页链接是否可以跳转至应用尝鲜入口？**

**A**：正式详情页链接（如https://appgallery.huawei.com/app/detail?id=包名）只能跳转正式应用详情页，无法跳转至测试渠道的应用尝鲜入口。公开测试渠道发布时，需要使用以下链接格式：https://appgallery.huawei.com/link/invite-test-wap?taskld=xxxxx&invitationcode=xxxxx。后续应用正式发布后，将链接修改回正式详情页链接即可。

**Q：应用还未上架时，如何测试能否跳转至应用市场详情页？**

**A**：可以通过Deep Linking方式跳转，使用已上架应用的包名进行测试。在DevEco Studio中可以查看其他应用的进程名获取包名。

**Q：应用尝鲜版本是否可以通过链接跳转引导用户下载？**

**A**：可以通过链接跳转引导用户下载。在配置测试类型和发布方式时，勾选“生成分享链接”选项，勾选后可将生成的“邀请链接”分享给用户来引导用户参与测试。上架至应用尝鲜专区的方式：在应用测试中创建新版本并选择测试类型（公开测试或邀请测试），完善测试版本信息时勾选生成分享链接和发布至测试专区，提交审核通过后即可上架。具体操作参考[公开测试](../app/agc-help-public-test-guide-0000002293706429.md)和[邀请测试](../app/agc-help-appgallery-invite-test-guide-0000002292711373.md)。

**Q：应用市场跳转是否支持设置参数跳转到应用尝鲜，或者在应用内通过点击链接引导用户更新到公测版本？**

**A**：可以通过[App Linking方式](../harmonyos-guides/appgallery-productview-loadproduct.md#app-linking方式)跳转，将链接参数设置为https://appgallery.huawei.com/app/test?taskId=xxxxxxx，其中taskId为上架测试版本的taskId。也可以参考[通过分享链接下载安装测试版本](../app/agc-help-publictest-user-test-0000002259136298.md#section768281215123)，在应用内引导用户使用浏览器打开链接。

**Q：如何通过服务端API获取应用尝鲜版本的分享链接并在应用中打开？**

**A**：可以通过服务端API获取应用尝鲜版本的分享链接。调用[查询应用信息](../app/agc-help-publish-api-appinfo-query-0000002236041422.md#section420734618165)接口获取shareLink，调用[查询邀请码](../app/agc-help-test-api-get-invite-code-0000002271160669.md)接口获取邀请码，拼接shareLink与invitationCode参数生成完整链接。然后在应用内通过startAbility或openLink打开该链接。

**Q：在卓易通中运行的其他平台应用或H5页面，如何跳转到应用市场或HarmonyOS浏览器？**

**A**：其他平台应用可通过隐式拉起方式跳转应用市场应用详情页。核心原理是利用其他平台标准Intent机制，卓易通兼容容器将其映射到HarmonyOS的隐式Want机制，由系统匹配并拉起目标应用。推荐统一使用应用市场应用详情页作为入口，系统自动判断目标应用是否已安装：已安装则展示应用详情可直接打开，未安装则显示下载页面引导用户安装。其他平台应用中，通过Intent.ACTION\_VIEW构造隐式拉起请求，URI使用store://appgallery.huawei.com/app/detail?id=拼接目标应用的bundleName。当store://scheme不支持时，回退使用https://链接拉起，该链接可在浏览器中打开。H5页面中直接使用<a>标签或window.location.href跳转，链接地址使用应用市场应用详情页URL。ArkWeb内核已自动适配App Linking，应用无需特殊处理。

**Q：应用正式在架版本下，触发跳转应用市场详情页逻辑时无法自动跳转，手动选择应用市场打开链接也无法定位到详情页，且无错误码返回，如何解决？**

**A**：该问题多为跳转目标地址配置异常导致的静默失败。优先核对跳转目标地址的来源与完整性：确认跳转地址是否由运维后台配置下发而非代码硬编码；检查配置地址是否被意外修改，如多出空格或不可见特殊字符；确认链接scheme与参数是否符合应用市场对appgallery.huawei.com/app/detail?id=链接的解析要求。若确认地址中误含多余空格字符，移除多余空格、重新保存并下发正确地址后，自动跳转与手动选择应用市场即可恢复正常。由于https形式的链接依赖系统的[App Linking Kit](../harmonyos-guides/applinking-introduction.md)匹配机制（需端云校验域名归属），并非系统级强制跳转，易受应用市场客户端版本、系统版本、网络连通性等因素影响，可能出现拉不起或拉起后定位不到的静默失败。建议改用Deep Linking方式（store://appgallery.huawei.com/app/detail?id=包名）并调用[startAbility](../harmonyos-guides/deep-linking-startup.md)直接拉起应用市场详情页，提升跳转稳定性，具体实现可参考上文Deep Linking拉起应用市场应用详情页的示例代码。

**Q：配置官网下载链接引导用户跳转商店下载，使用appmarket://details?id=应用包名格式的链接是否可以？**

**A**：不可以。需要使用store://appgallery.huawei.com/app/detail?id=拼接应用bundleName的链接拉起应用市场应用详情页，具体实现可参考上文Deep Linking拉起应用市场应用详情页的示例代码。

**Q：使用其他平台包名拼接的appmarket://details?id=链接也能在HarmonyOS上拉起应用，是否正常？是否做了校验？**

**A**：正常，不是校验，是关联映射。HarmonyOS应用可以关联一个在架的其他平台的应用，但关联关系建立后不可再变更。当用户将其设备上的其他平台系统升级到HarmonyOS 5系统时，其他平台系统上已安装的其他平台应用，将会根据绑定的关联关系，被自动替换为该应用的HarmonyOS版本，以及迁移相关其他平台用户数据至HarmonyOS应用。为防止包名重复导致应用覆盖安装，建议将HarmonyOS包名与其他平台的包名区分开来。

**Q：在应用内提供了检查更新按钮，点击后跳转到应用市场，显示“此应用暂不支持在当前设备安装”？**

**A**：

问题原因1：目标应用未在HarmonyOS NEXT应用市场上架。此场景一般出现在上架调试、邀请测试场景。

解决方案：需通过华为应用市场查看目标应用是否已上架；若应用未适配，需按HarmonyOS NEXT规范升级并重新发布。

问题原因2：若应用已经正式上架，仍然出现这个问题，需排查是否跳转链接使用错误。

解决方案：在应用内使用链接形式跳转到应用市场，id建议使用bundleName。

```screen
store://appgallery.huawei.com/app/detail?id= + bundleName
```

如果使用了appId，为兼容旧链接，可以在appId前拼接大写的C。如下所示：

```screen
store://appgallery.huawei.com/app/detail?id=C123456
```

推荐使用官方文档提供的方式实现[应用市场更新功能](../harmonyos-guides/store-update.md)。
