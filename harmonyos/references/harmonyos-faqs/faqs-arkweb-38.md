---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-38
title: Web组件对H5页面、常用框架VUE、React的页面支持情况，包括本地和网络端的页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件对H5页面、常用框架VUE、React的页面支持情况，包括本地和网络端的页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cabd1ef30143dbc752d8cbb8a8ef6277f226a9daee3007ba542d80ff153047a2
---

Web组件支持H5页面及常用框架Vue和React。

Web组件支持加载网络页面、本地页面和HTML文本数据。详情及代码示例请参考[使用Web组件加载页面](../harmonyos-guides/web-page-loading-with-web-components.md)。

加载Vue和React项目时，需先使用“npm run build”命令打包，再通过本地页面加载方式引入。如果上传到服务器，可以通过加载网络页面进行加载。

可参考以下示例代码：

1. 加载网络页面。

   ```ts
   // xxx.ets
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebComponent {
     webviewController: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Button('loadUrl').onClick(() => {
           try { // When the button is clicked, it redirects to www.example1.com via loadUrl
             this.webviewController.loadUrl('www.example1.com');
           } catch (error) {
             console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
           }
         })
         // When the component is created, load www.example.com 
         Web({ src: 'www.example.com', controller: this.webviewController })
       }
     }
   }
   ```
2. 加载本地页面时，[resource协议加载本地资源](../harmonyos-guides/web-page-loading-with-web-components.md#resource协议加载本地资源)：

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebComponent {
     webviewController: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Button('loadUrl')
           .onClick(() => {
             try {
               // When the button is clicked, load the local1.html file from the resources/rawfile directory via resource
               this.webviewController.loadUrl('resource://rawfile/local1.html');
             } catch (error) {
               console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
             }
           })
         // When creating the component, use the resource protocol to load the local file local.html
         Web({ src: 'resource://rawfile/local.html', controller: this.webviewController })
       }
     }
   }
   ```

   在“src/main/resources/rawfile”文件夹下创建local.html和local1.html。

   ```html
   <!-- local.html -->
   <!DOCTYPE html>
   <html>
   <body>
   <p>Hello World</p>
   </body>
   </html>
   ```

   ```html
   <!-- local1.html -->
   <!DOCTYPE html>
   <html>
   <body>
   <p>Hello World, local1.html</p>
   </body>
   </html>
   ```
3. 加载HTML格式的文本数据。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct WebComponent {
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Button('loadData')
           .onClick(() => {
             try {
               // When the button is clicked, load HTML-formatted text data using loadData
               this.controller.loadData(
                 "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
                 "text/html",
                 "UTF-8"
               );
             } catch (error) {
               console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
             }
           })
         // When the component is created, load www.example.com
         Web({ src: 'www.example.com', controller: this.controller })
       }
     }
   }
   ```
