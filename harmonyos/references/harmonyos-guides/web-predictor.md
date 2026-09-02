---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-predictor
title: 加速Web页面的访问
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页加载与浏览记录 > 加速Web页面的访问
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a004fd3eb9dcec1d39034d8c7b028ce3951ecb644f564b8332c928aa13662e36
---

当Web页面加载缓慢时，可以使用预连接、预加载和预获取POST请求的能力加速Web页面的访问。

针对Web页面加载性能优化的详细内容请参考[Web页面加载优化性能指导](../best-practices/bpta-web-develop-optimization.md#section128761465256)。

## 预解析和预连接

此方法可以针对域名级进行优化，通过[prepareForPageLoad()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prepareforpageload10)来预解析或者预连接将要加载的页面。该方式仅对url进行DNS解析以及建立tcp连接，但不会获取主资源子资源。

在下面的示例中，在Web组件的onAppear中对要加载的页面进行预连接。

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'https://www.example.com/', controller: this.webviewController })
        .onAppear(() => {
          // 指定第二个参数为true，代表要进行预连接，如果为false该接口只会对网址进行dns预解析
          // 第三个参数为要预连接socket的个数。最多允许6个。
          webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 2);
        })
    }
  }
}
```

也可以通过[initializeWebEngine()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#initializewebengine)来提前初始化内核，然后在初始化内核后调用[prepareForPageLoad()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prepareforpageload10)对即将要加载的页面进行预解析、预连接。这种方式适合提前对首页进行预解析、预连接。

在下面的示例中，Ability的onCreate中提前初始化Web内核并对首页进行预连接。

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 预连接时，需要将'https://www.example.com'替换成真实要访问的网站地址。
    webview.WebviewController.prepareForPageLoad("https://www.example.com/", true, 2);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

## 预加载

此方法可针对资源级进行优化。如果能够预测到Web组件将要加载的页面或者即将要跳转的页面。可以通过[prefetchPage()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchpage10)来预加载即将要加载的页面。

预加载会提前下载页面所需的资源，包括主资源子资源，避免阻塞页面渲染。但不会执行网页JavaScript代码。预加载是WebviewController的实例方法，需要一个已经关联好Web组件的WebviewController实例。

在下面的示例中，在onPageEnd的时候触发下一个要访问的页面的预加载。

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'https://www.example.com/', controller: this.webviewController })
        .onPageEnd(() => {
          // 预加载https://www.iana.org/help/example-domains。
          this.webviewController.prefetchPage('https://www.iana.org/help/example-domains');
        })
    }
  }
}
```

## 预获取POST请求

此方法可以针对请求级进行优化。可以通过[prefetchResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchresource12)预获取将要加载页面中的POST请求。在页面加载结束时，可以通过[clearPrefetchedResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#clearprefetchedresource12)清除后续不再使用的预获取资源缓存。

以下示例，在Web组件onAppear中，对要加载页面中的POST请求进行预获取。在onPageEnd中，可以清除预获取的POST请求缓存。

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'https://www.example.com/', controller: this.webviewController })
        .onAppear(() => {
          // 预获取时，需要将'https://www.example1.com/post?e=f&g=h'替换成真实要访问的网站地址。
          webview.WebviewController.prefetchResource(
            {
              url: 'https://www.example1.com/post?e=f&g=h',
              method: 'POST',
              formData: 'a=x&b=y',
            },
            [{
              headerKey: 'c',
              headerValue: 'z',
            },],
            'KeyX', 500);
        })
        .onPageEnd(() => {
          // 清除后续不再使用的预获取资源缓存。
          webview.WebviewController.clearPrefetchedResource(['KeyX',]);
        })
    }
  }
}
```

如果能够预测到Web组件将要加载页面或者即将要跳转页面中的POST请求。可以通过[prefetchResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchresource12)预获取即将要加载页面的POST请求。

以下示例，在onPageEnd中，触发预获取一个要访问页面的POST请求。

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'https://www.example.com/', controller: this.webviewController })
        .onPageEnd(() => {
          // 预获取时，需要将'https://www.example1.com/post?e=f&g=h'替换成真实要访问的网站地址。
          webview.WebviewController.prefetchResource(
            {
              url: 'https://www.example1.com/post?e=f&g=h',
              method: 'POST',
              formData: 'a=x&b=y',
            },
            [{
              headerKey: 'c',
              headerValue: 'z',
            },],
            'KeyX', 500);
        })
    }
  }
}
```

