---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-js-code-cache-by-interception-check
title: @performance/js-code-cache-by-interception-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/js-code-cache-by-interception-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3658147a8353cddfa17ec05dd9f596170dea317a678b35d042ea9b9932886ec
---

在资源拦截场景下，建议生成JavaScript字节码缓存，可以降低Web页面非首次的加载时间。

[Web完成时延](../best-practices/bpta-web-develop-optimization.md#section1495115588211)场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/js-code-cache-by-interception-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { webview } from '@kit.ArkWeb';
2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct JsCodeCacheByInterceptionCheckNoReport0 {
7. controller: webview.WebviewController = new webview.WebviewController();
8. responseResource: WebResourceResponse = new WebResourceResponse();
9. jsData: string = 'JavaScript Data';

11. build() {
12. Column() {
13. Web({ src: $rawfile('index.html'), controller: this.controller })
14. .onControllerAttached(async () => {
15. for (const config of this.configs) {
16. const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
17. let content = resourceMgr?.getRawFileContentSync(config.localPath);
18. try {
19. this.controller.precompileJavaScript(config.url, content, config.options)
20. .then((errCode: number) => {
21. console.log('precompile successfully!');
22. }).catch((errCode: number) => {
23. console.error('precompile failed.' + errCode);
24. })
25. } catch (err) {
26. console.error('precompile failed!.' + err.code + err.message);
27. }
28. }
29. })
30. .onInterceptRequest((event) => {
31. if (event?.request.getRequestUrl() === 'https://www.example.com/test.js') {
32. this.responseResource.setResponseHeader([
33. {
34. headerKey: 'ResponseDataID',
35. headerValue: '0000000000001'
36. }
37. ]);
38. this.responseResource.setResponseData(this.jsData);
39. this.responseResource.setResponseEncoding('utf-8');
40. this.responseResource.setResponseMimeType('application/javascript');
41. this.responseResource.setResponseCode(200);
42. this.responseResource.setReasonMessage('OK');
43. return this.responseResource;
44. }
45. return null;
46. })
47. .onPageBegin(() => {
48. hiTraceMeter.startTrace('getMessageData', 0);
49. })
50. .onPageEnd(() => {
51. hiTraceMeter.finishTrace('getMessageData', 0);
52. })
53. }
54. }

56. configs: Array<Config> = [
57. {
58. url: 'https://www.example.com/example.js',
59. localPath: 'example.js',
60. options: {
61. responseHeaders: [
62. { headerKey: 'E-Tag', headerValue: 'xxx' },
63. { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
64. ]
65. }
66. }
67. ]
68. }

70. interface Config {
71. url: string,
72. localPath: string,
73. options: webview.CacheOptions
74. }
```

## 反例

拦截请求中未设置ResponseDataID或者自定义协议中isCodeCacheSupported设置为false，均不会生成字节码缓存。

**示例1**：

```
1. // Example without a custom protocol and without setting ResponseDataID in the header
2. import { webview } from '@kit.ArkWeb';
3. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
4. @Entry
5. @Component
6. struct JsCodeCacheByInterceptionCheckReport0 {
7. controller: webview.WebviewController = new webview.WebviewController();
8. responseResource: WebResourceResponse = new WebResourceResponse();
9. jsData: string = 'JavaScript Data';
10. build() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .onPageBegin(() => {
14. hiTraceMeter.startTrace('getMessageData', 0);
15. })
16. // warning line
17. .onInterceptRequest(event => {
18. if (event?.request.getRequestUrl() === 'https://www.example.com/test.js') {
19. this.responseResource.setResponseData(this.jsData);
20. this.responseResource.setResponseEncoding('utf-8');
21. this.responseResource.setResponseMimeType('application/javascript');
22. this.responseResource.setResponseCode(200);
23. this.responseResource.setReasonMessage('OK');
24. return this.responseResource;
25. }
26. return null;
27. })
28. .onControllerAttached(async () => {
29. this.controller.precompileJavaScript('', 'content', null)
30. .then((errCode: number) => {
31. console.log('precompile successfully!' );
32. }).catch((errCode: number) => {
33. console.error('precompile failed.' + errCode);
34. })
35. })
36. .onPageEnd(() => {
37. hiTraceMeter.finishTrace('getMessageData', 0);
38. })
39. }
40. .width('100%')
41. }
42. }
```

**示例2**：

```
1. // Example with a custom protocol and with isCodeCacheSupported set to false
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. @Entry
5. @Component
6. struct JsCodeCacheByInterceptionCheckReport2 {
7. // warning line
8. scheme2: webview.WebCustomScheme = { schemeName: "scheme2", isSupportCORS: true, isSupportFetch: true, isCodeCacheSupported: false }
9. webController: webview.WebviewController = new webview.WebviewController();
10. jsData: string = 'JavaScript Data';
11. aboutToAppear(): void {
12. try {
13. webview.WebviewController.customizeSchemes([this.scheme2])
14. } catch (error) {
15. let e: BusinessError = error as BusinessError;
16. console.error(`ErrorCode: ${e.code},  Message: ${e.message}`);
17. }
18. }
19. build() {
20. Column() {
21. Web({
22. src: $rawfile('index2.html'),
23. controller: this.webController
24. })
25. .fileAccess(true)
26. .javaScriptAccess(true)
27. .width('100%')
28. .height('100%')
29. .onConsole((event) => {
30. console.log('ets onConsole:' + event?.message.getMessage());
31. return false
32. })
33. .onInterceptRequest((event) => {
34. if (event?.request.getRequestUrl() === 'scheme2://www.intercept.com/test-cc2.js') {
35. let responseResource = new WebResourceResponse();
36. responseResource.setResponseHeader([
37. {
38. headerKey: 'ResponseDataID',
39. headerValue: '0000000000002'
40. }]);
41. responseResource.setResponseData(this.jsData);
42. responseResource.setResponseEncoding('utf-8');
43. responseResource.setResponseMimeType('application/javascript');
44. responseResource.setResponseCode(200);
45. responseResource.setReasonMessage('OK');
46. return responseResource;
47. }
48. return null;
49. })
50. .onControllerAttached(async () => {
51. this.webController.precompileJavaScript('', 'content', null)
52. .then((errCode: number) => {
53. console.log('precompile successfully!' );
54. }).catch((errCode: number) => {
55. console.error('precompile failed.' + errCode);
56. })
57. })
58. }
59. }
60. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
