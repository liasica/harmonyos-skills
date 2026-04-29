---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-tool
title: hilogtool
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > hilogtool
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:21+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f475d9c6f8f16d5f58052c2ae8ec717f664128e42e5d26b0cf7397cae07ad645
---

## 使用场景

当前hilog日志为编码后二进制形式保存的gz格式文件，开发者从设备/data/log/hilog路径下导出后无法直接解压查看，需要使用hilogtool工具进行解析，将转换为明文hilog日志。

说明

当前机制下：kmsg日志不受影响，可直接查看；hilog日志，在shell窗口直接使用hilog命令在线查看日志，不受影响。

## 使用指导

### 工具获取

下载HarmonyOS SDK，hilogtool解析工具默认在对应平台的 hms/toolchains目录下。

### 环境配置

**Windows环境变量设置方法**

在此电脑 > 属性 > 高级系统设置 > 高级 > 环境变量 > Path > 编辑 中，将hilogtool.exe所在路径添加到 Path，环境变量配置完成后，请重启电脑，即可在cmd 窗口执行hilogtool命令。

**MacOS环境变量设置方法**

1. 打开终端工具，执行以下命令，根据输出结果分别执行不同命令。

   ```
   1. echo $SHELL
   ```

   如果输出结果为/bin/bash，则执行以下命令，打开.bash\_profile文件。

   ```
   1. vi ~/.bash_profile
   ```

   如果输出结果为/bin/zsh，则执行以下命令，打开.zshrc文件。

   ```
   1. vi ~/.zshrc
   ```
2. 单击字母“i”，进入Insert模式。
3. 输入以下内容，添加PATH信息。

   ```
   1. export PATH=$PATH:/path/to/your/hilogtool
   ```
4. 编辑完成后，单击Esc键，退出编辑模式，然后输入“:wq”，单击Enter键保存。
5. 执行以下命令，使配置的环境变量生效。

   如果步骤1打开的是.bash\_profile文件，请执行如下命令：

   ```
   1. source ~/.bash_profile
   ```

   如果步骤1打开的是.zshrc文件，请执行如下命令：

   ```
   1. source ~/.zshrc
   ```
6. 环境变量配置完成后，重启电脑。

### 使用方法

**命令：**

hilogtool parse -i xxx -o xxx -d xxx

hilogtool parse --input xxx --output xxx --dict xxx

**解析命令参数列表：**

| 选项 | 描述 | 举例 |
| --- | --- | --- |
| -h/--help | 查看帮助使用文档。 | hilogtool -h |
| -i/–-input inputDir | 用于指定输入路径，会扫描该目录下所有的hilog流水日志文件并进行解析；  缺省时，为命令行当前所在路径。 | 解析指定目录(D:\temp\hilog)下的所有hilog文件：  hilogtool parse -i D:\temp\hilog  解析当前目录下的所有hilog文件：  hilogtool parse -i .\ |
| -i/–-input inputFile | 解析指定的单个hilog文件。 | 解析指定的hilog文件:  hilogtool parse -i D:\temp\data\log\hilog.706.20230711-071816.gz  hilogtool parse -i .\hilog.706.20230711-071816.gz |
| -o/–-output outputDir | 用于指定输出路径，即解析后的日志文件保存路径；  缺省时，为解析的hilog原日志文件所在路径。 | 解析当前目录下的日志文件到D:\temp目录:  hilogtool parse -i .\ -o D:\temp |
| -d/--dict dictFile | 用于指定数据字典的路径；  缺省时，会在命令行当前所在路径下匹配最新的数据字典文件（格式：hilog\_dict.20230908-142200.zip）。 | 解析指定目录(D:\temp\hilog)下的所有hilog文件，并且指定使用该目录下的数据字典：  hilogtool parse -i D:\temp\hilog -d D:\temp\hilog\hilog\_dict.20230908-142200.zip |
| -v/--version | 查看当前版本号。 | hilogtool -v |

说明

1.数据字典文件在data/log/hilog目录下，格式为：hilog\_dict.2024xxxx-xxxxxx.zip，是设备启动时自动生成的，在解析日志时需要这个文件。

若缺少数据字典，会导致部分日志解析失败；重启设备可以重新生成该数据字典。

2.落盘的hilog日志文件默认格式为hilog\.\d{3}\.\d{8}-\d{6}\.gz$，若开发过程中使用了hilog -w start -f xxx 命令自定义了落盘文件名，可能导致日志无法被正常解析，需要升级hilogtool工具至1.0.0b版本及以上，才支持解析自定义文件名的hilog日志。

## 常用解析命令示例

### 解析当前目录下所有的hilog文件（推荐）

在当前日志所在目录，通过cmd进入shell窗口，在shell窗口直接执行hilogtool parse，即可进行解析操作，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/INqj5zE3SXaC5vcUFJC-bQ/zh-cn_image_0000002589324873.png?HW-CC-KV=V1&HW-CC-Date=20260429T053420Z&HW-CC-Expire=86400&HW-CC-Sign=FBF3815F796428A4C5AF8D033B77036233DA322E2BF5F6DBE570769F3EC3819D)

