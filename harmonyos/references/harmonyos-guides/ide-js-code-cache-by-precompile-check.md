---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-js-code-cache-by-precompile-check
title: @performance/js-code-cache-by-precompile-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/js-code-cache-by-precompile-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:14+08:00
doc_updated_at: 2026-03-24
content_hash: sha256:bb73904ea586d9109fcd1821ea9b9e5e16508275954024cc2c67228c98e51842
---

建议通过预编译生成JavaScript字节码缓存，可以降低Web页面第一次和第二次的加载时间。

[Web完成时延](../best-practices/bpta-web-develop-optimization.md#section563844632917)场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/js-code-cache-by-precompile-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { webview } from '@kit.ArkWeb';
2. interface Config {
3. url: string,
4. localPath: string,
5. options: webview.CacheOptions
6. }
7. @Entry
8. @Component
9. struct JsCodeCacheByPrecompileCheckNoReport {
10. controller: webview.WebviewController = new webview.WebviewController();
11. configs: Array<Config> = [
12. {
13. url: 'https://www.example.com/example.js',
14. localPath: 'example.js',
15. options: {
16. responseHeaders: [
17. { headerKey: 'E-Tag', headerValue: 'xxx' },
18. { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
19. ]
20. }
21. }
22. ]
23. build() {
24. Column() {
25. Web({ src: 'https://www.example.com/a.html', controller: this.controller })
26. .onControllerAttached(async () => {
27. for (const config of this.configs) {
28. let content = getContext().resourceManager.getRawFileContentSync(config.localPath);
29. try {
30. this.controller.precompileJavaScript(config.url, content, config.options)
31. .then((errCode: number) => {
32. console.log('precompile successfully!' );
33. }).catch((errCode: number) => {
34. console.error('precompile failed.' + errCode);
35. })
36. } catch (err) {
37. console.error('precompile failed!.' + err.code + err.message);
38. }
39. }
40. })
41. }
42. }
43. }
```

## 反例

```
1. import { webview } from '@kit.ArkWeb';
2. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
3. @Entry
4. @Component
5. struct JsCodeCacheByPrecompileCheckReport {
6. controller: webview.WebviewController = new webview.WebviewController();
7. build() {
8. Column() {
9. Button('加载页面')
10. .onClick(() => {
11. hiTraceMeter.startTrace('unPrecompileJavaScript', 1);
12. this.controller.loadUrl('https://www.example.com/b.html');
13. })
14. // warning line
15. Web({ src: 'https://www.example.com/a.html', controller: this.controller })
16. .fileAccess(true)
17. .onPageBegin((event) => {
18. console.log(`load page begin: ${event?.url}`);
19. })
20. .onPageEnd((event) => {
21. hiTraceMeter.finishTrace('unPrecompileJavaScript', 1);
22. console.log(`load page end: ${event?.url}`);
23. })
24. }
25. }
26. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
