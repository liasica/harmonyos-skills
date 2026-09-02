---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1032
title: 实现HSL颜色模型与HEX颜色模型互相转换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现HSL颜色模型与HEX颜色模型互相转换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9cbac135fa2efe0b357b6234948310d340892413ca4ffc50a4b21a277b0e42f2
---

## 问题现象

给定HSL颜色模型值，如何将其转换为HEX颜色模型的值？

## 背景知识

* HSL：HSL将颜色分解为三个参数。
  + 色相（Hue）：颜色的类型（如红、蓝、绿等），用0°~360°表示。
  + 饱和度（Saturation）：颜色的纯度或鲜艳程度，用0%~100%表示（0%为灰色，100%为纯色）。
  + 亮度（Lightness）：颜色的明暗程度，用0%~100%表示（0%为黑色，100%为白色）。
* HEX：HEX是一种基于RGB（红、绿、蓝）的编码方式，用十六进制数表示颜色的三原色分量。

## 解决方案

定义ColorModel类：

```ts
export class RgbType {
  // 红色分量，范围为0-255
  red: number = 0;
  // 绿色分量，范围为0-255
  green: number = 0;
  // 蓝色分量，范围为0-255
  blue: number = 0;
}

export class HslType {
  // 色相，范围为0-360
  hue: number = 0;
  // 饱和度，范围为0-100
  saturation: number = 0;
  // 亮度，范围为0-100
  lightness: number = 0;
}
```

在ColorUtils类中实现HSL颜色模型与HEX颜色模型互相转换：

* 实现HSL转换HEX：
  1. 先将HSL饱和度和亮度百分比转换为小数，计算RGB值。
  2. 再把RGB值转换为HEX值。
* 实现HEX转换HSL：
  1. 先将HEX值转为RGB整数。
  2. 再将得到的值归一化为[0,1]范围的浮点数计算HSL值。

