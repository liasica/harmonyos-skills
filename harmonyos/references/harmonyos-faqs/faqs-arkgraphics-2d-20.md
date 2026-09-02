---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-20
title: RGB和HSB颜色如何互相转换
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > RGB和HSB颜色如何互相转换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1eaf7e79360893aef4516de9710db21591ad1807376bfd91963cdfe5a6c99e57
---

## 问题现象

项目开发过程中不同的场景需要用到不同的颜色模型，如何通过ArkTS高效的对RGB、HSB两种颜色模型进行相互转换。

## 背景知识

RGB和HSB（有时也称为HSV）是两种不同的颜色模型，它们分别用于描述颜色的不同属性。RGB模型基于红、绿、蓝三种颜色的混合来定义颜色，而HSB模型则基于色调（Hue）、饱和度（Saturation）、亮度（Brightness或Value）来定义颜色。

## 解决方案

1. 可通过如下工具方法将RGB转换成HSB模型。

   ```ts
   interface ColorHsv {
     h: number;
     s: number;
     v: number;
   }

   // RGB模型转HSV模型
   function rgb2hsv(r: number, g: number, b: number): ColorHsv {
     r = r / 255.0;
     g = g / 255.0;
     b = b / 255.0;
     let max: number = Math.max(r, g, b);
     let min: number = Math.min(r, g, b);
     let delta: number = max - min;

     let h = 0, s = 0, v = 0;
     if (max == min) {
       h = 0;
     } else if (max == r) {
       h = (g >= b ? ((g - b) / delta) * 60 : ((g - b) / delta) * 60 + 360);
     } else if (max == g) {
       h = ((b - r) / delta) * 60 + 120;
     } else if (max == b) {
       h = ((r - g) / delta) * 60 + 240;
     }

     s = (max == 0 ? 0 : delta / max);
     v = max;
     return { h: h, s: s, v: v };
   }
   ```
2. 通过如下工具方法将HSB转成RGB模型。

   ```ts
   interface ColorRgb {
     r: number;
     g: number;
     b: number;
   }

   // HSV模型转RGB模型
   function hsv2rgb(h: number, s: number, v: number): ColorRgb {
     let r: number = 0, g: number = 0, b: number = 0;
     let i = Math.floor(h / 60);
     let f = h / 60 - i;
     let p = v * (1 - s);
     let q = v * (1 - f * s);
     let t = v * (1 - (1 - f) * s);
     switch (i % 6) {
       case 0:
         r = v;
         g = t;
         b = p;
         break;
       case 1:
         r = q;
         g = v;
         b = p;
         break;
       case 2:
         r = p;
         g = v;
         b = t;
         break;
       case 3:
         r = p;
         g = q;
         b = v;
         break;
       case 4:
         r = t;
         g = p;
         b = v;
         break;
       case 5:
         r = v;
         g = p;
         b = q;
         break;
     }
     r = Math.round(r * 255);
     g = Math.round(g * 255);
     b = Math.round(b * 255);
     return { r: r, g: g, b: b };
   }
   ```
