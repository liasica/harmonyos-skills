---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-120
title: 应用查询设备信息提示信息有误
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 应用查询设备信息提示信息有误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:82a8cae7102f58597cc9ee94c6c19c8bd9c5c67eee54c907155872aa434713e5
---

## 问题现象

应用内点击活动功能，跳转到活动页面，弹窗提示“设备信息有误”。

## 背景知识

[设备信息](../harmonyos-references/js-apis-device-info.md)：提供查询产品信息的能力，比如查询设备类型、设备品牌名称、产品系列、产品版本号等。

[前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)：开发者使用Web组件将应用侧代码注册到前端页面中，注册完成之后，前端页面中使用注册的对象名称就可以调用应用侧的方法，实现在前端页面中调用应用侧方法。

## 问题定位

1. 使用DevEco Testing的UIViewer查看问题页面的页面元素。
2. 通过关键词“设备信息有误|deviceInfo”过滤日志，结果如下：

   ```shell
   07-21 11:26:39.336   29228-29228   A01194/com.hm...RKWEB-CONSOLE  com.hm.example     I     [CONSOLE:1] "error:  设备信息有误", source: https://www.xxx.com/page/mp_activities/js/luck-draw-202304~luck-draw-202306~luck-draw-202307~luck-draw-202308~luck-draw-202309-10~luck-draw-20~0edc77cb.1b3e3151.js (1)
   07-21 11:26:39.342   29228-29228   A01194/com.hm...RKWEB-CONSOLE  com.hm.example     I     [CONSOLE:1] "设备信息有误", source: https://www.xxx.com/page/mp_activities/js/luck-draw-202507.614cbb12.js (1)
   07-21 11:26:39.508   29228-29228   A01194/com.hm...RKWEB-CONSOLE  com.hm.example     I     [CONSOLE:1] "error:  设备信息有误", source: https://www.xxx.com/page/mp_activities/js/luck-draw-202304~luck-draw-202306~luck-draw-202307~luck-draw-202308~luck-draw-202309-10~luck-draw-20~0edc77cb.1b3e3151.js (1)
   07-21 11:26:39.508   29228-29228   A01194/com.hm...RKWEB-CONSOLE  com.hm.example     I     [CONSOLE:1] "设备信息有误", source: https://www.xxx.com/page/mp_activities/js/luck-draw-202507.614cbb12.js (1)
   07-21 11:26:39.791   29228-29228   A01194/com.hm...RKWEB-CONSOLE  com.hm.example     I     [CONSOLE:1] "error:  设备信息有误", source: https://www.xxx.com/page/mp_activities/js/luck-draw-202304~luck-draw-202306~luck-draw-202307~luck-draw-202308~luck-draw-202309-10~luck-draw-20~0edc77cb.1b3e3151.js (1)
   07-21 11:26:39.791   29228-29228   A01194/com.hm...RKWEB-CONSOLE  com.hm.example     I     [CONSOLE:1] "设备信息有误", source: https://www.xxx.com/page/mp_activities/js/luck-draw-202507.614cbb12.js (1)
   ```

## 分析结论

在页面元素和日志中仅发现了与JavaScript相关的错误信息，无关键词“deviceInfo”的任何日志打印，说明应用并没有调用系统设备信息查询能力，导致在数据使用时报错。

## 修改建议

通过建立应用侧与H5侧的交互通道，调用应用侧设备信息接口获取数据，参考代码如下：

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  webviewController: webview.WebviewController = new webview.WebviewController();
  // 声明需要注册的对象
  @State devObj: DeviceInfoService = new DeviceInfoService();

  build() {
    Column({ space: 10 }) {
      Web({ src: $rawfile('getDeviceInfo.html'), controller: this.webviewController })
        .javaScriptProxy({
          object: this.devObj,
          name: 'devObjName',
          methodList: ['getDeviceInfo'],
          controller: this.webviewController,
        })
        .geolocationAccess(false)
        .fileAccess(false)
        .height('100%')
        .width('100%');
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }

  aboutToDisappear(): void {
    // 使用结束后清理注册，防止内存泄漏
    try {
      this.webviewController.deleteJavaScriptRegister('testObjName');
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }
}

class DeviceInfoService {
  constructor() {
  }

  getDeviceInfo(): string {
    let deviceTypeInfo: string = deviceInfo.deviceType;
    let brandInfo: string = deviceInfo.brand;
    let marketNameInfo: string = deviceInfo.marketName;
    let productModelInfo: string = deviceInfo.productModel;
    return `设备类型: ${deviceTypeInfo} | 设备品牌名称: ${brandInfo} | 外部产品系列: ${marketNameInfo} | 认证型号: ${productModelInfo}`;
  }
}
```

```ts
<!DOCTYPE html>
<html>
<body>
<button type="button" onclick="callArkTS()" style="font-size: 26px">Click Me!</button>
<p id="demo" style="font-size: 26px"></p>
<script>
    function callArkTS() {
        let str = devObjName.getDeviceInfo();
        document.getElementById("demo").innerHTML = str;
    }
</script>
</body>
</html>
```
