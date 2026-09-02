---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-options
title: 命令
breadcrumb: 指南 > AI Coding > DevEco CLI > 命令
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:70d7963326ce953339e94875512775b8b3cc318572a30467bce8c3f7d31d99f3
---

## help

查看版本、帮助信息以及所有子命令。

**命令格式：**

```shell
devecocli help
```

## init

将deveco-cli Skill或者MCP服务配置到智能体中。

**命令格式：**

```shell
devecocli init --agent <agents> --project <path> --path <path> --skill --mcp --force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --agent | 可选，智能体名称，多个智能体名称以英文逗号分隔。  缺省时配置到所有已检测到的智能体中。 |
| --project | 可选，指定工程路径，将deveco-cli Skill或MCP服务安装到该工程项目中。  默认安装在个人用户目录下。 |
| --path | 可选，指定deveco-cli Skill的配置路径。  不可与--project 、--agent 、--mcp同时使用。 |
| --skill | 可选，安装deveco-cli Skill。  不可与--mcp同时使用。  --mcp和--skill都缺省时，执行--skill。 |
| --mcp | 可选，配置MCP服务，与--project一起使用表示配置工程级MCP服务，独立使用表示配置用户级MCP服务。  不可与--skill同时使用。 |
| -f，--force | 可选，当目标位置已存在deveco-cli Skill或MCP服务时，覆盖重装。 |

**示例：**

```shell
# 配置Skill
devecocli init -f  # 安装或更新deveco-cli Skill
devecocli init --skill
devecocli init --agent agentname  # agentname需替换为实际的智能体名称
devecocli init --path D:\work\ARKTS\NewsData -f
# 配置MCP服务
devecocli init --mcp
devecocli init --mcp --agent agentname  # agentname需替换为实际的智能体名称
devecocli init --mcp --project D:\work\ARKTS\NewsData -f
```

## auth login

部分功能需要授权后才可正常使用，按照指引登录华为账号。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli auth login
```

## auth status

查询当前登录的用户。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli auth status
```

## auth team list

查询当前登录用户所在的团队信息，包括团队名称和团队ID。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli auth team list --json
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --json | 可选，输出格式。 |

**示例：**

```shell
devecocli auth team list
devecocli auth team list --json
```

## auth logout

退出登录。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli auth logout
```

## docs search

按关键词搜索[版本说明](../harmonyos-releases/overview-allversion.md)、[指南](application-dev-guide.md)、[API参考](../harmonyos-references/development-intro-api.md)、[最佳实践](../best-practices/bpta-best-practices-overview.md)、[FAQ](../harmonyos-faqs/faq-phone.md)、[变更预告](../harmonyos-roadmap/all-changelogs-610.md)中的内容。

**命令格式：**

