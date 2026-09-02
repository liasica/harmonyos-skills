---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-126
title: Web组件上PDF的预览下载以及常见问题定位解决
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件上PDF的预览下载以及常见问题定位解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:01764d0915d474b72c391c8c9905967cc92a33f81c0a7553bf09530d92727b6b
---

## 问题现象

如何通过Web组件实现预览和下载PDF文件？遇到PDF预览相关的问题应该如何定位解决？

## 背景知识

* [Web](../harmonyos-references/ts-basic-components-web.md)组件支持在网页中预览PDF。应用通过[WebOptions](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)的src参数和[loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口加载PDF文档。具体场景包括：网络PDF文档、应用沙箱内PDF文档和本地PDF文档。
* [PDF文件预览参数](../harmonyos-guides/web-pdf-preview.md#通过配置pdf文件预览参数控制打开预览时页面状态)：通过配置PDF文件预览参数，控制打开预览时页面状态。
* Web组件具备下载能力，应用可以通过调用[startDownload](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#startdownload11)来下载PDF文件，也可以通过[request.agent.create](../harmonyos-references/js-apis-request.md#requestagentcreate10)方法来下载PDF文件。
* [onPdfScrollAtBottom](../harmonyos-references/arkts-basic-components-web-events.md#onpdfscrollatbottom20)：通知用户PDF页面已滚 动到底。
* [onPdfLoadEvent](../harmonyos-references/arkts-basic-components-web-events.md#onpdfloadevent20)：通知用户PDF页面加载状态，包括成功或失败。
* [domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)：设置是否开启文档对象模型存储接口（DOM Storage API）权限。
* [fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)：设置是否开启应用中文件系统的访问。
* [onProgressChange](../harmonyos-references/arkts-basic-components-web-events.md#onprogresschange)：网页加载进度变化时触发该回调。
* [Progress](../harmonyos-references/ts-basic-components-progress.md)：进度条组件，用于显示内容加载或操作处理等进度。
* [onTitleReceive](../harmonyos-references/arkts-basic-components-web-events.md#ontitlereceive)：网页document标题更改时触发该回调，当H5未设置title元素时会返回对应的URL。
* [prefetchPage](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchpage10)：在预测到将要加载的页面之前调用，可提前下载页面所需的资源（包括：主资源和子资源），但不会执行网页JavaScript代码或呈现网页，以加快页面加载速度，下载的页面资源会缓存五分钟左右，超过这段时间Web组件会自动释放。

## 解决方案

* **关于预览：**

  PDF预览页面会根据用户操作使用window.localStorage记录侧导航栏的展开状态，因此需要开启文档对象模型存储[domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)权限。

  当前主要包含三种PDF文档加载预览场景：

  + 加载预览网络PDF文档，本场景需在module.json5中配置网络访问权限[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，添加方法请参考[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。
    1. 对于可以直接在网页上展示的PDF文档链接，使用如下方法进行展示：

       ```ts
       import { webview } from '@kit.ArkWeb';

       @Entry
       @Component
       struct OnlinePdf {
         controller: webview.WebviewController = new webview.WebviewController();
         url: string = 'www.example.com/test.pdf'; // 使用时需要替换成真实的在线URL

         build() {
           Column() {
             Web({
               src: this.url,
               controller: this.controller
             })
               .domStorageAccess(true)
               .fileAccess(false)
               .geolocationAccess(false);
           };
         }
       }
       ```
    2. 对于那种打开后自动进行下载的PDF文档链接，需要将在线文档下载到本地沙箱，再通过Web进行预览，参考如下demo：

       ```ts
       import { webview } from '@kit.ArkWeb';

       @Entry
       @Component
       struct DownloadUrlPreview {
         controller: webview.WebviewController = new webview.WebviewController();
         delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
         cacheDir: string = this.getUIContext().getHostContext()!.cacheDir;

         build() {
           Column() {
             Web({
               src: 'xxx.com/xxx.pdf', // 需要替换为那种打开后自动下载PDF文档的链接
               controller: this.controller
             })
               .fileAccess(true)
               .domStorageAccess(true)
               .geolocationAccess(false)
               .onControllerAttached(() => {
                 try {
                   this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
                     // 传入本地沙箱路径并开始下载
                     webDownloadItem.start(this.cacheDir + '/' + webDownloadItem.getSuggestedFileName());
                   });
                   this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
                     // 下载任务进度和速度监测处理
                     console.info(`download update guid: ${webDownloadItem.getGuid()}`);
                   });
                   this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
                     // 下载任务失败处理
                     console.error(`download failed guid: ${webDownloadItem.getGuid()}`);
                   });
                   this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
                     // 下载成功通过Web重新加载本地文件打开预览
                     this.controller.loadUrl(`file://${this.cacheDir}/` + webDownloadItem.getSuggestedFileName());
                   });
                   this.controller.setDownloadDelegate(this.delegate);
                 } catch (error) {
                   // 异常处理
                   console.error(
                     `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                 }
               });
           };
         }
       }
       ```
  + 加载预览应用沙箱内PDF文档，本场景需要开启文件系统的[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)权限。

    ```ts
    import { webview } from '@kit.ArkWeb';

    @Entry
    @Component
    struct SandboxPdf {
      controller: webview.WebviewController = new webview.WebviewController();
      url: string | Resource = this.getUIContext().getHostContext()!.filesDir + '/test.pdf';

      build() {
        Column() {
          Web({
            src: this.url,
            controller: this.controller
          })
            .domStorageAccess(true)
            .fileAccess(true)
            .geolocationAccess(false);
        };
      }
    }
    ```
  + 加载应用安装包rawfile目录下的PDF文档。

    ```ts
    import { webview } from '@kit.ArkWeb';

    @Entry
    @Component
    struct LocalFilePdf {
      controller: webview.WebviewController = new webview.WebviewController();
      url: string | Resource = $rawfile('test.pdf'); // 也可以替换成：'resource://rawfile/test.pdf'

      build() {
        Column() {
          Web({
            src: this.url,
            controller: this.controller
          })
            .domStorageAccess(true)
            .fileAccess(false)
            .geolocationAccess(false);
        };
      };
    }
    ```

  在创建Web组件时，通过WebOptions的第一个参数src加载默认PDF文档后，若需变更Web组件显示的PDF文档，不能通过状态变量动态更改src地址，而需要通过调用[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口重新加载指定的PDF文档。

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct LoadUrlDemo {
    controller: webview.WebviewController = new webview.WebviewController();
    url: string | Resource = $rawfile('test.pdf'); // 也可以替换成：'resource://rawfile/test.pdf'

    build() {
      Column() {
        Button('loadUrl')
          .onClick(() => {
            try {
              this.controller.loadUrl(this.url);
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
        Web({
          src: $rawfile('test2.pdf'), // 使用时需要替换成真实的URL
          controller: this.controller
        })
          .domStorageAccess(true)
          .fileAccess(false)
          .geolocationAccess(false);
      };
    }
  }
  ```

  在PDF预览时，很多时候需要实现设置背景色、自动缩放、隐藏下载按钮等功能，这时候需要在PDF地址后面添加配置[预览参数](../harmonyos-guides/web-pdf-preview.md#通过配置pdf文件预览参数控制打开预览时页面状态)，同时配置多个参数时中间使用&符号拼接，参考如下demo：

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct EndParamDemo {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Web({
          src: 'resource://rawfile/test.pdf#toolbar=0&pdfbackgroundcolor=ffffff',
          controller: this.controller
        })
          .domStorageAccess(true)
          .fileAccess(false)
          .geolocationAccess(false);
      };
    }
  }
  ```
* **关于下载**：

  使用[startDownload()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#startdownload11)接口发起一个下载。具体步骤如下：

  1. 向Web注册一个监听类，设置保存路径，初始化并调用WebDownloadItem接口；
  2. 调用startDownload下载PDF文件；
  3. 通过loadUrl接口加载下载到沙箱的PDF文件。

  示例代码如下：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct DownloadDemo {
    controller: webview.WebviewController = new webview.WebviewController();
    delegate: webview.WebDownloadDelegate = new webview.WebDownloadDelegate();
    webCacheDir: string = this.getUIContext().getHostContext()?.cacheDir + '/web/';
    @State myText: string = '未开启监听';
    @State suggestedFileName: string = '';

    build() {
      Column() {
        Text(this.myText);
        Button('注册监听类')
          .onClick(() => {
            try {
              this.myText = '已开启监听';
              this.delegate.onBeforeDownload((webDownloadItem: webview.WebDownloadItem) => {
                console.info('will start a download.');
                // 传入一个下载路径，并开始下载，如果传入一个不存在的路径，则会下载到默认/data/storage/el2/base/cache/web/目录。
                webDownloadItem.start(this.webCacheDir + webDownloadItem.getSuggestedFileName());
              });
              this.delegate.onDownloadUpdated((webDownloadItem: webview.WebDownloadItem) => {
                console.info(`download update guid: ${webDownloadItem.getGuid()}`);
              });
              this.delegate.onDownloadFailed((webDownloadItem: webview.WebDownloadItem) => {
                console.error(`download failed guid: ${webDownloadItem.getGuid()}`);
              });
              this.delegate.onDownloadFinish((webDownloadItem: webview.WebDownloadItem) => {
                console.info(`download finish guid: ${webDownloadItem.getGuid()}`);
                this.myText = '下载完成';
                this.suggestedFileName = webDownloadItem.getSuggestedFileName();
              });
              this.controller.setDownloadDelegate(this.delegate);
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
        Button('开始下载')
          .onClick(() => {
            try {
              // 开发者需要替换为自己想要下载的内容的地址。
              this.controller.startDownload('xxx.com/xxx.pdf');
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
        Button('打开下载的PDF').onClick(() => {
          try {
            this.controller.loadUrl(this.webCacheDir + this.suggestedFileName);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
        Web({
          src: $rawfile('test.pdf'),
          controller: this.controller
        })
          .domStorageAccess(true)
          .fileAccess(true)
          .geolocationAccess(false);
      };
    }
  }
  ```

  对于一些加载比较慢的网页PDF文件，可以通过[prefetchPage](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchpage10)方法在onPageEnd阶段进行预下载，当真正去加载下一个页面的时候，如果预加载已经成功，则相当于直接从缓存中加载页面资源，速度更快。参考如下demo：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct PrefetchDemo {
    prefetchUrl: string =
      'www.example.com/xxx.pdf'; // 网络PDF文件路径
    private controller: WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Button('loadUrl')
          .onClick(() => {
            try {
              this.controller.loadUrl(this.prefetchUrl);
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
        Web({
          src: $rawfile('test.pdf'),
          controller: this.controller
        })
          .domStorageAccess(true)
          .fileAccess(false)
          .geolocationAccess(false)
          .onPageEnd(() => {
            try {
              this.controller.prefetchPage(this.prefetchUrl);
            } catch (error) {
              console.error(
                `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            }
          });
      };
    }
  }
  ```
* **关于常见问题****：**
  + **预览失败，加载白屏/无法加载：**
    1. 首先检查是否开启文档对象模型存储[domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)和网络访问权限[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)。
    2. 搜索Web组件的src参数和loadUrl()接口，检查传入的URL是否正确。
    3. 将对应的链接复制到浏览器，检查是否能正常打开，对于那种打开时自动下载文件的链接，需要将在线文档下载到本地沙箱，再通过Web进行预览，详情参考本文关于预览中的加载网络PDF文档。
    4. 检查手机设置中是否开启了[坚盾守护模式](../harmonyos-guides/web-secure-shield-mode.md)，开启会导致PDF文件预览白屏，因此需要关闭手机设置中的坚盾守护模式。
    5. Web加载一个内含PDF的HTML页面，其他平台加载正常而HarmonyOS异常，对于这种场景，很可能是业务侧进行了限制，通常是通过User-Agent进行的判断，对于这种场景，规避方案是通过手动修改User-Agent来走其他平台下的业务逻辑，但是更推荐通过[User-Agent识别HarmonyOS](../harmonyos-guides/web-default-useragent.md#如何通过user-agent来识别harmonyos操作系统中不同设备)并进行业务侧的适配。
  + **页面展示问题：**
    1. 常见问题为如何隐藏下载按钮、侧边导航窗口、背景色修改以及页面缩放等。对于这一类问题，可以通过配置对应的[PDF文件预览](../harmonyos-guides/web-pdf-preview.md#通过配置pdf文件预览参数控制打开预览时页面状态)参数来解决；
    2. 对于预览本地PDF场景，通过$rawfile('test.pdf')这种方式加载的PDF文件无法添加预览参数，需要通过'resource://rawfile/test.pdf#toolbar=0&navpanes=0'这种方式来加载并添加预览参数。
  + **滚动事件监听失败：**

    Web组件的[onScroll](../harmonyos-references/arkts-basic-components-web-events.md#onscroll9)事件无法监控到Web组件加载的PDF的滑动，因为目前PDF是以插件的形式在Web中加载的，暂不支持监听滚动条（监听不到活动位移），可以通过Web组件的onOverScroll通知网页过度滚动的偏移量的回调判断PDF是否到达顶端，底端。

## 常见FAQ

Q：使用Web预览PDF时，如何判断PDF文件是否是最后一页或者滑动到底部？

A：可以通过[onPdfScrollAtBottom](../harmonyos-references/arkts-basic-components-web-events.md#onpdfscrollatbottom20)事件来通知用户PDF页面已滚动到底，参考如下demo：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct BottomDemo {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({
        src: $rawfile('test.pdf'),
        controller: this.controller
      })
        .domStorageAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .onPdfScrollAtBottom(
          (eventInfo: OnPdfScrollEvent) => {
            console.info(`Scroll at bottom callback called. url: ${eventInfo.url}.`);
          }
        );
    };
  };
}
```

Q：如何监听Web组件是否加载PDF成功？

A：可以通过[onPdfLoadEvent](../harmonyos-references/arkts-basic-components-web-events.md#onpdfloadevent20)事件通知用户PDF页面加载状态，包括成功或失败，样例demo如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct LoadEventDemo {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({
        src: $rawfile('test.pdf'),
        controller: this.controller
      })
        .domStorageAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .onPdfLoadEvent(
          (eventInfo: OnPdfLoadEvent) => {
            console.info(`Load event callback called. url: ${eventInfo.url}, result: ${eventInfo.result}.`);
          }
        );
    };
  };
}
```

Q：如何预览base64格式的PDF文件？

A：可以通过data url方式直接加载，例如：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Base64Demo {
  controller: webview.WebviewController = new webview.WebviewController();
  pdfStr: string = 'data:application/pdf;base64,xxx'; // 使用时将xxx替换为PDF的base64格式数据

  build() {
    Column() {
      Web({
        src: this.pdfStr,
        controller: this.controller
      })
        .domStorageAccess(true)
        .geolocationAccess(false)
        .fileAccess(false);
    };
  }
}
```

Q：如何在预览PDF时显示加载进度条？

A：可以通过[Progress](../harmonyos-references/ts-basic-components-progress.md)组件结合[onProgressChange](../harmonyos-references/arkts-basic-components-web-events.md#onprogresschange)事件来实现，demo如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct LoadProgressDemo {
  controller: webview.WebviewController = new webview.WebviewController();
  // 创建变量表示进度值
  @State value: number = 0;

  build() {
    Column() {
      Progress({ value: this.value, total: 100, type: ProgressType.Capsule })
        .height('200px')
        .borderRadius(80);
      Web({
        src: $rawfile('test.pdf'),
        controller: this.controller
      })
        .domStorageAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .onProgressChange((event) => {
          if (event) {
            this.value = event.newProgress;
          }
        });
    };
  }
}
```

Q：Web预览PDF时如何展示标题title？

A：使用Column嵌套Row和Web实现布局，通过[onTitleReceive](../harmonyos-references/arkts-basic-components-web-events.md#ontitlereceive)方法获取加载的网页的标题。参考如下demo：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct TitleDemo {
  @State title: string = '';
  private webviewController: WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Row() {
        Text(this.title)
          .fontSize('50px')
          .layoutWeight(1)
          .textAlign(TextAlign.Center);
      }
      .width('100%')
      .height(40);

      Web({
        src: 'xxx.com/xxx.pdf', // 运行时替换成真实的地址
        controller: this.webviewController,
      })
        .width('100%')
        .domStorageAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .onTitleReceive((event) => {
          if (event) {
            this.title = event.title;
          }
        });
    };
  }
}
```
