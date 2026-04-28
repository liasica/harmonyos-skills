---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-config
title: ohpm config
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm config
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:40+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:976f34348a8212dd7d85b85d62c6e9655192b4f517a5e77acc595f0dcc2de7bc
---

设置ohpm用户级配置项。

## 命令格式

```
1. ohpm config set <key> <value>
2. ohpm config get <key>
3. ohpm config delete <key>
4. ohpm config list
5. ohpm config encrypt [options]
```

说明

配置文件中信息以键值对<key> = <value>形式存在。

## 功能描述

ohpm 从命令行和 .ohpmrc 文件中获取其配置设置。有关更多 .ohpmrc 文件信息和可用配置选项，请参阅 [ohpmrc](ide-ohpmrc.md) 章节。

注意

ohpm config 仅支持配置项字段（默认项字段请查阅 [ohpmrc](ide-ohpmrc.md#zh-cn_topic_0000001792216397_默认配置项) 章节），且仅支持修改**用户级目录**下的 .ohpmrc 文件。

## 子命令

### set

```
1. ohpm config set <key> <value>
```

在用户级目录下 .ohpmrc 文件中，以键值对<key> = <value>形式写入数据。

**示例**

1. 以配置项"log\_level"为例，修改其值为debug（可选值：debug、info、warn、error）：

   ```
   1. ohpm config set log_level debug
   ```
2. 成功执行后，在用户目录/.ohpm/.ohpmrc文件中将显示log\_level=debug。

### get

```
1. ohpm config get <key>
```

将从命令行，项目级 .ohpmrc 文件，用户级 .ohpmrc 文件（优先级依次递减）中获取的值进行标准输出。

如果未提供键值，则此命令执行效果与命令 ohpm config list 相同。

**示例1**

1. 以项目级.ohpmrc中log\_level=info，用户级.ohpmrc中log\_level=debug为例，在工程任意目录下执行如下命令。

   ```
   1. ohpm config get log_level
   ```
2. 成功执行后，在控制台打印log\_level的值。

   ```
   1. info
   ```

**示例2**

1. 基于示例1，将项目级.ohpmrc删除，再次执行get命令。

   ```
   1. ohpm config get log_level
   ```
2. 成功执行后，在控制台打印log\_level的值。

   ```
   1. debug
   ```

**示例3**

1. 未提供<key>值时执行命令ohpm config get。

   ```
   1. ohpm config get
   ```
2. 成功执行后，将在控制台打印所有.ohpmrc配置。

   ```
   1. ; "user" config from C:\Users\username\.ohpm\.ohpmrc

   3. registry="http://localhost:8088/repos/ohpm"
   4. strict_ssl = false
   5. log_level = "debug"

   7. ; "user" config from C:\Users\username\.ohpm\.ohpmrc
   8. ; node bin location = C:\Program Files\nodejs\node.exe
   9. ; node version = v18.19.1
   10. ; ohpm local prefix = C:\Users\username
   11. ; ohpm version = 5.1.2-rc.2
   12. ; cwd = C:\Users\username
   13. ; HOME = C:\Users\username
   ```

### list

```
1. ohpm config list
2. alias: ls
```

显示所有配置项。

**示例**

1. 执行list命令。

   ```
   1. ohpm config list 或者 ohpm config ls
   ```
2. 成功执行后，将在控制台打印所有.ohpmrc配置。

   ```
   1. ; "user" config from C:\Users\username\.ohpm\.ohpmrc

   3. registry="http://localhost:8088/repos/ohpm"
   4. strict_ssl = false
   5. log_level = "debug"

   7. ; "user" config from C:\Users\username\.ohpm\.ohpmrc
   8. ; node bin location = C:\Program Files\nodejs\node.exe
   9. ; node version = v18.19.1
   10. ; ohpm local prefix = C:\Users\username
   11. ; ohpm version = 5.1.2-rc.2
   12. ; cwd = C:\Users\username
   13. ; HOME = C:\Users\username
   ```

### delete

```
1. ohpm config delete <key>
```

删除用户级目录下 ohpmrc 文件中指定的键值。

**示例**

1. 用户.ohpmrc中原始内容。

   ```
   1. registry=http://localhost:8088/repos/ohpm
   2. strict_ssl=false
   3. log_level=debug
   ```
2. 执行delete命令。

   ```
   1. ohpm config delete registry
   ```
3. 成功执行后，.ohpmrc内容如下。

   ```
   1. strict_ssl=false
   2. log_level=debug
   ```

### encrypt

```
1. ohpm config encrypt [options]
```

使用加密组件加密标准输入的数据，并输出密文到标准输出。

**首次使用**：

* 必须在 config encrypt 命令后面配置 [--crypto\_path <string>](ide-ohpm-config.md#section313318216424) 生成新的加密组件，并用于数据加密。

  **示例**

  1. 执行 encrypt --crypto\_path <string> 命令，指定的路径为空目录。

     ```
     1. ohpm config encrypt --crypto_path D:\path\to\empty_dir
     ```
  2. 成功执行后，在指定路径生成新的加密组件，并对用户输入内容进行加密，其中用户输入内容不可见。

     ```
     1. ohpm INFO: Attempted to create an crypto component at the "D:\path\to\empty_dir" path...
     2. ohpm INFO: The crypto component has been created successfully.
     3. Please enter the password to be encrypted:
     4. ohpm INFO: encrypted result:
     5. security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
     ```
  3. 将生成的加密组件路径配置到 .ohpmrc 文件中，方便后续自动读取加密组件。

     ```
     1. crypto_path=D:\path\to\empty_dir
     ```

**非首次使用：**

* 若不指定 [--crypto\_path](ide-ohpm-config.md#section313318216424)，则自动从 .ohpmrc 文件中读取配置（优先级：项目级 > 用户级 .ohpmrc），必须保证路径存在且包含有效加密组件。
* 若报错提示加密组件错误，可重新执行ohpm config encrypt --crypto\_path <string> 命令。
* **示例**

  1. 执行 encrypt 命令。

     ```
     1. ohpm config encrypt
     ```
  2. 成功执行后，对用户输入内容进行加密，其中用户输入内容不可见。

     ```
     1. Please enter the password to be encrypted:
     2. ohpm INFO: encrypted result:
     3. security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
     ```

**密文使用：**

生成的加密结果可以配置到项目级或用户级 .ohpmrc 文件中，用于[敏感配置项](ide-ohpmrc.md#section18322038185010)。

## Options

### json

* 默认值：false
* 类型： Boolean
* 别名：j

可以在 config list 命令后面配置 -j或者--json 参数，以 json 格式输出所有配置项及默认值。

```
1. // 示例
2. // 1.执行list命令并以json形式输出
3. ohpm config list -j 或 ohpm config list --json
4. // 2.命令执行结果
5. {
6. "registry": "http://localhost:8088/repos/ohpm",
7. "strict_ssl": false,
8. "log_level": "info",
9. ......
10. }
```

### crypto\_path

* 默认值：无
* 类型： string

指定加密组件路径用于数据加密。针对指定路径的不同情况，说明如下：

1. 若指定路径不存在，自动创建目录并生成新加密组件；
2. 若路径为空目录，将自动在目录中生成新加密组件；
3. 若路径已存在有效加密组件，则使用现有组件加密。

```
1. // 示例1
2. // 1.执行 encrypt --crypto_path <string> 命令，指定的路径为空目录
3. ohpm config encrypt --crypto_path D:\path\to\empty_dir
4. // 2.成功执行后，在指定路径生成新的加密组件，并对用户输入内容进行加密，其中用户输入内容不可见
5. ohpm INFO: Attempted to create an crypto component at the "D:\path\to\empty_dir" path...
6. ohpm INFO: The crypto component has been created successfully.
7. Please enter the password to be encrypted:
8. ohpm INFO: encrypted result:
9. security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx

11. // 示例2
12. // 1.执行 encrypt --crypto_path <string> 命令，指定的路径为有效的加密组件
13. ohpm config encrypt --crypto_path D:\path\to\crypto_dir
14. // 2.成功执行后，对用户输入内容进行加密，其中用户输入内容不可见
15. Please enter the password to be encrypted:
16. ohpm INFO: encrypted result:
17. security:01:61AE9D3219664B7B785XXXXX:201f713d625daddafcb12198ea9d5121xxxxxx
```

### log\_level

* 默认值：无
* 类型： string

从ohpm 6.0.2.636版本开始，可以在命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。
