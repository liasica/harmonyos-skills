---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-faq-0006
title: ArkWeb H5与原生交互常见问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 常见问题 > ArkWeb H5与原生交互常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:47+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:d06fff95a307e76e4ae44f8e4f421b6b4d8d07e4858965a5847dea87b80dc673
---

**Q：应用侧通过registerJavaScriptProxy注入方法到H5中，并在H5调用该方法并传入对象参数，请问应用侧如何获取H5返回对象的全部键值？**

**A**：通过Object.keys()方法获取对象键属性名组成的数组。

```ts
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

```html
-->
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
<!--
```
