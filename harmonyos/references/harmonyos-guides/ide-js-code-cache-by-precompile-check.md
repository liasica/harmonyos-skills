---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-js-code-cache-by-precompile-check
title: "@performance/js-code-cache-by-precompile-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/js-code-cache-by-precompile-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:00145dee7acc3f0b9c203d9407340e4f36c0692f7ca7e049b3242c88d8704e2c
---

建议通过预编译生成JavaScript字节码缓存，可以降低Web页面第一次和第二次的加载时间。

[Web完成时延](../best-practices/bpta-web-develop-optimization.md#section563844632917)场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/js-code-cache-by-precompile-check": "suggestion",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
import { webview } from '@kit.ArkWeb';
interface Config {
  url: string,
  localPath: string,
  options: webview.CacheOptions
}
@Entry
@Component
struct JsCodeCacheByPrecompileCheckNoReport {
  controller: webview.WebviewController = new webview.WebviewController();
  configs: Array<Config> = [
    {
      url: 'https://www.example.com/example.js',
      localPath: 'example.js',
      options: {
        responseHeaders: [
          { headerKey: 'E-Tag', headerValue: 'xxx' },
          { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
        ]
      }
    }
  ]
  build() {
    Column() {
      Web({ src: 'https://www.example.com/a.html', controller: this.controller })
        .onControllerAttached(async () => {
          for (const config of this.configs) {
            let content = getContext().resourceManager.getRawFileContentSync(config.localPath);
            try {
              this.controller.precompileJavaScript(config.url, content, config.options)
                .then((errCode: number) => {
                  console.log('precompile successfully!' );
                }).catch((errCode: number) => {
                console.error('precompile failed.' + errCode);
              })
            } catch (err) {
              console.error('precompile failed!.' + err.code + err.message);
            }
          }
        })
    }
  }
}
```

## 反例

```screen
import { webview } from '@kit.ArkWeb';
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct JsCodeCacheByPrecompileCheckReport {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Button('加载页面')
        .onClick(() => {
          hiTraceMeter.startTrace('unPrecompileJavaScript', 1);
          this.controller.loadUrl('https://www.example.com/b.html');
        })
      // warning line
      Web({ src: 'https://www.example.com/a.html', controller: this.controller })
        .fileAccess(true)
        .onPageBegin((event) => {
          console.log(`load page begin: ${event?.url}`);
        })
        .onPageEnd((event) => {
          hiTraceMeter.finishTrace('unPrecompileJavaScript', 1);
          console.log(`load page end: ${event?.url}`);
        })
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
