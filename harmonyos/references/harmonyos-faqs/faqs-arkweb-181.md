---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-181
title: Web组件如何清除缓存信息
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何清除缓存信息
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:50214315b1359b1d1a5c5b87c4df2a97b6d3f5a4c332cf78eb1c329d62a2da40
---

## 问题现象

Web组件在加载网页时，会产生多种缓存数据，如Cache，Cookie还有DOM Storage，要如何清除它们？

## 背景知识

* [缓存与存储管理](../harmonyos-guides/web-cookie-and-data-storage-mgmt.md#缓存与存储管理)：在访问网站时，网络资源请求通常需要较长的时间。开发者可以通过Cache和DOM Storage等手段将资源保存到本地，以提高访问同一网站的速度。
* [removeCache](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#removecache)：清除应用中的资源缓存文件，对应目录为data/storage/el2/base/cache/web/Cache目录。
* [removeAllCache](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#removeallcache18)：清除应用中的资源缓存文件，对应目录为data/storage/el2/base/cache/web目录。
* [clearAllCookiesSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#clearallcookiessync11)：清除所有Cookie信息。
* [deleteAllData](../harmonyos-references/arkts-apis-webview-webstorage.md#deletealldata)：清除被JavaScript存储API使用的所有存储数据，这包括Web SQL数据库和HTML5支持的Web存储API。

## 解决方案

场景一：清除Web的缓存Cache信息，对应存储目录data/storage/el2/base/cache/web。

1. 方法一：使用实例接口removeCache，清除应用中data/storage/el2/base/cache/web/Cache目录下所有的资源缓存文件，需要创建WebviewController实例对象之后调用。

   ```screen
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct WebComponent {
     // url需替换为真实路径
     url: string | Resource = 'xxxx';
     mode: CacheMode = CacheMode.None;
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Button('removeCache')
           .onClick(() => {
             try {
               // 设置为true时同时清除ROM和RAM中的缓存，设置为false时只清除RAM中的缓存
               this.controller.removeCache(true);
             } catch (error) {
               console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
             }
           });
         Web({ src: this.url, controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
           .cacheMode(this.mode);
       };
     }
   }
   ```
2. 方法二：API18及以上版本可以使用静态接口removeAllCache，清除应用中data/storage/el2/base/cache/web目录中所有的缓存文件，Web组件未初始化时也可调用。

   ```screen
   // xxx.ets
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct WebComponent {
     // url需替换为真实路径
     url: string | Resource = 'xxxx';
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Button('removeAllCache')
           .onClick(() => {
             try {
               webview.WebviewController.removeAllCache(true);
             } catch (error) {
               console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
             }
           });
         Web({ src: this.url, controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false);
       };
     }
   }
   ```

场景二：清除Web的缓存的Cookie信息，可使用clearAllCookiesSync方法进行清除，对应存储目录data/storage/el2/base/cache/web/Cookies。

```screen
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  // url需替换为真实路径
  url: string | Resource = 'xxxx';
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('clearAllCookiesSync')
        .onClick(() => {
          webview.WebCookieManager.clearAllCookiesSync();
        })
      Web({ src: this.url, controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false)
    }
  }
}
```

**说明** 

[clearSessionCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#clearsessioncookiesync11)函数仅用于清除会话Cookie，即那些未设置max-age或expires属性、在浏览器会话结束时自动失效的Cookie。对于设置了过期时间的持久化Cookie，该函数不会进行任何操作，从而确保不会误删长期有效的数据。

场景三：清除DOM Storage（Session Storage + Local Storage）信息，可使用webview.WebStorage.deleteAllData进行清除。

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  // url需替换为真实路径
  url: string | Resource = 'xxxx';
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('deleteAllData')
        .onClick(() => {
          try {
            webview.WebStorage.deleteAllData();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: this.url, controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false)
    }
  }
}
```

针对以上三种场景，除了以上提供的方法外，还可以通过文件管理方式，删除文件夹，达到清除应用Web缓存目的，以'data/storage/el2/base/cache/web/Cache'为例：

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  // url需替换为真实路径
  url: string | Resource = 'xxxx';
  controller: webview.WebviewController = new webview.WebviewController();

  deleteCache(): void {
    let dirPath = 'data/storage/el2/base/cache/web/Cache';
    fs.rmdir(dirPath).then(() => {
      console.info('rmdir succeed');
    }).catch((err: BusinessError) => {
      console.error(`rmdir failed with error message: ${err.message}, error code: ${err.code}`);
    });
  }

  build() {
    Column() {
      Button('删除缓存文件夹')
        .onClick(() => {
          this.deleteCache();
        });
      Web({ src: this.url, controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false);
    }.width('100%')
    .height('100%');
  }
}
```

上述提供了Web组件API清除缓存接口，以及文件管理清除缓存方式，建议使用Web提供接口触发清除缓存，不建议使用手动删除目录方式。

## 常见FAQ

Q：Web组件的removeCache和removeAllCache在清除资源优化上有什么区别？

A：removeCache是一个实例方法，作用范围仅清除当前Web组件实例的缓存，需创建WebviewController实例，而removeAllCache是一个静态方法，作用范围是清除整个应用内所有Web组件的缓存，无需初始化Web组件即可调用。

Q：Web组件的removeCache和removeAllCache能否清除localStorage？

A：removeCache和removeAllCache无法清除localStorage，它的清除由JavaScript垃圾回收自动处理，可通过使用webview.WebStorage.deleteAllData或runJavaScript调用前端代码实现清除功能。
