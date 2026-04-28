---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-38
title: Web组件对H5页面、常用框架VUE、React的页面支持情况，包括本地和网络端的页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件对H5页面、常用框架VUE、React的页面支持情况，包括本地和网络端的页面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cff7438f1fa9809eb8702d37da65bc8c0d15ab741d1c0ab104c8b06bace49398
---

Web组件支持H5页面及常用框架Vue和React。

Web组件支持加载网络页面、本地页面和HTML文本数据。详情及代码示例请参考[使用Web组件加载页面](../harmonyos-guides/web-page-loading-with-web-components.md)。

加载Vue和React项目时，需先使用“npm run build”命令打包，再通过本地页面加载方式引入。如果上传到服务器，可以通过加载网络页面进行加载。

可参考以下示例代码：

1. 加载网络页面。

   ```
   1. // xxx.ets
   2. import { webview } from '@kit.ArkWeb';

   4. @Entry
   5. @Component
   6. struct WebComponent {
   7. webviewController: webview.WebviewController = new webview.WebviewController();

   9. build() {
   10. Column() {
   11. Button('loadUrl').onClick(() => {
   12. try { // When the button is clicked, it redirects to www.example1.com via loadUrl
   13. this.webviewController.loadUrl('www.example1.com');
   14. } catch (error) {
   15. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
   16. }
   17. })
   18. // When the component is created, load www.example.com
   19. Web({ src: 'www.example.com', controller: this.webviewController })
   20. }
   21. }
   22. }
   ```

   [SupportVue.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/SupportVue.ets#L21-L42)
2. 加载本地页面时，[resource协议加载本地资源](../harmonyos-guides/web-page-loading-with-web-components.md#resource协议加载本地资源)：

   ```
   1. import { webview } from '@kit.ArkWeb';

   3. @Entry
   4. @Component
   5. struct WebComponent {
   6. webviewController: webview.WebviewController = new webview.WebviewController();

   8. build() {
   9. Column() {
   10. Button('loadUrl')
   11. .onClick(() => {
   12. try {
   13. // When the button is clicked, load the local1.html file from the resources/rawfile directory via resource
   14. this.webviewController.loadUrl('resource://rawfile/local1.html');
   15. } catch (error) {
   16. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
   17. }
   18. })
   19. // When creating the component, use the resource protocol to load the local file local.html
   20. Web({ src: 'resource://rawfile/local.html', controller: this.webviewController })
   21. }
   22. }
   23. }
   ```

   [SupportVue2.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/SupportVue2.ets#L21-L43)

   在“src/main/resources/rawfile”文件夹下创建local.html和local1.html。

   ```
   1. <!-- local.html -->
   2. <!DOCTYPE html>
   3. <html>
   4. <body>
   5. <p>Hello World</p>
   6. </body>
   7. </html>
   ```

   [local.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/local.html#L8-L14)

   ```
   1. <!-- local1.html -->
   2. <!DOCTYPE html>
   3. <html>
   4. <body>
   5. <p>Hello World, local1.html</p>
   6. </body>
   7. </html>
   ```

   [local1.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/local1.html#L7-L13)
3. 加载HTML格式的文本数据。

   ```
   1. import { webview } from '@kit.ArkWeb';

   3. @Entry
   4. @Component
   5. struct WebComponent {
   6. controller: webview.WebviewController = new webview.WebviewController();

   8. build() {
   9. Column() {
   10. Button('loadData')
   11. .onClick(() => {
   12. try {
   13. // When the button is clicked, load HTML-formatted text data using loadData
   14. this.controller.loadData(
   15. "<html><body bgcolor=\"white\">Source:<pre>source</pre></body></html>",
   16. "text/html",
   17. "UTF-8"
   18. );
   19. } catch (error) {
   20. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
   21. }
   22. })
   23. // When the component is created, load www.example.com
   24. Web({ src: 'www.example.com', controller: this.controller })
   25. }
   26. }
   27. }
   ```

   [SupportVue3.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/SupportVue3.ets#L21-L47)
