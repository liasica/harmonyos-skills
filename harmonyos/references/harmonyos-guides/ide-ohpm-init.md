---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-init
title: ohpm init
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm init
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:41+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:c9cbae538b3a604b68d6e434f1de2bcedb0c57cb5fc50d71f4c6a1b3cfc8fd8d
---

创建 oh-package.json5 文件。

## 命令格式

```
1. ohpm init [options]
```

## 功能描述

在工作目录下，生成一个新的 oh-package.json5 文件，初始化一个 package。

执行命令时，命令行会出现交互界面，可填写一系列关于三方库的基本信息，例如：三方库名称、版本等。ohpm 会根据现有字段、依赖项和所选选项做出合理的猜测，它会保留已设置的任何字段和值，在工作目录下创建一个 oh-package.json5 文件。

## Options

### yes

* 默认值：null
* 类型：null 或 Boolean
* 别名：y

可以在 init 命令后面指定 -y或者--yes 参数，命令行将会完全跳过交互界面，创建默认的 oh-package.json5 文件。

默认内容如下：

```
1. {
2. "name": "work_dir",
3. "version": "1.0.0",
4. "description": "",
5. "main": "Index.ets",
6. "author": "",
7. "license": "ISC",
8. "dependencies": {}
9. }
```

说明

若当前工作目录下不存在 oh-package.json5 文件，则文件中 name 字段默认为当前工作目录名称；若当前工作目录下已存在 oh-package.json5 文件，则新文件中 name 字段复用已存在文件中的 name 字段，并且最后覆盖原有oh-package.json5文件。

### group

* 默认值：当前项目的命名空间 或 ""
* 类型：String
* 别名：g

可以在 init 命令后面配置 -g <group\_name> 或者 --group <group\_name>参数，创建一个 oh-package.json5 文件，其中 name 字段的命名空间为 @group\_name。

### log\_level

* 默认值：无
* 类型： string

从ohpm 6.0.2.636版本开始，可以在 init 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

* 当前工作目录下不存在 oh-package.json5 文件。

  在" D:\demo " 路径下，执行如下命令：

  ```
  1. ohpm init -y
  ```

  执行结果为：

  ```
  1. Wrote to D:\demo\oh-package.json5:

  3. {
  4. "name": "demo",
  5. "version": "1.0.0",
  6. "description": "",
  7. "main": "Index.ets",
  8. "author": "",
  9. "license": "ISC",
  10. "dependencies": {}
  11. }
  ```
* 当前工作目录下已存在其中 name 字段为 demo\_name 的 oh-package.json5 文件。

  在" D:\demo " 路径下，执行如下命令：

  ```
  1. ohpm init -y
  ```

  执行结果为：

  ```
  1. Wrote to D:\demo\oh-package.json5:

  3. {
  4. "name": "demo_name",
  5. "version": "1.0.0",
  6. "description": "",
  7. "main": "Index.ets",
  8. "author": "",
  9. "license": "ISC",
  10. "dependencies": {}
  11. }
  ```
* 创建一个 oh-package.json5 文件，其中参数 name 字段为 "@group\_name/demo" ，而不是仅为 "demo"。

  ```
  1. ohpm init -g group_name
  ```

  执行结果为：示例中 name 字段自动显示为 @group\_name/demo。

  ```
  1. package name: (@group_name/demo)
  ```
