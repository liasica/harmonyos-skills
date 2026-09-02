---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-136
title: 如何解决Web组件高度无法动态改变的问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决Web组件高度无法动态改变的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d7a8227636e501a4492ebeeb28afe1f0b9b23f6fcdbc5174be5322819e6ea534
---

## 问题现象

在Web组件中，加载了一个包含输入区域的HTML页面，当点击页面中的任何区域，系统输入法弹出之后会通过listenKeyboard监听到输入法键盘高度，并压缩Web组件的高度，让它缩小到屏幕上半部分。

* 预期效果：系统输入法弹出后，Web组件的渲染区域缩小到屏幕上半部分，并且在Web组件和输入法之间有预留的动态避让区（通过Blank组件实现）。
* 实际效果：系统输入法弹出后，虽然组件树中感知到动态避让区（Blank组件）高度为413vp，但实际并没有绘制出动态避让区，且Web组件的渲染区域并未缩小到屏幕上半部分，如下图。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/4FAD7T_uSwGfZg1OHm-fuw/zh-cn_image_0000002628899134.png "点击放大")

  期望通过监听键盘高度来实现Web组件高度动态改变。

## 背景知识

* [使用Web组件加载页面](../harmonyos-guides/web-page-loading-with-web-components.md)：页面加载是Web组件的基本功能。根据页面加载数据来源可以分为三种常用场景，包括加载网络页面、加载本地页面、加载HTML格式的富文本数据。
* [Web组件大小自适应页面内容布局](../harmonyos-guides/web-fit-content.md)：使用Web组件大小自适应页面内容布局模式时，能使Web组件的大小根据页面内容自适应变化。
* [安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)：安全区域是指页面的显示区域，默认不与系统设置的非安全区域比如状态栏、导航栏区域重叠，默认情况下开发者开发的界面都被布局在安全区域内。

## 问题定位

* 排查Blank组件在高度动态修改时的作用。

  如果Blank组件高度动态修改后只是覆盖在Web上面，并不是把Web页面顶上去，那么Web页面高度实际没有变化。直接修改Web组件高度为`height('calc(100% - 413vp)')后可以达到理想效果，但并不是动态改变。
* 排查是否只是改变Web组件在屏幕上的显示区域。

  在Web组件上加一个layoutWeight(1)属性后，虽然会改变当前Web组件在屏幕上的显示区域，但它的高度是不会发生改变的。由于DevEco Studio的ArkUI Inspector是通过获取组件高度来绘制的，因此layoutWeight(1)属性没办法修改Web组件的高度，只能修改其在父组件中的布局，从ArkUI Inspector中可以看出Web高度始终没有改变。

## 分析结论

通过排查可以知道，问题代码的处理，并不能使Web组件的高度动态变化。参考背景知识，为了解决这个问题，需要通过突破安全区域的限制来处理。利用安全区域的[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性支持组件不改变布局情况下扩展其绘制区域至安全区外。

## 修改建议

设置Web的属性expandSafeArea([SafeAreaType.KEYBOARD])，让Web组件不避让软键盘。通过监听软键盘高度变化，在软键盘弹出时设置Web的底部的margin为键盘高度，实现Web组件的高度动态变化。

完整示例如下：

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct WebExpandHeightDemo {
  controller: webview.WebviewController = new webview.WebviewController();
  @State safeExpandHeight: number = 0;

  aboutToAppear(): void {
    try {
      webview.WebviewController.setWebDebuggingAccess(true);
      this.listenKeyboard();
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }

  // 监听键盘高度
  private listenKeyboard() {
    window.getLastWindow(this.getUIContext().getHostContext()).then(currentWindow => {
      // 监听键盘高度，处理工具条偏移量
      currentWindow.on('keyboardHeightChange', (data) => {
        let keyboardHeight = Math.floor(this.getUIContext().px2vp(data));
        if (keyboardHeight > 0) {
          // 键盘编辑态，偏移量=键盘高度
          this.safeExpandHeight = keyboardHeight;
        } else {
          // 无键盘编辑态，安全区高度
          this.safeExpandHeight = 0;
        }
      });
    });
  }

  build() {
    Stack() {
      Column() {
        Web({ src: $rawfile('index.html'), controller: this.controller })
          .fileAccess(false)
          .geolocationAccess(false)
          .onControllerAttached(() => {
            // 推荐在此loadUrl、设置自定义用户代理、注入JS对象等
            console.info('onControllerAttached execute');
          })
          .margin({ bottom: this.safeExpandHeight })
          .layoutWeight(1)
          .expandSafeArea([SafeAreaType.KEYBOARD]);
      };
    };
  }
}
```

HTML代码示例：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-size: 24px;
            line-height: 1.5;
        }
        contenteditable {
            display: block;
            width: 100%;
            height: 100vh;
            border: none;
            outline: none;
        }
    </style>
</head>
<body>
<h1>Hello, ArkWeb</h1>
<div contenteditable="true" id="editableContent">
    <script>
        let numbers = '';
        for (let i = 1; i <= 100; i++) {
            numbers += i + '<br>';
        }
        document.getElementById('editableContent').innerHTML = numbers;
    </script>
</div>
</body>
</html>
```

## 总结

对于组件在页面显示区域内的变化，可以考虑设置组件绘制内容突破安全区域的限制来处理。其中需要注意的几点是：

1. 组件设置expandSafeArea属性之后生效的条件为：
   * type为SafeAreaType.KEYBOARD时默认生效，组件不避让键盘。
   * 设置其他type，组件的边界与安全区域重合时组件能够延伸到安全区域下。例如：设备顶部状态栏高度100，那么组件在屏幕中的绝对位置需要为0<=y<=100。
2. 组件延伸到安全区域下，在安全区域处的事件，如点击事件等可能会被系统拦截，优先给状态栏等系统组件响应。
3. 滚动类容器内的组件不建议设置expandSafeArea属性，如果设置，需要按照组件嵌套关系，将当前节点到滚动类容器间所有子节点设置expandSafeArea属性，否则expandSafeArea属性在滚动后可能会失效。
4. 除了组件扩展其安全区域外，和键盘相关比较常见的还有**setKeyboardAvoidMode（控制虚拟键盘抬起时页面的避让模式）**、**getKeyboardAvoidMode（返回虚拟键盘抬起时的页面避让模式）**。

更多示例请见官方文档[安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)。
