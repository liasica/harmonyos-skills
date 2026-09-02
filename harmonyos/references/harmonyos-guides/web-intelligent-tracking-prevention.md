---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-intelligent-tracking-prevention
title: 使用智能防跟踪功能
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理Web组件的网络安全与隐私 > 使用智能防跟踪功能
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:00a0debc0359c29b7bccb1e47562ca3de47dc222e7b7270897e6134c21d668be
---

Web组件支持智能防跟踪功能，即当跟踪型网站作为第三方插入到其他网页时，其发送的网络请求将禁止携带cookie。

* 通过调用[enableIntelligentTrackingPrevention](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#enableintelligenttrackingprevention12)接口启用或关闭Web组件的智能防跟踪功能。默认情况下，该功能未启用。

  ```typescript
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Button('enableIntelligentTrackingPrevention')
          .onClick(() => {
            try {
              this.controller.enableIntelligentTrackingPrevention(true);
              console.info('enableIntelligentTrackingPrevention: true');
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        Web({ src: 'www.example.com', controller: this.controller });
      }
    }
  }
  ```
* 调用[isIntelligentTrackingPreventionEnabled](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#isintelligenttrackingpreventionenabled12)接口，判断Web组件是否开启了智能防跟踪功能。

  ```typescript
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Button('isIntelligentTrackingPreventionEnabled')
          .onClick(() => {
            try {
              let result = this.controller.isIntelligentTrackingPreventionEnabled();
              console.info('result: ' + result);
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        Web({ src: 'www.example.com', controller: this.controller });
      }
    }
  }
  ```
* 通过[onIntelligentTrackingPreventionResult](../harmonyos-references/arkts-basic-components-web-events.md#onintelligenttrackingpreventionresult12)接口将被拦截的跟踪型域名及其触发网站的域名回调给应用。

  ```typescript
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        // 需要打开智能防跟踪功能，才会触发onIntelligentTrackingPreventionResult回调
        Button('enableIntelligentTrackingPrevention')
          .onClick(() => {
            try {
              this.controller.enableIntelligentTrackingPrevention(true);
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
            }
          })
        Web({ src: 'www.example.com', controller: this.controller })
          .onIntelligentTrackingPreventionResult((details) => {
            console.info('onIntelligentTrackingPreventionResult: [websiteHost]= ' + details.host +
              ', [trackerHost]=' + details.trackerHost);
          })
      }
    }
  }
  ```

智能防跟踪功能提供了一组接口，用于设置绕过该功能的域名列表。这些接口设置的域名列表适用于整个应用，而非特定的Web组件。

* 调用[addIntelligentTrackingPreventionBypassingList](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#addintelligenttrackingpreventionbypassinglist12)接口设置绕过域名列表。

  ```typescript
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Button('addIntelligentTrackingPreventionBypassingList')
          .onClick(() => {
            try {
              let hostList = ['www.test1.com', 'www.test2.com', 'www.test3.com'];
              webview.WebviewController.addIntelligentTrackingPreventionBypassingList(hostList);
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        Web({ src: 'www.example.com', controller: this.controller });
      }
    }
  }
  ```
* 调用[removeIntelligentTrackingPreventionBypassingList](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#removeintelligenttrackingpreventionbypassinglist12)接口删除部分绕过域名列表。

  ```typescript
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Button('removeIntelligentTrackingPreventionBypassingList')
          .onClick(() => {
            try {
              let hostList = [ 'www.test1.com', 'www.test2.com' ];
              webview.WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList);
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          })
        Web({ src: 'www.example.com', controller: this.controller })
      }
    }
  }
  ```
* 调用[clearIntelligentTrackingPreventionBypassingList](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#clearintelligenttrackingpreventionbypassinglist12)接口清除所有绕过域名列表。

  ```typescript
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Button('clearIntelligentTrackingPreventionBypassingList')
          .onClick(() => {
            webview.WebviewController.clearIntelligentTrackingPreventionBypassingList();
          })
        Web({ src: 'www.example.com', controller: this.controller })
      }
    }
  }
  ```
