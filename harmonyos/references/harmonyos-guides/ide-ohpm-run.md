---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-run
title: ohpm run
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm run
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:54+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:4bb0c8fb28b7f1567fbaaf1b1619cd8a799ab0ee5012d101c5ecd744f7384456
---

执行用户自定义脚本。

## 命令格式

```
1. ohpm run [options] <script_name> [-- <args...>]
```

## 功能描述

* 指定运行定义在模块的 oh-package.json5 文件中 scripts 对象内的脚本。

  scripts对象内部支持"key":"value"方式配置多个待执行脚本。如以下示例所示，scriptName1、scriptName2、scriptName3为脚本别名（scriptName）；“echo hello”等为脚本内容（scriptContent），后续内容均参考此说明。

  oh-package.json5中scripts配置示例：

  ```
  1. {
  2. "scripts": {
  3. "scriptName1": "echo hello",
  4. "scriptName2": "ohpm run scriptName1",
  5. // 标识符"--"后可以通过'-p'或'--p'形式指定参数key, 可以通过' '或'='连接参数值
  6. "scriptName3": "node test.js -- -paramKey1 paramValue1 -paramKey2=paramValue2 --paramKey3 paramValue3"
  7. }
  8. }
  ```
* 脚本内容中可以用ohpm run引用同一个 oh-package.json5 文件中其它脚本别名，如scriptName2；ohpm run 引用关系是一个有向无环图，不支持递归或循环引用。
* 在解析脚本内容出错时，ohpm run命令将直接提示相应错误。比如，脚本内容中引用了一个在同一oh-package.json5文件中不存在的脚本别名；或在执行ohpm run时，发现脚本别名引用关系存在环的情况。

### 传递参数

* ohpm run命令可以通过标识符“--”覆盖被引用脚本的参数或为被引用脚本传递额外的参数，如：

  ```
  1. ohpm run scriptName3 -- -paramKey1 newValue -paramKey4 paramValue4
  ```

  该示例表明，脚本scriptName3的参数paramKey1会被替换为newValue, 并新增一个参数paramKey4。
* 如果脚本内容为ohpm run scriptName且使用了标识符“--”，则该scriptName对应的脚本内容不能再包含ohpm run相关的描述，避免嵌套引用。

### 支持多命令

支持 && 和 || 两种命令连接符 （&& 和 || 没有优先级区分，命令从左到右执行，不支持用括号来改变各个子命令的优先级），详细请参见下方[示例](ide-ohpm-run.md#section157898418348)。

### 约束

| 约束项 | 说明 |
| --- | --- |
| scriptKey 命名约束 | 合法的 scriptKey 的名字可以包含字母（包含大小写），数字，ASCII 冒号 :，ASCII下划线 \_ ，ASCII链接符 -，首字母必须是小写字母 |
| scriptContent 约束 | 合法的scriptContent不能引用除ohpm run以外的其它ohpm命令 |
| scriptContent 中使用 ohpm run 的约束 | 1、ohpm run 依赖的其它script别名必须在同一 oh-package.json5 中存在  2、ohpm run 引用关系是一个有向无环图，不支持递归或循环引用 |

## Options

### prefix

可以通过 --prefix 指定包的根目录，该目录下必须存在 oh-package.json5 文件。不支持通过这种方式调用依赖包中的脚本别名。

```
1. ohpm run --prefix <path> <脚本别名>
```

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该配置仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

下列所有示例的scripts配置均来自如下oh-package.json5：

```
1. {
2. "name": "example",
3. "version": "1.0.0",
4. "description": "this is an example for ohpm run.",
5. "main": "./src/index.ets",
6. "author": "oh",
7. "license": "ISC",
8. "scripts": {
9. "testLogic": "ohpm run testFail || ohpm run testSuc && ohpm run testSuc",
10. "testFail": "test1",
11. "testSuc": "echo hello"
12. }
13. ...
14. }
```

### 参数传递的使用示例

```
1. ohpm run script_name -- -arg1=1 --arg2=2 -arg3 3 --arg4 4
```

运行 script\_name 的脚本，并指定脚本中参数arg1，arg2，arg3，arg4，取值分别为1，2，3，4，以上四种参数传递的方法均可生效。

### 成功示例

执行脚本testSuc，如下所示：

```
1. ohpm run testSuc
```

执行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Oanp0VfySRKjtOUbJStHLA/zh-cn_image_0000002530913100.png?HW-CC-KV=V1&HW-CC-Date=20260429T054753Z&HW-CC-Expire=86400&HW-CC-Sign=59C16C7D997CCE4C9BAA1D8ED3B46D98D0EE1B09BAE785823D14A0CC03801403 "点击放大")

### 失败示例

执行脚本testFail，如下所示：

```
1. ohpm run testFail
```

执行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/59HOtoD3TlGDZjrGuimYkA/zh-cn_image_0000002530753106.png?HW-CC-KV=V1&HW-CC-Date=20260429T054753Z&HW-CC-Expire=86400&HW-CC-Sign=320C952192512A1FF0E75D2B1CB0DC489A6DC9E168E4FB7099E0A70197F8A651 "点击放大")

### 逻辑符(&&、||)使用示例

执行脚本testLogic，如下所示：

```
1. ohpm run testLogic
```

执行结果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/E9is5ljCSb-GNqK5WLGtXw/zh-cn_image_0000002561833025.png?HW-CC-KV=V1&HW-CC-Date=20260429T054753Z&HW-CC-Expire=86400&HW-CC-Sign=1FB022B568DDAE23CE55FDC1630A65C4B917565AEC2337AF880DCADD1DB02803 "点击放大")
