---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webstorage
title: Class (WebStorage)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebStorage)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b6b96e37af92ea19432a341bdd4913314a6977af7b578fba956e20dd13d24f58
---

通过WebStorage可管理Web SQL数据库接口和HTML5 Web存储接口，每个应用中的所有Web组件共享一个WebStorage。

## 概述

WebStorage提供对Web存储数据的管理能力，包括Web SQL数据库和HTML5 Web存储API，主要解决以下问题：

* 跨Web组件的数据存储管理。
* 存储空间配额和使用量的查询。
* 存储数据的清理。

### 基本概念

* **源（Origin）**：Web存储的数据隔离单位，相同源下的页面可以共享存储数据。
* **配额（Quota）**：每个源允许使用的最大存储空间，以字节为单位。
* **使用量（Usage）**：每个源当前已使用的存储空间，以字节为单位。

### 关键设计

WebStorage采用统一管理的设计模式：

1. 每个应用中的所有Web组件共享一个WebStorage实例。
2. 通过源（origin）作为索引来区分和管理不同源的存储数据。
3. 支持同步和异步两种方式访问存储数据。
4. 支持隐私模式和非隐私模式下的数据分离管理。

### 使用示例

```ts
import { webview } from '@kit.ArkWeb';

// 获取所有源的信息
webview.WebStorage.getOrigins((error, origins) => {
  if (!error) {
    origins.forEach(origin => {
      console.info(`Origin: ${origin.origin}, Usage: ${origin.usage}, Quota: ${origin.quota}`);
    });
  }
});

// 清除指定源的存储
webview.WebStorage.deleteOrigin('https://example.com');
```

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。
* 目前调用WebStorage下的方法，都需要先加载Web组件。
* 本Class下的接口在ArkWeb内核升级到M132版本后因内核废弃Web SQL，对Web SQL数据库的管理失效。ArkWeb内核版本参考ArkWeb简介[约束与限制](../harmonyos-guides/web-component-overview.md#约束与限制)。

## 导入模块

```ts
import { webview } from '@kit.ArkWeb';
```

## deleteOrigin

static deleteOrigin(origin: string): void

清除指定源所使用的存储。

**方法调用关系：**

* origin参数应从getOrigins()方法获取。
* 建议先调用getOrigins()获取源列表，再调用deleteOrigin()清除指定源存储。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引，来自于[getOrigins](arkts-apis-webview-webstorage.md#getorigins)。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('deleteOrigin')
        .onClick(() => {
          try {
            webview.WebStorage.deleteOrigin(this.origin);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件。

```html
 <!-- index.html -->
 <!DOCTYPE html>
 <html>
 <head>
   <meta charset="UTF-8">
   <title>test</title>
   <script type="text/javascript">

       // 打开或创建数据库
       var request = indexedDB.open('myDatabase', 1);

       // 如果数据库版本变化或首次创建时触发
       request.onupgradeneeded = function(event) {
           var db = event.target.result;

           // 创建对象存储（表），设置主键为‘id’
           var objectStore = db.createObjectStore('customers', { keyPath: 'id' });

           // 为‘name’创建索引
           objectStore.createIndex('name', 'name', { unique: false });
       };

       // 打开数据库成功时的回调
       request.onsuccess = function(event) {
           var db = event.target.result;

           const customerData = [
               {id: 1, name: 'John Doe', email: 'john@example.com'},
               {id: 2, name: 'John Doe', email: 'john@example.com'},
           ]

           // 插入数据
           var transaction = db.transaction('customers', 'readwrite');
           var objectStore = transaction.objectStore('customers');

           customerData.forEach((customer) => {
               objectStore.add(customer);
           });

           transaction.oncomplete = function () {
               console.info('Transaction completed: data added');
           }
           
           transaction.onerror = function (event) {
               console.error("Transaction failed", event);
           }
           
           // 查询数据
           var queryTransaction = db.transaction(['customers']);
           var queryObjectStore = queryTransaction.objectStore('customers');
           var query = queryObjectStore.get(2);
           
           query.onsuccess = function (event) {
               console.info('query succ');
               console.info('Customer:', event.target.result);
               console.info('Customer id:', event.target.result.id);
               console.info('Customer name:', event.target.result.name);
               console.info('Customer email:', event.target.result.email);
           };
           
           queryObjectStore.openCursor().onsuccess = (event) => {
               const cursor = event.target.result;
               if (cursor) {
                   var msg = "<p>查询记录：" + cursor.key + "</p>";
                   document.querySelector("#status").innerHTML += msg;
                   var msg = "<p><b>" + cursor.value.name + "</b></p>";
                   document.querySelector("#status").innerHTML += msg;
                   console.info(`SSN ${cursor.key} 对应的名字是 ${cursor.value.name}`);
                   cursor.continue();
               } else {
                   console.info("没有更多记录了")
               }
           }
       };

       // 错误处理
       request.onerror = function(event) {
           console.error('Database error:', event.target.error);
       };

     </script>
 </head>
 <body>
 <div id="status" name="status">状态信息</div>
 </body>
 </html>
```

## getOrigins

static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void

以回调方式异步获取当前使用Web SQL数据库和HTML5支持的Web存储API的所有源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[WebStorageOrigin](arkts-apis-webview-i.md#webstorageorigin)>> | 是 | 以数组方式返回源的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100012 | Invalid web storage origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getOrigins')
        .onClick(() => {
          try {
            webview.WebStorage.getOrigins((error, origins) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              for (let i = 0; i < origins.length; i++) {
                console.info('origin: ' + origins[i].origin);
                console.info('usage: ' + origins[i].usage);
                console.info('quota: ' + origins[i].quota);
              }
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOrigins

static getOrigins(): Promise<Array<WebStorageOrigin>>

以Promise方式异步获取当前使用Web SQL数据库和HTML5支持的Web存储API的所有源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[WebStorageOrigin](arkts-apis-webview-i.md#webstorageorigin)>> | Promise实例，用于获取当前所有源的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100012 | Invalid web storage origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('getOrigins')
        .onClick(() => {
          try {
            webview.WebStorage.getOrigins()
              .then(origins => {
                for (let i = 0; i < origins.length; i++) {
                  console.info('origin: ' + origins[i].origin);
                  console.info('usage: ' + origins[i].usage);
                  console.info('quota: ' + origins[i].quota);
                }
              })
              .catch((e: BusinessError) => {
                console.error('error: ' + JSON.stringify(e));
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginQuota

static getOriginQuota(origin: string, callback: AsyncCallback<number>): void

使用callback回调异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储配额，配额以字节为单位。

**方法调用关系：**

* origin参数应从getOrigins()方法获取。
* 建议先调用getOrigins()获取源列表，再调用getOriginQuota()获取指定源配额。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| callback | AsyncCallback<number> | 是 | 指定源的存储配额。  number是long型整数，范围为[-2147483648, 2147483647]。  单位：byte。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginQuota')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginQuota(this.origin, (error, quota) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              console.info('quota: ' + quota);
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginQuota

static getOriginQuota(origin: string): Promise<number>

以Promise方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储配额，配额以字节为单位。

**方法调用关系：**

* origin参数应从getOrigins()方法获取。
* 建议先调用getOrigins()获取源列表，再调用getOriginQuota()获取指定源配额。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise实例，用于获取指定源的存储配额。  单位：byte。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginQuota')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginQuota(this.origin)
              .then(quota => {
                console.info('quota: ' + quota);
              })
              .catch((e: BusinessError) => {
                console.error('error: ' + JSON.stringify(e));
              })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginUsage

static getOriginUsage(origin: string, callback: AsyncCallback<number>): void

以回调方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储量，存储量以字节为单位。

**方法调用关系：**

* origin参数应从getOrigins()方法获取。
* 建议先调用getOrigins()获取源列表，再调用getOriginUsage()获取指定源使用量。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引 |
| callback | AsyncCallback<number> | 是 | 指定源的存储量。  单位：byte。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginUsage')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginUsage(this.origin, (error, usage) => {
              if (error) {
                console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                return;
              }
              console.info('usage: ' + usage);
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }

        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginUsage

static getOriginUsage(origin: string): Promise<number>

以Promise方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储量，存储量以字节为单位。

**方法调用关系：**

* origin参数应从getOrigins()方法获取。
* 建议先调用getOrigins()获取源列表，再调用getOriginUsage()获取指定源使用量。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise实例，用于获取指定源的存储量。  单位：byte。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = "resource://rawfile/";

  build() {
    Column() {
      Button('getOriginUsage')
        .onClick(() => {
          try {
            webview.WebStorage.getOriginUsage(this.origin)
              .then(usage => {
                console.info('usage: ' + usage);
              }).catch((e: BusinessError) => {
              console.error('error: ' + JSON.stringify(e));
            })
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## deleteAllData

static deleteAllData(incognito?: boolean): void

清除被JavaScript存储API使用的所有存储数据，这包括Web SQL数据库和HTML5支持的Web存储API。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示删除所有隐私模式下内存中的web数据，false表示删除正常非隐私模式下被JavaScript存储API使用的所有存储数据，这包括Web SQL数据库和HTML5支持的Web存储API。  默认值：false。  传入undefined或null时为false。 |

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
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
      Web({ src: $rawfile('index.html'), controller: this.controller })
    }
  }
}
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下加载的html文件。
