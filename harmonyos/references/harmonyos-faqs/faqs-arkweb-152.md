---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-152
title: Tabs组件嵌套Web，无法左右滑动
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Tabs组件嵌套Web，无法左右滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0ec1dbbf765a616d26e70370ca264f6500e68e0d07d5ad79e2a04a5ef29ac848
---

## 问题现象

使用Tabs组件嵌套Web组件的布局，当左右滑动时，Tabs组件不能切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/vp-xoMhVRDKxLFsmYIm4oQ/zh-cn_image_0000002629059056.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/xvJYbdUaQsebW0J9jzdCMg/zh-cn_image_0000002659258359.png "点击放大")

## 背景知识

* [runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)：在当前显示页面的上下文中异步执行JavaScript脚本，脚本执行的结果将通过异步回调方式返回。此方法必须在用户界面（UI）线程上使用，并且回调也将在用户界面（UI）线程上调用。
* [nestedScroll](../harmonyos-references/arkts-basic-components-web-attributes.md#nestedscroll11)：调用以设置嵌套滚动选项。
* touch-action：用于指定某个给定的区域是否允许用户操作，以及如何响应用户操作（比如浏览器自带的划动、缩放等）。

## 问题定位

* 检查在线网址是否能左右滑动，排查是网址问题导致还是Web组件属性设置问题。
* 查看nestedScroll属性是否正确设置，若设置为SELF\_ONLY，则只自身滚动，不与父组件联动。
* 用浏览器查看该网址是否只设置了touch-action:pan-y属性，该属性只能支持垂直滑动。

## 分析结论

网页中CSS样式只设置了touch-action:pan-y，网页只能垂直滑动，导致不能响应Tabs切换操作。

## 修改建议

可以使用[runJavaScript](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)的方法向H5中注入touch-action:pan-x pan-y样式来覆盖之前的touch-action设置。

端侧示例代码如下：

```screen
import { webview } from '@kit.ArkWeb';

@Entry
@Component
export struct Index {
  @State currentIndex: number = 0;
  @State selectedIndex: number = 0;
  private tabController: TabsController = new TabsController();
  private controller1: webview.WebviewController = new webview.WebviewController();
  private controller2: webview.WebviewController = new webview.WebviewController();
  private fontColor: string = '#182431';
  private selectedFontColor: string = '#0a59f7';

  @Builder
  tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 7, bottom: 7 });
      Divider()
        .strokeWidth(2)
        .color('#0a59f7')
        .padding({
          left: 16,
          right: 16
        })
        .opacity(this.selectedIndex === index ? 1 : 0);
    }.width('100%');
  }

  build() {
    Column() {
      Column() {
        Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.tabController }) {
          TabContent() {
            CommonWeb({
              controller: this.controller1
            });
          }.tabBar(this.tabBuilder(0, '网页1'));

          TabContent() {
            CommonWeb({
              controller: this.controller2
            });
          }.tabBar(this.tabBuilder(1, '网页2'));
        }
        .vertical(false)
        .barMode(BarMode.Fixed)
        .barWidth('100%')
        .barHeight(56)
        .animationDuration(400)
        .onChange((index: number) => {
          this.currentIndex = index;
          this.selectedIndex = index;
        })
        .width('100%')
        .height('100%')
        .padding({
          left: 16,
          right: 16
        });
      }
      .width('100%')
      .height('100%');
    };
  }
}

@Component
struct CommonWeb {
  private controller: webview.WebviewController = new webview.WebviewController();
  private customStyle: string = '* {touch-action: pan-x pan-y!important; }';

  build() {
    Web({ src: $rawfile('fit_content.html'), controller: this.controller })
      .zoomAccess(false)
      .domStorageAccess(true)
      .javaScriptAccess(true)
      .onlineImageAccess(true)
      .imageAccess(true)
      .fileAccess(false)
      .geolocationAccess(false)
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      })
      .onPageEnd(() => {
        // 通过runJavaScript注入样式
        this.controller.runJavaScript(`
                    const head = document.head;
                    console.info(head);
                    const style = document.createElement('style');
                    style.appendChild(document.createTextNode("${this.customStyle}"));
                    head.appendChild(style)
                `);
      });
  }
}
```

fit\_content.html示例代码如下：

```screen
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
    <title>Fit-Content</title>
</head>
<style>
    * {
       touch-action: pan-y;
    }
</style>
<body>
<div>
    <div><h2 id="使用场景">使用场景</h2>
        <p>ArkWeb（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。常见使用场景包括：</p>
        <ul>
            <li><p>
                应用集成Web页面：应用可以在页面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运营效率。</p>
            </li>
            <li><p>
                浏览器网页浏览场景：浏览器类应用可以使用Web组件，打开三方网页，使用无痕模式浏览Web页面，设置广告拦截等。</p>
            </li>
            <li><p>小程序：小程序类宿主应用可以使用Web组件，渲染小程序的页面。</p></li>
        </ul>
    </div>
    <div><h2 id="能力范围">能力范围</h2>
        <p>Web组件为开发者提供了丰富的控制Web页面能力。包括：</p>
        <ul>
            <li><p>Web页面加载：声明式加载Web页面和离屏加载Web页面等。</p></li>
            <li><p>生命周期管理：组件生命周期状态变化，通知Web页面的加载状态变化等。</p></li>
            <li><p>常用属性与事件：UserAgent管理、Cookie与存储管理、字体与深色模式管理、权限管理等。</p>
            </li>
            <li><p>
                与应用界面交互：自定义文本选择菜单、上下文菜单、文件上传界面等与应用界面交互能力。</p>
            </li>
            <li><p>App通过JavaScriptProxy，与Web页面进行JavaScript交互。</p></li>
            <li><p>安全与隐私：无痕浏览模式、广告拦截、坚盾守护模式等。</p></li>
            <li><p>维测能力：DevTools工具调试能力，使用crashpad收集Web组件崩溃信息。
            </p></li>
        </ul>
    </div>
    <div><h2 id="约束与限制">约束与限制</h2>
        <ul>
            <li>Web内核版本：ArkWeb基于谷歌Chromium内核开发，使用的Chromium版本为M114。</li>
        </ul>
    </div>
</div>
</body>
</html>
```