### 解析指定目录下的hilog文件

hilogtool parse -i D:\09-temp\dict-test -d D:\09-temp\dict-test

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/HuJMqmiuS6K9yOflhzUTZw/zh-cn_image_0000002589244809.png?HW-CC-KV=V1&HW-CC-Date=20260429T053420Z&HW-CC-Expire=86400&HW-CC-Sign=06723225D9DF95B9D8228DA05B19D8B00D04CB006C25023EE6554D4712137C08)

### 解析单个hilog文件

hilogtool parse -i D:\09-temp\dict-test\hilog.025.20231020-154659.gz -d D:\09-temp\dict-test

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/iOSHaf-zRNuw6ZMkTxr4wQ/zh-cn_image_0000002558765004.png?HW-CC-KV=V1&HW-CC-Date=20260429T053420Z&HW-CC-Expire=86400&HW-CC-Sign=9CCCFB3A5D9B6DA3ACD2ADC2A8FE1EADF68CBE4115968AF1FC295B124F2A7A10)

## 自动化脚本

自动化调试脚本，将脚本与hilogtool工具放在同一目录下，执行get\_hilog.bat，脚本会导出设备中的data/log/hilog日志，并且自动解析生成明文日志。

### windows平台脚本

windows平台 get\_hilog.bat 脚本内容参考：

```
1. @set Ymd=%date:~0,4%_%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
2. @set Ymd=%Ymd: =0%
3. @set Dir=LOG_%YMD%
4. md %Dir%
5. hdc file recv /data/log/hilog/ .\%Dir%\
6. hilogtool parse -i .\%Dir% -d .\%Dir%
7. pause
```

脚本运行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/La4zKxnpRy-RlIvBkybFyg/zh-cn_image_0000002558605348.png?HW-CC-KV=V1&HW-CC-Date=20260429T053420Z&HW-CC-Expire=86400&HW-CC-Sign=7E78BEE47D24FE055A58ED3A4E1D72EE0F3467109155108BA9E0676BF76A1275)

### mac平台脚本

mac平台脚本内容参考：

```
1. Ymd=$(date "+%Y_%m%d_%H%M%S")
2. Dir=LOG_$Ymd
3. mkdir $Dir
4. hdc file recv /data/log/hilog/ ./$Dir/
5. ./hilogtool parse -i ./$Dir -d ./$Dir
```

## 可能有影响的场景

### 自动化分析日志

部分领域涉及到自动化分析/data/log/hilog目录下的明文日志文件，目前hilog轻量化后，日志以二进制保存，需要使用上述解析工具适配一下自动化反编译二进制日志动作。

### 日志转发他人

直接从手机/data/log/hilog目录下recv出来的日志文件为二进制日志文件，直接发送给他人，无法正常查看，建议解析后再发送，或者将二进制日志文件与数据字典一同转发。

## 错误码

| 错误码 | 含义 | 处理方法 |
| --- | --- | --- |
| 200 | 解码成功 | 不涉及 |
| 300 | 解码失败，存在部分领域的日志和字典不匹配 | 1.只有部分日志解析失败，一般不影响开发自调试，可不用关注  2、若影响自调试，可参考下方常见问题，增量生成数据字典 |
| 500 | 解析工具版本不匹配 | 更新hilogtool解析工具版本 |
| 999 | 日志是明文落盘的，不需要解析 | 不涉及 |

## 常见问题

**问题现象**

工具解析时，显示 there is no hilog dict zip in xxx, use -d to specify ，或者 open dict xxx fail, errno is: No such file or directory

解析完的日志中，显示 OpenUuidFile fail, unknown log, uuid is: xxxxxx

**可能原因**

解析日志时，未找到对应的数据字典导致的。

**解决措施**

1、解析命令使用错误，具体参考[常用解析命令示例](hilog-tool.md#常用解析命令示例)。

2、开发本地替换bin/so调试的场景，需要触发生成新的数据字典，才能解析，以下触发命令三选一即可。

（1）使用增量生成数据字典命令：hilog -d xxx

例如推送hilog相关测试程序bin文件hilogTest到 /system/bin/下面，想查看hilogTest打印的日志，需要执行以下命令，增量生成hilogTest的数据字典：

hdc shell hilog -d /system/bin/hilogTest

数据字典生成成功后hilogTest则可以正常打印日志。

（2）重启hilogd：service\_control stop hilogd && service\_control start hilogd

（3）重启设备；

3、数据字典被删掉了，检查导出的日志中是否存在hilog\_dict.2024xxxx-xxxxxx.zip格式的数据字典文件

若不存在，则大概率是被 rm -rf data/log/hilog/\* 命令删除掉了，需要重启设备生成新的数据字典，然后解析。
