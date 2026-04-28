---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-file
title: 文件组织
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 框架说明 > 文件组织
category: harmonyos-references
scraped_at: 2026-04-28T08:03:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:406c9468c41e7b3692949ee9a0baf06b5fcc827d115c885ec969955c01c8fd4c
---

## 目录结构

PhonePC/2in1TabletTVWearable

JS服务卡片(entry/src/main/js/Widget)的典型开发目录结构如下：

```
1. ├─widget
2. │   ├─common
3. │   │   └─widget.png
4. │   ├─i18n
5. │   │   ├─en-US.json
6. │   │   └─zh-CN.json
7. │   └─pages
8. │       └─index
9. │           ├─index.css
10. │           ├─index.hml
11. │           └─index.json
```

目录结构中文件分类如下：

* .hml结尾的HML模板文件，这个文件用来描述卡片页面的模板布局结构。
* .css结尾的CSS样式文件，这个文件用于描述页面样式。
* .json结尾的JSON配置文件，这个文件用于配置卡片中使用的变量action事件。

各个文件夹的作用：

* pages目录用于存放卡片模板页面。
* common目录用于存放公共资源文件，比如：图片资源。
* i18n目录用于配置不同语言场景资源内容，比如应用文本词条，图片路径等资源。

## 文件访问规则

PhonePC/2in1TabletTVWearable

应用资源可通过绝对路径或相对路径的方式进行访问，本开发框架中绝对路径以"/"开头，相对路径以"./"或"../"。具体访问规则如下：

* 引用代码文件，需使用相对路径，比如：../common/style.css。
* 引用资源文件，推荐使用绝对路径。比如：/common/test.png。
* 公共代码文件和资源文件推荐放在common下，通过规则1和规则2进行访问。
* CSS样式文件中通过url()函数创建<url>数据类型，如：url(/common/test.png)。

说明

当代码文件A需要引用代码文件B时：

* 如果代码文件A和文件B位于同一目录，则代码文件B引用资源文件时可使用相对路径，也可使用绝对路径。
* 如果代码文件A和文件B位于不同目录，则代码文件B引用资源文件时必须使用绝对路径。因为Webpack打包时，代码文件B的目录会发生变化。
* 在json文件中定义的数据为资源文件路径时，需使用绝对路径。

## 配置文件

PhonePC/2in1TabletTVWearable

FA卡片需要在应用配置文件config.json中进行配置。详细的配置内容请参考[应用配置文件概述（FA模型）](../harmonyos-guides/application-configuration-file-overview-fa.md)。

Stage卡片需要在应用配置文件module.json5中的extensionAbilities标签下，配置ExtensionAbility相关信息。详细的配置内容请参考[应用配置文件概述（Stage模型）](../harmonyos-guides/application-configuration-file-overview-stage.md)。
