---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-197
title: Web组件加载网页过程中遇到的证书相关问题及解决方案
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件加载网页过程中遇到的证书相关问题及解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:11+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:0e93a7b857b0121c00e3e98a4a0b69cb39c4a5e379d7eda5b751467f6739f93b
---

## 问题现象

Web组件加载网页过程中，会遇到证书相关问题，如：

1. 加载时网页出现证书校验错误，如何处理？
2. 网页与服务端需要证书双向认证，如何实现？

## 背景知识

[onSslErrorEvent](../harmonyos-references/arkts-basic-components-web-events.md#onsslerrorevent12)：通知用户加载资源（主资源+子资源）时发生SSL错误（证书校验错误），可在该函数中对SSL错误进行处理。

[onClientAuthenticationRequest](../harmonyos-references/arkts-basic-components-web-events.md#onclientauthenticationrequest9)：通知用户收到SSL客户端证书请求事件，可在该函数中触发客户端证书加载，完成双向认证。

## 解决方案

### 场景一、忽略证书校验

* 现象：

  网页加载过程中，可能会存在域名证书过期、证书链不完整、证书不受信等情况，导致加载时报证书校验失败，网页无法正常加载。
* 解决方案：

  在[onSslErrorEvent](../harmonyos-references/arkts-basic-components-web-events.md#onsslerrorevent12)接口中回调通知证书校验失败异常，可通过[SslErrorHandler](../harmonyos-references/arkts-basic-components-web-sslerrorhandler.md)对证书校验失败进行处理，具备能力：

  + [handleConfirm](../harmonyos-references/arkts-basic-components-web-sslerrorhandler.md#handleconfirm9)：通知Web组件继续加载并使用当前SSL证书，忽略证书错误。
  + [handleCancel](../harmonyos-references/arkts-basic-components-web-sslerrorhandler.md#handlecancel20)：在低于API20版本时，表示不忽略证书校验错误，阻止网页请求加载。在API20及以上版本，可以传布尔值，决定是否停止加载：

    true：表示停止加载页面；

    false：表示继续加载页面，与[handleConfirm](../harmonyos-references/arkts-basic-components-web-sslerrorhandler.md#handleconfirm9)效果类似，默认值为false。
* 示例代码：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { cert } from '@kit.DeviceCertificateKit';

  function LogCertInfo(certChainData: Array<Uint8Array> | undefined) {
    if (!(certChainData instanceof Array)) {
      console.error('failed, cert chain data type is not array');
      return;
    }

    for (let i = 0; i < certChainData.length; i++) {
      let encodeBlobData: cert.EncodingBlob = {
        data: certChainData[i],
        encodingFormat: cert.EncodingFormat.FORMAT_DER
      };
      cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
        if (error) {
          console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
        } else {
          console.info('createX509Cert success');
          console.info(ParseX509CertInfo(x509Cert));
        }
      });
    }
    return;
  }

  function Uint8ArrayToString(dataArray: Uint8Array) {
    let dataString = '';
    for (let i = 0; i < dataArray.length; i++) {
      dataString += String.fromCharCode(dataArray[i]);
    }
    return dataString;
  }

  function ParseX509CertInfo(x509Cert: cert.X509Cert) {
    let res: string = 'getCertificate success, ' + 'issuer name = ' + Uint8ArrayToString(x509Cert.getIssuerName().data) +
      ', subject name = ' + Uint8ArrayToString(x509Cert.getSubjectName().data) + ', valid start = ' +
    x509Cert.getNotBeforeTime() + ', valid end = ' + x509Cert.getNotAfterTime();
    return res;
  }

  @Entry
  @Component
  struct Index1 {
    controller: webview.WebviewController = new webview.WebviewController();
    uiContext: UIContext = this.getUIContext();

    build() {
      Column() {
        // 使用时请替换为真实url
        Web({ src: '*****', controller: this.controller })
          .onSslErrorEvent((event: SslErrorEvent) => {
            console.info('onSslErrorEvent url: ' + event.url);
            console.info('onSslErrorEvent error: ' + event.error);
            console.info('onSslErrorEvent originalUrl: ' + event.originalUrl);
            console.info('onSslErrorEvent referrer: ' + event.referrer);
            console.info('onSslErrorEvent isFatalError: ' + event.isFatalError);
            console.info('onSslErrorEvent isMainFrame: ' + event.isMainFrame);
            LogCertInfo(event.certChainData);
            this.uiContext.showAlertDialog({
              title: 'onSslErrorEvent',
              message: '网页证书校验出错，是否继续加载网页',
              primaryButton: {
                value: '继续加载',
                action: () => {
                  event.handler.handleConfirm();
                }
              },
              secondaryButton: {
                value: '停止加载',
                action: () => {
                  event.handler.handleCancel(true);
                }
              },
              cancel: () => {
                event.handler.handleCancel();
              }
            });
          })
          .geolocationAccess(false)
          .fileAccess(true);
      };
    }
  }
  ```

### 场景二、证书双向认证

* 现象：

  双向认证是指客户端和服务器端都需要验证对方的身份，在建立HTTPS连接的过程中，握手的过程比单向认证多了几步。
  + 单向认证的流程是：客户端（浏览器）请求服务端，服务端返回证书，客户端验证证书合法性后，开始通信。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/v0cIgGIeSKmAZv3uxYIPqw/zh-cn_image_0000002639521234.png "点击放大")
  + 双向认证的流程是：除单向认证步骤外，服务端还会验证客户端提供证书，验证通过后，开始通信。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/OQZdYj4MSEOOYrL0xm7nOA/zh-cn_image_0000002669681273.png "点击放大")
* 解决方案：

  双向认证，客户端发送请求时，需要携带客户端证书，此时依赖客户端设备证书库中已经安装了客户端证书，若是未安装，需要在发送请求前，完成证书安装，再发送请求。实现方式有两种：

  + 方式一：
    1. 将证书预置在应用rawfile目录。
    2. 打开网页前，使用certificateManager.installPrivateCertificate接口，将预置在rawfile目录下的证书安装至证书库。
    3. 打开需要双向认证的网页。
    4. [onClientAuthenticationRequest](../harmonyos-references/arkts-basic-components-web-events.md#onclientauthenticationrequest9)收到SSL客户端证书请求事件。
    5. 调用[ClientAuthenticationHandler.confirm](../harmonyos-references/arkts-basic-components-web-clientauthenticationhandler.md#confirm10)接口，通知Web组件使用证书库中指定证书继续请求。
    6. 完成上述步骤后，客户端请求发送时会自动携带客户端证书，进而进行双向认证。

    示例代码：

    ```ts
    // xxx.ets
    import { webview } from '@kit.ArkWeb';
    import { common } from '@kit.AbilityKit';
    import { certificateManager } from '@kit.DeviceCertificateKit';
    import { BusinessError } from '@kit.BasicServicesKit';

    @Entry
    @Component
    struct Index2 {
      controller: WebviewController = new webview.WebviewController();
      uiContext: UIContext = this.getUIContext();
      context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
      uri: string = '';

      build() {
        Column() {
          Button('安装客户端证书至证书库').onClick(() => {
            if (!this.context) {
              return;
            }

            // ****指证书名称，使用时请提前替换为真实证书，需提前预置在rawfile目录下
            let value: Uint8Array = this.context.resourceManager.getRawFileContentSync('****');
            // keystorePwd指证书凭据密码，certAlias指证书凭据别名，使用时请替换成证书真实密码、别名
            certificateManager.installPrivateCertificate(value, 'keystorePwd', 'certAlias',
              async (err: BusinessError, data: certificateManager.CMResult) => {
                console.info(`installPrivateCertificate, uri==========${JSON.stringify(data.uri)}`);
                if (!err && data.uri) {
                  this.uri = data.uri;
                }
              });
          });
          Button('加载需要客户端SSL证书的网站')
            .onClick(() => {
              // 使用时，请替代真实网址
              this.controller.loadUrl('****');
            });
          Web({
            // 使用时，请替代真实网址
            src: 'www.example.com',
            controller: this.controller,
          })
            .geolocationAccess(false)
            .domStorageAccess(true)
            .fileAccess(true)
            .onPageBegin(event => {
              console.info('extensions onpagebegin url ' + event.url);
            })
            .onClientAuthenticationRequest((event) => {
              console.info('onClientAuthenticationRequest ');
              event.handler.confirm(this.uri);
              return true;
            })
            .onSslErrorEventReceive(e => {
              console.info(`onSslErrorEventReceive->${e.error.toString()}`);
            })
            .onErrorReceive((event) => {
              if (event) {
                this.getUIContext().getPromptAction().showToast({
                  message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
                  alignment: Alignment.Center
                });
                console.info('getErrorInfo:' + event.error.getErrorInfo());
                console.info('getErrorCode:' + event.error.getErrorCode());
                console.info('url:' + event.request.getRequestUrl());
              }
            })
            .onTitleReceive(event => {
              console.info('title received ' + event.title);
            });
        };
      }
    }
    ```
  + 方式二：
    1. 用户将客户端使用证书提前安装至证书库，将证书下载至设备本地后，点击系统设置->隐私和安全->高级->证书与凭据->从存储设备安装->用户凭据，选择下载的客户端证书，输入证书密码后，安装至证书库。
    2. 应用加载需要双向认证的网页，[onClientAuthenticationRequest](../harmonyos-references/arkts-basic-components-web-events.md#onclientauthenticationrequest9)收到SSL客户端证书请求事件。
    3. 在onClientAuthenticationRequest中拉起证书管理，并授权应用使用证书凭据。
    4. 完成上述步骤后，客户端网页请求发送时会自动携带客户端证书，进行双向认证。

    示例代码：

    GlobalContext.ets：

    ```ts
    export class GlobalContext {
      private constructor() {
      }

      private static instance: GlobalContext;
      private _objects = new Map<string, Object>();

      public static getContext(): GlobalContext {
        if (!GlobalContext.instance) {
          GlobalContext.instance = new GlobalContext();
        }
        return GlobalContext.instance;
      }

      getObject(value: string): Object | undefined {
        return this._objects.get(value);
      }

      setObject(key: string, objectClass: Object): void {
        this._objects.set(key, objectClass);
      }
    }
    ```

    CertMgrService.ets：

    ```ts
    import { bundleManager, common, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { GlobalContext } from './GlobalContext';

    export default class CertManagerService {
      private static sInstance: CertManagerService;
      private authUri = '';
      private appUid = '';

      public static getInstance(): CertManagerService {
        if (CertManagerService.sInstance == null) {
          CertManagerService.sInstance = new CertManagerService();
        }
        return CertManagerService.sInstance;
      }

      async grantAppPm(): Promise<string> {
        let bundleFlags =
          bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
        try {
          const data = await bundleManager.getBundleInfoForSelf(bundleFlags)
            .catch((err: BusinessError) => {
              console.error('getBundleInfoForSelf failed. Cause: %{public}s', err.message);
              return null;
            });
          this.appUid = data?.appInfo?.uid?.toString() ?? '';
          console.info('getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
        } catch (err) {
          let message = (err as BusinessError).message;
          console.error('getBundleInfoForSelf failed: %{public}s', message);
        }

        // 注：需要在EntryAbility.ets文件的onCreate函数里添加GlobalContext.getContext().setObject("AbilityContext", this.context)
        let abilityContext = GlobalContext.getContext().getObject('AbilityContext') as common.UIAbilityContext;
        await abilityContext.startAbilityForResult(
          {
            bundleName: 'com.ohos.certmanager',
            abilityName: 'MainAbility',
            uri: 'requestAuthorize',
            parameters: {
              appUid: this.appUid, // 传入申请应用的appUid
            }
          } as Want)
          .then((data: common.AbilityResult) => {
            if (!data.resultCode && data.want) {
              if (data.want.parameters) {
                this.authUri = data.want.parameters.authUri as string; // 授权成功后获取返回的authUri
              }
            }
          });
        return this.authUri;
      }
    };
    ```

    EntryAbility.ets onCreate中，将当前Ability的上下文存储到GlobalContext中：

    ```ts
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      try {
        hilog.info(DOMAIN, 'testTag',
          `want ${want ? 'not' : ''} empty, launchParam ${launchParam ? 'not' : ''} empty`);
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
        // 将当前Ability的上下文存储到GlobalContext中
        GlobalContext.getContext().setObject('AbilityContext', this.context);
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
      }
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }
    ```

    Index.ets：

    ```ts
    import { webview } from '@kit.ArkWeb';
    import CertManagerService from '../common/CertMgrService';

    @Entry
    @Component
    struct Index {
      controller: WebviewController = new webview.WebviewController();
      certManager = CertManagerService.getInstance();

      aboutToAppear(): void {
        webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
      }

      build() {
        Column() {
          Button('加载需要客户端SSL证书的网站')
            .onClick(() => {
              // 使用时请替换真实网址
              this.controller.loadUrl('***');
            });
          Web({
            // 使用时请替换真实网址
            src: 'www.example.com',
            controller: this.controller,
          })
            .domStorageAccess(true)
            .geolocationAccess(false)
            .fileAccess(true)
            .onPageBegin(event => {
              console.info('extensions onpagebegin url ' + event.url);
            })
            .onClientAuthenticationRequest((event) => {
              console.info('onClientAuthenticationRequest ');

              this.certManager.grantAppPm().then(result => {
                console.info(`grantAppPm, URI==========${result}`);
                event.handler.confirm(result);
              });
              return true;
            })
            .onSslErrorEventReceive(e => {
              console.info(`onSslErrorEventReceive->${e.error.toString()}`);
            })
            .onErrorReceive((event) => {
              if (event) {
                this.getUIContext().getPromptAction().showToast({
                  message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
                  alignment: Alignment.Center
                });
                console.info('getErrorInfo:' + event.error.getErrorInfo());
                console.info('getErrorCode:' + event.error.getErrorCode());
                console.info('url:' + event.request.getRequestUrl());
              }
            })
            .onTitleReceive(event => {
              console.info('title received ' + event.title);
            });
        };
      }
    }
    ```

证书安装，需要依赖权限：[ohos.permission.ACCESS\_CERT\_MANAGER](../harmonyos-guides/permissions-for-all.md#ohospermissionaccess_cert_manager)，

访问在线网页，需要依赖权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，

申请权限参考[权限声明](../harmonyos-guides/declare-permissions.md)。

## 常见FAQ

Q：双向认证有什么优缺点？

A：双向认证的优点是安全性更高，因为对客户端和服务器的身份都进行了验证。这样可以有效防止中间人攻击。但是，双向认证的实现比单向认证更复杂，且需要更多的资源（如证书等）。

Q：什么情况下应该选择双向认证而不是单向认证？

A：如果安全性要求不高，或者客户端数量众多、管理困难时，可以选择单向认证；如果安全性要求较高，或者需要确保通信双方的身份可靠性时，可以选择双向认证。

Q：什么情况下需要安装证书？证书的来源是什么？

A：只有当目标服务器采用双向认证时需要安装客户端证书。客户端证书通常是由服务器管理者生成并预先提供给各客户端。
