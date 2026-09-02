---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-arktsdoc
title: ArkTSDoc文档生成工具（arktsdoc）
breadcrumb: 指南 > 命令行工具 > ArkTSDoc文档生成工具（arktsdoc）
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:63478a89b480cda08407acf4aab2432c8f7433387b952d52106a333b3bb29851
---

## 简介

从26.0.0版本开始，Command Line Tools集成arktsdoc工具，支持通过arktsdoc命令行将代码文件中的变量、方法、接口、类等需要对外暴露的信息快速生成相应的参考文档（ArkTSDoc文档）。

arktsdoc命令行格式为：

```screen
arktsdoc [options] [dir]
```

options：可选，命令行的配置参数，具体请参考[表1](ide-command-line-arktsdoc.md#table25697717185)。

dir：可选，绝对路径或相对路径。

**说明** 

* 若命令行中输入的路径包含"$"、"|"、"<"、">"、"%"、"^"、","、":"、"="、"\*"等特殊字符，命令可能会解析异常，导致参考文档导出失败。建议用引号包裹路径字符串，或删除路径中的特殊字符。
* 因操作系统差异导致的参数解析问题，请开发者处理使命令参数符合规格，保证可正常解析。

**表1** arktsdoc命令行配置参数

| 参数 | 说明 |
| --- | --- |
| --help/-h | 查看arktsdoc命令行的帮助信息。 |
| --version/-v | 查看arktsdoc命令行的版本信息。 |
| --workspace/-w | 可选，指定工程根目录，支持绝对路径和相对路径，最多指定一个工程。  默认为当前命令行执行的目录。 |
| --input/-i | 可选，指定工程/模块/文件/目录的路径，设置ArkTSDoc文档的生成范围，支持绝对路径和相对路径（相对于项目路径）。  支持指定多个路径，各路径使用英文;分隔，整个路径字符串使用引号包裹。 |
| --exclude/-e | 可选，生成ArkTSDoc文档时，无需被导出的文件/目录的路径，支持绝对路径和相对路径。  支持指定多个路径，各路径使用英文;分隔，整个路径字符串使用引号包裹。  支持Ant风格的路径匹配模式。在Ant风格中，使用'?'匹配单字符、'\*'匹配单层目录/文件、'\*\*'匹配任意层目录等。 |
| --destination/-d | 可选，用于指定ArkTSDoc文档导出时的存储位置，支持相对路径和绝对路径。  默认在当前命令行执行目录下创建一个output目录，存放ArkTSDoc文档。 |

## 环境准备

arktsdoc工具在Command Line Tools的bin目录下，执行命令前，需要[将bin目录配置到PATH变量中](ide-commandline-get.md#section17776863449)。

## 使用示例

* 查看帮助

  ```bash
  arktsdoc -h
  Usage:  arktsdoc [options] [dir] 
  Options: 
        -h, --help                         Display help for command 
        -e, --exclude [excludePaths]       Indicates the excludePaths of project. Optional.
        -i, --input <input>                Indicates the input file/directory.
        -w, --workspace <path>             Indicates the project path of current path.
        -d, --destination <path>           Indicates the path of the generation result.
        -v, --version                      Display the version number and quit.
  ```
* 查看arktsdoc命令行版本

  ```bash
  arktsdoc -v
  ```
* 缺省options和dir

  导出当前命令行执行目录下整个工程的ArkTSDoc文档，输出到当前目录下的output目录中。若当前目录非工程根目录，则会导出失败并提示对应报错信息。

  ```bash
  arktsdoc
  ```
* 指定工程根目录

  导出指定工程的ArkTSDoc文档，输出到该工程下的output目录中。若指定目录非工程根目录或目录不存在，则会导出失败并提示对应报错信息。

  ```bash
  arktsdoc -w D:\MyApplication
  ```
* 指定目标文件

  导出entry目录下的ArkTSDoc文档，输出到工程下的output目录中。如果entry目录不存在，则会导出失败并提示对应报错信息。

  ```bash
  arktsdoc -w D:\MyApplication -i entry
  ```

* 导出忽略部分目录

  导出entry目录下的ArkTSDoc文档时，无需导出entry/test目录，输出到工程下的output目录中。如果被忽略目录不存在，则忽略排除指令，正常导出。

  ```bash
  arktsdoc -w D:\MyApplication -i entry -e entry/test
  ```
* 指定输出目录

  将生成的ArkTSDoc文档输出到D:\doc目录中。若输入的路径不存在，则会导出失败并提示对应报错信息。

  ```bash
  arktsdoc -w D:\MyApplication -i entry -e entry/test -d D:\doc
  ```
