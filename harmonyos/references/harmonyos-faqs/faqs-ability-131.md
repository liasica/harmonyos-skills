---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-131
title: 启动页未铺满屏幕、边缘出现黑边
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 启动页未铺满屏幕、边缘出现黑边
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:840250a836d244e44ca489572b28cfbc8913bb944c8fb7a9cdbe3029d7b840d2
---

## 问题现象

进入应用时，启动页未铺满屏幕，屏幕边缘显示黑边。

## 背景知识

1. 启动页分为简易启动页和增强启动页，开发者通过在module.json5配置文件中的abilities标签配置启动页资源，涉及的对应字段及含义详见[启动页的分类和实现方式](../harmonyos-guides/launch-page-config.md#启动页的分类和实现方式)。
2. startWindow字段提供了[配置增强启动页](../harmonyos-guides/launch-page-config.md#配置增强启动页)的能力，可用于元素更复杂的启动页配置。同时，相应资源也具备根据窗口尺寸进行缩放的能力，更易于多设备适配设计。
3. 启动页中的图片资源支持的文件格式同[Image](../harmonyos-references/ts-basic-components-image.md)组件，考虑到解码性能和显示效果，建议启动页中使用jpg或png格式的图片资源。
4. 二级json文件中startWindowBackgroundImageFit字段的配置项如下：
   * "Contain"：保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。
   * "Cover"：保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。
   * "Auto"：图像会根据其自身尺寸和组件的尺寸进行适当缩放，以在保持比例的同时填充视图。
   * "Fill"：不保持宽高比进行放大缩小，使得图片充满显示边界。
   * "ScaleDown"：保持宽高比显示，图片缩小或者保持不变。
   * "None"：保持原有尺寸显示。

## 问题定位

1. 查看是否在module.json5的abilities标签中配置新增startWindow字段指向二级配置json文件，以启用启动页增强配置。参考文件名及路径为resources/base/profile/start\_window.json。

   ```ts
   // entry模块的module.json5配置文件
   "startWindow": "$profile:start_window"
   ```
2. 查看二级json文件配置的具体字段。
   * 通过startWindowBackgroundColor查看背景色设置情况，背景色显示层级最低，填充整个窗口，查看背景色是否配置为黑色。
   * 通过startWindowBackgroundImage查看图片资源设置情况，将整个窗口作为背景资源容器，填充方式由startWindowBackgroundImageFit字段指定。
   * 查看startWindowBackgroundImageFit字段的配置情况。
   * 查看startWindowBackgroundImageFit字段的配置情况。若startWindowBackgroundImageFit字段配置为"Contain"、"ScaleDown"或"None"，则会导致图片无法填充视图。

     ```ts
     // resources/base/profile/start_window.json
     {
       "startWindowBackgroundColor": "$color:start_window_background", // color.json中背景色设为黑色
       "startWindowBackgroundImage": "$media:bgImage",
       "startWindowBackgroundImageFit": "Contain"
     }
     ```

## 分析结论

在启动页资源配置时，通过startWindowBackgroundColor字段将背景色配置为黑色，且startWindowBackgroundImageFit字段配置为"Contain"、"ScaleDown"或"None"，则会导致图片无法填满视图，屏幕边缘显示黑边。

## 修改建议

将[startWindow标签](../harmonyos-guides/module-configuration-file.md#startwindow标签)配置文件中的startWindowBackgroundImageFit字段配置为"Cover"、"Auto"或"Fill"，确保图片能够填充视图，使得启动页铺满屏幕。
