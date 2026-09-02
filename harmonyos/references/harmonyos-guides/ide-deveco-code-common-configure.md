---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-common-configure
title: 常用配置
breadcrumb: 指南 > AI Coding > DevEco Code > 常用配置
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:30+08:00
doc_updated_at: 2026-07-21
content_hash: sha256:202c05125f3e4d4efb3c434add0eb90d558668f8a0b43d51fdf5e74e9ca3fac0
---

DevEco Code支持在deveco.jsonc文件中配置绿灯模式、Skill、MCP的相关能力。

deveco.jsonc文件在项目和用户目录下各有一份，若不存在需新建该文件，优先级如下：

* Windows：.deveco/deveco.jsonc（项目级） > C:/Users/用户名/.config/deveco/deveco.jsonc（用户级）
* macOS：.deveco/deveco.jsonc（项目级） > ~/.config/deveco/deveco.jsonc（用户级）

**说明** 

新增/修改Skill、MCP配置后，需关闭并重启DevEco Code。

## 配置绿灯模式

启用绿灯模式后，所有工具调用将自动执行，无需逐次确认。默认关闭。

在本地查找和编辑deveco.jsonc文件，若不存在需新建。

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": "allow"
}
```

## 配置MCP

模型上下文协议（Model Context Protocol，简称MCP）可用于连接浏览器、数据库等第三方服务。

在本地查找和编辑deveco.jsonc文件配置MCP，若不存在需新建。

示例：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "playwright": {
      "type": "local",
      "command": ["npx", "@playwright/mcp@latest"],
      "enabled": true
    }
  }
}
```

## 配置Skill

在DevEco Code对话框输入**/skills**可查看所有Skill。DevEco Code已内置部分Skill，如下表，同时也支持自定义创建Skill。

| 内置Skill | 说明 | 适用场景 |
| --- | --- | --- |
| deveco-create-project | 快速创建标准化HarmonyOS模板工程 | 项目初始化 |
| arkts-grammar-standards | ArkTS语法规则、TypeScript迁移差异及ArkUI组件开发最佳实践参考 | ArkTS语法规范、ArkUI界面开发 |
| arkts-error-fixes | 编译与类型错误快速查询 | 快速调试 |
| arkts-runtime-fix | 运行时常见问题修复方案 | 稳定性保障 |

### 创建自定义Skill

**编写frontmatter**

Skill文件命名固定为SKILL.md，每个SKILL.md必须以YAML frontmatter开头。

frontmatter通过如下字段进行识别，超出字段会被忽略。

* name：必填，Skill的唯一标识符。长度不超过64个字符，由小写字母，数字、中划线组成，不能以-开头或结尾，不能包含连续的-，与所在文件夹命名一致。
* description：必填，一句话描述技能的功能或使用场景。长度不超过1024个字符。
* license：可选。
* compatibility：可选。
* metadata：可选，字符串到字符串的映射。

**说明** 

SKILL.md中正文指令长度不超过32768个字符。

**放置文件**

创建一个与name同名的文件夹，将SKILL.md放到指定路径，DevEco Code启动时会自动扫描并解析 。

DevEco Code扫描以下位置的Skill：

* 项目配置：.deveco/skills/<name>/SKILL.md
* 用户配置：C:/Users/用户名/.config/deveco/skills/<name>/SKILL.md
* 项目Agent兼容：.agents/skills/<name>/SKILL.md
* 用户Agent兼容：C:/Users/用户名/.agents/skills/<name>/SKILL.md

**说明** 

* 以上用户级配置以Windows为例，如果是macOS环境，需要把路径中的C:/Users/用户名替换为~。
* SKILL.md所在文件夹大小不超过100MB。

**示例：**

创建.deveco/skills/release/SKILL.md，内容如下。

```md
---
name: release
description: Create consistent releases and changelogs
license: MIT
compatibility: deveco
metadata:
  audience: maintainers
  workflow: github
---

## What I do

- Draft release notes from merged PRs
- Propose a version bump
- Provide a copy-pasteable `gh release create` command

## When to use me

Use this when you are preparing a tagged release.
Ask clarifying questions if the target versioning scheme is unclear.
```

### 配置访问Skill权限

在deveco.jsonc文件中使用权限来控制Agent可以访问哪些Skill。

配置时支持通配符，如internal-\*可匹配internal-docs、internal-tools等。

```json
{
  "permission": {
    "skill": {
      "*": "allow",
      "pr-review": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

| 权限 | 行为 |
| --- | --- |
| allow | Skill立即加载 |
| deny | 对Agent隐藏Skill，拒绝访问 |
| ask | 加载前提示用户确认 |

### 按Agent覆盖权限

在deveco.jsonc文件中为Agent授予与全局默认值不同的权限。

```json
{
  "agent": {
    "plan": {
      "permission": {
        "skill": {
          "internal-*": "allow"
        }
      }
    }
  }
}
```

### 禁用Skill工具

在deveco.jsonc中为Agent添加禁用Skill功能。

```json
{
  "agent": {
    "plan": {
      "tools": {
        "skill": false
      }
    }
  }
}
```

**说明** 

查看Skill时，如果某个Skill没有显示，可以从如下方面排查：

* 确认SKILL.md文件名是否为全大写字母。
* 检查frontmatter是否包含name和description。
* Skill名称在所有路径中是否唯一。
* 检查权限设置是否设置为deny。
