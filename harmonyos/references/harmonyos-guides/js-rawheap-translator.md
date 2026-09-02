---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-rawheap-translator
title: js-rawheap-translator工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > 命令行工具 > js-rawheap-translator工具
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:ea8cb8d877e416ceb0eccfe82d104fc1a59d5f1de7cbf1545299848d7af35aef
---

## 使用场景

为方便开发者定位问题，应用在ArkWeb或JSVM的JS堆内存OOM（Out of Memory）时会自动进行HeapDump。此操作会将虚拟机当前堆上的所有对象信息保存在后缀为.rawheap的二进制文件中。开发者可使用js\_rawheap\_translator工具解析.rawheap文件，生成.heapsnapshot文件。该文件可通过DevEco Studio的[Heap Snapshot离线导入](ide-snapshot-basic-operations.md#section6760173514388)或Chrome浏览器的开发者工具中的内存工具导入并查看。

## 使用指导

### 工具获取

此工具支持Windows、Linux和macOS平台，获取方法如下：

* SDK中获取：sdk/default/openharmony/toolchains/js\_rawheap\_translator，适用于各平台。

### 环境配置

建议将js\_rawheap\_translator工具所在的路径配置为系统环境变量。这样可以在终端中直接使用工具，无需每次指定路径。

在不同系统中，环境变量的配置方法存在差异。以下提供一些配置示例，供开发者参考。

* Windows环境变量设置方法（以Windows 10某版本为例）。

  1. 右键点击“此电脑”选择“属性”选项。
  2. 在弹出的窗口中，找到并点击“高级系统设置”标签。
  3. 在弹出的窗口中，找到并点击“高级”页签下的“环境变量”按钮。
  4. 在弹出的窗口中，找到并双击“系统变量”框中的“Path”变量。
  5. 在弹出的窗口中，找到并点击“新建”按钮。
  6. 将本地存放js\_rawheap\_translator工具的文件路径填至新建的文本框中。
  7. 点击“确定”按钮关闭所有弹出的窗口。
  8. 重启终端。
* macOS环境变量设置方法（以macOS 15某版本为例）。

  1. 打开终端工具，执行以下命令。

     ```bash
     echo $SHELL
     ```
  2. 根据步骤1的返回结果做如下对应处理。

     a. 如果返回结果为/bin/bash，则执行以下命令：

     ```bash
     echo 'export PATH=$PATH:/path/to/your/js_rawheap_translator' >> ~/.bash_profile
     source ~/.bash_profile
     ```

     b. 如果返回结果为/bin/zsh，则执行以下命令：

     ```bash
     echo 'export PATH=$PATH:/path/to/your/js_rawheap_translator' >> ~/.zshrc
     source ~/.zshrc
     ```
* Linux环境变量设置方法。

  1. 打开终端工具，执行以下命令查看当前Shell。

     ```bash
     echo $SHELL
     ```
  2. 根据步骤1的返回结果做如下对应处理。

     a. 如果返回结果为/bin/bash，则执行以下命令：

     ```bash
     echo 'export PATH=$PATH:/path/to/your/js_rawheap_translator' >> ~/.bash_profile
     source ~/.bash_profile
     ```

     b. 如果返回结果为/bin/zsh，则执行以下命令：

     ```bash
     echo 'export PATH=$PATH:/path/to/your/js_rawheap_translator' >> ~/.zshrc
     source ~/.zshrc
     ```

## 使用方法

### 解析命令

```bash
js_rawheap_translator --translate <input.rawheap> [--translate-out <output.heapsnapshot>] [v8 flags]
```

### 参数列表

| 选项 | 必选 | 描述 |
| --- | --- | --- |
| --translate <input.rawheap> | 是 | 需要解析的JS堆OOM时生成的.rawheap文件路径。 |
| --translate-out <output.heapsnapshot> | 否 | 解析生成的heapsnapshot文件路径，路径必须具有读写权限。  参数缺省时，默认为当前执行命令的路径。  参数给定时，文件的后缀名必须是heapsnapshot。 |
| [v8 flags] | 否 | 可附加v8相关的命令行参数。 |

## 解析命令示例

### 解析示例

Windows系统中解析示例

打开cmd并进入rawheap文件路径，调用解析工具命令，指定在当前路径下生成heapsnapshot文件。

```bash
> js_rawheap_translator.exe --translate test.rawheap --translate-out test.heapsnapshot
```

Linux系统中解析示例

进入rawheap文件路径，调用解析工具命令，指定在当前路径下生成heapsnapshot文件。

```bash
> ./js_rawheap_translator --translate test.rawheap --translate-out test.heapsnapshot
```

macOS系统中解析示例

打开终端并进入rawheap文件路径，调用解析工具命令，指定在当前路径下生成heapsnapshot文件。

```bash
> js_rawheap_translator --translate test.rawheap --translate-out test.heapsnapshot
```

仅指定输入文件，使用默认输出路径示例

```bash
> js_rawheap_translator --translate test.rawheap
```

参考输出

```bash
binary reader file size:xxxxx
[HeapDump]print header_: magic_: 0x56384844, dump_format_version_: 1, flags_: 0xf37 {...}, ... v8_version: 14.4.258.16, ...
[HeapDump][HeapDump]elapsed time: xxx.xxxxx ms
[HeapDump]fd closed
```

## 文件参考规格

rawheap文件的大小和生成耗时与当前JS堆内存大小及存活对象数量呈强正相关。当JS堆内存占用较大、存活对象数量较多时，生成的rawheap文件会更大，耗时也会更长。

## 常见问题

### 工具版本不匹配

**问题现象**

工具解析时会提示版本不匹配错误。

**原因**

当前工具版本低于rawheap文件版本。

**解决措施**

升级工具版本至匹配版本可解决此问题。

### 文件无法打开

**问题现象**

工具解析时，提示：open file failed

**原因**

指定的输入文件不存在或输出文件路径没有写入权限。

**解决措施**

确认输入文件路径正确，或更改到有写权限的路径可以解决。

### 参数格式错误

**问题现象**

工具解析时，提示参数错误信息。

**原因**

命令参数格式不正确。

**解决措施**

使用js\_rawheap\_translator --help查看正确的参数格式。
