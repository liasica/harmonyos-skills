---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-107
title: 进入页面后，页面内容抖动
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 进入页面后，页面内容抖动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7e435e7c821401adb92847149cbe70ef902d0b12bfa2335b2e83e471ac286a6e
---

## 问题现象

进入Web页面后，页面内容先上移后下移，造成视觉上页面内容抖动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/VihWuHjgTbWFdX9YoDLIzA/zh-cn_image_0000002629059044.png "点击放大")

## 背景知识

* 在H5页面中，如果需要定时执行某些操作（如轮询数据、更新界面、动画等），可以使用JavaScript提供的两个核心定时器函数：
  + setTimeout()：在指定时间后执行一次函数。
  + setInterval()：每隔一定时间重复执行函数。
* 在H5页面中，display属性设置为hidden可实现不显示组件。

## 问题定位

查看该H5页面的设置，该页面使用setTimeout在数据为空时不显示该组件。

```screen
<head>
    <link rel="stylesheet" type="text/css" href="./css/index.css">
    <meta charset="UTF-8">
    <style>
        body {
          font-size: 18px;
          height: 100%;
          width: 100%;
          padding: 30px;
        }

        .hidden {
          display: none;
        }
    </style>
</head>
<body>
<div id="contentA" class="hidden" style="height: 60px;width:100%;font-size: 30px;">
    <h1 id="displayName"></h1>
</div>
<div style="height: 80px;width:100%;font-size: 50px;margin-top:20px;">
    青青园中葵，朝露待日晞。
    阳春布德泽，万物生光辉。
    常恐秋节至，焜黄华叶衰。
    百川东到海，何时复西归？
    少壮不努力，老大徒伤悲。
</div>
<script>
    let name = null;
    document.getElementById("displayName").textContent = name;
    document.getElementById("contentA").classList.remove("hidden");

    // 0.1秒后若没有获取到数据则不显示组件
    setTimeout(() => {
        if(name==null){
            document.getElementById("contentA").classList.add("hidden");
        }
      }, 100);

    // 模拟加载数据
    setTimeout(() => {
        name = "汉乐府";
        document.getElementById("contentA").classList.remove("hidden");
        document.getElementById("displayName").textContent = "作者：" + name;
      }, 500);
</script>
</body>
```

## 分析结论

H5页面设置了在数据为空时不显示该组件，且数据获取的等待时间过短，导致未在规定时间内获取到数据时该组件进行隐藏，下方内容上移。而加载到数据后显示该组件，下方内容下移，从而造成页面内容抖动。

## 修改建议

* 方案一：删除在数据为空时不显示该组件的设置。

  ```screen
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebVideo {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Stack() {
        Web({ src: $rawfile('text1.html'), controller: this.controller })
          .height('100%')
          .width('100%')
          .fileAccess(true)
          .geolocationAccess(false)
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  src/main/resources/rawfile/text1.html：

  ```screen
  <head>
      <link rel="stylesheet" type="text/css" href="./css/index.css">
      <meta charset="UTF-8">
      <style>
          body {
            font-size: 18px;
            height: 100%;
            width: 100%;
            padding: 30px;
          }
      </style>
  </head>
  <body>
  <div id="contentA" class="hidden" style="height: 60px;width:100%;font-size: 30px;">
      <h1 id="displayName"></h1>
  </div>
  <div style="height: 80px;width:100%;font-size: 50px;margin-top:20px;">
      青青园中葵，朝露待日晞。
      阳春布德泽，万物生光辉。
      常恐秋节至，焜黄华叶衰。
      百川东到海，何时复西归？
      少壮不努力，老大徒伤悲。
  </div>
  <script>
      let name = null;
      document.getElementById("displayName").textContent = name;

      // 模拟加载数据
      setTimeout(() => {
          name = "汉乐府"
          document.getElementById("displayName").textContent = "作者：" + name;
        }, 500);
  </script>
  </body>
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/DXslEHIbT_CIIY1e7jQjYw/zh-cn_image_0000002659258347.png "点击放大")
* 方案二：延长数据获取的等待时间。

  ```screen
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebVideo {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Stack() {
        Web({ src: $rawfile('text2.html'), controller: this.controller })
          .height('100%')
          .width('100%')
          .fileAccess(true)
          .geolocationAccess(false)
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  src/main/resources/rawfile/text2.html：

  ```screen
  <head>
      <link rel="stylesheet" type="text/css" href="./css/index.css">
      <meta charset="UTF-8">
      <style>
          body {
            font-size: 18px;
            height: 100%;
            width: 100%;
            padding: 30px;
          }

          .hidden {
            display: none;
          }
      </style>
  </head>
  <body>
  <div id="contentA" class="hidden" style="height: 60px;width:100%;font-size: 30px;">
      <h1 id="displayName"></h1>
  </div>
  <div style="height: 80px;width:100%;font-size: 50px;margin-top:20px;">
      青青园中葵，朝露待日晞。
      阳春布德泽，万物生光辉。
      常恐秋节至，焜黄华叶衰。
      百川东到海，何时复西归？
      少壮不努力，老大徒伤悲。
  </div>
  <script>
      let name = null;
      document.getElementById("displayName").textContent = name;
      document.getElementById("contentA").classList.remove("hidden");

      // 1秒后若没有获取到数据则不显示组件
      setTimeout(() => {
          if(name==null){
              document.getElementById("contentA").classList.add("hidden");
          }
        }, 1000);

      // 模拟加载数据
      setTimeout(() => {
          name = "汉乐府";
          document.getElementById("contentA").classList.remove("hidden");
          document.getElementById("displayName").textContent = "作者：" + name;
        }, 500);
  </script>
  </body>
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/CY7_AWWIRqu4Cx0zHSd6qg/zh-cn_image_0000002628899128.png "点击放大")