```ts
import { HslType, RgbType } from '../model/ColorModel';

// 将HSL颜色模型转换为HEX颜色模型
export function hslToHex(hue: number, saturation: number, lightness: number): string {
  // 将HSL转换为RGB
  const rgb: RgbType = hslToRgb(hue, saturation, lightness);
  // 返回HEX颜色值
  return rgbToHex(rgb.red, rgb.green, rgb.blue);
}

// 将HSL颜色值转换为RGB颜色格式
function hslToRgb(hue: number, saturation: number, lightness: number): RgbType {
  let red: number, green: number, blue: number;
  // 将饱和度和亮度从百分比转换为小数
  saturation /= 100;
  lightness /= 100;

  if (saturation === 0) {
    // 无饱和度，返回灰色
    red = Math.round(lightness * 255);
    green = Math.round(lightness * 255);
    blue = Math.round(lightness * 255);
  } else {
    // 辅助函数：根据HSL值计算RGB值，处理不同的色相区间
    const convertHueToRgb = (baseValue: number, brightnessMultiplier: number, hueFraction: number): number => {
      // 确保hueFraction在0到1之间
      if (hueFraction < 0) {
        hueFraction += 1;
      }
      if (hueFraction > 1) {
        hueFraction -= 1;
      }
      // 第一个区间
      if (hueFraction < 1 / 6) {
        return baseValue + (brightnessMultiplier - baseValue) * 6 * hueFraction;
      }
      // 第二个区间
      if (hueFraction < 1 / 2) {
        return brightnessMultiplier;
      }
      // 第三个区间
      if (hueFraction < 2 / 3) {
        return baseValue + (brightnessMultiplier - baseValue) * (2 / 3 - hueFraction) * 6;
      }
      // 第四个区间
      return baseValue;
    };
    // 根据亮度计算中间值brightnessMultiplier和baseValue
    const brightnessMultiplier =
      lightness < 0.5 ? lightness * (1 + saturation) : lightness + saturation - lightness * saturation;
    const baseValue = 2 * lightness - brightnessMultiplier;
    // 计算RGB值
    red = Math.round(convertHueToRgb(baseValue, brightnessMultiplier, hue / 360 + 1 / 3) * 255);
    green = Math.round(convertHueToRgb(baseValue, brightnessMultiplier, hue / 360) * 255);
    blue = Math.round(convertHueToRgb(baseValue, brightnessMultiplier, hue / 360 - 1 / 3) * 255);
  }
  return {
    red: red,
    green: green,
    blue: blue
  };
}

// 将RGB颜色值转换为十六进制格式
function rgbToHex(red: number, green: number, blue: number): string {
  return '#' + ((1 << 24) + (red << 16) + (green << 8) + blue).toString(16).slice(1);
}

// 将十六进制颜色值转换为HSL颜色格式
export function hexToHsl(hex: string): HslType | null {
  // 将HEX类型颜色转为RGB类型
  let rgb = hexToRgb(hex);
  if (rgb === null) {
    return null;
  }
  // 将RGB类型颜色转为HSL类型
  return rgbToHsl(rgb.red, rgb.green, rgb.blue);
}

// 将十六进制颜色字符串转换为RGB对象
export function hexToRgb(hex: string): RgbType | null {
  // 使用正则表达式匹配十六进制颜色字符串
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  if (result) {
    // 将匹配的十六进制值转换为十进制RGB值
    return {
      red: parseInt(result[1], 16),
      green: parseInt(result[2], 16),
      blue: parseInt(result[3], 16)
    };
  } else {
    // 如果输入无效，返回null
    return null;
  }
}

// 将RGB颜色值转换为HSL颜色对象
function rgbToHsl(red: number, green: number, blue: number): HslType {
  // 将RGB值归一化到0-1范围
  red /= 255;
  green /= 255;
  blue /= 255;
  // 计算最大值和最小值
  let max = Math.max(red, green, blue);
  let min = Math.min(red, green, blue);
  // 计算亮度lightness
  let hue: number = (max + min) / 2;
  let saturation: number = (max + min) / 2;
  let lightness: number = (max + min) / 2;

  if (max === min) {
    // 如果最大值和最小值相等，色相和饱和度为0
    hue = 0;
    saturation = 0;
  } else {
    let difference = max - min; // 计算色差
    // 计算饱和度saturation
    saturation = lightness > 0.5 ? difference / (2 - max - min) : difference / (max + min);
    // 计算色相hue
    if (max === red) {
      hue = (green - blue) / difference + (green < blue ? 6 : 0);
    } else if (max === green) {
      hue = (blue - red) / difference + 2;
    } else {
      hue = (red - green) / difference + 4;
    }
    hue *= 60; // 将色相转换为度数
  }
  // 返回HSL值，四舍五入后返回
  return { hue: Math.round(hue), saturation: Math.round(saturation * 100), lightness: Math.round(lightness * 100) };
}
```

运行示例参考如下：

```ts
import { hexToHsl, hslToHex } from '../Utils/ColorUtils';

@Entry
@Component
struct ColorPage {
  build() {
    Row() {
      Column({ space: 10 }) {
        Button("click me").onClick(() => {
          const color_hsl = hexToHsl("#DDDCC7");
          console.info("hexToHsl:" + JSON.stringify(color_hsl));
          if (color_hsl != null) {
            const color_change = hslToHex(color_hsl.hue, color_hsl.saturation + 10, color_hsl.lightness - 10);
            console.info("饱和度+10、亮度-10结果：" + color_change);
          }
        })
      }.width('100%')

    }.height('100%')
  }
}
```

## 常见FAQ

Q：将HEX转为HSL后，再将HSL转回HEX颜色值与初始不一致。

A：HEX转为HSL转换时，HEX需先转为RGB整数，再归一化为[0,1]范围的浮点数计算HSL值，此过程因浮点运算可能产生小数点后多位误差。HSL转为HEX时，需将HSL的百分比重新映射为RGB浮点数，再四舍五入到整数，产生误差。结合这两次转换可能导致最终结果与初始值不一致。