```shell
devecocli docs search <keywords...> --catalog <name> --format <fmt> --limit <n>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <keywords...> | 必选，搜索关键词，多个关键词用空格隔开。 |
| --catalog | 可选，文档类别，取值包含harmonyos-releases（版本说明）、harmonyos-guides（指南）、harmonyos-references（API参考）、best-practices（最佳实践）、harmonyos-faqs（FAQ）、harmonyos-roadmap（变更预告）、all（所有分类）。默认为all。 |
| --format | 可选，输出格式，取值包括default、json。默认为default。  输出结果包含文档ID（用于指明文档路径）、标题、文档的概括内容。 |
| --limit | 可选，设置搜索结果返回条数，默认为20。 |

**示例：**

```shell
devecocli docs search 沉浸光感
devecocli docs search '@State' '@Prop' --catalog best-practices --limit 10
devecocli docs search Row Column --format json
```

## docs read

按文档ID查询文档的完整内容。

**命令格式：**

```shell
devecocli docs read <documentId>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <documentId> | 必选，文档ID，需通过[docs search](ide-deveco-cli-options.md#section18607104514449)命令获取。 |

**示例：**

```shell
devecocli docs read 开发指南/应用框架/UI_Design_Kit_UI设计套件/沉浸光感/ui-design-hds-component-material
```

## docs catalog

查询文档类别和类别名称。

**命令格式：**

```shell
devecocli docs catalog --format <fmt>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --format | 可选，输出格式，取值包括default、json。默认为default。 |

**示例：**

```shell
devecocli docs catalog
devecocli docs catalog --format json
```

## create

创建HarmonyOS应用工程，仅支持创建工程模板中的[Empty Ability模板](ide-template.md)。

**命令格式：**

```shell
devecocli create --app-name <name> --project-path <path> --bundle-name <bundle> --api-level <level>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --app-name | 必选，应用名称。 |
| --project-path | 可选，工程路径，默认为：./<appName>。 |
| --bundle-name | 可选，包名，默认为：com.example.<appname>，appname自动转为小写。更多请参考[app.json5配置文件标签](app-configuration-file.md#配置文件标签)。 |
| --api-level | 可选，API级别，最小值为17，最大值从安装的DevEco Studio的HarmonyOS SDK中自动获取。 |

**示例：**

```shell
devecocli create --project-path ./MyApp --app-name MyApp
devecocli create --project-path ./MyApp --app-name MyApp --bundle-name com.acme.myapp --api-level 23
devecocli create --app-name MyApp
```

## build

编译并打包HarmonyOS工程或工程中的模块。

**命令格式：**

```shell
devecocli build --product <product> --modules <modules> --build-mode <mode>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --product | 可选，产品名称，默认为default。更多可参考[products](ide-hvigor-build-profile-app.md#section45865492619)字段。 |
| --modules | 可选，模块名称，多个模块用空格隔开。  如需指定模块的target信息，使用module@target形式。  当工程中只有一个模块时，可缺省；当工程中存在多个模块，且仅存在一个entry类型模块时，可缺省。 |
| --build-mode | 可选，构建模式，默认为debug。更多可参考[buildModeSet](ide-hvigor-build-profile-app.md#section137297344398)字段。 |

**示例：**

```shell
devecocli build --build-mode release
devecocli build --modules entry library
devecocli build --modules library@phone
devecocli build --product oversea --modules entry --build-mode release
```

**说明** 

* 选定模块的依赖会被自动解析和构建。
* 执行devecocli build --product <name>命令后，产物为.app。
* 执行devecocli build --product <name> --modules <m1>命令后，产物为.hap/.hsp/.har。

## build clean

清理HarmonyOS项目的构建产物。

**命令格式：**

```shell
devecocli build clean
```

## signature generate

配置调试签名。执行命令可自动生成签名所需的材料，并将签名信息配置到工程级的build-profile.json5中。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli signature generate --product <product> --team-id <team-id> --force --help
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --product | 可选，产品名称，默认为default。 |
| --team-id | 可选，团队ID（Team ID），默认为主账号用户ID（userID）。 |
| --force | 可选，强制覆盖本地的签名材料。 |
| --help,--h | 可选，查看帮助信息。 |

**示例：**

```shell
# 自动生成签名并写入工程配置
devecocli signature generate
# 指定product
devecocli signature generate --product default1  #default1为指定的product名称
# 指定team-id
devecocli signature generate --team-id 1222    #1222为指定的team-id
# 强制覆盖已存在的证书文件
devecocli signature generate --force
# 查询帮助信息
devecocli signature generate --help
```

## run

构建应用后，将应用安装到真机设备或模拟器上，并启动执行。

**命令格式：**

```shell
devecocli run --module <module> --device <device> --product <product> --build-mode <mode> --ability <ability> --uninstall --skip-build --apply <fileName> --hotreload --hotreload-apply
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --module | 可选，模块名称，多个模块用空格隔开。  如需指定[模块的target信息](ide-hvigor-build-profile-app.md#section1961794812219)，使用module@target形式。  当工程中只有一个可运行模块（entry / feature / shared）时，可缺省。 |
| --device | 设备名称或设备序列号，单设备时可选，多设备时必选。 |
| --product | 可选，产品名称，默认为default。更多请参考[products](ide-hvigor-build-profile-app.md#section45865492619)。 |
| --build-mode | 可选，构建模式名称，默认为debug。更多请可参考[buildModeSet](ide-hvigor-build-profile-app.md#section137297344398)。 |
| --ability | 可选，待启动的Ability，默认是模块module.json5中的mainElement。 |
| --uninstall | 可选，安装前先卸载已有应用。 |
| --skip-build | 可选，跳过构建操作，直接安装应用。  说明：  使用该参数时，需确保对应模块已有构建产物。 |
| --apply | 可选，将全量构建部署生成缓存后的修改生成增量修改文件（.hqf文件），重启应用后增量修改文件会生效。  fileName须在工程.hvigor目录下，中记录被修改源文件相对工程根目录的路径。通过读取该文件，工具可以定位发生变化的文件，并执行增量编译，提高构建效率。  说明：  * 执行该命令前，需先执行devecocli run命令完成全量构建部署，生成缓存。 * 若devecocli run --apply执行失败，工具会自动执行devecocli run命令进行全量构建。 * 需使用DevEco Studio 6.1.1以上版本。 |
| --hotreload | 可选，使用热重载功能。  使用热重载功能时，该命令进程需持续存活，以使热重载构建可以快速响应。当不需要热重载功能时，通过执行“devecocli run --hotreload stop”命令终止该进程，释放系统资源。 |
| --hotreload-apply | 可选，将热重载基础缓存后的修改生成增量修改文件（.hqf文件），并将.hqf文件应用到运行中的应用，使修改直接生效。  说明：  * 执行该命令前，需先执行devecocli run --hotreload命令，生成热重载基础缓存。 * 增量修改时，仅支持修改运行模块中的ArkTS文件。 |

**示例：**

```shell
devecocli run
devecocli run --module entry --device 127.0.0.1:5555
devecocli run --module library@phone --device 127.0.0.1:5555
devecocli run --product oversea --module entry --ability EntryAbility
devecocli run --build-mode release
devecocli run --uninstall
devecocli run --apply changes.txt
devecocli run --hotreload-apply change.txt
```

## log

查看hilog普通日志或崩溃日志。

**命令格式：**

```shell
devecocli log --device <device> --crash --level <level> --bundle-name <bundle-name> --keyword <keyword> --tail <num> --from <start> --to <end> --follow
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --device | 设备名称或设备序列号，单设备时可选，多设备时必选。 |
| --crash | 可选，查看崩溃日志。 |
| --level | 可选，日志级别，取值包括D（Debug）、 I（Info）、 W（Warn）、E（Error）、F（Fatal）。 |
| --bundle-name | 可选，根据包名查看日志。 |
| --keyword | 可选，根据关键词查看日志，关键词区分大小写。 |
| --tail | 可选，显示最新的N行日志，取值为正整数。 |
| --from | 可选，起始时间偏移量，以当前时间为基准时间点，通过减去预设的时间偏移量，可计算得出起始时间。单位为m/s，m和s为小写，默认为s。  说明：  如当前时间为05:00:00，start设置为30s，则起始时间为04:59:30。 |
| --to | 可选，结束时间偏移量，以当前时间为基准时间点，通过减去预设的时间偏移量，可计算得出结束时间。单位为m/s，m和s为小写，默认为s。  不可与--follow同时使用。  说明：  如当前时间为05:00:00，end设置为10s，则结束时间为04:59:50。 |
| --follow | 可选，实时输出日志。  不可与--to同时使用。 |

**示例：**

```shell
devecocli log --level E
devecocli log --crash --bundle-name com.example.app
devecocli log --device 127.0.0.1:5555 --level W --keyword Init
devecocli log --tail 100 --from 5m --to 2m
devecocli log --follow --bundle-name com.example.app
```

## check lint

按照[Code Linter代码规则](ide-codelinter-rule.md)，对ArkTS代码工程进行正确性、兼容性等检查，并自动修复问题。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli check lint [path] --fix --incremental --config-path <path> --product <product> --format <format> --output-path <path> --limit <number>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [path] | 可选，待检查的文件或目录的路径，文件或目录所在的工程中必须包含build-profile.json5文件。默认为工程根目录。  不可与--incremental同时使用。 |
| --fix | 可选，填写时，进行代码检查及自动修复代码问题；不填写时，只进行代码检查。 |
| --incremental | 可选，对Git工程中的增量文件（包含新增/修改/重命名的文件）进行检查。  不可与[path]同时使用。 |
| --config-path | 可选，指定Code Linter代码检查规则配置文件的位置。 |
| --product | 可选，产品名称，默认为default。更多可参考[products](ide-hvigor-build-profile-app.md#section45865492619)字段。 |
| --format | 可选，检查结果的输出格式，取值包括default、json。默认为default。 |
| --output-path | 可选，检查结果保存位置，支持相对路径和绝对路径。默认在控制台输出。 |
| --limit | 可选，控制台显示的最大记录条数。默认显示所有内容。 |

**示例：**

```shell
devecocli check lint
devecocli check lint ./entry/src/main/ets
devecocli check lint --fix
devecocli check lint --incremental
devecocli check lint --incremental --fix
devecocli check lint --format json
devecocli check lint --product default --config-path ./lint.json
devecocli check lint ./entry --fix --format json
devecocli check lint --output-path ./entry/output
devecocli check lint --limit 20
```

## check compat

检查当前工程/模块/文件对目标SDK版本的兼容性。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli check compat [files] --source-version <version> --target-version <version> --modules <modules...> --format <format> --output-path <path> --limit <number>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [files...] | 可选，待检查的文件路径，支持相对路径或绝对路径，当前仅支持.ets、.c、.cpp后缀文件。 |
| --source-version | 必选，工程使用的精确的SDK版本号，格式为HarmonyOS\_SDK版本号\_Beta/Release，如HarmonyOS\_26.0.0(26)\_Beta2，可在File > Settings > HarmonyOS SDK查询。 |
| --target-version | 必选，需要检查兼容性的目标SDK版本，可以先通过check compat versions命令查询用于兼容性检查的SDK版本，版本大于--source-version。 |
| --modules | 可选，模块名称，指定要检查的模块，多个模块用空格隔开。默认检查工程中的所有模块。 |
| --format | 可选，输出格式，取值包括json、default。默认为default。  不填写时，若不指定--output-path，在控制台以文本形式输出；若指定--output-path，以csv形式输出。 |
| --output-path | 可选，兼容性报告的输出路径。默认值在控制台输出。 |
| --limit | 可选，控制台显示的最大记录条数。默认为100。 |

**示例：**

```shell
devecocli check compat ./entry/src/main/ets/pages/Index.ets --source-version "HarmonyOS_6.1.0(23)_Beta2" --target-version "HarmonyOS_26.0.0(26)_Beta2"
devecocli check compat ./entry/src/main/ets/pages/Index.ets ./entry/src/main/ets/entrybackupability/EntryBackupAbility.ets --source-version "HarmonyOS_6.1.0(23)_Beta2" --target-version "HarmonyOS_26.0.0(26)_Beta2"
devecocli check compat --source-version "HarmonyOS_6.1.0(23)_Beta2" --target-version "HarmonyOS_26.0.0(26)_Beta2"
devecocli check compat --source-version "HarmonyOS_6.1.0(23)_Beta2" --target-version "HarmonyOS_26.0.0(26)_Beta2" --modules entry library
devecocli check compat --source-version "HarmonyOS_6.1.0(23)_Beta2" --target-version "HarmonyOS_26.0.0(26)_Beta2" --format json
devecocli check compat --source-version "HarmonyOS_6.1.0(23)_Beta2" --target-version "HarmonyOS_26.0.0(26)_Beta2" --output-path ./entry/output
devecocli check compat --source-version "HarmonyOS_6.1.0(23)_Beta2" --target-version "HarmonyOS_26.0.0(26)_Beta2" --limit 20
```

## check compat versions

查询可用于兼容性检查的SDK版本。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli check compat versions --format <format>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --format | 可选，输出格式，取值包括default、json。默认为default。 |

**示例：**

```shell
devecocli check compat versions
devecocli check compat versions --format json
```

## emulator list

查看模拟器实例。

**命令格式：**

```shell
devecocli emulator list
```

**返回信息：**

| 返回信息 | 说明 |
| --- | --- |
| Name | 模拟器名称。 |
| Status | 模拟器运行状态。 |
| Serial | 模拟器序列号。 |
| Device Type | 模拟器产品类型。 |
| OS Version | 模拟器镜像版本。 |

## emulator start

启动模拟器。首次使用时，需要签署HarmonyOS软件许可与服务协议，具体请参考[emulator license accept](ide-deveco-cli-options.md#section469814010492)。

**命令格式：**

```shell
devecocli emulator start [names...]
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [names...] | 必选，模拟器实例名称或序列号，多个名称用空格隔开。  若名称中带有空格，则名称需要添加英文引号。 |

**示例：**

```shell
devecocli emulator start Phone
devecocli emulator start Phone1 Phone2
```

**说明** 

emulator start命令仅支持启动release版本的模拟器。

## emulator stop

关闭模拟器。

**命令格式：**

```shell
devecocli emulator stop [names...]
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [names...] | 必选，模拟器实例名称或序列号，多个名称或序列号用空格隔开。  若名称中带有空格，则名称需要添加英文引号。 |

**示例：**

```shell
devecocli emulator stop Phone
devecocli emulator stop 127.0.0.1:5555
```

## emulator create

创建模拟器。

**命令格式：**

```shell
devecocli emulator create <name> --device-type <type> --os-version <version> --force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <name> | 必选，模拟器名称。 |
| --device-type | 必选，模拟器产品类型，支持的产品类型请参考[设备支持类型](ide-emulator-devicetype.md)，全小写。 |
| --os-version | 必选，模拟器镜像版本。 |
| --force | 可选，覆盖已有同名的模拟器。 |

**示例：**

```shell
devecocli emulator create MyPhone --device-type phone --os-version "HarmonyOS 6.0.1(21)"
devecocli emulator create MyPhone --device-type phone --os-version "HarmonyOS 6.1.1(24)"
```

## emulator delete

删除模拟器。

**命令格式：**

```shell
devecocli emulator delete <name>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <name> | 必选，模拟器实例名称或序列号。 |

**示例：**

```shell
devecocli emulator delete MyPhone
```

## emulator image list

查询模拟器镜像列表。

**命令格式：**

```shell
devecocli emulator image list --device-type <type> --all --format <format>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --device-type | 可选，模拟器产品类型，支持的产品类型请参考[设备支持类型](ide-emulator-devicetype.md)，全小写。 |
| --all | 可选，查询已下载和未下载的所有镜像。 |
| --format | 可选，控制输出格式，取值包括table、json，默认为table。 |

**返回信息：**

| 返回信息 | 说明 |
| --- | --- |
| OS Version | 镜像版本号，可用于下载镜像时指定--os-version参数。 |
| Device Type | 模拟器产品类型，可用于下载镜像时指定--device-type参数。 |
| Software Version | 镜像详细版本号，可用于下载镜像时指定--os-version参数。 |
| Release Type | 镜像发布类型。 |
| Upgradable | 对比本地镜像，是否有可更新的镜像版本，true/false。 |
| Downloaded | 本地是否已下载过镜像，true/false。 |

**示例：**

```shell
devecocli emulator image list
devecocli emulator image list --all
devecocli emulator image list --device-type phone
devecocli emulator image list --format json
```

## emulator image download

下载模拟器镜像。首次使用时，需要签署HarmonyOS SDK许可协议，具体请参考[emulator license accept](ide-deveco-cli-options.md#section469814010492)。

**命令格式：**

```shell
devecocli emulator image download --device-type <type> --os-version <version> --force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --device-type | 必选，模拟器产品类型，支持的产品类型请参考[设备支持类型](ide-emulator-devicetype.md)，全小写。 |
| --os-version | 必选，模拟器镜像版本。 |
| --force | 可选，覆盖已有的模拟器镜像。 |

**示例：**

```shell
devecocli emulator image download --device-type phone --os-version "HarmonyOS 6.0.1(21)" --force
devecocli emulator image download --device-type phone --os-version "HarmonyOS 6.1.1(24)" --force
```

**说明** 

emulator image download命令仅支持下载release版本的模拟器镜像。

## emulator image remove

删除模拟器镜像。

**命令格式：**

```shell
devecocli emulator image remove --device-type <type> --os-version <version>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --device-type | 必选，模拟器产品类型，与[下载镜像](ide-deveco-cli-options.md#section7190115134818)的--device-type参数一致。 |
| --os-version | 必选，模拟器镜像版本，与[下载镜像](ide-deveco-cli-options.md#section7190115134818)的--os-version参数一致。 |

**示例：**

```shell
devecocli emulator image remove --device-type phone --os-version "HarmonyOS 6.0.1(21)"
```

## emulator license view

查看HarmonyOS软件许可与服务协议和HarmonyOS SDK许可协议文本（只读）。

**命令格式：**

```shell
devecocli emulator license view
```

## emulator license accept

查看并接受协议。使用模拟器需要同意HarmonyOS软件许可与服务协议，下载镜像需要同意HarmonyOS SDK许可协议。

**命令格式：**

```shell
devecocli emulator license accept
```

## emulator shake

触发一次模拟器的摇一摇功能。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator shake --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --target | 必选，模拟器名称或序列号。 |

**示例：**

```shell
devecocli emulator shake --target myPhone
```

## emulator power

设置模拟器亮/熄屏。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator power --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --target | 必选，模拟器名称或序列号。 |

**示例：**

```shell
devecocli emulator power --target myPhone
```

## emulator rotate

旋转模拟器。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator rotate <direction> --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <direction> | 必选，旋转方向，取值包括left、right。   * left：向左旋转90°。 * right：向右旋转90°。 |
| --target | 必选，模拟器名称或序列号。 |

**示例：**

```shell
devecocli emulator rotate left --target myPhone
```

## emulator volume

调整模拟器的音量。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator volume <direction> --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <direction> | 必选，调整音量，取值包括up、down。   * up：音量加1。 * down：音量减1。 |
| --target | 必选，模拟器名称或序列号。 |

**示例：**

```shell
devecocli emulator volume up --target myPhone
```

## emulator fold

设置模拟器的折叠开合状态。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator fold <state> --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <state> | 必选，折叠开合状态。支持以下状态：   * 双折叠设备、Pura X Max：open | half-open | close * 折叠2in1设备：open | vertical-open | half-open | close * 三折叠设备：single | double | triple | left-folded-right-half-folded | left-half-folded-right-expanded | left-expanded-right-folded | left-half-folded-right-folded | left-expanded-right-half-folded | left-half-folded-right-half-folded |
| --target | 必选，模拟器名称或序列号。 |

**示例：**

```shell
# 双折叠
devecocli emulator fold open --target myPhone
devecocli emulator fold half-open --target myPhone
devecocli emulator fold close --target myPhone

# 折叠2in1
devecocli emulator fold open --target myPhone
devecocli emulator fold vertical-open --target myPhone
devecocli emulator fold half-open --target myPhone
devecocli emulator fold close --target myPhone

# 三折叠
devecocli emulator fold single --target myPhone
devecocli emulator fold double --target myPhone
devecocli emulator fold triple --target myPhone
devecocli emulator fold left-folded-right-half-folded --target myPhone
devecocli emulator fold left-half-folded-right-expanded --target myPhone
devecocli emulator fold left-expanded-right-folded --target myPhone
devecocli emulator fold left-half-folded-right-folded --target myPhone
devecocli emulator fold left-expanded-right-half-folded --target myPhone
devecocli emulator fold left-half-folded-right-half-folded --target myPhone
```

## emulator battery

设置模拟器电池的电量和充电状态。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator battery --level <1-100> --status <status> --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --level | 必选，模拟器电池电量，充电状态下取值范围为[0,100]，未充电状态下取值范围为[1,100]。  不可与--status同时使用。 |
| --status | 必选，模拟器电池充电状态，取值为charging、discharging。   * charging：充电中。 * discharging：未充电。   不可与--level同时使用。 |
| --target | 必选，模拟器名称或序列号。 |

**示例：**

```shell
devecocli emulator battery --target myPhone --level 90
devecocli emulator battery --target myPhone --status discharging
devecocli emulator battery --target myPhone --status charging
```

## emulator geolocation

设置模拟器的地理坐标和方向信息。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator geolocation --longitude <value> --latitude <value> --altitude <value> --direction <value> --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --longitude | 可选，经度，取值范围为 [-180.0, 180.0]，支持小数点后八位。 |
| --latitude | 可选，纬度，取值范围为 [-90.0, 90.0]，支持小数点后八位。 |
| --altitude | 可选，海拔高度，单位为m，取值范围为[-10000.0, 10000.0]，支持小数点后两位。 |
| --direction | 可选，方向角，取值范围为[0, 359.99]，支持小数点后两位。 |
| --target | 必选，模拟器名称或序列号。 |

**说明** 

当前仅支持设置经度、纬度、海拔高度、方向角中的一种。

**示例：**

```shell
devecocli emulator geolocation --target myPhone --longitude 116.400244
devecocli emulator geolocation --target myPhone --latitude 39.915599
devecocli emulator geolocation --target myPhone --altitude 45.49
devecocli emulator geolocation --target myPhone --direction 0
```

## emulator scene

启动运动模拟场景。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator scene <type> --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <type> | 必选，模拟运动场景类型，取值包括outdoorRunning、outdoorCycling、drivingNavigation。   * outdoorRunning：模拟跑步。 * outdoorCycling：模拟骑行。 * drivingNavigation：模拟驾驶。 |
| --target | 必选，模拟器名称或序列号。 |

**示例：**

```shell
devecocli emulator scene outdoorRunning --target myPhone 
devecocli emulator scene outdoorCycling --target myPhone 
devecocli emulator scene drivingNavigation --target myPhone
```

## emulator sensor

为模拟器设置传感器。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli emulator sensor --light-intensity <value> --humidity <value> --temperature <value> --steps <value> --heartrate <value> --target <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --light-intensity | 可选，光照强度传感器，取值范围为[0, 100000.0]，支持小数点后1位。 |
| --humidity | 可选，湿度传感器，取值范围为[0, 100]，支持小数点后1位。 |
| --temperature | 可选，温度传感器，取值范围为[-273.1, 100]，支持小数点后1位。 |
| --steps | 可选，步数传感器，取值范围为[0, 10000]，需要为整数。 |
| --heartrate | 可选，心率传感器，取值范围为[0, 255]，需要为整数。 |
| --target | 必选，模拟器名称或序列号。 |

**说明** 

当前仅支持设置一种传感器。

**示例：**

```shell
devecocli emulator sensor --target myPhone --light-intensity 500
devecocli emulator sensor --target myPhone --humidity 50
devecocli emulator sensor --target myPhone --temperature 25
devecocli emulator sensor --target myPhone --steps 1000
devecocli emulator sensor --target myPhone --heartrate 80
```

## device list

查询所有已连接的设备，包括真机设备和运行中的模拟器。

**命令格式：**

```shell
devecocli device list
```

**返回信息：**

| 返回信息 | 说明 |
| --- | --- |
| Name | 真机或模拟器名称。 |
| Serial | 真机或模拟器序列号。 |
| Kind | 类型，真机或模拟器。 |
| Device Type | 设备类型。 |

## device view

查询已连接设备的详细信息，包括设备序列号、设备名称、设备类型、OS版本等。

**命令格式：**

```shell
devecocli device view --target <serialOrName>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -t, --target | 可选，目标设备名称或序列号。多设备缺省时，会列出所有已连接设备序列号和名称。 |

**返回信息：**

| 返回信息 | 说明 |
| --- | --- |
| Serial | 真机或模拟器序列号。 |
| Device Name | 真机或模拟器名称。 |
| Device Type | 设备类型。 |
| Os Version | 镜像版本号，可用于下载镜像时指定--os-version参数。 |

**示例：**

```shell
devecocli device view
devecocli device view --target 127.0.0.1:5555
devecocli device view -t "My Device Name"
```

## skills list

查询可用的Skill。

**命令格式：**

```shell
devecocli skills list --long
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -l, --long | 可选，Skill详情，包括描述和已安装的智能体列表。缺省时，仅展示Skill名称。 |

**示例：**

```shell
devecocli skills list
devecocli skills list --long
devecocli skills list -l
```

## skills find

按关键词搜索Skill。

**命令格式：**

```shell
devecocli skills find <keyword>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <keyword> | 必选，搜索关键词。 |

**示例：**

```shell
devecocli skills find deveco
```

## skills add

将Skill添加到智能体中。

**命令格式：**

```shell
devecocli skills add --all --agent <agents> --skill <skill-name> --project <path> --path <path> --force
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --all | 可选，添加所有可用的Skill，与--skill二选一。 |
| --agent | 可选，智能体名称，多个智能体时以英文逗号分隔。缺省时，添加到已检测到的智能体中。 |
| --skill | 可选，待添加的Skill名称，与--all二选一。 |
| --project | 可选，指定工程路径，将Skill添加到该工程项目中。 |
| --path | 可选，指定路径，将Skill添加到该路径，不可与--project或--agent同时使用。 |
| -f, --force | 可选，当目标位置已有同名Skill时，覆盖重添加。 |

**示例：**

```shell
devecocli skills add --all 
devecocli skills add --skill skillname --agent agentname --force  # skillname需替换为实际的Skill名称
devecocli skills add --skill skillname --project ./my-app  # skillname需替换为实际的Skill名称
```

## skills remove

从智能体中删除已添加的Skill。

**命令格式：**

```shell
devecocli skills remove --skill <skill-name> --agent <agents> --project <path> --path <path>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --skill | 必选，待删除的Skill名称。 |
| --agent | 可选，智能体名称，多个智能体时以英文逗号分隔。缺省时，删除已检测到的智能体中的Skill。 |
| --project | 可选，指定项目路径，删除该项目中的Skill。 |
| --path | 可选，指定路径，删除该路径下的Skill，不可与--project或--agent同时使用。 |

**示例：**

```shell
devecocli skills remove --skill skillname   # skillname需替换为实际的Skill名称
devecocli skills remove --skill skillname --agent agentname  # skillname需替换为实际的Skill名称
```

## ui layout

以字符树的形式查看应用的界面布局，包括控件类型、控件ID、控件坐标边界（[left,top,right,bottom]） 、控件文本和交互标志（clickable、longClickable、scrollable、checkable）。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui layout --device <name|serial> --id <id> --window <windowId> --all-windows --depth <n> --format <format> --mode <mode>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --device | 真机或模拟器设备的名称/序列号，使用时只支持连接一个设备。  单设备时可选，多设备时必填。若名称中带有空格，则名称需要添加英文引号。 |
| --id | 可选，控件ID，填写时可输出匹配的控件节点（不含子节点）。 |
| --window | 可选，目标窗口ID，不可与--all-windows同时使用。 |
| --all-windows | 可选，包含系统窗口和应用窗口。默认只包含应用窗口。  不可与--window同时使用。 |
| --depth | 可选，字符树的深度，0表示不限制。默认为0。 |
| --format | 可选，输出格式，取值包含default、json，default也以json格式显示。默认为default。 |
| --mode | 可选，输出模式，取值包含full、simplified。默认为simplified。   * full：输出所有控件。 * simplified：无控件ID、无控件文本和无交互标志的控件不显示。 |

**示例：**

```shell
devecocli ui layout
devecocli ui layout --device Phone
devecocli ui layout --device Phone --format json
devecocli ui layout --mode full --depth 2
devecocli ui layout --id submit_button
devecocli ui layout --window 15 --format json
```

**说明** 

从API version 20开始支持该命令。

## ui window list

查看设备上的窗口列表。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui window list --device <name|serial> --format <format> --all
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --device | 真机或模拟器设备的名称/序列号，使用时只支持连接一个设备。  单设备时可选，多设备时必填。若名称中带有空格，则名称需要添加英文引号。 |
| --format | 可选，输出格式，取值包括default、json，默认为default。 |
| --all | 可选，包含系统窗口和应用窗口。默认只包含应用窗口。 |

**返回信息：**

| 返回信息 | 说明 |
| --- | --- |
| Id | 窗口ID。 |
| Name | 窗口名称。 |
| Pid | PID。 |
| DisplayId | 所属屏幕ID。 |
| Focused | 是否为聚焦窗口。   * true：是聚焦窗口。 * false：不是聚焦窗口。 |

**示例：**

```shell
devecocli ui window list
devecocli ui window list --device Phone
devecocli ui window list --format json
devecocli ui window list --all
```

## ui screenshot

对真机或模拟器进行全屏截图。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui screenshot --device <name|serial> --display <--displayId> --path <path>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --device | 真机或模拟器设备的名称/序列号，使用时只支持连接一个设备。  单设备时可选，多设备时必填。若名称中带有空格，则名称需要添加英文引号。 |
| --display | 可选，目标屏幕ID。 |
| --path | 必选，截图的输出路径，支持相对路径和绝对路径。路径可以是已存在的文件路径，也可以是完整的PNG文件路径。   * 传入已存在的文件夹时，会在目录下自动生成截图文件，命名格式为：screenshot-时间戳.png。 * 传入完整的PNG文件路径时，若路径下存在同名的.png和.jpeg文件时，会报错，截图不会覆盖现有文件，以及若传入.jpeg或.pngd等非PNG文件路径，也会报错。 |

**示例：**

```shell
# 传入已存在的文件夹
devecocli ui screenshot --path ./screenshots

# 传入完整的PNG文件路径
devecocli ui screenshot --device Phone --path ./screenshots/phone.png
devecocli ui screenshot --device Phone --display 0 --path ./screenshots/phone.png
```

## ui click

单击指定坐标或单击节点ID的中心位置。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui click [x] [y] --device <name|serial> --id <id> --window <windowId>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [x] [y] | 可选，目标坐标，取值为大于0的整数，单位：px。  不可与--id同时使用，且与--id至少使用一个。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  单设备时可选，多设备时必填。若名称中带有空格，则名称需要添加英文引号。 |
| --id | 可选，控件ID。  不可与[x] [y]同时使用，且与[x] [y]至少使用一个。 |
| --window | 可选，目标窗口ID，可通过devecocli ui window list获取，与--id配合使用。 |

**示例：**

```shell
devecocli ui click 100 200
devecocli ui click 100 200 --device Phone
devecocli ui click --id submit_button
devecocli ui click --id submit_button --window main_window
```

## ui doubleclick

双击指定坐标或双击节点ID的中心位置。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui doubleclick [x] [y] --device <name|serial> --id <id> --window <windowId>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [x] [y] | 可选，目标坐标，取值是大于0的整数，单位：px。  不可与--id同时使用，且与--id至少使用一个。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  单设备时可选，多设备时必填。若名称中带有空格，则名称需要添加英文引号。 |
| --id | 可选，控件ID。  不可与[x] [y]同时使用，且与[x] [y]至少使用一个。 |
| --window | 可选，目标窗口ID，可通过devecocli ui window list获取，与--id配合使用。 |

**示例：**

```shell
devecocli ui doubleclick 100 200
devecocli ui doubleclick 100 200 --device Phone
devecocli ui doubleclick --id photo_thumb
devecocli ui doubleclick --id photo_thumb --window main_window
```

## ui longclick

长按指定坐标或长按节点ID的中心位置。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui longclick [x] [y] --device <name|serial> --id <id> --window <windowId>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [x] [y] | 可选，目标坐标，取值是大于0的整数，单位：px。  不可与--id同时使用，且与--id至少使用一个。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  若名称中带有空格，则名称需要添加英文引号。 |
| --id | 可选，控件ID。  不可与[x] [y]同时使用，且与[x] [y]至少使用一个。 |
| --window | 可选，目标窗口ID，可通过devecocli ui window list获取，与--id配合使用。 |

**示例：**

```shell
devecocli ui longclick 100 200
devecocli ui longclick 100 200 --device Phone
devecocli ui longclick --id menu_item
devecocli ui longclick --id menu_item --window main_window
```

## ui swipe

从起点缓慢滑到终点。内容随手指移动，手指离开即停止，适用于在特定区域滑动的场景，如拖动Slider。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui swipe [x1] [y1] [x2] [y2] --device <name|serial> --speed <n>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [x1] [y1] | 必选，起点坐标，取值为大于0的整数，单位：px。 |
| [x2] [y2] | 必选，终点坐标，取值为大于0的整数，单位：px。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  若名称中带有空格，则名称需要添加英文引号。 |
| --speed | 可选，滑动速度，单位为px/s，取值范围为[200,40000]。默认值为600。 |

**示例：**

```shell
devecocli ui swipe 100 500 100 200
devecocli ui swipe 100 500 100 200 --device Phone
devecocli ui swipe 100 500 100 200 --speed 1000
```

## ui fling

从起点快速滑到终点。手指快速滑动后脱离屏幕，内容存在惯性滚动，适用于在特定区域快速滑动的场景。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui fling [x1] [y1] [x2] [y2] --device <name|serial> --speed <n>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [x1] [y1] | 必选，起点坐标，取值为大于0的整数，单位：px。 |
| [x2] [y2] | 必选，终点坐标，取值为大于0的整数，单位：px。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  若名称中带有空格，则名称需要添加英文引号。 |
| --speed | 可选，滑动速度，单位为px/s，取值范围为[200,40000]。默认值为600。 |

**示例：**

```shell
devecocli ui fling 100 800 100 200
devecocli ui fling 100 800 100 200 --device Phone
devecocli ui fling 100 800 100 200 --speed 1000
```

## ui dircfling

按照指定的方向快速滑动且有惯性。适用于快速按方向浏览的场景，如页面滚动、列表快速滑动。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui dircfling <direction> --device <name|serial>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| <direction> | 必选，方向，取值为up，down，left，right。   * up：向上。 * down：向下。 * left：向左。 * right：向右。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  若名称中带有空格，则名称需要添加英文引号。 |

**示例：**

```shell
devecocli ui dircfling up
devecocli ui dircfling down --device Phone
devecocli ui dircfling left
devecocli ui dircfling right
```

## ui drag

拖拽操作。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui drag [x1] [y1] [x2] [y2] --device <name|serial> --speed <n>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [x1] [y1] | 必选，起点坐标，取值为大于0的整数，单位：px。 |
| [x2] [y2] | 必选，终点坐标，取值为大于0的整数，单位：px。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  若名称中带有空格，则名称需要添加英文引号。 |
| --speed | 可选，滑动速度，单位为px/s，取值范围为[200,40000]。默认值为600。 |

**示例：**

```shell
devecocli ui drag 100 500 100 200
devecocli ui drag 100 500 100 200 --device Phone
devecocli ui drag 100 500 100 200 --speed 1500
```

## ui text

在当前焦点、指定坐标或指定节点位置输入文本。从1.3.0版本开始支持。

**命令格式：**

```shell
devecocli ui text [text] [x] [y] --device <name|serial> --id <id> --window <windowId>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| [text] | 必选，待输入的文本。 |
| [x] [y] | 可选，目标坐标，取值是大于0的整数，单位：px。  不可与--id同时使用。 |
| --device | 真机或模拟器设备的名称/序列号，只支持连接一个设备。  若名称中带有空格，则名称需要添加英文引号。 |
| --id | 可选，控件ID，自动解析为中心坐标。  不可与[x] [y]同时使用。 |
| --window | 可选，目标窗口ID，可通过devecocli ui window list获取，与--id配合使用。 |

**示例：**

```shell
devecocli ui text "Hello World"
devecocli ui text "Hello World" --device Phone
devecocli ui text "Hello World" 100 200
devecocli ui text "Hello World" --id search_box
devecocli ui text "Hello World" --id search_box --window main_window
```

## serve mcp

启动本地MCP服务。智能体配置MCP服务后，可通过MCP协议调用ArkTS/C++语法检查工具。不同智能体平台配置MCP服务的界面不一样，某智能平台的配置示例如下。

推荐通过[devecocli init --mcp](ide-deveco-cli-options.md#section272801794417)自动配置。

```json
{
  "mcp": {
    "deveco-mcp": {
      "type": "local",
      "command": [
        "devecocli",
        "serve",
        "mcp"
      ],
      "environment": {
        "PROJECT_PATH": "D:\\code\\sample_in_harmonyos",  // 工程路径
        "NODE_MAX_OLD_SPACE_SIZE": "8192",  // 可选，设置内部node进程最大的老生代内存大小，默认为8192
        "DEVECO_PATH": "D:\\Applications\\DevEco Studio"  // 可选，DevEco Studio的安装路径
      },
      "enabled": true
    }
  }
}
```

| 工具名 | 用途 | 支持语言 |
| --- | --- | --- |
| check | 静态语法分析，返回结构化诊断信息。 | ArkTS、C/C++ |
| hover | 获取指定位置的悬浮信息（类型、文档）。 | ArkTS、C/C++ |
| definition | 查找符号定义位置。 | ArkTS、C/C++ |
| declaration | 查找符号声明位置（ArkTS 中可能与定义不同）。 | ArkTS、C/C++ |
| references | 查找符号在全工程中的所有引用。 | ArkTS、C/C++ |
| implementation | 查找符号的实现（如接口实现）。 | ArkTS、C/C++ |
| workspaceSymbol | 按名称在全工程搜索符号。 | ArkTS、C/C++ |
| documentSymbol | 获取单文件的符号树（函数、类、变量及范围）。 | ArkTS、C/C++ |
| callHierarchy | 查询函数调用关系。 | ArkTS、C/C++仅支持调用方 |

**说明** 

* 环境要求：DevEco Studio 26.0.0 Release及以上版本，DevEco CLI 1.3.0及以上版本。
* 若出现"please retry in N seconds"提示信息，开发者需稍等后再使用。
* 支持的文件扩展名如下：
  + ArkTS：.ets
  + C/C++：.c、.cc、.cpp、.cxx、.c++、.h 、.hh、.hpp、.hxx、.h++、.ipp、.ixx、.inl、.inc、.tpp。

## serve lsp

启动本地LSP语言服务。智能体配置LSP服务后，可通过LSP协议实现代码检查、代码引用查找、代码跳转、代码补全等代码编辑相关的能力。从1.3.0版本开始支持。

具体配置如下，当前支持ArkTS和clangd：

```shell
{
  "lsp": {
    "ArkTS": {
      "command": [
        "devecocli",
        "serve",
        "lsp",
        "--arkts"
      ],
      "extensions": [  // 支持的文件格式
        ".ets"
      ]
    },
    "clangd": {
      "command": [
        "devecocli",
        "serve",
        "lsp",
        "--cpp"
      ],
      "extensions": [  // 支持的文件格式
        ".c",
        ".cpp",
        ".cc",
        ".cxx",
        ".h",
        ".hpp",
        ".hxx",
        ".hh"
      ]
    }
  }
}
```

**命令格式：**

```shell
devecocli serve lsp --arkts --cpp --project-path <path> --auto-detect
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| --arkts | 必选，启动ArkTS语言服务器，不可与--cpp同时使用。 |
| --cpp | 必选，启动C/C++语言服务器，不可与--arkts同时使用。 |
| --project-path | 可选，工程根目录。默认为当前目录。 |
| --auto-detect | 可选，在当前目录和子目录中查找工程根目录，最多向下查找3层子目录。  不可与--project-path同时使用。 |

**示例：**

```shell
devecocli serve lsp --arkts
devecocli serve lsp --cpp
devecocli serve lsp --arkts --project-path ./MyApp
devecocli serve lsp --arkts --auto-detect
```
