---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-110
title: 网页弹窗点击后，跳转失败停留空白页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 网页弹窗点击后，跳转失败停留空白页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:572b6a62683ebd92d2bdd5943933e0b031552adf47e47058643ebdd83b631926
---

## 问题现象

应用网页弹窗点击“取消”后，会停留在一个空白页面。

## 背景知识

[backward](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#backward)按照网页历史栈，后退一个页面。一般结合[accessBackward](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#accessbackward)一起使用。

## 问题定位

弹窗提示选择“取消”后，弹窗消失，页面保持原有空白页面。同时，侧滑后返回了上一界面。证明网页未进行返回或者跳转新页面来响应“取消”事件。

## 分析结论

应用没有对“取消”事件做返回处理。

## 修改建议

1. 使用backward返回上一页面。

   简易示例代码如下：

   ```screen
   // xxx.ets
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct WebBackward {
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       Column() {
         Blank()
           .height(20)
         Button('返回')
           .onClick(() => {
             try {
               this.controller.backward();
             } catch (error) {
               console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
             }
           })
         Web({ src: $rawfile('one.html'), controller: this.controller })
           .fileAccess(false)
           .geolocationAccess(false)
       }
     }
   }
   ```
2. 修改网页代码，添加返回上一页面操作。

   ```screen
   <!-- one.html -->
   <!DOCTYPE html>

   <html>
   <head>
       <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
       <title>页面1</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               padding: 20px;
           }
           .nav-link {
               display: inline-block;
               padding: 15px 25px;
               background: #4CAF50;
               color: white;
               text-decoration: none;
               border-radius: 5px;
           }
       </style>
   </head>
   <body>
   <h1>这是页面1</h1>
   <p>点击下方按钮跳转到页面2：</p>
   <a href="two.html" class="nav-link">前往页面2</a>
   </body>
   </html>
   ```

   ```screen
   <!-- two.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
       <title>页面2</title>
       <style>
           body {
               font-family: Arial, sans-serif;
               padding: 20px;
           }
           .back-btn {
               display: inline-block;
               padding: 15px 25px;
               background: #f44336;
               color: white;
               text-decoration: none;
               border-radius: 5px;
               margin-bottom: 20px;
           }
       </style>
       <script>
           // 移动端侧滑返回功能
           let touchStartX = 0;
           let touchStartY = 0;

           document.addEventListener('touchstart', function(e) {
               touchStartX = e.changedTouches[0].screenX;
               touchStartY = e.changedTouches[0].screenY;
           });

           document.addEventListener('touchend', function(e) {
               const touchEndX = e.changedTouches[0].screenX;
               const touchEndY = e.changedTouches[0].screenY;

               // 右滑返回
               if (touchEndX > touchStartX + 30 && Math.abs(touchEndY - touchStartY) < 50) {
                   window.history.back();
               }
           });

           function historyBack() {
               // 返回上一级页面
               history.back();
           }

           function historyGo() {
               // 返回上一级页面
               history.go(-1);
           }

           function windowHistoryGo() {
               // 返回上一级页面
               window.history.go(-1);
           }

           function windowHistoryBack() {
               // 返回上一级页面
               window.history.back();
           }
       </script>
   </head>
   <body>
   <h1>这是页面2</h1>
   <p>点击下方按钮或者右滑跳转到页面2：</p>
   <button onclick="historyBack()" class="back-btn">historyBack返回页面1</button>
   <button onclick="historyGo()" class="back-btn">historyGo返回页面1</button>
   <button onclick="windowHistoryGo()" class="back-btn">windowHistoryGo返回页面1</button>
   <button onclick="windowHistoryBack()" class="back-btn">windowHistoryBack返回页面1</button>
   </body>
   </html>
   ```
