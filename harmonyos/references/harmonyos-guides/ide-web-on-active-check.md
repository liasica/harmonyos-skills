---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-web-on-active-check
title: @performance/web-on-active-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/web-on-active-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:20+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:88847b3dddcc4c6739b4b5cb7051a17a477ad302d968b485c5825e17814b8026
---

使用了Web预渲染技术的应用，建议在预渲染完成后（onFirstMeaningfulPaint），调用停止渲染接口（onInactive）。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/web-on-active-check": "warn",
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
11. struct WebComponent {
12. controller: webview.WebviewController = new webview.WebviewController();
13. @State mode: CacheMode = CacheMode.None;
14. configs: Array<Config> = [
15. {
16. url: 'https://www.example.com/example.js',
17. localPath: 'example.js',
18. options: {
19. responseHeaders: [
20. { headerKey: 'E-Tag', headerValue: 'xxx' },
21. { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
22. ]
23. }
24. }
25. ]

27. build() {
28. Column() {
29. Web({ src: 'www.example.com', controller: this.controller })
30. .onPageBegin(() => {
31. this.controller.onActive();
32. })
33. // 预渲染完成后（onFirstMeaningfulPaint）
34. .onFirstMeaningfulPaint(() => {
35. // 调用停止渲染接口（onInactive）
36. this.controller.onInactive();
37. })
38. .cacheMode(this.mode)
39. .onControllerAttached(async () => {
40. for (const config of this.configs) {
41. const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
42. let content = resourceMgr?.getRawFileContentSync(config.localPath);
43. try {
44. this.controller.precompileJavaScript(config.url, content, config.options)
45. .then((errCode: number) => {
46. console.log('precompile successfully!');
47. }).catch((errCode: number) => {
48. console.error('precompile failed.' + errCode);
49. })
50. } catch (err) {
51. console.error('precompile failed!.' + err.code + err.message);
52. }
53. }
54. })
55. }
56. }
57. }
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
11. struct WebComponent {
12. controller: webview.WebviewController = new webview.WebviewController();
13. @State mode: CacheMode = CacheMode.Default;
14. configs: Array<Config> = [
15. {
16. url: 'https://www.example.com/example.js',
17. localPath: 'example.js',
18. options: {
19. responseHeaders: [
20. { headerKey: 'E-Tag', headerValue: 'xxx' },
21. { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
22. ]
23. }
24. }
25. ]

27. build() {
28. Column() {
29. // web中没有onFirstMeaningfulPaint属性，告警
30. Web({ src: 'www.example.com', controller: this.controller })
31. .cacheMode(this.mode)
32. .onPageBegin(() => {
33. this.controller.onActive();
34. })
35. .onControllerAttached(async () => {
36. for (const config of this.configs) {
37. const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
38. let content = resourceMgr?.getRawFileContentSync(config.localPath);
39. try {
40. this.controller.precompileJavaScript(config.url, content, config.options)
41. .then((errCode: number) => {
42. console.log('precompile successfully!');
43. }).catch((errCode: number) => {
44. console.error('precompile failed.' + errCode);
45. })
46. } catch (err) {
47. console.error('precompile failed!.' + err.code + err.message);
48. }
49. }
50. })
51. }
52. }
53. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
