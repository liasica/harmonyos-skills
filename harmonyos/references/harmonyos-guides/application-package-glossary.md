---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-glossary
title: 应用程序包术语
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用程序包术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:08+08:00
doc_updated_at: 2026-06-16
content_hash: sha256:0a9a05f3f244b94031a9bd9a0746eb1e1d3abca5ed15cca72c68b09d54caa5f7
---

## A

### APP；应用包

当应用发布上架到应用市场时，需要将应用打包为一个.app后缀的文件用于上架，这个.app文件称为App Pack（Application Package），包含应用的所有HAP和HSP文件，以及pack.info描述文件，是发布上架的基本单元。

## B

### Bundle；应用包集合

一个应用中所有HAP与HSP文件的集合，其bundleName是应用的唯一标识。Bundle打包为App Pack后上架应用市场。

### bm (Bundle Manager)；包管理工具

用于应用包管理的命令行工具，支持应用的安装、卸载、查询等操作。

## E

### Entry UIAbility；入口UIAbility

skills标签中entities包含"entity.system.home"且actions包含"ohos.want.action.home"的UIAbility，作为应用的入口组件。

## H

### HAP (Harmony Ability Package)

Harmony Ability Package，是应用安装和运行的基本单元。一个HAP文件包含应用的所有内容，由代码、资源、第三方库及配置文件组成，文件后缀为.hap。分为entry和feature两种类型，支持独立安装和运行。

### HAR (Harmony Archive)；静态共享包

Harmony Archive，静态共享包，用于编译态复用。可以包含代码、C++库、资源和配置文件，文件后缀为 .har，用于实现代码和资源的共享。支持应用内共享，也可发布到OHPM供其他应用使用，但多包引用会造成代码和资源重复拷贝。

### HSP (Harmony Shared Package)；动态共享包

Harmony Shared Package，动态共享包，运行时复用。可以包含代码、C++库、资源和配置文件，文件后缀为.hsp，用于实现代码和资源的共享。多包引用时不会造成重复拷贝，有效控制应用包大小。

## I

### Integrated HSP；集成态HSP

应用内HSP的中间编译产物，用于解决使用方的bundleName与签名之间的强耦合问题。构建发布过程中，不与特定应用包名耦合，工具链支持自动将集成态HSP的包名替换为宿主应用包名。

## M

### Module；模块

应用的一部分，每个模块都有独立的module.json5配置文件。在项目工程中，Entry、Feature、HSP和HAR均为应用模块，支持独立编译和功能实现。

## S

### Static Library；静态共享库

Library类型模块，编译后生成HAR文件，代码和资源跟随使用方编译，编译态复用。

### Shared Library；动态共享库

Library类型模块，编译后生成HSP文件，代码和资源可以独立编译，在应用运行期间可被多个模块复用。
