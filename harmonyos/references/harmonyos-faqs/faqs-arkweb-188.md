---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-188
title: Web中登录界面登录后如何不触发密码保险箱保存密码
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web中登录界面登录后如何不触发密码保险箱保存密码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7cd3eb93fc616f814dff9f06c0923237edddf8706f1a3ffa871c7da7701848df
---

## 问题现象

Web中登录界面，登录成功后，会触发弹出密码保险箱，提示保存密码，如何设置可以让密码保险箱不弹出？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/fBhVULwuQ3SlB9TnYtAffQ/zh-cn_image_0000002659258401.png "点击放大")

## 背景知识

网页触发密码保险箱规格：

* ArkWeb使用Chromium智能算法，自动识别网页中的用户名、密码元素。
* ArkWeb依赖密码表单提交成功后，触发页面跳转到其他页面，才能触发密码保存。

## 解决方案

解决方案有3种：

* **方案一**：手机设置->隐私和安全->密码保险箱，关闭“自动填充和保存”，关闭之后，所有应用登录界面都不会再触发密码保险箱提示保存密码。
* **方案二**：将前端代码全部预置在应用resources->rawfile目录下，通过[加载本地页面](../harmonyos-guides/web-page-loading-with-web-components.md#加载本地页面)的方式加载前端页面，登录页面登录后，不会触发密码保险箱提示保存密码。

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct LoginDemo1 {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        Web({ src: $rawfile('login.html'), controller: this.controller })
          .javaScriptAccess(true)
          .fileAccess(true)
          .domStorageAccess(true)
          .geolocationAccess(true)
          .width('100%')
          .height('100%');
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  login.html：

  ```html
  <!DOCTYPE html>
  <html lang="zh-CN">
  <head>
      <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
      <title>登录界面</title>
  </head>
  <body>
  <h2>欢迎登录</h2>
  <form id="loginForm" autocomplete="on">
      <label for="username">用户名：</label><br>
      <input type="text" id="username" name="username" required><br><br>

      <label for="password">密码：</label><br>
      <input type="password" id="password" name="password" required><br><br>

      <button type="submit">登录</button>
  </form>

  <script>
      document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
        // 这里登录逻辑
        // ....
        // 跳转至首页
        window.location.href = './index.html';
      });
  </script>
  </body>
  </html>
  ```

  index.html：

  ```html
  <!DOCTYPE html>
  <html lang="zh">
  <head>
      <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
      <title>首页</title>
      <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
          }
          h1 {
            font-size: 3rem;
            color: #333;
            text-align: center;
          }
      </style>
  </head>
  <body>
  <h1>Hello World</h1>
  </body>
  </html>
  ```
* **方案三**：密码input框type类型不要使用type="password"，设置为type="text"，登录后不会密码保险箱提示保存密码。这种方案会导致input框不能使用password类型，需要开发过程中自己实现密码框，成本较高，且对于密码安全存在一定风险。

  ```ts
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct LoginDemo2 {
    controller: webview.WebviewController = new webview.WebviewController();

    build() {
      Column() {
        // src须替换为真实url
        Web({ src: 'https://***', controller: this.controller })
          .javaScriptAccess(true)
          .fileAccess(true)
          .domStorageAccess(true)
          .geolocationAccess(true)
          .width('100%')
          .height('100%');
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  login.html：

  ```html
  <!DOCTYPE html>
  <html lang="zh-CN">
  <head>
      <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
      <title>登录界面</title>
  </head>
  <body>
  <h2>欢迎登录</h2>
  <form id="loginForm" autocomplete="on">
      <label for="username">用户名：</label><br>
      <input type="text" id="username" name="username" required><br><br>

      <label for="password">密码：</label><br>
      <!--  密码框type不使用password，改成text，避免触发密码保险箱  -->
      <input type="text" id="password" name="password" required><br><br>

      <button type="submit">登录</button>
  </form>

  <script>
      document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
        // 这里登录逻辑
        // ....
        // 跳转至首页
        window.location.href = './index.html';
      });
  </script>
  </body>
  </html>
  ```
