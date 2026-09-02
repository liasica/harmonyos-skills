---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-114
title: 加载网页，图片被截断且页面能够横向滑动
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 加载网页，图片被截断且页面能够横向滑动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:817bb885c36c8f3c36e4c455b07019ed0ab02b8e0c13d05a8d9b8ee0274c6bcd
---

## 问题现象

应用加载网页，网页中的图片被截断，显示不完全，且页面可以通过横向滑动查看图片被截断的部分。

## 背景知识

1. [layoutMode](../harmonyos-references/arkts-basic-components-web-attributes.md#layoutmode11)：使用Web组件大小自适应页面内容布局模式layoutMode(WebLayoutMode.FIT\_CONTENT)时，能使Web组件的大小根据页面内容自适应变化。
2. viewport：viewport是用户网页的可视区域。手机浏览器是把页面放在一个虚拟的"窗口"（viewport）中，通常这个虚拟的"窗口"（viewport）比屏幕宽，这样就不用把每个网页挤到很小的窗口中，用户可以通过平移和缩放来看网页的不同部分。

## 问题定位

1. 检查是否正确设置viewport元标签：若网页未添加移动端适配的viewport元标签，可能导致内容宽度超出屏幕，引发横向滚动。

   ```ts
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```
2. 检查webview是否启用自适应模式：若未正确设置layoutMode，可能导致Web组件无法根据内容调整高度或宽度，造成截断或横向溢出。

   ```ts
   Web({ src: '...', renderMode: RenderMode.SYNC_RENDER })
     .layoutMode(WebLayoutMode.FIT_CONTENT)  // 自适应内容尺寸
     .width('100%')  // 宽度占满容器
     .overScrollMode(OverScrollMode.NEVER)  // 禁用回弹
     .zoomAccess(false)  // 禁用缩放
   ```
3. 检查网页内容固定宽度是否过大：若网页内容采用固定宽度（如1200px），在小屏设备上会横向溢出。

   ```ts
   body { 
     max-width: 100%;
     overflow-x: hidden;  /* 隐藏横向溢出 */
   }
   ```

## 分析结论

1. 未设置响应式视口。
2. Web组件布局模式设置不当。
3. 网页内容宽度超出限制。

## 修改建议

1. 设置视口与限制内容宽度。确保网页添加移动端适配的viewport元标签，并限制元素最大宽度。

   ```ts
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <style>
     body { 
       max-width: 100%; 
       overflow-x: hidden;  /* 隐藏横向溢出 */
     }
     img { 
       max-width: 100%;  /* 防止图片超出容器 */
       height: auto; 
     }
   </style>
   ```
2. 启用自适应布局模式。设置Web组件自适应内容尺寸并限制滚动方向：

   ```ts
   Web({ src: '...', controller: this.controller })
     .layoutMode(WebLayoutMode.FIT_CONTENT)
     .width('100%')  // 占满父容器
     .overScrollMode(OverScrollMode.NEVER)  // 禁用回弹
     .zoomAccess(false)  // 禁用缩放
   ```
3. 限制网页宽度（如使用百分比），防止超出屏幕宽度。
