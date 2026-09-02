---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-performance-web-cache-mode-check
title: "@performance/web-cache-mode-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/web-cache-mode-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d22b755e6bf12529755946872bc32175f4e457979692ce32a6c7c1b1d158f996
---

web组件的cacheMode属性参数不建议设置为Online。

Web完成时延场景下，建议优先修改。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/web-cache-mode-check": "suggestion",
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
struct WebCacheModeNoReport {
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
        .onAppear(() => {
          webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 120);
        })
        .cacheMode(CacheMode.Default)
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
struct WebCacheModeNoReport {
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
        .onAppear(() => {
          webview.WebviewController.prepareForPageLoad('https://www.example.com/', true, 120);
        })
        // warning
        .cacheMode(CacheMode.Online)
    }
  }
}
```

## 规则集

```screen
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
