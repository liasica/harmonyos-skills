---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-935
title: 自定义DatePicker实现不同日历效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义DatePicker实现不同日历效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6111cb59d281b1d413c872448bc2457ebe6986ce387c11b0b17b3380c9a431a2
---

## 问题现象

实现一个日期选择器，仅允许选择年份和月份，不显示具体的日期。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/4q18oYP_TNyjXoQ3LhT7HQ/zh-cn_image_0000002658799623.gif "点击放大")

## 背景知识

* [DatePickerDialog](../harmonyos-references/ts-methods-datepicker-dialog.md)是一个用于显示日期选择对话框的组件，用户可以在指定的日期范围内通过滑动或点击来选择具体的日期。
* [TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)是一个允许用户从一组预定义的选项中通过滑动选择文本内容的组件。

## 解决方案

* **方案一**：DatePickerOptions中提供相应属性mode可设置日期展示模式。具体可参考官网示例：[设置显示月、日列](../harmonyos-references/ts-methods-datepicker-dialog.md#示例8设置显示月日列)。该属性在HarmonyOS API18及以上版本支持。
* **方案二**：可通过TextPicker的多列模式自定义年月选择器。
  1. 使用range属性定义两列数据（第一列为年份，第二列为月份）。
  2. 结合onChange监听选择结果的变化。

  ```ts
  @Entry
  @Component
  struct TextPickerExample {
    private years: string[] =
      ['1990年', '1991年', '1992年', '1993年', '1994年', '1995年', '1996年', '1997年', '1998年', '1999年',
        '2000年', '2001年', '2002年', '2003年', '2004年', '2005年', '2006年', '2007年', '2008年', '2009年', '2010年',
        '2011年', '2012年',
        '2013年', '2014年', '2015年', '2016年', '2017年', '2018年', '2019年', '2020年', '2021年', '2022年', '2023年',
        '2024年', '2025年',
        '2026年', '2027年', '2028年', '2029年', '2030年'];
    private months: string[] = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
    private multi: string[][] = [this.years, this.months];

    build() {
      Column() {
        TextPicker({ range: this.multi })
          .onChange((value: string | string[], index: number | number[]) => {
            console.info(`TextPicker 多列:onChange ${value}, index: ${index}`);
          }).margin(50)
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
