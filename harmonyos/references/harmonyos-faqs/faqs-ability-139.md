---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-139
title: 应用安装后，文件预览可用的打开方式不正确
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用安装后，文件预览可用的打开方式不正确
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dfe2947303a08c6192cdb333686051a8c5c22e897a21a624603378b37fcdf7a9
---

## 问题现象

应用安装后，文件预览时（比如：mp4视频文件），弹窗显示的可用打开方式包含该应用，但是并不能正常打开此文件。

## 背景知识

* [skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)：该标签标识UIAbility组件或者ExtensionAbility组件能够接收的Want的特征。
* [拉起文件处理类应用](../harmonyos-guides/file-processing-apps-startup.md)：开发者可以通过调用startAbility接口，由系统从已安装的应用中寻找符合要求的应用，打开特定文件。
* [utd预置类型](../harmonyos-guides/uniform-data-type-list.md)：为了方便业务使用，系统中预置了一部分常用类型，从通用性、场景以及归属等角度将预置类型分为三类：基础类型，系统关联类型以及应用定义类型。

## 问题定位

1. 在文件管理器中，选择一个mp4视频文件，在更多选项->其他应用打开，拉起可打开视频文件的应用，安装的应用在列表中，说明不是拉起方适配的问题，是应用skills能力配置的问题。
2. 排查工程配置，在module.json5里配置了如下skills：

   ```json
   "skills": [
     {
       "actions": [
         "ohos.want.action.viewData"
         // 必填，声明数据处理能力
       ],
       "uris": [
         {
           "scheme": "file",
           // 必填，声明协议类型为文件
           "type": "general.video",
           // 必填，表示支持打开的文件类型，支持MIME和UniformDataType
           "linkFeature": "FileOpen"
           // 必填且大小写敏感，表示此URI的功能为文件打开
         }
       ]
     }
   ]
   ```

   该配置表明此应用具有打开视频文件的能力，因此系统为视频文件选择打开方式时匹配上了该应用。

## 分析结论

因为应用错误的配置了skills参数，导致系统按照匹配规则为该类型文件的打开方式匹配到了应用。

## 修改建议

应用按照实际能提供的能力配置skills参数，如文本处理应用只配置打开文本类型文件的能力。

例如：

```json
"skills": [
  {
    "actions": [
      "ohos.want.action.viewData"
      // 必填，声明数据处理能力
    ],
    "uris": [
      {
        "scheme": "file",
        // 必填，声明协议类型为文件
        "type": "general.plain-text",
        // 必填，表示支持打开的文件类型，支持MIME和UniformDataType
        "linkFeature": "FileOpen"
        // 必填且大小写敏感，表示此URI的功能为文件打开
      }
    ]
  }
]
```
