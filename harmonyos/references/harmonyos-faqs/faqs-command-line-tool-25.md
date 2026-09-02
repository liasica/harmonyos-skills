---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-25
title: onClick中使用async方法导致codelinter扫描告警处理
breadcrumb: FAQ > DevEco Studio > 命令行工具 > onClick中使用async方法导致codelinter扫描告警处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e8a78f81398c18c139ef07ad73ebef1749b7e265340603fcecd4d6f022736ef0
---

## 问题现象

在使用codelinter代码规范检测工具时对代码检测时，由于在onClick点击事件中使用了async方法，被codelinter检测出为错误规范的代码行，应该如何修改，被检测出的报错代码块具体如下所示：

```ts
@Entry
@Component
struct IndexFalse {
  build() {
    Column() {
      Text('识别为错误规范的代码行')
        .onClick(async () => { // 这一行被检测出识别为错误规范的代码行
          // ...
        })
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

## 背景知识

codelinter检测工具针对ArkTS/TS代码进行最佳实践/编程规范方面的检查，开发者可根据扫描结果中告警提示手工修复代码缺陷，或者执行一键式自动修复，在代码开发阶段，确保代码质量。其中一条规则"@typescript-eslint/no-misused-promises"，是禁止在不正确的位置使用Promise。

## 解决方案

使用codelinter检测工具对代码扫描完成后，在底部工具面板查看检查结果。选中告警结果时，可以在右侧Defect Description窗口查看告警对应的规则详细说明，其中包含正向和反向示例，并根据其中的建议修改代码。

可以从告警对应的规则详细说明中看到，针对在onClick中使用了async方法检测报错，一般是规则配置文件code-linter.json5中的"rules"配置了规则"@typescript-eslint/no-misused-promises": "error",即禁止在不正确的位置使用Promise，机制如此。

* 方式1：在async方法的外层包裹一层void方法，即与void关键字结合，告诉"@typescript-eslint/no-misused-promises"规则忽略未处理的rejection。
* 方式2：在检测出规范错误的代码行的上一行添加注释//eslint-disable-next-line @typescript-eslint/no-misused-promises即可屏蔽对该代码行的no-misused-promises规则的codelinter检查。

完整示例参考如下：

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('修改方式1')
        .onClick(() => {
          void (async () => {
            // ...
          })();
        });

      Text('修改方式2')
      // eslint-disable-next-line @typescript-eslint/no-misused-promises
        .onClick(async () => {
          // ...
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

方式3：修改code-linter.json5文件中rules中的"@typescript-eslint/no-misused-promises"规则，将该规则中的checksVoidReturn属性设置为false。