也可以通过[initializeWebEngine()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#initializewebengine)提前初始化内核，然后在初始化内核后调用[prefetchResource()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchresource12)预获取将要加载页面中的POST请求。这种方式适合提前预获取首页的POST请求。

以下示例，在Ability的onCreate中，提前初始化Web内核并预获取首页的POST请求。

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    console.info("EntryAbility onCreate");
    webview.WebviewController.initializeWebEngine();
    // 预获取时，需要将"https://www.example1.com/post?e=f&g=h"替换成真实要访问的网站地址。
    webview.WebviewController.prefetchResource(
      {
        url: "https://www.example1.com/post?e=f&g=h",
        method: "POST",
        formData: "a=x&b=y",
      },
      [{
        headerKey: "c",
        headerValue: "z",
      },],
      "KeyX", 500);
    AppStorage.setOrCreate("abilityWant", want);
    console.info("EntryAbility onCreate done");
  }
}
```

## 预编译生成编译缓存

可以通过[precompileJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#precompilejavascript12)在页面加载前提前生成脚本文件的编译缓存。

推荐配合动态组件使用，使用离线的Web组件用于生成字节码缓存，并在适当的时机加载业务用Web组件使用这些字节码缓存。下方是代码示例：

1. 首先，在EntryAbility中将[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)存到[localStorage](arkts-localstorage.md)中。

   ```ts
   // EntryAbility.ets
   import { UIAbility } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   const localStorage: LocalStorage = new LocalStorage('uiContext');

   export default class EntryAbility extends UIAbility {
     storage: LocalStorage = localStorage;

     onWindowStageCreate(windowStage: window.WindowStage) {
       windowStage.loadContent('pages/Index', this.storage, (err, data) => {
         if (err.code) {
           return;
         }

         this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
       });
     }
   }
   ```
2. 编写动态组件所需基础代码。

   ```typescript
   // main/ets/pages/DynamicComponent.ets
   import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

   export interface BuilderData {
     url: string;
     controller: WebviewController;
     context: UIContext;
   }

   let storage : LocalStorage | undefined = undefined;

   export class NodeControllerImpl extends NodeController {
     private rootNode: BuilderNode<BuilderData[]> | null = null;
     private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

     constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
       storage = context.getSharedLocalStorage();
       super();
       this.wrappedBuilder = wrappedBuilder;
     }

     makeNode(): FrameNode | null {
       if (this.rootNode != null) {
         return this.rootNode.getFrameNode();
       }
       return null;
     }

     initWeb(url: string, controller: WebviewController) {
       if(this.rootNode != null) {
         return;
       }

       const uiContext: UIContext = storage!.get<UIContext>('uiContext') as UIContext;
       if (!uiContext) {
         return;
       }
       this.rootNode = new BuilderNode(uiContext);
       this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
     }
   }

   export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
     const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
     baseNode.initWeb(data.url, data.controller);
     return baseNode;
   }
   ```
3. 编写用于生成字节码缓存的组件，本例中的本地JavaScript资源内容通过文件读取接口读取rawfile目录下的本地文件。

   ```typescript
   // main/ets/pages/PrecompileWebview.ets
   import { BuilderData } from './DynamicComponent';
   import { Config, configs } from './PrecompileConfig';

   @Builder
   function webBuilder(data: BuilderData) {
     Web({ src: data.url, controller: data.controller })
       .onControllerAttached(() => {
         precompile(data.controller, configs, data.context);
       })
       .fileAccess(true)
   }

   export const precompileWebview = wrapBuilder<BuilderData[]>(webBuilder);

   export const precompile = async (controller: WebviewController, configs: Array<Config>, context: UIContext) => {
     for (const config of configs) {
       let content = await readRawFile(config.localPath, context);

       try {
         controller.precompileJavaScript(config.url, content, config.options)
           .then(errCode => {
             console.info('precompile successfully! ' + errCode);
           }).catch((errCode: number) => {
             console.error('precompile failed. ' + errCode);
         });
       } catch (err) {
         console.error('precompile failed. ' + err.code + ' ' + err.message);
       }
     }
   }

   async function readRawFile(path: string, context: UIContext) {
     try {
       return await context.getHostContext()!.resourceManager.getRawFileContent(path);
     } catch (err) {
       return new Uint8Array(0);
     }
   }
   ```

   JavaScript资源的获取方式也可通过[数据请求](../harmonyos-references/js-apis-http.md)的方式获取，但此方法获取到的HTTP响应头非标准HTTP响应头格式，需额外将响应头转换成标准HTTP响应头格式后使用。如通过网络请求获取到的响应头是e-tag，则需要将其转换成E-Tag后使用。
4. 编写业务用组件代码。

   ```typescript
   // main/ets/pages/BusinessWebview.ets
   import { BuilderData } from './DynamicComponent';

   @Builder
   function webBuilder(data: BuilderData) {
     // 此处组件可根据业务需要自行扩展
     Web({ src: data.url, controller: data.controller })
       .cacheMode(CacheMode.Default)
   }

   export const businessWebview = wrapBuilder<BuilderData[]>(webBuilder);
   ```
5. 编写资源配置信息。

   ```typescript
   // main/ets/pages/PrecompileConfig.ets
   import { webview } from '@kit.ArkWeb'

   export interface Config {
     url:  string,
     localPath: string, // 本地资源路径
     options: webview.CacheOptions
   }

   export let configs: Config[] = [
     {
       url: 'https://www.example.com/example.js',
       localPath: 'example.js',
       options: {
         responseHeaders: [
           { headerKey: 'E-Tag', headerValue: 'aWO42N9P9dG/5xqYQCxsx+vDOoU='},
           { headerKey: 'Last-Modified', headerValue: 'Wed, 21 Mar 2025 10:38:41 GMT'}
         ]
       }
     }
   ]
   ```
6. 在页面中使用。

   ```typescript
   // main/ets/pages/Index.ets
   import { webview } from '@kit.ArkWeb';
   import { NodeController } from '@kit.ArkUI';
   import { createNode } from './DynamicComponent';
   import { precompileWebview } from './PrecompileWebview';
   import { businessWebview } from './BusinessWebview';

   @Entry
   @Component
   struct Index {
     @State precompileNode: NodeController | undefined = undefined;
     precompileController: webview.WebviewController = new webview.WebviewController();

     @State businessNode: NodeController | undefined = undefined;
     businessController: webview.WebviewController = new webview.WebviewController();

     aboutToAppear(): void {
       // 初始化用于注入本地资源的Web组件
       this.precompileNode = createNode(precompileWebview,
         { url: 'https://www.example.com/empty.html', controller: this.precompileController, context: this.getUIContext()});
     }

     build() {
       Column() {
         // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
         Button('加载页面')
           .onClick(() => {
             this.businessNode = createNode(businessWebview, {
               url: 'https://www.example.com/business.html',
               controller: this.businessController,
               context: this.getUIContext()
             });
           })
         // 用于业务的Web组件
         NodeContainer(this.businessNode);
       }
     }
   }
   ```

当需要更新本地已经生成的编译字节码时，修改cacheOptions参数中responseHeaders中的E-Tag或Last-Modified响应头对应的值，再次调用接口即可。

## 离线资源免拦截注入

可以通过[injectOfflineResources()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#injectofflineresources12)在页面加载前提前将图片、样式表或脚本资源注入到应用的内存缓存中。

推荐配合动态组件使用，使用离线的Web组件用于将资源注入到内核的内存缓存中，并在适当的时机加载业务用Web组件使用这些资源。下方是代码示例：

1. 首先，在EntryAbility中将[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)存到[localStorage](arkts-localstorage.md)中。

   ```ts
   // EntryAbility.ets
   import { UIAbility } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   const localStorage: LocalStorage = new LocalStorage('uiContext');

   export default class EntryAbility extends UIAbility {
     storage: LocalStorage = localStorage;

     onWindowStageCreate(windowStage: window.WindowStage) {
       windowStage.loadContent('pages/Index', this.storage, (err, data) => {
         if (err.code) {
           return;
         }

         this.storage.setOrCreate<UIContext>("uiContext", windowStage.getMainWindowSync().getUIContext());
       });
     }
   }
   ```
2. 编写动态组件所需基础代码。

   ```typescript
   // main/ets/pages/DynamicComponent.ets
   import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

   export interface BuilderData {
     url: string;
     controller: WebviewController;
     context: UIContext;
   }

   let storage : LocalStorage | undefined = undefined;

   export class NodeControllerImpl extends NodeController {
     private rootNode: BuilderNode<BuilderData[]> | null = null;
     private wrappedBuilder: WrappedBuilder<BuilderData[]> | null = null;

     constructor(wrappedBuilder: WrappedBuilder<BuilderData[]>, context: UIContext) {
     storage = context.getSharedLocalStorage();
       super();
       this.wrappedBuilder = wrappedBuilder;
     }

     makeNode(): FrameNode | null {
       if (this.rootNode != null) {
         return this.rootNode.getFrameNode();
       }
       return null;
     }

     initWeb(url: string, controller: WebviewController) {
       if(this.rootNode != null) {
         return;
       }

       const uiContext: UIContext = storage!.get<UIContext>('uiContext') as UIContext;
       if (!uiContext) {
         return;
       }
       this.rootNode = new BuilderNode(uiContext);
       this.rootNode.build(this.wrappedBuilder, { url: url, controller: controller });
     }
   }

   export const createNode = (wrappedBuilder: WrappedBuilder<BuilderData[]>, data: BuilderData) => {
     const baseNode = new NodeControllerImpl(wrappedBuilder, data.context);
     baseNode.initWeb(data.url, data.controller);
     return baseNode;
   }
   ```
3. 编写用于注入资源的组件代码，本例中的本地资源内容通过文件读取接口读取rawfile目录下的本地文件。

   ```typescript
   // main/ets/pages/InjectWebview.ets
   import { webview } from '@kit.ArkWeb';
   import { resourceConfigs } from './Resource';
   import { BuilderData } from './DynamicComponent';

   @Builder
   function webBuilder(data: BuilderData) {
     Web({ src: data.url, controller: data.controller })
       .onControllerAttached(async () => {
         try {
           data.controller.injectOfflineResources(await getData (data.context));
         } catch (err) {
           console.error('error: ' + err.code + ' ' + err.message);
         }
       })
       .fileAccess(true)
   }

   export const injectWebview = wrapBuilder<BuilderData[]>(webBuilder);

   export async function getData(context: UIContext) {
     const resourceMapArr: webview.OfflineResourceMap[] = [];

     // 读取配置，从rawfile目录中读取文件内容
     for (let config of resourceConfigs) {
       let buf: Uint8Array = new Uint8Array(0);
       if (config.localPath) {
         buf = await readRawFile(config.localPath, context);
       }

       resourceMapArr.push({
         urlList: config.urlList,
         resource: buf,
         responseHeaders: config.responseHeaders,
         type: config.type,
       })
     }

     return resourceMapArr;
   }

   export async function readRawFile(url: string, context: UIContext) {
     try {
       return await context.getHostContext()!.resourceManager.getRawFileContent(url);
     } catch (err) {
       return new Uint8Array(0);
     }
   }
   ```
4. 编写业务用组件代码。

   ```typescript
   // main/ets/pages/BusinessWebview.ets
   import { BuilderData } from './DynamicComponent';

   @Builder
   function webBuilder(data: BuilderData) {
     // 此处组件可根据业务需要自行扩展
     Web({ src: data.url, controller: data.controller })
       .cacheMode(CacheMode.Default)
   }

   export const businessWebview = wrapBuilder<BuilderData[]>(webBuilder);
   ```
5. 编写资源配置信息。

   ```typescript
   // main/ets/pages/Resource.ets
   import { webview } from '@kit.ArkWeb';

   export interface ResourceConfig {
     urlList: Array<string>,
     type: webview.OfflineResourceType,
     responseHeaders: Array<Header>,
     localPath: string, // 本地资源存放在rawfile目录下的路径
   }

   export const resourceConfigs: ResourceConfig[] = [
     {
       localPath: 'example.png',
       urlList: [
         'https://www.example.com/',
         'https://www.example.com/path1/example.png',
         'https://www.example.com/path2/example.png',
       ],
       type: webview.OfflineResourceType.IMAGE,
       responseHeaders: [
         { headerKey: 'Cache-Control', headerValue: 'max-age=1000' },
         { headerKey: 'Content-Type', headerValue: 'image/png' },
       ]
     },
     {
       localPath: 'example.js',
       urlList: [ // 仅提供一个url，这个url既作为资源的源，也作为资源的网络请求地址
         'https://www.example.com/example.js',
       ],
       type: webview.OfflineResourceType.CLASSIC_JS,
       responseHeaders: [
         // 以<script crossorigin='anonymous' />方式使用，提供额外的响应头
         { headerKey: 'Cross-Origin', headerValue:'anonymous' }
       ]
     },
   ];
   ```
6. 在页面中使用。

   ```typescript
   // main/ets/pages/Index.ets
   import { webview } from '@kit.ArkWeb';
   import { NodeController } from '@kit.ArkUI';
   import { createNode } from './DynamicComponent';
   import { injectWebview } from './InjectWebview';
   import { businessWebview } from './BusinessWebview';

   @Entry
   @Component
   struct Index {
     @State injectNode: NodeController | undefined = undefined;
     injectController: webview.WebviewController = new webview.WebviewController();

     @State businessNode: NodeController | undefined = undefined;
     businessController: webview.WebviewController = new webview.WebviewController();

     aboutToAppear(): void {
       // 初始化用于注入本地资源的Web组件, 提供一个空的html页面作为url即可
       this.injectNode = createNode(injectWebview,
         { url: 'https://www.example.com/empty.html', controller: this.injectController, context: this.getUIContext()});
     }

     build() {
       Column() {
         // 在适当的时机加载业务用Web组件，本例以Button点击触发为例
         Button('加载页面')
           .onClick(() => {
             this.businessNode = createNode(businessWebview, {
               url: 'https://www.example.com/business.html',
               controller: this.businessController,
               context: this.getUIContext()
             });
           })
         // 用于业务的Web组件
         NodeContainer(this.businessNode);
       }
     }
   }
   ```
7. 加载的HTML网页示例。

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head></head>
   <body>
     <img src="https://www.example.com/path1/request.png" />
     <img src="https://www.example.com/path2/request.png" />
     <script src="https://www.example.com/example.js" crossorigin="anonymous"></script>
   </body>
   </html>
   ```
