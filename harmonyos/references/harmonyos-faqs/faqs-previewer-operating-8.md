---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-8
title: SVG图片在真机和DevEco Studio中颜色显示不一致该如何解决
breadcrumb: FAQ > DevEco Studio > 界面预览 > SVG图片在真机和DevEco Studio中颜色显示不一致该如何解决
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:09e3f6a06c5f7d022e42585e3b694dcaed12af023cfec4df4a003f9c8c829edc
---

## 问题现象

SVG图片在DevEco Studio和浏览器中打开显示为黄色，但是在测试机和DevEco Studio的Previewer上显示为红色。

* DevEco Studio中预览为黄色：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/rdyG-przQbyb9wgWGveSFA/zh-cn_image_0000002628408094.png "点击放大")

* DevEco Studio的Previewer中渲染为红色：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/rI0iTaxGR-C3eVVW-ShU-Q/zh-cn_image_0000002628567994.png "点击放大")

  ```screen
  <svg id='vector' xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'>
    <defs>
      <linearGradient gradientUnits='userSpaceOnUse' x1='6.935' y1='3.252' x2='6.909' y2='10.552' id='gradient_0'>
        <stop offset='0' stop-color='#FFFE4144'/>
        <stop offset='1' stop-color='#FFFF6D67'/>
      </linearGradient>
    </defs>
    <path fill='url(#gradient_0)' d='M10.983,3.951C10.983,3.313 10.461,2.79 9.823,2.79C5.983,2.79 2.862,5.913 2.862,9.755C2.862,10.393 3.384,10.915 4.022,10.915C4.66,10.915 5.182,10.393 5.182,9.755C5.182,7.189 7.259,5.112 9.823,5.112C10.461,5.112 10.983,4.589 10.983,3.951Z' stroke-width='1'
          fill-rule='evenodd' stroke='#00000000' id='path_6' />
  </svg>
  ```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/hhl-xOpYTiif1wCpbghrag/zh-cn_image_0000002658927315.png "点击放大")

## 定位思路

DevEco Studio和浏览器仅支持解析颜色值为RGBA格式的SVG图片，不支持#FFFE4144和#FFFF6D67等十六进制格式，因此如果遇到了DevEco Studio和浏览器的SVG预览错误，可以将SVG图片的颜色值改为RGBA格式。

## 解决方案

颜色的十六进制格式改为RGBA格式可自行搜索相关资料。

```screen
<svg id='vector' xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28'>
  <defs>
    <linearGradient gradientUnits='userSpaceOnUse' x1='6.935' y1='3.252' x2='6.909' y2='10.552' id='gradient_0'>
      <stop offset='0' stop-color='rgba(254,65,68,1)'/> // 修改颜色为RGBA格式
      <stop offset='1' stop-color='rgba(255,109,103,1)'/> // 修改颜色为RGBA格式
    </linearGradient>
  </defs>
 <path fill='url(#gradient_0)' d='M10.983,3.951C10.983,3.313 10.461,2.79 9.823,2.79C5.983,2.79 2.862,5.913 2.862,9.755C2.862,10.393 3.384,10.915 4.022,10.915C4.66,10.915 5.182,10.393 5.182,9.755C5.182,7.189 7.259,5.112 9.823,5.112C10.461,5.112 10.983,4.589 10.983,3.951Z' stroke-width='1'
       fill-rule='evenodd' stroke='#00000000' id='path_6' />
</svg>
```
