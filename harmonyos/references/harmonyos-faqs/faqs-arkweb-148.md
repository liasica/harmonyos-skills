---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-148
title: 应用侧如何获取H5返回对象的全部键值
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 应用侧如何获取H5返回对象的全部键值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b24e63ad34878126cee111e8e1974b1f615fc8b7edeea529416363b4db826b38
---

## 问题现象

应用侧通过registerJavaScriptProxy注入方法到H5中，并在H5调用该方法并传入对象参数，请问应用侧如何获取H5返回对象的全部键值？

## 背景知识

* Object.keys()：JavaScript中，该静态方法返回一个由给定对象自身的可枚举的字符串键属性名组成的数组。
* Reflect.get()：JavaScript中，该方法与从对象(target[propertyKey])中读取属性类似，但它是通过一个函数执行来操作的。

## 解决方案

通过Object.keys()方法获取对象键属性名组成的数组。

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class jsBridgeClass {
  constructor() {
  }

  // 通过Object.keys()方法获取对象键属性名组成的数组
  // 通过Reflect.get()方法获取对应对象属性的value值
  getObjectKeyValue(obj: ESObject) {
    for (const key of Object.keys(obj)) {
      console.info('获取类对象的属性和值', key, Reflect.get(obj, key));
      // 也可以通过obj[key]获取对象属性的value值
      console.info('获取类对象的属性和值', key, obj[key]);
    }
  }
}

@Entry
@Component
struct Index {
  @State jsBridgeObj: jsBridgeClass = new jsBridgeClass();
  private webviewController: WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({
        src: $rawfile('getObjectKeyValue.html'),
        controller: this.webviewController,
      })
        .width('100%')
        .height('100%')
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .onControllerAttached(() => {
          try {
            this.webviewController.registerJavaScriptProxy(this.jsBridgeObj, 'jsBridgeObjName', ['getObjectKeyValue']);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        });
    };
  }
}
```

```screen
<!DOCTYPE html>
<html>
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<body>
<button onclick="callArkTS()" type="button">Click Me!</button>
</body>
<script>
    function callArkTS() {
        let obj ={
            id:1,
            name:'LILY'
        }
        jsBridgeObjName.getObjectKeyValue(obj);
    }
</script>
</html>
```
