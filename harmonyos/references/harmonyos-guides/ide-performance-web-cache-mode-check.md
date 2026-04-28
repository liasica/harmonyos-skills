---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-performance-web-cache-mode-check
title: @performance/web-cache-mode-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/web-cache-mode-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:19+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d93767b55cd2b4385560a571b7ba4ef8d207a993a9f9142de022d29a5a210207
---

web组件的cacheMode属性参数不建议设置为Online。

Web完成时延场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/web-cache-mode-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { webview } from '@kit.ArkWeb';

3. interface Config {
4. url: string,
5. localPath: string,
6. options: webview.CacheOptions
7. }

9. @Entry
10. @Component
11. struct WebCacheModeNoReport {
12. controller: webview.WebviewController = new webview.WebviewController();
13. configs: Array<Config> = [
14. {
15. url: 'https://www.example.com/example.js',
16. localPath: 'example.js',
17. options: {
18. responseHeaders: [
19. { headerKey: 'E-Tag', headerValue: 'xxx' },
20. { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
21. ]
22. }
23. }
24. ]

26. build() {
27. Column() {
28. Web({ src: 'https://www.example.com/a.html', controller: this.controller })
29. .onControllerAttached(async () => {
30. for (const config of this.configs) {
31. const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
32. let content = resourceMgr?.getRawFileContentSync(config.localPath);
33. try {
34. this.controller.precompileJavaScript(config.url, content, config.options)
35. .then((errCode: number) => {
36. console.log('precompile successfully!');
37. }).catch((errCode: number) => {
38. console.error('precompile failed.' + errCode);
39. })
40. } catch (err) {
41. console.error('precompile failed!.' + err.code + err.message);
42. }
43. }
44. })
45. .onAppear(() => {
46. webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 120);
47. })
48. .cacheMode(CacheMode.Default)
49. }
50. }
51. }
```

## 反例

```
1. import { webview } from '@kit.ArkWeb';

3. interface Config {
4. url: string,
5. localPath: string,
6. options: webview.CacheOptions
7. }

9. @Entry
10. @Component
11. struct WebCacheModeNoReport {
12. controller: webview.WebviewController = new webview.WebviewController();
13. configs: Array<Config> = [
14. {
15. url: 'https://www.example.com/example.js',
16. localPath: 'example.js',
17. options: {
18. responseHeaders: [
19. { headerKey: 'E-Tag', headerValue: 'xxx' },
20. { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
21. ]
22. }
23. }
24. ]

26. build() {
27. Column() {
28. Web({ src: 'https://www.example.com/a.html', controller: this.controller })
29. .onControllerAttached(async () => {
30. for (const config of this.configs) {
31. const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
32. let content = resourceMgr?.getRawFileContentSync(config.localPath);
33. try {
34. this.controller.precompileJavaScript(config.url, content, config.options)
35. .then((errCode: number) => {
36. console.log('precompile successfully!');
37. }).catch((errCode: number) => {
38. console.error('precompile failed.' + errCode);
39. })
40. } catch (err) {
41. console.error('precompile failed!.' + err.code + err.message);
42. }
43. }
44. })
45. .onAppear(() => {
46. webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 120);
47. })
48. // warning
49. .cacheMode(CacheMode.Online)
50. }
51. }
52. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
