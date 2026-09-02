---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-web-on-active-check
title: "@performance/web-on-active-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/web-on-active-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:60c612ccefc7ffeb1eca787b1fc063c2f830d0dd3f8474bd387e5c34e0b8b448
---

使用了Web预渲染技术的应用，建议在预渲染完成后（onFirstMeaningfulPaint），调用停止渲染接口（onInactive）。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/web-on-active-check": "warn",
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
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: CacheMode = CacheMode.None;
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
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageBegin(() => {
          this.controller.onActive();
        })
        // 预渲染完成后（onFirstMeaningfulPaint）
        .onFirstMeaningfulPaint(() => {
          // 调用停止渲染接口（onInactive）
          this.controller.onInactive();
        })
        .cacheMode(this.mode)
        .onControllerAttached(async () => {
          for (const config of this.configs) {
            const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
            let content = resourceMgr?.getRawFileContentSync(config.localPath);
            try {
              this.controller.precompileJavaScript(config.url, content, config.options)
                .then((errCode: number) => {
                  console.log('precompile successfully!');
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

interface Config {
  url: string,
  localPath: string,
  options: webview.CacheOptions
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: CacheMode = CacheMode.Default;
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
      // web中没有onFirstMeaningfulPaint属性，告警
      Web({ src: 'www.example.com', controller: this.controller })
        .cacheMode(this.mode)
        .onPageBegin(() => {
          this.controller.onActive();
        })
        .onControllerAttached(async () => {
          for (const config of this.configs) {
            const resourceMgr = this.getUIContext()?.getHostContext()?.resourceManager;
            let content = resourceMgr?.getRawFileContentSync(config.localPath);
            try {
              this.controller.precompileJavaScript(config.url, content, config.options)
                .then((errCode: number) => {
                  console.log('precompile successfully!');
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

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
