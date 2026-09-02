---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-164
title: ArkWeb如何根据异步请求返回数据加载真实Url页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > ArkWeb如何根据异步请求返回数据加载真实Url页面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4ea04cfab3466df4965f950e11f833836a465dfb253538bc0c8d674139e6f2f1
---

## 问题现象

ArkWeb首次加载的URL默认为空字符串，真正要加载的地址是通过接口获取到地址，当接口返回真实的URL后，怎么可以让已经创建的ArkWeb组件再次加载这个URL呢？

## 背景知识

* [loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)：加载指定的URL。
* [onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)：当Controller成功绑定到Web组件时触发该回调，并且该Controller必须为WebviewController，且禁止在该事件回调前调用Web组件相关的接口，否则会抛出js-error异常。

## 解决方案

当接口返回真实的URL后，可以调用loadUrl完成页面加载。

代码示例如下：

```ts
import { webview } from '@kit.ArkWeb';
import { http } from '@kit.NetworkKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: '', controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false)
        .onControllerAttached(() => {
          let httpRequest = http.createHttp();
          httpRequest.request('EXAMPLE_URL', (err: Error, data: http.HttpResponse) => { // 需要替换网址才可运行
            if (!err) {
              try {
                this.controller.loadUrl(data.result.toString()); // 根据请求返回类型自行处理数据, 接口返回URL链接, 需要替换网址才可运行
              } catch (error) {
                console.error(`err${JSON.stringify(err)}`);
              }
            } else {
              console.error(`err${JSON.stringify(err)}`);
            }
          });
        });
    };
  }
}
```

**须知** 

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

## 常见FAQ

Q：Web组件网页资源地址src用@State或@Prop修饰时，无法动态刷新。

A：不能通过状态变量动态更改src，如需更改，可在[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)回调中通过[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)重新加载。
