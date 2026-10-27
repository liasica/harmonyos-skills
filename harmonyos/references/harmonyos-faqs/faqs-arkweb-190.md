---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-190
title: 如何解决Web组件设置Cookie属性无法生效的问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决Web组件设置Cookie属性无法生效的问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:08+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:4b05ee0c3af10c9e0af0b9fdffb8493fb984a17b7367b449b1f94ea157a74b50
---

## 问题现象

Web组件设置Cookie属性时无法生效，报错信息为：ErrorCode: 17100005, Message: Invalid cookie value。以设置过期时间为例。如下代码示例，把**expires=Fri, 13 Aug 2032 12:31:23 GMT** 改成 **expires=Sat, 13 Aug 2016 12:34:02 GMT**未生效。

设置代码示例如下：

```ts
let cookieData = 'A=B,path=/,expires=Sat, 13 Aug 2016 12:34:02 GMT,domain=.example.com,httponly,secure';
webview.WebCookieManager.configCookie('https://www.example.com', cookieData);
```

## 背景知识

* [fetchCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#fetchcookiesync11)：获取指定url对应Cookie的值。
  + 系统会自动清理过期的Cookie，对于同名key的数据，新数据将会覆盖前一个数据。
  + 为了获取可正常使用的Cookie值，fetchCookieSync需传入完整链接。
  + fetchCookieSync用于获取所有的Cookie值，每条Cookie值之间会通过;进行分隔，但无法单独获取某一条特定的Cookie值。
* [configCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)：为指定url设置单个Cookie的值。

## 解决方案

17100005错误码为Cookie设置的格式不符合规范，通过configCookieSync方法设置Cookie，Cookie的内容以;进行分割。若设置的Cookie时间已过期，则不会存储该Cookie，此时通过fetchCookieSync获取的Cookie值为空。代码示例如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct CookieGive {
  controller: webview.WebviewController = new webview.WebviewController();
  cookieData1 = 'A=B;path=/;expires=Fri,13 Aug 2032 12:31:23 GMT;domain=.example.com;httponly;secure;';
  cookieData2 = 'A=B;path=/;expires=Sat,13 Aug 2016 12:34:02 GMT;domain=.example.com;httponly;secure;';

  build() {
    Column() {
      Button('configCookieSync1')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookieSync('www.example.com', this.cookieData1);
            console.info('cookie ：configCookieSync1');
          } catch (error) {
          }
        });

      Button('configCookieSync2')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookieSync('www.example.com', this.cookieData2);
            console.info('cookie ：configCookieSync2');
          } catch (error) {
          }
        });

      Button('fetchCookieSync')
        .onClick(() => {
          try {
            let value = webview.WebCookieManager.fetchCookieSync('www.example.com');
            console.info('cookie ：fetchCookieSync cookie = ' + value);
          } catch (error) {
          }
        });
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false);
    };

  }
}
```

其中关键步骤是：

1. 首先点击configCookieSync1后再通过fetchCookieSync获取Cookie，日志如下则说明Cookie设置成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/jF0yTzyfQhetZdJeMIRhPw/zh-cn_image_0000002659138443.png "点击放大")
2. 然后点击configCookieSync2后再通过fetchCookieSync获取Cookie，日志如下则说明Cookie清除成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/-6PInVITTS-Yered_HWGsQ/zh-cn_image_0000002629059100.png "点击放大")

## 常见FAQ

Q：可以设置多个Cookie吗？

A：如果需要设置多个Cookie，可以多次调用[configCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync14)方法，每次仅能设置一个键值对。

Q：设置多个Cookie后，通过fetchCookieSync接口获取所有的Cookie值，分隔每个Cookie值的分号后面有空格吗？

A：有空格，Cookie的键值对以;进行分隔。

Q：Web组件已通过configCookieSync设置好Cookie里的token值，但是有些token服务端从Cookie里为什么获取不到？

A：需要客户端设置的域名和服务端获取的域名一致才能获取。

Q：Cookie的存储路径支持修改吗？

A：Cookie信息存储在应用沙箱路径下/proc/{pid}/root/data/storage/el2/base/cache/web/Cookie，且不支持修改。

Q：uni-app框架无法使用void plus.navigator.setCookie(url, value)设置Cookie如何解决？

A：HarmonyOS开发uni-app目前不支持plus。可以通过uni.getElementById('web-view') as UniWebViewElement得到Webview，再通过调用Webview的evalJS函数执行JS来设置。
